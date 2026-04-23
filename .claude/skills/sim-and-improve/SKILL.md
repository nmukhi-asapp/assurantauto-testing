---
description: Iteratively test GA conversations and improve prompts/code
---

Run iterative test-improve cycles on a GA version. For each cycle, simulate a batch of test conversations using the single-turn simulator, analyze the results, identify issues, apply fixes, and repeat.

## Parameters

The user should provide (ask if not specified):
- **Company**: The company marker to test with (e.g., `american-airlines`)
- **Version**: The GA version to iterate on (e.g., `v5-alpha`, `v4`, `v3`)
- **Conversation scenarios**: A set of test conversations to run. Each scenario is either a single message or a multi-turn sequence. If not provided, ask the user to describe the personas and intents they want tested.
- **Number of cycles**: How many test-improve iterations to run (default: 3)
- **Focus areas** (optional): Specific aspects to evaluate (e.g., "greeting quality", "escalation handling", "tool usage efficiency")

## Workflow

### Phase 1: Setup

1. **Create a test notes file** at `simulator_output/<version>_test_notes.md` to track all results across cycles.
2. **Document the test plan**: Write the conversation scenarios as a numbered list in the notes file.
3. **Read the relevant prompt templates and processor code** for the version being tested, so you understand the system before evaluating outputs. Key locations:
   - Processor: `asapp/generative_agent/processors/` (find the processor(s) used by the version's orchestrator)
   - Prompter templates: look for `.j2` Jinja2 template files within the processor's `prompter/` subdirectory
   - Orchestrator: `asapp/generative_agent/orchestration/orchestrators.py`
   - Version info: `asapp/generative_agent/orchestration/versions.py`

### Phase 2: Run a Cycle (repeat N times)

For each cycle:

#### Step A: Run all test conversations

Use the **single-turn simulator** to run each scenario. Execute conversations in sequence (not parallel — each simulation call takes a few seconds and needs its output analyzed).

```bash
# First turn of a conversation
poetry run python tools/simulator/run.py \
  --company <company> --version <version> \
  --message "<customer_message>" --single-turn

# Subsequent turns (multi-turn scenarios)
poetry run python tools/simulator/run.py \
  --company <company> --version <version> \
  --state <previous_state_file.json> \
  --message "<next_message>" --single-turn
```

For each test, capture:
- The **gate/classifier decisions** (if applicable — check log output)
- The **bot messages** sent to the customer (and whether they are interim/synthetic)
- Any **tool calls** made
- Whether the conversation **escalated** or **finished**
- The **saved state file path** (for multi-turn continuation)

#### Step B: Analyze and document results

For each test conversation, write a short assessment in the notes file:
- What happened (gate decision, ack message, agentic response, tool calls)
- Whether the behavior was **GOOD**, **OK** (acceptable but not ideal), or **ISSUE** (needs fixing)
- For issues: describe what went wrong and categorize it:
  - **[BUG]**: Incorrect behavior (e.g., wrong classification, missing tool call, broken flow)
  - **[PROMPT]**: LLM output quality issue fixable via prompt changes (e.g., too verbose, leaks specifics, duplicates content)
  - **[ARCH]**: Architectural issue requiring code changes (e.g., missing guard condition, wrong processor ordering)

#### Step C: Summarize the cycle

At the end of each cycle, write a cycle summary listing:
- What was **fixed** (from previous cycle's issues)
- What **remains** unfixed
- Whether remaining issues are **actionable** (worth fixing) or **LLM variance** (acceptable noise)

#### Step D: Apply fixes (if issues found)

For each actionable issue, apply the fix:

1. **Prompt fixes**: Edit the relevant `.j2` template files. Common patterns:
   - Add negative examples ("Do NOT say X, Y, Z")
   - Add explicit classification rules ("If the customer says X, always do Y")
   - Strengthen existing instructions with more specific language
   - Adjust tone instructions

2. **Code fixes**: Edit processor or prompter Python code. Common patterns:
   - Add guard conditions
   - Fix classification logic
   - Adjust retry behavior

3. **Do NOT over-engineer**: Only fix clear issues. If something is borderline, note it and move on. Don't make a prompt 2x longer to fix a minor variance issue.

After applying fixes, proceed to the next cycle to verify they worked.

### Phase 3: Final Report

After all cycles are complete, write a final summary in the notes file covering:
- Total number of test invocations across all cycles
- Issues found and fixed (with cycle numbers)
- Remaining LLM-variance items that don't warrant further changes
- Overall readiness assessment

## Evaluation Criteria

When analyzing bot responses, check for:

### Critical (must fix)
- **Wrong action**: Bot fails to escalate when asked, calls wrong tool, gives wrong information
- **Missing action**: Bot should have called a tool but didn't (e.g., escalation request → no escalation)
- **Broken flow**: Conversation gets stuck, loops, or crashes

### Important (should fix)
- **Redundant messages**: Two messages saying essentially the same thing (e.g., ack + agentic both greeting)
- **Leaking specifics before processing**: Quick ack promises specific actions before the system knows what it can do
- **Tone mismatch**: Response doesn't match the customer's tone (too formal for casual, too casual for urgent)

### Minor (note but don't necessarily fix)
- **Mild phrasing variation**: "I'd be happy to help" vs "Let me help you with that" — acceptable LLM variance
- **Slightly different wording across runs**: Same intent expressed differently — normal for LLMs
- **Minor redundancy**: Two messages both asking "how can I help" — not ideal but not harmful

## Important Notes

- **Always use `--single-turn` mode** so you can execute the simulator yourself.
- **One test at a time**: Run each simulation sequentially so you can verify output before proceeding.
- **State files for multi-turn**: The simulator saves state to `simulator_output/`. Use the saved file path for `--state` in follow-up turns.
- **Keep notes organized**: Each cycle should be clearly labeled (## Cycle 1, ## Cycle 2, etc.) with per-test results.
- **Don't change prompts between tests within a cycle**: Run all tests first, then analyze, then fix. This gives you a consistent baseline per cycle.
- **After all cycles, consider running the unit test suite** (`poetry run pytest --no-cov -v`) to make sure code changes didn't break anything.
