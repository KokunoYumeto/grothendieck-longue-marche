"""Isolated WF026 evidence extension; no global files or builders are changed/run."""
from pathlib import Path
from collections import Counter
import copy,difflib,hashlib,json,re
B=Path('/workspace/scratch/94548b74fbe0');O=B/'out/checks'
sha=lambda x:hashlib.sha256(x.encode() if isinstance(x,str) else x).hexdigest()
dump=lambda x:(json.dumps(x,ensure_ascii=False,indent=2)+'\n').encode()
pack=lambda x:json.dumps(x,ensure_ascii=False,separators=(',',':'))
def meta(path):
 raw=(B/path).read_bytes();return {'path':path,'sha256':sha(raw),'bytes':len(raw)}
def save(name,value,raw=False):
 body=value if raw else dump(value);p=O/name
 if p.exists():assert p.read_bytes()==body
 else:p.write_bytes(body)
 return {'path':str(p.relative_to(B)),'sha256':sha(body),'bytes':len(body)}
prior_path='out/checks/wf_root_crop_counts_through025_proposal/evidence.json';prior_raw=(B/prior_path).read_bytes();prior=json.loads(prior_raw)
selector_path='out/checks/final_readiness026_workflow_selector_proposal.json';selector=json.loads((B/selector_path).read_text())
assert sha(prior_raw)==selector['expected_before_sha256']=='1a1bdd82104ce0981bc6efbc3ec372ef417f676d9081245922f9f7fbc2315dab'
assert dump(prior)==prior_raw
corrected=copy.deepcopy(prior)
assert corrected['earlier_pages'][2]['scan']==4
assert corrected['earlier_pages'][2]['enumeration_selector']==selector['exact_before']
corrected['earlier_pages'][2]['enumeration_selector']=selector['exact_after']
assert sha(dump(corrected))==selector['proposed_after_sha256']=='9babfd57508488eb20a45aa50b6d55590628429c8b87faa6dea23fa7319db78c'
audit_path='out/checks/scan026_root_crop_audit.json';audit_raw=(B/audit_path).read_bytes();audit=json.loads(audit_raw)
assert audit['scan']==26 and audit['planned_crops_completed'] is True and audit['pending_root_crops']==[] and audit['closed_utc']
assert audit['whole_or_half_views']==0 and audit['whole_or_halves_seen_by_root'] is False
assert len(audit['viewed_once'])==audit['total_distinct']==27
seen={};owners=Counter();eligible=[]
for i,row in enumerate(audit['viewed_once']):
 assert type(row['successful_display_count']) is int and row['successful_display_count']==1
 path=row['path'];assert path not in seen
 if path.startswith('crops/scan026_'):owner='root'
 else:
  assert path.startswith('readers/026/');owner=path.split('/')[2];assert owner in 'ABC'
 assert type(row['created_by_root']) is bool and row['created_by_root']==(owner=='root')
 seen[path]=i;owners[owner]+=1
 eligible.append({'json_pointer':f'/viewed_once/{i}','path':path,'recorded_sha256':row['sha256'],
  'successful_display_count':row['successful_display_count'],'owner_from_exact_path':owner,
  'created_by_root':row['created_by_root'],'decision_sections':copy.deepcopy(row['decision_sections'])})
assert owners==Counter({'root':4,'A':10,'B':9,'C':4})
assert audit['created_by_root_count']==4 and audit['reused_reader_crop_count']==23
failures=copy.deepcopy(audit['failed_unseen_deliveries']);assert len(failures)==2
recoveries=[]
for i,failure in enumerate(failures):
 assert failure['path'] in seen;success_index=seen[failure['path']];success=audit['viewed_once'][success_index]
 assert failure['section'] in success['decision_sections']
 recoveries.append({'failure_json_pointer':f'/failed_unseen_deliveries/{i}','exact_path':failure['path'],
  'successful_row_json_pointer':f'/viewed_once/{success_index}','recorded_successful_displays':success['successful_display_count'],
  'recorded_failure_time':failure['recorded_utc'],'recorded_success_time':success['recorded_utc'],
  'failure_record_copied_unchanged':True,'successful_path_count_contribution':1})
