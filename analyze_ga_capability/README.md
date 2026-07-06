# GenAgent Capability Analyzer - Phase 1 Implementation

**Status:** Phase 1 - Core Analysis Engine (In Development)

This directory contains the Python implementation of the GenAgent Capability Analysis skill's core engine.

## Overview

The analyzer determines whether GenerativeAgent can automate a conversation by examining:
1. **What the agent did** - Extracting all actions (API calls, information provided)
2. **What's available** - Querying GACS for available functions and KB articles  
3. **What's missing** - Identifying gaps in tools or knowledge
4. **Classification** - Determining if the conversation is automatable

## Project Structure

```
analyze_ga_capability/
├── analyzer.py              # Core ConversationAnalyzer class
├── test_analyzer.py         # Unit tests
├── __init__.py             # Package initialization
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Key Classes

### ConversationAnalyzer
Main class that orchestrates the analysis workflow.

**Constructor:**
```python
analyzer = ConversationAnalyzer(
    conversation_id="3408138022-1698370033-2504114677-1773867395",
    company_marker="assurantauto",
    branch_name="main"
)
```

**Main Method:**
```python
result = await analyzer.analyze()  # Returns AnalysisResult
```

**Process:**
1. `_fetch_conversation()` - Fetch from data-sampling MCP
2. `_fetch_gacs_config()` - Fetch from GACS MCP
3. `_extract_agent_actions()` - Parse conversation for actions
4. `_check_action_feasibility()` - Validate each action
5. `_classify_conversation()` - Generate result and recommendations

### Gap
Represents a capability gap (missing tool or knowledge).

**Fields:**
- `action` - What the agent tried to do
- `gap_type` - 'missing_knowledge' | 'missing_api' | 'missing_tool'
- `reason` - Why the gap exists
- `specific_knowledge` - What knowledge is missing (for KB gaps)
- `affected_task` - Which task is affected
- `confidence` - Confidence in this gap assessment (0.0-1.0)

### AnalysisResult
Result of analyzing a single conversation.

**Fields:**
- `conversation_id` - Conversation ID analyzed
- `generative_agent` - 'yes' (automatable) or 'no'
- `category` - Why: 'AUTOMATABLE' | 'MISSING_KNOWLEDGE' | 'MISSING_APIS' | 'APPROPRIATE_ESCALATION'
- `missing_actions` - List of Gap objects
- `recommended_improvements` - List of RecommendedImprovement objects
- `confidence` - Overall confidence (0.0-1.0)

**Method:**
```python
result_dict = result.to_dict()  # Convert to JSON-serializable dict
```

## Current Implementation Status

### ✅ Implemented

- [x] Gap and AnalysisResult data classes
- [x] ConversationAnalyzer initialization
- [x] Placeholder MCP fetch methods (structure ready)
- [x] Action extraction from conversation JSON
  - [x] Bot message extraction
  - [x] Function call extraction
  - [x] Task context tracking
- [x] Function availability checking
- [x] Classification logic (no gaps → automatable, gaps → categorization)
- [x] Recommendation generation stub
- [x] Unit tests (all passing)
- [x] JSON serialization

### ⚠️ TODO - Next Steps (Phase 1 Completion)

- [ ] Implement MCP (Model Context Protocol) integration
  - [ ] Connect to `mcp__data-sampling__fetch_conversations_by_id` MCP tool
  - [ ] Connect to `mcp__gacs__get_branch` MCP tool
- [ ] Implement LLM-based message feasibility checking
  - [ ] Parse messages for domain concepts
  - [ ] Check against KB articles
  - [ ] Use Claude to assess if content requires unavailable knowledge
- [ ] Implement recommendation generation
  - [ ] Generate specific GACS location for improvement
  - [ ] Estimate implementation hours
  - [ ] Assign priority based on impact
- [ ] Integration tests with real conversation data
- [ ] Performance optimization
- [ ] Logging and monitoring improvements

## Testing

### Run Unit Tests

```bash
cd /Users/nmukhi/code/assurantauto-testing/analyze_ga_capability
pytest test_analyzer.py -v
```

### Test Coverage

- Gap data structure: ✅
- AnalysisResult serialization: ✅
- ConversationAnalyzer initialization: ✅
- Message extraction: ✅
- Function call extraction: ✅
- Function availability checking: ✅
- Classification logic: ✅
- Integration tests: ⏭️ (skipped until MCP available)

## Usage Example

### Current (Placeholder)

```python
import asyncio
from analyzer import ConversationAnalyzer

async def main():
    analyzer = ConversationAnalyzer(
        conversation_id="3408138022-1698370033-2504114677-1773867395",
        company_marker="assurantauto",
        branch_name="main"
    )
    
    result = await analyzer.analyze()
    print(f"Automatable: {result.generative_agent}")
    print(f"Category: {result.category}")

asyncio.run(main())
```

### Future (With MCP Integration)

Once MCP integration is complete, the same code will:
1. Fetch real conversations from Athena
2. Fetch real GACS configurations
3. Analyze actual GenAgent capabilities
4. Generate actionable recommendations

## Dependencies

```
python >= 3.10
pytest >= 7.0
pytest-asyncio >= 0.20.0
```

See `requirements.txt` for full list.

## Integration with Skill

This code is called by the `/analyze-ga-capability` skill defined in:
`.claude/skills/analyze-ga-capability/SKILL.md`

The skill:
1. Receives conversation_id, company_marker, branch_name from user
2. Creates ConversationAnalyzer instance
3. Calls analyze()
4. Returns formatted JSON result to user

## Phase 2: Synthesis Engine

Once Phase 1 is complete, we'll build the synthesis engine in:
`analyze_ga_capability/synthesis_engine.py`

The synthesis engine will:
- Cluster similar findings from multiple conversations
- Deduplicate overlapping gaps
- Consolidate into unified recommendations
- Rank by ROI (conversations_affected / implementation_hours)

## Questions / TODOs

### Architecture Decisions

- [x] Use async/await for MCP calls
- [x] Dataclasses for structured data
- [x] Separate class for each major component
- [ ] Error handling strategy
- [ ] Logging levels and format
- [ ] Caching strategy for GACS configs

### Implementation Details

- [ ] How to map AI message content to KB articles?
- [ ] Confidence score heuristics?
- [ ] How to handle conversations with no clear outcome?
- [ ] How to categorize escalations (expected vs fixable)?

## References

- `ANALYSIS_GenAgent_Capability_Framework.md` - Full methodology
- `SYNTHESIS_EXAMPLE.md` - Example output from batch analysis
- `PROJECT_RESUMPTION_GUIDE.md` - Quick start guide

## Author Notes

Phase 1 establishes the foundation for single-conversation analysis. The architecture is designed to be extended in Phase 2 with:
- Parallel batch processing
- Semantic clustering of findings
- Synthesis engine for deduplication

The placeholder MCP calls are ready to be connected to actual services once MCP infrastructure is available.