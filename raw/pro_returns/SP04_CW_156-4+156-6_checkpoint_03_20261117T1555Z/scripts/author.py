"""Root-authored manual page records; this helper makes no reading decisions."""
from pathlib import Path
import csv,json,re
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'out'
MAP=list(csv.DictReader((ROOT/'witnesses/page_map.tsv').open(),delimiter='\t'))
class Page:
 def __init__(self,cote,scan):
  self.m=next(m for m in MAP if m['cote']==cote and int(m['our_scan'])==scan)
  self.cote=cote;self.scan=scan
  self.source=(ROOT/'witnesses'/self.m['codex_file']).read_text();self.text=self.source
  self.r=dict(cote=cote,scan=scan,changes=[],inventory=[],doubts=[],notation=[],abbreviations=[])
 def replace(self,a,b):
  assert a in self.text,(self.cote,self.scan,a)
  self.text=self.text.replace(a,b)
 def crop(self,name):return f'crops/{self.cote}_{self.scan:03}_{name}.jpg'
 def change(self,place,C,H,final,evidence,crop,dc=False,dh=True,kind='other',confidence='high',marked='no',consequential=''):
  self.r['changes'].append(dict(place=place,C=C,H=H,final=final,scan_shows=evidence,crop=self.crop(crop),differs_C=dc,differs_H=dh,kind=kind,confidence=confidence,marked_in_H=marked,consequential=consequential))
 def doubt(self,place,reading,reason,crop,confidence='medium'):
  self.r['doubts'].append(dict(line=place,reading=reading,alternatives=reading.split('|')[1:],confidence=confidence,comment=reason+'; crop '+self.crop(crop)))
 def inventory(self,items,sheet='text'):
  for k,p,w in items:self.r['inventory'].append(dict(element=f'E{len(self.r["inventory"])+1:02}',kind=k,position=p,first_words_or_objects=w,sheet_kind=sheet,hand='Grothendieck',transcribed='yes'))
 def notation(self,sign,latex,appearance,alternatives=''):
  self.r['notation'].append(dict(sign=sign,latex=latex,appearance=appearance,locations=f'{self.cote}:{self.scan:03}',alternatives=alternatives))
 def save(self):
  (OUT/'pages'/Path(self.m['codex_file']).name).write_text(self.text)
  (OUT/'records'/f'{self.cote}_scan{self.scan:03}.json').write_text(json.dumps(self.r,ensure_ascii=False,indent=2)+'\n')
  print(f'{self.cote} {self.scan}: saved manual text/record, {len(self.r["changes"])} change places, {len(self.r["inventory"])} inventory elements')
