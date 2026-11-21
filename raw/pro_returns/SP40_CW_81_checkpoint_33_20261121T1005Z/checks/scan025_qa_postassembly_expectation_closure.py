#!/usr/bin/env python3
"""Close only the three documented checker shape assumptions; never rerun QA."""
from pathlib import Path
from copy import deepcopy
from collections import Counter
import hashlib,json

BASE=Path(__file__).resolve().parents[2];O=BASE/'out/checks'
def sha(v):return hashlib.sha256(v if isinstance(v,bytes) else v.encode('utf-8')).hexdigest()
def load(name):return json.loads((O/name).read_text())
def dump(v):return json.dumps(v,ensure_ascii=False,indent=2)+'\n'

initial_path=O/'scan025_qa_postassembly_replay.json'
initial=load(initial_path.name)
assert sha(initial_path.read_bytes())=='fb93c642caf752b813f3e576095a6eaeaff1a9a9356aa5f76ce805030ca7bd84'
record=load('scan025_record_draft.json');mapping=load('scan025_final_source_map.json')
assert sha((O/'scan025_record_draft.json').read_bytes())=='74abd9b6e3779e1cd7e051027574bfc6436aa62b395737b2a6dbbcdc454768d7'
map_hash=sha((O/'scan025_final_source_map.json').read_bytes())
assert map_hash=='c4895161d5aa8caf7f3a1767a3de67546f6290ed7d25d92cec937fdc6067849f'
flag_counts=Counter(x['check'] for x in initial['concrete_defects'])
assert flag_counts=={'selected-group-map-record-equality':1,'S-source-only-status':7,'reader-C-scope-complete-projection':57}
map_ref={'path':'out/checks/scan025_final_source_map.json','sha256':map_hash}
draft_path='out/checks/scan025_final_draft.tex'
draft=(BASE/draft_path).read_text()
assert sha(draft)=='e5098e342952e5103022ef30641cdda851e5d74203913db9f2060661e50297ad'

def strip_map_bindings(value):
    if isinstance(value,dict):
        if 'source_map_reference' in value:assert value['source_map_reference']==map_ref
        return {k:strip_map_bindings(v) for k,v in value.items() if k!='source_map_reference'}
    if isinstance(value,list):return [strip_map_bindings(v) for v in value]
    return value

def add_map_bindings(value):
    if isinstance(value,dict):
        result={k:add_map_bindings(v) for k,v in value.items()}
        if result.get('workspace_path')==draft_path:
            assert 'source_map_reference' not in result
            result['source_map_reference']=deepcopy(map_ref)
        return result
    if isinstance(value,list):return [add_map_bindings(v) for v in value]
    return value

def group_to_map(group):
    result=strip_map_bindings(group);s=result['source']
    assert s['path']=='checks/scan025_final_draft.tex' and s['workspace_path']==draft_path and s['manifest']=='scan025_final_source_map.json'
    s['path']=s.pop('workspace_path');s.pop('manifest');s['sha256_utf8']=s['sha256']
    return result

def group_to_record(group):
    result=deepcopy(group);s=result['source']
    assert s['path']==draft_path and s.pop('sha256_utf8')==s['sha256']
    s['workspace_path']=s['path'];s['path']=s['path'][4:];s['manifest']='scan025_final_source_map.json'
    return add_map_bindings(result)

group_proofs=[]
for rg,mg in zip(record['selected_graphical_groups'],mapping['selected_groups']):
    assert rg['id']==mg['id'] and group_to_map(rg)==mg and group_to_record(mg)==rg
    keys=['path','sha256','sha256_utf8','workspace_path','manifest','source_map_reference']
    group_proofs.append({'id':rg['id'],'record_source_shape':{k:rg['source'][k] for k in keys if k in rg['source']},'map_source_shape':{k:mg['source'][k] for k in keys if k in mg['source']},'all_other_group_fields_and_exact_literal_unchanged':True,'forward_exact':True,'inverse_exact':True})

