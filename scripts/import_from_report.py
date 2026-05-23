"""Parse per-conv score table from a historical markdown report and merge into all_scored_rows.json."""
import json, re, sys
from pathlib import Path

REPO = Path(__file__).parent.parent
OUT = REPO / 'data' / 'all_scored_rows.json'

WEIGHTS = {'D1':0.20,'D2':0.10,'D3':0.10,'D4':0.10,'D5':0.08,'D6':0.07,
           'D8':0.05,'D9':0.05,'D10':0.05,'D12':0.10}
DIMS = list(WEIGHTS.keys())

def weighted_score(row):
    return round(sum(row[d] * WEIGHTS[d] for d in DIMS), 2)

FRUSTRATION_KW = ["kept asking","loop","circles","stuck","refused","never transferred",
    "never escalated","didn't escalate","ended without","ended call when","wrong info",
    "dismissed","couldn't connect","false transfer","abandon","frustrat","told customer to call",
    "couldn't authenticate","looped","unable to assist further","kept saying unable",
    "stuck in loop","failed 6+","kept refusing","answered specific question instead"]

def classify(row):
    frustrated = (
        'ABANDONED' in row.get('flags', []) or
        row.get('D1') == 1 or
        any(kw in (row.get('notes') or '').lower() for kw in FRUSTRATION_KW)
    )
    return 'PASS' if row.get('D1', 0) >= 4 and not frustrated else 'FAIL'

def parse_report(path, year='2026'):
    rows = []
    # Pattern: | [CONV N](url) | MM-DD | turns | D1 D2 D3 D4 D5 D6 D8 D9 D10 D12 | score | P/F | flags |
    pattern = re.compile(
        r'\[CONV \d+\]\(https://[^)]+/externalConversationIds/([^?]+)\?[^)]*\)'
        r'\s*\|\s*(\d{2}-\d{2})\s*\|\s*(\d+)\s*\|'
        r'\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|'
        r'\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|'
        r'\s*[\d.]+ \(\d+\)\s*\|\s*([✓✗] (?:PASS|FAIL))\s*\|\s*([^|]*)\|'
    )
    text = Path(path).read_text()
    for m in pattern.finditer(text):
        conv_id = m.group(1)
        date = f'{year}-{m.group(2)}'
        turns = int(m.group(3))
        d1,d2,d3,d4,d5,d6,d8,d9,d10,d12 = [int(m.group(i)) for i in range(4,14)]
        flags_raw = m.group(15).strip()
        flags = []
        if 'ABANDONED' in flags_raw: flags.append('ABANDONED')
        if 'SAFETY' in flags_raw: flags.append('SAFETY_VIOLATION')
        if 'HALLUC' in flags_raw: flags.append('CRITICAL_HALLUCINATION')
        row = dict(conv_id=conv_id, date=date, turns=turns, tasks=['CallerIdentification'],
                   D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6, D8=d8, D9=d9, D10=d10, D12=d12,
                   flags=flags, notes='')
        row['score5'] = weighted_score(row)
        row['score100'] = round(row['score5'] / 5 * 100)
        row['pass_fail'] = classify(row)
        rows.append(row)
    return rows

if __name__ == '__main__':
    report_path = sys.argv[1]
    new_rows = parse_report(report_path)
    print(f'Parsed {len(new_rows)} rows from {report_path}')

    existing = json.loads(OUT.read_text()) if OUT.exists() else []
    existing_ids = {r['conv_id'] for r in existing}
    added = [r for r in new_rows if r['conv_id'] not in existing_ids]
    print(f'New (not already in all_scored_rows): {len(added)}')

    merged = added + existing
    merged.sort(key=lambda r: r['date'])
    OUT.write_text(json.dumps(merged, indent=2))
    print(f'Total rows now: {len(merged)}')
    dates = sorted(set(r['date'] for r in merged))
    print(f'Date range: {dates[0]} to {dates[-1]}')
