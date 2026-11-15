from pathlib import Path
from datetime import datetime,timezone
import json,csv
B=Path(__file__).resolve().parents[1]
def change(n,a,b):
 p=B/'pages'/f'MPL_18_018-062_18_scan{n:03d}.tex'
 s=p.read_text(); assert a in s,(n,a);p.write_text(s.replace(a,b))
def doubt(n,pos,reading,alt='',confidence='medium'):
 with (B/'records/doubts.jsonl').open('a') as f:f.write(json.dumps(dict(cote=18,scan=n,position=pos,reading=reading,alternatives=alt,confidence=confidence),ensure_ascii=False)+'\n')
def item(n,kind,pos,words,sheet='text'):
 p=B/'MPL_18_018-062_inventory.csv'
 with p.open() as f:rows=list(csv.DictReader(f))
 i=max(int(r['element']) for r in rows if int(r['scan'])==n)+1
 with p.open('a',newline='') as f:csv.writer(f).writerow([18,n,sheet,i,kind,pos,words,'yes'])
def audited(n,note):
 now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 with (B/'progress.log').open('a') as f:f.write(f'scan {n:03d} audited {now}\n')
 with (B/'records/audit_observations.md').open('a') as f:f.write(f'## Scan {n:03d}\n\n{note}\n\n')
