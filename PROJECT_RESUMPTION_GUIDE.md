# GenAgent Capability Analysis Skill - Resumption Guide

**Created:** 2026-06-18  
**Status:** Ready for implementation  
**Next Steps:** Build core analysis engine (Phase 1-2)

---

## Quick Context

You're building a skill that analyzes conversations to determine if **GenerativeAgent can automate them**.

**Key Innovation:** When analyzing 100s/1000s of conversations, the skill **synthesizes findings** to avoid overlaps. Instead of 487 raw findings, you get 12 consolidated gaps ranked by ROI (conversations_affected / implementation_hours).

**Example:** 
- Conversation A says "missing payment status knowledge"
- Conversation B says "missing payment timeline"  
- Conversation C says "missing escalation logic"
→ Consolidated into single gap: "Claim Payment Status Communication"

---

## Files Created

All documentation in `/Users/nmukhi/code/assurantauto-testing/`:

1. **ANALYSIS_GenAgent_Capability_Framework.md** (8KB)
   - Complete methodology
   - Parts 1-10 covering:
     - Discoverability framework overview
     - Detailed analysis of one assurantauto conversation
     - 3 key questions answered
     - Skill architecture
     - Implementation guide with Python code templates
   - Ready for use as implementation spec

2. **SYNTHESIS_EXAMPLE.md** (7KB)
   - Concrete example: 200 conversations analyzed
   - Shows: 487 raw findings → 12 consolidated gaps
   - Demonstrates deduplication ratio (97.5%)
   - Shows ROI scoring and prioritization

3. **PROJECT_RESUMPTION_GUIDE.md** (this file)
   - Quick orientation for resuming work

---

## Key Findings from Analysis

### AssurantAuto Conversation (Case Study)

**Conversation ID:** 3408138022-1698370033-2504114677-1773867395

**Analysis Result:** Category 1 - MISSING_KNOWLEDGE (not missing APIs)

| Finding | Details |
|---------|---------|
| **APIs Available** | ✅ All 5 required APIs present in GACS |
| **Knowledge Gap** | ❌ Missing: How to interpret claim status "Payment Approved" → customer message "under review for payment" + timeline expectations |
| **Root Cause** | RepairShopIssues task instructions don't cover payment status communication guidelines |
| **Solution** | Add 50-line section to task instructions covering: (1) status mapping rules, (2) timeline expectations, (3) escalation logic |
| **Impact** | Estimated to affect 120+ conversations in batch analysis |

**Conclusion:** Escalation was due to **knowledge gap**, not missing tools. With proper task instructions, this conversation could be fully automated.

---

## Architecture Overview

### Two Skills to Build

```
┌─────────────────────────────────────────┐
│  analyze-ga-capability (Single Conv)    │
│ ─────────────────────────────────────── │
│ Input: conversation_id, company, branch │
│ Output: {"generative_agent": "yes/no"}  │
│         + missing_actions               │
│         + recommended_improvements      │
└─────────────────────────────────────────┘
                    │
                    ├─→ Used by batch analyzer
                    │
                    └─→ Can be called standalone
                    
┌─────────────────────────────────────────────────────┐
│ batch-analyze-ga-capability (Multiple Convs)        │
│ ───────────────────────────────────────────────────  │
│ Phase A: Analyze conversations (parallelized)      │
│ Phase B: SYNTHESIZE & DEDUPLICATE findings         │
│ Phase C: Rank by ROI and output consolidated list  │
│                                                     │
│ Input: [conv_id1, conv_id2, ...], company, workers │
│ Output: {"synthesized_gaps": [...],                 │
│          "deduplication_ratio": 0.975}              │
└─────────────────────────────────────────────────────┘
```

### Core Components

**ConversationAnalyzer** (analyzer.py)
- Extracts agent actions from conversation
- Checks action feasibility against GACS config
- Classifies as automatable or identifies gaps

**SynthesisEngine** (synthesis_engine.py) ✨ Key Component
- Embeds findings using LLM
- Clusters by semantic similarity (threshold: 0.80)
- Consolidates clusters into unified gaps
- Preserves traceability (which conversations → which gaps)
- Ranks by ROI score

### Data Flow

```
Conversation 
    ↓
Extract Actions (bot messages, API calls)
    ↓
Check Each Action
    ├─ Can we call this API? (query GACS)
    ├─ Is this KB knowledge? (query GACS KB articles)
    └─ Is this common sense? (LLM judgment)
    ↓
Generate Finding (if gap detected)
    ↓
[Repeat for 200 conversations]
    ↓
487 Raw Findings
    ↓
SYNTHESIS ENGINE:
  1. Embed findings
  2. Cluster by similarity
  3. Consolidate per cluster
  4. Score by ROI
    ↓
12 Consolidated Gaps (ranked by priority)
    ↓
Output: Actionable GACS change recommendations
```

