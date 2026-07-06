---
description: Fetch a production conversation, summarize what happened, and answer questions about agent behavior.
arguments:
  - name: args
    description: "Optional: <conversation-id> <company-marker> [--env prod|sandbox] [--type voice|chat] — if omitted, the skill will ask"
---

# Inspect Conversation

Interactively fetch a conversation, summarize it, and answer questions about agent behavior.

## Step 1: Gather Parameters

If `$ARGUMENTS` is empty or incomplete, ask the user for the missing values one at a time:

1. **Conversation ID** (required) — e.g. `2209534218-1045828081-2391966186-2917985560`
2. **Company marker** (required) — e.g. `assurantauto`
3. **Environment** (optional, default: `prod`) — `prod` or `sandbox`
4. **Conversation type** (optional, default: `voice`) — `voice` or `chat`

Do not proceed until you have at least the conversation ID and company marker.

## Step 2: Fetch the Conversation

### Voice conversations

Voice conversations have two parts: a base conversation and an `_int` (internal/reasoner) conversation. Both must be fetched and merged.

**Try this first** — use the `mcp__data-sampling__fetch_conversations_by_id` MCP tool:

```
mcp__data-sampling__fetch_conversations_by_id(
  company_marker="<company-marker>",
  conversation_ids=["<conversation-id>"],
  save_conversations=True,
  is_voice=True,
  include_human_agent_utterances=True,
  output_dir="<absolute-path-to-this-repo>/fetched_conversations"
)
```

The merged file is saved to:
`fetched_conversations/platform::<company-marker>::<conversation-id>::<customer-id>.json`

**If the MCP tool is unavailable or fails**, fall back to `scripts/fetch_conversation.py`:

```bash
# Edit scripts/fetch_conversation.py to set:
#   company_marker = "<company-marker>"
#   conversation_id = "<conversation-id>"
# Then (from repo root):
uv run python scripts/fetch_conversation.py
```

If the script also fails, present the command to the user and ask them to run it, then wait for them to confirm it completed and tell you the output file path.

### Chat conversations

```bash
_GA=${GENERATIVE_AGENT_DIR:-$HOME/code/generative-agent}
cd "$_GA" && poetry run python tools/fetch_convo_from_athena/fetch_convo_from_athena.py \
  --company-marker <company-marker> \
  --conversation-id <conversation-id> \
  --profile-team mleng
```

Output: `tools_output/athena_actions/<company-marker>_<conversation-id>_actions.json`

## Step 3: Parse the Conversation

Read the fetched JSON file. The conversation is in `model_input.actions[]`. Parse each action using the `type` field:

| type | Meaning |
|------|---------|
| `input_variables` | Initial variables set at call start |
| `enter_task` | Agent entered a new task |
| `exit_task` | Agent exited a task |
| `instructions` | Task instructions rendered to the reasoner — check `instructions_metadata.task_name` and `len(content)` (0 = Jinja rendering failure) |
| `message` | A spoken message — check `source_system` and `message.sender` (`customer`/`bot`) |
| `function_request` | Agent called a function — check `function_request.function_name` and `parameters` |
| `function_response` | Response to a function call |
| `thought` | Reasoner's internal reasoning (step-by-step plan) |
| `llm_request` | LLM call metadata (model, tokens, cost) |
| `set_variables` | Reference variables updated after a function call |
| `system_transfer` | Call transferred to another system |
| `disconnect` | Call ended |

Key things to check while parsing:
- Any `instructions` with `len(content) == 0` → **Jinja rendering failure** (agent ran without task instructions)
- Any `function_request` with no matching mock → potential lookup failure
- `escalate_to_live_agent` vs `escalate_to_agent_from_ivr` — were both called? In what order?
- `end_of_conversation` — was this called correctly or prematurely?

## Step 4: Summarize the Conversation

Present a structured summary covering:

**Overview**
- Conversation ID, company, duration (first → last timestamp), total actions
- Task path: which tasks were entered/exited (CallerIdentification → DealershipIssues, etc.)
- Any Jinja rendering failures (instructions with empty content)

**Conversation Flow** (chronological, readable)
List the key turns as a readable narrative — not every action, just the meaningful ones:
- What the customer wanted
- How the agent responded and what functions it called
- Key decision points (escalation offers, lookups, task switches)
- How the call ended

**Issues Detected**
Flag any of the following automatically:
- Instructions rendered with `len=0` (Jinja failure)
- Functions called with no response / error response
- Agent said "No problem / Is there anything else?" after a Supervisor-scripted message without calling `send_customer_request_or_update` first (talker dropped the callback)
- `escalate_to_live_agent` called but `escalate_to_agent_from_ivr` never called after customer declined chat
- `end_of_conversation` called prematurely (before customer confirmed they're done)
- Unexpected task routing

## Step 5: Answer Questions

After presenting the summary, tell the user:

> "I've summarized the conversation above. Ask me anything about what the agent did, why it made a specific decision, or what went wrong at any point."

For each question:
- Reference the specific action index(es) relevant to the answer (e.g. "At action [142]...")
- Quote the relevant `thought`, `function_request`, or `message` content directly
- If the question is about WHY the agent did something, look at the `thought` immediately before the relevant action — that's the reasoner's step-by-step reasoning
- If the question is about the instructions the agent had at that point, find the most recent `instructions` action before the relevant turn and report its `task_name` and content length
- If content is encrypted or missing, say so explicitly rather than guessing

## Step 6: Wait for More Questions

After answering each question, ask: "Any other questions about this conversation?"

Continue answering until the user says they're done or moves on to a new topic.

## Important Notes

- Voice conversations fetched via `fetch_conversation.py` have `source_system` fields: `voice_assistant` (talker), `task_bot` (reasoner), `voice_digital_ga` (digital GA bridge), `customer`, `function_caller`, `voice_orchestrator`
- The talker (`voice_assistant`) and reasoner (`task_bot`) are separate components — the talker delivers speech, the reasoner decides what to do
- `send_customer_request_or_update` is how the talker communicates customer input to the reasoner
- A callback directive in the reasoner's instruction (e.g. "call me back with their response") means the talker MUST call `send_customer_request_or_update` after the customer replies — if it doesn't, the reasoner never learns the customer's answer
- `escalate_to_live_agent` triggers the Unified Escalation Protocol: offer chat first, then if declined call `escalate_to_agent_from_ivr` for phone transfer
