from pathlib import Path
from datetime import datetime, timezone
import csv
ROOT=Path(__file__).resolve().parents[1]
def audit(scan, changes=(), note='', sheet_kind=None):
    p=ROOT/'pages'/f'MPL_136_235-281_136_scan{scan:03}.tex'
    s=p.read_text()
    for old,new in changes:
        if old not in s: raise ValueError(f'{scan}: absent replacement {old!r}')
        s=s.replace(old,new)
    p.write_text(s)
    if sheet_kind:
        ip=ROOT/'MPL_136_235-281_inventory.csv'
        with ip.open(newline='') as f:
            r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
        for row in rows:
            if int(row['scan'])==scan: row['sheet_kind']=sheet_kind
        with ip.open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'scan {scan:03} audited {now}\n')
        if note: f.write(f'136 scan {scan:03} audit: {note}\n')
    print(f'scan {scan} audited {now}')
