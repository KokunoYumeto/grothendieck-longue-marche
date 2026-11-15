"""Save a visually transcribed page and its manually supplied inventory.

No image processing, OCR, inference, or automatic manuscript transcription.
Input on stdin is a JSON object supplied by the human-readable tool call.
"""
import csv
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_33_050-097'

def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def main():
    p = json.load(sys.stdin)
    n = int(p['scan'])
    target = ROOT / 'pages' / f'{PREFIX}_33_scan{n:03d}.tex'
    if target.exists():
        raise SystemExit(f'Refusing to replace saved page: {target}')
    expected = 50 + len(list((ROOT/'pages').glob('*.tex')))
    if n != expected:
        raise SystemExit(f'Expected scan {expected}, received {n}')
    tex = p['tex'].rstrip() + '\n'
    assert f'\\scanpage{{{n}}}' in tex
    target.write_text(tex, encoding='utf-8')
    with (ROOT/f'{PREFIX}_inventory.csv').open('a', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        for j, item in enumerate(p['inventory'], 1):
            kind, position, beginning = item
            assert kind in ['text','display','diagram','drawing','margin note','insertion','deletion']
            w.writerow(['33',n,p.get('sheet_kind','text'),f'{n:03d}.{j:02d}',kind,position,beginning,'yes'])
    with (ROOT/'records'/'doubt_details.md').open('a', encoding='utf-8') as f:
        f.write(f'\n## Scan {n:03d}\n\n')
        for d in p.get('doubts',[]):
            f.write('- '+d+'\n')
    with (ROOT/'records'/'research_leads.md').open('a', encoding='utf-8') as f:
        f.write(f'\n## Scan {n:03d}\n\n')
        for d in p.get('leads',[]):
            f.write('- '+d+'\n')
    with (ROOT/'progress.log').open('a', encoding='utf-8') as f:
        f.write(f'33 scan {n:03d} done {now()}\n')
    print(f'Saved scan {n:03d}: {len(p["inventory"])} inventory elements; {len(tex)} characters.')

if __name__ == '__main__':
    main()
