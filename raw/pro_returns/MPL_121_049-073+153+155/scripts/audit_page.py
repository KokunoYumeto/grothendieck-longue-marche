#!/usr/bin/env python3
"""Record a second visual comparison and only the supplied, explicit corrections."""
import csv,json,sys
from pathlib import Path
from datetime import datetime,timezone
from record_page import ROOT,PREFIX,combine
v=json.load(sys.stdin); c,n=int(v['cote']),int(v['scan']); p=ROOT/'pages'/f'{PREFIX}_{c}_scan{n:03d}.tex'
s=p.read_text(); edits=[]
for old,new in v.get('replacements',[]):
 if s.count(old)!=1:raise RuntimeError(f'Expected one occurrence of {old!r}; found {s.count(old)}')
 s=s.replace(old,new,1); edits.append({'before':old,'after':new})
if 'tex' in v:s=v['tex'];edits.append({'whole_page_replaced':True})
p.write_text(s.rstrip()+'\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f:f.write(f'{c} scan {n:03d} audited {now}\n')
with (ROOT/'audit_records.jsonl').open('a') as f:f.write(json.dumps({'cote':c,'scan':n,'utc':now,'edits':edits,'note':v.get('note','')},ensure_ascii=False)+'\n')
for d in v.get('doubts',[]):
 with (ROOT/'doubt_records.jsonl').open('a') as f:f.write(json.dumps(dict(cote=str(c),scan=n,**d),ensure_ascii=False)+'\n')
if v.get('inventory'):
 inv=ROOT/f'{PREFIX}_inventory.csv'; rows=list(csv.DictReader(inv.open()))
 current=[r for r in rows if int(r['cote'])==c and int(r['scan'])==n]
 with inv.open('a',newline='') as f:
  w=csv.writer(f)
  for i,row in enumerate(v['inventory'],len(current)+1):w.writerow([c,n,current[0]['sheet_kind'],f'{c}-{n:03d}-{i:02d}',*row,'yes'])
combine();print(f'{c} scan {n:03d} audited, {len(edits)} explicit corrections.')