S_proofs=[]
for d in record['decisions'][27:]:
    assert d['diff_C'] is False and d['diff_H'] is False and d['root_ink_choice_applied'] is False and d['root_source_audit_choice_applied'] is True
    assert d['crop']==[] and d['root_crop_evidence']==[] and d['selected_group_ids']==[] and d['proof_event'] is False and d['confidence']=='high' and d['main_approved'] is False
    assert len(d['source_attachments'])==1
    a=d['source_attachments'][0]
    assert a['workspace_path']==draft_path and a['char_start']==0 and a['char_end']==len(draft) and a['literal']==draft and a['body_sha256']==sha(draft) and a['source_map_reference']==map_ref
    assert d['root_source_attachment_status']=='Complete selected page source supplied for scope coverage; no local ink correction attached.'
    S_proofs.append({'decision_id':d['id'],'source_id':d['S_id'],'prior_checker_assumption':'source_attachments must be empty','actual_attachment_scope':'the complete exact selected-page source as context','source_attachment_without_repeated_literal':{k:v for k,v in a.items() if k!='literal'},'root_source_attachment_status':d['root_source_attachment_status'],'source_only_scope':d['source_only_scope'],'evidence':d['evidence'],'diff_C':False,'diff_H':False,'root_ink_choice_applied':False,'crop':[],'proof_event':False})

refs=record['provenance']['source_reference_pool'];scope_proofs={};uses=0
exclusions={'A':{'source_file','source_heading','raw_source_row'},'B':{'literal_source_row'},'C':{'original_row_literal'}}
for kind,rows in [('decision',record['decisions']),('locus',record['source_locus_coverage'])]:
    for row in rows:
        for reader,detail in row['reader_source_details'].items():
            local=json.loads(detail['public_local_suffix'].split('\n',2)[2])
            ids=detail['raw_own_difference_refs']+detail['raw_own_doubt_refs']+detail['original_C_reader_scope_refs']
            for value,rid in zip(local,ids):
                if 'original_reader_scope_and_status_fields' not in value:continue
                original=json.loads(refs[rid]['literal']); public=value['original_reader_scope_and_status_fields']
                omitted={k:original[k] for k in original if k not in public}
                assert set(omitted)==exclusions[reader]
                assert public=={k:v for k,v in original.items() if k not in exclusions[reader]}
                reconstructed={k:public[k] if k in public else omitted[k] for k in original}
                assert reconstructed==original
                usage={'container':kind,'row':row.get('id',row['source_locus_id']),'reader':reader}
                if rid not in scope_proofs:
                    scope_proofs[rid]={'reader':reader,'source_path':refs[rid]['path'],'source_json_pointer':refs[rid]['json_pointer'],'complete_raw_reference_hash':refs[rid]['body_sha256'],'original_field_order':list(original),'original_scope_row':original,'public_scope_row':public,'excluded_witness_source_fields':omitted,'forward_exact':True,'inverse_exact':True,'uses':[]}
                scope_proofs[rid]['uses'].append(usage);uses+=1
assert len(scope_proofs)==24 and uses==57

result={'scan':25,'source_only':True,'status':'All three checker expectation gaps closed by exact field mappings; no assembled source defect found.','initial_replay':{'path':str(initial_path.relative_to(BASE)),'sha256':sha(initial_path.read_bytes()),'preserved_unchanged':True},'closure_script_sha256':sha(Path(__file__).read_bytes()),'frozen_record_sha256':sha((O/'scan025_record_draft.json').read_bytes()),'frozen_source_map_sha256':map_hash,'frozen_page_sha256':sha(draft),'flagged_instances':sum(flag_counts.values()),'flag_families':dict(flag_counts),'group_attachment_shape_morphism':{'forward':'Erase only checked current source_map_reference attachments; on group /source replace path by workspace_path, remove workspace_path and manifest, add sha256_utf8 equal to sha256.','inverse':'On group /source remove the duplicate sha256_utf8 after equality check, add workspace_path equal to its complete path, remove only leading out/ from path, add exact manifest name; add the checked current map binding to every selected attachment.','groups':group_proofs},'S_whole_page_context_attachments':S_proofs,'C_scope_public_projection':{'forward':'Remove only the enumerated witness-source fields from each original reader C-scope object; preserve every other key and value.','inverse':'Merge the exact retained excluded fields back in original key order, yielding the entire exact original scope object.','unique_original_rows':24,'public_uses':57,'rows':scope_proofs},'unclosed_flagged_instances':0,'assembled_source_mutations':0,'replay_repeated':False,'stage1_replay_repeated':False,'images_opened':0,'main_approved':False,'root_approval_status':'Root independent complete review and approval remain pending.'}
output=O/'scan025_qa_postassembly_expectation_closure.json';output.write_text(dump(result))
print(dump({'path':str(output.relative_to(BASE)),'sha256':sha(output.read_bytes()),'status':result['status'],'flagged_instances_closed':65,'remaining_defects':0,'initial_replay_preserved':True}))
