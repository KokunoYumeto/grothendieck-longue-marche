from pathlib import Path
from datetime import datetime, timezone
import csv
ROOT=Path(__file__).resolve().parents[1]
def audit(scan, replacements=(), doubts=(), elements=()):
    p=ROOT/'pages'/f'MPL_93_092-134_93_scan{scan:03d}.tex'
    s=p.read_text()
    for old,new in replacements:
        if old not in s: raise ValueError(f'{scan}: missing replacement {old!r}')
        s=s.replace(old,new)
    p.write_text(s)
    if doubts:
        with (ROOT/'documentation/doubts_rows.tsv').open('a') as f:
            for line,reading,alt,conf in doubts:f.write('\t'.join(['93',str(scan),line,reading,alt,conf])+'\n')
    if elements:
        inv=ROOT/'MPL_93_092-134_inventory.csv'
        with inv.open(newline='') as f:rows=list(csv.DictReader(f))
        n=sum(r['scan']==str(scan) for r in rows)
        with inv.open('a',newline='') as f:
            w=csv.writer(f)
            for j,(kind,pos,words) in enumerate(elements,n+1):w.writerow(['93',scan,'text',f'{scan:03d}.{j:02d}',kind,pos,words,'yes'])
    stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03d} audited {stamp}\n')
    print(f'Audited scan {scan:03d}: {len(replacements)} edits, {len(doubts)} added doubts. {stamp}')
