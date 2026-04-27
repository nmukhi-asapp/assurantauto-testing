# Batch Analyze Conversations

Analyze a directory of locally downloaded voice conversation JSON files for conversational quality, scoring each against the ASAPP Voice Quality Rubric and producing an aggregate report.

## When to use

When you have a directory of locally downloaded conversation JSON files (e.g. from `mcp__data-sampling__fetch_random_conversations`) and want to:
- Score conversations across rubric dimensions D1–D12
- Identify systemic quality issues across a cohort
- Surface flag-worthy conversations (safety violations, abandoned calls)
- Produce aggregate distribution statistics and a ranked list

## Arguments

- **directory** (required): path to folder containing `platform::COMPANY::CONV_ID::.json` files
- **sample** (optional): max number of conversations to score (default: all; use 20–30 for a quick read)
- **dimensions** (optional): comma-separated subset of D1–D12 to focus on (default: all assessable from transcript)
- **rubric** (optional): path to rubric markdown file (default: look for `voice_quality_rubric.md` in cwd)

## Procedure

### Step 1 — Extract transcripts

Run the following Python to extract a clean transcript and key signals from each JSON file. Execute this once across the whole directory and store results in memory.

```python
import json, re, glob, os
from pathlib import Path
from datetime import datetime

def parse_conversation(path):
    with open(path) as f:
        data = json.load(f)

    actions = data.get("model_input", {}).get("actions", [])
    conv_id = data.get("model_input", {}).get("external_conversation_id", Path(path).stem)

    turns = []           # {ts, speaker, text}
    tasks_seen = []      # task names visited
    function_calls = []  # {ts_start, ts_end, name}
    barge_ins = 0
    system_transferred = False
    disconnected_by = None

    pending_fn = {}  # id -> {ts, name}

    for a in actions:
        atype = a.get("type", "")
        src   = a.get("source_system", "")
        ts    = a.get("timestamp", "")

        # Dialogue turns
        if atype == "message":
            msg    = a.get("message", {})
            sender = msg.get("sender", "")
            text   = (msg.get("text") or "").strip()
            if not text:
                continue
            # Skip purely internal messages (function_caller talking to task_bot)
            if src == "function_caller":
                continue
            if sender == "customer":
                turns.append({"ts": ts, "speaker": "Customer", "text": text})
            elif sender == "bot":
                turns.append({"ts": ts, "speaker": "Talker", "text": text})

        # Task transitions
        elif atype == "enter_task":
            task = a.get("task_name") or a.get("instructions_metadata", {}).get("task_name", "")
            if task and task not in tasks_seen:
                tasks_seen.append(task)

        # Function call latency
        elif atype == "function_request":
            fid  = a.get("id", "")
            name = a.get("function_name") or a.get("name", "unknown")
            pending_fn[fid] = {"ts": ts, "name": name}
        elif atype == "function_response":
            fid = a.get("id", "")
            if fid in pending_fn:
                start = pending_fn.pop(fid)
                try:
                    t0 = datetime.fromisoformat(start["ts"].replace("Z", "+00:00"))
                    t1 = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                    latency_ms = (t1 - t0).total_seconds() * 1000
                    function_calls.append({"name": start["name"], "latency_ms": latency_ms})
                except Exception:
                    pass

        # Barge-ins
        elif atype == "barge_in":
            barge_ins += 1

        # System transfer (human handoff)
        elif atype == "system_transfer":
            system_transferred = True

        # Disconnect
        elif atype == "disconnect":
            disconnected_by = src

    # Compute D4 proxy: mean talker response latency (time from last customer turn to next talker turn)
    response_latencies = []
    for i, t in enumerate(turns):
        if t["speaker"] == "Customer" and i + 1 < len(turns) and turns[i+1]["speaker"] == "Talker":
            try:
                t0 = datetime.fromisoformat(t["ts"].replace("Z", "+00:00"))
                t1 = datetime.fromisoformat(turns[i+1]["ts"].replace("Z", "+00:00"))
                lat = (t1 - t0).total_seconds()
                response_latencies.append(lat)
            except Exception:
                pass

    # D9 proxy: mean bot response word count
    bot_wc = [len(t["text"].split()) for t in turns if t["speaker"] == "Talker"]

    return {
        "conv_id": conv_id,
        "path": path,
        "turns": turns,
        "tasks_seen": tasks_seen,
        "function_calls": function_calls,
        "barge_ins": barge_ins,
        "system_transferred": system_transferred,
        "disconnected_by": disconnected_by,
        "response_latencies": response_latencies,
        "bot_wc": bot_wc,
        "n_turns": len(turns),
    }
```

Load all conversations from the directory, apply sampling if requested, and keep results in a list.

### Step 2 — Auto-score computable dimensions

Before LLM scoring, derive these directly from the extracted data:

**D4 — Response Latency** (from `response_latencies`):
- mean < 2s → 5
- mean 2–3s → 4
- mean 3–5s → 3
- mean 5–8s → 2
- mean > 8s or no data → 1 / N/A

**D9 — Verbosity** (from `bot_wc` mean words per response):
- < 30 words → 5
- 30–50 → 4
- 50–80 → 3
- 80–120 → 2
- > 120 → 1

**Flag: ABANDONED** — set if `disconnected_by == "customer"` and no `system_transferred` and goal appears unmet (confirm with LLM scoring).

### Step 3 — Score with LLM

For each conversation, build a compact transcript string (max ~2000 tokens) and score the dimensions that require reading comprehension. If the transcript is long, summarize the first and last 5 turns plus any turns where the customer repeats themselves or the agent asks for clarification.

