from pathlib import Path
from datetime import datetime, timezone
import csv
ROOT=Path(__file__).resolve().parents[1]
def audit(scan,replacements=(),doubts=(),extra_elements=(),note='Second visual reading completed against the scan.'):
    p=ROOT/'pages'/f'MPL_64_078-115_64_scan{scan:03d}.tex'
    s=p.read_text()
    for a,b in replacements:
        if a not in s: raise ValueError(f'Expected text missing in {scan}: {a!r}')
        s=s.replace(a,b)
    if replacements:p.write_text(s)
    with (ROOT/'MPL_64_078-115_doubts.md').open('a') as f:
        for pos,reading,alternative,conf in doubts:
            vals=['64',str(scan),pos,reading,alternative,conf]
            f.write('| '+' | '.join(x.replace('|',' / ').replace('\n',' ') for x in vals)+' |\n')
    if extra_elements:
        with (ROOT/'MPL_64_078-115_inventory.csv').open() as f:rows=list(csv.DictReader(f))
        n=sum(int(r['scan'])==scan for r in rows)
        with (ROOT/'MPL_64_078-115_inventory.csv').open('a',newline='') as f:
            w=csv.writer(f)
            for j,(kind,pos,first) in enumerate(extra_elements,n+1):w.writerow([64,scan,'text',f'{scan:03d}-{j:02d}',kind,pos,first,'yes'])
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'scan {scan:03d} audited {now}\n')
    with (ROOT/'records'/'audit_notes.tsv').open('a') as f:f.write(f'{scan:03d}\t{now}\t{len(replacements)}\t{note}\n')
    print(f'Audited {scan:03d}; {len(replacements)} explicit edits.')
