#!/usr/bin/env python3
"""Mechanical catalogue of supplied research context; never reads manuscript files."""
from pathlib import Path
from collections import Counter,defaultdict
from datetime import datetime,timezone
import re,json,csv,hashlib
root=Path(__file__).resolve().parents[1]
context=root.parent/'context'
work=root/'working'
state_path=context/'notes/RESULTS_STATE.md'
state_lines=state_path.read_text().splitlines()
state=[]
for lineno,line in enumerate(state_lines,1):
 m=re.match(r'^- \*\*(.+?)\*\* \[([^\]]*)\] (.*)$',line)
 if m:
  id_,status,body=m.groups()
  src=re.search(r'\(([^()]*(?:\.csv|\.md))\)\s*$',body)
  loc=re.search(r' Where: (.*?)(?: \([^()]*(?:\.csv|\.md)\))?$',body)
  state.append({'id':id_,'source_file':'notes/RESULTS_STATE.md','source_line':lineno,'status_exact':status,'text_exact':body,'register_source_file':src.group(1) if src else None,'manuscript_locator_exact':loc.group(1) if loc else None,'contains_ellipsis':'…' in body,'raw_line':line})
index=defaultdict(list)
for r in state:index[r['id']].append(r)
def pattern(id_):return re.compile(r'(?<![A-Za-z0-9_])'+re.escape(id_)+r'(?![A-Za-z0-9_.])')
def mentions(id_):
 p=pattern(id_)
 return [{'source_line':n,'text_exact':l} for n,l in enumerate(state_lines,1) if p.search(l)]
def refs(text):
 return [{'id':id_,'state_source_lines':[x['source_line'] for x in records],'state_statuses_exact':[x['status_exact'] for x in records]} for id_,records in index.items() if pattern(id_).search(text)]
dossier=[]
for lineno,line in enumerate((context/'DOSSIER_STATEMENTS_WITH_STATUS.md').read_text().splitlines(),1):
 if not re.match(r'^\| (STRATA|PATHS|BISITE|RESIDUE) ',line):continue
 assert line.startswith('| ') and line.endswith(' |')
 cells=line[2:-2].split(' | ')
 assert len(cells)==4,(lineno,len(cells))
 id_,statement,status,locator=cells
 dossier.append({'id':id_,'source_id':id_,'run':id_.split()[0],'source_file':'DOSSIER_STATEMENTS_WITH_STATUS.md','source_line':lineno,'statement_exact':statement,'status_exact':status,'manuscript_locator_exact':locator,'locator_present':bool(locator),'statement_contains_ellipsis':'…' in statement,'state_same_id_entries':index.get(id_,[]),'state_same_id_mentions':mentions(id_),'state_referenced_entries':refs(' '.join(cells)),'raw_row':line})
assert len(dossier)==255 and len({r['id'] for r in dossier})==255
new=[]
explicit_refs={1:['CATHOT G.4'],2:[],3:['CATHOT E.17','GALOIS B.10','GALOIS B.11','GALOIS B.12'],4:['CATHOT D.6'],5:['CATHOT G.8'],6:['CATHOT G.14','CATHOT G.15','CATHOT G.9'],7:['POLES F.14'],8:['TOTASPH A.13'],9:[],10:[],11:['TOTASPH C.5','TOTASPH C.6','TOTASPH C.7','TOTASPH C.8','TOTASPH C.9','TOTASPH C.10'],12:['CATHOT G.4','CATHOT G.6']}
for lineno,line in enumerate((context/'NEW_RESULTS.md').read_text().splitlines(),1):
 if not re.match(r'^\| \d+ ',line):continue
 cells=line[2:-2].split(' | ')
 assert len(cells)==6,(lineno,len(cells))
 number,statement,proof,author,checked,locator=cells
 n=int(number)
 new.append({'id':f'NEW_RESULTS {n}','source_id':number,'catalog_key':f'NR{n:02d}','source_file':'NEW_RESULTS.md','source_line':lineno,'entry_type':'numbered','statement_exact':statement,'proof_locator_exact':proof,'proved_by_exact':author,'checked_by_exact':checked,'status_exact':None,'status_note':'The source has no formal status column; the exact review status is preserved in checked_by_exact. Its heading describes these as results proved while writing the companion.','manuscript_locator_exact':locator,'statement_contains_ellipsis':'…' in statement,'explicit_run_ids_from_source':explicit_refs[n],'state_referenced_entries':refs(' '.join(cells)),'state_explicit_id_matches':[{'id':i,'entries':index.get(i,[]),'mentions':mentions(i)} for i in explicit_refs[n]],'raw_row':line})
assert [r['source_id'] for r in new]==[str(i) for i in range(1,13)]
newlines=(context/'NEW_RESULTS.md').read_text().splitlines()
coda_start=next(i for i,l in enumerate(newlines) if l.startswith('Known after all'))
assert len([l for l in newlines[coda_start:] if l.strip()])==3
coda_status='Known after all (listed so that nobody claims them)'
for k,line in enumerate(newlines[coda_start:],1):
 if not line.strip():continue
 text=line.split(': ',1)[1] if k==1 else line
 # Retain the source punctuation (including separating semicolons).
 inherited=explicit_refs[11] if k==1 else []
 new.append({'id':f'NEW_RESULTS unnumbered coda {k}','source_id':None,'catalog_key':f'NRK{k}','source_file':'NEW_RESULTS.md','source_line':coda_start+k,'entry_type':'unnumbered_known_coda','statement_exact':text,'status_exact':coda_status,'checked_by_exact':None,'proved_by_exact':None,'proof_locator_exact':None,'manuscript_locator_exact':'item 11' if k==1 else None,'locator_note':'No independent manuscript page locator is supplied for this coda entry.','explicit_numbered_item_reference':11 if k==1 else None,'explicit_run_ids_from_source':[],'state_referenced_entries':refs(text),'state_matches_inherited_from_item_11':[{'id':i,'entries':index.get(i,[]),'mentions':mentions(i)} for i in inherited],'raw_row':line})