---

## Implementation Roadmap

### Phase 1: Core Analysis Engine (1-2 weeks)
- [ ] Implement ConversationAnalyzer class
- [ ] Implement action extraction from conversation
- [ ] Implement feasibility checking (API, KB, common sense)
- [ ] Test on 1 conversation manually

### Phase 2: Synthesis Engine (1 week)
- [ ] Implement SynthesisEngine class
- [ ] Implement embedding function
- [ ] Implement clustering algorithm
- [ ] Implement consolidation logic
- [ ] Implement ROI scoring

### Phase 3: Build Skills (1 week)
- [ ] Create `.claude/skills/analyze-ga-capability/`
- [ ] Create `.claude/skills/batch-analyze-ga-capability/`
- [ ] Write SKILL.md definitions
- [ ] Register with settings.json

### Phase 4: Validation (1-2 weeks)
- [ ] Test on 10 assurantauto conversations
- [ ] Manual review of output
- [ ] Validate synthesis quality
- [ ] Test on 100 conversations

### Phase 5: Scale (1 week)
- [ ] Run on 1000+ conversations
- [ ] Generate company report
- [ ] Create GACS improvement roadmap
- [ ] Integrate with existing skills

---

## Key Technical Decisions Made

| Decision | Rationale |
|----------|-----------|
| Similarity threshold: 0.80 | Balance between over-consolidation and leaving duplicates |
| Synthesis uses LLM embeddings | Captures semantic meaning better than keyword matching |
| Preserve traceability | Allows validation of consolidation quality |
| ROI = convos × priority × feasibility | Prioritizes high-impact, easy improvements |
| Synthesis as separate phase | Can be iterated independently from analysis |
| Task instructions > KB for domain rules | Policies/decisions belong in task logic, not KB |

---

## Integration Points

This skill connects with existing infrastructure:

**MPCs Used:**
- `mcp__data-sampling__fetch_conversations_by_id` — Fetch conversations
- `mcp__gacs__get_branch` — Get task configs
- `mcp__gacs__get_branch_function` — Get function definitions

**Skills to Integrate With:**
- `fetch-conversation` — For step-by-step analysis
- `gacs` — For retrieving task information
- `run-scenarios` — For testing improvements after implementing them
- `sim-and-improve` — For iterative GenAgent enhancement

---

## Questions Still To Answer

When resuming, need to make decisions on:

1. **Similarity Threshold**: Is 0.80 right? Adjust per domain?
2. **Knowledge Type**: KB article vs task instruction?
3. **Escalation Categories**: How to distinguish expected escalations from fixable issues?
4. **Confidence Scoring**: Heuristics for 0.0-1.0 confidence?
5. **Consolidation Validation**: Test protocol for verifying merged findings are truly related?

---

## Running the Analysis (When Ready)

Once skills are built:

```bash
# Analyze single conversation
/analyze-ga-capability 3408138022-1698370033-2504114677-1773867395 assurantauto main

# Analyze batch of conversations
/batch-analyze-ga-capability \
  --conversation_ids conv1 conv2 conv3 ... conv200 \
  --company assurantauto \
  --batch_size 100 \
  --workers 5
  
# Output: Synthesized gaps with ROI scores
```

---

## References

**External Projects:**
- Discoverability Project: `github.asapp.dev/lsedeno/Discoverability_project`
  - Existing "GA Replace Agent" pipeline
  - Can learn from their approach and integrate ideas

**Documentation Created:**
- Part 9 of ANALYSIS_GenAgent_Capability_Framework.md has full Python code templates for implementation

---

## Memory Notes

Full context saved to:
`/Users/nmukhi/.claude/projects/-Users-nmukhi-code-assurantauto-testing/memory/ga_capability_analysis_skill.md`

When resuming, this file will be automatically loaded to restore full context.

---

## Next Steps When Resuming

1. Read ANALYSIS_GenAgent_Capability_Framework.md Part 9 (implementation guide)
2. Set up file structure for `.claude/skills/analyze-ga-capability/`
3. Implement ConversationAnalyzer class (Part 9 has template)
4. Implement SynthesisEngine class (Part 9 has template)
5. Test on single assurantauto conversation
6. Build skills and SKILL.md files
7. Validate on 100 conversations

---

**Good luck! This is a high-impact project that will significantly improve GenAgent capability analysis across the company.**