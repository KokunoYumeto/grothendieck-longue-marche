#!/usr/bin/env python3
"""Assemble reviewed research components; never modify the frozen transcription."""
from pathlib import Path
import datetime as dt
import hashlib
import json
import re

root=Path(__file__).resolve().parents[1]
records=root/'records'
def read(name):
    return (records/name).read_text()
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

parts={name:read(name) for name in [
    'research_summary.md','research_root_draft.md','research_standing_sections_draft.md',
    'research_ps_comparison_draft.md','research_new_results_draft.md','research_dossier_map_draft.md'
]}
dossier=json.loads(read('research_dossier_coverage.json'))
assert dossier['mapped_count']==dossier['source_row_count']==255
assert all(dossier['validation'].get(k) for k in [
    'all_255_ids_exact_and_in_source_order','all_255_source_rows_exact',
    'all_255_status_claims_exact','all_current_quotes_exact_at_reported_source_lines',
    'all_45_frozen_source_hashes_unchanged','markdown_has_all_255_item_headings_once_in_source_order'
])

main=parts['research_root_draft.md'].split('\n',1)[1].strip()
assert re.findall(r'^### (R\d{3}) —',main,re.M)==[f'R{i:03d}' for i in range(1,83)]
review=read('research_root_review.md')
assert digest(records/'research_root_draft.md') in review, 'Root notes changed since the recorded review.'

standing=parts['research_standing_sections_draft.md']
standing=standing[standing.index('## 1. Every literal question-mark row'):]
standing=standing.replace('## 1. Every literal question-mark row','## Standing question: steps the manuscript marks as unverified\n\n### Literal question marks')
standing=standing.replace('## 2. Verbal questions, proof obligations and explicit rewriting flags','## Verbal questions, proof obligations and explicit rewriting flags')
standing=standing.replace('## 3. Explicit incomplete phrases and formulas','## Explicit incomplete phrases and formulas')
standing=standing.replace('## 4. Sheet-by-sheet titles and pagination','## Standing question: title sheets and page counts')
standing=standing.replace('## 5. Withdrawn and revised claims or wording','## Withdrawn and revised claims or wording')
standing=standing.replace('## 6. Coverage audit','## Standing-section coverage audit')
standing=standing.replace('## 3A. Qualifications and emphasis in support text','## Qualifications and emphasis in support text')
standing=standing.replace('## 3B. Other literal NB and OK markers','## Other literal NB and OK markers')
standing=standing.replace('The draft adds 9 verbal/attention entries','The register adds 9 verbal/attention entries')
standing=standing.replace('; no transcription, doubts, inventory, progress, root draft or main notes file was edited.','; the standing-section research was conducted on the frozen text and made no changes to it.')
standing=re.sub(r'^(### Q\d{3}[^\n]+)$',r'\1\n\n**Kind: self-flagged.**',standing,flags=re.M)
standing=re.sub(r'^(### V\d{3}[^\n]+)$',r'\1\n\n**Kind: self-flagged / source rewriting signal.**',standing,flags=re.M)
standing=re.sub(r'^(### U\d{3}[^\n]+)$',r'\1\n\n**Kind: reading question / unfinished expression.**',standing,flags=re.M)
standing=re.sub(r'^(### S\d{3}[^\n]+)$',r'\1\n\n**Kind: reading question / qualified source assertion.**',standing,flags=re.M)
standing=re.sub(r'^(### K\d{3}[^\n]+)$',r'\1\n\n**Kind: reading question / source checkpoint.**',standing,flags=re.M)

ps=parts['research_ps_comparison_draft.md']
ps=ps[ps.index('## Cluster-by-cluster comparison'):]
ps=ps.replace('## Cluster-by-cluster comparison','## Comparison with the supplied Pursuing Stacks typescript')
ps_ids=[]
def ps_item(m):
    n=int(m.group(1));ps_ids.append(n)
    title=m.group(2);body=m.group(3)
    kind='reading question' if n>=37 or n==1 else 'unpursued implication / source comparison'
    if n in [7,10,14,16,19,21,23,26,31,33,34]:kind='self-flagged / source comparison'
    return f'### PS{n:02d} — {title}\n\n**Kind: {kind}.**\n\n{body}'
ps=re.sub(r'^(\d+)\. \*\*(.*?)\*\* (.+)$',ps_item,ps,flags=re.M)
assert ps_ids==list(range(1,46)),ps_ids

