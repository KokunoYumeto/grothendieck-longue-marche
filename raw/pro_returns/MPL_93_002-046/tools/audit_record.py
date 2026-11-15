from pathlib import Path
from datetime import datetime,timezone
import csv
ROOT=Path(__file__).resolve().parents[1]
def audit(scan,changes=(),note='',doubts=(),items=()):
    page=ROOT/'pages'/f'MPL_93_002-046_93_scan{scan:03}.tex'
    text=page.read_text()
    for before,after in changes:
        if before not in text:raise ValueError(f'{scan}: text not found: {before!r}')
        text=text.replace(before,after)
    if changes:page.write_text(text)
    if doubts:
        with (ROOT/'doubt_records.csv').open('a',newline='') as f:
            w=csv.writer(f)
            for row in doubts:w.writerow(['93',f'{scan:03}',*row])
    if items:
        inv=ROOT/'MPL_93_002-046_inventory.csv'
        with inv.open() as f:rows=list(csv.DictReader(f))
        old=[r for r in rows if int(r['scan'])==scan]
        with inv.open('a',newline='') as f:
            w=csv.writer(f)
            for i,(kind,pos,words) in enumerate(items,len(old)+1):w.writerow(['93',f'{scan:03}',old[0]['sheet_kind'],f'{scan:03}.{i:02}',kind,pos,words,'yes'])
    utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT/'progress.log').open('a') as f:
        if note:f.write(f'audit correction 93 scan {scan:03}: {note}\n')
        f.write(f'scan {scan:03} audited {utc}\n')
    print(f'Audited {scan:03}; {len(changes)} replacements.')
