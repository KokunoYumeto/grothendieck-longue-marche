# Root-authored recording convenience; no reading decisions are made by this module.
from pathlib import Path
import json, csv, re
ROOT=Path(__file__).resolve().parents[1]
W=ROOT.parent/'source/SP02_CW_10+12_witnesses'
class Record:
 def __init__(self,folder,cote,scan,kind='typescript'):
  self.r=dict(folder=folder,cote=str(cote),scan=scan,sheet_kind=kind,inventory_confirmed=True,inventory_from_C=True,edits=[],changes=[],remaining_doubts=[],notation_updates=[],crops=[],inventory_extra=[])
 def edit(self,old,new,count=None):
  e=dict(old=old,new=new)
  if count is not None:e['count']=count
  self.r['edits'].append(e)
 def change(self,place,C,H,final,shows,crop,kind='other',confidence='high',against_C=False,against_H=True,marked_in_H=False,consequential=False):
  self.r['changes'].append(dict(place=place,C=C,H=H,final=final,shows=shows,crop=crop,kind=kind,confidence=confidence,against_C=against_C,against_H=against_H,marked_in_H=marked_in_H,consequential=consequential))
 def doubt(self,line,reading,alternatives='',confidence='medium',comment=''):
  self.r['remaining_doubts'].append(dict(line=line,reading=reading,alternatives=alternatives,confidence=confidence,comment=comment))
 def crop(self,id,box,rotation=0,scale=2,**kw):
  r=self.r;name=f"{r['folder']}_{r['cote']}_scan{r['scan']:03d}.jpg"
  self.r['crops'].append(dict(id=id,source='SP02_CW_10+12_scans/'+name,box=box,rotation=rotation,scale=scale,**kw))
 def notation(self,sign,form,attestations,status='read'):
  self.r['notation_updates'].append(dict(sign=sign,form=form,attestations=attestations,status=status))
 def save(self,path):
  Path(path).write_text(json.dumps(self.r,ensure_ascii=False,indent=2))
