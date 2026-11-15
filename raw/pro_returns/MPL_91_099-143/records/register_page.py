from pathlib import Path
from datetime import datetime, timezone
import csv, json, sys

ROOT = Path(__file__).resolve().parents[1]

def register(scan, kind, elements, notes='', notation=''):
    page = ROOT / 'pages' / f'MPL_91_099-143_91_scan{scan:03}.tex'
    assert page.exists()
    with (ROOT / 'MPL_91_099-143_inventory.csv').open('a', newline='') as f:
        writer = csv.writer(f)
        for i, (k, pos, first) in enumerate(elements, 1):
            writer.writerow(['91', f'{scan:03}', kind, i, k, pos, first, 'yes'])
    if notes:
        with (ROOT / 'records/research_leads.md').open('a') as f:
            f.write(f'\n## Scan {scan:03}\n\n{notes}\n')
    if notation:
        with (ROOT / 'records/notation.md').open('a') as f:
            f.write(notation+'\n')
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT / 'progress.log').open('a') as f:
        f.write(f'91 scan {scan:03} done {now}\n')
    print(f'Saved scan {scan:03}; {len(elements)} inventory elements; {now}')

if __name__ == '__main__':
    register(**json.load(sys.stdin))
