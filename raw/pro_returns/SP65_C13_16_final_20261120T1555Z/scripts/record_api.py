"""Compact authoring interface for manually established page evidence."""
import json,subprocess,sys
from pathlib import Path
from record import ROOT,SOURCE,utc,build,RECORDS
class Page:
 def __init__(self,n):
  self.n=n;self.p={'scan':n,'changes':[],'decisions':[],'inventory':[],'notes':'','doubts':[],'certainty':[],'hand':[],'notation':[],'checks':[],'abbreviations':[]};self.text=(SOURCE/'pages'/f'16_scan{n:03}.tex').read_text()
 def r(self,a,b):
  assert a in self.text,repr(a);self.text=self.text.replace(a,b)
 def ch(self,place,c,h,final,ink,flags='H',confidence='high',kind='misread word',error=2,marked='no',consequence=''):
  self.p['changes'].append(dict(place=place,c=c,h=h,final=final,ink=ink,dc='C' in flags,dh='H' in flags,confidence=confidence,kind=kind,error=error,marked_h=marked,consequence=consequence))
 def d(self,id,decision,reading,ink,crop='page',confidence='high'):
  self.p['decisions'].append([id,decision,reading,ink,crop,confidence])
 def inv(self,*rows):self.p['inventory'].extend(rows)
 def save(self):
  (ROOT/'pages'/f'16_scan{self.n:03}.tex').write_text(self.text.rstrip()+'\n')
  (RECORDS/f'{self.n:03}.json').write_text(json.dumps(self.p,ensure_ascii=False,indent=2)+'\n');build()
  with (ROOT/'progress.log').open('a') as f:f.write(f'scan {self.n:03} done {utc()} cote 16\n')
  print(f"Recorded {self.n:03}: {len(self.p['changes'])} changed loci, {len(self.p['decisions'])} decisions")
