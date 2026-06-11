"""Generate slide content for the weekly CallerIdentification voice quality report.

Reads data/all_scored_rows.json and data/aggregates.json (produced by aggregate_scores.py).

Outputs to reports/weekly_slides/{week_end}/:
  slide_4_pass_rate.png        — daily pass rate bars + total line + trend
  slide_5_quality_score.png    — daily mean quality score line
  slide_6_low_quality_count.png — daily count of calls scoring ≤ 3.5 + trend
  slides_4_5_tables.md         — period tables for slides 4 and 5
  slide_10_good_bad.md         — one good call / one bad call picks for the week

Usage:
  python scripts/generate_weekly_slides.py [--week-end YYYY-MM-DD]
"""
import json, os, argparse
from pathlib import Path
from collections import defaultdict
from statistics import mean

os.environ['MPLCONFIGDIR'] = str(Path(__file__).parent.parent / 'data' / '.matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

REPO = Path(__file__).parent.parent


def aiconsole(cid):
    return (f'https://ai-console.asapp.com/company/assurantauto/generative-agent/'
            f'main/conversations/externalConversationIds/{cid}?organization=assurantauto')


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

    # Build daily aggregates over full baseline window for trend charts
    daily = defaultdict(list)
    for r in rows:
        if r.get('date') and r['date'] >= '2026-04-18':
            daily[r['date']].append(r)

    labels = sorted(daily.keys())
    x = list(range(len(labels)))
    x_arr = np.array(x)
    pcts = [100 * sum(1 for r in daily[d] if r['pass_fail'] == 'PASS') / len(daily[d]) for d in labels]
    totals = [len(daily[d]) for d in labels]
    mean_scores = [mean(r['score5'] for r in daily[d]) for d in labels]
    bad_pcts = [100 * sum(1 for r in daily[d] if r['score5'] <= 3.5) / len(daily[d]) for d in labels]

    out_dir = REPO / 'reports' / 'weekly_slides' / week_end
    out_dir.mkdir(parents=True, exist_ok=True)

    # ── Slide 4: pass rate bars + total line + trend ──────────────────────
    fig, ax1 = plt.subplots(figsize=(14, 6))
    ax1.bar(x, pcts, color='#D44A3F', alpha=0.85, label='Pass rate %')
    z = np.polyfit(x_arr, pcts, 1)
    ax1.plot(x_arr, np.poly1d(z)(x_arr), color='#991B1B', linewidth=2,
             linestyle='--', label='Trend')
    ax1.set_ylabel('Pass rate (%)', color='#D44A3F')
    ax1.set_ylim(0, 100)
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, rotation=45, ha='right', fontsize=9)
    ax2 = ax1.twinx()
    ax2.plot(x, totals, color='#3B82F6', marker='o', linewidth=2, label='Total')
    ax2.set_ylabel('Total conversations', color='#3B82F6')
    ax2.set_ylim(0, (max(totals) if totals else 1) * 1.2)
    lines1, l1 = ax1.get_legend_handles_labels()
    lines2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, l1 + l2, loc='upper center',
               bbox_to_anchor=(0.5, 1.10), ncol=3, frameon=False)
    plt.title('Pass rate (re-anchored rubric, Apr 18 onward)', loc='left',
              fontsize=11, color='#555', pad=20)
    plt.tight_layout()
    plt.savefig(out_dir / 'slide_4_pass_rate.png', dpi=150, bbox_inches='tight')
    plt.close()

    # ── Slide 5: quality score line ───────────────────────────────────────
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x, mean_scores, color='#3B82F6', marker='o', linewidth=2)
    ax.axhline(y=3.0, color='#D44A3F', linestyle='--', linewidth=1, alpha=0.7,
               label='Failing threshold (3.0)')
    ax.axhline(y=3.5, color='#F59E0B', linestyle='--', linewidth=1, alpha=0.7,
               label='Borderline (3.5)')
    ax.set_ylim(0, 5)
    ax.set_ylabel('Average score')
    ax.set_xlabel('Date')
    ax.set_title('Average score vs. Date (re-anchored rubric)', loc='left',
                 fontsize=12, color='#555')
    ax.legend(loc='lower right', fontsize=9)
    n = len(labels)
    if n > 6:
        tick_idx = list(range(0, n, max(1, n // 6)))
        if tick_idx[-1] != n - 1:
            tick_idx.append(n - 1)
        ax.set_xticks(tick_idx)
        ax.set_xticklabels([labels[i] for i in tick_idx], rotation=45, ha='right')
    else:
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(out_dir / 'slide_5_quality_score.png', dpi=150, bbox_inches='tight')
    plt.close()

    # ── Slide 6: daily % of calls scoring ≤ 3.5 ─────────────────────────
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.bar(x, bad_pcts, color='#D44A3F', alpha=0.85, label='% ≤ 3.5')
    z6 = np.polyfit(x_arr, bad_pcts, 1)
    ax.plot(x_arr, np.poly1d(z6)(x_arr), color='#991B1B', linewidth=2,
            linestyle='--', label='Trend')
    ax.set_ylabel('% calls scoring ≤ 3.5')
    ax.set_xlabel('Date')
    ax.set_ylim(0, 100)
    ax.set_title('Daily % of low-quality calls (score ≤ 3.5, re-anchored rubric)',
                 loc='left', fontsize=11, color='#555')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=9)
    ax.grid(True, alpha=0.3, axis='y')
    ax.legend(loc='upper right', fontsize=9)
    plt.tight_layout()
    plt.savefig(out_dir / 'slide_6_low_quality_count.png', dpi=150, bbox_inches='tight')
    plt.close()

    # ── Slide 4 & 5 period tables ─────────────────────────────────────────
    from datetime import date as date_cls
    ws = date_cls.fromisoformat(week_start)
    we = date_cls.fromisoformat(week_end)
    w = agg['week']
    b = agg['baseline']
    tables = [
        '# Slide 4 — Pass Rate (period table on the right)\n',
        '*Scored under the re-anchored rubric (effective 2026-05-13).*\n',
        '| Period | Avg pass rate |',
        '|---|---|',
        f'| **Week of {ws.strftime("%b %-d")}** ({ws.strftime("%b %-d")}–{we.strftime("%-d")}, N={w["n"]}) | **{w["pass_rate_pct"]:.1f}%** ({w["pass_count"]}/{w["n"]}) |',
        f'| **Since April 18** (N={b["n"]}) | **{b["pass_rate_pct"]:.1f}%** ({b["pass_count"]}/{b["n"]}) |',
        '',
        '# Slide 5 — Quality Score (period table on the right)\n',
        '| Period | Avg quality score |',
        '|---|---|',
        f'| **Week of {ws.strftime("%b %-d")}** ({ws.strftime("%b %-d")}–{we.strftime("%-d")}, N={w["n"]}) | **{w["mean_score_5"]:.2f} / 5** ({w["mean_score_100"]}/100) |',
        f'| **Since April 18** (N={b["n"]}) | **{b["mean_score_5"]:.2f} / 5** ({b["mean_score_100"]}/100) |',
        '',
    ]
    (out_dir / 'slides_4_5_tables.md').write_text('\n'.join(tables))

    # ── Slide 10: one good / one bad ──────────────────────────────────────
    goods = [r for r in week_rows if r['pass_fail'] == 'PASS' and r['D1'] >= 4
             and r['turns'] >= 8]
    goods.sort(key=lambda r: -r['score5'])
    good = goods[0] if goods else None

    bads = [r for r in week_rows if r['pass_fail'] == 'FAIL' and r['D1'] <= 3]
    bads.sort(key=lambda r: (r['D1'], r['score5']))
    bad = bads[0] if bads else None

    slide10 = [
        '# Slide 10 — One good, one bad', '',
        f'Week of {ws.strftime("%b %-d")} – {we.strftime("%b %-d")}  ',
        '*Scored under the re-anchored rubric (effective 2026-05-13).*', '',
    ]
    if good:
        slide10 += [
            '## Good', good['notes'][:300], '',
            f'[{good["conv_id"]}]({aiconsole(good["conv_id"])})', '',
            f'*(score {good["score5"]:.2f}/5, {good["turns"]} turns, {" → ".join(good["tasks"])})*', '',
        ]
    else:
        slide10 += ['## Good', 'No clean PASS scenario found this week.', '']

    if bad:
        slide10 += [
            '## Bad', bad['notes'][:300], '',
            f'[{bad["conv_id"]}]({aiconsole(bad["conv_id"])})', '',
            f'*(score {bad["score5"]:.2f}/5, D1={bad["D1"]}, {bad["turns"]} turns, {" → ".join(bad["tasks"])})*', '',
        ]
    else:
        slide10 += ['## Bad', 'No FAIL scenario found this week.', '']

    (out_dir / 'slide_10_good_bad.md').write_text('\n'.join(slide10))

    print(f'Output: {out_dir}')
    for fn in sorted(out_dir.iterdir()):
        print(f'  {fn.name}')
    print(f'\nWeek of {week_start}: pass {w["pass_rate_pct"]:.1f}%, score {w["mean_score_5"]:.2f}/5')
    print(f'Since Apr 18:        pass {b["pass_rate_pct"]:.1f}%, score {b["mean_score_5"]:.2f}/5')


if __name__ == '__main__':
    main()
