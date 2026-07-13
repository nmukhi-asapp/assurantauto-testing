# Batch GenAgent Capability Analysis

Analyze a batch of conversations to identify GenAgent automation capability gaps at scale. Synthesizes findings across hundreds of conversations, deduplicates similar gaps, and ranks them by impact (estimated number of conversations that could be unblocked by each improvement).

## ADR Reference

When analyzing capability gaps at scale, consult:

- **ADR 0006: Voice Configuration Design Decisions** — Architectural patterns help identify categories of gaps:
  - **DD-03**: Voice Settings vs. Procedures boundary — missing FAQs (Talker) vs. missing business logic (Reasoner)
  - **DD-06**: API sequencing issues — workflows that violate proper sequencing patterns
  - **DD-08**: Escalation gaps — conditions not captured in Procedures
  - **DD-10/DD-11**: Function design gaps — missing functions or incorrect API access patterns

**When categorizing gaps:**
1. **Talker gaps** (Voice Settings): FAQs, time-buying phrases, verification instructions
2. **Reasoner gaps** (Procedures): Business logic, escalation conditions, error handling
3. **Function gaps**: Missing functions, incorrect signatures, improper parameter mapping
4. **Architectural violations**: Talker/Reasoner boundary crossed, improper sequencing (DD-06)

**Prioritization:** Rank gaps by:
- **Impact**: How many conversations would be unblocked?
- **Category**: Systemic (affects many) vs. one-off?
- **Severity**: Does it violate architectural constraints (DD-03, DD-06, DD-08)?

**Location:** `../generative-agent/asapp/generative_agent/tools/workbench/docs/adrs/0006-voice-configuration-design-decisions.md`

---

## When to use

When you have:
- A directory of locally downloaded conversation JSON files (e.g., escalated conversations from a date range)
- Want to understand **why** these conversations escalated or went to human agents
- Need to prioritize GACS improvements by impact (how many conversations each would unblock)
- Want to avoid duplicating effort (dedup similar gaps across conversations)

This is **Phase 2 analysis**: batch synthesis and impact metrics. Use after Phase 1 (single conversation analysis with `/analyze-ga-capability`) to understand patterns across hundreds of conversations.

## Arguments

- **directory** (required): path to folder containing `platform::COMPANY::CONV_ID::.json` files
- **sample** (optional): max number of conversations to analyze (default: all; use 50–100 for exploration)
- **company_marker** (optional): company identifier for GACS queries (inferred from JSON filenames if not provided)
- **branch** (optional): GACS branch to check (default: "main")
- **environment** (optional): "prod" or "sandbox" (default: "prod")

## Procedure

### Step 1 — Parse Conversation Flows

For each conversation JSON file, extract:

```python
import json
from pathlib import Path
from collections import defaultdict

def parse_conversation_flow(json_file):
    """Extract task flow, function calls, and escalation point."""
    with open(json_file) as f:
        data = json.load(f)
    
    actions = data.get('model_input', {}).get('actions', [])
    conv_id = data.get('model_input', {}).get('external_conversation_id', 'unknown')
    
    flow = {
        'conv_id': conv_id,
        'json_path': str(json_file),
        'task_path': [],           # [task1, task2, ...] in order entered
        'functions_called': [],    # List of function names
        'escalation_function': None,  # Which escalate_* was called
        'escalation_index': None,   # Action index where escalation occurred
        'messages': [],            # [{speaker, text, index}]
        'customer_requests': [],   # Extracted customer needs/questions
        'handoff_to_task': None,   # If escalated, what task was active
        'errors_seen': [],         # Function responses with errors/failures
        'has_human_agent_response': False,
    }
    
    # First pass: extract structure
    for i, action in enumerate(actions):
        atype = action.get('type')
        
        if atype == 'enter_task':
            task = action.get('task_name')
            if task and task not in flow['task_path']:
                flow['task_path'].append(task)
        
        elif atype == 'function_request':
            func = action.get('function_request', {}).get('function_name')
            if func:
                flow['functions_called'].append(func)
                if 'escalate' in func.lower():
                    flow['escalation_function'] = func
                    flow['escalation_index'] = i
                    flow['handoff_to_task'] = flow['task_path'][-1] if flow['task_path'] else None
        
        elif atype == 'function_response':
            resp = action.get('function_response', {})
            if resp.get('error') or resp.get('status') == 'error':
                flow['errors_seen'].append({
                    'function': flow['functions_called'][-1] if flow['functions_called'] else '?',
                    'error': str(resp.get('error', resp.get('message', 'unknown')))[:100]
                })
        
        elif atype == 'message':
            msg = action.get('message', {})
            sender = msg.get('sender', '')
            text = msg.get('content') or msg.get('text') or ''
            if text.strip():
                flow['messages'].append({
                    'speaker': sender,
                    'text': text[:200],  # Truncate long messages
                    'index': i
                })
                if sender == 'human_agent':
                    flow['has_human_agent_response'] = True
    
    return flow
```

Apply this to all conversation files in the directory. Store results in a list.

