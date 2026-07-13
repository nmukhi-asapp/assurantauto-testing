---
description: Analyze a conversation for gaps between GenAgent's capabilities and what a human agent did after escalation. Fetches the conversation including human agent utterances, fetches the GenAgent config from GACS, and produces a gap report with suggested knowledge articles and hypothetical API signatures.
arguments:
  - name: args
    description: "<conversation-id> <company-marker> [--branch <gacs-branch>] — branch defaults to 'main'"
---

# Analyze GenAgent Gaps

Compare what a human agent did in a conversation against what GenAgent has available (instructions + functions), and identify capability gaps.

## ADR Reference

When analyzing gaps, consider:

- **ADR 0006: Voice Configuration Design Decisions** — Understanding the Talker-Reasoner architecture helps identify where capability gaps exist:
  - **DD-03**: Voice Settings (Talker FAQs) vs. Procedures (Reasoner business logic) — gaps may be in either layer
  - **DD-06**: Proper API sequencing — human agents follow different patterns than the Reasoner loop design allows
  - **DD-08**: Escalation responsibility — human agents decide escalation; Procedures must encode those business rules
  - **DD-10/DD-11**: Function design — human agents use implicit knowledge; functions must make it explicit

**When analyzing capability gaps:**
1. Distinguish between **Talker gaps** (immediate answers from Voice Settings) vs. **Reasoner gaps** (business logic in Procedures)
2. Check if task instructions match the Talker-Reasoner model (DD-03 boundary)
3. Identify if missing functions violate proper sequencing (DD-06)
4. Assess whether escalation conditions should be in Procedures (DD-08)

**Location:** `../generative-agent/asapp/generative_agent/tools/workbench/docs/adrs/0006-voice-configuration-design-decisions.md`

---

## Step 1: Parse Arguments

Parse `$ARGUMENTS`:
- **conversation-id** (required) — e.g. `2209534218-1045828081-2391966186-2917985560`
- **company-marker** (required) — e.g. `assurantauto`
- **--branch** (optional, default: `main`) — GACS branch to pull GenAgent config from

If conversation-id or company-marker are missing, ask for them before proceeding.

## Step 2: Fetch the Conversation

Use `mcp__data-sampling__fetch_conversations_by_id` with **all three flags** set:

```python
mcp__data-sampling__fetch_conversations_by_id(
    company_marker="<company-marker>",
    conversation_ids=["<conversation-id>"],
    is_voice=True,
    include_human_agent_utterances=True,
    save_conversations=True,
    output_dir="<absolute-path-to-assurantauto-testing-repo>/fetched_conversations"
)
```

The saved file will be at:
`fetched_conversations/platform::<company-marker>::<conversation-id>::<customer-id>.json`

Read the file after fetching.

## Step 3: Parse the Conversation

Run the following Python to extract the dialogue and check for human agent utterances. Pass the actual file path.

```python
import json, sys
from pathlib import Path

f = Path("<path-to-conversation-json>")
data = json.load(open(f))
actions = data.get('model_input', {}).get('actions', [])

tasks_visited = []
current_task = '(init)'
dialogue = []
functions_called = []
has_human_agent = False

for a in actions:
    t = a.get('type', '')
    ts = a.get('timestamp', '')[:19]
    src = a.get('source_system', '')

    if t == 'enter_task':
        current_task = a.get('task_name', current_task)
        tasks_visited.append(current_task)

    elif t == 'message':
        msg = a.get('message', {})
        sender = msg.get('sender', '')
        text = (msg.get('text', '') or '').strip()
        is_synth = msg.get('is_synthetic_interim_message', False)
        # Human agent utterances are interleaved as synthetic actions.
        # They carry message_sender_type='HUMAN_AGENT' at the action level
        # or as msg.get('sender_type') == 'HUMAN_AGENT'.
        sender_type = (
            a.get('message_sender_type', '') or
            msg.get('sender_type', '') or
            ''
        ).upper()

        if not text:
            continue
        if sender_type == 'HUMAN_AGENT' or src == 'human_agent':
            has_human_agent = True
            dialogue.append(f"[{ts[11:16]}][{current_task}] HUMAN AGENT: {text}")
        elif sender == 'customer' or src == 'customer' or sender_type == 'CUSTOMER':
            dialogue.append(f"[{ts[11:16]}][{current_task}] CUSTOMER: {text}")
        elif sender == 'bot' and not is_synth:
            dialogue.append(f"[{ts[11:16]}][{current_task}] GENAGENT: {text}")

    elif t == 'function_request':
        fr = a.get('function_request', {})
        fn = fr.get('function_name', '')
        params = fr.get('parameters', {})
        if fn:
            functions_called.append({'task': current_task, 'fn': fn, 'params': params})

print("=== TASKS VISITED ===")
print(tasks_visited)
print()
print("=== HAS HUMAN AGENT UTTERANCES ===")
print(has_human_agent)
print()
print("=== DIALOGUE ===")
for line in dialogue:
    print(line)
print()
print("=== GENAGENT FUNCTION CALLS ===")
for fc in functions_called:
    print(f"  [{fc['task']}] {fc['fn']}({json.dumps(fc['params'])[:120]})")
```

