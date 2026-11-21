"""Build a reviewable source-only record; no page/record/application writes."""
from pathlib import Path
import collections
import copy
import hashlib
import json

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'out/checks'
P='scan026_release_'
def sha(b):return hashlib.sha256(b).hexdigest()
def compact(v):return json.dumps(v,ensure_ascii=False,separators=(',',':'))
def encoded(v):return (json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode()
def read(name):return json.loads((OUT/name).read_text())
def save(name,value):
    assert name.startswith(P)
    b=encoded(value);(OUT/name).write_bytes(b)
    return {'path':'out/checks/'+name,'sha256':sha(b),'bytes':len(b)}
def ref(name,p=''):return {'path':'out/checks/'+name,'json_pointer':p}
def esc(k):return str(k).replace('~','~0').replace('/','~1')
def ptr(v,p):
    for k in p.split('/')[1:] if p else []:
        k=k.replace('~1','/').replace('~0','~');v=v[int(k)] if isinstance(v,list) else v[k]
    return v

input_names=[
    'scan026_source_union_v01.json','scan026_source_union_state_pool_v01.json','scan026_source_union_sources_v01.json',
    'scan026_source_record_scaffold_v01.json','scan026_source_selected_contract_v01.json',
    'scan026_root_decisions.json','scan026_root_locus_supplement_v01.json',
    'scan026_root_scalar_authority_v01.json','scan026_root_consequential_authority_v01.json','scan026_root_notes_abbreviation_authority_v01.json',
    P+'audit_v02.json',P+'scalar_authority_projection_v02.json',P+'witness_bindings_v02.json',
    P+'exact_raw_values_v01.json',P+'exact_own_source_spans_v01.json',P+'inventory_bindings_v01.json',P+'C_row_outcomes_v01.json',
]
input_manifest=[{'path':'out/checks/'+n,'sha256':sha((OUT/n).read_bytes()),'bytes':(OUT/n).stat().st_size} for n in input_names]
union=read('scan026_source_union_v01.json');union_by={x['locus_id']:x for x in union};union_ix={x['locus_id']:i for i,x in enumerate(union)}
scaffold=read('scan026_source_record_scaffold_v01.json')
contract=read('scan026_source_selected_contract_v01.json');contract_by={x['locus_id']:x for x in contract['loci']};contract_ix={x['locus_id']:i for i,x in enumerate(contract['loci'])}
audit=read(P+'audit_v02.json');audit_by={x['source_locus_id']:x for x in audit['rows']}
scalar=read(P+'scalar_authority_projection_v02.json')['rows'];scalar_by={x['source_locus_id']:x for x in scalar}
authority=read('scan026_root_scalar_authority_v01.json')
consequence=read('scan026_root_consequential_authority_v01.json')
notes=read('scan026_root_notes_abbreviation_authority_v01.json')
root_decisions=read('scan026_root_decisions.json')
root_supplement=read('scan026_root_locus_supplement_v01.json')
raw_list=read(P+'exact_raw_values_v01.json')['records'];raw={x['record_id']:x for x in raw_list}
span_pool=read(P+'exact_own_source_spans_v01.json');spans={x['span_id']:x for x in span_pool['spans']}
registry=read('scan026_source_union_sources_v01.json')
for alias,info in registry.items():assert sha((BASE/info['path']).read_bytes())==info['sha256']
loaded_json={};loaded_bytes={}
reference_table={x['reference_id']:x for x in contract['reference_table']}
def reference_value(jid):
    r=reference_table[jid];path=r['path']
    if path not in loaded_json:
        loaded_bytes[path]=(BASE/path).read_bytes();loaded_json[path]=json.loads(loaded_bytes[path])
    assert sha(loaded_bytes[path])==r['file_sha256']
    value=ptr(loaded_json[path],r['json_pointer'])
    exact=loaded_bytes[path].decode()[r['raw_json_char_start']:r['raw_json_char_end']]
    assert sha(exact.encode())==r['raw_json_sha256'] and compact(json.loads(exact))==compact(value)
    assert sha(compact(value).encode())==r['ordered_decoded_value_sha256']
    return copy.deepcopy(value)
for jid in reference_table:reference_value(jid)

selected_models={};selected_inverse=[]
def selected_model(lid,stack=()):
    assert lid not in stack
    if lid in selected_models:return selected_models[lid]
    binding=contract_by[lid]['selected_state_binding'];kind=binding['kind']
    if kind=='exact_complete_candidate_array':
        model={'kind':kind,'candidates':reference_value(binding['array_ref'])}
        assert len(model['candidates'])==binding['candidate_count']
    elif kind=='singleton_exact_object':
        model={'kind':kind,'candidates':[reference_value(binding['object_ref'])]}
    elif kind=='whole_object_permutation':
        original=reference_value(binding['original_array_ref']);order=binding['new_index_to_old_index']
        values=[original[i] for i in order]
        inverse=[values[i] for i in binding['inverse_old_index_to_new_index']]
        assert compact(inverse)==compact(original)
        model={'kind':kind,'candidates':values,'exact_original_candidates':original,'new_index_to_old_index':order,'inverse_old_index_to_new_index':binding['inverse_old_index_to_new_index'],'root_scope':reference_value(binding['root_scope_ref'])}
    elif kind=='exact_parent_component_projection':
        model={'kind':kind,'component_values':[reference_value(j) for j in binding['ordered_value_refs']],
               'root_scope':reference_value(binding['shared_root_scope_ref']),
               'complete_parent_candidates':reference_value(binding['parent_array_ref']),
               'explicit_parent_indices':binding['explicit_parent_indices']}
    elif kind in ['fixed_parent_with_scoped_child_candidates','fixed_parent_text_with_scoped_child_candidates']:
        model={'kind':kind,'root_scope':reference_value(binding['root_scope_ref']),
               'children':[{'locus_id':child,'complete_selected_scope':selected_model(child,stack+(lid,))} for child in binding['child_loci']],
               'scope_rule':binding['scope_rule']}
        if 'original_A_parent_candidate_provenance_ref' in binding:
            model['original_A_parent_candidate_provenance']=reference_value(binding['original_A_parent_candidate_provenance_ref'])
    else:raise AssertionError((lid,kind))
    selected_models[lid]=model
    selected_inverse.append({'locus_id':lid,'contract_pointer':f'/loci/{contract_ix[lid]}/selected_state_binding','kind':kind,'expanded_ordered_sha256':sha(compact(model).encode()),'contract_binding_exact':binding})
    return model
for row in scalar:selected_model(row['source_locus_id'])

# The excluded fields stay intact in the frozen R object. Rejoining the two exact
# key sets in the original key order is checked below for each public projection.
excluded_report_fields=[
    'C','H','C_anchor','H_anchor','C_reading_summary','H_reading_summary','C_doubt_status',
    'diff_C','diff_H','marked_in_H','C_count_parent','H_count_parent','H_parent_scope',
    'raw_diff_C','raw_diff_H','raw_diff_H_before_parent_count','witness_excerpt_policy',
]
reader_projection_maps=[]
def reader_value(lid,role):
    bundle=audit_by[lid]['readers'][role]
    categories=bundle['source_categories']
    own_literals=[]
    for sid in bundle['exact_local_source_span_ids']:
        item=spans[sid]
        own_literals.append({'span_id':sid,'literal':item['span']['literal']})
    groups=[{'raw_record':rid,'exact_original_fields':copy.deepcopy(raw[rid]['value'])} for rid in categories.get('source_group_records',[])]
    own_rows=[]
    for category in ['difference_records','doubt_records']:
        for rid in categories.get(category,[]):
            original=raw[rid]['value']
            retained={k:v for k,v in original.items() if k not in excluded_report_fields}
            excluded={k:v for k,v in original.items() if k in excluded_report_fields}
            recovered={k:(retained[k] if k in retained else excluded[k]) for k in original}
            assert compact(recovered)==compact(original)
            own_rows.append({'raw_record':rid,'original_role':category,'own_fields':retained})
            reader_projection_maps.append({'locus_id':lid,'reader':role,'raw_record':rid,'original_key_order':list(original),'retained_keys':list(retained),'excluded_keys':list(excluded),'exact_source_ref':raw[rid]['source']})
    value={
        'reader':role,'exact_local_source':own_literals,'complete_original_source_groups':groups,
        'own_report_and_doubt_fields':own_rows,
        'original_inventory_scopes':[{'raw_record':rid,'exact_original_fields':copy.deepcopy(raw[rid]['value'])} for rid in categories.get('inventory_records',[])],
        'original_complete_source_scope_records':[{'raw_record':rid,'exact_original_fields':copy.deepcopy(raw[rid]['value'])} for rid in categories.get('other_state_records',[])],
        'complete_own_source_partition':ref('scan026_source_state_catalog_v01.json',f'/complete_source_partitions/{role}'),
    }
    text=compact(value);assert compact(json.loads(text))==text
    return text

record_rows=[];blueprint_rows=[]
for i,s in enumerate(scalar):
    lid=s['source_locus_id'];entry=copy.deepcopy(s);a=audit_by[lid];root=a['root_authority'];rd=root['decision'];model=selected_models[lid]
    if 'candidates' in model:
        alternatives=[compact(x) for x in model['candidates']]
        assert compact([json.loads(x) for x in alternatives])==compact(model['candidates'])
    else:
        alternatives=[compact(model)]
        assert compact(json.loads(alternatives[0]))==compact(model)
    if lid=='L051':
        evidence=rd['evidence'];evidence_ref=ref('scan026_root_locus_supplement_v01.json','/agreed_locus/evidence')
    else:
        evidence=ptr(root_decisions,root['body_ref']['json_pointer']);evidence_ref=root['body_ref']
    entry.update(
        readers={role:reader_value(lid,role) for role in 'ABC'},alternatives=alternatives,evidence=evidence,
        qualification=compact(rd),root_selected_state_model=model,
        selected_state_binding=contract_by[lid]['selected_state_binding'],
        selected_group_ids=contract_by[lid]['selected_source_groups'],
        source_attachments=contract_by[lid]['selected_source_spans'],
        witness_source_references=a['exact_witnesses'],
        C_source_part_ids=a['C_source_part_ids'],C_recurrence_binding=a['C_recurrence_binding'],
        crop=[root['crop_path']] if root.get('crop_path') else [],root_crop_evidence=[root] if root.get('crop_path') else [],
        root_ink_choice_applied=True,root_source_audit_choice_applied=True,
        mathematical_consequence=consequence['mathematical_consequence_by_locus'].get(lid,consequence['all_other_loci_mathematical_consequence']),
        provenance={'root_scalar_ref':ref('scan026_root_scalar_authority_v01.json',f'/rows/{i}'),'authorized_witness_projection_ref':ref(P+'scalar_authority_projection_v02.json',f'/rows/{i}'),'root_evidence_ref':evidence_ref,'root_qualification_object_ref':root['decision_ref'],'selected_contract_ref':ref('scan026_source_selected_contract_v01.json',f'/loci/{contract_ix[lid]}'),'original_all_reader_union_ref':a['original_union_ref']},
    )
    for k,v in s.items():assert compact(entry[k])==compact(v)
    record_rows.append(entry)
    blueprint_rows.append({'record_index':i,'locus_id':lid,'scalar_index':i,'original_union_index':union_ix.get(lid),'selected_contract_index':contract_ix[lid],'root_decision_ref':root['decision_ref'],'root_evidence_ref':evidence_ref,'source_attachment_count':len(entry['source_attachments']),'mathematical_consequence_pointer':'/mathematical_consequence_by_locus/'+lid if lid in consequence['mathematical_consequence_by_locus'] else '/all_other_loci_mathematical_consequence'})

# Inventory kinds are finite source-scope proposals for root review. These choices
# do not change any selected reading, component state, attribution or count flag.
L_kinds={
 'L001':'text','L002':'text','L003':'display','L004':'text','L005':'text','L006':'drawing','L007':'insertion','L008':'insertion','L009':'text','L010':'drawing',
 'L011':'insertion','L012':'deletion','L013':'drawing','L014':'drawing','L015':'diagram','L016':'deletion','L017':'drawing','L018':'drawing','L019':'drawing','L020':'drawing',
 'L021':'text','L022':'drawing','L023':'text','L024':'drawing','L025':'text','L026':'drawing','L027':'drawing','L028':'text','L029':'display','L030':'drawing',
 'L031':'deletion','L032':'insertion','L033':'drawing','L034':'text','L035':'drawing','L036':'insertion','L037':'drawing','L038':'drawing','L039':'text','L040':'drawing',
 'L041':'drawing','L042':'text','L043':'drawing','L044':'drawing','L045':'deletion','L046':'text','L047':'text','L048':'drawing','L049':'drawing','L050':'drawing','L051':'text','L052':'drawing',
}
hand_fields=[]
def collect_hand_nodes(value,path=''):
    if isinstance(value,dict):
        for k,v in value.items():
            p=path+'/'+esc(k)
            if 'hand' in k.lower():yield p,v
            else:yield from collect_hand_nodes(v,p)
    elif isinstance(value,list):
        for i,v in enumerate(value):yield from collect_hand_nodes(v,path+'/'+str(i))

inventory=[];inventory_review=[]
for i,d in enumerate(record_rows):
    lid=d['source_locus_id'];rd=audit_by[lid]['root_authority']['decision']
    field_nodes=[]
    if 'hand' in rd:field_nodes.append({'source_scope':'root_decision','pointer':'/hand','value':rd['hand']})
    field_nodes.extend({'source_scope':'root_selected_state_model','pointer':p,'value':v} for p,v in collect_hand_nodes(d['root_selected_state_model']))
    values=[];lookup={};assignments=[]
    for item in field_nodes:
        k=compact(item['value'])
        if k not in lookup:lookup[k]=len(values);values.append(item['value'])
        assignments.append({'source_scope':item['source_scope'],'pointer':item['pointer'],'value_index':lookup[k]})
    reconstructed=[{'source_scope':a['source_scope'],'pointer':a['pointer'],'value':values[a['value_index']]} for a in assignments]
    assert compact(reconstructed)==compact(field_nodes)
    hand_text=compact({'exact_hand_field_values':values})
    kind='deletion' if lid=='S06' else 'display' if lid.startswith('S') else L_kinds[lid]
    inv={
        'sheet_kind':'text','hand':hand_text,'element':'026.S.'+lid,'kind':kind,'position':d['location'],
        'first_words_or_objects':d['final'],'transcribed':'yes','main_approved':False,
        'selection_status':'Proposed exact root-selected source coverage; pending final record approval.',
        'hand_status':'Every exact hand value retains its original root, candidate, component or provenance scope in selected_hand_scope_map.',
        'decision_ids':[d['id']],'selected_group_ids':d['selected_group_ids'],'source_attachments':d['source_attachments'],
        'source_inventory_identity':'026.S.'+lid,'source_inventory_role':'root-selected locus proposal','page_order':i+1,
        'selected_hand_scope_map':{'values':values,'assignments':assignments},
        'original_reader_inventory_bindings_ref':ref(P+'inventory_bindings_v01.json','/reader_inventory_bindings'),
        'provenance':{'root_scope_ref':audit_by[lid]['root_authority']['decision_ref'],'selected_contract_ref':ref('scan026_source_selected_contract_v01.json',f'/loci/{contract_ix[lid]}'),'inventory_kind_is_reviewable_proposal':True},
    }
    inventory.append(inv)
    inventory_review.append({'record_inventory_index':i,'locus_id':lid,'element':inv['element'],'kind_proposal':kind,'position':inv['position'],'first_words_or_objects_exact_scalar_ref':ref(P+'scalar_authority_projection_v02.json',f'/rows/{i}/final'),'hand_exact_values':values,'hand_assignment_count':len(assignments),'hand_scope_map_ref':ref(P+'record_proposal_v01.json',f'/inventory/{i}/selected_hand_scope_map'),'source_contract_ref':inv['provenance']['selected_contract_ref']})

c_outcomes=read(P+'C_row_outcomes_v01.json')['rows'];c_source_rows=copy.deepcopy(scaffold['C_source_rows'])
record_by={x['source_locus_id']:x for x in record_rows}
for i,row in enumerate(c_source_rows):
    outcome=c_outcomes[i];cid=row['source_id'];assert cid==outcome['source_id']
    loci=outcome['source_binding']['loci']
    row['selected_outcome']=authority['all_C_parent_outcomes'][cid]
    row['decision_ids']=[record_by[lid]['id'] for lid in loci]
    row['root_outcome_mapping_ref']=ref(P+'C_row_outcomes_v01.json',f'/rows/{i}')
    for j,part in enumerate(row['source_parts']):
        exact=outcome['source_parts'][j]
        part_loci=loci
        if cid=='C026-R02':part_loci=[outcome['source_binding']['four_local_part_correspondences'][j]['locus']]
        part['selected_outcome']=exact['selected_outcome_exact']
        part['decision_ids']=[record_by[lid]['id'] for lid in part_loci]
        part['source_attachments']=[copy.deepcopy(span) for lid in part_loci for span in record_by[lid]['source_attachments']]
        part['root_authority']=exact['root_ref'];part['main_approved']=False
    if cid=='C026-R15':row['recurrence_outcomes']=outcome['recurrence_outcomes']
assert len(c_source_rows[1]['source_parts'])==4 and len(c_source_rows[14]['source_parts'])==1

doubts=[]
for d in record_rows:
    if d['remaining_doubt']:
        doubts.append({'id':'D026-'+d['source_locus_id'],'decision_id':d['id'],'location':d['location'],'reading':d['final'],'alternatives':d['alternatives'],'confidence':d['confidence'],'reason':d['qualification'],'selected_group_ids':d['selected_group_ids'],'source_attachments':d['source_attachments'],'root_crop_evidence':d['root_crop_evidence'],'main_approved':False,'selected_state_binding':d['selected_state_binding']})
assert len(doubts)==66

record={k:copy.deepcopy(scaffold[k]) for k in ['scan','folder','their_page','hua_has','filename']}
record.update(
    brief_version='scan026 source-only review proposal v01',main_adjudicated=False,main_approved=False,
    decisions=record_rows,doubts=doubts,inventory=inventory,C_source_rows=c_source_rows,
    selected_graphical_groups=[copy.deepcopy(v) for v in contract['source_group_registry'].values()],
    source_locus_coverage=copy.deepcopy(contract['loci']),
    abbreviations=copy.deepcopy(notes['abbreviations']),notes=notes['notes'],
    attributed_content_note={'text':notes['notes'],'root_authority':ref('scan026_root_notes_abbreviation_authority_v01.json','/notes'),'attributed_only':notes['attributed_only'],'mathematical_check':notes['mathematical_check'],'main_approved':False},
    root_selected_content_note={'text':notes['notes'],'root_authority':ref('scan026_root_notes_abbreviation_authority_v01.json','/notes'),'main_approved':False},
    check_events=copy.deepcopy(notes['check_events']),
    counts={'C':70,'H':82,'decision_loci':91,'remaining_doubt_loci':66,'inventory_elements':len(inventory),'check_events':0},
    count_status='Exact root scalar authority applied to this review proposal.',
    root_count_authorization=ref('scan026_root_scalar_authority_v01.json',''),
    pending_root_decision_ids=[],root_actions_pending=['Review and approve proposed public inventory kinds and exact scoped hand-field projection.','Attach and review the agreed-context inventory supplement.','Review final record fields and freeze the final source attachments.'],
    root_approval_status='Final record approval pending.',
    source_attachment_status='Exact accepted staged-source spans; root freeze/approval remains pending.',
    selected_draft=copy.deepcopy(contract['final_staged_source']),selected_source_contract=ref('scan026_source_selected_contract_v01.json',''),
    original_reader_inventory_bindings=read(P+'inventory_bindings_v01.json'),
    all_reader_raw_pool_ref=ref(P+'exact_raw_values_v01.json',''),
    complete_own_source_span_pool_ref=ref(P+'exact_own_source_spans_v01.json',''),
    provenance={'frozen_inputs':input_manifest,'root_scalar_authority':ref('scan026_root_scalar_authority_v01.json',''),'S06_exact_correction':ref(P+'S06_scope_correction_v01.json',''),'selected_contract':ref('scan026_source_selected_contract_v01.json','')},
)
assert sum(x['diff_C'] for x in record_rows)==70 and sum(x['diff_H'] for x in record_rows)==82
assert sum(x['marked_in_H']=='yes' for x in record_rows)==9
assert len(record['check_events'])==0 and record['notes']==notes['notes'] and compact(record['abbreviations'])==compact(notes['abbreviations'])
for source in input_manifest:assert sha((BASE/source['path']).read_bytes())==source['sha256']
record_manifest=save(P+'record_proposal_v01.json',record)
selected_manifest=save(P+'expanded_selected_models_v01.json',{'models':selected_models,'inverse_mappings':selected_inverse})
projection_manifest=save(P+'reader_projection_maps_v01.json',{'exact_excluded_report_field_names':excluded_report_fields,'rows':reader_projection_maps,'all_finite_field_rejoins_equal_original_ordered_values':True})
inventory_manifest=save(P+'inventory_review_v01.json',{'status':'Kind proposals and exact scoped hand-field projection await root; agreed contexts are being attached.','rows':inventory_review})
blueprint_manifest=save(P+'record_blueprint_v01.json',{
    'record':record_manifest,'source_inputs':input_manifest,'row_bindings':blueprint_rows,
    'public_reader_serializer':{'json_ensure_ascii':False,'json_separators':[',',':'],'field_order':['reader','exact_local_source','complete_original_source_groups','own_report_and_doubt_fields','original_inventory_scopes','original_complete_source_scope_records','complete_own_source_partition'],'report_projection':projection_manifest},
    'selected_alternatives_rule':'For a candidates array, serialize every complete candidate object independently with the compact JSON serializer, preserving its array order. For a scoped parent or component-projection model, serialize its complete expanded object once; its child arrays and complete parent states remain inside the object.',
    'evidence_rule':'Copy the exact root section body; L051 copies the exact agreement-supplement evidence. The qualification string is the exact compact JSON serialization of the root locus object.',
    'hand_scope_rule':'Traverse selected model dictionaries in original key order and arrays in index order. A key containing hand contributes its entire exact value; descendants of that contributed value stay inside it. Root hand is separately retained first when present. Pool only exactly identical typed values; preserve every ordered source scope/pointer assignment and its value index. Reverse expansion is checked against the full traversal.',
    'inventory_kind_proposals':{'S06':'deletion','all_other_S_loci':'display','L_loci':L_kinds},
    'selected_models':selected_manifest,'inventory_review':inventory_manifest,
    'root_review_claimed':False,'no_original_source_mutations':True,
})
print(json.dumps({'record':record_manifest,'blueprint':blueprint_manifest,'inventory':inventory_manifest,'reader_projection':projection_manifest},ensure_ascii=False))
