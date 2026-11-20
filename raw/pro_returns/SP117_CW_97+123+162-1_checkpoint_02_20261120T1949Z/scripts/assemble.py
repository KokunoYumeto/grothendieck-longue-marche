from pathlib import Path
import csv,json,re,collections
O=Path(__file__).resolve().parents[1]; ID='SP117_CW_97+123+162-1'; NL='\n'
order=json.loads((O/'work/page_order.json').read_text())
def esc(x):return str(x).replace('|','&#124;').replace(NL,'<br>')
def tab(h,rs):return NL.join(['| '+' | '.join(h)+' |','|'+'|'.join(['---']*len(h))+'|']+['| '+' | '.join(map(esc,r))+' |' for r in rs])+NL
def savecsv(n,h,rs,d=','):
 with (O/n).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=h,delimiter=d,extrasaction='ignore');w.writeheader();w.writerows(rs)
records=[]
for m in order:
 p=O/'work'/(Path(m['codex_file']).stem+'_decided.json')
 if p.exists():
  r=json.loads(p.read_text());r['meta']=m;records.append(r)
counts=[];allchanges=[];coll=[];inv=[];doubts=[];notes=[];audits=[];hands=[];notation=[];checks=[];sections=[];major=[];combined=[];last=None
for r in records:
 m=r['meta'];page=r['page'];label=f"{m['cote']}/{int(m['our_scan']):03}"
 cs=[c for c in r['changes'] if not c.get('added_doubt_only')];allchanges.extend((label,c) for c in cs)
 counts.append([label,sum(bool(c.get('changed_C')) for c in cs),sum(bool(c.get('changed_H')) for c in cs),sum(bool(c.get('certainty_only')) for c in cs)]+[sum(c.get('confidence')==a for c in cs) for a in ['high','medium','low']])
 rows=[]
 for c in cs:
  ev=c.get('scan_shows','')
  if c.get('crop'):ev+=f" Evidence: {c['crop']}; original box {c.get('box')}."
  for j,p in enumerate(c.get('supporting_crops',[])):
   bs=c.get('supporting_boxes',[]);ev+=f" Additional evidence: crops/{Path(p).name}; original box {bs[j] if j<len(bs) else 'see crop manifest'}."
  rows.append([c.get('id',''),c.get('line',''),c.get('c',''),c.get('h',''),c.get('final',''),ev,c.get('confidence','')])
  if c.get('consequential'):major.append(f"- {label}, {c.get('line','')}: {c.get('final','')} — {c.get('scan_shows','')}")
  if c.get('changed_H') and not c.get('certainty_only'):
   coll.append(dict(folder=m['folder'],their_page=m['their_page'],our_scan=m['our_scan'],line=c.get('line',''),their_reading=c.get('h',''),codex_reading=c.get('c',''),final_reading=c.get('final',''),scan_shows=ev,kind=c.get('kind','other'),marked_in_H='yes' if c.get('marked_in_H') else 'no',confidence=c.get('confidence','')))
 ds=r.get('doubts',[])
 section=f'## {label} — {page}\n\n'+tab(['ID','Place','C','H','Consolidated','Ink and evidence','Confidence'],rows)+'\n### Still unresolved\n\n'
 section+=tab(['Place','Reading','Alternatives','Confidence','Reason'],[[d.get(k,'') for k in ['line','reading','alternatives','confidence','reason']] for d in ds]) if ds else 'None recorded.\n'
 decision_file=O/'second'/f'{page}_decisions.json'
 if decision_file.exists():
  blind_changes=[d for d in json.loads(decision_file.read_text()) if d.get('changed')]
  section+='\n### Changes after the blind second reading\n\n'
  section+=tab(['Box','First reading, written before comparison','Blind second reading','Final decision','Ink and evidence'],[[d.get('box',''),d.get('first',''),d.get('second',''),d.get('final',''),d.get('reason','')+f" Evidence: {d.get('crop','')}; original box {d.get('coords',[])}."] for d in blind_changes]) if blind_changes else 'No change to the consolidated reading after crop adjudication. Every token difference, including equivalent markup and differing context, is recorded in the page’s second-reading decisions file.\n'
 sections.append(section)
 for d in ds:doubts.append([label]+[d.get(k,'') for k in ['line','reading','alternatives','confidence','reason']])
 for x in r.get('inventory',[]):
  x=dict(x);x['scan']=label;inv.append(x)
 notes.append(f'## {label}\n\n'+'\n\n'.join(f'[{label}-N{j:02}] {n}' for j,n in enumerate(r.get('reading_notes',r.get('notes',[])),1))+'\n')
 audits.append(f'## {label}\n\n'+'\n\n'.join(f'[{label}-A{j:02}] {n}' for j,n in enumerate(r.get('notes',[]),1))+'\n')
 hands.extend((label,h) for h in r.get('hand_log',[]));notation.extend((label,n) for n in r.get('notation',[]))
 for e in r.get('check_events',[]):
  checks.append(dict(statement_id=e.get('statement_id',label),date=e.get('date',r.get('decided_utc','')[:10]),who=e.get('who','GPT-6 Astra Pro; effort not exposed; SP117'),type=e.get('type','carried as background without fault found'),outcome=e.get('outcome','')))
 text=(O/'pages'/f'{page}.tex').read_text();text=re.sub(r'\\cotefile\{[^}]*\}\s*','',text)
 if m['cote']!=last:combined.append('\\cotefile{'+m['cote']+'}\n');last=m['cote']
 combined.append('% '+page+'\n'+text.strip()+'\n')