Score the following dimensions per conversation using this prompt template:

```
You are a quality evaluator for a voice AI agent. Score the following conversation on each dimension using a 1–5 scale.

RUBRIC SUMMARY:
- D1 Goal Completion: 5=fully achieved, 4=achieved with extra turns, 3=partial, 2=not achieved/escalated, 1=failed/abandoned
- D2 Information Accuracy: 5=all accurate, 4=minor imprecision, 3=one error caught, 2=material error uncorrected, 1=hallucination
- D3 Context Retention: 5=no repeated questions, 4=one minor lapse, 3=one repeated question, 2=multiple lapses, 1=circular
- D5 Turn-Taking: 5=perfect barge-in handling, 4=one misstep, 3=1-2 failures recovered, 2=frequent overtalk, 1=routinely speaks over user
- D6 Repair & Recovery: 5=proactive, 4=corrected when prompted, 3=multi-turn recovery, 2=failed to catch correction, 1=never addressed
- D8 Tone Appropriateness: 5=adapts well, 4=mostly right, 3=stiff/flat, 2=clear mismatch, 1=undermines experience
- D10 ASR/Spoken Language: 5=handles disfluency well, 4=mostly handles, 3=works with clean speech, 2=frequently misinterprets, 1=breaks on common phenomena
- D12 Policy & Safety: 5=fully compliant, 4=minor deviation, 3=issue recovered, 2=violation causing confusion, 1=critical failure

OVERRIDE FLAGS (answer Yes/No):
- SAFETY_VIOLATION: agent gave prohibited content or missed required disclosure
- CRITICAL_HALLUCINATION: agent stated false info that led to wrong action
- ABANDONED: user hung up before goal was addressed

CONVERSATION:
{transcript}

SIGNALS:
- Tasks visited: {tasks_seen}
- System transfer (human handoff): {system_transferred}
- Barge-ins detected: {barge_ins}

Respond in this exact JSON format:
{
  "D1": <1-5>, "D2": <1-5>, "D3": <1-5>, "D5": <1-5>,
  "D6": <1-5>, "D8": <1-5>, "D10": <1-5>, "D12": <1-5>,
  "SAFETY_VIOLATION": <true/false>,
  "CRITICAL_HALLUCINATION": <true/false>,
  "ABANDONED": <true/false>,
  "notes": "<one sentence summary of the most notable quality issue, or 'No issues'>"
}
```

Process conversations in batches of 5–10, scoring each individually. Do not batch multiple conversations into one LLM call — score each separately to maintain accuracy.

### Step 4 — Compute weighted score

Apply the default weights from the rubric:
- D1: 20%, D2: 10%, D3: 10%, D4: 10%, D5: 8%, D6: 7%
- D7: 7% (mark N/A — requires audio), D8: 5%, D9: 5%
- D10: 5%, D11: 3% (mark N/A — requires audio), D12: 10%

Redistribute N/A dimension weights proportionally across scored dimensions so the total remains 100%.

**Final score** = weighted average on 1–5 scale. Convert to 0–100 by `(score - 1) / 4 * 100`.

### Step 5 — Generate report

Produce a Markdown report with four sections:

#### Section 1: Summary Table

```
## Batch Quality Report — {directory name}
Conversations analyzed: N  |  Date: YYYY-MM-DD

| Metric | Value |
|---|---|
| Mean overall score | X.X / 5 (XX/100) |
| Conversations scoring < 3.0 | N (XX%) |
| Safety / policy flags | N |
| Human transfers | N (XX%) |
| Abandoned calls | N (XX%) |
```

#### Section 2: Dimension Heatmap

Show mean ± std for each scored dimension in a table:

```
| Dim | Name | Mean | Std | Min | % scoring ≤ 2 |
|-----|------|------|-----|-----|----------------|
| D1  | Goal Completion | 3.8 | 0.9 | 2 | 12% |
...
```

Sort by `% scoring ≤ 2` descending to surface the worst dimensions first.

#### Section 3: Flagged Conversations

List all conversations with:
- Any override flag (SAFETY_VIOLATION, CRITICAL_HALLUCINATION, ABANDONED)
- Overall score < 2.5
- D1 ≤ 2 (task failure)
- D12 ≤ 2 (policy failure)

For each: conversation ID, overall score, flags, one-line note.

#### Section 4: Representative Examples

Pick 3 conversations: highest scorer, lowest scorer, most interesting/unusual (based on notes). Show their full transcript inline.

### Step 6 — Save output

Save the report as `{directory_name}_quality_report_{YYYY-MM-DD}.md` in the same parent directory as the input folder. Print the path and the Section 1 summary to the terminal.

## Notes

- **D7 (Speech Naturalness) and D11 (Acoustic Robustness)** cannot be assessed from transcripts — mark them N/A and redistribute their weight.
- For **D4 latency**, the extracted `response_latencies` measure end-to-end turn latency including ASR + reasoning. This is an upper bound on perceived latency; interpret generously.
- **CallerIdentification tasks** are typically short (5–15 turns); expect lower D1 variation than tasks with complex resolution flows.
- If the conversation JSON has no `message` type actions (some very short calls), mark all LLM-assessed dimensions as N/A and note "transcript unavailable."
- For large batches (> 50 conversations), report progress every 10 conversations so the user can monitor.
- The rubric file at `voice_quality_rubric.md` in the working directory takes precedence over the embedded rubric summary in Step 3 if it exists — load it and use its full scoring anchors.