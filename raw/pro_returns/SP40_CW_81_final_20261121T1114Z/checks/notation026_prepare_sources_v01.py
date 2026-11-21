#!/usr/bin/env python3
"""Exact source-only historical cells and scan026 root/locus authority index."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re
ROOT=Path('/workspace/scratch/94548b74fbe0')
OUT=ROOT/'out/checks'
FILES={
 'baseline_json':'out/checks/notation_audit_through025_preparation.json',
 'baseline_md':'out/checks/notation_audit_through025_preparation.md',
 'baseline_root_read':'out/checks/notation_audit_through025_root_preliminary_read.json',
 'root_decisions':'out/checks/scan026_root_decisions.json',
 'root_journal':'out/checks/scan026_root_journal.md',
 'root_crop_plan':'out/checks/scan026_root_crop_plan.json',
 'root_crop_audit':'out/checks/scan026_root_crop_audit.json',
 'root_locus_supplement':'out/checks/scan026_root_locus_supplement_v01.json',
 'root_reader_fullreview':'out/checks/scan026_root_text_progress_v05.json',
 'union':'out/checks/scan026_source_union_v01.json',
 'NREV_proposal':'out/checks/notation_NREV01_NREV02_public_report_proposal_v01.json',
 'NREV_proposal_md':'out/checks/notation_NREV01_NREV02_public_report_proposal_v01.md',
 'NREV_root_read':'out/checks/notation_NREV01_NREV02_root_preliminary_read.json',
 'NREV_map_dependency':'out/checks/notation_NREV01_NREV02_map_dependency_v01.json',
}
def sha(b):return hashlib.sha256(b).hexdigest()
def exact_json(x):return json.dumps(x,ensure_ascii=False,separators=(',',':')).encode('utf-8')
def write(name,value):
 p=OUT/name
 with p.open('x',encoding='utf-8') as f:json.dump(value,f,ensure_ascii=False,indent=2);f.write('\n')
 return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256_utf8':sha(p.read_bytes())}
raw={key:(ROOT/name).read_bytes() for key,name in FILES.items()}
docs={key:{'path':FILES[key],'bytes':len(b),'sha256_utf8':sha(b)} for key,b in raw.items()}
assert docs['baseline_json']['sha256_utf8']=='a410950b40eb25df5be17cb40e05e1fde1c8a28f33f583edff3f49e3aebf60b7'
assert docs['baseline_md']['sha256_utf8']=='3424de7deb35ac0df33b543cac26808d30335da3b0eaf1fb4f8b5404a7d95dc0'
base=json.loads(raw['baseline_json']);dec=json.loads(raw['root_decisions']);journal=raw['root_journal'].decode('utf-8');union=json.loads(raw['union']);supp=json.loads(raw['root_locus_supplement']);audit=json.loads(raw['root_crop_audit'])
assert len(base['exact_notation_rows'])==180 and len(base['recurring_form_families'])==14
assert len(dec['decisions'])==27 and len(union)==90
assert audit['total_distinct']==27 and len(audit['viewed_once'])==27
assert all(x['successful_display_count']==1 for x in audit['viewed_once'])
assert supp['physical_loci_total']==91 and supp['sigma_loci']==39 and supp['other_loci']==52
baseline_rows=[]
for i,row in enumerate(base['exact_notation_rows']):
 literal=row['source']['literal'];assert literal.startswith('| ') and literal.endswith(' |\n')
 cells=literal[2:-3].split(' | ');assert len(cells)==4
 assert '| '+' | '.join(cells)+' |\n'==literal
 cursor=2;spans=[]
 for cell in cells:
  assert literal[cursor:cursor+len(cell)]==cell
  spans.append({'char_start':cursor,'char_end_exclusive':cursor+len(cell),'value':cell});cursor+=len(cell)+3
 literal_sha=sha(literal.encode('utf-8'));assert literal_sha==row['source']['span_sha256_utf8']
 baseline_rows.append({'id':row['id'],'scan':row['scan'],'original_row_pointer':f'/exact_notation_rows/{i}','original_ordered_row_json_sha256':sha(exact_json(row)),'literal_pointer':f'/exact_notation_rows/{i}/source/literal','literal_sha256_utf8':literal_sha,'exact_cells_in_source_order':spans,'cell_semantics':'Source-position cells only; the original row object and original column wording are unchanged.','rejoin_rule':'Literal | SPACE, then the four exact cells separated by SPACE | SPACE, then SPACE | LF.'})
baseline={'schema':'notation026-frozen-baseline-cells-v1','source_only':True,'source_document':docs['baseline_json'],'markdown_document':docs['baseline_md'],'original_rows_unchanged':True,'original_families_unchanged':True,'row_count':180,'family_count':14,'family_objects_exact':base['recurring_form_families'],'rows':baseline_rows,'original_exact_rows_ordered_json_sha256':sha(exact_json(base['exact_notation_rows'])),'original_families_ordered_json_sha256':sha(exact_json(base['recurring_form_families'])),'historical_NREV_objects_pointer':'/concrete_root_review_items','historical_NREV_objects_ordered_json_sha256':sha(exact_json(base['concrete_root_review_items']))}
root_sections=[]
for i,x in enumerate(dec['decisions']):
 body=x['body'];assert journal.count(body)==1
 start=journal.index(body);end=start+len(body)
 root_sections.append({'section':x['section'],'root_decision_pointer':f'/decisions/{i}','exact_root_section_object':x,'ordered_root_section_json_sha256':sha(exact_json(x)),'journal_body_span':{'char_start':start,'char_end_exclusive':end,'utf8_byte_start':len(journal[:start].encode('utf-8')),'utf8_byte_end_exclusive':len(journal[:end].encode('utf-8')),'literal_sha256_utf8':sha(body.encode('utf-8')),'line_start':journal.count('\n',0,start)+1,'line_end':journal.count('\n',0,end)+1},'body_identical_in_root_json_and_journal':True})
loci=[]
for i,u in enumerate(union):
 locus=u['locus_id'];refs=[]
 for di,x in enumerate(dec['decisions']):
  if locus in x.get('locus_decisions',{}):
   refs.append({'source_document':'root_decisions','json_pointer':f'/decisions/{di}/locus_decisions/{locus}','root_section':x['section'],'exact_value':x['locus_decisions'][locus]})
 if locus=='L051':refs.append({'source_document':'root_locus_supplement','json_pointer':'/agreed_locus','root_section':None,'exact_value':supp['agreed_locus']})
 assert refs,locus
 loci.append({'locus_id':locus,'original_union_index':i,'union_pointer':f'/{i}','location_exact':u['location'],'root_authorities':refs,'selected_state_binding_status':'awaiting source026 exact final selected-state pointer contract; no inferred array'})
new=supp['new_locus'];assert new['locus_id']=='L052'
l052refs=[]
for di,x in enumerate(dec['decisions']):
 if 'L052' in x.get('locus_decisions',{}):l052refs.append({'source_document':'root_decisions','json_pointer':f'/decisions/{di}/locus_decisions/L052','root_section':x['section'],'exact_value':x['locus_decisions']['L052']})
 if x['section']=='15':l052refs.append({'source_document':'root_decisions','json_pointer':f'/decisions/{di}/assembly/main_composite','root_section':'15','exact_value':x['assembly']['main_composite']})
l052refs.append({'source_document':'root_locus_supplement','json_pointer':'/new_locus','root_section':'14','exact_value':new})
loci.append({'locus_id':'L052','original_union_index':None,'union_pointer':None,'location_exact':new['reading'],'root_authorities':l052refs,'selected_state_binding_status':'awaiting source026 exact final selected-state pointer contract; no inferred array'})
assert len(loci)==91 and len({x['locus_id'] for x in loci})==91
assert {x['locus_id'] for x in loci}=={f'S{i:02d}' for i in range(1,40)}|{f'L{i:03d}' for i in range(1,53)}
nrev=json.loads(raw['NREV_proposal']);page_invariants=[]
for invariant in nrev['page_invariants']:
 p=ROOT/invariant['path'];actual=sha(p.read_bytes())
 page_invariants.append({'exact_proposal_invariant':invariant,'actual_sha256_utf8':actual,'matches':actual==invariant['sha256_utf8']})
assert all(x['matches'] for x in page_invariants)
root_index={'schema':'notation026-root-authorities-v1','source_only':True,'audit_complete':False,'main_approved':False,'source_documents':docs,'section_count':27,'sigma_locus_count':39,'other_locus_count':52,'physical_locus_count':91,'presentation_order':'The90 exact union locus positions, followed by new root L052. Every original union position is retained.','root_sections':root_sections,'loci':loci,'NREV_page_invariants_checked_only':page_invariants,'NREV_operations_applied':[],'global_notation_substitutions':[],'ink_decisions_added':0,'images_accessed':0,'rendering_or_compilation':False}
for key,b in raw.items():assert (ROOT/FILES[key]).read_bytes()==b
artifacts=[write('notation026_baseline_cells_v01.json',baseline),write('notation026_root_authority_index_v01.json',root_index)]
proof={'utc':datetime.now(timezone.utc).isoformat(),'source_only':True,'sources':docs,'historical_rows_checked':180,'historical_families_checked':14,'all180_literal_cells_rejoin_exact_original_strings':True,'all180_literal_hashes_match_frozen_source_records':True,'all27_root_body_strings_equal_exact_journal_substrings':True,'all91_root_loci_have_exact_authority_pointers':True,'39_sigma_loci_and52_other_loci_exact':True,'root_crop_audit_records27_once_only_successful_views':True,'source_files_modified':False,'all_inputs_byte_identical_after_preparation':True,'NREV_pages_match_recorded_invariants':True,'NREV_applied':False,'final_selected_state_contract_bound':False,'outputs':artifacts,'read_scope_note':'This source index preserves the complete180-row original objects by frozen JSON pointer/hash and the14 exact family objects. Exact cells are a reversible positional extraction; no candidate normalization or ink selection is performed.'}
write('notation026_preparation_replay_v01.json',proof)
print(json.dumps({'outputs':artifacts,'rows':180,'families':14,'root_sections':27,'physical_loci':91,'sigma_loci':39,'all_checks_passed':True,'waiting_for':'source026 final91-locus selected-state contract'},indent=2))
