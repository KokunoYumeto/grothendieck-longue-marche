"""Record a manually read page, its inventory and doubts, then its UTC completion."""
from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]

def record(scan, text, elements, doubts=(), leads=''):
    target = ROOT / 'pages' / f'MPL_2_2_scan{scan:03d}.tex'
    if target.exists():
        raise FileExistsError(target)
    target.write_text(text.strip()+'\n', encoding='utf-8')
    with (ROOT/'MPL_2_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        for i, item in enumerate(elements,1):
            sheet, kind, position, start=item
            w.writerow([2,scan,sheet,f'{scan:03d}-{i:02d}',kind,position,start,'yes'])
    with (ROOT/'MPL_2_doubts.md').open('a',encoding='utf-8') as f:
        for line,reading,alternatives,confidence in doubts:
            values=[2,scan,line,reading,alternatives,confidence]
            f.write('| '+' | '.join(str(x).replace('|',' / ') for x in values)+' |\n')
    if leads:
        with (ROOT/'records'/'research_leads.md').open('a',encoding='utf-8') as f:
            f.write(f'\n## Scan {scan:03d}\n\n{leads.strip()}\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'2 scan {scan:03d} done '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
    print(f'Saved scan {scan:03d}: {len(elements)} inventory elements; {len(doubts)} doubt records.')
