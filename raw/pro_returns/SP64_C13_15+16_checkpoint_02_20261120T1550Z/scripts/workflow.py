from pathlib import Path
import csv,sys,hashlib
from datetime import datetime,timezone
from collections import Counter
from PIL import Image,ImageOps,ImageEnhance,ImageFilter
ROOT=Path(__file__).resolve().parents[2]
WORK=Path(__file__).resolve().parents[1]
SRC=ROOT/'source/SP64_C13_15+16_texts'
SCANS=ROOT/'source/SP64_C13_15+16_scans'
VIEWS=ROOT/'views'
PREFIX='SP64_C13_15+16'
ORDER=[('15',str(n)) for n in (180,183,184,185,187,189,190,191,192,193,194)]+[('16',f'{n:03}') for n in range(3,17)]
HEADERS={
 'decisions.tsv':['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],
 PREFIX+'_collation.tsv':['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],
 PREFIX+'_inventory.csv':['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],
 'CHECK_EVENTS.tsv':['statement_id','date','who','type','outcome'],
 'changes_records.tsv':['cote','scan','place','C','H','final','scan_shows','confidence','kind','against_C','against_H','crop','consequential'],
 'notation.tsv':['notation','written_form','scans'],
 'remaining_doubts.tsv':['scan','line','reading','alternatives','confidence'],
 'abbreviations.tsv':['form','expansion','scans']}
def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def readrows(name):
 p=WORK/name
 if not p.exists():return []
 return list(csv.DictReader(p.open(),delimiter=',' if name.endswith('.csv') else '\t'))
def write_rows(name,rows):
 with (WORK/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=HEADERS[name],delimiter=',' if name.endswith('.csv') else '\t');w.writeheader();w.writerows(rows)
def add(name,rows):
 old=readrows(name);write_rows(name,old+rows)
def log(line):
 with (WORK/'progress.log').open('a') as f:f.write(line+'\n')
def prepare(cote,scan):
 stem=f'{cote}_scan{scan}'
 im=Image.open(SCANS/(stem+'.jpg'))
 w,h=im.size
 boxes=[(0,0,w,round(h*.55)),(0,round(h*.45),w,h)] if h>=w else [(0,0,round(w*.55),h),(round(w*.45),0,w,h)]
 for k,b in enumerate(boxes,1):
  p=VIEWS/f'{stem}_half{k}.png'
  if not p.exists():im.crop(b).save(p)
 print('IMAGE',stem,im.size,'HALVES',boxes)
 print('C\n'+(SRC/'pages'/(stem+'.tex')).read_text())
 hp=SRC/'hua'/('hua_'+stem+'.tex')
 print('H\n'+(hp.read_text() if hp.exists() else '[No H text supplied]'))
 for r in csv.DictReader((SRC/'MARKS.tsv').open(),delimiter='\t'):
  if r['cote']==str(cote) and int(r['scan'])==int(scan):print(r)
def crop(cote,scan,box,label,angle=0,width=2800):
 stem=f'{cote}_scan{scan}'
 p=VIEWS/f'{stem}_crop_{label}.png'
 if p.exists():raise ValueError('A crop with this label already exists; do not recrop decided places.')
 im=Image.open(SCANS/(stem+'.jpg')).crop(box)
 im=ImageOps.autocontrast(im)
 if angle:im=im.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
 im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=130,threshold=3));im.save(p)
 log(f'crop {cote}/{scan} {tuple(box)} {label} rotation {angle}')
 print(p)
def mdcell(s):return str(s).replace('|','\\|').replace('\n','<br>')
def rebuild():
 import runpy
 reports=runpy.run_path(str(WORK/'scripts'/'report_helpers.py'))
 crop_register=reports['crop_register_markdown'](WORK)
 rows=readrows('changes_records.tsv')
 out=['# Changes and visual evidence','', 'Counts concern substantive reading differences. Certainty-only changes are recorded in decisions.tsv and the doubts file. A row may differ from both witnesses. No H comparison is counted on pages without supplied H text.','', '| Cote / scan | Against C | Against H | High | Medium | Low |','|---|---:|---:|---:|---:|---:|']
 totals=Counter()
 for c,s in ORDER:
  rr=[r for r in rows if r['cote']==c and r['scan']==s]
  if not (WORK/'pages'/f'{c}_scan{s}.tex').exists():continue
  counts=Counter({k:sum(r['confidence']==k for r in rr) for k in ('high','medium','low')})
  counts['C']=sum(r['against_C']=='yes' for r in rr);counts['H']=sum(r['against_H']=='yes' for r in rr);totals.update(counts)
  out.append(f'| {c}/{s} | {counts["C"]} | {counts["H"]} | {counts["high"]} | {counts["medium"]} | {counts["low"]} |')
 out+=['| **Total** | '+ ' | '.join(str(totals[k]) for k in ['C','H','high','medium','low'])+' |','','## Consequential corrections','']
 out += [f'- {r["cote"]}/{r["scan"]}, {r["place"]}: {r["consequential"]}' for r in rows if r['consequential']]
 doubts=readrows('remaining_doubts.tsv')
 for c,s in ORDER:
  if not (WORK/'pages'/f'{c}_scan{s}.tex').exists():continue
  out += [f'\n## Cote {c}, scan {s}\n','| Place | C | H | Final | What the scan shows | Confidence |','|---|---|---|---|---|---|']
  for r in rows:
   if r['cote']==c and r['scan']==s:
    evidence=r['scan_shows']+(f' Crop: {c}/{s} {r["crop"]}.' if r['crop'] and r['crop']!='page' else ' Settled from the full-resolution page halves.')
    out.append('| '+' | '.join(mdcell(v) for v in [r['place'],r['C'],r['H'],r['final'],evidence,r['confidence']])+' |')
  dd=[d for d in doubts if d['scan']==c+'/'+s]
  out+=['','Remaining unresolved places: '+('; '.join(d['line']+': `'+d['reading']+'`' for d in dd) if dd else 'none recorded.')]
 out+=['',crop_register]
 (WORK/(PREFIX+'_changes.md')).write_text('\n'.join(out)+'\n')
 combined=[]
 for c,s in ORDER:
  p=WORK/'pages'/f'{c}_scan{s}.tex'
  if p.exists():
   if not combined or c!=prev:combined.append('\\cotefile{'+c+'}\n')
   combined.append(p.read_text().rstrip()+'\n');prev=c
 (WORK/(PREFIX+'_transcription.tex')).write_text('\n'.join(combined))
 reports['rebuild_reports'](WORK)
def commit(cote,scan,text,changes,decisions,inventory,notes,hand='',notation=(),doubts=(),abbreviations=(),events=()):
 cote=str(cote);scan=str(scan);stem=f'{cote}_scan{scan}'
 p=WORK/'pages'/(stem+'.tex')
 if p.exists():raise ValueError('page already committed')
 allmarks=[r for r in csv.DictReader((SRC/'MARKS.tsv').open(),delimiter='\t') if r['cote']==cote and int(r['scan'])==int(scan)]
 assert [r['id'] for r in allmarks]==[d['id'] for d in decisions],([r['id'] for r in allmarks],[d['id'] for d in decisions])
 p.write_text(text.rstrip()+'\n')
 for d in decisions:d.update(cote=cote,scan=scan)
 add('decisions.tsv',decisions)
 cr=[];hr=[]
 for r in changes:
  r=dict(r);r.update(cote=cote,scan=scan)
  for k in HEADERS['changes_records.tsv']:r.setdefault(k,'')
  cr.append(r)
  if r['against_H']=='yes':hr.append(dict(zip(HEADERS[PREFIX+'_collation.tsv'],[cote,str(int(scan)-1),scan,r['place'],r['H'],r['C'],r['final'],r['scan_shows']+(' Crop '+str(r['crop']) if r['crop']!='page' else ' Page halves.'),r['kind'],r.get('marked_in_H','no'),r['confidence']])))
 add('changes_records.tsv',[{k:r[k] for k in HEADERS['changes_records.tsv']} for r in cr]);add(PREFIX+'_collation.tsv',hr)
 for i,r in enumerate(inventory,1):r.update(scan=cote+'/'+scan,element=str(i),transcribed='yes')
 add(PREFIX+'_inventory.csv',inventory)
 with (WORK/(PREFIX+'_notes.md')).open('a') as f:f.write(f'\n## Cote {cote}, scan {scan}\n\n'+notes+'\n')
 if hand:
  with (WORK/(PREFIX+'_hand_log.md')).open('a') as f:f.write(f'\n## {cote}/{scan}\n\n'+hand+'\n')
 for name,rs in [('notation.tsv',notation),('remaining_doubts.tsv',doubts),('abbreviations.tsv',abbreviations),('CHECK_EVENTS.tsv',events)]:add(name,list(rs))
 rebuild();log(f'scan {scan} done {now()} cote {cote}')
 print(f'Committed {cote}/{scan}: {len(changes)} difference rows; {len(decisions)} mark decisions; {len(inventory)} inventory elements.')
for name in HEADERS:
 if not (WORK/name).exists():write_rows(name,[])
if __name__=='__main__':prepare(sys.argv[1],sys.argv[2])

def change(place,C,H,final,shows,kind='other',c=False,h=True,confidence='high',crop='page',consequential='',marked='no'):
 return dict(place=place,C=C,H=H,final=final,scan_shows=shows,kind=kind,against_C='yes' if c else 'no',against_H='yes' if h else 'no',confidence=confidence,crop=crop,consequential=consequential,marked_in_H=marked)
def decision(id,decision,reading,shows,crop='page',confidence='high'):
 return dict(id=id,decision=decision,reading=reading,**{'what the ink shows':shows},crop=crop,confidence=confidence)
def inv(kind,position,words,sheet='text',hand='his hand'):
 return dict(sheet_kind=sheet,hand=hand,kind=kind,position=position,first_words_or_objects=words)
def doubt(scan,line,reading,alternatives='',confidence='low'):
 return dict(scan=scan,line=line,reading=reading,alternatives=alternatives,confidence=confidence)
