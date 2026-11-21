"""Clerical serialization helpers. All readings and collation flags are supplied explicitly."""
from pathlib import Path
import csv,json
W=Path(__file__).resolve().parents[1]
class AuditRecord:
 def __init__(self,page):
  self.page=page;self.S=W/'second';self.r=json.loads((W/'reports'/page/'report.json').read_text())
  self.comp=json.loads((self.S/f'{page}_comparison.json').read_text());self.c={x['box']:x for x in self.comp}
  self.boxes={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((self.S/f'{page}_boxes.tsv').open(),delimiter='\t')}
  self.ds=[];self.ed=dict(source_replacements=[],report_updates=[],report_removals=[],report_appends={})
 def decide(self,b,e,final=None,outcome=None,crop=None):
  d=dict(box=b,decision='retain' if final is None else 'revise',evidence=e,outcome=outcome or ('First reading retained after personal crop inspection.' if final is None else 'Final source revised on the personally inspected crop.'))
  if final is not None:d['final']=final
  if crop:d['crop']=crop
  self.ds.append(d)
 def replace(self,old,new,count=1):self.ed['source_replacements'].append(dict(old=old,new=new,count=count))
 def update(self,collection,key,value,**fields):self.ed['report_updates'].append(dict(collection=collection,match={key:value},set=fields))
 def change(self,id,**fields):self.update('changes','id',id,**fields)
 def inventory(self,id,**fields):self.update('inventory','element',id,**fields)
 def append(self,collection,**row):self.ed['report_appends'].setdefault(collection,[]).append(row)
 def doubt(self,place,reading,alternatives,reason,confidence='low'):
  self.append('doubts',place=place,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason)
 def new_change(self,id,box,place,c,h,final,evidence,kind,against_c,against_h,confidence='medium',marked_in_h=False,consequential=False,error_category='1'):
  self.append('changes',id=id,place=place,c=c,h=h,final=final,evidence=evidence,crop=f'crops/{self.page}_second_{box}.png',box=self.boxes[box],confidence=confidence,kind=kind,against_c=against_c,against_h=against_h,marked_in_h=marked_in_h,consequential=consequential,error_category=error_category)
 def get(self,collection,key,value):return next(x for x in self.r[collection] if x[key]==value)
 def save(self):
  assert [x['box'] for x in self.ds]==[x['box'] for x in self.comp if not x['token_equal']]
  for suffix,data in [('root_decisions',self.ds),('edits',self.ed)]:
   p=self.S/f'{self.page}_{suffix}.json'
   if p.exists():raise RuntimeError('Already serialized '+str(p))
   p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
  print(self.page,len(self.ds),'decisions;',sum(x['decision']=='revise' for x in self.ds),'revised')
