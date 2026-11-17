from pathlib import Path
from datetime import datetime,timezone
import csv,json
ROOT=Path(__file__).resolve().parent
PREFIX='MPL_68_033-056+162-1+162-6'
def audit(scan, changes=(), extra=(), doubts=(), comment=''):
    p=ROOT/'pages'/f'{PREFIX}_68_scan{scan:03}.tex'
    s=p.read_text()
    for old,new in changes:
        n=s.count(old)
        if n!=1: raise ValueError((scan,old,n))
        s=s.replace(old,new)
    p.write_text(s)
    inv=ROOT/f'{PREFIX}_inventory.csv'
    rows=list(csv.DictReader(inv.open()))
    count=sum(int(r['scan'])==scan for r in rows)
    with inv.open('a',newline='') as f:
        w=csv.writer(f)
        for i,(kind,pos,anchor) in enumerate(extra,count+1):
            kind_sheet=next(r['sheet_kind'] for r in rows if int(r['scan'])==scan)
            w.writerow(['68',scan,kind_sheet,f'{scan:03}-{i:02}',kind,pos,anchor,'yes'])
    with (ROOT/'doubts_rows.jsonl').open('a') as f:
        for pos,reading,alternatives,confidence in doubts:
            f.write(json.dumps(dict(cote='68',scan=scan,position=pos,reading=reading,alternatives=alternatives,confidence=confidence,audit=True),ensure_ascii=False)+'\n')
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT/'progress.log').open('a') as f:
        if comment: f.write(f'audit detail 68 scan {scan:03}: {comment}\n')
        f.write(f'scan {scan:03} audited {now}\n')
    print(f'Audited {scan:03}: {len(changes)} changes; {len(extra)} inventory additions.')
