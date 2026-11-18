from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def save(scan, text, sheet_kind, elements, observations=''):
    path = ROOT / 'pages' / f'MPL_118_118_scan{scan:03d}.tex'
    if path.exists():
        raise RuntimeError(f'Page already exists: {path}')
    if f'\\scanpage{{{scan}}}' not in text:
        raise ValueError('Missing scan marker')
    path.write_text(text.strip()+'\n', encoding='utf-8')
    with (ROOT/'MPL_118_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        for n,(kind,position,words) in enumerate(elements,1):
            w.writerow([118,scan,sheet_kind,f'{scan:03d}-{n:02d}',kind,position,words,'yes'])
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'118 scan {scan:03d} done {utc()}\n')
    if observations:
        with (ROOT/'records/pre_context_observations.md').open('a',encoding='utf-8') as f:
            f.write(f'\n## Scan {scan:03d}\n\n{observations}\n')
    print(f'Saved scan {scan:03d}: {len(text)} characters, {len(elements)} inventory elements; {utc()}')