### Step 2 — Infer Customer Needs

For each conversation, identify what the customer was trying to accomplish. Use heuristics + LLM if needed:

```python
def infer_customer_needs(flow):
    """
    Infer what the customer needed based on:
    - Task path (CallerIdentification → ContractHolderIssues suggests claim info lookup)
    - Customer messages (parse for keywords: claim, renew, coverage, etc.)
    - Escalation function called (escalate_to_agent_from_ivr suggests GenAgent couldn't help)
    - Function calls that failed (if lookup_claim failed, customer was seeking claim info)
    """
    needs = []
    
    # Map task path to common needs
    task_patterns = {
        'ContractHolderIssues': ['claim_info', 'policy_info', 'billing'],
        'RepairShopIssues': ['authorization', 'claim_status', 'settlement'],
        'DealershipIssues': ['recall_info', 'warranty', 'coverage'],
        'CarRentalInquiry': ['rental_authorization', 'rental_details'],
    }
    
    for task in flow['task_path']:
        if task in task_patterns:
            needs.extend(task_patterns[task])
    
    # Parse customer messages for keywords
    keywords = {
        'claim': 'claim_info',
        'coverage': 'coverage_info',
        'renew': 'renewal_info',
        'payment': 'billing_info',
        'authorization': 'repair_authorization',
        'rental': 'rental_authorization',
    }
    
    for msg in flow['messages']:
        if msg['speaker'] == 'customer':
            text_lower = msg['text'].lower()
            for keyword, need in keywords.items():
                if keyword in text_lower and need not in needs:
                    needs.append(need)
    
    return list(set(needs))  # Deduplicate
```

### Step 3 — Identify Capability Gaps

For each conversation, determine why it escalated:

```python
def identify_gaps(flow, customer_needs):
    """
    Classify gaps: missing_api, missing_knowledge, process_gap, or appropriate_escalation
    """
    gaps = []
    
    if not flow['escalation_function']:
        return gaps  # Conversation didn't escalate
    
    # Gap 1: Missing functions
    # Check if GenAgent tried and failed to call a function
    for error in flow['errors_seen']:
        gaps.append({
            'type': 'missing_capability',
            'category': 'function_failure',
            'function': error['function'],
            'error': error['error'],
            'severity': 'HIGH'
        })
    
    # Gap 2: Missing knowledge
    # If customer asked about something GenAgent didn't address
    addressed_needs = set()
    for func in flow['functions_called']:
        if 'get_' in func or 'lookup' in func or 'retrieve' in func:
            # This function retrieves information
            if 'claim' in func.lower():
                addressed_needs.add('claim_info')
            if 'contract' in func.lower():
                addressed_needs.add('policy_info')
    
    for need in customer_needs:
        if need not in addressed_needs:
            gaps.append({
                'type': 'missing_capability',
                'category': 'missing_knowledge',
                'knowledge_needed': need,
                'severity': 'MEDIUM'
            })
    
    # Gap 3: Missing escalation handling
    # If escalated without trying resolution first
    if len(flow['functions_called']) < 3:  # Heuristic: very few attempts
        gaps.append({
            'type': 'process_gap',
            'description': 'Escalated with minimal resolution attempt',
            'severity': 'LOW'
        })
    
    return gaps
```

### Step 4 — Deduplicate and Synthesize

Group similar gaps across all conversations:

```python
def synthesize_gaps(all_conversations):
    """
    Deduplicate gaps and count impact.
    
    Returns:
    {
        'gap_id': {
            'type': 'missing_api' | 'missing_knowledge' | 'process_gap',
            'description': 'What is missing',
            'impact': {
                'conversations_affected': 42,
                'percentage': 7.8,
                'examples': [conv_id1, conv_id2, ...]
            },
            'recommendation': 'Exact GACS change needed',
            'severity': 'HIGH' | 'MEDIUM' | 'LOW',
            'related_gaps': ['gap_id2', ...],  # Similar gaps grouped together
        }
    }
    """
    
    gap_clusters = {}
    gap_to_convs = defaultdict(list)
    
    for conv in all_conversations:
        for gap in conv['gaps']:
            # Create a gap signature (dedup key)
            if gap['category'] == 'function_failure':
                sig = f"function_failure:{gap['function']}"
            elif gap['category'] == 'missing_knowledge':
                sig = f"missing_knowledge:{gap['knowledge_needed']}"
            else:
                sig = f"process_gap:{gap['description'][:50]}"
            
            gap_to_convs[sig].append(conv['conv_id'])
    
    # Convert to output format
    results = {}
    for i, (sig, conv_ids) in enumerate(gap_to_convs.items()):
        gap_id = f"gap_{i+1:03d}"
        results[gap_id] = {
            'signature': sig,
            'impact': {
                'conversations_affected': len(conv_ids),
                'percentage': (len(conv_ids) / len(all_conversations)) * 100,
                'examples': conv_ids[:5]  # First 5 examples
            }
        }
    
    return results
```

### Step 5 — Rank by Impact

