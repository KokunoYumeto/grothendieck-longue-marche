from pathlib import Path
import csv,json,hashlib,re
from datetime import datetime,timezone
from PIL import Image,ImageOps,ImageEnhance,ImageFilter
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'output'; SRC=ROOT/'source'; STEM='SP69_C13_141+142'
ORDER=['141_scan015','141_scan016']+['142_scan%03d'%n for n in [2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,24,25]]
def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def log(t):
 with (OUT/'progress.log').open('a') as f:f.write(t+'\n')
def prep(key):
 im=Image.open(SRC/(STEM+'_scans')/(key+'.jpg'));w,h=im.size
 d=ROOT/'views';d.mkdir(exist_ok=True)
 for label,box in [('top',(0,0,w,round(h*.55))),('bottom',(0,round(h*.45),w,h))] if h>=w else [('left',(0,0,round(w*.55),h)),('right',(round(w*.45),0,w,h))]:
  target=d/(key+'_'+label+'.png')
  if not target.exists():im.crop(box).save(target)
 print(key,im.size)
 t=SRC/(STEM+'_texts')
 print('C:\n'+(t/'pages'/(key+'.tex')).read_text())
 hp=t/'hua'/('hua_'+key+'.tex')
 print('H:\n'+(hp.read_text() if hp.exists() else '[absent]'))
 for m in csv.DictReader((t/'MARKS.tsv').open(),delimiter='\t'):
  if key=='%s_scan%03d'%(m['cote'],int(m['scan'])): print(m['id'],m['the mark as written'],m['the LaTeX around it'])
