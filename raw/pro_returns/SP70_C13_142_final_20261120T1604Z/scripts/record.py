from pathlib import Path
from datetime import datetime,timezone
import csv,collections,re,hashlib
W=Path(__file__).resolve().parents[1]
ROOT=W.parent
SOURCE=ROOT/'source/SP70_C13_142_texts'
N=None
T=None
COUNTER=0

def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def append(name,row,delim='\t'):
 with (W/name).open('a',newline='') as f:csv.writer(f,delimiter=delim,lineterminator='\n').writerow(row)
def read(name,delim='\t'):
 with (W/name).open(newline='') as f:return list(csv.DictReader(f,delimiter=delim))
def begin(n):
 global N,T,COUNTER
 N=n;COUNTER=0;T=(SOURCE/f'pages/142_scan{n:03}.tex').read_text()
 return T
def change(place,c,h,final,ink,dc=True,dh=True,kind='misread word',cat=2,conf='high',crop='page',conseq='',marked='no'):
 global COUNTER
 COUNTER+=1
 append('CHANGES.tsv',[f'{N:03}-{COUNTER:02}',N,place,c,h,final,ink,crop,conf,'yes' if dc else 'no','yes' if dh else 'no',kind,cat,conseq])
 if dh:append('SP70_C13_142_collation.tsv',['142',N-1,N,place,h,c,final,ink+'; '+crop,kind,marked,conf])
def decision(mid,decision,reading,ink,crop='page',conf='high'):
 append('decisions.tsv',[f'M{mid:04}',142,N,decision,reading,ink,crop,conf])
def inv(kind,position,words,sheet='text',hand='his hand'):
 rows=read('SP70_C13_142_inventory.csv',',');idx=1+sum(int(x['scan'])==N for x in rows)
 append('SP70_C13_142_inventory.csv',[N,sheet,hand,f'{N:03}-{idx:02}',kind,position,words,'yes'],',')
def note(text):
 with (W/'SP70_C13_142_notes.md').open('a') as f:f.write(f'## Scan {N:03}\n\n{text}\n\n')
def hand(title,text):
 with (W/'SP70_C13_142_hand_log.md').open('a') as f:f.write(f'### Scan {N:03}: {title}\n\n{text}\n\n')
def notation(sign,form,scans=None):append('NOTATION.tsv',[sign,form,scans or str(N)])
def abbrev(sign,form,scans=None):append('ABBREVIATIONS.tsv',[sign,form,scans or str(N)])
def check(sid,kind,outcome):append('CHECK_EVENTS.tsv',[sid,now(),'GPT-6 Astra Pro; effort not exposed; run 2026-11-20 second pass',kind,outcome])
def finish(t):
 (W/f'pages/142_scan{N:03}.tex').write_text(t)
 with (W/'progress.log').open('a') as f:f.write(f'scan {N:03} done {now()} cote 142\n')
 refresh()
def md(s):return str(s).replace('|','&#124;').replace('\n','<br>')
def table(headers,rows):return '| '+' | '.join(headers)+' |\n|'+'|'.join(['---']*len(headers))+'|\n'+''.join('| '+' | '.join(md(x) for x in r)+' |\n' for r in rows)
def uncertainty(text):
 for match in re.finditer(r'\\unsure\{',text):
  start=match.end();level=1;i=start
  while i<len(text) and level:
   if text[i]=='{':level+=1
   elif text[i]=='}':level-=1
   i+=1
  yield text.count('\n',0,match.start())+1,text[start:i-1]
 for match in re.finditer(r'\\illegible\{([^}]+)\}',text):yield text.count('\n',0,match.start())+1,match.group(0)
def full_doubt_payload(reading):
 """Unwrap only one complete unsure macro; preserve all payload characters.

 No whitespace, alternatives, or inner LaTeX are normalized. Literal illegible
 macros remain whole, matching the key yielded by uncertainty().
 """
 prefix='\\unsure{'
 if not reading.startswith(prefix):return reading
 depth=1;i=len(prefix)
 while i<len(reading):
  if reading[i]=='\\':
   # An escaped brace is literal. A doubled backslash is consumed as a unit.
   if i+1<len(reading) and reading[i+1] in '{}\\':i+=2;continue
  if reading[i]=='{':depth+=1
  elif reading[i]=='}':
   depth-=1
   if depth==0:return reading[len(prefix):i] if i==len(reading)-1 else reading
  i+=1
 return reading