journal_path='out/checks/scan026_root_journal.md';journal=(B/journal_path).read_text();crop_lines=[]
for n,line in enumerate(journal.splitlines(),1):
 if line.startswith('Crop `'):
  m=re.match(r'Crop `([^`]+)`; SHA-256 `([^`]+)`\.',line);assert m
  path,digest=m.groups();assert path in seen and audit['viewed_once'][seen[path]]['sha256']==digest
  crop_lines.append({'line':n,'text':line})
assert len(crop_lines)==27
entry={'scan':26,'evidence_kind':'existing_formal_root_crop_audit','audit_source':meta(audit_path),
 'success_array':'viewed_once','selection':'successful_display_count > 0; count each exact path once',
 'counts':{'total':27,'root_created':4,'reused':23,'reused_by_role':{'A':10,'B':9,'C':4}},
 'declared_total':27,'eligible_rows':eligible,'duplicate_successful_path_count':0,
 'excluded_failure_records':{'failed_unseen_deliveries':failures},
 'journal_source':meta(journal_path),'journal_exact_crop_lines':crop_lines,'formal_audit_created_by_this_proposal':False,
 'closed_audit_fields':{k:copy.deepcopy(audit[k]) for k in ['whole_or_half_views','whole_or_halves_seen_by_root','planned_crops_completed','last_decision_recorded_utc','pending_root_crops','created_by_root_count','reused_reader_crop_count','closed_utc','locus_supplement','physical_loci_total']},
 'failed_unseen_recovery_bindings':recoveries,
 'evidence_scope':'The existing closed root audit supplies all image-use facts. This source-only proposal reads no image bytes.'}
entry_file=save('scan026_source_wf_extension_entry_v01.json',entry)
assert [x['scan'] for x in corrected['formal_pages']]==list(range(13,26))
after=copy.deepcopy(corrected)
old_scope=after['scope'];new_scope='Source reporting through scan026; prior through025 evidence and the exact scan004 selector correction are preserved.'
old026=after['scan026']
after['scope']=new_scope;after['formal_pages'].append(copy.deepcopy(entry))
after['scan026']={'status':'closed root audit reviewed in this source-only extension','formal_pages_index':13,
 'audit_path':audit_path,'total_distinct_successful_paths':27,'root_created_shown':4,'reader_crops_reused':23,
 'failed_unseen_delivery_records_preserved':2,'whole_or_half_views':0}
after['extension_026_provenance']={'prior_evidence':meta(prior_path),'preserved_selector_correction':meta(selector_path),
 'selector_corrected_base_sha256':sha(dump(corrected)),'closed_root_audit':meta(audit_path),
 'prior_prepared_utc_retained':prior['prepared_utc'],'global_builder_or_workflow_changes_applied':False}
after_raw=dump(after);after_file=save('scan026_source_wf_through026_evidence_proposal_v01.json',after)
base_file=save('scan026_source_wf_through025_selector_corrected_base_v01.json',dump(corrected),True)
# Exact inverse to selector-corrected base, then exact inverse of prior selector correction.
back=copy.deepcopy(after);assert pack(back['formal_pages'].pop())==pack(entry)
back['scope']=old_scope;back['scan026']=old026;del back['extension_026_provenance']
assert dump(back)==dump(corrected)
back['earlier_pages'][2]['enumeration_selector']=selector['exact_before'];assert dump(back)==prior_raw
assert pack(after['formal_pages'][:13])==pack(prior['formal_pages'])
old_earlier=copy.deepcopy(after['earlier_pages']);old_earlier[2]['enumeration_selector']=selector['exact_before']
assert pack(old_earlier)==pack(prior['earlier_pages'])
changed_top=['scope','formal_pages','earlier_pages','scan026','extension_026_provenance']
for key in prior:
 if key not in changed_top:assert pack(after[key])==pack(prior[key])