assert len(new)==15
metadata={'created_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'method':'Exact source-cell extraction using the literal Markdown column delimiter space-pipe-space. Mathematical escaped bars remain unchanged. Only supplied context was read; no scans or frozen transcription was read by this agent.','state_cross_reference_method':'Exact same-ID state entries and occurrences, plus exact named state IDs found in the source row. NEW_RESULTS explicit run-ID ranges are expanded only when named by that row. These are mechanical references, not an assessment of mathematical equivalence.','source_hashes':{str(p.relative_to(context)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [context/'README.md',state_path,context/'NEW_RESULTS.md',context/'DOSSIER_STATEMENTS_WITH_STATUS.md']},'counts':{'dossier_total':len(dossier),'dossier_by_run':dict(Counter(r['run'] for r in dossier)),'new_results_total':len(new),'new_results_numbered':12,'new_results_unnumbered_coda':3,'state_structured_entries':len(state),'dossier_exact_same_id_state_entries':sum(bool(r['state_same_id_entries']) for r in dossier),'dossier_empty_locators':sum(not r['locator_present'] for r in dossier)},'dossier_status_counts':dict(Counter(r['status_exact'] for r in dossier))}
data={'metadata':metadata,'new_results':new,'dossier_statements':dossier,'results_state_entries':state}
(work/'context_catalog.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
with (work/'context_catalog.csv').open('w',newline='') as f:
 cols=['dataset','id','source_line','status_exact','checked_by_exact','manuscript_locator_exact','state_exact_ids']
 writer=csv.DictWriter(f,fieldnames=cols);writer.writeheader()
 for r in new+dossier:
  writer.writerow({'dataset':'DSS' if r in dossier else 'NEW_RESULTS','id':r['id'],'source_line':r['source_line'],'status_exact':r.get('status_exact') or '', 'checked_by_exact':r.get('checked_by_exact') or '', 'manuscript_locator_exact':r.get('manuscript_locator_exact') or '', 'state_exact_ids':'; '.join(x['id'] for x in r.get('state_referenced_entries',[]))})
missing=[r['id'] for r in dossier if not r['locator_present']]
markers=[r['id'] for r in dossier if r['statement_contains_ellipsis']]
same=[r for r in dossier if r['state_same_id_entries']]
report=['# Mechanical context coverage catalogue','',f"Created {metadata['created_utc']}.",'','## Source coverage','',f"- DSS: **{len(dossier)}** rows; STRATA 10, PATHS 76, BISITE 113, RESIDUE 56.",'- NEW_RESULTS: **15** items: numbered rows 1–12 and three unnumbered “Known after all” coda entries (Isbell–Mitchell; Nielsen realization; localiseur spécial/accessibility).','- DSS IDs are unique. No missing numerical IDs have been invented or repaired; the source selects particular sections.','- All 255 DSS rows have exactly four table columns; all 12 numbered NEW_RESULTS rows have exactly six. The internal mathematical bar in BISITE A.28 is preserved.','- No pre-existing partial catalog files were found before this catalog was written.','','## Status and locator boundaries','',"- DSS statuses are copied literally, including `claim (return: ...)`; no status is upgraded.",'- NEW_RESULTS has no formal status column. The exact `Checked by` and `Proved by` cells are retained separately; the three coda items retain their shared “Known after all” status.',f"- DSS has {len(missing)} blank manuscript-locator cells: "+'; '.join(missing)+'.',f"- DSS statement cells containing an ellipsis character: {', '.join(markers) if markers else 'none'}. No explicit source truncation marker was found in the DSS statement cells; this does not certify source correctness or completeness of the original research returns.",'- Many RESULTS_STATE excerpts are visibly truncated with an ellipsis. The exact excerpts, status text, line numbers and original register-source filenames are preserved in the JSON; no missing statement text is reconstructed.','- The three coda entries are short bibliographic notices; only the Isbell–Mitchell notice points back to numbered item 11, and none supplies its own manuscript page range.','','## Exact same-ID RESULTS_STATE entries','',f'{len(same)} of the 255 DSS IDs have their own structured status entry in RESULTS_STATE:','']
for r in same:
 report.append('- '+r['id']+': '+', '.join(f"state line {x['source_line']} [{x['status_exact']}]" for x in r['state_same_id_entries']))
report+=['','The JSON also records mentions of each DSS ID elsewhere in RESULTS_STATE and exact named cross-references found in its statement/locator; these are references only, not substantive manuscript judgments.','','## Files','', '- `working/context_catalog.json`: exact source statements and metadata, including the structured state-entry index.','- `working/context_catalog.csv`: flat status/locator/ID reference index.','- `scripts/catalog_context.py`: reproducible extraction and coverage assertions.','']
(work/'context_catalog_report.md').write_text('\n'.join(report))
print(json.dumps(metadata['counts'],ensure_ascii=False,indent=2))
print('DSS statuses:',metadata['dossier_status_counts'])
print('DSS blank locators:',missing)
print('DSS ellipsis markers:',markers)
print('Wrote working/context_catalog.json, .csv, _report.md; script scripts/catalog_context.py')