def remaining_doubt_confidences():
 """Exact-match confidence metadata, independent of CHANGES.tsv.

 Optional DOUBT_CONFIDENCE.tsv columns: scan, payload, confidence.
 Payload is the entire unsure argument, including every alternative; for an
 illegible mark use the entire literal macro. Extra columns are permitted.
 Priority: optional override, exact undecided decision, then low in refresh().
 Conflicting explicit values for one exact key require an explicit override.
 """
 allowed={'low','medium','high'};overrides={};result={}
 if (W/'DOUBT_CONFIDENCE.tsv').exists():
  for r in read('DOUBT_CONFIDENCE.tsv'):
   if not {'scan','payload','confidence'}.issubset(r):raise ValueError('DOUBT_CONFIDENCE.tsv requires scan, payload, confidence columns')
   key=(int(r['scan']),r['payload']);confidence=r['confidence']
   if confidence not in allowed:raise ValueError('Invalid DOUBT_CONFIDENCE.tsv confidence for scan '+str(key[0]))
   if key in overrides and overrides[key]!=confidence:raise ValueError('Conflicting DOUBT_CONFIDENCE.tsv values for one exact scan/payload key')
   overrides[key]=confidence
 for r in read('decisions.tsv'):
  if r['decision']!='undecided':continue
  key=(int(r['scan']),full_doubt_payload(r['reading']));confidence=r['confidence']
  if key in overrides:continue
  if confidence not in allowed:raise ValueError('Invalid undecided-decision confidence for '+r['id'])
  if key in result and result[key]!=confidence:raise ValueError('Conflicting undecided confidences for one exact scan/payload key; specify DOUBT_CONFIDENCE.tsv')
  result[key]=confidence
 result.update(overrides)
 return result
def inspected_crops(crops,n):
 rr=[r for r in crops if int(r['scan'])==n]
 out='\n### Inspected crops\n\n'
 if not rr:return out+'No separate tight crop is recorded for this scan in `CROPS.tsv`.\n'
 entries=[]
 for r in rr:
  coordinates='('+', '.join(r[k] for k in ('x0','y0','x1','y1'))+')' if all(r[k] for k in ('x0','y0','x1','y1')) else 'not recovered'
  angle=r['rotation_degrees']+'°' if r['rotation_degrees'] else 'not documented'
  sources='; '.join(dict.fromkeys(s.strip() for s in r['source_documentation'].split(';') if s.strip()))
  association=r['filename_association']
  if association=='exact_pixel_match':provenance='Exact reconstructed RGB equality; '+sources
  elif association=='reader_confirmed':provenance='Reader-confirmed command mapping; '+sources
  else:provenance=association.replace('_',' ')+'; '+sources+'. '+r['notes']
  entries.append(['`'+r['crop_file']+'`',coordinates,angle,provenance])
 return out+table(['Crop filename','Original pixels (x0, y0, x1, y1)','Rotation','Provenance and caveats'],entries)