## Step 4: Check for Human Agent Utterances

**If `has_human_agent` is `False`:**

The conversation was fully contained by GenAgent. Write a short report and stop:

```markdown
# GenAgent Gap Analysis: <conversation-id>

**Company:** <company-marker>
**GACS Branch:** <branch>
**Tasks visited:** <tasks>

## Result: No Gaps Identified ✅

This conversation was fully contained by GenAgent — no human agent handled any part of it.
No knowledge or tool gaps to report.
```

Save to `gap-analysis/gap-analysis-<conversation-id>.md` and stop.

---

**If `has_human_agent` is `True`:** continue to Step 5.

## Step 5: Fetch GenAgent Configuration from GACS

Fetch the full branch config (tasks with instructions + functions) using:

```python
mcp__gacs__get_branch(
    company_marker="<company-marker>",
    branch_name="<branch>",
    output_dir="<absolute-path-to-assurantauto-testing-repo>/outputs/gacs"
)
```

Read the saved output file. Focus on:
- **Task instructions** (`prompt_instructions`) for each task the conversation visited
- **Functions list** — the complete set of functions available to GenAgent

## Step 6: Analyze Gaps

You now have:
- The human agent's messages and the context in which they occurred
- The customer's messages and what they were trying to accomplish
- GenAgent's instructions for each relevant task
- The full list of functions GenAgent can call

Carefully read the human agent side of the conversation and identify:

### Knowledge Gaps
Things the human agent knew or explained that are **not covered** (or are insufficiently covered) by GenAgent's task instructions or knowledge base.

For each gap:
- Describe what knowledge the human agent applied
- Write a concise knowledge article snippet (2–5 sentences) that could be added to GenAgent's instructions or knowledge base to cover this gap
- Note which task's instructions it should be added to

### Tool / Action Gaps
Actions the human agent performed that require **capabilities GenAgent does not have** — i.e., no existing function covers this action.

For each gap:
- Describe what the human agent did
- Write a hypothetical API signature in this format:
  ```
  functionName(param1: Type, param2: Type, ...) -> ResponseType
  ```
- Write a 1–2 sentence description of what the function does and what system it would integrate with

**Important:** Do not flag something as a gap if:
- GenAgent has a function that covers it (even if it wasn't called in this conversation)
- The human agent was just rephrasing or clarifying something already in GenAgent's instructions
- The human agent was performing social niceties unrelated to resolving the customer's issue

## Step 7: Write the Gap Report

Save to `gap-analysis/gap-analysis-<conversation-id>.md` (create the directory if needed).

```markdown
# GenAgent Gap Analysis: <conversation-id>

**Company:** <company-marker>
**GACS Branch:** <branch>
**Date analyzed:** <today's date>
**Tasks visited:** <comma-separated list>

## Conversation Summary

<2–4 sentences: what the customer wanted, what GenAgent did, why it escalated to a human agent, and what the human agent did>

## Human Agent Transcript

<Reproduce only the human agent turns and the surrounding customer context — enough to understand what the HA was doing>

---

## Gap Analysis

### Knowledge Gaps

<If none found, write: "No knowledge gaps identified.">

1. **<Short gap title>**
   - **What the human agent knew:** <description>
   - **Suggested addition to task:** `<task-name>`
   - **Article snippet:**
     > <2–5 sentence knowledge article text, written in the voice of GA instructions>

2. ...

---

### Tool / Action Gaps

<If none found, write: "No tool gaps identified.">

1. **<Short gap title>**
   - **What the human agent did:** <description>
   - **Suggested API:**
     ```
     functionName(param1: Type, param2: Type) -> ResponseType
     ```
     <1–2 sentence description of what it does and what system it would connect to>

2. ...

---

## Summary

| Category | Count |
|---|---|
| Knowledge gaps | N |
| Tool gaps | N |

<1–2 sentence overall takeaway: what is the biggest leverage point for improving GenAgent's containment on this call type?>
```

After saving the file, tell the user where the report was saved and give a brief summary of findings.