# The earlier proposed builder already selects a per-scan audit with no upper scan bound.
builder_proposal='out/checks/wf_root_crop_counts_through025_proposal/build_records.proposed.py'
builder=(B/builder_proposal).read_text();a=builder.index('def root_crop_counts(scan):');b=builder.index('\nworkflow=',a)
function=builder[a:b]
assert "f'scan{scan:03d}_root_crop_audit.json'" in function
assert "('images', 'viewed_once')" in function and "row.get('successful_display_count')" in function
assert "f'crops/scan{scan:03d}_'" in function and "f'readers/{scan:03d}/'" in function
builder_binding={'proposal':meta(builder_proposal),'exact_helper_char_start':a,'exact_helper_char_end':b,
 'exact_helper_sha256':sha(function),'scan026_filename_substitution':'scan026_root_crop_audit.json',
 'recognized_positive_array':'viewed_once','eligible_path_owner_totals':dict(owners),
 'builder_source_modified':False,'builder_executed_or_imported':False}
original_global={p:meta(p) for p in [prior_path,selector_path,'out/scripts/build_records.py',builder_proposal]}
diff=''.join(difflib.unified_diff(prior_raw.decode().splitlines(keepends=True),after_raw.decode().splitlines(keepends=True),fromfile=prior_path,tofile=after_file['path'],n=3))
diff_file=save('scan026_source_wf_extension_delta_v01.diff',diff.encode(),True)
totals={k:sum(x['counts'][k] for x in after['formal_pages']) for k in ['total','root_created','reused']}
assert totals=={'total':320,'root_created':56,'reused':264}
preview=('# Source-only WF026 evidence extension\n\n'
 'The existing closed audit records 27 distinct successful root crop paths: 4 root-created and 23 reused (A 10, B 9, C 4). Each has one successful display. The two failed-unseen records are copied unchanged and linked to their later same-path successes. Root whole/half views remain 0.\n\n'
 '| Scan | Root shown, distinct | Root-created shown | Reused A | Reused B | Reused C | Reused total | Failed-unseen records retained |\n'
 '| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |\n'
 '| 026 | 27 | 4 | 10 | 9 | 4 | 23 | 2 |\n\n'
 'The proposed evidence copy preserves every formal-page object through scan025. The earlier-page objects retain only the separately proposed exact scan004 selector correction. The original prepared timestamp and historical workflow snapshot fields remain unchanged. Formal scans013–026 total 320 successful distinct paths, 56 root-created and 264 reused. These totals retain each earlier stored count.\n\n'
 'The existing proposed build_records helper already selects scan026 through the per-scan audit filename and positive-success array. Its source is unchanged and has not been run. The existing global evidence, selector proposal, builder and workflow remain untouched by this extension.\n')
preview_file=save('scan026_source_wf_extension_preview_v01.md',preview.encode(),True)
proposal={'status':'source-only proposal; no global application','entry':entry_file,'selector_corrected_base':base_file,
 'complete_proposed_evidence':after_file,'delta':diff_file,'preview':preview_file,
 'exact_field_operations':[{'path':'/earlier_pages/2/enumeration_selector','before':selector['exact_before'],'after':selector['exact_after']},
  {'path':'/scope','before':old_scope,'after':new_scope},
  {'path':'/formal_pages/13','operation':'append exact standalone entry','value_file':entry_file},
  {'path':'/scan026','before':old026,'after':after['scan026']},
  {'path':'/extension_026_provenance','operation':'append exact provenance object','after':after['extension_026_provenance']}],
 'builder_binding':builder_binding,'formal_totals_through026':totals,
 'proof':{'prior13_formal_page_objects_unchanged':True,'all_earlier_pages_unchanged_except_exact_preserved_selector_correction':True,
  'all_other_prior_top_level_values_and_key_order_unchanged':True,'inverse_restores_selector_corrected_base_bytes':True,
  'second_inverse_restores_original_through025_bytes':True,'all27_success_paths_unique_and_once':True,
  'all2_failed_unseen_records_unchanged':True,'same_path_success_recoveries_bound':True,
  'global_inputs_unchanged':True,'image_bytes_read':0,'builder_executed':False},
 'preserved_global_inputs':original_global}
for path,before in original_global.items():assert meta(path)==before
proposal_file=save('scan026_source_wf_extension_proposal_v01.json',proposal)
print(json.dumps({'proposal':proposal_file,'entry':entry_file,'evidence':after_file,'delta_bytes':diff_file['bytes'],
 'root026_counts':entry['counts'],'formal013_026_totals':totals,'all_inverse_checks_passed':True},ensure_ascii=False,indent=2))
