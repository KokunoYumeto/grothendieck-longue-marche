"""Record manual ink readings and render the required apparatus; no recognition."""
from pathlib import Path
import csv,datetime,runpy,pprint,collections,re
ROOT=Path(__file__).resolve().parents[1]
PREFIX='SP71_C13_142'
RECORDS=ROOT/'scripts/records';RECORDS.mkdir(exist_ok=True)
def now():return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def write_tsv(name,header,rows,delimiter='\t'):
 with (ROOT/name).open('w',newline='') as f:
  w=csv.writer(f,delimiter=delimiter);w.writerow(header);w.writerows(rows)
def table(headers,rows):
 def v(x):return str(x).replace('|','\\|').replace('\n','<br>')
 return '\n'.join(['| '+' | '.join(map(v,headers))+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(map(v,r))+' |' for r in rows])+'\n'
def change(place,c,h,final,ink,kind='misread word',confidence='high',against_c=True,against_h=True,crop='page',marked_h='no',math=False):
 return dict(place=place,C=c,H=h,final=final,ink=ink,kind=kind,confidence=confidence,c=against_c,h=against_h,crop=crop,marked_h=marked_h,math=math)
def decision(id,decision,reading,ink,crop='page',confidence='high'):
 return [id,decision,reading,ink,crop,confidence]
def substantive_changes(d):
 # Explicit witness-difference flags distinguish readings from certainty only.
 return [c for c in d['changes'] if c['c'] or c['h']]
def uncertainty_occurrences():
 """Index existing TeX marks mechanically; never infer a manuscript reading."""
 rows=[]
 for p in sorted((ROOT/'pages').glob('*.tex')):
  src=p.read_text();spans=[]
  for m in re.finditer(r'\\(deleted|unsure|illegible)\s*\{',src):
   depth=1;j=m.end()
   while j<len(src) and depth:
    ch=src[j]
    # An odd run of preceding backslashes makes this brace a control symbol.
    k=j-1
    while k>=0 and src[k]=='\\':k-=1
    escaped=(j-1-k)%2
    if not escaped:
     if ch=='{':depth+=1
     elif ch=='}':depth-=1
    j+=1
   if depth:raise ValueError(f'Unclosed mark in {p.name}:{src.count(chr(10),0,m.start())+1}')
   spans.append((m.group(1),m.start(),j,src[m.start():j]))
  deleted=[(a,b) for kind,a,b,_ in spans if kind=='deleted']
  for kind,a,b,mark in spans:
   if kind=='deleted':continue
   rows.append([p.stem[-3:],f"final TeX line {src.count(chr(10),0,a)+1}",'inside `\\deleted`' if any(x<a and b<y for x,y in deleted) else 'outside `\\deleted`',f'`{mark}`'])
 return rows
def save(n,tex,changes,decisions,inventory,note,checks=None,doubts=None,hand=None,notation=None,abbreviations=None,sheet_kind='text',default_hand='his hand'):
 if (RECORDS/f'{n:03}.py').exists():raise RuntimeError('Page already recorded')
 if n==52 and not tex.startswith('\\cotefile'):tex='\\cotefile{142}\n'+tex
 (ROOT/'pages'/f'142_scan{n:03}.tex').write_text(tex.rstrip()+'\n\n')
 d=dict(scan=n,changes=changes,decisions=decisions,inventory=inventory,note=note,checks=checks or [],doubts=doubts or [],hand=hand or [],notation=notation or [],abbreviations=abbreviations or [],sheet_kind=sheet_kind,default_hand=default_hand)
 (RECORDS/f'{n:03}.py').write_text('DATA = '+pprint.pformat(d,width=140,sort_dicts=False)+'\n')
 render()
 with (ROOT/'progress.log').open('a') as f:f.write(f'scan {n:03} done {now()} cote 142\n')
 print(f'scan {n:03} recorded: {len(substantive_changes(d))} differences; {len(decisions)} MARKS decisions; {len(inventory)} elements')
