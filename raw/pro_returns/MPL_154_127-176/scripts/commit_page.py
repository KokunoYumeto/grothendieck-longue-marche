from pathlib import Path
from datetime import datetime, timezone
import csv, json, sys, re

ROOT = Path(__file__).resolve().parents[1]
def stamp():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def commit(scan, elements, sheet_kind='text', observations=''):
    p = ROOT / 'pages' / f'MPL_154_127-176_154_scan{scan:03}.tex'
    if not p.is_file():
        raise RuntimeError('Write the page before committing it')
    with (ROOT/'MPL_154_127-176_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        for i,(kind,position,words) in enumerate(elements,1):
            writer.writerow([154,scan,sheet_kind,f'E{i:02}',kind,position,words,'yes'])
    if observations:
        with (ROOT/'records/reading_observations.md').open('a',encoding='utf-8') as f:
            f.write(f'\n## Scan {scan}\n\n{observations}\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'154 scan {scan:03} done {stamp()}\n')
    print(f'scan {scan}: saved; {len(elements)} inventory elements')

if __name__=='__main__':
    commit(**json.load(sys.stdin))
