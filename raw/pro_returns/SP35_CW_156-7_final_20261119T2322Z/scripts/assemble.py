#!/usr/bin/env python3
"""Rebuild documentary deliverables from adjudicated per-page records."""
from pathlib import Path
import csv,json,collections
root=Path(__file__).resolve().parents[1]
records=[json.loads(p.read_text()) for p in sorted((root/'records').glob('scan[0-9][0-9][0-9].json'))]
def md(s):return str(s if s is not None else '').replace('|','\\|').replace('\n','<br>')
def code(s):return '<code>'+md(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')+'</code>'
changes=['# Changes and adjudications','', '## Counts','', 'Counts are loci in the tables below. A resolved doubt counts against C; a retained unchanged doubt is recorded but is not counted as a change. Pure equivalent macro syntax does not count. Confidence describes the final ink reading, not the mathematical correctness of the manuscript.','', '| Scan | Against C | Against H | High / medium / low (changed loci) | C doubts reviewed |','|---:|---:|---:|---|---:|']
totC=totH=0;totconf=collections.Counter();nd=0
for r in records:
 rows=r['decisions'];cc=sum(bool(x.get('diff_C')) for x in rows);hh=sum(bool(x.get('diff_H')) for x in rows)
 conf=collections.Counter(x['confidence'] for x in rows if x.get('diff_C') or x.get('diff_H'))
 doubts=len(r.get('C_doubt_audit',[]));nd+=doubts
 changes.append(f"| {r['scan']:03d} | {cc} | {hh} | {conf['high']} / {conf['medium']} / {conf['low']} | {doubts} |")
 totC+=cc;totH+=hh;totconf.update(conf)
changes+= [f"| **Total** | **{totC}** | **{totH}** | **{totconf['high']} / {totconf['medium']} / {totconf['low']}** | **{nd}** |",'', '## Consequential corrections and retained manuscript slips','']
conseq=[]
for r in records:
 for d in r['decisions']:
  if d.get('math_consequence'):conseq.append(f"- Scan {r['scan']:03d}, {d['id']}: {d['math_consequence']}")
changes+=conseq or ['None recorded in the pages adjudicated so far.']
changes+=['','## Reading and evidence conventions','', 'C = the supplied Codex witness; H = the supplied Commutator witness (commit aef7db2); S = the supplied sweep corrections. R1/R2/R3 are independent readers in this run. The final column records M’s adjudication. Full independent transcriptions, individual C-doubt audits and crop records are retained in readers/. Crops are named relative to this archive. “Half a/b” means the supplied full-resolution image. Mathematical expectations never replace manuscript ink.','', 'H’s emph macro marks the author’s emphasis, while its uncertain macro uses underlining as an uncertainty marker. Equivalent same-span emphasis conversions and the standard between/TikZ rendering of the same undecorated compatibility sign are not counted as changed readings. Genuine wording, span, decoration, state and placement differences remain. Documentary counting reviews are retained with review-only flags; see records/documentary_harmonization.json and the two reader audits.','']
collation=[];inventory=[];events=[];notes=['# Notes while reading','', 'Only scans 002–009 are considered. Statements are attributed to the manuscript unless expressly identified as an actual check in this run. A visual transcription check is not a proof. The check-event ledger separates background use, targeted mathematical checks and computations.',''];notation=[];doubts=[];abbrev=[]
for r in records:
 scan=r['scan'];changes+= [f'## Scan {scan:03d} — manuscript page {scan-1}','', '| ID / place | C | H | R1 / R2 / R3 | Final | What the scan shows; evidence | Confidence |','|---|---|---|---|---|---|---|']
 for d in r['decisions']:
  rs=d.get('readers',{});readers='<br>'.join(f'{k}: {code(rs.get(k,"same as final"))}' for k in ['R1','R2','R3'])
  evidence=md(d['evidence'])
  if d.get('crop'):evidence+=' Crop: '+md(d['crop'])+'.'
  if d.get('review_only'):evidence+=' Review only; no changed reading.'
  if d.get('S_id'):evidence+=' S row '+d['S_id']+': '+md(d.get('S_outcome',''))+'.'
  changes.append(f"| {md(d['id']+' · '+d['place'])} | {code(d['C'])} | {code(d['H'])} | {readers} | {code(d['final'])} | {evidence} | {d['confidence']} |")
  if d.get('diff_H'):
   collation.append({'folder':'H156-01','their_page':scan-1,'our_scan':scan,'line':d['place'],'their_reading':d['H'],'codex_reading':d['C'],'final_reading':d['final'],'scan_shows':d['evidence']+(' Crop: '+d['crop'] if d.get('crop') else ''),'kind':d['kind'],'marked_in_H':'yes' if d.get('marked_in_H') else 'no','confidence':d['confidence']})
 changes+=['', '### C doubt audit','', '| Place / witness C doubt | Decision | Evidence / decision ID |','|---|---|---|']
 for d in r.get('C_doubt_audit',[]):changes.append('| '+md(d.get('place','')+' · '+d['C'])+' | '+md(d['status']+'; '+d.get('final',''))+' | '+md(d.get('evidence',d.get('decision_id','')))+' |')
 changes+=['','### Still unresolved','']
 unresolved=r.get('unresolved',[])
 if unresolved:
  for u in unresolved:
   changes.append('- '+md(u['place'])+': '+code(u['reading'])+'; alternatives: '+code(u.get('alternatives','none separately legible'))+' ('+u['confidence']+'). '+u.get('reason',''))
   doubts.append(dict(u,scan=scan))
 else:changes.append('None.')
 changes.append('')
 for i,x in enumerate(r['inventory'],1):inventory.append({'scan':scan,'sheet_kind':x.get('sheet_kind','text'),'hand':x.get('hand','his hand'),'element':x.get('element',f'{scan:03d}-{i:02d}'),'kind':x['kind'],'position':x['position'],'first_words_or_objects':x['first_words_or_objects'],'transcribed':'yes'})
 events+=r.get('check_events',[])
 notes += [f'## Scan {scan:03d} — manuscript page {scan-1}','']+r.get('notes',[])+['']
 notation+=r.get('notation',[]);abbrev+=r.get('abbreviations',[])
(root/'SP35_CW_156-7_changes.md').write_text('\n'.join(changes)+'\n')
for fn,data,fields,delimiter in [
 ('SP35_CW_156-7_collation.tsv',collation,['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],'\t'),
 ('SP35_CW_156-7_inventory.csv',inventory,['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],','),
 ('CHECK_EVENTS.tsv',events,['statement_id','date','who','type','outcome'],'\t')]:
 with (root/fn).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter);w.writeheader();w.writerows(data)
notes+=['## Documentary references','', 'Grothendieck, A. (1986). *Analysis situs (troisième mouture)* [Handwritten manuscript, 23 juin; Montpellier archive, cote 156-7, scans 2–9]. Supplied facsimile images.','', 'OpenAI. (2026, November 13–15). *H156-01: Diplomatic transcription of cote 156-7, scans 2–9* [Unverified AI witness C; GPT-6 Astra, reported reasoning effort max]. Supplied files.','', 'Commutator project. (2026). *Transcription of cote 156-7, batch 01* (commit aef7db2) [Unverified AI witness H, Michel Hua’s project]. Supplied files.','', 'Sweep 3. (2026, November 18–19). *156-7_CORRECTIONS.tsv* [Supplied AI witness S]. Only row SA21-K7-01 falls within the eight scans of this task.']
(root/'SP35_CW_156-7_notes.md').write_text('\n'.join(notes)+'\n')
master=root/'records/notation_master.json'
if master.exists():notation=json.loads(master.read_text())
db=['# Notation table','', '| Sign / usage | LaTeX | Ink evidence and locations | Status |','|---|---|---|---|']
for n in notation:db.append('| '+md(n['sign'])+' | '+code(n['latex'])+' | '+md(n['evidence'])+' | '+md(n.get('status','settled'))+' |')
db+=['','## Remaining doubts','', '| Scan | Place | Reading | Alternatives | Confidence | Reason |','|---:|---|---|---|---|---|']
for d in doubts:db.append(f"| {d['scan']:03d} | {md(d['place'])} | {code(d['reading'])} | {code(d.get('alternatives',''))} | {d['confidence']} | {md(d.get('reason',''))} |")
if not doubts:db.append('| — | None in adjudicated pages | | | | |')
db+=['','## Abbreviations','', 'Expansions here are interpretive aids; none is silently expanded in the transcription.','', '| Abbreviation | Proposed expansion | Location |','|---|---|---|']
seen=set()
for a in abbrev:
 key=(a['form'],a['meaning'])
 if key not in seen:db.append('| '+code(a['form'])+' | '+md(a['meaning'])+' | '+md(a['location'])+' |');seen.add(key)
leg=root/'records/legibility.md'
db+=['','## Legibility and witness comparison','',leg.read_text() if leg.exists() else 'Assessment pending the complete collation.']
(root/'SP35_CW_156-7_doubts.md').write_text('\n'.join(db)+'\n')
pagefiles=[root/'pages'/f"H156-01_156-7_scan{r['scan']:03d}.tex" for r in records]
if pagefiles:(root/'SP35_CW_156-7_transcription.tex').write_text('\n\n'.join(p.read_text().rstrip() for p in pagefiles)+'\n')
print(json.dumps({'pages':len(records),'changed_C':totC,'changed_H':totH,'confidence':dict(totconf),'C_doubts_reviewed':nd,'remaining_doubts':len(doubts),'inventory_elements':len(inventory),'H_collation_rows':len(collation),'check_events':len(events)},indent=2))
