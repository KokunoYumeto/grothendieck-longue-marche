from pathlib import Path
import datetime,json,csv
ROOT=Path(__file__).resolve().parents[1]
def audit(scan, changes=(), notes='', extras=(), doubts=()):
 p=ROOT/'pages'/f'MPL_36_002-052_36_scan{scan:03}.tex'
 s=p.read_text()
 for old,new in changes:
  assert old in s,(scan,old)
  s=s.replace(old,new)
 p.write_text(s)
 stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 with (ROOT/'records/audit_changes.jsonl').open('a') as f:f.write(json.dumps({'scan':scan,'utc':stamp,'changes':list(changes),'notes':notes},ensure_ascii=False)+'\n')
 if extras:
  ip=ROOT/'MPL_36_002-052_inventory.csv'
  rows=list(csv.DictReader(ip.open()))
  own=[r for r in rows if int(r['scan'])==scan]
  start=len(own)
  with ip.open('a',newline='') as f:
   w=csv.writer(f)
   for i,(kind,pos,incipit) in enumerate(extras,start+1):w.writerow([36,scan,own[0]['sheet_kind'],f'{scan:03}.{i:02}',kind,pos,incipit,'yes'])
 if doubts:
  with (ROOT/'records/doubts_rows.jsonl').open('a') as f:
   for r in doubts:f.write(json.dumps({'cote':36,'scan':scan,**r},ensure_ascii=False)+'\n')
 with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03} audited {stamp}\n')
 print(f'Audited {scan:03}; {len(changes)} revisions.')
