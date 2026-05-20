"""Aggregate LLM-judge scores into per-conv rows and period summaries.

Reads per-conv JSON files from data/scores/ and conversation JSONs from
data/conversations/CallerIdentification/.

Writes:
  data/all_scored_rows.json  — one row per scored conversation
  data/aggregates.json       — summary stats (all, baseline Apr 18+, week, daily)

Usage:
  python scripts/aggregate_scores.py [--week-start YYYY-MM-DD --week-end YYYY-MM-DD]

If --week-start/--week-end are omitted, the most recent complete Mon–Sat week is used.
"""
import json, glob, argparse
from pathlib import Path
from datetime import date, timedelta
from collections import defaultdict
from statistics import mean, stdev

REPO = Path(__file__).parent.parent
SCORES_DIR = REPO / 'data' / 'scores'
DATA = REPO / 'data' / 'conversations' / 'CallerIdentification'
ROWS_OUT = REPO / 'data' / 'all_scored_rows.json'
AGG_OUT = REPO / 'data' / 'aggregates.json'

WEIGHTS = {
    'D1': 0.20, 'D2': 0.10, 'D3': 0.10, 'D4': 0.10, 'D5': 0.08, 'D6': 0.07,
    'D8': 0.05, 'D9': 0.05, 'D10': 0.05, 'D12': 0.10,
}

FRUSTRATION_KW = [
    "kept asking", "loop", "circles", "stuck", "refused", "never transferred",
    "never escalated", "didn't escalate", "ended without", "ended call when",
    "wrong info", "dismissed", "couldn't connect", "false transfer", "abandon",
    "frustrat", "told customer to call", "couldn't authenticate", "looped",
    "unable to assist further", "kept saying unable", "stuck in loop",
    "failed 6+", "kept refusing", "answered specific question instead",
]


def conv_date(conv_id):
    fp = DATA / f'platform::assurantauto::{conv_id}::.json'
    with open(fp) as f:
        d = json.load(f)
    ts = (d['model_input']['actions'] or [{}])[0].get('timestamp', '')[:10]
    return ts or None


def n_turns_voice(conv_id):
    fp = DATA / f'platform::assurantauto::{conv_id}::.json'
    with open(fp) as f:
        d = json.load(f)
    return sum(
        1 for a in d['model_input']['actions']
        if a.get('type') == 'message' and a.get('source_system') == 'voice_assistant'
    )


def compute_weighted(scores):
    total = wsum = 0.0
    for dim, w in WEIGHTS.items():
        v = scores.get(dim)
        if isinstance(v, (int, float)):
            total += v * w
            wsum += w
    return total / wsum if wsum else None


def is_frustrated(s):
    if any(f == 'ABANDONED' for f in (s.get('flags') or [])):
        return True
    if s.get('D1') == 1:
        return True
    notes = (s.get('notes') or '').lower()
    return any(kw in notes for kw in FRUSTRATION_KW)


def classify(s):
    return 'PASS' if s.get('D1', 0) >= 4 and not is_frustrated(s) else 'FAIL'


def summarize(rs):
    if not rs:
        return None
    passes = sum(1 for r in rs if r['pass_fail'] == 'PASS')
    ws = [r['score5'] for r in rs if r['score5'] is not None]
    return {
        'n': len(rs),
        'pass_count': passes,
        'fail_count': len(rs) - passes,
        'pass_rate_pct': 100 * passes / len(rs),
        'mean_score_5': mean(ws),
        'std_score_5': stdev(ws) if len(ws) > 1 else 0,
        'mean_score_100': round(mean(ws) / 5 * 100),
        'pct_below_3': 100 * sum(1 for v in ws if v < 3.0) / len(ws),
        'safety_flags': sum(1 for r in rs if 'SAFETY_VIOLATION' in r['flags']),
        'hallucination_flags': sum(1 for r in rs if 'CRITICAL_HALLUCINATION' in r['flags']),
        'abandoned': sum(1 for r in rs if 'ABANDONED' in r['flags']),
        'dim_means': {
            dim: mean(r[dim] for r in rs if r.get(dim) is not None)
            for dim in WEIGHTS
        },
    }


