from pathlib import Path
from datetime import datetime,timezone
from PIL import Image,ImageOps,ImageEnhance,ImageFilter
import csv,ast,pprint,collections,hashlib,zipfile,re
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parents[1]
SOURCE=BASE/'source/SP67_C13_136_texts'
SCANS=BASE/'source/SP67_C13_136_scans'
VIEWS=BASE/'work/views'
ORDER=[330,332,333,334,335,337,338,339,340,342,343,345,346,348,350,351,352,355,357,358,359,360,361,362,363]
PFX='SP67_C13_136'
def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def log(s):
 with (ROOT/'progress.log').open('a') as f: f.write(s+'\n')
def marks(n):
 with (SOURCE/'MARKS.tsv').open(newline='') as f: return [r for r in csv.DictReader(f,delimiter='\t') if int(r['scan'])==n]
def prep(n):
 im=Image.open(SCANS/f'136_scan{n}.jpg'); w,h=im.size
 if w<=h: boxes=[(0,0,w,round(h*.55)),(0,round(h*.45),w,h)]
 else: boxes=[(0,0,round(w*.55),h),(round(w*.45),0,w,h)]
 for name,box in zip(['top','bottom'],boxes):
  p=VIEWS/f'{n}_{name}.png'
  if not p.exists(): im.crop(box).save(p)
 print('SCAN',n,'SIZE',im.size,'HALVES',boxes)
 print('WITNESS C\n'+(SOURCE/f'pages/136_scan{n}.tex').read_text())
 hp=SOURCE/f'hua/hua_136_scan{n}.tex'
 print('WITNESS H\n'+(hp.read_text() if hp.exists() else '(absent)'))
 print('MARKS')
 for r in marks(n): print(r['id'],r['the mark as written'])
def crop(n,label,box,rotate=0):
 p=VIEWS/f'{n}_{label}.png'
 if p.exists(): raise RuntimeError('Crop already exists; do not crop a decided place again')
 im=Image.open(SCANS/f'136_scan{n}.jpg').crop(box)
 if rotate: im=im.rotate(rotate,expand=True,fillcolor='white')
 im=ImageOps.autocontrast(im).resize((2800,round(im.height*2800/im.width)),Image.Resampling.LANCZOS)
 im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=130,threshold=3))
 im.save(p)
 log(f'crop scan {n} {label} box {tuple(box)} rotation {rotate}')
 return str(p)
def resolve(n, choices):
 ms=marks(n); assert len(ms)==len(choices),(len(ms),len(choices))
 text=(SOURCE/f'pages/136_scan{n}.tex').read_text(); replacements=[]; ds=[]; pos=0
 for m,ch in zip(ms,choices):
  reading,ink,*etc=ch
  cp=etc[0] if etc else 'page'; conf=etc[1] if len(etc)>1 else 'high'
  old=m['the mark as written']; ix=text.find(old,pos)
  assert ix>=0,(m['id'],old)
  pos=ix+len(old)
  alternatives=old[old.index('{')+1:-1].split('|')
  decision='undecided' if '\\unsure{' in reading or '\\illegible{' in reading else ('first' if reading==alternatives[0] else ('alternative' if reading in alternatives[1:] else 'other'))
  ds.append(dict(id=m['id'],cote='136',scan=str(n),decision=decision,reading=reading,**{'what the ink shows':ink},crop=cp,confidence=conf))
  replacements.append((ix,pos,reading))
 for a,b,r in reversed(replacements): text=text[:a]+r+text[b:]
 return text,ds
def repl(text, old,new,count=1):
 assert text.count(old)>=count,(old,text.count(old),count)
 return text.replace(old,new,count)
def change(place,c,h,f,ink,kind='other',dc=True,dh=True,confidence='high',crop='page',marked='no',consequential=False):
 return dict(place=place,C=c,H=h,final=f,ink=ink,kind=kind,dc=dc,dh=dh,confidence=confidence,crop=crop,marked=marked,consequential=consequential)
def inv(kind,position,first,hand='his hand',sheet='text'): return dict(kind=kind,position=position,first_words_or_objects=first,hand=hand,sheet_kind=sheet)
def check(id,outcome,type='carried as background without fault found'): return dict(statement_id=id,date=now(),who='GPT-6 Astra Pro; current configured effort; run 2026-11-20',type=type,outcome=outcome)
ADDITIONAL_DOUBT_FIELDS={'place','reading','alternatives','evidence','confidence'}
def _validate_additional_doubt(value):
 if isinstance(value,str): return  # legacy entries remain usable during partial work
 if not isinstance(value,dict): raise TypeError('An additional doubt must be a string or a structured dictionary')
 missing=ADDITIONAL_DOUBT_FIELDS-set(value); extra=set(value)-ADDITIONAL_DOUBT_FIELDS-{'id'}
 if missing or extra: raise ValueError(f'Additional-doubt fields: missing={sorted(missing)}, extra={sorted(extra)}')
 for key in ADDITIONAL_DOUBT_FIELDS:
  if not isinstance(value[key],str): raise TypeError(f'Additional-doubt {key} must be a string')
 if not value['place'].strip() or not value['reading'].strip(): raise ValueError('Additional doubts require a nonempty place and reading')
 if value['confidence'] not in {'low','medium','high'}: raise ValueError('Additional-doubt confidence must be explicitly low, medium, or high')
 if 'id' in value and (not isinstance(value['id'],str) or not value['id'].strip()): raise ValueError('Additional-doubt id must be a nonempty string when supplied')
