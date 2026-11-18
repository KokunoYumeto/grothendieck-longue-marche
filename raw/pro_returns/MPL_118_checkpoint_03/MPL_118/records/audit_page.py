from pathlib import Path
from datetime import datetime, timezone
import csv
ROOT=Path(__file__).resolve().parents[1]
def audit(scan, replacements=(), note='', added_elements=()):
    p=ROOT/'pages'/f'MPL_118_118_scan{scan:03d}.tex'
    t=p.read_text()
    for old,new in replacements:
        if old not in t: raise ValueError(f'No match in scan {scan}: {old!r}')
        t=t.replace(old,new)
    p.write_text(t,encoding='utf-8')
    stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT/'progress.log').open('a') as f: f.write(f'scan {scan:03d} audited {stamp}\n')
    with (ROOT/'records/audit_notes.md').open('a') as f:
        f.write(f'\n## Scan {scan:03d} — {stamp}\n\n{note or "Compared personally against scan; no textual change."}\n')
        for old,new in replacements: f.write(f'\n- Changed `{old}` to `{new}`.\n')
    if added_elements:
        with (ROOT/'MPL_118_inventory.csv').open(newline='') as f: rows=list(csv.DictReader(f))
        n=sum(int(r['scan'])==scan for r in rows)
        kind=next(r['sheet_kind'] for r in rows if int(r['scan'])==scan)
        with (ROOT/'MPL_118_inventory.csv').open('a',newline='') as f:
            w=csv.writer(f)
            for m,(typ,pos,words) in enumerate(added_elements,n+1): w.writerow([118,scan,kind,f'{scan:03d}-{m:02d}',typ,pos,words,'yes'])
    print(f'Audited scan {scan:03d}, {len(replacements)} changes; {stamp}')