total=['TOTAL']+[sum(x[i] for x in counts) for i in range(1,7)]
intro='# Consolidated changes\n\nAll readings are adjudicated from the supplied scan images. C and H are draft witnesses. Only the selected scans are in scope. No OCR or external source was used. Boxes are in original whole-page pixels. H editorial notes, unrelated headings, and macro-only differences are excluded.\n\nCounts are recorded places, not tokens. Resolved C doubts are included when flagged; certainty-only rows change no underlying text.\n\n'
(O/f'{ID}_changes.md').write_text(intro+tab(['Scan','Against C','Against H','Certainty only','High','Medium','Low'],counts+[total])+'\n## Consequential corrections\n\n'+('\n'.join(major) or 'None recorded yet.')+'\n\n'+'\n'.join(sections))
savecsv(f'{ID}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],coll,'\t')
savecsv(f'{ID}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inv)
(O/f'{ID}_transcription.tex').write_text('\n'.join(combined))
(O/f'{ID}_notes.md').write_text('# Notes while reading\n\nThese notes distinguish source statements from checks actually made here. Nothing beyond the supplied pages was researched. The supplied sweep correction rows name none of the selected scans; no S row was imported as authority.\n\n'+'\n'.join(notes))
(O/'transcription_audit.md').write_text('# Reading workflow and visual audit\n\nThese entries document image reading and editorial decisions. They are not mathematical proof checks.\n\n'+'\n'.join(audits))
extra=O/'work/additional_checks.tsv'
if extra.exists():checks.extend(csv.DictReader(extra.open(),delimiter='\t'))
savecsv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],checks,'\t')
nt=tab(['Observed on','Reading and convention'],notation)
if records:(O/'notation.md').write_text('# Running notation table\n\n'+nt)
a=O/'work/abbreviations.md';l=O/'work/legibility.md'
(O/f'{ID}_doubts.md').write_text('# Notation table\n\n'+nt+'\n# Remaining doubts\n\n'+tab(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubts)+'\n# Abbreviations\n\n'+(a.read_text() if a.exists() else 'Consolidation in progress.')+'\n# Legibility and witnesses\n\n'+(l.read_text() if l.exists() else 'Review in progress.'))
(O/f'{ID}_hand_log.md').write_text('# Hand and notation log\n\nObservations apply only where their scope is stated. Earlier habits supplied with the task were leads, not established readings of these sheets.\n\n'+tab(['Pages','Observation, scope, and witness effect'],hands))
kinds=['misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'];feedback=[]
for k in kinds:
 hits=[(l,c) for l,c in allchanges if c.get('kind')==k and not c.get('certainty_only')]
 feedback.append([k,len(hits),sum(bool(c.get('changed_C')) for _,c in hits),sum(bool(c.get('changed_H')) for _,c in hits),'; '.join(l+':'+c.get('id','') for l,c in hits)])
(O/f'{ID}_sheet_feedback.md').write_text('# Feedback on the error sheet\n\nOne adjudicated place is counted once under its primary kind. Pure confidence and macro changes are excluded.\n\n'+tab(['Kind','Places','Against C','Against H','Places in changes log'],feedback)+'\n## Additional patterns\n\n'+'\n'.join('- '+l+': '+str(h) for l,h in hands)+'\n')
print(f'Assembled {len(records)} pages; {len(allchanges)} apparatus rows; {len(coll)} H collation rows; {len(inv)} inventory elements.')
