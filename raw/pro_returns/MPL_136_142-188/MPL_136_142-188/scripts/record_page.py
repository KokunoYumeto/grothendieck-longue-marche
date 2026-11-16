from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def record(n, tex, elements, doubts=(), observations='', sheet_kind='text'):
    page = ROOT / 'pages' / f'MPL_136_142-188_136_scan{n:03}.tex'
    if page.exists():
        raise RuntimeError(f'Page already exists: {page}')
    page.write_text(tex.strip()+'\n', encoding='utf-8')
    with (ROOT/'MPL_136_142-188_inventory.csv').open('a', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        for i, (kind, position, first) in enumerate(elements, 1):
            w.writerow([136,n,sheet_kind,f'{n}.{i:02}',kind,position,first,'yes'])
    with (ROOT/'records'/'doubts_rows.md').open('a', encoding='utf-8') as f:
        for line, reading, alternative, confidence in doubts:
            vals = [str(136),str(n),line,reading,alternative,confidence]
            f.write('| '+' | '.join(v.replace('|','\\|').replace('\n',' ') for v in vals)+' |\n')
    if observations:
        with (ROOT/'records'/'pre_context_observations.md').open('a', encoding='utf-8') as f:
            f.write(f'\n## Scan {n}\n\n{observations}\n')
    with (ROOT/'progress.log').open('a', encoding='utf-8') as f:
        f.write(f'136 scan {n:03} done {utc()}\n')
    print(f'Saved scan {n}: {len(elements)} inventory elements.')
