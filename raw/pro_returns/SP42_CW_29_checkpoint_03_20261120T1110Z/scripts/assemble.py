"""Assemble decided pages and their evidence records, without altering readings."""
from pathlib import Path
import csv,json,collections,sys
OUT=Path(__file__).resolve().parents[1]
def md(s):
 return str(s if s is not None else '').replace('\n','<br>').replace('|','\\|')
def code(s):
 import re
 value=str(s if s is not None else '').replace('\n',' ')
 fence='`'*(max([len(x) for x in re.findall(r'`+',value)]+[0])+1)
 return fence+' '+value+' '+fence
def table(headers,rows):
 return '| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+''.join('| '+' | '.join(md(c) for c in r)+' |\n' for r in rows)
decisions=[json.loads(f.read_text()) for f in sorted((OUT/'decisions').glob('scan*.json'))]
counts=[];total=collections.Counter();consequential=[];witness_counts=[];witness_total=collections.Counter()
for d in decisions:
 changes=[r for r in d['rows'] if r['against_c'] or r['against_h']]
 c=collections.Counter(r['confidence'] for r in changes)
 c['C']=sum(r['against_c'] for r in d['rows']);c['H']=sum(r['against_h'] for r in d['rows'])
 c['confirmations']=len(d['rows'])-len(changes)
 total.update(c);counts.append([f"{d['scan']:03d}",c['C'],c['H'],c['high'],c['medium'],c['low'],c['confirmations']])
 wc=collections.Counter()
 for r in d['rows']:
  for witness,flag in [('C','against_c'),('H','against_h')]:
   if r[flag]:wc[witness+'_'+r['confidence']]+=1
 witness_total.update(wc)
 witness_counts.append([f"{d['scan']:03d}"]+[wc[k] for k in ['C_high','C_medium','C_low','H_high','H_medium','H_low']])
 for r in d['rows']:
  if r.get('consequential'):consequential.append(f"- Scan {d['scan']:03d}, {r['place']}: {r['consequential']}")
text='# SP42_CW_29 — changes and adjudications\n\n'
text+='Counts are distinct recorded loci, not words. A locus may differ from both witnesses. Confidence counts concern changed loci; retained C doubts and S confirmations without a change are additional records. Pure macro-syntax and layout differences are excluded. Reader R1/R2/R3 readings are preserved at disputed loci and in the independent returns.\n\n'
text+=table(['Scan','Against C','Against H','High','Medium','Low','Additional confirmations'],counts+[['TOTAL',total['C'],total['H'],total['high'],total['medium'],total['low'],total['confirmations']]])
text+='\n### Confidence by witness\n\n'+table(['Scan','C high','C medium','C low','H high','H medium','H low'],witness_counts+[['TOTAL']+[witness_total[k] for k in ['C_high','C_medium','C_low','H_high','H_medium','H_low']]])
text+='\n## Consequential corrections\n\n'+('\n'.join(consequential) if consequential else 'None recorded in the pages decided so far.')+'\n'
collation=[];inv=[];events=[];notes='# SP42_CW_29 — notes while reading\n\nThese notes use only the supplied pages and witnesses. They distinguish what the page says from any mathematical check performed in this run. A transcription reading is never corrected from mathematical expectation.\n'
doubtrows=[];abbreviations={};slips=[]
workflow='# SP42_CW_29 — workflow record\n\n## Reading arrangement\n\nPages are handled in ascending archive scan order. Each page receives three new sub-agents, with no inherited conversation or previous-page images. Each receives only its page images, C and H page excerpts, page-specific earlier questions, the conventions, and a snapshot of the evolving notation table. Readers do not exchange returns. The main reader compares the three completed readings and personally views evidence crops for adjudications. No OCR, image text-recognition library, PDF text layer, or outside research is used.\n\nThe independent readings and structured reports are retained under `readers/`; their original decisions are never rewritten to conceal disagreements. Main-reader decisions are under `decisions/`. Derived crops are evidence records; source scans, full witness packages and attached files are not included.\n\n## Brief versions\n\n'
for f in sorted((OUT/'briefs').glob('*.md')):
 workflow+=f'- `{f.relative_to(OUT)}`\n'
