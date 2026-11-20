from pathlib import Path
from datetime import datetime,timezone
import csv, json, hashlib, zipfile
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent
PREFIX='SP61_CW_75'
def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def log(s):
 with (ROOT/'progress.log').open('a') as f:f.write(s+' '+utc()+'\n')
def read_table(name):
 p=ROOT/name
 if not p.exists():return []
 with p.open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def append_table(name,fields,rows):
 p=ROOT/name; exists=p.exists()
 with p.open('a',newline='') as f:
  w=csv.DictWriter(f,fields,delimiter='\t');
  if not exists:w.writeheader()
  w.writerows(rows)
def append_md(name,s):
 with (ROOT/name).open('a') as f:f.write(s.rstrip()+'\n\n')
def save_tex(scan,tex):
 folder='J75-02' if scan<18 else 'J75-03'
 (ROOT/'pages'/f'{folder}_75_scan{scan:03}.tex').write_text(tex.strip()+'\n')
def crop(scan,key,box,angle=0,width=2600):
 from PIL import Image,ImageOps,ImageFilter
 folder='J75-02' if scan<18 else 'J75-03'
 src=WORK/'source'/'SP61_CW_75_scans'/f'{folder}_75_scan{scan:03}.jpg'
 dst=WORK/'work_crops'/f'{scan:03}_{key}.png'
 if dst.exists():raise RuntimeError('Do not recrop a decided place: '+str(dst))
 im=Image.open(src).crop(box)
 if angle:im=im.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 im=ImageOps.autocontrast(im)
 im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2,percent=110,threshold=3))
 im.save(dst)
 append_table('crop_register.tsv',['scan','key','box','rotation','width'],[dict(scan=scan,key=key,box=str(tuple(box)),rotation=angle,width=width)])
 print(str(dst))
 return dst
CHANGE_FIELDS=['id','scan','place','C','H','final','evidence','confidence','against_C','against_H','kind','marked_in_H','error_sheet','consequence']
def changes(scan,rows):
 out=[]
 prior=[r for r in read_table('reading_decisions.tsv') if int(r['scan'])==scan]
 for i,r in enumerate(rows,len(prior)+1):
  place,c,h,final,evidence,confidence,againstC,againstH,kind,marked,error,consequence=r
  out.append(dict(zip(CHANGE_FIELDS,[f'S{scan:03}-{i:03}',scan,place,c,h,final,evidence,confidence,'yes' if againstC else 'no','yes' if againstH else 'no',kind,marked,error,consequence])))
 append_table('reading_decisions.tsv',CHANGE_FIELDS,out)
 build_changes()