def render():
 ds=[runpy.run_path(str(p))['DATA'] for p in sorted(RECORDS.glob('*.py'))]
 crop_rows=[]
 if (ROOT/'crop_register.tsv').exists():
  with (ROOT/'crop_register.tsv').open(newline='') as f:crop_rows=list(csv.DictReader(f,delimiter='\t'))
 (ROOT/f'{PREFIX}_transcription.tex').write_text(''.join(p.read_text() for p in sorted((ROOT/'pages').glob('*.tex'))))
 counts=[];allchanges=[]
 for d in ds:
  cs=substantive_changes(d);co=collections.Counter(c['confidence'] for c in cs)
  counts.append([f"{d['scan']:03}",sum(c['c'] for c in cs),sum(c['h'] for c in cs),co['high'],co['medium'],co['low']]);allchanges+=cs
 total=['Total']+[sum(row[i] for row in counts) for i in range(1,6)]
 s='# Consolidated reading: changes against C and H\n\nCounts are places, not changed characters. A row may differ from both witnesses. Pure macro conventions and certainty-only changes are excluded. Diagram omissions are grouped by figure; repeated changes within one display are explicitly located in that display. All decisions were made by visual inspection, without OCR.\n\n'+table(['Scan','Against C','Against H','High','Medium','Low'],counts+[total])
 s+='\n## Consequential readings\n\n'
 for d in ds:
  for c in substantive_changes(d):
   if c['math']:s+=f"- Scan {d['scan']:03}, {c['place']}: {c['final']}. {c['ink']}\n"
 s+='\n'
 col=[];decs=[];inv=[];checks=[];doubts=[];hands=[];notations=[];abbs=[];notes='# Reading notes\n\nThese notes report only the supplied sheets. Manuscript claims are attributed, not silently endorsed. A reading is not a proof check. Check types and actual outcomes are recorded separately in CHECK_EVENTS.tsv. No external sources were consulted. Model: GPT-6 Astra Pro; effort setting not exposed; run: SP71_C13_142 second pass, 2026-11-20. Scan references are the primary-source citations for this edition.\n\n'
 for d in ds:
  n=d['scan'];s+=f'## Scan {n:03}\n\n'
  rows=[]
  for i,c in enumerate(substantive_changes(d),1):
   evidence=c['ink']+' ['+c['crop']+']'
   rows.append([f"{n:03}.{i:02} — {c['place']}",c['C'],c['H'],c['final'],evidence,c['confidence']])
   if c['h']:col.append(['142',str(n-1),str(n),c['place'],c['H'],c['C'],c['final'],evidence,c['kind'],c['marked_h'],c['confidence']])
  s+=table(['Place','C','H','Final','What the scan shows','Confidence'],rows) if rows else 'No substantive differences.\n'
  page_crops=[r for r in crop_rows if int(r['scan'])==n]
  if page_crops:
   s+='\n### Crop ledger\n\nEvery crop made for this scan is listed, including crops that confirmed a witness or left a doubt unresolved. These ledger entries are not additional changes. Boxes are in original-image pixels; rotation is in degrees, positive counterclockwise. No crop images are included in the deliverable.\n\n'
   s+=table(['Crop / place','Original box (x0, y0, x1, y1)','Rotation','Enlarged width (pixels)'],[[f"scan {n:03} — {r['label']}",'('+', '.join(r[k] for k in ('x0','y0','x1','y1'))+')',r['rotation'],r['width']] for r in page_crops])
  s+='\nRemaining unresolved: '+('; '.join(x[0]+': '+x[1] for x in d['doubts']) or 'none')+'.\n\n'
  for x in d['decisions']:decs.append([x[0],'142',str(n),*x[1:]])
  for i,x in enumerate(d['inventory'],1):
   # kind, position, first words/objects; optional author
   inv.append([str(n),d['sheet_kind'],x[3] if len(x)>3 else d['default_hand'],f'{n:03}-{i:02}',x[0],x[1],x[2],'yes'])
  for x in d['checks']:checks.append([x[0],x[1] if len(x)>3 else now()[:10],'GPT-6 Astra Pro; effort not exposed; SP71_C13_142',x[-2],x[-1]])
  notes+=f"## Scan {n:03}\n\n{d['note']}\n\n"
  doubts += [[f'{n:03}',*x] for x in d['doubts']]
  hands += [[f'{n:03}',*x] for x in d['hand']]
  notations += [[*x[:2],f'{n:03}',*x[2:]] for x in d['notation']]
  abbs += [[*x,f'{n:03}'] for x in d['abbreviations']]
 (ROOT/f'{PREFIX}_changes.md').write_text(s)
 write_tsv(f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],col)
 write_tsv('decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],decs)
 write_tsv(f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inv,',')
 write_tsv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],checks)
 (ROOT/f'{PREFIX}_notes.md').write_text(notes)
 s='# Notation and remaining doubts\n\n## Notation table\n\n'
 if (ROOT/'scripts/notation_review.md').exists():s+=(ROOT/'scripts/notation_review.md').read_text()+'\n\n'
 s+=table(['Notation','Written form and reading','Scan','Qualification'],notations)
 s+='\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence'],doubts)
 s+='\n## Complete index of in-text uncertainty marks\n\nThe table above groups related damaged words or indices by manuscript place. This mechanical index lists every surviving `\\unsure` and `\\illegible` occurrence, including cancelled text, with its exact final encoding. TeX line numbers locate the delivered page fragments, not manuscript ruled lines. Wrapper status is mechanical; cancellation drawn graphically in TikZ need not use a `\\deleted` wrapper. The index introduces no new reading or certainty claim.\n\n'+table(['Scan','Location in page fragment','TeX wrapper status','Exact mark'],uncertainty_occurrences())
 s+='\n## Disposition of witness C doubt marks\n\n'
 for d in ds:
  for x in d['decisions']:s+=f"- {x[0]} (scan {d['scan']:03}): {x[1]}; `{x[2]}`; {x[3]} ({x[5]}).\n"
 certainty=[]
 for d in ds:
  for c in d['changes']:
   if not c['c'] and not c['h']:
    certainty.append([f"{d['scan']:03}",c['place'],c['final'],c['ink']+' ['+c['crop']+']',c['confidence']])
 if certainty:
  s+='\n## Certainty-only observations\n\nThese entries carry no substantive reading difference from either witness and are excluded from the changes counts and changes tables.\n\n'+table(['Scan','Place','Reading','What the scan shows','Confidence'],certainty)
 s+='\n## Abbreviations\n\n'+table(['Written','Possible expansion (editorial only)','Scan'],abbs)
 s+='\n## Legibility and witnesses\n\n'+((ROOT/'scripts/legibility.txt').read_text() if (ROOT/'scripts/legibility.txt').exists() else 'Assessment in progress during ordered reading; overwritten digits, cancelled ink and crowded marginal indices remain the least secure areas.\n')
 (ROOT/f'{PREFIX}_doubts.md').write_text(s)
 (ROOT/f'{PREFIX}_hand_log.md').write_text('# Hand and notation log\n\nEach row reports observed habits, scope, and witness consequences. Similar shapes never authorize a silent correction of a clearly different letter.\n\n'+table(['Scan(s)','Habit','Scope / exceptions','Witness consequences'],hands))
 kinds=collections.Counter(c['kind'] for c in allchanges)
 mapk=[('Symbols and indices',['misread symbol or index']),('Words',['misread word']),('Omissions',['omission']),('Drawings and diagrams',['drawing or diagram']),('Readable ink left as illegible',['readable ink left as \\ill{}']),('Insertions put in the wrong place',['insertion or placement']),('Struck text',['deletion state']),('Abbreviation / spelling normalization',['abbreviation expanded or spelling modernised']),('Text not on page',['text not on the page']),('Other',['other'])]
 feedback='# Error-sheet feedback\n\nCounts use the primary category assigned to each logged place, against either witness; a place is counted once. Certainty-only resolutions are excluded.\n\n'+table(['Error-sheet kind','Places'],[[k,sum(kinds[v] for v in vs)] for k,vs in mapk])
 feedback+='\n## Recurring phenomena\n\nSee the hand log for exact scan locators. Any additional recurring issue found in this run is recorded there. No extrapolation is made from this sample to other folders.\n'
 if (ROOT/'scripts/feedback_additions.md').exists():feedback+='\n'+(ROOT/'scripts/feedback_additions.md').read_text()
 (ROOT/f'{PREFIX}_sheet_feedback.md').write_text(feedback)
if __name__=='__main__':render()
