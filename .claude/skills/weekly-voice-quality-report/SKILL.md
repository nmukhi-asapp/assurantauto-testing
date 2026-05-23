# Weekly Voice Quality Report

Generate the weekly CallerIdentification voice quality report for production conversations from the previous Mon–Sat week. Includes the design-adherence rubric scoring and the binary pass/fail metric.

All data, scripts, and outputs live within the `assurantauto-testing` repo. Repo root is referred to as `REPO` below.

## When to use

- Sunday morning runs (scheduled via CronCreate).
- Ad-hoc when the user asks for a week-over-week voice quality report.

## Repo layout

```
REPO/
  data/
    conversations/CallerIdentification/   ← fetched conversation JSONs
    scores/                               ← per-conv LLM-judge score JSONs
    all_scored_rows.json                  ← aggregated rows (all scored convs)
    aggregates.json                       ← summary stats (all / baseline / week / daily)
  scripts/
    llm_judge_score.py                    ← LLM judge scorer
    aggregate_scores.py                   ← aggregation + pass/fail logic
    generate_weekly_report.py             ← markdown report builder
    generate_weekly_slides.py             ← slide PNG + table builder
  reports/
    CallerIdentification_quality_report_{week_end}.md
    weekly_slides/{week_end}/
      slide_4_pass_rate.png
      slide_5_quality_score.png
      slide_6_low_quality_count.png
      slides_4_5_tables.md
      slide_10_good_bad.md
  voice_quality_rubric.md
  .env                                    ← LITELLM_URL, LITELLM_API_KEY
```

## Procedure

### 1. Determine date range

Use Python `date.today()` for today. Compute:
- `week_end` = most recent Saturday
- `week_start` = week_end − 5 days (Monday)

### 2. List CallerIdentification conversations from Athena

```
mcp__data-sampling__list_conversation_ids(
  company_marker="assurantauto",
  start_date="{week_start}",
  end_date="{week_end_plus_1}",   # Athena BETWEEN is exclusive on the right
  first_task_name="CallerIdentification"
)
```

Each conversation has both a base ID and `_int` suffix — collapse pairs to unique base IDs.

### 3. Identify which are new

Cross-reference the new IDs against `data/all_scored_rows.json`. Only fetch and score IDs not already present.

### 4. Fetch new conversations

```
mcp__data-sampling__fetch_conversations_by_id(
  company_marker="assurantauto",
  conversation_ids=[...new ids...],
  save_conversations=true,
  is_voice=true,
  output_dir="REPO/data/conversations/CallerIdentification"
)
```

### 5. Score new conversations with LLM judge

```bash
# From REPO root — unset SOCKS proxy, keep HTTP proxy for LiteLLM reachability
env -u ALL_PROXY -u all_proxy -u FTP_PROXY -u ftp_proxy -u GRPC_PROXY -u grpc_proxy \
  JUDGE_MODEL=vertex-claude-4.7-opus \
  .venv/bin/python3 scripts/llm_judge_score.py \
  --ids <id1> <id2> ... --workers 10
```

Or pipe from a file of IDs:
```bash
cat ids.txt | env -u ALL_PROXY -u all_proxy -u FTP_PROXY -u ftp_proxy -u GRPC_PROXY -u grpc_proxy \
  JUDGE_MODEL=vertex-claude-4.7-opus \
  .venv/bin/python3 scripts/llm_judge_score.py --ids - --workers 10
```

Scores are written to `data/scores/{conv_id}.json`. If the LiteLLM proxy returns connection errors, check VPN is connected and `https://litellm.test.asapp.com/health` is reachable.

**Dimensions (production):**
- D1 Design Adherence (20%) — did bot follow task config? 1–5
- D2 Information Accuracy (10%)
- D3 Context Retention (10%)
- D4 Response Latency (10%)
- D5 Turn-Taking (8%)
- D6 Repair & Recovery (7%)
- D7 N/A (audio)
- D8 Tone (5%)
- D9 Verbosity (5%)
- D10 ASR (5%)
- D11 N/A (audio)
- D12 Policy & Safety (10%)

Reference rubric: `voice_quality_rubric.md`

**D1 anchors:**
- **5**: bot followed designed flow exactly
- **4**: right outcome, minor deviation
- **3**: noticeable problem — clear friction that impacted the caller
- **2**: wrong behavior — looped on identifiers after second refusal, escalated in-scope call
- **1**: critical mismatch — refused valid escalation, looped without ever escalating

**Calibrated behaviors — do NOT penalize as D1 deviations:**
- **Pre-transfer identifier collection**: asking for identifiers twice before transfer is by design. First ask = standalone; second = expanded ("contract number, claim number, or last 8 of VIN") framed as "before I transfer you." Do NOT treat the second ask as a D3 or D6 failure.
- **Smart Deflection**: deflecting the *first* agent-transfer request by asking what the caller needs help with is intentional. Only the second explicit insistence triggers the transfer obligation.
- **Dealer claim funneling**: for dealer callers asking about claims, two funneling questions before identifier collection are by design: (1) existing vs. new vs. other, (2) issue type (payment/status/modification).
- **D10 = recognition fidelity only**: how the bot responds to an ASR error belongs in D6 and D1, not D10.
- **D2 anchors**: 5 = directly addresses the specific question. 4 = relevant and correct but doesn't directly address the specific need (no wrong facts). 3 = incomplete or misleading in a way that affected the caller. 2 = wrong information.

### 6. Aggregate scores

```bash
python3 scripts/aggregate_scores.py --week-start {week_start} --week-end {week_end}
```

Updates `data/all_scored_rows.json` and `data/aggregates.json`.

### 7. Generate the weekly report

```bash
python3 scripts/generate_weekly_report.py
```

Writes `reports/CallerIdentification_quality_report_{week_end}.md`.

### 8. Generate slides

```bash
python3 scripts/generate_weekly_slides.py
```

Writes to `reports/weekly_slides/{week_end}/`:
- `slide_4_pass_rate.png` — daily pass rate bars + total conversations line + linear trend
- `slide_5_quality_score.png` — daily mean quality score with 3.0 (failing) and 3.5 (borderline) reference lines
- `slide_6_low_quality_count.png` — daily count of calls scoring ≤ 3.5 + linear trend
- `slides_4_5_tables.md` — period tables for slides 4 and 5
- `slide_10_good_bad.md` — one good / one bad call picks for the week

### 9. Notify user

Report back with:
- Report file path
- Week's pass rate and mean score
- Notable changes vs. baseline (>5pp pass rate change or ±0.15 score change)

## Pass/fail definition

```python
FRUSTRATION_KW = ["kept asking","loop","circles","stuck","refused","never transferred",
  "never escalated","didn't escalate","ended without","ended call when","wrong info",
  "dismissed","couldn't connect","false transfer","abandon","frustrat","told customer to call",
  "couldn't authenticate","looped","unable to assist further","kept saying unable",
  "stuck in loop","failed 6+","kept refusing","answered specific question instead"]

def classify(s):
    frustrated = (
        'ABANDONED' in (s.get('flags') or []) or
        s.get('D1') == 1 or
        any(kw in (s.get('notes') or '').lower() for kw in FRUSTRATION_KW)
    )
    return 'PASS' if s.get('D1', 0) >= 4 and not frustrated else 'FAIL'
```

## Scale reminder

Under the re-anchored rubric (effective 2026-05-13):
- **3.0–3.5** = failing internal QA
- **3.5–4.0** = borderline
- **4.0+** = solid
- **5** = no observable defects (rare)

Reports dated 2026-05-09 or earlier used old anchors and are not directly comparable.