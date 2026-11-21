"""Stage root-journal source references without assigning ink or counts."""
from datetime import datetime, timezone
import copy
import json
import re
from scan022_source_support_prepare import BASE, OUT, file_ref, json_ref, read, span, write

JOURNAL='out/checks/scan022_main_decisions.md'
UNION='out/checks/scan022_source_support_union.json'
STATE='out/checks/scan022_source_support_journal_state.json'
AUTH='out/checks/scan022_source_support_root_authorizations.json'

def stage():
    union=json.loads(read(UNION))
    journal=read(JOURNAL)
    journal_ref=file_ref(JOURNAL)
    old=json.loads((BASE/STATE).read_text()) if (BASE/STATE).exists() else {'history':[]}
    history=old['history']
    if not history or history[-1]['original_journal_sha256']!=journal_ref['sha256']:
        phase=len(history)+1
        name=f'scan022_source_support_journal_phase_{phase:03d}.md'
        snapshot_path=OUT/name
        if snapshot_path.exists():
            assert snapshot_path.read_bytes()==(BASE/JOURNAL).read_bytes(),snapshot_path
        else:
            snapshot_path.write_bytes((BASE/JOURNAL).read_bytes())
        history.append({'phase':phase,'recorded_utc':datetime.now(timezone.utc).isoformat(),
                        'original_journal_sha256':journal_ref['sha256'],
                        'snapshot':file_ref(str(snapshot_path.relative_to(BASE))),
                        'scope':'Exact source journal snapshot. Later journal text supplies later root authorizations; snapshots are not additional readings.'})
    snapshot=history[-1]['snapshot']['path']
    headings=list(re.finditer(r'^##+\s+(.+)$',journal,re.M))
    sections=[]
    for i,m in enumerate(headings):
        end=headings[i+1].start() if i+1<len(headings) else len(journal)
        sections.append({'heading':m.group(1),
                         'root_journal_source':span(JOURNAL,m.start(),end),
                         'frozen_snapshot_source':span(snapshot,m.start(),end),
                         'authorization_mapping_status':'Pending source-clerk reading of this exact new root entry.'})
    rows=[]
    authorization_data=json.loads((BASE/AUTH).read_text()) if (BASE/AUTH).exists() else {'entries':[]}
    applied_scopes=set()
    for i,row in enumerate(union['textual_locus_crosswalk']):
        rows.append({'scope_id':row['id'],'location':row['location'],
                     'complete_union_scope':json_ref(UNION,f'/textual_locus_crosswalk/{i}'),
                     'readers':row['readers'],
                     'witness_blocks':row['witness_blocks'],
                     'H_local_marker_source_fact':row['H_local_marker_source_fact'],
                     'canonical_C_doubt_source_id':row['canonical_C_doubt_source_id'],
                     'canonical_C_doubt_part_id':row['canonical_C_doubt_part_id'],
                     'root_journal_authorizations':[],
                     'root_selected_reading':None,'root_selected_confidence':None,
                     'root_selected_source_group_ids':None,
                     'root_selected_count_parent_C':None,'root_selected_count_parent_H':None,
                     'root_selected_diff_C':None,'root_selected_diff_H':None,
                     'root_selected_C_doubt_outcome':None,
                     'root_component_confidences':{},
                     'root_ink_choice_applied':False,
                     'root_source_audit_choice_applied':False,
                     'main_approved':False,
                     'selection_status':'Pending explicit root journal authorization.'})
    by_scope={row['scope_id']:row for row in rows}
    for entry in authorization_data['entries']:
        for addition in entry.get('additional_scope_seeds',[]):
            assert addition['scope_id'] not in by_scope,addition['scope_id']
            seed=copy.deepcopy(by_scope[addition['base_union_scope_id']])
            seed['parent_union_context']=seed.pop('complete_union_scope')
            seed.update({k:v for k,v in addition.items() if k!='base_union_scope_id'})
            seed['root_added_scope']=True
            seed['canonical_C_doubt_source_id']=None
            seed['canonical_C_doubt_part_id']=None
            rows.append(seed)
            by_scope[seed['scope_id']]=seed
    for index,entry in enumerate(authorization_data['entries']):
        for update in entry['scope_updates']:
            target=by_scope[update['scope_id']]
            target['root_journal_authorizations'].append({
                'source_authorization_ref':json_ref(AUTH,f'/entries/{index}'),
                'root_journal_snapshot_source':entry['root_journal_snapshot_source']})
            target.update({k:v for k,v in update.items() if k!='scope_id'})
            target['selection_status']='Explicit root source/ink choices recorded; unprovided fields remain pending.'
            applied_scopes.add(update['scope_id'])
    applied_sections={x['journal_section_id'] for x in authorization_data['entries']}
    for section in sections:
        number=section['heading'].split(' ',1)[0]
        if number in applied_sections:
            section['authorization_mapping_status']='Read and applied only to explicitly named source/ink fields; remaining fields pending.'
    state={'scan':22,'current_journal':journal_ref,'latest_snapshot':history[-1]['snapshot'],
           'history':history,'sections':sections,
           'root_return_read_gate_source':file_ref('out/checks/scan022_root_return_read_progress.json'),
           'scope':'Source-only journal ingestion. No image or image-hash access. No root choices or counts inferred.',
           'main_adjudicated':False,'main_approved':False}
    original_C_rows=union['original_C_source_rows']
    for original in original_C_rows:
        applied=[r for r in rows if r['canonical_C_doubt_source_id']==original['source_id']
                 and r['root_selected_C_doubt_outcome'] is not None]
        if applied:
            assert len(applied)==1,original['source_id']
            original['root_outcome']={**applied[0]['root_selected_C_doubt_outcome'],
                                      'root_journal_authorizations':applied[0]['root_journal_authorizations'],
                                      'main_approved':False,
                                      'status_scope':'Root ink outcome recorded; original source-part pending status retained separately.'}
    ledger={'scan':22,'artifact_role':'Source-support candidate ledger; incomplete and unselected.',
            'main_adjudicated':False,'main_approved':False,
            'frozen_union':file_ref(UNION),'journal_state':{'path':STATE,'status':'Bound after current state write.'},
            'scope_candidates':rows,
            'preserved_original_union_scope_count':len(union['textual_locus_crosswalk']),
            'original_C_source_rows':original_C_rows,
            'immutable_reader_fingerprints':union['immutable_reader_fingerprints'],
            'all_graphical_and_inventory_source_associations':json_ref(UNION,'/graphical_source_associations'),
            'raw_physical_count_proposals':{r:union['reader_source_scopes'][r]['all_raw_counts_and_physical_count_proposals'] for r in 'ABC'},
            'root_authorizations_source':file_ref(AUTH) if (BASE/AUTH).exists() else None,
            'root_process_instructions':authorization_data.get('root_process_instructions',[]),
            'root_page_level_source_choices':[
                {'root_journal_snapshot_source':entry['root_journal_snapshot_source'],
                 'source_authorization_ref':json_ref(AUTH,f'/entries/{index}'),
                 'choices':entry['page_level_source_choices']}
                for index,entry in enumerate(authorization_data['entries'])
                if entry.get('page_level_source_choices')],
            'pending_root_authorization_summary':{
                'scopes_without_explicit_recorded_ink_or_source_choice':[x['scope_id'] for x in rows if not x['root_journal_authorizations']],
                'scopes_with_count_flags_pending':[x['scope_id'] for x in rows if x['root_selected_diff_C'] is None or x['root_selected_diff_H'] is None],
                'remaining_requirements':['Selected graphical/text source blocks and literal replacements where not yet named.',
                    'Final C/H physical count parents and Boolean flags, including compound scopes.',
                    'Final outcomes for the seven actual C source rows/parts.',
                    'S confirmations and administrative source choices, with exact journal entries.'],
            },
            'assembly_status':'Awaiting final root journal before a complete record draft.'}
    state_ref=write('scan022_source_support_journal_state.json',state)
    # Bind the ledger only after the current state file has been written.
    ledger['journal_state']=json_ref(STATE)
    ledger_ref=write('scan022_source_support_record_candidates.json',ledger)
    return {'state':state_ref,'candidate_ledger':ledger_ref,
            'journal_phase':len(history),'journal_sections':len(sections),
            'source_scopes_with_explicit_root_authorization':len(applied_scopes),'scope_candidates':len(rows)}

if __name__=='__main__':
    print(json.dumps(stage(),ensure_ascii=False))
