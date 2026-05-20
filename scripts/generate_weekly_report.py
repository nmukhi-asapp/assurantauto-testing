"""Generate the weekly CallerIdentification voice quality report.

Reads data/all_scored_rows.json and data/aggregates.json (produced by aggregate_scores.py).
Writes reports/CallerIdentification_quality_report_{week_end}.md.

Usage:
  python scripts/generate_weekly_report.py [--week-end YYYY-MM-DD]

If --week-end is omitted it is read from data/aggregates.json.
"""
import json, argparse
from pathlib import Path
from statistics import mean, stdev

REPO = Path(__file__).parent.parent
DATA = REPO / 'data' / 'conversations' / 'CallerIdentification'


def aiconsole(cid):
    return (f'https://ai-console.asapp.com/company/assurantauto/generative-agent/'
            f'main/conversations/externalConversationIds/{cid}?organization=assurantauto')


def get_transcript(cid, max_turns=40):
    fp = DATA / f'platform::assurantauto::{cid}::.json'
    with open(fp) as f:
        d = json.load(f)
    out = []
    for a in d['model_input']['actions']:
        if a.get('type') != 'message':
            continue
        m = a.get('message') or {}
        sp = m.get('speaker') or m.get('sender')
        if a.get('source_system') != 'voice_assistant':
            continue
        text = (m.get('text') or '').strip()
        if not text:
            continue
        if sp == 'bot':
            out.append(f'  Talker: {text}')
        elif sp == 'customer':
            out.append(f'  Customer: {text}')
        if len(out) >= max_turns:
            break
    return '\n'.join(out)