def md(s): return str(s).replace('|','&#124;').replace('\n','<br>')
def build_changes():
 rows=read_table('reading_decisions.tsv')
 scans=sorted(set(int(r['scan']) for r in rows))
 text=['# SP61_CW_75 — Changes from the two witnesses','', 'Each row is a reading locus, not a macro-syntax difference. Counts against C and H can overlap. Certainty-only decisions are listed separately in the doubts file. Evidence marked “half” was settled at full resolution without an extra crop. Cropped loci give original whole-image pixel coordinates. H’s editorial comments and page markers are not source text.','', '| Scan | Against C | Against H | High | Medium | Low |','| --- | ---: | ---: | ---: | ---: | ---: |']
 for n in scans+['Total']:
  rs=rows if n=='Total' else [r for r in rows if int(r['scan'])==n]
  vals=[sum(r[k]==v for r in rs) for k,v in [('against_C','yes'),('against_H','yes'),('confidence','high'),('confidence','medium'),('confidence','low')]]
  text.append('| '+str(n)+' | '+' | '.join(map(str,vals))+' |')
 text += ['', '### Confidence counts by witness', '', '| Scan | C high | C medium | C low | H high | H medium | H low |', '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
 for n in scans+['Total']:
  rs=rows if n=='Total' else [r for r in rows if int(r['scan'])==n]
  vals=[sum(r[w]=='yes' and r['confidence']==c for r in rs) for w in ['against_C','against_H'] for c in ['high','medium','low']]
  text.append('| '+str(n)+' | '+' | '.join(map(str,vals))+' |')
 text+=['','## Consequential corrections','']
 cons=[r for r in rows if r['consequence']]
 text += [f"- {r['id']} (scan {r['scan']}, {r['place']}; {r['confidence']} confidence): {r['consequence']}" for r in cons] or ['None recorded yet.']
 for n in scans:
  text+=['',f'## Scan {n:03}','', '| ID / place | C | H | Consolidated reading | What the scan shows | Confidence |','| --- | --- | --- | --- | --- | --- |']
  for r in rows:
   if int(r['scan'])==n:text.append('| '+' | '.join(md(r[k]) for k in ['id','C','H','final','evidence','confidence']).replace(md(r['id']),md(r['id']+' — '+r['place']),1)+' |')
  ds=[r for r in read_table('remaining_doubts.tsv') if int(r['scan'])==n]
  text+=['','### Still unresolved','']
  text += [f"- {d['line']}: `{d['reading']}`; alternatives: {d['alternatives']}. {d['reason']}" for d in ds] or ['No unresolved locus recorded for this page.']
  text += ['', '### Crop register for this page', '', 'Each box is in original whole-image pixels (x0, y0, x1, y1). This includes certainty-only loci, whose decisions are in the doubts file.', '', '| Locus | Box | Rotation | Width after enlargement |', '| --- | --- | ---: | ---: |']
  for c in read_table('crop_register.tsv'):
   if int(c['scan'])==n:text.append('| '+' | '.join(md(c[k]) for k in ['key','box','rotation','width'])+' |')
 (ROOT/f'{PREFIX}_changes.md').write_text('\n'.join(text)+'\n')
 fields=['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']
 with (ROOT/f'{PREFIX}_collation.tsv').open('w',newline='') as f:
  w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader()
  for r in rows:
   if r['against_H']=='yes':
    n=int(r['scan']); w.writerow(dict(zip(fields,['J75-02' if n<18 else 'J75-03',n-1,n,r['place'],r['H'],r['C'],r['final'],r['evidence'],r['kind'],r['marked_in_H'],r['confidence']])))
def inventory(scan,rows):
 p=ROOT/f'{PREFIX}_inventory.csv';exists=p.exists();fields=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']
 with p.open('a',newline='') as f:
  w=csv.DictWriter(f,fields); 
  if not exists:w.writeheader()
  for i,r in enumerate(rows,1):
   kind,pos,words=r;w.writerow(dict(zip(fields,[scan,'text','his hand',f'S{scan:03}-E{i:02}',kind,pos,words,'yes'])))
def doubts(scan,rows):
 append_table('remaining_doubts.tsv',['scan','line','reading','alternatives','confidence','reason'],[dict(zip(['scan','line','reading','alternatives','confidence','reason'],[scan]+list(r))) for r in rows])
def checks(rows):
 fields=['statement_id','date','who','type','outcome']
 append_table('CHECK_EVENTS.tsv',fields,[dict(zip(fields,[sid,utc(),'GPT-6 Astra Pro; effort not exposed; SP61_CW_75',typ,outcome])) for sid,typ,outcome in rows])
def assemble():
 pages=sorted((ROOT/'pages').glob('*.tex'),key=lambda p:int(p.stem[-3:]))
 (ROOT/f'{PREFIX}_transcription.tex').write_text('\\cotefile{75}\n'+''.join(p.read_text() for p in pages))
def checkpoint_due():
 first=(ROOT/'progress.log').read_text().splitlines()[0]
 start=datetime.strptime(first,'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
 existing=sorted((WORK/'deliverables').glob(PREFIX+'_checkpoint_*.zip'))
 minutes=(datetime.now(timezone.utc)-start).total_seconds()/60
 return minutes>=45*(len(existing)+1),minutes,len(existing)+1
if __name__=='__main__':
 assemble();build_changes();print(checkpoint_due())
