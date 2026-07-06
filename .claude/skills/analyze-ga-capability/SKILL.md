---
description: Analyze a conversation to determine if GenerativeAgent can automate it
---

# Analyze GenAgent Capability

Analyzes a single conversation to determine if GenerativeAgent has the necessary tools and knowledge to automate it.

## Usage Examples

```bash
# Analyze against prod deployment (default)
/analyze-ga-capability 3408138022-1698370033-2504114677-1773867395 assurantauto main

# Analyze against sandbox deployment
/analyze-ga-capability 3408138022-1698370033-2504114677-1773867395 assurantauto main sandbox

# Analyze specific branch
/analyze-ga-capability 3408138022-1698370033-2504114677-1773867395 assurantauto feature-branch prod
```

## EXECUTE THIS SKILL BY FOLLOWING THESE STEPS

### Step 1: Parse Input Arguments
Extract from the user input:
- `conversation_id` - Required. The conversation ID to analyze
- `company_marker` - Required. The company (e.g., "assurantauto")
- `branch_name` - Optional, default "main". The GACS branch to check
- `environment` - Optional, default "prod". The GACS environment: "prod" (deployed to production) or "sandbox" (deployed to sandbox)

### Step 2: Fetch Conversation Data
Call: `mcp__data-sampling__fetch_conversations_by_id`
```
{
  "company_marker": <company_marker>,
  "conversation_ids": [<conversation_id>],
  "save_conversations": true,
  "is_voice": true,
  "include_human_agent_utterances": true
}
```
This returns the complete conversation history including:
- All GenAgent actions, messages, and function calls
- Human agent utterances (if conversation was escalated)
- All customer utterances throughout

### Step 3: Fetch GenAgent Configuration from Deployment
Call: `mcp__gacs__get_deployments` to find the deployment for this branch/environment:
```
{
  "company_marker": <company_marker>,
  "environment": <environment>,
  "n": 10,
  "save_output": false
}
```

Then identify the deployment that corresponds to <branch_name> (typically deployment name includes branch name).

Call: `mcp__gacs__get_deployment_info` with the matching deployment_id:
```
{
  "deployment_id": <deployment_id>,
  "save_output": false
}
```

This returns available tasks, functions, and KB articles for the deployed configuration in the specified environment (prod or sandbox).

**Note:** This fetches the deployed version of the branch, not the draft version. If you need the draft (undeployed) version, use `mcp__gacs__get_branch` instead.

### Step 4: Analyze the Conversation

For each message and action in the conversation:

**A. Extract Agent Actions**
- Identify what the agent said to the customer
- Identify what functions the agent called
- Identify what information the agent provided
- Note which tasks were active during each action

**B. Check Function Availability**
For each function called:
- Look up the function in GACS config's function list
- If NOT found → Create a gap with `gap_type: "missing_api"`
- If found → Check the function's **actual capabilities** — NOT just whether it exists
  - Some functions have fixed/constrained behavior (e.g., send_sms_repair_facility only sends portal reminders, not custom messages)
  - Just because a function exists doesn't mean it can accomplish what the agent needs
  - If function exists but is too constrained for the use case → Document as capability gap

**C. Check Knowledge Availability**
For each piece of information provided by the agent:
- Does it come from a KB article in the GACS config?
- Is it common sense conversational knowledge?
- Is it domain-specific knowledge NOT in any KB article?
- If domain-specific and NOT in KB → Create a gap with `gap_type: "missing_knowledge"`

**D. Identify Special Cases**
- If agent escalated to a human → Check if this was necessary given available tools
- If multiple gaps → Are they fixable with GACS changes or inherently require human judgment?

**E. Analyze Human Agent Phase (if escalation occurred)**
- What did the human agent do differently than GenAgent?
- What information did they gather that GenAgent didn't?
- What functions/capabilities did they use that GenAgent didn't attempt?
- What was the final outcome/resolution provided to the customer?
- Identify specific gaps: What GenAgent could have done with additional knowledge/APIs?
- Example: If human agent sent documentation that GenAgent cannot send → document as `missing_api` gap

### Step 5: Classify the Conversation

Based on gaps found:

**If NO gaps:**
```json
{
  "generative_agent": "yes",
  "category": "AUTOMATABLE"
}
```

**If gaps exist:**
Determine category based on gap types:
- Only `missing_knowledge` gaps → `category: "MISSING_KNOWLEDGE"`
- Only `missing_api` gaps → `category: "MISSING_APIS"`
- Escalation was appropriate given available resources → `category: "APPROPRIATE_ESCALATION"`

```json
{
  "generative_agent": "no",
  "category": "<one of above>"
}
```

### Step 6: Generate Recommendations

For each gap, create a recommendation with the specific GACS change needed:

**For `missing_api` gaps:**
```json
{
  "type": "api_enhancement",
  "location": "functions/<function_name>",
  "priority": "HIGH",
  "description": "Add or enhance API: <specific_knowledge>"
}
```