def bar(pct, width=25):
    f = round(pct / 100 * width)
    return '█' * f + '·' * (width - f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--week-end', default=None)
    args = ap.parse_args()

    with open(REPO / 'data' / 'all_scored_rows.json') as f:
        rows = json.load(f)
    with open(REPO / 'data' / 'aggregates.json') as f:
        agg = json.load(f)

    week_start = agg['week_start']
    week_end = args.week_end or agg['week_end']
    week_rows = [r for r in rows if r.get('date') and week_start <= r['date'] <= week_end]

    out = []
    out.append('## Weekly Voice Quality Report — CallerIdentification\n')
    out.append(f'*Week of {week_start} (Mon) → {week_end} (Sat) | Generated {week_end}*  ')
    out.append('*Scoring under the re-anchored rubric (effective 2026-05-13). Prior weeks have been re-scored under the same rubric for consistent WoW comparison.*\n')

    out.append(f'Conversations scored: {len(week_rows)}  |  Force-skipped (no caller dialogue): see baseline doc\n')
    w = agg['week']
    out.append('| Metric | Value |')
    out.append('|---|---|')
    out.append(f'| Mean overall score | {w["mean_score_5"]:.2f} / 5 ({w["mean_score_100"]}/100) |')
    out.append(f'| **Pass rate** | **{w["pass_count"]}/{w["n"]} = {w["pass_rate_pct"]:.1f}%** |')
    out.append(f'| Conversations scoring < 3.0 | {sum(1 for r in week_rows if r["score5"] < 3.0)} ({100*sum(1 for r in week_rows if r["score5"] < 3.0)/len(week_rows):.0f}%) |')
    out.append(f'| Safety / policy flags | {w["safety_flags"]} |')
    out.append(f'| Critical hallucination flags | {w["hallucination_flags"]} |')
    out.append(f'| Abandoned calls | {w["abandoned"]} |')
    out.append('')
    out.append('> **Scale reminder.** Under the re-anchored rubric, **3.0–3.5 = failing internal QA**, 3.5–4.0 = borderline, 4.0+ = solid.\n')
    out.append('---\n')

    # Section 1.5
    out.append('## Section 1.5: Pass / Fail\n')
    out.append('PASS iff D1 ≥ 4 AND no frustration indicators.\n')
    out.append('| Metric | Value |')
    out.append('|---|---|')
    out.append(f'| **Pass rate** | **{w["pass_count"]}/{w["n"]} = {w["pass_rate_pct"]:.1f}%** |')
    out.append(f'| Fail | {w["fail_count"]} ({100*w["fail_count"]/w["n"]:.1f}%) |')
    out.append('')
    out.append('### Daily Pass/Fail Trend\n')
    out.append('| Date | Total | Pass | % Pass | Trend |')
    out.append('|------|-------|------|--------|-------|')
    for d_, s in sorted(agg['week_daily'].items()):
        out.append(f'| {d_} | {s["total"]} | {s["pass"]} | {s["pass_rate_pct"]:.0f}% | {bar(s["pass_rate_pct"])} |')
    out.append('')

    # Section 2
    out.append('---\n')
    out.append('## Section 2: Daily Score Trend\n')
    out.append('| Date | N | Mean /5 | /100 | Trend |')
    out.append('|------|---|---------|------|-------|')
    for d_, s in sorted(agg['week_daily'].items()):
        out.append(f'| {d_} | {s["total"]} | {s["mean_score_5"]:.2f} | {s["mean_score_100"]} | {bar(s["mean_score_100"], 30)} |')
    out.append('')

    # Section 3
    out.append('---\n')
    out.append('## Section 3: Dimension Heatmap\n')
    out.append('| Dim | Name | Weight | Mean | Std | Min | Max | %≤2 |')
    out.append('|-----|------|--------|------|-----|-----|-----|------|')
    dim_info = [
        ('D1', 'Design Adherence', '20%'),
        ('D2', 'Information Accuracy', '10%'),
        ('D3', 'Context Retention', '10%'),
        ('D4', 'Response Latency', '10%'),
        ('D5', 'Turn-Taking', '8%'),
        ('D6', 'Repair & Recovery', '7%'),
        ('D8', 'Tone', '5%'),
        ('D9', 'Verbosity', '5%'),
        ('D10', 'ASR', '5%'),
        ('D12', 'Policy & Safety', '10%'),
    ]
    for dim, name, wt in dim_info:
        vals = [r[dim] for r in week_rows if r.get(dim) is not None]
        n_low = sum(1 for v in vals if v <= 2)
        s_v = stdev(vals) if len(vals) > 1 else 0
        out.append(f'| {dim} | {name} | {wt} | {mean(vals):.2f} | {s_v:.2f} | {min(vals)} | {max(vals)} | {100*n_low/len(vals):.0f}% |')
    out.append('| D7 | Speech Naturalness | 7% | N/A | — | — | — | — |')
    out.append('| D11 | Acoustic Robustness | 3% | N/A | — | — | — | — |')
    out.append('')

    # Section 4
    out.append('---\n')
    out.append('## Section 4: Per-Conversation Scores\n')
    out.append('| # | Date | Turns | D1 | D2 | D3 | D4 | D5 | D6 | D8 | D9 | D10 | D12 | Score | P/F | Flags |')
    out.append('|---|------|-------|----|----|----|----|----|----|----|-----|-----|-----|-------|-----|-------|')
    for i, r in enumerate(sorted(week_rows, key=lambda x: (x['date'], x['conv_id'])), start=1):
        pf_str = '✓ PASS' if r['pass_fail'] == 'PASS' else '✗ FAIL'
        fl = ','.join(r['flags']) if r['flags'] else '—'
        out.append(
            f"| [CONV {i}]({aiconsole(r['conv_id'])}) | {r['date'][5:]} | {r['turns']} | "
            f"{r['D1']} | {r['D2']} | {r['D3']} | {r['D4']} | {r['D5']} | {r['D6']} | "
            f"{r['D8']} | {r['D9']} | {r['D10']} | {r['D12']} | "
            f"{r['score5']:.2f} ({r['score100']}) | {pf_str} | {fl} |"
        )
    out.append('')

    # Section 5
    flagged = [r for r in week_rows if r['D1'] <= 2 or r['D12'] <= 2 or r['score5'] < 2.5 or r['flags']]
    out.append('---\n')
    out.append('## Section 5: Flagged Conversations\n')
    out.append(f'*Criteria: any flag, score < 2.5, D1 ≤ 2, or D12 ≤ 2 — {len(flagged)} of {len(week_rows)}.*\n')
    out.append('| Date | D1 | D12 | Score | Flags | Conv ID | Notes |')
    out.append('|------|----|----|-------|-------|---------|-------|')
    for r in sorted(flagged, key=lambda x: x['score5']):
        fl = ','.join(r['flags']) if r['flags'] else '—'
        notes = r['notes'][:200].replace('|', '/').replace('\n', ' ')
        out.append(f"| {r['date'][5:]} | {r['D1']} | {r['D12']} | {r['score5']:.2f} | {fl} | [`{r['conv_id'][:24]}...`]({aiconsole(r['conv_id'])}) | {notes} |")
    out.append('')

    # Section 6
    out.append('---\n')
    out.append('## Section 6: Representative Examples\n')
    sorted_rows = sorted(week_rows, key=lambda x: x['score5'])
    lowest = sorted_rows[0]
    highest = sorted_rows[-1]
    fail_candidates = [r for r in week_rows if r['pass_fail'] == 'FAIL']
    notable = sorted(fail_candidates, key=lambda r: (r['D1'], r['score5']))[0] if fail_candidates else lowest

    def render(r, label):
        return [
            f'### {label}: {r["score5"]:.2f}/5 ({r["score100"]}/100)',
            f'**Conv ID:** [`{r["conv_id"]}`]({aiconsole(r["conv_id"])})  ',
            f'**Date:** {r["date"]}  |  **Tasks:** {", ".join(r["tasks"])}  |  **D1:** {r["D1"]}  |  **D12:** {r["D12"]}',
            f'**Flags:** {", ".join(r["flags"]) if r["flags"] else "—"}  ',
            f'**Notes:** {r["notes"]}  ',
            '',
            '**Transcript:**',
            '```',
            get_transcript(r['conv_id']),
            '```',
            '',
        ]

    out.extend(render(highest, 'Highest scorer'))
    out.extend(render(notable, 'Most notable failure'))
    out.extend(render(lowest, 'Lowest scorer'))

    # Section 7
    out.append('---\n')
    out.append('## Section 7: Systemic Issues (Week)\n')
    note_blob = ' '.join((r['notes'] or '').lower() for r in week_rows)
    patterns = [
        ('Transfer-intent not recognized', ['kept asking for representative', 'asked for representative', 'asked for agent', "didn't escalate", 'never escalated', 'failed to escalate']),
        ('ASR mishearing', ['mis-transcribed', 'misheard', 'asian', 'misrecognized']),
        ('Repeated questions / poor context retention', ['repeated question', 'forgot', 'asked again', 're-asked', 'asked twice']),
        ('Generic response did not address specific need', ['generic', 'adjudicated in the order', 'under review', 'didn\'t address']),
        ('Excessive filler / verbosity', ['filler', 'one moment please', 'let me check', 'script-y', 'verbose']),
    ]
    for name, kws in patterns:
        n = sum(1 for r in week_rows if any(k in (r['notes'] or '').lower() for k in kws))
        if n > 0:
            out.append(f'- **{name}** — flagged in {n} of {len(week_rows)} calls ({100*n/len(week_rows):.0f}%) in notes.')
    out.append('')

    # Comparison
    b = agg['baseline']
    out.append('---\n')
    out.append('## Comparison vs. Re-scored Baseline (Apr 18 onward)\n')
    out.append('| Metric | This Week | Baseline | Δ |')
    out.append('|---|---|---|---|')
    dp = w['pass_rate_pct'] - b['pass_rate_pct']
    ds = w['mean_score_5'] - b['mean_score_5']
    out.append(f'| Pass rate | {w["pass_rate_pct"]:.1f}% | {b["pass_rate_pct"]:.1f}% | **{dp:+.1f} pp** |')
    out.append(f'| Mean score (/5) | {w["mean_score_5"]:.2f} | {b["mean_score_5"]:.2f} | **{ds:+.2f}** |')
    out.append(f'| Scored conversations | {w["n"]} | {b["n"]} | — |')
    out.append('')
    if abs(dp) > 5:
        out.append(f'- **Pass rate {"improved" if dp > 0 else "regressed"} by {abs(dp):.1f} pp** vs. baseline.')
    if abs(ds) > 0.15:
        out.append(f'- **Mean score {"improved" if ds > 0 else "regressed"} by {abs(ds):.2f}** points.')

    report_path = REPO / 'reports' / f'CallerIdentification_quality_report_{week_end}.md'
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text('\n'.join(out))
    print(f'Wrote: {report_path}')
    print(f'Week pass rate: {w["pass_rate_pct"]:.1f}% ({w["pass_count"]}/{w["n"]}), mean score: {w["mean_score_5"]:.2f}/5')


if __name__ == '__main__':
    main()