workflow+='\n## Per-page execution\n\n'
wfrows=[]
for d in decisions:
 scan=d['scan'];text+=f'\n## Scan {scan:03d} — {d["folder"]}; H page {d["their_page"]}\n\n'
 rows=[]
 for r in d['rows']:
  read=r.get('readers',{})
  readings='; '.join(k+': '+v for k,v in read.items())
  evidence=r['scan_shows']
  if r.get('crop'):evidence+=' [Evidence: '+str(r['crop'])+']'
  if r.get('s_where'):evidence+=' S: '+r['s_where']+' — '+r.get('s_decision','')
  rows.append([r['place'],code(r['c']),code(r['h']),code(r['final']),evidence,r['confidence'],readings])
  if r['against_h']:
   collation.append(dict(folder=d['folder'],their_page=d['their_page'],our_scan=scan,line=r['place'],their_reading=r['h'],codex_reading=r['c'],final_reading=r['final'],scan_shows=evidence,kind=r['kind'],marked_in_H='yes' if r['marked_in_H'] else 'no',confidence=r['confidence']))
 text+=table(['Place','C','H','Consolidated','What the scan shows / decision','Confidence','Independent readers'],rows) if rows else 'No substantive difference from either witness and no C doubt to adjudicate.\n'
 text+='\n### Still unresolved\n\n'
 if d.get('doubts'):
  for u in d['doubts']:
   text+=f"- {u['place']}: {code(u['reading'])}; alternatives: {md(', '.join(u.get('alternatives',[])))}. {u.get('reason','')}\n"
   doubtrows.append([scan,u['place'],code(u['reading']),'; '.join(u.get('alternatives',[])),u['confidence'],u.get('reason','')])
 else:text+='None.\n'
 for i in d['inventory']:inv.append(dict(scan=scan,**i))
 for e in d.get('check_events',[]):events.append(e)
 n=d['notes'];notes+=f'\n## Scan {scan:03d}\n\n{n["content"]}\n\n'
 for title,key in [('Mathematics and reading decisions','math_reading_decisions'),('The page’s own checks and doubts','author_checks'),('Titles, dates and page counts','titles_dates_pages')]:
  notes+=f'### {title}\n\n'
  vals=n.get(key,[]);notes+=('\n'.join('- '+s for s in vals) if vals else 'None.')+'\n\n'
 for a in d.get('abbreviations',[]):abbreviations.setdefault(a['form'],set()).add(a['expansion'])
 slips.extend((scan,s) for s in d.get('slips',[]))
 w=d['workflow'];wfrows.append([f'{scan:03d}',w['brief'],w.get('r1_crops',0),w.get('r2_crops',0),w.get('r3_crops',0),w.get('main_crops',0),w.get('main_reader_crops_viewed','not separately tabulated'),w.get('feedback','')])
workflow+=table(['Scan','Brief','R1 crops','R2 crops','R3 crops','Main new crops','Reader crops inspected by main','Observation / adaptation'],wfrows)
wp=OUT/'workflow_assessment.md'
if wp.exists():workflow+='\n'+wp.read_text()
brief_files=sorted((OUT/'briefs').glob('*.md'))
if brief_files:
 workflow+='\n## First brief, verbatim\n\n'+brief_files[0].read_text()
 if len(brief_files)>1:workflow+='\n## Latest issued brief, verbatim\n\n'+brief_files[-1].read_text()
(OUT/'SP42_CW_29_changes.md').write_text(text)
for filename,fields,data in [
 ('SP42_CW_29_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation),
 ('SP42_CW_29_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inv),
 ('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)]:
 with (OUT/filename).open('w',newline='') as f:
  wr=csv.DictWriter(f,fieldnames=fields,delimiter='\t' if filename.endswith('.tsv') else ',',extrasaction='ignore');wr.writeheader();wr.writerows(data)
(OUT/'SP42_CW_29_notes.md').write_text(notes)
doubts=(OUT/'notation.md').read_text()+'\n## Remaining doubts\n\n'
doubts+=table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubtrows) if doubtrows else 'None in the pages decided so far.\n'
doubts+='\n## Abbreviations encountered\n\nThe proposed expansions in this list do not alter the transcription.\n\n'
doubts+=table(['Form','Proposed expansion'],[[k,'; '.join(sorted(v))] for k,v in sorted(abbreviations.items())])
doubts+='\n## Slips retained as written\n\n'+('\n'.join(f'- Scan {s:03d}: {t}' for s,t in slips) if slips else 'See the page-by-page notes and changes log.')+'\n'
lp=OUT/'legibility_assessment.md'
if lp.exists():doubts+='\n'+lp.read_text()
(OUT/'SP42_CW_29_doubts.md').write_text(doubts)
(OUT/'SP42_CW_29_workflow.md').write_text(workflow)
combined='\n\n'.join((OUT/'pages'/d['filename']).read_text().rstrip() for d in decisions)+'\n'
(OUT/'SP42_CW_29_transcription.tex').write_text(combined)
print(json.dumps({'decided_pages':len(decisions),'changes_C':total['C'],'changes_H':total['H'],'remaining_doubts':len(doubtrows),'inventory_rows':len(inv),'check_events':len(events)}))