**For `missing_knowledge` gaps:**
```json
{
  "type": "task_instruction_update",
  "location": "tasks/<task_name>/promptInstructions",
  "priority": "HIGH",
  "description": "Add knowledge about: <specific_knowledge>"
}
```

**NOTE: Do NOT estimate impact across other conversations.** Impact metrics (how many other conversations would be unblocked) require batch analysis across many conversations. This is Phase 2 work. Phase 1 only analyzes the single conversation provided.

### Step 7: Return Result JSON

Return a JSON object with this exact structure:

```json
{
  "conversation_id": "<conversation_id>",
  "company_marker": "<company_marker>",
  "branch": "<branch_name>",
  "environment": "<prod|sandbox>",
  "deployment_id": "<deployment_id>",
  "generative_agent": "yes|no",
  "category": "AUTOMATABLE|MISSING_KNOWLEDGE|MISSING_APIS|APPROPRIATE_ESCALATION",
  "missing_actions": [
    {
      "action": "What the agent tried to do",
      "gap_type": "missing_knowledge|missing_api",
      "reason": "Why GenAgent can't do it",
      "specific_knowledge": "What knowledge is missing (for knowledge gaps)"
    }
  ],
  "available_resources": {
    "functions_available": ["function1", "function2", ...],
    "kb_articles_available": ["article1", "article2", ...]
  },
  "recommended_improvements": [
    {
      "type": "task_instruction_update|kb_article|api_enhancement",
      "location": "GACS path where improvement should go",
      "priority": "HIGH|MEDIUM|LOW",
      "description": "What needs to be added/fixed"
    }
  ],
  "human_agent_analysis": {
    "escalation_occurred": true,
    "human_agent_actions": [
      {
        "action": "What the human agent did",
        "genagent_capability": "Could GenAgent do this? (yes/no/partially)",
        "gap_identified": "If no/partially: What's missing?"
      }
    ],
    "gaps_found_in_human_phase": [
      {
        "action": "What human agent accomplished that GenAgent couldn't",
        "gap_type": "missing_knowledge|missing_api|process_gap",
        "severity": "HIGH|MEDIUM|LOW",
        "description": "Specific capability needed"
      }
    ],
    "outcome": "What was the final resolution provided to customer?"
  },
  "scope": "single_conversation_analysis",
  "confidence": 0.92,
  "analysis_timestamp": "<ISO 8601 timestamp>"
}
```

## Key Analysis Principles

1. **Use ACTUAL data** - Only report gaps if GenAgent genuinely lacks tools/knowledge to do what the agent did
2. **Be specific** - Recommend exact GACS changes, not generic suggestions
3. **Distinguish gaps** - Missing tools (APIs) vs. missing knowledge (KB articles) are different
4. **Consider context** - An escalation might be appropriate even if all tools are available
5. **Single conversation scope** - Analyze only this conversation. Do NOT estimate impact across other conversations (that requires Phase 2 batch analysis)
6. **Environment matters** - By default, fetch the prod deployment of the branch. Use `environment=sandbox` to analyze against sandbox deployment instead
7. **Check function capabilities** - A function existing in GACS does NOT mean it can accomplish the use case. Verify actual function behavior (message templates, parameters, constraints) before concluding a capability is available. For example: `send_sms_repair_facility` only sends fixed portal reminders, not custom authorization messages.

8. **CallerIdentification task architecture** - In assurantauto, CallerIdentification is always the *first* task in a conversation. Its job is to identify the caller type (repair facility, contract holder, or dealer). After identification, the conversation continues in a specialized downstream task:
   - Repair facility → `RepairShopIssues`
   - Contract holder → `ContractHolderIssues`
   - Dealer → `DealershipIssues`
   
   The full conversation (including all tasks and transitions) is captured in the fetched conversation data. Look for `ACTION_TYPE_ENTER_TASK` events to see when task switches happen. **Do NOT classify a conversation as a "routing stub process gap" just because CallerIdentification ends with a task switch—that is expected behavior.** Instead, **evaluate the complete conversation across all tasks entered**, not just the CallerIdentification phase. When filtering by `first_task_name=CallerIdentification`, the filter means "conversations that started in CallerIdentification," not "conversations that stayed in CallerIdentification." Gaps observed during CallerIdentification (e.g., a repair facility needing to file a claim) may be fully resolved in the downstream task (RepairShopIssues).

## Expected Outcome

A JSON object that clearly states:
- Whether GenAgent can automate this conversation (yes/no)
- Why or why not (category: AUTOMATABLE, MISSING_KNOWLEDGE, MISSING_APIS, or APPROPRIATE_ESCALATION)
- Specific GACS changes needed to enable automation
- Confidence in the assessment

**Note:** This skill analyzes a single conversation in isolation. To understand how many other conversations might be affected by the same gap, use Phase 2 (batch analysis with synthesis) to cluster findings across hundreds of conversations.