#!/usr/bin/env python3
"""One bounded post-assembly source replay. Run only after final frozen handoff."""
from pathlib import Path
from collections import Counter
from copy import deepcopy
import hashlib
import importlib.util
import json
import re

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'out/checks'


def sha(value):
    return hashlib.sha256(value if isinstance(value,bytes) else value.encode('utf-8')).hexdigest()


def walk(value,pointer=''):
    yield pointer,value
    if isinstance(value,dict):
        for key,child in value.items():
            yield from walk(child,pointer+'/'+str(key).replace('~','~0').replace('/','~1'))
    elif isinstance(value,list):
        for i,child in enumerate(value):yield from walk(child,pointer+'/'+str(i))


def main():
    handoff_path=OUT/'scan025_qa_postassembly_handoff.json'
    handoff=json.loads(handoff_path.read_text())
    authority_path=OUT/'scan025_qa_assembly_authority_map.json'
    authority=json.loads(authority_path.read_text())
    failures=[]
    counts=Counter()
    cache={}
    def check(kind,ok,**where):
        counts[kind]+=1
        if not ok:failures.append({'check':kind,**where})
        return ok
    def source(path):
        if path not in cache:
            if Path(path).suffix.lower() in ['.png','.jpg','.jpeg','.gif','.webp','.pdf']:
                raise ValueError('No image/document binary read authorized: '+path)
            if path=='source/SP40_CW_81_sweep3/readings/cote81_CORRECTIONS.tsv':
                # Only the already verified stage1 payload is in this agent's
                # read scope. Do not open the external original S file.
                pooled=json.loads(source('out/checks/scan025_source_pool_v01.json'))
                file=next(x for x in pooled['files'] if x['path']==path)
                strings={x['id']:x['literal'] for x in pooled['strings']}
                cache[path]=''.join(strings[x['string_ref']] for x in file['payload']['text_chunks'])
                check('new-record-S-ref-frozen-payload-binding',sha(cache[path])==file['sha256_utf8']==json.loads(source('out/checks/scan025_S_scope.json'))['source_sha256'])
            else:
                cache[path]=(BASE/path).read_text()
        return cache[path]
    def validate_span(ref,pointer):
        path=ref.get('workspace_path',ref['path'])
        text=source(path)
        a,b=ref['char_start'],ref['char_end']
        literal=ref['literal']
        check('exact-source-span',0<=a<=b<=len(text) and text[a:b]==literal,pointer=pointer,path=path)
        check('source-span-file-hash',all(ref[k]==sha(text) for k in ['sha256','sha256_utf8'] if k in ref),pointer=pointer,path=path)
        check('source-span-literal-hash',ref['body_sha256']==sha(literal),pointer=pointer,path=path)
        check('source-span-byte-boundaries',ref['utf8_byte_start']==len(text[:a].encode('utf-8')) and ref['utf8_byte_end']==len(text[:b].encode('utf-8')),pointer=pointer,path=path)
        check('source-span-line-boundaries',ref['line_start']==text.count('\n',0,a)+1 and ref['line_end']==text.count('\n',0,max(a,b-1))+1,pointer=pointer,path=path)
    inputs={}
    for role,entry in handoff['frozen_artifacts'].items():
        raw=(BASE/entry['path']).read_bytes()
        inputs[role]={'path':entry['path'],'sha256_utf8':sha(raw)}
        check('frozen-handoff-hash',sha(raw)==entry['sha256_utf8'],role=role,path=entry['path'])
    draft=source(handoff['frozen_artifacts']['draft']['path'])
    map_path=handoff['frozen_artifacts']['map']['path']
    mapping=json.loads(source(map_path))
    assembly=json.loads(source('out/checks/scan025_source_assembly_map_v02.json'))
    check('frozen-v02-assembly-hash',sha(source('out/checks/scan025_source_assembly_map_v02.json'))=='7edf4da01314025441637026c22e8f6b3b7c585f79332e2f7238816572e8fc38')
    check('selected-draft-frozen-v02-hash',sha(draft)=='e5098e342952e5103022ef30641cdda851e5d74203913db9f2060661e50297ad')
    check('selected-map-draft-binding',mapping['draft_sha256_utf8']==sha(draft) and mapping['final_draft_sha256']==sha(draft))
    check('current-root-journal-binding',sha(source(authority['authority']['journal_path']))==authority['authority']['journal_sha256_utf8']==mapping['authority']['root_journal_sha256'])
    check('current-root-crop-audit-binding',sha(source(authority['authority']['crop_audit_path']))==authority['authority']['crop_audit_sha256_utf8']==mapping['authority']['root_crop_audit_sha256'])
    for pointer,value in walk(mapping):
        if isinstance(value,dict) and {'path','char_start','char_end','literal','body_sha256'}<=set(value):
            validate_span(value,'map'+pointer)

    selected={entry['id']:entry for entry in mapping['selected_groups']}
    check('selected-group-identities',len(selected)==len(mapping['selected_groups'])==25 and set(selected)==set(authority['expected_selected_group_ids']))
    donor_maps={r:json.loads(source(f'out/readers/025/{r}/source_map.json')) for r in 'ABC'}
    donors={g['id']:g for m in donor_maps.values() for g in m['groups']}
    for gid,entry in selected.items():
        check('exact-selected-donor-group',entry['source']['literal']==entry['donor_source']['literal']==donors[gid]['literal_source'] and entry['exact_donor_group'] is True and entry['local_outer_unsure_added'] is False,group=gid)
        check('complete-original-donor-metadata',entry['donor_map']==donors[gid],group=gid)
        check('selected-group-occurs-once',draft.count(entry['source']['literal'])==1,group=gid)
        check('selected-group-unapproved',entry['main_approved'] is False,group=gid)
    for gid in authority['exact_source_recurring_groups']:
        check('later-recurring-group-source-convention',selected[gid]['donor_map']['printed_qualifier'] is False and selected[gid]['source']['literal']==donors[gid]['literal_source'],group=gid)
    check('no-current-added-wrapper-list',authority['wrapper_only_groups']==[])

    original_c=source('out/readers/025/C/reading.tex')
    changes=mapping['literal_replacements']
    check('seven-authorized-source-replacements',len(changes)==7)
    replay=original_c
    for edit in reversed(changes):
        a,b=edit['original_start'],edit['original_end']
        check('literal-replacement-old-source',original_c[a:b]==edit['original_source']['literal'],edit=edit['edit_id'])
        replay=replay[:a]+edit['replacement']+replay[b:]
    check('forward-complete-draft-replay',replay==draft)
    reverse=draft
    for edit in reversed(changes):
        a,b=edit['selected_start'],edit['selected_end']
        check('literal-replacement-selected-source',draft[a:b]==edit['replacement']==edit['selected_source']['literal'],edit=edit['edit_id'])
        reverse=reverse[:a]+edit['original_source']['literal']+reverse[b:]
        for side in ['start','end']:
            recorded=edit['splice_boundaries'][side]
            i=recorded['char_offset']
            check('literal-splice-character-boundary',recorded['preceding_character']==draft[i-1:i] and recorded['following_character']==draft[i:i+1],edit=edit['edit_id'],side=side)
            check('literal-splice-byte-boundary',recorded['preceding_last_byte_hex']==draft[:i].encode('utf-8')[-1:].hex() and recorded['following_first_byte_hex']==draft[i:].encode('utf-8')[:1].hex(),edit=edit['edit_id'],side=side)
    check('inverse-complete-original-C-replay',reverse==original_c)
    word=authority['participle_exact_change']
    word_edit=[x for x in changes if x['original_source']['literal']==word['old']]
    check('exact-two-candidate-word-change',len(word_edit)==1 and word_edit[0]['replacement']==word['new'])
    partition=mapping['complete_selected_source_partition']
    cursor=0
    literals=[]
    for i,part in enumerate(partition):
        check('selected-source-partition-contiguous',part['selected_start']==cursor and part['selected_end']-part['selected_start']==len(part['selected_source']['literal']),part=i)
        cursor=part['selected_end'];literals.append(part['selected_source']['literal'])
        if part['kind']=='unchanged_C':check('unchanged-C-partition-literal',part['source']['literal']==part['selected_source']['literal'],part=i)
    check('selected-source-partition-complete',cursor==len(draft) and ''.join(literals)==draft)

    spec=importlib.util.spec_from_file_location('scan025_qa_source_inventory',OUT/'scan025_qa_source_inventory.py')
    helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
    lexical=helper.drawing_commands(draft)
    command_rows=mapping['exact_command_ownership']
    check('complete-selected-command-inventory',[(c,a,b) for c,a,b in lexical]==[(x['command'],x['selected_source']['char_start'],x['selected_source']['char_end']) for x in command_rows])
    exact=0;newline=0
    for row in command_rows:
        literal=row['selected_source']['literal']
        if row['exact_donor_matches']:
            check('selected-command-exact-donor',all(x['literal']==literal for x in row['exact_donor_matches']),command=row['id']);exact+=1
        else:
            old=row['donor_with_only_authorized_marker_newline']
            check('selected-outer-node-marker-newline-only',old is not None and old['path']=='out/readers/025/B/reading.tex' and old['literal'].replace('$% BEGIN','$\n% BEGIN')==literal,command=row['id']);newline+=1
    check('selected-command-donor-totals',len(command_rows)==172 and exact==170 and newline==2)

    try:
        record_result=check_record(handoff,mapping,authority,check,source,validate_span)
    except Exception as error:
        failures.append({'check':'qa-checker-schema-exception','exception_type':type(error).__name__,'message':str(error)})
        record_result={'status':'checker exception; no source defect inferred from exception'}
    result={'scan':25,'source_only':True,'status':'passed' if not failures else 'concrete defects recorded','scope':'One bounded post-assembly source/map/record replay; stage1 replay is not repeated. No images, source mutation, ink/count choice, rendering, compilation, mathematical inference, approval or commit.','frozen_inputs':inputs,'qa_authority_map_sha256_utf8':sha(authority_path.read_bytes()),'qa_script_sha256_utf8':sha(Path(__file__).read_bytes()),'check_counts':dict(counts),'selected_groups':len(selected),'literal_replacements':len(changes),'selected_command_rows':len(command_rows),'record_replay':record_result,'concrete_defects':failures,'root_approval_status':'Root review and approval remain pending.'}
    output=OUT/'scan025_qa_postassembly_replay.json'
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'path':str(output.relative_to(BASE)),'sha256_utf8':sha(output.read_bytes()),'status':result['status'],'counts':dict(counts),'record_replay':record_result,'concrete_defects':failures},ensure_ascii=False,indent=2))