def crop(key,label,box,angle=0):
 d=ROOT/'views';target=d/(key+'_'+label+'.png')
 if target.exists():raise ValueError('No recropping: '+str(target))
 im=Image.open(SRC/(STEM+'_scans')/(key+'.jpg')).crop(box)
 im=ImageOps.autocontrast(im)
 if angle:im=im.rotate(angle,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
 factor=max(2, min(8, 2400/im.width))
 im=im.resize((round(im.width*factor),round(im.height*factor)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.4,percent=130,threshold=3))
 im.save(target)
 with (OUT/'crop_register.tsv').open('a') as f:f.write('\t'.join([key,label,','.join(map(str,box)),str(angle)])+'\n')
 return str(target)
def write_table(path,headers,rows,delimiter='\t'):
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=headers,delimiter=delimiter,extrasaction='ignore');w.writeheader();w.writerows(rows)
def esc(v):return str(v).replace('|','&#124;').replace('\n',' ')
def mdtable(headers,rows):return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join(['---']*len(headers))+'|']+['| '+' | '.join(esc(v) for v in r)+' |' for r in rows])+'\n'
def save(key,tex,data):
 (OUT/'pages'/(key+'.tex')).write_text(tex.rstrip()+'\n')
 data['key']=key
 (OUT/'records'/(key+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 rebuild()
 log('scan '+key[-3:]+' done '+utc()+' cote '+key[:3])
def rebuild():
 records=[json.loads((OUT/'records'/(k+'.json')).read_text()) for k in ORDER if (OUT/'records'/(k+'.json')).exists()]
 (OUT/(STEM+'_transcription.tex')).write_text('\n'.join((OUT/'pages'/(r['key']+'.tex')).read_text().rstrip() for r in records)+'\n')
 changes=[];coll=[];decs=[];inventory=[];checks=[];notes=[];hands=[];notations=[];abbr=[];doubts=[];certainty=[];stats=[];cons=[]
 cropmap={}
 if (OUT/'crop_register.tsv').exists():
  for row in csv.reader((OUT/'crop_register.tsv').open(),delimiter='\t'):
   if len(row)==4:cropmap.setdefault(row[0],[]).append(row)
 for r in records:
  k=r['key'];cc=hh=0;conf={c:0 for c in ['high','medium','low']}
  rows=[]
  for i,c in enumerate(r.get('changes',[]),1):
   c.setdefault('id',k+'-C%02d'%i);cc+=bool(c.get('against_C'));hh+=bool(c.get('against_H'));conf[c['confidence']]+=1;changes.append((k,c))
   evidence=c['ink']+' ['+c.get('crop','page / full-resolution halves')+']'
   rows.append([c['id']+' '+c['place'],c['C'],c.get('H','—'),c['final'],evidence,c['confidence']])
   if c.get('consequential'):cons.append('- '+k+', '+c['place']+': '+c['consequential'])
   if c.get('against_H'):coll.append(dict(folder=k[:3],their_page=str(int(k[-3:])-1),our_scan=str(int(k[-3:])),line=c['place'],their_reading=c['H'],codex_reading=c['C'],final_reading=c['final'],scan_shows=evidence,kind=c['kind'],marked_in_H=c.get('marked_in_H','no'),confidence=c['confidence']))
  stats.append([k,cc,hh,conf['high'],conf['medium'],conf['low']])
  notes.append('## '+k+'\n\n'+r.get('notes','')+'\n')
  hands.extend([[k]+list(x) for x in r.get('hand',[])])
  notations.extend([[k]+list(x) for x in r.get('notation',[])])
  abbr.extend([[k]+list(x) for x in r.get('abbreviations',[])])
  doubts.extend([[k]+list(x) for x in r.get('doubts',[])])
  for d in r.get('decisions',[]):
   d.update(cote=k[:3],scan=str(int(k[-3:])));decs.append(d)
   if d['decision']=='first':certainty.append([d['id'],k,d['reading'],d['what the ink shows'],d['confidence']])
  for n,e in enumerate(r.get('inventory',[]),1):
   inventory.append(dict(scan=k,sheet_kind=r.get('sheet_kind','text'),hand=e[0],element=str(n),kind=e[1],position=e[2],first_words_or_objects=e[3],transcribed='yes'))
  for c in r.get('checks',[]):
   c.setdefault('date',utc().split(' ')[0]);c.setdefault('who','GPT-6 Astra Pro; effort not exposed; second-pass run 2026-11-20');checks.append(c)
  segment='## '+k+'\n\n'+(mdtable(['Place','Witness C','Witness H','Final reading','What the scan shows / view','Confidence'],rows) if rows else 'No substantive differences from available witnesses.\n')
  segment+='\n### Unresolved\n\n'+('\n'.join('- '+str(x[0])+': '+str(x[1])+'; '+str(x[2])+' ('+str(x[3])+').' for x in r.get('doubts',[])) or 'None.')+'\n'
  if cropmap.get(k):segment+='\n### Crop register\n\n'+mdtable(['Scan','Place label','Original-pixel box (x0,y0,x1,y1)','Rotation degrees'],cropmap[k])
  r['_segment']=segment
 heads='# Changes against the two draft witnesses\n\nCounts are places, not individual characters. A row can differ from both witnesses. Certainty-only resolutions are recorded in decisions.tsv and the doubts file, not counted as textual changes. Macro syntax alone is excluded. H page = our scan minus one; absence of H is not an omission. Pixel boxes refer to the original supplied JPG. All reading decisions are by the primary reader; structural validation is not a manuscript reading.\n\n'
 totals=['TOTAL']+[sum(x[i] for x in stats) for i in range(1,6)]
 heads+=mdtable(['Scan','Changes against C','Changes against H','High','Medium','Low'],stats+[totals])
 heads+='\n## Consequential corrections\n\n'+('\n'.join(cons) or 'None recorded yet.')+'\n\n'
 (OUT/(STEM+'_changes.md')).write_text(heads+'\n'.join(r['_segment'] for r in records))
 write_table(OUT/(STEM+'_collation.tsv'),['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],coll)
 order={m['id']:i for i,m in enumerate(csv.DictReader((SRC/(STEM+'_texts')/'MARKS.tsv').open(),delimiter='\t'))}
 decs.sort(key=lambda d:order[d['id']]);write_table(OUT/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],decs)
 write_table(OUT/(STEM+'_inventory.csv'),['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory,',')
 write_table(OUT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome','place','statement'],checks)
 (OUT/(STEM+'_notes.md')).write_text('# Reading notes\n\nThese notes describe only the supplied pages. No external sources were consulted. A descriptive summary is not a proof check; CHECK_EVENTS.tsv distinguishes the actual checks performed from background statements.\n\n'+'\n'.join(notes))
 (OUT/(STEM+'_hand_log.md')).write_text('# Hand log\n\nObservations are entered in page order. Local evidence is not claimed to be universal; scope and exceptions are stated in each row.\n\n'+mdtable(['Page','Habit / notation','Scope and exceptions','Witness errors / places'],hands))
 (OUT/(STEM+'_doubts.md')).write_text('# Notation and remaining doubts\n\n## Notation table\n\n'+mdtable(['Page','Form / reading','How it is written; scope'],notations)+'\n## Remaining doubts\n\n'+mdtable(['Scan','Place','Reading retained','Alternatives / limitation','Confidence'],doubts)+'\n## Certainty-only decisions for C marks\n\n'+mdtable(['Mark','Scan','Reading','Ink evidence','Confidence'],certainty)+'\n## Abbreviations (expansions only here)\n\n'+mdtable(['Page','Abbreviation','Probable expansion'],abbr)+'\n## Legibility and witness comparison\n\n'+((OUT/'legibility.txt').read_text() if (OUT/'legibility.txt').exists() else 'Reading is in progress. The most crowded cancellations and minute sketch labels are explicitly left doubtful where the strokes do not distinguish a unique reading.')+'\n')
 kinds=['misread symbol or index','misread word','omission','drawing or diagram',r'readable ink left as \ill{}','insertion or placement','deletion state (struck given live or live given struck)','abbreviation expanded or spelling modernised','text not on the page','other']
 from collections import Counter
 ct=Counter(c['kind'] for _,c in changes)
 (OUT/(STEM+'_sheet_feedback.md')).write_text('# Feedback on the error sheet\n\nCounts are unique recorded places with substantive differences from C or H, classified by the primary error at that place; they are not a reclassification of every changed character. Certainty-only resolutions are counted separately below.\n\n'+mdtable(['Kind','Places'],[[x,ct[x]] for x in kinds])+'\nCertainty-only first-reading decisions: '+str(len(certainty))+'.\n\n## Additional recurring issues\n\n'+((OUT/'feedback_extra.txt').read_text() if (OUT/'feedback_extra.txt').exists() else 'No additional class has yet been established. See the hand log for page-specific habits.')+'\n')
 print('Rebuilt',len(records),'pages;',len(decs),'mark decisions;',len(changes),'change rows')
if __name__=='__main__':
 import sys
 if len(sys.argv)>1:prep(sys.argv[1])
 else:rebuild()
