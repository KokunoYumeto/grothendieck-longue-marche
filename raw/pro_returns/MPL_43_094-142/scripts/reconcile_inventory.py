from pathlib import Path
import csv, json, sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from page_work import ROOT,PREFIX,FIELDS,utc
p=ROOT/f'{PREFIX}_inventory.csv'
record=ROOT/'records/inventory_reconciliation.json'
if record.exists():raise RuntimeError('Already reconciled')
rows=list(csv.DictReader(p.open(encoding='utf-8',newline='')))
moves={
 '094-16':'094-04','096-14':'096-08','098-21':'098-09','098-22':'098-15',
 '100-28':'100-01','104-22':'104-02','104-23':'104-12','108-32':'108-03',
 '110-36':'110-23','116-19':'116-09','130-32':'130-27','133-30':'133-21'
}
byid={r['element']:r for r in rows}
byafter={}
for added,anchor in moves.items():
 assert added in byid and anchor in byid
 byafter.setdefault(anchor,[]).append(byid[added])
ordered=[]
for r in rows:
 if r['element'] in moves:continue
 ordered.append(r)
 ordered.extend(byafter.get(r['element'],[]))
mapping=[]
counts={}
for r in ordered:
 old=r['element']; scan=int(r['scan'])
 counts[scan]=counts.get(scan,0)+1
 r['element']=f'{scan:03}-{counts[scan]:02}'
 if old!=r['element']:mapping.append({'old':old,'new':r['element'],'position':r['position']})
 if scan in (100,102):
  r['first_words_or_objects']=r['first_words_or_objects'].replace('gamma','sigma')
 if scan==130:
  r['first_words_or_objects']=r['first_words_or_objects'].replace('tau','sigma')
 if scan==116 and r['first_words_or_objects']=='DeltaT(P bullet) et T(Pprime bullet) sont =0':
  r['first_words_or_objects']='DeltaT(P bullet) et T(Pprime bullet) sont =Delta (0 alternative)'
 if scan==108 and r['kind']=='insertion' and r['position']=='above cancelled property':
  r['first_words_or_objects']='1/2 continue (both doubtful)'
 if scan==108 and r['kind']=='deletion' and r['position']=='upper sentence end':
  r['first_words_or_objects']='un (doubtful) voisinage'
assert len(ordered)==len(rows)
with p.open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(ordered)
record.write_text(json.dumps({'time':utc(),'reason':'Audit-added elements placed beside their observed anchors; first-words index reconciled to audited ink readings. No page text changed.','moves':moves,'renumbering':mapping,'rows':len(ordered)},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (ROOT/'progress.log').open('a',encoding='utf-8') as f:f.write('inventory reconciled '+utc()+'\n')
print(len(ordered),'inventory rows reconciled')