def at(value,pointer):
    for token in pointer.split('/')[1:]:
        token=token.replace('~1','/').replace('~0','~')
        value=value[int(token)] if isinstance(value,list) else value[token]
    return value


def replace_at(value,pointer,replacement):
    parent=at(value,pointer.rsplit('/',1)[0])
    key=pointer.rsplit('/',1)[1].replace('~1','/').replace('~0','~')
    if isinstance(parent,list):parent[int(key)]=replacement
    else:parent[key]=replacement


def check_record(handoff,mapping,authority,check,source,validate_span):
    record_path=handoff['frozen_artifacts']['record']['path']
    record=json.loads(source(record_path))
    map_path=handoff['frozen_artifacts']['map']['path']
    draft_path=handoff['frozen_artifacts']['draft']['path']
    draft=source(draft_path)
    map_hash=sha(source(map_path)); draft_hash=sha(draft)
    provenance=record['provenance']; refs=provenance['source_reference_pool']
    union=json.loads(source('out/checks/scan025_source_union_v01.json'))
    union_loci={x['id']:x for x in union['source_locus_union']}
    union_rows={x['id']:x for x in union['raw_row_correspondence']}
    union_groups=union['complete_own_groups']
    donors={g['id']:g for r in 'ABC' for g in json.loads(source(f'out/readers/025/{r}/source_map.json'))['groups']}
    frames=provenance['complete_own_source_frames']
    decisions={x['id']:x for x in record['decisions']}
    physical=[x for x in record['decisions'] if x['physical_count_parent'] is not None]
    source_only=[x for x in record['decisions'] if x['physical_count_parent'] is None]
    inventory={x['element']:x for x in record['inventory']}
    selected={x['id']:x for x in record['selected_graphical_groups']}
    map_selected={x['id']:x for x in mapping['selected_groups']}
    loci={x['source_locus_id']:x for x in record['source_locus_coverage']}
    raw_rows={x['id']:x for x in provenance['raw_main_row_correspondence']}
    audit=json.loads(source(authority['authority']['crop_audit_path']))
    spec=importlib.util.spec_from_file_location('scan025_qa_source_inventory_record',OUT/'scan025_qa_source_inventory.py')
    helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
    json_positions={}

    def ref_value(key):
        return json.loads(refs[key]['literal'])

    def same_span(left,right):
        return (left['path'],left['char_start'],left['char_end'],left['body_sha256'])==(right['path'],right['char_start'],right['char_end_exclusive'],right['literal_sha256_utf8'])

    def original_value(ref):
        return at(json.loads(source(ref['source_path'])),ref['json_pointer'])

    def attachment_view(attachment):
        # The final map avoids a self-hash; the record adds the exact map hash.
        return {k:v for k,v in attachment.items() if k!='source_map_reference'}

    def map_projection(value):
        # Exact declared projection: erase only current source-map hash
        # attachments. Every erased value is checked separately above.
        if isinstance(value,dict):return {k:map_projection(v) for k,v in value.items() if k!='source_map_reference'}
        if isinstance(value,list):return [map_projection(v) for v in value]
        return value

    for pointer,value in walk(record):
        if isinstance(value,dict) and {'path','char_start','char_end','literal','body_sha256'}<=set(value):
            validate_span(value,'record'+pointer)
            if 'workspace_path' in value:
                check('selected-attachment-path-morphism',value['path']=='checks/scan025_final_draft.tex' and value['workspace_path']==draft_path,pointer=pointer)
                check('selected-attachment-current-map-binding',value.get('manifest')==Path(map_path).name and value.get('source_map_reference')=={'path':map_path,'sha256':map_hash},pointer=pointer)
            if 'json_pointer' in value:
                path=value['path']
                if path not in json_positions:json_positions[path]=helper.json_spans(source(path))
                check('record-json-reference-exact-pointer-boundaries',json_positions[path].get(value['json_pointer'])==(value['char_start'],value['char_end']),pointer=pointer,source_path=path,json_pointer=value['json_pointer'])
                check('record-json-reference-complete-value',json.loads(value['literal'])==at(json.loads(source(path)),value['json_pointer']),pointer=pointer)
    check('record-draft-map-bindings',record['selected_draft']['path']==draft_path and record['selected_draft']['sha256']==draft_hash and record['selected_source_map']=={'path':map_path,'sha256':map_hash})
    check('pending-approval-preserved',record['main_adjudicated'] is False and record['main_approved'] is False and record['pending_root_decision_ids']==[] and record['root_actions_pending'])
    closure_path='out/checks/scan025_root_record_field_clarifications.json'
    closure=json.loads(source(closure_path))
    before_path='out/checks/scan025_source_record_pending_v02.json'
    before=json.loads(source(before_path))
    check('root-seven-leaf-closure-authority',sha(source(closure_path))=='d015ee50059678082d89d76c26c2e8c288152bb53fed82a3e86b53a1eebdcb76' and len(closure['changes'])==7 and sha(source(before_path))==closure['before_record_sha256'] and map_hash==closure['before_source_map_sha256'])
    replay=deepcopy(before)
    for operation in closure['changes']:
        check('root-record-correction-exact-old-new',at(before,operation['path'])==operation['old'] and at(record,operation['path'])==operation['new'],pointer=operation['path'])
        replace_at(replay,operation['path'],operation['new'])
    check('root-seven-leaf-forward-record-replay',replay==record)
    reverse=deepcopy(record)
    for operation in reversed(closure['changes']):replace_at(reverse,operation['path'],operation['old'])
    check('root-seven-leaf-inverse-record-replay',reverse==before)
    check('record-row-counts',len(decisions)==len(record['decisions'])==34 and len(physical)==27 and len(source_only)==7 and len(record['doubts'])==19 and len(inventory)==len(record['inventory'])==36)
    check('root-count-arithmetic-copy',sum(x['diff_C'] for x in physical)==25 and sum(x['diff_H'] for x in physical)==27 and record['counts']['C']==25 and record['counts']['H']==27 and len({x['physical_count_parent'] for x in physical})==27)
    check('record-count-metadata',record['counts']=={'C':25,'H':27,'decision_loci':34,'physical_decision_rows':27,'source_only_S_rows':7,'inventory_elements':36,'remaining_doubt_loci':19,'check_events':0})
    check('selected-group-map-record-equality',map_projection(record['selected_graphical_groups'])==mapping['selected_groups'] and set(selected)==set(authority['expected_selected_group_ids']))
    check('locus-map-record-equality',map_projection(record['source_locus_coverage'])==mapping['source_locus_coverage'] and len(loci)==28 and set(loci)==set(union_loci))
    check('record-no-check-events',record['check_events']==[])
    check('root-viewing-metadata-copy',record['root_viewing_scope']=={'whole_or_half_views':0,'total_distinct_crops':18,'each_successfully_viewed_once':True,'original_audit_sha256':authority['authority']['crop_audit_sha256_utf8']})

    selection_to_decision={g:d for d in physical for g in d['selected_group_ids']}
    selection_to_decision.update({'mut_raised_t_stop':decisions['SRC025-P15'],'participle':decisions['SRC025-P18'],'final_set_endpoint':decisions['SRC025-P26'],'disjoints_endpoint':decisions['SRC025-P27']})
    for expected in authority['expected_authorized_clusters']:
        key=expected['qa_selection_key']; d=selection_to_decision[key]
        check('physical-decision-root-scalar-binding',d['source_locus_id']==expected['source_locus'] and int(d['diff_C'])==expected['authorized_count_C'] and int(d['diff_H'])==expected['authorized_count_H'] and d['confidence']==expected['authorized_confidence'] and d['kind']==expected['authorized_kind'] and d['marked_in_H'] is expected['authorized_marked_in_H'],selection=key,decision=d['id'])
        check('physical-count-single-parent',d['physical_count_parent']==d['id'],decision=d['id'])
        check('physical-decision-authority-span',same_span(d['root_count_authorization'],expected['root_section_ref']),decision=d['id'])
        check('physical-decision-root-choice-status',d['root_ink_choice_applied'] is True and d['root_source_audit_choice_applied'] is True and d['main_approved'] is False,decision=d['id'])
        cref=expected['crop_audit_reference']; crop_entry=at(audit,cref['json_pointer'])
        check('physical-decision-exact-crop-reference',d['crop']==[cref['crop_path']] and len(d['root_crop_evidence'])==1,decision=d['id'])
        for evidence in d['root_crop_evidence']:
            check('physical-decision-crop-audit-metadata',evidence['crop']==cref['crop_path'] and evidence['crop_sha256']==cref['recorded_crop_sha256'] and evidence['successful_display_count']==1 and evidence['original_audit_entry']==crop_entry and evidence['additional_display'] in [None,False],decision=d['id'])
            check('physical-decision-evidence-root-literal',evidence['observation'] in evidence['journal']['literal'] and evidence['observation'] in d['evidence'],decision=d['id'])
        check('physical-local-H-flag',d['marked_in_H'] is False and d['H_marker_ids']==[],decision=d['id'])
        for witness in 'CH':
            check('witness-local-reference-present',bool(d['witness_source_references'][witness]),decision=d['id'],witness=witness)
            for wr in d['witness_source_references'][witness]:
                check('witness-role-path',wr['path']==f'packets/025/{witness}.tex',decision=d['id'],witness=witness)
    for d in source_only:
        check('S-source-only-status',d['diff_C'] is False and d['diff_H'] is False and d['root_ink_choice_applied'] is False and d['root_source_audit_choice_applied'] is True and d['crop']==[] and d['root_crop_evidence']==[] and d['source_attachments']==[] and d['selected_group_ids']==[] and d['proof_event'] is False and d['confidence']=='high' and d['main_approved'] is False,decision=d['id'])
        sref=refs[d['provenance']['original_S_row_ref']]
        check('S-seven-separate-source-identities',sref['literal'].split('\t',1)[0]==d['S_id'],decision=d['id'])
    check('S-source-row-identities',set(d['S_id'] for d in source_only)==set(x['id'] for x in json.loads(source('out/checks/scan025_S_scope.json'))['row_scopes']))

    check('all-own-frame-identities',set(frames)==set(union['reader_frames']) and len(frames)==21)
    frame_group_coverage=set()
    frame_inventory_coverage=set()
    own_scope_fields={'reading','proposal','alternatives','complete_alternatives','complete_candidates','complete_qualified_candidates','reader_complete_candidates','reader_complete_alternatives','reader_source_qualification','reader_semantic_annotation','reader_printed_qualifier','reader_ownership','reader_role_and_attachment','reader_hand','local_hand_scopes','scope','local_decisions','source_group','source_groups','group_id','printed_qualifier','qualified_here','reason','qualification','hand','role','role_and_attachment','ownership','owns','semantic_annotation'}
    for fid,frame in frames.items():
        old=union['reader_frames'][fid]; complete=refs[frame['complete_source_ref']]
        check('complete-own-frame-source-binding',complete['path']==old['complete_source']['source_path'] and complete['char_start']==old['complete_source']['char_start'] and complete['char_end']==old['complete_source']['char_end_exclusive'] and complete['body_sha256']==old['complete_source']['literal_sha256_utf8'],frame=fid)
        cursor=complete['char_start']; source_parts=[]
        for n,part in enumerate(frame['parts']):
            pr=refs[part['source_ref']]; source_parts.append(pr['literal'])
            check('own-frame-source-part-contiguous',pr['path']==complete['path'] and pr['char_start']==cursor,frame=fid,part=n)
            cursor=pr['char_end']
            if part['kind']=='literal_companion':
                check('own-frame-companion-literal-preserved',part['public_literal']==pr['literal'],frame=fid,part=n)
            else:
                metadata=part['metadata']; frame_group_coverage.update(part['group_ids'])
                check('own-frame-descriptor-metadata-identities',[x['id'] for x in metadata]==part['group_ids'],frame=fid,part=n)
                expected_public=f"[Reader {frame['reader']} complete own graphical group {part['group_ids'][0]}; editorial descriptor of original fields: "+json.dumps(metadata,ensure_ascii=False,separators=(',',':'))+']'
                check('own-frame-reversible-descriptor',part['public_literal']==expected_public,frame=fid,part=n)
                for meta in metadata:
                    gid=meta['id']; original=ref_value(meta['original_map_ref'])
                    check('descriptor-complete-original-group',original==donors[gid] and gid.startswith(frame['reader']+'025-'),frame=fid,group=gid)
                    check('descriptor-complete-candidate-hand-role-fields',own_scope_fields.intersection(original)<=set(meta),frame=fid,group=gid)
                    for field,value in meta.items():
                        if field not in ['exact_source_comments','original_map_ref']:
                            check('descriptor-own-field-exact',field in original and value==original[field],frame=fid,group=gid,field=field)
                    check('descriptor-source-comments-exact',meta['exact_source_comments']==[line for line in original['literal_source'].splitlines() if line.lstrip().startswith('%')],frame=fid,group=gid)
        check('complete-own-source-frame-reconstruction',cursor==complete['char_end'] and ''.join(source_parts)==complete['literal'] and sha(''.join(source_parts))==frame['source_reconstruction_sha256'],frame=fid)
        prefix=f"Reader {frame['reader']} complete own {frame['scope']} frame, in original source order. Bracketed graphical descriptors below contain only this reader's own fields; every replaced source group is exactly recoverable from its source reference.\n"
        body=''.join(x['public_literal'] for x in frame['parts'])
        inv_rows=[{'original_json_pointer':refs[k]['json_pointer'],'value':ref_value(k)} for k in frame['original_inventory_refs']]
        suffix='\nComplete own inventory fields in this frame, with their original hand and local candidate scopes:\n'+json.dumps(inv_rows,ensure_ascii=False,separators=(',',':'))
        check('complete-own-public-frame-reconstruction',frame['public']==prefix+body+suffix,frame=fid)
        check('frame-original-group-identities',frame['group_ids']==old['groups'],frame=fid)
        frame_inventory_coverage.update((refs[k]['path'],refs[k]['json_pointer']) for k in frame['original_inventory_refs'])
    check('all60-own-groups-in-public-frames',frame_group_coverage==set(union_groups) and len(frame_group_coverage)==60)
    expected_inventory={(f'out/readers/025/{r}/report.json',f'/inventory/{i}') for r in 'ABC' for i in range(len(json.loads(source(f'out/readers/025/{r}/report.json'))['inventory']))}
    check('all92-original-inventory-public-scopes',frame_inventory_coverage==expected_inventory and len(frame_inventory_coverage)==92)
    check('all60-original-candidate-group-records',provenance['reader_candidate_groups']==union_groups)

    omitted_field_shapes=Counter()
    for container_kind,rows in [('decision',record['decisions']),('locus',record['source_locus_coverage'])]:
        for d in rows:
            key=d.get('id',d['source_locus_id']); locus=union_loci.get(d['source_locus_id'],union_loci['L025-28'])
            check('all-three-own-reader-values',set(d['readers'])==set('ABC') and set(d['reader_source_details'])==set('ABC'),container=container_kind,row=key)
            for reader,detail in d['reader_source_details'].items():
                fid=detail['complete_own_frame_id']; frame=frames[fid]
                check('reader-public-frame-suffix-reconstruction',d['readers'][reader]==detail['public_frame_value']+detail['public_local_suffix'] and detail['public_frame_value']==frame['public'],container=container_kind,row=key,reader=reader)
                check('reader-frame-own-role',frame['reader']==reader and detail['semantic_role']==f'reader_{reader}_complete_own_reading_and_own_candidates' and detail['complete_own_literal_source_ref']==frame['complete_source_ref'],container=container_kind,row=key,reader=reader)
                check('reader-original-locus-role-mapping',detail['stage1_locus_reader_mapping']==locus['readers'][reader],container=container_kind,row=key,reader=reader)
                check('reader-original-group-list',detail['complete_own_group_ids']==locus['readers'][reader]['complete_own_groups'] and [ref_value(x)['id'] for x in detail['own_group_refs']]==detail['complete_own_group_ids'],container=container_kind,row=key,reader=reader)
                check('reader-original-inventory-frame-list',detail['complete_frame_inventory_refs']==frame['original_inventory_refs'],container=container_kind,row=key,reader=reader)
                for ref_field in ['own_group_refs','raw_own_difference_refs','raw_own_doubt_refs','raw_own_local_inventory_refs','complete_frame_inventory_refs','original_C_reader_scope_refs']:
                    for rid in detail[ref_field]:check('own-reader-reference-source-role',refs[rid]['path'].startswith(f'out/readers/025/{reader}/'),container=container_kind,row=key,reader=reader,field=ref_field,ref=rid)
                check('reader-report-silence-preserved',detail['report_silent']==locus['readers'][reader]['report_silent'],container=container_kind,row=key,reader=reader)
                prefix='\nLocal original own-proposal report and doubt fields (their original field roles and order are retained):\n'
                check('reader-local-suffix-labeled',detail['public_local_suffix'].startswith(prefix),container=container_kind,row=key,reader=reader)
                projected=json.loads(detail['public_local_suffix'][len(prefix):])
                expected_refs=detail['raw_own_difference_refs']+detail['raw_own_doubt_refs']+detail['original_C_reader_scope_refs']
                check('reader-local-suffix-original-row-coverage',len(projected)==len(expected_refs),container=container_kind,row=key,reader=reader)
                for local,rid in zip(projected,expected_refs):
                    original=ref_value(rid)
                    field='own_proposal_fields' if 'own_proposal_fields' in local else 'original_reader_scope_and_status_fields'
                    check('reader-local-suffix-pointer-binding',local['original_json_pointer']==refs[rid]['json_pointer'],container=container_kind,row=key,reader=reader,ref=rid)
                    for k,v in local[field].items():check('reader-local-suffix-own-field-exact',k in original and original[k]==v,container=container_kind,row=key,reader=reader,ref=rid,field=k)
                    if field=='original_reader_scope_and_status_fields':check('reader-C-scope-complete-projection',local[field]==original,container=container_kind,row=key,reader=reader,ref=rid)
                    else:
                        for omitted in set(original)-set(local[field]):omitted_field_shapes[omitted]+=1
                        check('reader-local-candidate-hand-role-fields',own_scope_fields.intersection(original)<=set(local[field]),container=container_kind,row=key,reader=reader,ref=rid)
                        check('reader-local-suffix-no-witness-field-adoption',not {'C','H','diff_C','diff_H','marked_in_C','marked_in_H'}&set(local[field]),container=container_kind,row=key,reader=reader,ref=rid)

    check('all216-original-row-identities',set(raw_rows)==set(union_rows) and len(raw_rows)==216)
    original_row_counts=Counter()
    for rid,row in raw_rows.items():
        original=union_rows[rid]; ref=refs[row['raw_row_ref']]
        expected_decisions=[d['id'] for d in physical if d['source_locus_id']==row['source_locus_id']]
        check('original-main-row-binding',row['reader']==original['reader'] and row['section']==original['section'] and row['original_index']==original['original_index'] and row['original_identity']==original['original_identity'] and row['source_locus_id']==original['locus'] and ref['path']==original['raw']['source_path'] and ref['json_pointer']==original['raw']['json_pointer'] and ref_value(row['raw_row_ref'])==original_value(original['raw']),row=rid)
        check('original-main-row-all-fields-retained',row['all_original_fields']==original['all_original_fields'],row=rid)
        check('original-row-selected-decision-correspondence',row['selected_decision_ids']==expected_decisions,row=rid)
        original_row_counts[row['section']]+=1
    check('original-row-counts',dict(original_row_counts)=={'differences':77,'doubts':47,'inventory':92})
    for lid,locus in loci.items():
        expected_decisions=[d for d in physical if d['source_locus_id']==lid]
        check('locus-decision-reciprocity',locus['decision_ids']==[d['id'] for d in expected_decisions],locus=lid)
        if expected_decisions:
            check('locus-selected-reading-reciprocity',locus['selected_readings']==[d['final'] for d in expected_decisions],locus=lid)
        else:
            check('ordinary-source-agreement-closure',lid in ['L025-02','L025-20','L025-27','L025-28'] and len(locus['selected_readings'])==1 and locus['root_ink_choice_applied'] is False and locus['root_source_audit_choice_applied'] is True and locus['root_authority_sections']==['19'],locus=lid)
        check('locus-all-original-rows',[rid for rid,r in raw_rows.items() if r['source_locus_id']==lid]==locus['original_main_row_ids'],locus=lid)
        check('locus-unapproved',locus['main_approved'] is False,locus=lid)
    for gid,g in selected.items():
        check('selected-group-decision-reciprocity',g['decision_ids']==[d['id'] for d in physical if gid in d['selected_group_ids']] and g['selected_readings']==[decisions[x]['final'] for x in g['decision_ids']],group=gid)
        check('selected-group-inventory-reciprocity',g['inventory_ids']==[x['element'] for x in record['inventory'] if gid in x['selected_group_ids']],group=gid)
    for item in record['inventory']:
        ident=item['element']
        check('selected-inventory-status',item['transcribed']=='yes' and item['main_approved'] is False and item['source_inventory_identity']==ident and item['source_inventory_role']=='root-selected' and bool(item['source_attachments']),inventory=ident)
        check('selected-inventory-decision-group-references',set(item['decision_ids'])<=set(decisions) and set(item['selected_group_ids'])<=set(selected),inventory=ident)
        for rid in item['provenance']['original_reader_inventory_rows']:check('selected-inventory-original-role',refs[rid]['path'].endswith('/report.json') and refs[rid]['json_pointer'].startswith('/inventory/'),inventory=ident,ref=rid)
        expected={'element':ident,'decision_ids':item['decision_ids'],'selected_group_ids':item['selected_group_ids'],'source_attachments':[attachment_view(a) for a in item['source_attachments']]}
        check('selected-inventory-map-reciprocity',expected in mapping['selected_inventory_associations'],inventory=ident)
    check('selected-inventory-page-order',[x['page_order'] for x in record['inventory']]==list(range(1,37)))
    check('original13-C-inventory-mapped',set(x for v in inventory.values() for x in v['source_original_C_inventory_ids'])==set(x['element'] for x in json.loads(source('packets/025/C_inventory.json'))))
    check('nested-upper-trace-hand-scope',all(token in inventory['025.S.10']['hand'] for token in ['his hand','undetermined hand']) and inventory['025.S.11']['hand']=='undetermined hand')
    check('final-display-hand-scope',inventory['025.S.31']['hand']=='his hand')
    check('point-hand-scopes',inventory['025.S.29']['hand']=='his hand for que and its descender; undetermined hand for the separate point' and inventory['025.S.30']['hand']=='undetermined hand')
    check('lower-mark-and-archive-hand-scopes',all(inventory[k]['hand']=='undetermined hand' for k in ['025.S.34','025.S.35','025.S.36']))
    check('all-original-metadata-complete',len(provenance['all_original_metadata'])==23 and all(refs[x['complete_original_ref']]['path']==x['source_path'] and json.loads(refs[x['complete_original_ref']]['literal'])==json.loads(source(x['source_path'])) for x in provenance['all_original_metadata']))
    check('original-C-context-and-inventory-unchanged',provenance['original_C_inventory']==union['original_C_inventory'] and provenance['other_C_notation_and_slips_context']==union['other_C_notation_and_slips_context'])

    c_rows={x['source_id']:x for x in record['C_source_rows']}
    check('eight-canonical-C-rows-only',len(c_rows)==8 and set(c_rows)=={x['source_id'] for x in authority['canonical_original_C_rows']})
    c_catalog=json.loads(source('out/checks/scan025_C_doubt_catalog.json'))
    for expected in authority['canonical_original_C_rows']:
        row=c_rows[expected['source_id']]; original=original_value(expected['canonical_catalog_ref'])
        check('canonical-C-original-source-row',row['literal']==original['literal'] and row['char_start']==original['char_start'] and row['char_end']==original['char_end'] and row['source_path']==original['source_path'] and row['line']==original['line'],row=row['source_id'])
        check('canonical-C-original-parts-complete',row['original_source_parts']==expected['source_parts'] and [x['part_id'] for x in row['source_parts']]==[x['part_id'] for x in expected['source_parts']],row=row['source_id'])
        check('canonical-C-root-outcome',row['selected_outcome']==expected['authorized_status'],row=row['source_id'])
        check('canonical-C-decision-reciprocity',row['decision_ids']==[d['id'] for d in physical if row['source_id'] in d['C_source_row_ids']],row=row['source_id'])
        check('canonical-C-complete-original-reference',ref_value(row['original_row_reference'])==original,row=row['source_id'])
        for reader,rid in row['reader_reported_scopes'].items():check('canonical-C-reader-scopes-preserved',ref_value(rid)==original_value(expected['reader_reported_scopes'][reader]),row=row['source_id'],reader=reader)
        for part in row['source_parts']:
            old_part=next(x for x in expected['source_parts'] if x['part_id']==part['part_id'])
            check('canonical-C-part-original-qualification-retained',part['decision_status']==old_part['decision_status'] and part['original_decision_status']==old_part['decision_status'] and part['location_label']==old_part['location_label'],row=row['source_id'],part=part['part_id'])
            check('canonical-C-part-selected-binding',part['selected_outcome']==row['selected_outcome'] and part['main_approved'] is False and all(pid in decisions for pid in part['decision_ids']) and same_span(part['root_authority'],expected['root_section_ref']),row=row['source_id'],part=part['part_id'])
    check('R08-selected-two-state-word',decisions['SRC025-P18']['alternatives']==['determinés','determines'] and '\\unsure{determinés|determines}' in decisions['SRC025-P18']['final'] and len(c_rows['C025-R08']['selected_local_outcomes'])==2)
    check('R08-raw-C-three-state-witness',decisions['SRC025-P18']['C']=='\\unsure{determinés|déterminés|determines}' and decisions['SRC025-P18']['H']=='déterminés')
    check('pre-les-selected-five-states',decisions['SRC025-P13']['alternatives']==donors['C025-G08']['complete_candidates'] and len(decisions['SRC025-P13']['alternatives'])==5)
    check('B-K-own-firm-state-retained',ref_value(decisions['SRC025-P16']['reader_source_details']['B']['own_group_refs'][0])['alternatives']==[] and ref_value(decisions['SRC025-P16']['reader_source_details']['B']['own_group_refs'][0])['qualification'] is None)
    for doubt in record['doubts']:
        d=decisions[doubt['decision_id']]
        check('remaining-doubt-selected-binding',doubt['reading']==d['final'] and doubt['alternatives']==d['alternatives'] and doubt['selected_group_ids']==d['selected_group_ids'] and doubt['source_attachments']==d['source_attachments'] and doubt['root_crop_evidence']==d['root_crop_evidence'] and doubt['main_approved'] is False,doubt=doubt['id'])
    check('resolved-R07-no-retained-doubt',all(x['decision_id']!='SRC025-P15' for x in record['doubts']))
    check('two-apparatus-abbreviations',len(record['abbreviations'])==2 and [(x['form'],x['expansion']) for x in record['abbreviations']]==[(x['form'],x['expansion']) for x in authority['authorized_abbreviations']])
    for ab,expected in zip(record['abbreviations'],authority['authorized_abbreviations']):
        check('abbreviation-root-authority',same_span(ab['root_authority'],expected['root_authority_ref']) and ab['main_approved'] is False and ab['form'] in draft and ab['expansion'] not in draft,form=ab['form'])
    check('attributed-notes-no-proof-event',isinstance(record['notes'],str) and record['notes']==record['attributed_content_note']['text']==record['root_selected_content_note']['text'] and record['attributed_content_note']['attributed_only'] is True and record['root_selected_content_note']['attributed_only'] is True and record['attributed_content_note']['mathematical_check_performed'] is False and record['root_selected_content_note']['mathematical_check_performed'] is False)
    for binding in ['frozen_source_union','frozen_source_skeleton','original_lossless_source_pool','frozen_reader_fingerprints']:
        item=provenance[binding]
        check('record-frozen-provenance-binding',item['sha256']==sha(source(item['path'])),binding=binding)
    projection_result=check_projection(handoff,record,mapping,check,source)
    return {'decisions':len(decisions),'physical_decisions':len(physical),'source_only_rows':len(source_only),'doubts':len(record['doubts']),'inventory':len(inventory),'C_source_rows':len(c_rows),'source_loci':len(loci),'original_main_rows':dict(original_row_counts),'complete_own_frames':len(frames),'source_reference_pool_entries':len(refs),'own_public_suffix_omitted_field_shapes':dict(omitted_field_shapes),'projection':projection_result}