def additional_doubt(place,reading,*,confidence,alternatives='',evidence='See page changes and notes',id=None):
 """Create a structured additional doubt; confidence has no default."""
 value=dict(place=place,reading=reading,alternatives=alternatives,evidence=evidence,confidence=confidence)
 if id is not None: value['id']=id
 _validate_additional_doubt(value)
 return value
def _additional_doubt_summary(value):
 if isinstance(value,str): return value
 _validate_additional_doubt(value)
 prefix=(value['id']+'; ') if value.get('id') else ''
 return prefix+value['place']+': '+value['reading']+(' (alternatives: '+value['alternatives']+')' if value['alternatives'] else '')
def _additional_doubt_row(scan,index,value):
 generated_id=f'U136-{scan}-{index:02d}'
 if isinstance(value,str): return (scan,generated_id,value,'Explicit confidence pending the sole reader\'s migration','unassigned')
 _validate_additional_doubt(value)
 place=value.get('id',generated_id)+'; '+value['place']
 reading=value['reading']+(' | '+value['alternatives'] if value['alternatives'] else '')
 return (scan,place,reading,value['evidence'],value['confidence'])
def commit(n,text,ds,changes,inventory,note,hand=(),notation=(),abbr=(),checks=(),unresolved=()):
 unresolved=list(unresolved)
 for value in unresolved: _validate_additional_doubt(value)
 assert not (ROOT/f'pages/136_scan{n}.tex').exists(),'Use audit to revise a committed page'
 prior=[int(p.stem.split('scan')[-1]) for p in (ROOT/'pages').glob('*.tex')]
 assert ORDER[len(prior)]==n,(prior,n)
 record=dict(scan=n,decisions=ds,changes=changes,inventory=inventory,note=note,hand=list(hand),notation=list(notation),abbr=list(abbr),checks=list(checks),unresolved=list(unresolved))
 (ROOT/f'pages/136_scan{n}.tex').write_text(text.strip()+'\n')
 (ROOT/f'records/scan{n}.py').write_text(pprint.pformat(record,sort_dicts=False,width=120)+'\n')
 rebuild(); log(f'scan {n:03d} done {now()} cote 136')
 print('COMMITTED',n,'changes',len(changes),'marks',len(ds))
def records(): return [ast.literal_eval(p.read_text()) for p in sorted((ROOT/'records').glob('scan*.py'))]
def table(headers,rows):
 def esc(s): return str(s).replace('|','\\|').replace('\n','<br>')
 return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(esc(x) for x in r)+' |\n' for r in rows)
def writecsv(name,fields,rows,delim):
 with (ROOT/name).open('w',newline='') as f:
  wr=csv.DictWriter(f,fieldnames=fields,delimiter=delim);wr.writeheader();wr.writerows(rows)
