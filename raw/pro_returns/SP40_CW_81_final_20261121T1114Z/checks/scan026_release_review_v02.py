"""Bounded new-field review and exact forward/inverse replay of the frozen v02 record."""
from pathlib import Path
import collections
import contextlib
import copy
import hashlib
import io
import json
import runpy

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'out/checks'
P='scan026_release_'
def sha(b):return hashlib.sha256(b).hexdigest()
def compact(v):return json.dumps(v,ensure_ascii=False,separators=(',',':'))
def enc(v):return (json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode()
def read(n):return json.loads((OUT/n).read_text())
def save(n,v):
    assert n.startswith(P)
    b=enc(v);(OUT/n).write_bytes(b);return {'path':'out/checks/'+n,'sha256':sha(b),'bytes':len(b)}
def ptr(v,p):
    for k in p.split('/')[1:] if p else []:
        k=k.replace('~1','/').replace('~0','~');v=v[int(k)] if isinstance(v,list) else v[k]
    return v
def chunks(name,rows):
    groups=[];batch=[];size=0
    for row in rows:
        line=(compact(row)+'\n').encode()
        assert len(line)<=11000,(name,len(line))
        if batch and size+len(line)>11000:groups.append(batch);batch=[];size=0
        batch.append(line);size+=len(line)
    if batch:groups.append(batch)
    out=[]
    for i,batch in enumerate(groups,1):
        b=b''.join(batch);filename=P+name+f'_{i:02d}.jsonl';(OUT/filename).write_bytes(b)
        out.append({'path':'out/checks/'+filename,'sha256':sha(b),'bytes':len(b),'rows':len(batch)})
    return out

record_path=OUT/(P+'record_proposal_v02.json');record_bytes=record_path.read_bytes();record=json.loads(record_bytes)
assert enc(record)==record_bytes
blueprint=read(P+'record_blueprint_v02.json')
assert sha(record_bytes)==blueprint['record']['sha256']
captured={};original_write=Path.write_bytes
def memory_write(path,data):
    relative=str(path.resolve().relative_to(BASE))
    assert relative.startswith('out/checks/'+P)
    captured[relative]=bytes(data);return len(data)
try:
    Path.write_bytes=memory_write
    with contextlib.redirect_stdout(io.StringIO()):runpy.run_path(str(OUT/(P+'record_build_v02.py')),run_name='__main__')
finally:Path.write_bytes=original_write
replays=[]
for path,b in captured.items():
    assert (BASE/path).read_bytes()==b,path
    replays.append({'path':path,'sha256':sha(b),'bytes':len(b),'full_exact_byte_replay':True})

scalar=read(P+'scalar_authority_projection_v02.json');reverse_scalar=copy.deepcopy(scalar)
for i,old in enumerate(scalar['rows']):
    d=record['decisions'][i]
    reverse_scalar['rows'][i]={k:copy.deepcopy(d['root_final_exact'] if k=='final' else d[k]) for k in old}
assert enc(reverse_scalar)==(OUT/(P+'scalar_authority_projection_v02.json')).read_bytes()

raw_list=read(P+'exact_raw_values_v01.json')['records'];raw={r['record_id']:r for r in raw_list}
catalog=read('scan026_source_state_catalog_v01.json')
catalog_by={r['record_id']:r for r in catalog['raw_pool_value_bindings']}
record_raw_locations=collections.OrderedDict();all_raw_occurrences=0;reader_payloads={}
for i,d in enumerate(record['decisions']):
    for role,text in d['readers'].items():
        value=json.loads(text);assert compact(value)==text
        reader_payloads[i,role]=value
        for field in ['complete_original_source_groups','original_report_and_doubt_records','original_inventory_scopes','original_complete_source_scope_records','original_declared_crop_metadata']:
            for j,item in enumerate(value[field]):
                rid=item['raw_record'];exact=item['exact_original_fields']
                assert compact(exact)==compact(raw[rid]['value']),(d['source_locus_id'],role,rid)
                record_raw_locations.setdefault(rid,{'record_string_pointer':f'/decisions/{i}/readers/{role}','decoded_string_pointer':f'/{field}/{j}/exact_original_fields','decision_index':i,'reader':role,'value':exact})
                all_raw_occurrences+=1
        for item in value['own_report_and_doubt_fields']:
            rid=item['raw_record'];original=raw[rid]['value'];own=item['own_fields']
            assert all(compact(v)==compact(original[k]) for k,v in own.items())
            restored={k:(own[k] if k in own else original[k]) for k in original}
            assert compact(restored)==compact(original)

# Original JSON lexical spans are immutable source references. Each value span
# is checked against the full object recovered from the record string. Literal
# complement spans preserve all original JSON punctuation, whitespace and fields
# outside the selected source objects; concatenation restores whole source files.
source_segments=collections.defaultdict(list)
all_raw_inverse=[]
for rid,loc in record_raw_locations.items():
    original=catalog_by[rid]['raw_value_source'];path=original['path'];data=(BASE/path).read_bytes()
    a,b=original['utf8_byte_start'],original['utf8_byte_end'];lexeme=data[a:b]
    assert sha(lexeme)==original['body_sha256']
    assert compact(json.loads(lexeme))==compact(loc['value'])
    mapping={'record_id':rid,'record_string_pointer':loc['record_string_pointer'],'decoded_string_pointer':loc['decoded_string_pointer'],'original_source_path':path,'original_json_pointer':original['json_pointer'],'original_utf8_byte_start':a,'original_utf8_byte_end':b,'original_lexeme_sha256':sha(lexeme),'ordered_value_equal':True}
    all_raw_inverse.append(mapping);source_segments[path].append((a,b,rid,mapping))
file_inverse=[];lexical_partitions=[]
for path,items in source_segments.items():
    original=(BASE/path).read_bytes();ordered=sorted(items,key=lambda x:(x[0],-x[1]));chosen=[];end=-1
    for a,b,rid,mapping in ordered:
        if a>=end:chosen.append((a,b,rid,mapping));end=b
        else:
            assert any(pa<=a and b<=pb for pa,pb,_,_ in chosen),(path,rid,'crossing span')
    rebuilt=[];parts=[];cursor=0
    for a,b,rid,mapping in chosen:
        if cursor<a:
            rebuilt.append(original[cursor:a]);parts.append({'kind':'frozen_literal_complement','source_utf8_span':[cursor,a]})
        value=record_raw_locations[rid]['value'];lexeme=original[a:b]
        assert compact(json.loads(lexeme))==compact(value)
        rebuilt.append(lexeme);parts.append({'kind':'exact_original_value_lexeme','record_id':rid,'source_utf8_span':[a,b],'original_value_sha256':sha(lexeme)})
        cursor=b
    if cursor<len(original):rebuilt.append(original[cursor:]);parts.append({'kind':'frozen_literal_complement','source_utf8_span':[cursor,len(original)]})
    replay=b''.join(rebuilt);assert replay==original
    file_inverse.append({'path':path,'sha256':sha(replay),'bytes':len(replay),'full_original_byte_replay':True,'value_spans':len(chosen)})
    lexical_partitions.append({'path':path,'parts':parts})

source_pool=read(P+'exact_own_source_spans_v01.json');span_by={x['span_id']:x for x in source_pool['spans']};tex_inverse=[]
for role,parts in source_pool['reader_source_partitions'].items():
    reconstructed=''.join(span_by[x['span_id']]['span']['literal'] for x in parts).encode()
    path=f'out/readers/026/{role}/reading.tex';assert reconstructed==(BASE/path).read_bytes()
    tex_inverse.append({'reader':role,'path':path,'sha256':sha(reconstructed),'bytes':len(reconstructed),'full_original_byte_replay':True,'partition_count':len(parts)})

sep='\nComplete selected state objects, with original scopes and fields:\n'
for d in record['decisions']:
    root_part,states=d['final'].split(sep,1)
    assert root_part==d['root_final_exact'] and compact(json.loads(states))==compact(d['root_selected_state_model'])
    model=d['root_selected_state_model']
    if 'candidates' in model:assert compact([json.loads(s) for s in d['alternatives']])==compact(model['candidates'])
    else:assert compact(json.loads(d['alternatives'][0]))==compact(model)
remaining=[d for d in record['decisions'] if d['remaining_doubt']]
assert len(remaining)==len(record['doubts'])==66
for d,q in zip(remaining,record['doubts']):
    assert q['decision_id']==d['id'] and q['reading']==d['final'] and compact(q['alternatives'])==compact(d['alternatives'])

def hand_factors(assignments,context=False):
    groups=collections.OrderedDict()
    for a in assignments:
        if context:
            scope=a['reader'];prefix=a['raw_record'];suffix=a['field_pointer']
        else:
            scope=a['source_scope'];pointer=a['pointer'];bits=pointer.split('/')
            split=None
            for j in range(1,len(bits)-1):
                if bits[j] in ['candidates','complete_parent_candidates','exact_original_candidates'] and bits[j+1].isdigit():split=j+2
            prefix='/'.join(bits[:split]) if split is not None else ''
            suffix=('/'+'/'.join(bits[split:])) if split is not None else pointer
        groups.setdefault((scope,a['value_index'],suffix),[]).append(prefix)
    factors=collections.OrderedDict()
    for (scope,index,suffix),prefixes in groups.items():factors.setdefault((scope,index,tuple(prefixes)),[]).append(suffix)
    result=[{'scope':scope,'value_index':index,'prefixes':list(prefixes),'suffixes':suffixes} for (scope,index,prefixes),suffixes in factors.items()]
    expanded=[(x['scope'],x['value_index'],p+s) for x in result for p in x['prefixes'] for s in x['suffixes']]
    expected=[(a['reader'],a['value_index'],a['raw_record']+a['field_pointer']) if context else (a['source_scope'],a['value_index'],a['pointer']) for a in assignments]
    assert len(expanded)==len(expected) and collections.Counter(expanded)==collections.Counter(expected)
    return result

hand_review=[]
for i,inv in enumerate(record['inventory']):
    context='original_inventory_hand_scope_map' in inv
    field='original_inventory_hand_scope_map' if context else 'selected_hand_scope_map';scope=inv[field]
    hand_review.append({'inventory_index':i,'element':inv['element'],'field':field,'exact_values':scope['values']})
    for j,product in enumerate(hand_factors(scope['assignments'],context)):
        # Only the finite prefix set is split; the exact product remains explicit.
        for start in range(0,len(product['prefixes']),30):
            part=dict(product);part['prefixes']=product['prefixes'][start:start+30]
            hand_review.append({'inventory_index':i,'product_index':j,'prefix_start':start,'exact_path_product':part})
hand_files=chunks('hand_scope_review_v02',hand_review)

inventory_files=chunks('inventory_review_v02',read(P+'inventory_review_v02.json')['rows'])
row_files=chunks('record_row_bindings_v02',blueprint['row_bindings'])
blueprint_definitions={k:v for k,v in blueprint.items() if k!='row_bindings'}
definition_file=save(P+'record_constructor_definitions_v02.json',blueprint_definitions)
source=(OUT/(P+'record_build_v02.py')).read_bytes();source_lines=source.splitlines(keepends=True)
code_files=[];current=[];size=0;first=1
for i,line in enumerate(source_lines,1):
    if current and size+len(line)>11000:
        b=b''.join(current);name=P+f'constructor_v02_{len(code_files)+1:02d}.txt';(OUT/name).write_bytes(b);code_files.append({'path':'out/checks/'+name,'first_line':first,'last_line':i-1,'bytes':len(b),'sha256':sha(b)});current=[];size=0;first=i
    current.append(line);size+=len(line)
if current:
    b=b''.join(current);name=P+f'constructor_v02_{len(code_files)+1:02d}.txt';(OUT/name).write_bytes(b);code_files.append({'path':'out/checks/'+name,'first_line':first,'last_line':len(source_lines),'bytes':len(b),'sha256':sha(b)})
assert b''.join((BASE/x['path']).read_bytes() for x in code_files)==source

top_new_fields={k:v for k,v in record.items() if k not in ['decisions','doubts','inventory','C_source_rows','selected_graphical_groups','source_locus_coverage','abbreviations','notes','attributed_content_note','root_selected_content_note','original_reader_inventory_bindings','complete_selected_source_contexts','provenance']}
constant_inventory_fields={}
for i,inv in enumerate(record['inventory']):
    for k in ['sheet_kind','transcribed','main_approved','selection_status','hand_status','source_inventory_role']:
        value=inv[k];key=(k,compact(value));constant_inventory_fields.setdefault(key,{'field':k,'exact_value':value,'inventory_indices':[]})['inventory_indices'].append(i)
new_fields_file=save(P+'new_public_field_constants_v02.json',{'top_level_exact_fields':top_new_fields,'inventory_exact_constant_fields':list(constant_inventory_fields.values()),'decision_field_order':list(record['decisions'][0]),'locus_inventory_field_order':list(record['inventory'][0]),'context_inventory_field_order':list(record['inventory'][-1]),'doubt_field_order':list(record['doubts'][0]),'final_expansion_separator_exact':sep})

inverse_manifest=save(P+'raw_object_inverse_mappings_v02.json',{'raw_objects':all_raw_inverse,'full_original_file_partitions':lexical_partitions})
proof=save(P+'record_replay_v02.json',{
    'record_path':'out/checks/'+P+'record_proposal_v02.json','record_sha256':sha(record_bytes),'record_bytes':len(record_bytes),
    'constructor_replayed_in_memory_without_file_writes':True,'all_constructor_outputs_exact_bytes':replays,
    'inverse_complete_scalar_projection_exact_bytes':True,'scalar_projection_sha256':sha(enc(reverse_scalar)),
    'complete_public_reader_raw_object_occurrences':all_raw_occurrences,'distinct_exact_raw_objects_recovered_from_public_reader_fields':len(record_raw_locations),
    'all_full_raw_objects_preserve_key_order_and_typed_values':True,'full_original_JSON_source_byte_inverse':file_inverse,'full_original_reader_TeX_byte_inverse':tex_inverse,
    'raw_inverse_mappings':inverse_manifest,
    'all_final_reading_strings_inverse_to_exact_root_text_and_complete_state_models':True,
    'all_doubt_readings_match_exact_66_root_flags_and_complete_decision_fields':True,
    'all_hand_scope_products_expand_to_exact_ordered_assignment_multisets':True,
    'counts':record['counts'],'H_marked_rows':sum(x['marked_in_H']=='yes' for x in record['decisions']),
    'C_parent_rows':len(record['C_source_rows']),'R02_actual_parts':len(record['C_source_rows'][1]['source_parts']),'R15_actual_parts':len(record['C_source_rows'][14]['source_parts']),'R15_occurrences':len(record['C_source_rows'][14]['recurrence_outcomes']),
    'source_files_unchanged':all(sha((BASE/x['path']).read_bytes())==x['sha256'] for x in blueprint['source_inputs']),
    'root_review_claimed':False,
})
index=save(P+'final_review_index_v02.json',{
    'scope':'Complete reviewable final-record proposal. All unchanged full source objects retain exact frozen references; public string constructors and finite inverse mappings preserve every candidate field and original scope.',
    'record':blueprint['record'],'constructor':{'path':'out/checks/'+P+'record_build_v02.py','sha256':sha(source),'bytes':len(source)},
    'constructor_source_chunks':code_files,'constructor_definitions':definition_file,'new_public_constants':new_fields_file,
    'row_binding_chunks':row_files,'inventory_chunks':inventory_files,'hand_scope_chunks':hand_files,
    'hand_product_rule':'For each product use every prefix + every suffix under its stated scope and value index. Context products concatenate raw record id and original field pointer. All products reproduce the original assignment multiset exactly.',
    'record_replay':proof,'already_root_reviewed_inputs_retained':['91 scalar authority rows','S06 complete witness correction','91 selected-state contract bindings','15 original C parent outcomes','15 agreed contexts and complete source partition','all original own-reader raw fields'],
    'counts':record['counts'],'pending':'Root review of constructors and all public inventory fields, then final approval. No proposal is applied by this package.',
    'root_review_claimed':False,
})
print(json.dumps({'index':index,'constructor_chunks':len(code_files),'row_binding_chunks':len(row_files),'inventory_chunks':len(inventory_files),'hand_scope_chunks':len(hand_files),'proof':proof,'raw_objects':len(record_raw_locations)},ensure_ascii=False))