def check_projection(handoff,record,mapping,check,source):
    from bisect import bisect_left
    from functools import lru_cache
    manifest_path=handoff['frozen_artifacts']['projection_manifest']['path']
    manifest=json.loads(source(manifest_path))
    codec=json.loads(source(manifest['codec']['path']))
    check('projection-codec-hash',sha(source(manifest['codec']['path']))==manifest['codec']['sha256'])
    base=json.loads(source(codec['base_pool']['path']))
    check('projection-frozen-base-binding',sha(source(codec['base_pool']['path']))==codec['base_pool']['sha256']=='b0a10f517a4b2037e746080d9c0a7450016c514b0b046f3024e723314d949aa0')
    base_files={x['id']:x for x in base['files']}
    base_strings={x['id']:x for x in base['strings']}
    base_spans={x['id']:x for x in base['spans']}
    source_table={x['id']:x for x in codec['source_table']}
    strings={x['id']:x for x in codec['strings']}
    containers={x['id']:x for x in codec['containers']}
    used_paths=set(); geometry={}; json_cache={}; position_cache={}
    spec=importlib.util.spec_from_file_location('scan025_qa_source_inventory_projection',OUT/'scan025_qa_source_inventory.py')
    helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)

    def text_path(path,expected_hash=None):
        text=source(path)
        if path not in used_paths:
            used_paths.add(path)
            if expected_hash:check('projection-used-source-hash',sha(text)==expected_hash,path=path)
        return text

    def qtext(q):
        item=source_table[q]
        return text_path(item['path'],item['sha256'])

    def positions(path):
        if path not in position_cache:position_cache[path]=helper.json_spans(source(path))
        return position_cache[path]

    def bounds(path,a,b):
        if path not in geometry:
            text=source(path); extra=0; nonascii=[]; cumulative=[]
            for i,c in enumerate(text):
                if ord(c)>127:extra+=len(c.encode('utf-8'))-1;nonascii.append(i);cumulative.append(extra)
            geometry[path]=([m.start() for m in re.finditer('\n',text)],nonascii,cumulative)
        lines,nonascii,cumulative=geometry[path]
        def byte(i):
            n=bisect_left(nonascii,i)
            return i+(cumulative[n-1] if n else 0)
        return [a,b,byte(a),byte(b),bisect_left(lines,a)+1,bisect_left(lines,max(a,b-1))+1]

    def json_document(path):
        if path not in json_cache:json_cache[path]=json.loads(source(path))
        return json_cache[path]

    def base_value(ref):
        file=base_files[ref['file']];path=file['path']; text=text_path(path,file['sha256_utf8']);span=base_spans[ref['span']]
        value=at(json_document(path),ref['pointer']); a,b=span['char_start'],span['char_end_exclusive']
        check('projection-base-reference-exact-pointer',span['source_file']==ref['file'] and positions(path)[ref['pointer']]==(a,b) and json.loads(text[a:b])==value,file=ref['file'],pointer=ref['pointer'])
        return value

    def external_value(ref):
        q=ref['source'];text=qtext(q);path=source_table[q]['path'];a,b=ref['bounds'][:2]
        value=at(json_document(path),ref['pointer'])
        check('projection-external-reference-exact-pointer',ref['bounds']==bounds(path,a,b) and positions(path)[ref['pointer']]==(a,b) and json.loads(text[a:b])==value,source=q,pointer=ref['pointer'])
        return value

    def decode(value):
        if isinstance(value,dict) and set(value)=={'$t'}:return string_value(value['$t'])
        if isinstance(value,dict) and set(value)=={'$o'}:return object_value(value['$o'])
        if isinstance(value,(dict,list)):raise ValueError('Unknown encoded container: '+repr(value)[:200])
        return value

    @lru_cache(None)
    def string_value(sid):
        entry=strings[sid];recipe=entry['recipe']
        if 'literal' in recipe:value=recipe['literal']
        elif 'base_json_string' in recipe:value=base_value(recipe['base_json_string'])
        elif 'external_json_string' in recipe:value=external_value(recipe['external_json_string'])
        elif 'base_pool_string' in recipe:
            value=base_strings[recipe['base_pool_string']]['literal']
            if not isinstance(value,str):
                span=base_spans[value['span_ref']];file=base_files[span['source_file']]
                value=text_path(file['path'],file['sha256_utf8'])[span['char_start']:span['char_end_exclusive']]
        elif 'source_span' in recipe:
            span=recipe['source_span'];q=span['source'];a,b=span['bounds'][:2]
            value=qtext(q)[a:b]
            check('projection-string-source-bounds',span['bounds']==bounds(source_table[q]['path'],a,b),string=sid)
        elif 'concatenate' in recipe:value=''.join(decode(x) for x in recipe['concatenate'])
        elif 'json_serialization' in recipe:
            form=recipe['json_serialization'];value=json.dumps(decode(form['value']),ensure_ascii=form['ensure_ascii'],separators=tuple(form['separators']))
        else:raise ValueError('Unknown string recipe '+sid)
        check('projection-string-exact-value',isinstance(value,str) and len(value)==entry['characters'] and len(value.encode('utf-8'))==entry['utf8_bytes'] and sha(value)==entry['sha256'],string=sid)
        return value

    @lru_cache(None)
    def object_value(oid):
        entry=containers[oid]; kind=entry['kind']
        if kind=='object':return {k:decode(v) for k,v in entry['items']}
        if kind=='array':return [decode(v) for v in entry['items']]
        if kind=='base_json_value':return base_value(entry['source'])
        if kind=='external_json_value':return external_value(entry['source'])
        if kind!='source_span_object':raise ValueError('Unknown container kind '+kind)
        q=entry['source']; path=source_table[q]['path'];text=qtext(q);a,b=entry['bounds'];loc=bounds(path,a,b);literal=text[a:b];file_hash=source_table[q]['sha256']
        values={'path':path,'workspace_path':path,'source_path':path,'out_relative_path':path[4:],'sha256':file_hash,'sha256_utf8':file_hash,'source_sha256_utf8':file_hash,'char_start':a,'char_end':b,'char_end_exclusive':b,'utf8_byte_start':loc[2],'utf8_byte_end':loc[3],'utf8_byte_end_exclusive':loc[3],'line_start':loc[4],'line_end':loc[5],'line_start_1based':loc[4],'line_end_1based':loc[5],'body_sha256':sha(literal),'literal_sha256_utf8':sha(literal),'literal':literal}
        extra=iter(entry['extra_values']); result={}
        for key,rule in codec['source_span_object_templates'][entry['template']]:result[key]=decode(next(extra)) if rule=='extra' else values[rule]
        check('projection-span-template-extras-exhausted',next(extra,None) is None,container=oid)
        return result

    docs={}; pointer_total=0
    for description in codec['documents']:
        value=decode(description['root']);form=description['serializer'];text=json.dumps(value,ensure_ascii=form['ensure_ascii'],indent=form['indent'])+form['ending'];path=description['path']
        check('projection-complete-document-exact-UTF8',text==source(path) and sha(text)==description['sha256'] and len(text)==description['characters'] and len(text.encode('utf-8'))==description['utf8_bytes'],path=path)
        actual_positions=positions(path); recorded_positions=codec['document_pointer_bounds'][path]
        check('projection-all-document-pointer-identities',set(actual_positions)==set(recorded_positions),path=path)
        for pointer,(a,b) in actual_positions.items():
            item=recorded_positions[pointer]
            check('projection-document-pointer-exact-bounds',[item[k] for k in ['char_start','char_end','utf8_byte_start','utf8_byte_end','line_start','line_end']]==bounds(path,a,b),path=path,pointer=pointer)
        pointer_total+=len(actual_positions);docs[description['id']]=(description,value,text)
    for sid in strings:string_value(sid)
    for oid in containers:object_value(oid)
    check('projection-three-document-identities',len(docs)==3 and codec['documents']==manifest['documents'])
    seen_strings=set();seen_objects=set();field_rows=[];line_sequence=0
    def known(value,row):
        if isinstance(value,dict) and set(value)=={'$t'}:check('projection-string-defined-before-use',value['$t'] in seen_strings,row=row,ref=value['$t'])
        elif isinstance(value,dict) and set(value)=={'$o'}:check('projection-container-defined-before-use',value['$o'] in seen_objects,row=row,ref=value['$o'])
    for page in manifest['pages']:
        text=source(page['path']);lines=text.splitlines()
        check('projection-page-frozen-hash',sha(text)==page['sha256'] and len(text.encode('utf-8'))==page['utf8_bytes'] and len(lines)==page['lines'],path=page['path'])
        for line in lines:
            line_sequence+=1;row=json.loads(line)
            if 't' in row:
                sid=row['t'];check('projection-string-definition-once',sid not in seen_strings and row['recipe']==strings[sid]['recipe'],row=line_sequence,string=sid)
                for dependency in row['recipe'].get('concatenate',[]):known(dependency,line_sequence)
                if 'json_serialization' in row['recipe']:known(row['recipe']['json_serialization']['value'],line_sequence)
                seen_strings.add(sid)
            elif 'o' in row:
                oid=row['o'];check('projection-container-definition-once',oid not in seen_objects and {k:v for k,v in row.items() if k!='o'}=={k:v for k,v in containers[oid].items() if k!='id'},row=line_sequence,container=oid)
                entry=containers[oid]
                dependencies=([v for k,v in entry['items']] if entry['kind']=='object' else entry['items'] if entry['kind']=='array' else entry['extra_values'] if entry['kind']=='source_span_object' else [])
                for dependency in dependencies:known(dependency,line_sequence)
                seen_objects.add(oid)
            else:
                did,pointer=row['field'];description,value,full=docs[did];path=description['path'];a,b=positions(path)[pointer];known(row['value'],line_sequence)
                check('projection-field-exact-value-and-boundaries',decode(row['value'])==at(value,pointer) and row['span']==bounds(path,a,b) and json.loads(full[a:b])==at(value,pointer),row=line_sequence,path=path,pointer=pointer)
                field_rows.append((path,pointer,line_sequence))
    expected_rows=[(x['document'],x['json_pointer'],x['line_sequence']) for x in manifest['field_index']]
    check('projection-field-index-complete-ordered-replay',field_rows==expected_rows and len(field_rows)==manifest['total_review_field_count']==1775 and len(set((p,ptr) for p,ptr,n in field_rows))==1775)
    check('projection-all-string-container-definitions',seen_strings==set(strings) and seen_objects==set(containers) and len(strings)==manifest['string_count']==3719 and len(containers)==manifest['container_count']==4503)
    return {'documents':len(docs),'strings':len(strings),'containers':len(containers),'projected_fields':len(field_rows),'pages':len(manifest['pages']),'complete_document_pointers':pointer_total,'source_texts_used':len(used_paths),'external_S_original_opened':False,'stage1_replay_repeated':False}


if __name__=='__main__':main()
