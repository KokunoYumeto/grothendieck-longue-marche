from pathlib import Path
from datetime import datetime, timezone
import csv, json, sys

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_15_170-194r'

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def record(scan, tex, elements, sheet_kind='text', observations=''):
    path = ROOT/'pages'/f'{PREFIX}_15_scan{scan:03}.tex'
    if path.exists():
        raise RuntimeError(f'Page already recorded: {scan}; revise explicitly.')
    path.write_text(tex.rstrip()+'\n', encoding='utf-8')
    with (ROOT/f'{PREFIX}_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        for k,e in enumerate(elements,1):
            kind,position,words=e
            w.writerow(['15',scan,sheet_kind,f'{scan}-{k:02}',kind,position,words,'yes'])
    if observations:
        with (ROOT/'records/reading_observations.md').open('a',encoding='utf-8') as f:
            f.write(f'\n## Scan {scan}\n\n{observations.strip()}\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'15 scan {scan:03} done {utc()}\n')
    print(f'Saved scan {scan}: {len(tex)} characters; {len(elements)} inventory elements.')

if __name__=='__main__':
    record(**json.load(sys.stdin))
