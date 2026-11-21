"""Mechanical support for explicit main-reader edits after image inspection."""
from pathlib import Path
import csv,json
from audit_helpers import adjudicate
ROOT=Path(__file__).resolve().parents[1]
class AuditEdit:
 def __init__(self,scan):
  self.scan=f'{int(scan):03}';self.stem='150_scan'+self.scan
  self.pp=ROOT/'pages'/f'{self.stem}.tex';self.rp=ROOT/'records'/f'{self.stem}.json'
  self.text=self.pp.read_text();self.r=json.loads(self.rp.read_text());assert not self.r.get('audited')
  with (ROOT/'second'/f'{self.stem}_boxes.tsv').open() as f:self.boxes={x['box']:x for x in csv.DictReader(f,delimiter='\t')}
  self.comp={x['box']:x for x in json.loads((ROOT/'second'/f'{self.stem}_comparison.json').read_text())};self.decisions=[]
 def replace(self,old,new,count=1):
  assert self.text.count(old)==count,(self.scan,old,self.text.count(old),count)
  self.text=self.text.replace(old,new)
 def amend(self,cid,final,evidence,box,confidence='low',**updates):
  c=next(x for x in self.r['changes'] if x['id']==cid)
  c.setdefault('first_pass_evidence',c['evidence']);c.update(final=final,evidence=evidence,confidence=confidence,crop=f'crops/{self.stem}_second_{box}.png',box=[int(self.boxes[box][k]) for k in ['x0','y0','x1','y1']],**updates)
 def add(self,cid,place,C,H,final,evidence,box,against_C=False,against_H=False,kind='other',category='Other',confidence='low',marked_in_H=False):
  assert all(x['id']!=cid for x in self.r['changes'])
  self.r['changes'].append(dict(id=cid,place=place,C=C,H=H,final=final,evidence=evidence,crop=f'crops/{self.stem}_second_{box}.png',box=[int(self.boxes[box][k]) for k in ['x0','y0','x1','y1']],against_C=against_C,against_H=against_H,kind=kind,error_category=category,confidence=confidence,marked_in_H=marked_in_H,mathematical_consequence=''))
 def doubt(self,place,reading,alternatives,reason,confidence='low'):
  self.r['doubts'].append(dict(place=place,reading=reading,alternatives=alternatives,reason=reason,confidence=confidence))
 def keep(self,box,evidence,confidence='medium'):
  self.decisions.append(dict(box=box,choice='first',changed='no',evidence=evidence,confidence=confidence))
 def change(self,box,final,ids,evidence,confidence='low'):
  self.decisions.append(dict(box=box,choice='explicit',final=final,changed='yes',change_ids=ids,evidence=evidence,confidence=confidence))
 def note(self,text):self.r['notes'].append(dict(id=f'150-{self.scan}-AUD01',text=text))
 def save(self):
  assert {x['box'] for x in self.decisions}=={k for k,v in self.comp.items() if v['different']}
  self.pp.write_text(self.text);self.rp.write_text(json.dumps(self.r,ensure_ascii=False,indent=2)+'\n');adjudicate(self.scan,self.decisions)
