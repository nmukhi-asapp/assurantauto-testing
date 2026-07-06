# Phase 1 - Actual Implementation (Rewrite)

**Status:** Simplified to MCP-based skill orchestration

---

## What Phase 1 Actually Is

A skill that orchestrates two MCP tools to analyze whether GenerativeAgent can automate a conversation.

**No Python code needed.**

## The Skill

**Location:** `.claude/skills/analyze-ga-capability/SKILL.md`

The skill:
1. Takes conversation_id, company_marker, branch_name as input
2. Calls `mcp__data-sampling__fetch_conversations_by_id` → gets real conversation
3. Calls `mcp__gacs__get_branch` → gets real GenAgent config
4. Uses Claude's reasoning to analyze:
   - What agent actions were taken
   - What functions are available in GACS
   - What knowledge is in KB articles
   - What gaps exist
5. Returns classification + recommendations

## That's It

Phase 1 is a SKILL.md file that uses MCP tools. No framework needed.

## Usage

```bash
/analyze-ga-capability 3408138022-1698370033-2504114677-1773867395 assurantauto main
```

Returns JSON with analysis and recommendations.

## Why This is Better

- ✅ Uses MCP tools directly (what they're for)
- ✅ Lightweight, maintainable
- ✅ Follows the pattern of existing skills
- ✅ No unnecessary infrastructure
- ✅ Can be extended to Phase 2 (synthesis) when needed

## What Was Wrong With The First Attempt

I wrote a full Python analyzer framework with:
- ConversationAnalyzer class
- Gap dataclass
- Test suite
- etc.

But the skill just needs to **call MCP tools and analyze results**. That's what Claude does best - reasoning over data, not building application frameworks.

## Phase 2 Will Need Code

Phase 2 (synthesis engine) will need Python for:
- Clustering similar findings
- Deduplication (cosine similarity, embeddings)
- ROI scoring

But Phase 1? Just orchestrate the tools.

---

**The lesson:** Skills are lightweight orchestrators, not application frameworks.