def rebuild():
 rr=records(); changes=[(r['scan'],x) for r in rr for x in r['changes']]
 for r in rr:
  for value in r['unresolved']: _validate_additional_doubt(value)
 totals=[]
 for r in rr:
  cc=collections.Counter(x['confidence'] for x in r['changes'])
  totals.append([r['scan'],sum(x['dc'] for x in r['changes']),sum(x['dh'] for x in r['changes']),cc['high'],cc['medium'],cc['low']])
 totals.append(['TOTAL']+[sum(row[i] for row in totals) for i in range(1,6)])
 out='# Consolidation changes\n\nCounts are substantive reading or placement differences, not macro syntax or certainty alone. A place differing from both witnesses counts once in each witness column. Confidence counts count places once. Crop coordinates refer to the original JPG; “page” means the full-resolution halves settled the place.\n\n'+table(['scan','against C','against H','high','medium','low'],totals)+'\n## Consequential corrections\n\n'
 for n,x in changes:
  if x['consequential']: out+=f'- Scan {n}, {x["place"]}: {x["final"]}. {x["ink"]}\n'
 for r in rr:
  out+=f'\n## Scan {r["scan"]}\n\n'+table(['place','C','H','final','scan evidence / crop','confidence'],[[x['place'],x['C'],x['H'],x['final'],x['ink']+'; '+x['crop'],x['confidence']] for x in r['changes']])
  out+='\nUnresolved: '+('; '.join(_additional_doubt_summary(value) for value in r['unresolved']) or 'none')+'.\n'
 (ROOT/f'{PFX}_changes.md').write_text(out)
 cols=['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']
 writecsv(f'{PFX}_collation.tsv',cols,[dict(zip(cols,['136',str(n-1),str(n),x['place'],x['H'],x['C'],x['final'],x['ink']+'; '+x['crop'],x['kind'],x['marked'],x['confidence']])) for n,x in changes if x['dh']], '\t')
 writecsv('decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],[d for r in rr for d in r['decisions']], '\t')
 fields=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']
 writecsv(f'{PFX}_inventory.csv',fields,[dict(scan=r['scan'],element=str(i),transcribed='yes',**x) for r in rr for i,x in enumerate(r['inventory'],1)],',')
 writecsv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],[x for r in rr for x in r['checks']], '\t')
 (ROOT/f'{PFX}_notes.md').write_text('# Reading notes\n\nThese notes distinguish what the manuscript states from mathematical checks actually performed. No outside material was consulted.\n'+''.join(f'\n## Scan {r["scan"]}\n\n'+r['note']+'\n' for r in rr))
 (ROOT/f'{PFX}_hand_log.md').write_text('# Hand log\n\nClaims of consistency are limited to the occurrences explicitly inspected; notation is confirmed in each later page, not imposed against clear ink.\n'+''.join(f'\n## Scan {r["scan"]}\n\n'+''.join('- '+x+'\n' for x in r['hand']) for r in rr if r['hand']))
 notation=[(r['scan'],*x) for r in rr for x in r['notation']]
 doubt=[(r['scan'],x['id'],x['reading'],x['what the ink shows'],x['confidence']) for r in rr for x in r['decisions'] if x['decision']=='undecided']
 doubt += [_additional_doubt_row(r['scan'],i,x) for r in rr for i,x in enumerate(r['unresolved'],1)]
 with (SOURCE/'MARKS.tsv').open(newline='',encoding='utf-8') as f: mark_count=sum(1 for _ in csv.DictReader(f,delimiter='\t'))
 decision_count=sum(len(r['decisions']) for r in rr)
 (ROOT/f'{PFX}_doubts.md').write_text('# Notation, doubts and abbreviations\n\n## Notation table\n\n'+table(['scan','notation','how written / scope'],notation)+'\n## Remaining doubts\n\n'+table(['scan','place / mark','reading / alternatives','evidence','confidence'],doubt)+f'\n## Certainty decisions\n\n{decision_count} of {mark_count} original live-text doubt marks are currently accounted for in decisions.tsv; certainty-only decisions are recorded there and do not inflate the changes log.\n\n## Abbreviations\n\n'+table(['scan','form','proposed expansion'],[(r['scan'],*x) for r in rr for x in r['abbr']])+'\n## Legibility and witnesses\n\nWorking assessment, to be finalized after the second reading. Pale superscripts, overwritten endings, deletions and cramped interlinear insertions require the most caution. Agreement between C and H has not been treated as evidence.\n')
 kinds=['misread symbol or index','misread word','omission','drawing or diagram','readable ink left as \\ill{}','insertion or placement','deletion state','abbreviation expanded or spelling modernised','text not on the page','other']
 counts=collections.Counter(x['kind'] for _,x in changes)
 (ROOT/f'{PFX}_sheet_feedback.md').write_text('# Error-sheet feedback\n\nCounts concern distinct substantive places recorded in the changes log, regardless of which witness differs. Certainty-only resolutions appear separately in decisions.tsv.\n\n'+table(['kind','places'],[(k,counts[k]) for k in kinds])+ '\n## Places by kind\n\n'+''.join(f'### {k}\n\n'+('; '.join(f'{n}: {x["place"]}' for n,x in changes if x['kind']==k) or 'None recorded')+'\n\n' for k in kinds))
 (ROOT/f'{PFX}_transcription.tex').write_text('\n'.join((ROOT/f'pages/136_scan{r["scan"]}.tex').read_text().rstrip() for r in rr)+'\n')
def audit(n,text=None,changes=(),note='Second reading against the image; no further reading change.'):
 p=ROOT/f'records/scan{n}.py';r=ast.literal_eval(p.read_text())
 if text is not None:(ROOT/f'pages/136_scan{n}.tex').write_text(text.strip()+'\n')
 r['changes']+=list(changes);r['note']+='\n\nSecond reading: '+note
 p.write_text(pprint.pformat(r,sort_dicts=False,width=120)+'\n');rebuild();log(f'scan {n:03d} audited {now()}')
if __name__=='__main__':
 import sys
 if len(sys.argv)>1:prep(int(sys.argv[1]))