new=parts['research_new_results_draft.md']
new=new[new.index('## A. Every NEW_RESULTS entry'):]
new=new.replace('## A. Every NEW_RESULTS entry','## Every NEW_RESULTS entry and closing attribution')
new=new.replace('## B. All 26 open RESULTS_STATE entries mapped to the frozen pages','## All 26 open RESULTS_STATE entries mapped to the frozen pages')
new=new.replace('## Coverage and limits','## NEW_RESULTS and open-state coverage')
new=re.sub(r'^(### (?:NEW_RESULTS \d+|Closing entry K\d+|\d+\.)[^\n]*)$',r'\1\n\n**Kind: reading question / context-statement mapping.**',new,flags=re.M)
assert len(re.findall(r'^### NEW_RESULTS \d+',new,re.M))==12
assert len(re.findall(r'^### Closing entry K\d+',new,re.M))==3
assert len(re.findall(r'^### \d+\. ',new,re.M))==26

dos=parts['research_dossier_map_draft.md']
dos=dos.split('\n',1)[1].strip()
dos='## Every DOSSIER_STATEMENTS_WITH_STATUS statement\n\n'+dos
dos=dos.replace('## Scope and reading controls','### Dossier scope and reading controls')
dos=dos.replace('No item is assigned **present form** in this draft.','No item is assigned **present form** in this mapping.')
dos=dos.replace('No image was read, and this research changed no transcription, inventory, doubt register or progress log.','The dossier mapping was made from the frozen text after the primary reader had completed the visual transcription and audit; the mapping did not change those source files.')
for fam in ['STRATA','PATHS','BISITE','RESIDUE']:
    dos=dos.replace(f'## {fam}\n',f'## Dossier family {fam}\n')
byid={r['id']:r for r in dossier['rows']}
dos_ids=[]
def dos_item(m):
    ident=m.group(1);dos_ids.append(ident)
    kind='unpursued implication' if byid[ident]['classification']=='related-method' else 'reading question'
    return f'### {ident}\n\n**Kind: {kind} / context-statement mapping.**'
dos=re.sub(r'^### ((?:STRATA|PATHS|BISITE|RESIDUE) [^\n]+)$',dos_item,dos,flags=re.M)
assert dos_ids==[r['id'] for r in dossier['rows']]

summary=parts['research_summary.md'].strip()
sources_note='''## Citation, coverage, and preservation record

The current-page evidence in these notes comes from the frozen diplomatic transcription and the primary reader's two visual passes. Research helpers used that frozen text after the context boundary; none transcribed or selected a reading from scan images. The principal source passages and explicit formulas were checked during integration, and `records/research_root_review.md` records the applied source-fidelity corrections to R001–R082.

The standing sections point back to R-items for mathematical context and RESULTS_STATE links; the material-only entries preserve titles and production data without assigning an unrelated mathematical status. The word “first” in the historical entries is always limited to the explicit witnesses located within the supplied context searches. Referenced research returns that were named but not supplied were not reconstructed from their filenames.

All 82 main items have recorded text-search groups in `records/research_context_search_ledger.json`; the three comparison manifests record the PS, NEW_RESULTS/open-state, and 255-row dossier search coverage. Searches, extracted lines, and source-ID checks aid reproducibility; they do not independently prove the mathematical claims copied from a register. The final unchanged-hash verification is recorded in `progress.log`, covering all 44 page fragments and their combined source.
'''
out='# Research notes — MPL_134-8_043-087\n\n'+ '\n\n'.join([summary,main,standing.strip(),ps.strip(),new.strip(),dos.strip(),sources_note.strip()])+'\n'
assert 'Research in progress; remaining sections' not in out
assert not re.search(r'Status: in progress; \d+/255',out)
target=root/'MPL_134-8_043-087_notes.md'
target.write_text(out)
manifest={
 'integrated_utc':dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
 'source_components':{name:digest(records/name) for name in parts},
 'note_file':target.name,'note_sha256':digest(target),'words_approx':len(out.split()),
 'main_items':82,'historical_summary_items':4,'ps_items':45,'new_numbered':12,'new_closing':3,
 'open_state_items':26,'dossier_items':255,'dossier_family_counts':dossier['family_counts'],
 'dossier_relation_counts':dossier['classification_counts'],
 'standing_section_coverage':json.loads(read('research_standing_sections_coverage.json'))['coverage'],
 'frozen_transcription_changed':False,
 'notes_only_transformations':['heading levels and stable PS IDs','explicit per-item note-kind labels','integration of reviewed components','overview and preservation record'],
}
(records/'research_integration.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:manifest[k] for k in ['note_file','note_sha256','words_approx','main_items','ps_items','new_numbered','new_closing','open_state_items','dossier_items']},indent=2))
