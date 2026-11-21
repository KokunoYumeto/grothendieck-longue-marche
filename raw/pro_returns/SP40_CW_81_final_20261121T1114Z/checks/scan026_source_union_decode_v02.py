"""Independent source-only decoder. It never writes the v01 artefacts."""
from pathlib import Path
from collections import OrderedDict
import copy
import hashlib
import json
import re

BASE=Path('/workspace/scratch/94548b74fbe0')
OUT=BASE/'out/checks'
digest=lambda b:hashlib.sha256(b).hexdigest()
packed=lambda v:json.dumps(v,ensure_ascii=False,separators=(',',':'))
pretty=lambda v:(json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode()
def read(name):return json.loads((OUT/name).read_bytes())
def save(name,value):
 b=pretty(value);(OUT/name).write_bytes(b)
 return {'path':str(OUT/name),'sha256':digest(b),'bytes':len(b)}

registry=read('scan026_source_union_sources_v01.json')
original={};source_bytes={}
for key,m in registry.items():
 b=(BASE/m['path']).read_bytes()
 assert digest(b)==m['sha256'] and len(b)==m['bytes'],key
 source_bytes[key]=b
 original[key]=json.loads(b) if m['path'].endswith('.json') else b.decode()
def pointer(key,path):
 v=original[key]
 for part in path.split('/')[1:]:
  part=part.replace('~1','/').replace('~0','~')
  v=v[int(part)] if isinstance(v,list) else v[part]
 return v
def deref(ref):return pointer(ref['source'],ref['json_pointer'])

pool=read('scan026_source_union_state_pool_v01.json')
decoded={};directory={}
for row in pool:
 rid=row['record_id'];assert rid not in decoded
 raw=deref(row['raw_ref'])
 if 'ordered_fields' in row:
  fields=row['ordered_fields'];assert len({f['key'] for f in fields})==len(fields)
  value=OrderedDict((f['key'],copy.deepcopy(f['value']) if 'value' in f else copy.deepcopy(deref(f['exact_value_ref']))) for f in fields)
 else:value=copy.deepcopy(row['value'])
 assert packed(value)==packed(raw),rid
 decoded[rid]=value
 directory[rid]={'raw_ref':row['raw_ref'],'raw_id':next((raw[k] for k in ['id','source_id','graphic_id','element','source_group'] if isinstance(raw,dict) and k in raw),None)}

base_path=OUT/'scan026_source_union_v01.json'
base_bytes=base_path.read_bytes();union=json.loads(base_bytes)
replay=read('scan026_source_union_replay_v01.json')
all_chunks=[]
for item in replay['review_files']:
 b=(BASE/item['path']).read_bytes();assert digest(b)==item['sha256'] and len(b)==item['bytes']
 lines=[json.loads(line) for line in b.decode().splitlines()]
 assert len(lines)==item['rows'];all_chunks.extend(lines)
assert packed(all_chunks)==packed(union)
assert pretty(union)==base_bytes

span_count=0
for row in union:
 for w,scopes in row['reader_sources'].items():
  for category,values in scopes.items():
   if category=='local_source_spans':
    for s in values:
     text=original[s['source']];literal=text[s['start_char']:s['end_char_exclusive']]
     assert digest(literal.encode())==s['sha256']
     assert source_bytes[s['source']][s['start_utf8_byte']:s['end_utf8_byte_exclusive']]==literal.encode()
     if 'literal' in s:assert s['literal']==literal
     span_count+=1
   else:
    for rid in values:assert rid in decoded,(row['locus_id'],w,category,rid)
 for s in row['witness_source_spans']:
  text=original[s['source']];literal=text[s['start_char']:s['end_char_exclusive']]
  assert s['literal']==literal and digest(literal.encode())==s['sha256']
  assert source_bytes[s['source']][s['start_utf8_byte']:s['end_utf8_byte_exclusive']]==literal.encode()
  span_count+=1

subtargets=read('scan026_source_union_C_rows_v01.json')
assert len(subtargets)==15
assert [x['source_row_id'] for x in subtargets]==[x['source_id'] for x in original['C.doubts']['canonical_doubt_rows']]
parts=subtargets[1]['four_local_part_correspondences']
expected=[('S04',0,0,0),('S05',2,2,1),('S05',1,1,2),('S07',3,3,3)]
for item,(loc,ai,bi,ci) in zip(parts,expected):
 assert item['locus']==loc and (item['A_part_index'],item['B_part_index'],item['C_part_index'])==(ai,bi,ci)
 for w,index,key in [('A',ai,'C_doubt_source_rows'),('B',bi,'C_uncertainty_source_rows'),('C',ci,'C_uncertainty_rows')]:
  rid=item['raw_reader_part_records'][w]
  assert packed(decoded[rid])==packed(original[w+'.report'][key][1]['local_parts'][index])
rings=subtargets[14]['eight_local_recurrences']
assert [x['locus'] for x in rings]==['S05','S08','S09','S10','S11','S12','S13','S14']
assert len(parts)==4 and len(rings)==8
markers=read('scan026_source_union_H_marker_bindings_v01.json')
raw_markers=[m for key in ['uncertainty_macros','editorial_supplies','notes','marginal_drawing_source_descriptions'] for m in original['H.markers'][key]]
assert len(markers)==len(raw_markers)==19
assert [x['source_id'] for x in markers]==[x['source_id'] for x in raw_markers]
for item,raw in zip(markers,raw_markers):assert packed(decoded[item['raw_record']])==packed(raw)

# Parent requested precisely these two observational replacements. The raw
# states, mappings, paths, spans and v01 bytes are kept untouched.
new_observation='A uses an ordinary Sigma label token within its complete diagram source. B draws the label through the exact local head, body and sign paths cited here. C has a separate literal group with its own detached-head states. Catalogue Sigma ordinals 15/16 do not fabricate A/B local group ids.'
operations=[];forward=copy.deepcopy(union)
for loc in ['S15','S16']:
 i=next(i for i,x in enumerate(union) if x['locus_id']==loc)
 old=union[i]['source_observations'];assert len(old)==1
 operations.append({'locus_id':loc,'json_pointer':f'/{i}/source_observations/0','old':old[0],'new':new_observation})
 forward[i]['source_observations'][0]=new_observation
inverse=copy.deepcopy(forward)
for op in reversed(operations):
 _,index,field,position=op['json_pointer'].split('/')
 assert inverse[int(index)][field][int(position)]==op['new']
 inverse[int(index)][field][int(position)]=op['old']
assert pretty(inverse)==base_bytes
delta={'scope':'Two source_observations strings only; no v01 file was rewritten. No other field changes.','base_path':str(base_path),'base_sha256':digest(base_bytes),'operations':operations,'forward_logical_json_sha256':digest(pretty(forward)),'inverse_exact_base_bytes':True,'forward_then_inverse_equal':True}
delta_artifact=save('scan026_source_union_S15S16_delta_v02.json',delta)

coordinate_requests={
 'L002':{'A':[('differences',16)],'B':[('differences',16)],'C':[('differences',3)]},
 'L004':{'A':[('inventory',0)],'B':[('inventory',2)],'C':[('inventory',2)]},
 'L051':{'A':[('inventory',77)],'B':[('inventory',93)],'C':[('inventory',86)]}}
facts=[]
for loc,readers in coordinate_requests.items():
 item={'locus_id':loc,'scope':'Exact existing reader metadata only; no image inspected and no fresh crop chosen.','readers':{}}
 for w,refs in readers.items():
  item['readers'][w]=[]
  for section,index in refs:
   ptr=f'/{section}/{index}';raw=original[w+'.report'][section][index]
   fields=OrderedDict((k,v) for k,v in raw.items() if k in ['id','location','hand','element','kind','position','first_words_or_objects','bbox','readers_crop','evidence_view','provenance','source_C_inventory_identity','source_C_inventory_hand'])
   assert all(packed(fields[k])==packed(raw[k]) for k in fields)
   item['readers'][w].append({'raw_ref':{'source':w+'.report','json_pointer':ptr},'literal_fields_in_raw_order':fields})
 if loc=='L004':item['limitation']='B supplies the enclosing family/naming-line box, A a broad top-to-middle text box, and C a textual position with no bbox; no dedicated first-quote box is supplied by these rows.'
 if loc=='L051':item['limitation']='All three quoted archive inventory hand fields say undetermined hand. C gives no numeric bbox in this archive inventory row.'
 facts.append(item)
facts_artifact=save('scan026_source_union_requested_coordinates_v02.json',facts)

proof={
 'source_only':True,'frozen_text_files_hashed':len(registry),'pool_records_exactly_reconstructed_with_original_key_order':len(pool),
 'union_rows':len(union),'review_chunks':len(replay['review_files']),'chunk_parse_concatenation_exact_values_and_key_order':True,
 'local_and_witness_spans_rechecked':span_count,'C_parents':15,'R02_explicit_parts':4,'R15_local_recurrences':8,'H_marker_scope_records':19,
 'two_string_delta_forward_inverse':True,'base_union_sha256':digest(base_bytes),'artifacts':[delta_artifact,facts_artifact],
 'input_bytes_unchanged':all((BASE/registry[key]['path']).read_bytes()==b for key,b in source_bytes.items()) and base_path.read_bytes()==base_bytes,
 'images_opened':0,'root_crop_choices':0,'root_ink_choices':0,'root_review_claimed':False}
save('scan026_source_union_decoder_proof_v02.json',proof)
save('scan026_source_union_record_directory_v02.json',directory)
print(json.dumps(proof,ensure_ascii=False,indent=2))
