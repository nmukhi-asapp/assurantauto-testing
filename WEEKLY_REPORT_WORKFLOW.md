# Weekly CallerIdentification Voice Quality Report — Workflow Status

**Report Period:** Monday, June 15, 2026 → Saturday, June 21, 2026  
**Generated:** June 22, 2026  
**Status:** IN PROGRESS (Remote agent with AWS access executing)

## Workflow Overview

The weekly voice quality report automates the collection, scoring, and analysis of CallerIdentification conversations to track quality trends.

### Architecture

```
Athena (production conversations)
  ↓
List conversation IDs (filter: CallerIdentification task)
  ↓
Fetch new conversations (base + _int pairs)
  ↓
Score with LLM judge (Claude Opus 4.7 via LiteLLM)
  ↓
Aggregate scores + compute metrics
  ↓
Generate reports:
  - Markdown quality report
  - PNG slides (pass rate, quality, flagged calls)
  - Weekly summary tables
```

### Data Pipeline

| Step | Command | Input | Output | Status |
|------|---------|-------|--------|--------|
| 1-2 | `mcp__data-sampling__list_conversation_ids()` | Date range + task filter | Conversation IDs | RUNNING |
| 3 | Cross-ref `all_scored_rows.json` | Existing IDs | New IDs to fetch | PENDING |
| 4 | `mcp__data-sampling__fetch_conversations_by_id()` | New IDs | JSON files in `data/conversations/` | PENDING |
| 5 | `llm_judge_score.py` | Conversation JSONs | Score JSONs in `data/scores/` | PENDING |
| 6 | `aggregate_scores.py` | Score JSONs + conversation JSONs | `all_scored_rows.json`, `aggregates.json` | PENDING |
| 7 | `generate_weekly_report.py` | Aggregates + conversation data | `reports/CallerIdentification_quality_report_2026-06-21.md` | PENDING |
| 8 | `generate_weekly_slides.py` | Aggregates | PNG slides + markdown tables | PENDING |

## Expected Outputs

Once the remote agent completes:

### 1. Report File
```
reports/CallerIdentification_quality_report_2026-06-21.md
```
Contains:
- Weekly pass rate (target: ~75%)
- Mean quality score (target: 3.8–4.0/5)
- Daily trends (pass rate, score)
- Dimension heatmap (D1–D12 performance)
- Per-conversation scores table
- Flagged conversations analysis
- Representative examples (best, worst, notable)
- Systemic issues summary

### 2. Data Files
```
data/all_scored_rows.json       — Rows: [conv_id, date, D1–D12, score5, score100, pass_fail, ...]
data/aggregates.json            — Summary stats: {week, baseline, daily, ...}
data/conversations/CallerIdentification/*.json    — Fetched conversation JSONs
data/scores/*.json              — LLM judge scores per conversation
```

### 3. Slide Artifacts
```
reports/weekly_slides/2026-06-21/
  ├── slide_4_pass_rate.png           — Daily pass rate bars + trend line
  ├── slide_5_quality_score.png       — Daily mean score with QA threshold lines
  ├── slide_6_low_quality_count.png   — Daily count of ≤3.5 calls
  ├── slides_4_5_tables.md            — Period summary tables
  └── slide_10_good_bad.md            — Top/bottom conversation examples
```

## Key Metrics (Previous Week Reference)

For comparison, the week of 2026-06-08 to 2026-06-13:
- **Conversations scored:** 73
- **Pass rate:** 78.1% (57/73)
- **Mean score:** 3.93/5 (79/100)
- **Conversations < 3.0:** 16 (22%)
- **Safety flags:** 0
- **Hallucination flags:** 1
- **Abandoned calls:** 0

This week (2026-06-15 to 2026-06-21) metrics will follow the same structure once calculations complete.

## Requirements Met

✓ Directory structure created  
✓ Scripts available and validated  
✓ Previous baseline data available for comparison  
✓ Remote agent launched with AWS credentials and full environment access  

## Next Steps (Automatic)

Once the remote agent completes:
1. Review generated report at `reports/CallerIdentification_quality_report_2026-06-21.md`
2. Check key metrics (pass rate, mean score, flagged calls)
3. Compare vs. baseline (Apr 18 onward)
4. Identify trends and systemic issues
5. Share report and slides with stakeholders

## Access & Permissions

**Report Location:** `/Users/nmukhi/code/assurantauto-testing/reports/`  
**Raw Data:** `/Users/nmukhi/code/assurantauto-testing/data/`  
**Owner:** nmukhi@asapp.com  
**Team:** AssurantAuto GA Quality