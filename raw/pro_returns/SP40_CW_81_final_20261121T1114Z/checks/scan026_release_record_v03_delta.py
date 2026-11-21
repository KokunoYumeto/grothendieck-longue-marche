"""Finite root-authorized reporting/metadata corrections; frozen v02 stays unchanged."""
import copy
import hashlib
import json
import re
from pathlib import Path

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'out/checks'
P='scan026_release_'
def sha(b):return hashlib.sha256(b).hexdigest()
def compact(v):return json.dumps(v,ensure_ascii=False,separators=(',',':'))
def enc(v):return (json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode()
def save(name,value):
    assert name.startswith(P)
    b=enc(value);(OUT/name).write_bytes(b);return {'path':'out/checks/'+name,'sha256':sha(b),'bytes':len(b)}
def chunks(name,rows):
    batches=[];batch=[];size=0
    for row in rows:
        b=(compact(row)+'\n').encode();assert len(b)<=11000
        if batch and size+len(b)>11000:batches.append(batch);batch=[];size=0
        batch.append(b);size+=len(b)
    if batch:batches.append(batch)
    result=[]
    for i,batch in enumerate(batches,1):
        b=b''.join(batch);n=P+name+f'_{i:02d}.jsonl';(OUT/n).write_bytes(b)
        result.append({'path':'out/checks/'+n,'sha256':sha(b),'bytes':len(b),'rows':len(batch)})
    return result

before_path=OUT/(P+'record_proposal_v02.json');before_bytes=before_path.read_bytes();before=json.loads(before_bytes)
assert sha(before_bytes)=='098043e22a7a7edb2e9e00280b472ac5f16a6f0858fa0fdcf362d8a463cf5668'
assert enc(before)==before_bytes
after=copy.deepcopy(before)
scaffold=json.loads((OUT/'scan026_source_record_scaffold_v01.json').read_text())
S_context=copy.deepcopy(scaffold['S_source_only_context'])
assert compact(S_context)==compact(json.loads((OUT/'scan026_S_scope.json').read_text()))
S_path=BASE/S_context['source'];S_bytes=S_path.read_bytes();S_text=S_bytes.decode()
assert sha(S_bytes)==S_context['source_sha256']
lines=S_text.splitlines(keepends=True);assert len(lines)==8 and all(x.endswith('\n') for x in lines)
header=lines[0][:-1].split('\t');assert len(header)==len(set(header))==8
S_rows=[];S_bindings=[];cursor=len(lines[0])
for i,line in enumerate(lines[1:]):
    fields=line[:-1].split('\t');assert len(fields)==len(header)
    row=dict(zip(header,fields));S_rows.append(row)
    assert row['id']==S_context['row_scopes'][i]['id']
    for key in ['id','where','kind']:assert row[key]==S_context['row_scopes'][i][key]
    end=cursor+len(line)
    S_bindings.append({'source_id':row['id'],'record_pointer':f'/S_source_rows/{i}','source_line':i+2,
                       'char_start':cursor,'char_end':end,'utf8_byte_start':len(S_text[:cursor].encode()),'utf8_byte_end':len(S_text[:end].encode()),
                       'literal':line,'literal_sha256':sha(line.encode())})
    cursor=end
S_inverse=(lines[0]+''.join('\t'.join(row[k] for k in header)+'\n' for row in S_rows)).encode()
assert S_inverse==S_bytes
S_provenance={'source_path':S_context['source'],'source_sha256':sha(S_bytes),'source_bytes':len(S_bytes),
              'original_header_fields':header,'original_header_literal':lines[0],'rows':S_bindings,
              'source_scope_context_ref':{'path':'out/checks/scan026_source_record_scaffold_v01.json','json_pointer':'/S_source_only_context'},
              'full_original_TSV_forward_inverse_exact_bytes':True}
for name,value in [('S_source_only_context',S_context),('S_source_rows',S_rows),('S_source_provenance',S_provenance)]:
    assert name not in after;after[name]=value

inventory=before['inventory'];assert len(inventory)==106
def ordering_key(i):
    row=inventory[i];spans=row['source_attachments'];assert spans
    assert all(s['path']=='checks/scan026_final_draft.tex' for s in spans)
    start=min(s['char_start'] for s in spans);end=max(s['char_end'] for s in spans)
    context_rank=0 if 'original_inventory_hand_scope_map' in row else 1
    return start,-end,context_rank,i
new_to_old=sorted(range(len(inventory)),key=ordering_key)
old_to_new={old:new for new,old in enumerate(new_to_old)}
assert set(old_to_new)==set(range(106)) and sorted(new_to_old)==list(range(106))
permutation=[]
for new,old in enumerate(new_to_old):
    k=ordering_key(old)
    permutation.append({'element':inventory[old]['element'],'old_index':old,'new_index':new,'old_page_order':inventory[old]['page_order'],'new_page_order':new+1,
                        'anchor_char_start':k[0],'enclosing_end_char':-k[1],'context_tie_rank':k[2],
                        'original_array_pointer':f'/inventory/{old}','new_array_pointer':f'/inventory/{new}'})
permutation_file=save(P+'inventory_permutation_v03.json',{
    'source_anchor_path':'checks/scan026_final_draft.tex','source_anchor_sha256':sha((OUT/'scan026_final_draft.tex').read_bytes()),
    'sort_key':['minimum selected-source char_start','negative maximum selected-source char_end','context 0 / locus 1','original v02 inventory index'],
    'sort_scope':'Exact accepted selected-source order; enclosing context precedes a child when the start anchors coincide. No image coordinate is reinterpreted.',
    'old_index_to_new_index':[old_to_new[i] for i in range(106)],'new_index_to_old_index':new_to_old,'rows':permutation})
after['inventory']=[copy.deepcopy(inventory[i]) for i in new_to_old]
pointer_rebases=[];hand_constructors=[];kind_changes=[]
for new,old in enumerate(new_to_old):
    row=after['inventory'][new];original=inventory[old];element=row['element']
    row['page_order']=new+1
    if 'selected_child_hand_scope_refs' in row:
        for j,binding in enumerate(row['selected_child_hand_scope_refs']):
            old_pointer=binding['record_inventory_pointer'];m=re.fullmatch(r'/inventory/(\d+)/selected_hand_scope_map',old_pointer);assert m
            old_target=int(m.group(1));new_target=old_to_new[old_target]
            assert inventory[old_target]['element']=='026.S.'+binding['locus_id']
            new_pointer=f'/inventory/{new_target}/selected_hand_scope_map';binding['record_inventory_pointer']=new_pointer
            pointer_rebases.append({'element':element,'old_index':old,'new_index':new,'child_ref_index':j,'before':old_pointer,'after':new_pointer})
    assert 'public_hand_v02_exact' not in row['provenance']
    row['provenance']['public_hand_v02_exact']=original['hand']
    if 'selected_hand_scope_map' in row:
        hand_value=copy.deepcopy(row['selected_hand_scope_map'])
        constructor={'kind':'compact_exact_selected_hand_scope_map','frozen_v02_map_pointer':f'/inventory/{old}/selected_hand_scope_map'}
    else:
        hand_value={'original_inventory':copy.deepcopy(row['original_inventory_hand_scope_map']),
                    'selected_child_hand_scope_refs':copy.deepcopy(row['selected_child_hand_scope_refs'])}
        constructor={'kind':'compact_original_inventory_and_rebased_selected_child_refs','frozen_v02_original_map_pointer':f'/inventory/{old}/original_inventory_hand_scope_map',
                     'rebased_current_child_refs_pointer':f'/inventory/{new}/selected_child_hand_scope_refs',
                     'ordered_keys':['original_inventory','selected_child_hand_scope_refs']}
    row['hand']=compact(hand_value);assert compact(json.loads(row['hand']))==compact(hand_value)
    hand_constructors.append({'element':element,'old_index':old,'new_index':new,'public_hand_before_exact_pointer':f'/inventory/{old}/hand',
                              'preserved_verbatim_provenance_pointer':f'/inventory/{new}/provenance/public_hand_v02_exact','constructor':constructor})
    if element=='026.S.S08':
        assert row['kind']=='display';row['kind']='deletion'
        kind_changes.append({'element':element,'old_index':old,'new_index':new,'before':'display','after':'deletion',
                             'authority':'Root inventory review: S08 remains inside the fixed deleted les … connexes group in section 11; selected parent scope L011.',
                             'root_decision_ref':{'path':'out/checks/scan026_root_decisions.json','json_pointer':'/decisions/10/locus_decisions/S08'}})
assert len(kind_changes)==1
after['inventory_order_provenance']={'frozen_v02_record':{'path':'out/checks/'+P+'record_proposal_v02.json','sha256':sha(before_bytes),'json_pointer':'/inventory'},
                                     'permutation':permutation_file,'raw_reader_arrays_and_original_source_pointers_preserved':True}

brief_path='out/briefs/brief_v24_scan026.md';audit_path='out/checks/scan026_root_crop_audit.json'
brief_bytes=(BASE/brief_path).read_bytes();audit_bytes=(BASE/audit_path).read_bytes();crop_audit=json.loads(audit_bytes)
assert crop_audit['closed_utc'] and crop_audit['total_distinct']==27 and crop_audit['created_by_root_count']==4 and crop_audit['reused_reader_crop_count']==23
assert crop_audit['whole_or_halves_seen_by_root'] is False and crop_audit['physical_loci_total']==91
brief_version='v24 (brief_v24_scan026.md)'
workflow_note='Three fresh independent readers returned this page under brief_v24_scan026.md. Root read all three complete returns and all three pairwise TeX diffs before the first root crop. Root successfully viewed 27 distinct crop paths once each: 4 root-created and 23 reused (A 10, B 9, C 4). Two failed unseen image deliveries were recovered once from the same existing files. No whole scan or supplied half was viewed by root. The final 91-locus contract includes the separately recorded L052 fleck; source-only helpers made no ink decisions.'
metadata_binding=save(P+'workflow_metadata_binding_v03.json',{
    'author':'/root','brief_version_exact':brief_version,'workflow_note_exact':workflow_note,
    'brief':{'path':brief_path,'sha256':sha(brief_bytes),'bytes':len(brief_bytes)},
    'closed_root_crop_audit':{'path':audit_path,'sha256':sha(audit_bytes),'bytes':len(audit_bytes),'closed_utc':crop_audit['closed_utc']},
    'brief_version_before_exact':before['brief_version'],
    'original_v02_workflow_note_present':'workflow_note' in before,
})
assert 'workflow_note' not in after and 'workflow_metadata_authority' not in after['provenance']
after['brief_version']=brief_version;after['workflow_note']=workflow_note
after['provenance']['workflow_metadata_authority']=metadata_binding
metadata_changes=[{'field':'brief_version','before':before['brief_version'],'after':brief_version},
                  {'field':'workflow_note','before_absent':True,'after':workflow_note},
                  {'field':'/provenance/workflow_metadata_authority','before_absent':True,'after':metadata_binding}]

# Exact inverse restores original pointer strings, public hand, kind and ordering.
inverse=copy.deepcopy(after)
for change in pointer_rebases:
    inverse['inventory'][change['new_index']]['selected_child_hand_scope_refs'][change['child_ref_index']]['record_inventory_pointer']=change['before']
for new,old in enumerate(new_to_old):
    row=inverse['inventory'][new]
    row['hand']=row['provenance'].pop('public_hand_v02_exact');row['page_order']=inventory[old]['page_order']
for change in kind_changes:inverse['inventory'][change['new_index']]['kind']=change['before']
inverse['inventory']=[inverse['inventory'][old_to_new[old]] for old in range(106)]
for name in ['S_source_only_context','S_source_rows','S_source_provenance','inventory_order_provenance']:del inverse[name]
inverse['brief_version']=before['brief_version'];del inverse['workflow_note'];del inverse['provenance']['workflow_metadata_authority']
assert enc(inverse)==before_bytes
for key in before:
    if key not in ['inventory','brief_version','provenance']:assert compact(after[key])==compact(before[key]),key
restored_provenance=copy.deepcopy(after['provenance']);del restored_provenance['workflow_metadata_authority']
assert compact(restored_provenance)==compact(before['provenance'])
assert before_path.read_bytes()==before_bytes
after_file=save(P+'record_proposal_v03.json',after)
S_append_file=save(P+'S_source_append_v03.json',{'S_source_only_context':S_context,'S_source_rows':S_rows,'S_source_provenance':S_provenance})
delta_file=save(P+'record_v02_to_v03_delta.json',{
    'before':{'path':'out/checks/'+P+'record_proposal_v02.json','sha256':sha(before_bytes),'bytes':len(before_bytes)},'after':after_file,
    'only_changes':['Append exact original S scope and all seven complete original source rows with lexical provenance.','Permute the 106 public inventory entries by the exact selected-source ordering key; update page_order and only current-record child-hand pointers.','Serialize each public hand with its full original/selected scope map; preserve the complete v02 hand verbatim in provenance.','Change the S08 inventory kind from display to deletion under root authority.','Set the exact root-supplied brief_version and workflow_note and bind them to the existing brief and closed root crop audit.'],
    'S_append':S_append_file,'inventory_permutation':permutation_file,'pointer_rebases':pointer_rebases,'hand_field_constructors':hand_constructors,'kind_changes':kind_changes,
    'metadata_changes':metadata_changes,'metadata_binding':metadata_binding,
    'public_hand_serializer':{'ensure_ascii':False,'separators':[',',':']},
    'new_inventory_provenance_key':'public_hand_v02_exact','new_root_inventory_order_provenance':after['inventory_order_provenance'],
    'all_other_v02_values_exactly_unchanged':True,'full_inverse_original_record_bytes':True,'full_original_S_TSV_bytes_recovered':True,
    'frozen_v02_unchanged':True,'counts_unchanged':after['counts'],'root_review_claimed':False,
})
permutation_chunks=chunks('inventory_order_review_v03',permutation)
pointer_chunks=chunks('inventory_pointer_review_v03',pointer_rebases)
hand_chunks=chunks('public_hand_constructor_review_v03',hand_constructors)
S_chunks=chunks('S_source_review_v03',[{'scope_context_exact':S_context,'header':header}]+[{'raw_row_exact':r,'binding':b} for r,b in zip(S_rows,S_bindings)])
proof=save(P+'record_v03_replay.json',{'before_sha256':sha(before_bytes),'after_sha256':after_file['sha256'],'full_forward_after_bytes':after_file['bytes'],'full_inverse_v02_byte_equality':True,
    'permutation_bijection':True,'record_field_key_order_restored_on_inverse':True,'S_context_exact_scaffold_object':True,'S_rows':len(S_rows),'S_source_inverse_sha256':sha(S_inverse),
    'public_hand_constructors':len(hand_constructors),'current_child_hand_pointer_rebases':len(pointer_rebases),'kind_changes':kind_changes,
    'metadata_changes':metadata_changes,'all_other_v02_fields_unchanged':True,'counts':after['counts'],'check_events_exact_unchanged':after['check_events']==before['check_events'],
    'all_frozen_source_bytes_unchanged':S_path.read_bytes()==S_bytes and before_path.read_bytes()==before_bytes,'root_review_claimed':False})
index=save(P+'final_review_index_v03.json',{'record':after_file,'delta':delta_file,'constructor':{'path':'out/checks/'+P+'record_v03_delta.py','sha256':sha(Path(__file__).read_bytes())},
    'S_scope_chunks':S_chunks,'inventory_order_chunks':permutation_chunks,'current_pointer_rebase_chunks':pointer_chunks,'public_hand_constructor_chunks':hand_chunks,
    'kind_changes':kind_changes,'metadata_binding':metadata_binding,'metadata_changes':metadata_changes,'replay':proof,'frozen_v02_record_preserved':True,'root_review_claimed':False})
print(json.dumps({'index':index,'record':after_file,'delta':delta_file,'replay':proof,'chunks':{'S':len(S_chunks),'order':len(permutation_chunks),'pointers':len(pointer_chunks),'hands':len(hand_chunks)}},ensure_ascii=False))
