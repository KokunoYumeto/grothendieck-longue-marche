"""Append the primary reader's page decisions and regenerate human-readable logs.
No OCR or image interpretation is performed by this script.
"""
from pathlib import Path
import csv,json,re,sys
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'source/SP66_C13_16+120+136_texts'
PREFIX='SP66_C13_16+120+136'
def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def readtsv(name):
 p=ROOT/name
 return list(csv.DictReader(p.open(),delimiter='\t')) if p.exists() else []
def append(name,fields,rows,delimiter='\t'):
 p=ROOT/name;exists=p.exists()
 with p.open('a',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter)
  if not exists:w.writeheader()
  w.writerows(rows)
def mdcell(s):return str(s).replace('|','&#124;').replace('\n','<br>')
def table(fields,rows):return '| '+' | '.join(fields)+' |\n|'+'|'.join('---' for _ in fields)+'|\n'+''.join('| '+' | '.join(mdcell(x) for x in r)+' |\n' for r in rows)
def addtext(name,title,body):
 p=ROOT/name
 with p.open('a') as f:f.write('\n## '+title+'\n\n'+body.strip()+'\n')
def commit(key,text,changes,marks,inventory,notes,checks=(),habits=(),notation=(),abbreviations=(),doubts=(),sheet='text',hand='his hand',certainty=()):
 cote,scan=key.split('_scan');scan=int(scan)
 p=ROOT/'pages'/f'{key}.tex'
 if p.exists():raise RuntimeError('Already committed '+key)
 if key in ['16_scan053','120_scan002','136_scan328']:text='\\cotefile{'+cote+'}\n'+text.lstrip()
 p.write_text(text.strip()+'\n')
 fields=['page','place','C','H','final','scan_shows','confidence','kind','diff_C','diff_H','marked_H','consequential','crop']
 rr=[]
 for c in changes:
  if len(c)!=12:raise ValueError((key,len(c),c))
  rr.append(dict(zip(fields,[key]+list(c))))
 append('CHANGE_LEDGER.tsv',fields,rr)
 original=list(csv.DictReader((SOURCE/'MARKS.tsv').open(),delimiter='\t'))
 expected=[x['id'] for x in original if x['cote']==cote and int(x['scan'])==scan]
 if [m[0] for m in marks]!=expected:raise ValueError(('marks order',key,expected,[m[0] for m in marks]))
 mf=['id','cote','scan','decision','reading','what the ink shows','crop','confidence']
 append('decisions.tsv',mf,[dict(zip(mf,[m[0],cote,str(scan)]+list(m[1:]))) for m in marks])
 inv=[]
 for i,x in enumerate(inventory,1):
  if isinstance(x,str):x=x.split('|',2)
  kind,position,words=x[:3];who=x[3] if len(x)>3 else hand
  inv.append(dict(zip(['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],[key,sheet,who,f'E{i:02}',kind,position,words,'yes'])))
 append(PREFIX+'_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inv,',')
 addtext(PREFIX+'_notes.md',key,notes)
 cf=['statement_id','date','who','type','outcome']
 append('CHECK_EVENTS.tsv',cf,[dict(zip(cf,[c[0],now(),'GPT-6 Astra Pro; effort not exposed; SP66 second-pass run',c[1],c[2]])) for c in checks])
 for habit in habits:addtext(PREFIX+'_hand_log.md',key,habit)
 append('NOTATION.tsv',['page','sign_or_form','reading_and_manuscript_form'],[{'page':key,'sign_or_form':x[0],'reading_and_manuscript_form':x[1]} for x in notation])
 append('ABBREVIATIONS.tsv',['page','form','expansion'],[{'page':key,'form':x[0],'expansion':x[1]} for x in abbreviations])
 append('DOUBTS.tsv',['page','place','reading','alternatives','confidence'],[dict(zip(['page','place','reading','alternatives','confidence'],[key]+list(x))) for x in doubts])
 certainty_fields=['page','place','C','final','ink','crop','confidence']
 certainty_rows=[]
 for x in certainty:
  if len(x)!=6:raise ValueError(('certainty row',key,len(x),x))
  certainty_rows.append(dict(zip(certainty_fields,[key]+list(x))))
 append('CERTAINTY.tsv',certainty_fields,certainty_rows)
 with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03} done {now()} cote {cote}\n')
 regenerate()
def regenerate():
 changes=readtsv('CHANGE_LEDGER.tsv'); inv=[]
 ip=ROOT/(PREFIX+'_inventory.csv')
 if ip.exists():inv=list(csv.DictReader(ip.open()))
 keys=list(dict.fromkeys(x['scan'] for x in inv))
 counts=[]
 for k in keys:
  rs=[r for r in changes if r['page']==k]
  counts.append([k,sum(r['diff_C']=='yes' for r in rs),sum(r['diff_H']=='yes' for r in rs),*[sum(r['confidence']==c for r in rs) for c in ['high','medium','low']]])
 totals=['TOTAL']+[sum(row[i] for row in counts) for i in range(1,6)]
 s='# Changes against witnesses C and H\n\nCounts are places, not changed characters. A row can differ from both witnesses. Pure macro and certainty changes are excluded. A recurring sign has separate rows when its occurrences are separately located. “page” means the whole or native-resolution half settled it. H’s editorial notes/page markers are not manuscript text.\n\n'+table(['Page','Against C','Against H','High','Medium','Low'],counts+[totals])
 s+='\n## Consequential corrections and retained slips\n\n'
 for r in changes:
  if r['consequential']:s+='- '+r['page']+', '+r['place']+': '+r['consequential']+'\n'
 for k in keys:
  rs=[r for r in changes if r['page']==k]
  s+='\n## '+k+'\n\n'+(table(['Place','C','H','Final','What the scan shows / crop','Confidence'],[[r['place'],r['C'],r['H'],r['final'],r['scan_shows']+' ['+r['crop']+']',r['confidence']] for r in rs]) if rs else 'No substantive differences from the available witnesses.\n')
  ds=[x for x in readtsv('DOUBTS.tsv') if x['page']==k]
  s+='\nUnresolved: '+('; '.join(x['place']+': '+x['reading'] for x in ds) if ds else 'none recorded')+'.\n'
  crops=sorted(set(r['crop'] for r in rs if r['crop']!='page')|set(r['crop'] for r in readtsv('decisions.tsv') if r['cote']+'_'+f"scan{int(r['scan']):03}"==k and r['crop']!='page'))
  crops += [x['page']+' ('+','.join(x[z] for z in ['x0','y0','x1','y1'])+')'+(' rotated '+x['rotation_degrees']+'°' if x['rotation_degrees']!='0.0' else '') for x in readtsv('CROP_LEDGER.tsv') if x['page']==k]
  crops=list(dict.fromkeys(crops))
  if crops:s+='\nCrop register (original-image pixel boxes): '+ '; '.join(crops)+'.\n'
 (ROOT/(PREFIX+'_changes.md')).write_text(s)
 cf=['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']
 with (ROOT/(PREFIX+'_collation.tsv')).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cf,delimiter='\t');w.writeheader()
  for r in changes:
   if r['diff_H']=='yes':
    cote,scan=r['page'].split('_scan')
    w.writerow(dict(zip(cf,[cote,str(int(scan)-1),str(int(scan)),r['place'],r['H'],r['C'],r['final'],r['scan_shows']+' ['+r['crop']+']',r['kind'],r['marked_H'],r['confidence']])))
 n=readtsv('NOTATION.tsv');d=readtsv('DOUBTS.tsv');a=readtsv('ABBREVIATIONS.tsv');dec=readtsv('decisions.tsv');cert=readtsv('CERTAINTY.tsv')
 s='# Notation table\n\n'+table(['Page','Sign or form','Reading and manuscript form'],[[x['page'],x['sign_or_form'],x['reading_and_manuscript_form']] for x in n])
 s+='\n# Remaining doubts\n\n'+table(['Page','Place','Reading','Alternatives','Confidence'],[[x[f] for f in ['page','place','reading','alternatives','confidence']] for x in d])
 s+='\n# Decisions on witness C’s doubt marks\n\nCertainty-only decisions are recorded here and in decisions.tsv, not counted as textual changes.\n\n'+table(['ID','Page','Decision','Reading','Confidence'],[[x['id'],x['cote']+'_scan'+x['scan'].zfill(3),x['decision'],x['reading'],x['confidence']] for x in dec])
 s+='\n# Other certainty-only decisions\n\nResolved uncertainty wrappers outside MARKS.tsv are recorded here and in CERTAINTY.tsv, not counted as textual changes.\n\n'+table(['Page','Place','C','Final','What the ink shows','Crop','Confidence'],[[x[f] for f in ['page','place','C','final','ink','crop','confidence']] for x in cert])
 s+='\n# Abbreviations (expansions are editorial and never substituted into the transcription)\n\n'+table(['Page','Form','Possible expansion'],[[x['page'],x['form'],x['expansion']] for x in a])
 lf=ROOT/'LEGIBILITY.txt';s+='\n# Legibility and witnesses\n\n'+(lf.read_text() if lf.exists() else 'Reading in progress; final assessment will follow the second reading.\n')
 (ROOT/(PREFIX+'_doubts.md')).write_text(s)
 (ROOT/(PREFIX+'_transcription.tex')).write_text('\n'.join((ROOT/'pages'/(k+'.tex')).read_text() for k in keys))
if __name__=='__main__':regenerate()

def R(place,C,H,final,ink,kind='misread word',dc='no',dh='yes',conf='high',crop='page',marked='no',con=''):
 return (place,C,H,final,ink,conf,kind,dc,dh,marked,con,crop)
