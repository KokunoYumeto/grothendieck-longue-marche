from pathlib import Path
from datetime import datetime, timezone
import csv, json, re

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_66+68_002-032'

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def record(n, tex, elements, observations='', sheet_kind='text'):
    path = ROOT / 'pages' / f'{PREFIX}_68_scan{n:03d}.tex'
    if path.exists():
        raise RuntimeError(f'Page already recorded: {n}')
    tex = tex.strip() + '\n'
    if n == 2 and not tex.startswith('\\cotefile{68}'):
        raise RuntimeError('Missing cote')
    if f'\\scanpage{{{n}}}' not in tex:
        raise RuntimeError('Missing scan marker')
    path.write_text(tex)
    with (ROOT / f'{PREFIX}_inventory.csv').open('a', newline='') as f:
        w=csv.writer(f)
        for i,(kind,position,words) in enumerate(elements,1):
            w.writerow([68,n,sheet_kind,f'{n:03d}.{i:02d}',kind,position,words,'yes'])
    if observations:
        with (ROOT/'records'/'precontext_observations.md').open('a') as f:
            f.write(f'\n## Cote 68 scan {n:03d}\n\n{observations.strip()}\n')
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'68 scan {n:03d} done {utc()}\n')
    print(f'Saved scan {n:03d}: {len(tex)} characters, {len(elements)} inventory rows')
