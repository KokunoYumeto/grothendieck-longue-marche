"""Compact comparison of three saved reports, without adjudicating any reading."""
from pathlib import Path
import argparse,json,re,difflib
p=argparse.ArgumentParser();p.add_argument('scan',type=int);p.add_argument('--reports-only',action='store_true')
p.add_argument('--reader',choices=['R1','R2','R3'])
p.add_argument('--section',choices=['findings','inventory','metadata','manifest','reading'],default='findings')
p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=20)
p.add_argument('--texts-only',action='store_true');a=p.parse_args()
O=Path(__file__).resolve().parents[1];P=O/'readings'/f'scan{a.scan:03d}'
if a.reader:
 rp=P/a.reader
 if a.section=='reading':print((rp/'reading.tex').read_text())
 elif a.section=='manifest':print((rp/'crop_manifest.json').read_text())
 else:
  data=json.loads((rp/'report.json').read_text())
  if a.section=='metadata':
   for key,value in data.items():
    if key not in ('findings','inventory'):print(key,json.dumps(value,ensure_ascii=False))
  else:
   items=data[a.section];print(a.reader,a.section,'total',len(items),'range',a.start,a.start+a.count)
   for item in items[a.start:a.start+a.count]:print(json.dumps(item,ensure_ascii=False))
 raise SystemExit(0)
def norm(s):
 s=str(s).replace('’',"'").replace('′',"'").replace('\\,','').replace('\\text{','{').replace('\\mathrm{','{')
 return re.sub(r'[\s{}$]','',s)
def bbox(f):
 b=f.get('bbox');return b if isinstance(b,list) and len(b)==4 and all(isinstance(v,(int,float)) for v in b) else None
def overlap(f,g):
 b,c=bbox(f),bbox(g)
 if not b or not c:return True
 x=max(0,min(b[2],c[2])-max(b[0],c[0]));y=max(0,min(b[3],c[3])-max(b[1],c[1]))
 return x*y/max(1,min((b[2]-b[0])*(b[3]-b[1]),(c[2]-c[0])*(c[3]-c[1])))>=.15
def covered(f,g):
 return overlap(f,g) and all(norm(f.get(k,'')) in norm(g.get(k,'')) for k in ['c','h','final'])
rs={r:json.loads((P/r/'report.json').read_text()) for r in ['R1','R2','R3']}
base=(P/'R1/reading.tex').read_text()
if a.texts_only:
 print('BASE R1 COMPLETE READING\n'+base)
 for rn in ('R2','R3'):print(''.join(difflib.unified_diff(base.splitlines(True),(P/rn/'reading.tex').read_text().splitlines(True),fromfile='R1',tofile=rn)))
 raise SystemExit(0)
if not a.reports_only:print('BASE R1 COMPLETE READING\n'+base)
for rn in rs:
 r=rs[rn];print('\nREADER',rn,'crops',r.get('crop_count'),'findings',len(r['findings']))
 if rn!='R1':
  if not a.reports_only:print(''.join(difflib.unified_diff(base.splitlines(True),(P/rn/'reading.tex').read_text().splitlines(True),fromfile='R1',tofile=rn)))
  covered_ids=[]
 for f in r['findings']:
  if rn!='R1':
   match=next((g for g in rs['R1']['findings'] if covered(f,g)),None)
   if match:covered_ids.append(f['id']+'→'+match['id']);continue
  d={k:f.get(k) for k in ['id','place','c','h','final','confidence','diff_c','diff_h','crop','bbox','doubt_action','s_id']}
  for k in ['c','h','final']:
   if isinstance(d[k],str) and len(d[k])>650:d[k]=d[k][:650]+' … [full text in report]'
  print(json.dumps(d,ensure_ascii=False))
 if rn!='R1':print('Text-covered finding references:',', '.join(covered_ids))
 print('Unresolved:',json.dumps(r.get('unresolved',[]),ensure_ascii=False))
 print('Actual math checks:',json.dumps(r.get('checks',[]),ensure_ascii=False))