def refresh():
 pages=sorted((W/'pages').glob('142_scan*.tex'))
 doubt_confidence=remaining_doubt_confidences()
 (W/'SP70_C13_142_transcription.tex').write_text('\n'.join(p.read_text().rstrip()+'\n' for p in pages))
 rows=read('CHANGES.tsv');scans=[int(p.stem[-3:]) for p in pages]
 crops=read('CROPS.tsv') if (W/'CROPS.tsv').exists() else []
 counts=[]
 for n in scans:
  rr=[r for r in rows if int(r['scan'])==n]
  counts.append([f'{n:03}',sum(r['against_C']=='yes' for r in rr),sum(r['against_H']=='yes' for r in rr),*[sum(r['confidence']==c for r in rr) for c in ['high','medium','low']]])
 counts.append(['TOTAL',*[sum(r[i] for r in counts) for i in range(1,6)]])
 out='# Changes against the two witnesses\n\nCounts are distinct recorded places; a place differing from both witnesses counts once in each witness column and once by confidence. Pure certainty and macro changes are excluded. Where the supplied H text only describes a drawing, the missing drawing or its differing components are recorded at the locations specified below; these are counts of recorded places, not counts of drawings. “page” means the whole-page/half-page reading settled the place. Crop coordinates refer to the original scan.\n\n'+table(['Scan','Against C','Against H','High','Medium','Low'],counts)
 out+='\nCrop subsections document the tight crops used, including views that confirmed an existing reading. They do not add divergence rows or alter the counts above. Coordinates are original-image pixels; a blank rotation record is reported as “not documented”, not assumed to be zero. Numerical RGB verification establishes file/rectangle provenance only and is not a manuscript reading or a mathematical check.\n'
 out+='\n## Consequential corrections\n\n'+('\n'.join('- Scan '+r['scan']+', '+r['place']+': '+r['consequential'] for r in rows if r['consequential']) or 'None recorded yet.')+'\n'
 doubtrows=[]
 for p in pages:
  n=int(p.stem[-3:]);out+=f'\n## Scan {n:03}\n\n'
  rr=[r for r in rows if int(r['scan'])==n]
  out+=table(['Place','C','H','Final','Ink and view','Confidence'],[[r['place'],r['C'],r['H'],r['final'],r['scan_shows']+'; '+r['crop'],r['confidence']] for r in rr]) if rr else 'No substantive divergence recorded.\n'
  out+=inspected_crops(crops,n)
  us=list(uncertainty(p.read_text()))
  out+='\nUnresolved: '+('; '.join(f'TeX line {l}: `{s}`' for l,s in us) if us else 'none.')+'\n'
  for l,s in us:
   parts=s.split('|');doubtrows.append([n,f'TeX line {l}',parts[0],' | '.join(parts[1:]) or 'no secure alternative',doubt_confidence.get((n,s),'low')])
 (W/'SP70_C13_142_changes.md').write_text(out)
 with (W/'REMAINING_DOUBTS.tsv').open('w',newline='') as f:
  wr=csv.writer(f,delimiter='\t',lineterminator='\n');wr.writerow(['scan','line','reading','alternatives','confidence']);wr.writerows(doubtrows)
 out='# Notation, doubts, and abbreviations\n\n## Notation table\n\n'+table(['Sign or convention','Written form and interpretation','Scans and cautions'],[[r['sign'],r['form'],r['scans']] for r in read('NOTATION.tsv')])
 out+='\n## Remaining doubts\n\nThese include uncertain cancelled readings. Line locators refer to the per-page TeX files; the changes log gives manuscript locations and evidence. Remaining marks default to low: this labels unresolved ink, not uncertainty that a passage, insertion, or deletion is present. An explicit undecided-decision confidence is reused only when the scan and complete reading, including alternatives, match exactly. Optional `DOUBT_CONFIDENCE.tsv` entries override those values; its columns are `scan`, `payload`, and `confidence`, with the full unsure argument as payload (or the literal illegible macro). Divergence-row confidence is never used to infer remaining-doubt confidence.\n\n'+table(['Scan','Location','Reading','Alternatives','Confidence'],doubtrows)
 out+='\n## Certainty decisions in the supplied register\n\n'+table(['ID','Scan','Decision','Reading','Evidence / view','Confidence'],[[r['id'],r['scan'],r['decision'],r['reading'],r['what the ink shows']+'; '+r['crop'],r['confidence']] for r in read('decisions.tsv')])
 out+='\n## Abbreviations\n\nExpansions are explanatory only and are not substituted into the transcription.\n\n'+table(['Written abbreviation','Possible expansion','Scans'],[[r['abbreviation'],r['expansion'],r['scans']] for r in read('ABBREVIATIONS.tsv')])
 if (W/'LEGIBILITY.md').exists():out+='\n## Legibility and witness comparison\n\n'+(W/'LEGIBILITY.md').read_text()
 (W/'SP70_C13_142_doubts.md').write_text(out)
 cats={1:'Symbols and indices',2:'Words',3:'Omissions',4:'Drawings and diagrams',5:'Readable ink left as illegible',6:'Insertion placement',7:'Struck text',8:'Abbreviation expansion or spelling normalisation',9:'Text not on the page',10:'Other'}
 cc=collections.Counter(int(r['error_category']) for r in rows)
 out='# Feedback on the recurring-error sheet\n\nA place is assigned one primary category, so the counts do not double-count a correction. Counts concern substantive divergences from either witness, not certainty changes alone.\n\n'+table(['No.','Kind','Places','Locations'],[[k,v,cc[k],'; '.join(r['scan']+': '+r['place'] for r in rows if int(r['error_category'])==k)] for k,v in cats.items()])
 out+='\n## Additional recurrent patterns\n\n'+((W/'ADDITIONAL_PATTERNS.md').read_text() if (W/'ADDITIONAL_PATTERNS.md').exists() else 'No additional pattern established yet.\n')
 (W/'SP70_C13_142_sheet_feedback.md').write_text(out)
if __name__=='__main__':refresh()