def daily_summary(rs):
    d = defaultdict(list)
    for r in rs:
        if r.get('date'):
            d[r['date']].append(r)
    out = {}
    for dt in sorted(d):
        group = d[dt]
        passes = sum(1 for r in group if r['pass_fail'] == 'PASS')
        ws = [r['score5'] for r in group if r['score5'] is not None]
        out[dt] = {
            'total': len(group),
            'pass': passes,
            'pass_rate_pct': 100 * passes / len(group),
            'mean_score_5': mean(ws) if ws else 0,
            'mean_score_100': round(mean(ws) / 5 * 100) if ws else 0,
        }
    return out


def current_week():
    today = date.today()
    end = today - timedelta(days=1)       # yesterday (Saturday)
    start = end - timedelta(days=6)        # prior Sunday … but report uses Mon-Sat
    # Align to Mon-Sat: find most recent Saturday
    # end is already yesterday; ensure it's Saturday (weekday 5)
    while end.weekday() != 5:
        end -= timedelta(days=1)
    start = end - timedelta(days=5)        # Monday
    return str(start), str(end)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--week-start', default=None)
    ap.add_argument('--week-end', default=None)
    args = ap.parse_args()

    week_start, week_end = args.week_start, args.week_end
    if not week_start or not week_end:
        week_start, week_end = current_week()

    rows = []
    for fp in sorted(SCORES_DIR.glob('*.json')):
        with open(fp) as f:
            d = json.load(f)
        cid = d['conv_id']
        if d.get('force_skip') or not d.get('scores'):
            continue
        s = d['scores']
        ws = compute_weighted(s)
        row = {
            'conv_id': cid,
            'date': conv_date(cid),
            'turns': n_turns_voice(cid),
            'tasks': d.get('tasks', []),
            **{dim: s.get(dim) for dim in WEIGHTS},
            'flags': s.get('flags') or [],
            'notes': s.get('notes', ''),
            'score5': round(ws, 2) if ws is not None else None,
            'score100': round(ws / 5 * 100) if ws is not None else None,
            'pass_fail': classify(s),
        }
        rows.append(row)

    print(f'Scored rows: {len(rows)}')

    baseline = [r for r in rows if r['date'] and r['date'] >= '2026-04-18']
    week = [r for r in rows if r['date'] and week_start <= r['date'] <= week_end]
    print(f'Baseline (Apr 18 onward): {len(baseline)}')
    print(f'Week ({week_start} – {week_end}): {len(week)}')

    agg = {
        'week_start': week_start,
        'week_end': week_end,
        'all_scored': summarize(rows),
        'baseline': summarize(baseline),
        'week': summarize(week),
        'week_daily': daily_summary(week),
        'baseline_daily': daily_summary(baseline),
    }

    with open(ROWS_OUT, 'w') as f:
        json.dump(rows, f, indent=1)
    with open(AGG_OUT, 'w') as f:
        json.dump(agg, f, indent=2, default=str)

    for k in ('all_scored', 'baseline', 'week'):
        a = agg[k]
        if not a:
            continue
        print(f'\n== {k} (n={a["n"]}) ==')
        print(f'  Pass rate: {a["pass_count"]}/{a["n"]} = {a["pass_rate_pct"]:.1f}%')
        print(f'  Mean score: {a["mean_score_5"]:.2f}/5 ({a["mean_score_100"]}/100)')
        print(f'  < 3.0: {a["pct_below_3"]:.0f}%')
        print(f'  Safety/Halluc/Abandoned: {a["safety_flags"]}/{a["hallucination_flags"]}/{a["abandoned"]}')


if __name__ == '__main__':
    main()