Sort gaps by impact (conversations affected) and generate recommendations:

```python
def generate_recommendations(gap_clusters, total_conversations):
    """
    For each gap, generate a specific GACS recommendation.
    """
    recommendations = []
    
    for gap_id, gap in sorted(
        gap_clusters.items(),
        key=lambda x: -x[1]['impact']['conversations_affected']
    ):
        if 'function_failure' in gap['signature']:
            func = gap['signature'].split(':')[1]
            recommendation = {
                'priority': 'HIGH' if gap['impact']['percentage'] > 5 else 'MEDIUM',
                'type': 'api_enhancement',
                'function': func,
                'description': f"Enhance or fix `{func}` (currently failing in {gap['impact']['conversations_affected']} conversations)",
                'location': f"functions/{func}",
                'estimated_unblock': gap['impact']['conversations_affected']
            }
        elif 'missing_knowledge' in gap['signature']:
            knowledge = gap['signature'].split(':')[1]
            recommendation = {
                'priority': 'MEDIUM',
                'type': 'knowledge_base',
                'knowledge': knowledge,
                'description': f"Add KB articles or task instructions about: {knowledge}",
                'location': f"tasks/*/promptInstructions",
                'estimated_unblock': gap['impact']['conversations_affected']
            }
        else:
            recommendation = {
                'priority': 'LOW',
                'type': 'process',
                'description': gap['signature'],
                'estimated_unblock': gap['impact']['conversations_affected']
            }
        
        recommendations.append(recommendation)
    
    return recommendations
```

### Step 6 — Generate Report

Create a Markdown report with:

#### Section 1: Executive Summary
- Total conversations analyzed
- Escalation rate (conversations that escalated / total)
- Top 3 capability gaps by impact
- Estimated conversations that could be unblocked by addressing top gaps

#### Section 2: Capability Gap Ranking

Table sorted by impact (conversations affected):

```
| Rank | Gap | Type | Affected | % | Recommendation |
|------|-----|------|----------|---|-----------------|
| 1 | gap_001 | missing_api | 87 | 16.0% | Enhance `get_claims_status` to support claim lookups |
| 2 | gap_002 | missing_knowledge | 54 | 9.9% | Add KB articles on coverage scenarios |
| ... |
```

#### Section 3: Gap Details

For top 10 gaps:
- Impact: N conversations, X% of total
- Examples: [conv_id, conv_id, ...]
- Description: What is missing
- Recommendation: Exact GACS change
- Severity: HIGH/MEDIUM/LOW

#### Section 4: Task-Based Breakdown

Show which task paths escalate most and their primary gaps:

```
| Task Path | Count | Primary Gap | Unblock Potential |
|-----------|-------|-------------|-------------------|
| CallerIdentification → ContractHolderIssues | 104 | missing_knowledge (claim_info) | 87 convs |
| CarRentalInquiry | 255 | missing_api (send_email) | 64 convs |
| ... |
```

#### Section 5: Sample Conversations

Show 3–5 representative conversations with their gaps:
- Conversation ID
- Task path
- What customer needed
- Gaps identified
- How it escalated

### Step 7 — Save Output

Save as `{directory}_capability_analysis_{YYYY-MM-DD}.md` in parent directory of input folder.

Also save a JSON file with full gap data for programmatic access:
```json
{
  "metadata": {
    "date": "2026-07-07",
    "directory": "escalated_convs_with_ha",
    "conversations_analyzed": 542,
    "escalation_rate": 0.95
  },
  "gaps": [
    {
      "gap_id": "gap_001",
      "type": "missing_api",
      "function": "get_claims_status",
      "impact": 87,
      "percentage": 16.0,
      "severity": "HIGH",
      "recommendation": "Enhance function to...",
      "examples": [...]
    }
  ],
  "recommendations": [
    {
      "priority": "HIGH",
      "type": "api_enhancement",
      "change": "...",
      "estimated_unblock": 87
    }
  ]
}
```

## Notes

- **Deduplication is critical**: "send_sms to contract holder" appearing in 50 conversations = 1 gap with impact 50, not 50 separate gaps
- **Severity tiers**:
  - HIGH: affects > 5% of conversations
  - MEDIUM: affects 1–5%
  - LOW: affects < 1%
- **Estimated unblock** is conservative: actual impact may vary depending on whether a single fix resolves multiple failure modes
- Don't over-infer: if data is ambiguous about why escalation occurred, mark as "unclear" rather than guess
- If conversations lack customer messages (corrupted/redacted), skip those and note in report
- Phase 2 analysis: this skill focuses on **patterns and impact metrics**. For detailed capability mapping of a specific conversation, use Phase 1 (`/analyze-ga-capability`)

## Expected Output

**Report**: `escalated_convs_with_ha_capability_analysis_2026-07-07.md` (markdown with tables and narrative)

**Data**: `escalated_convs_with_ha_capability_analysis_2026-07-07.json` (structured gap records for further processing)

**Terminal output**: Summary statistics (total conversations, escalation rate, top 3 gaps by impact)