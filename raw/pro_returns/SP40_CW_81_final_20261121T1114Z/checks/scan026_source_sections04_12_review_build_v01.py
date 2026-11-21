"""Bounded exact review of the newly mapped candidate values, with inverse."""
from pathlib import Path
import copy,hashlib,json
O=Path('/workspace/scratch/94548b74fbe0/out/checks');B=O.parents[1]
data=json.loads((O/'scan026_source_sections04_12_state_maps_v01.json').read_bytes())
C=json.loads((B/'out/readers/026/C/source_map.json').read_bytes())
rows=[];decoded={}
for i,item in enumerate(data):
 group=item['group']
 if 'ordered_exact_changes' in item:
  g=next(g for g in C['groups'] if g['id']==item['source_candidate_group'])
  values=[]
  for change in item['ordered_exact_changes']:
   j=change['candidate_index'];original=g['candidate_states'][j]
   value=copy.deepcopy(original);assert value['complete_reading']==change['old_complete_reading'];value['complete_reading']=change['new_complete_reading']
   assert value==item['exact_selected_candidate_states'][j]
   inverse=copy.deepcopy(value);inverse['complete_reading']=change['old_complete_reading'];assert inverse==original
   rows.append({'kind':'one exact candidate-reading field map','group':group,'candidate_index':j,
    'frozen_original_source':'out/readers/026/C/source_map.json','original_json_pointer':item['source_candidate_pointer']+'/'+str(j),
    'exact_mapping':change,'other_fields':'Every other original field and its order are retained through the cited whole object; finite forward/inverse equality checked.'})
   values.append(value)
  decoded[group]=values
 elif 'permutation_new_index_to_old_index' in item:
  rows.append({'kind':'exact complete-state permutation','group':group,'permutation_new_index_to_old_index':item['permutation_new_index_to_old_index'],'original_complete_objects':item['exact_original_objects'],'selected_complete_objects':item['exact_selected_objects']})
  values=[copy.deepcopy(item['exact_original_objects'][j]) for j in item['permutation_new_index_to_old_index']]
  assert values==item['exact_selected_objects'];decoded[group]=values
 else:
  for j,ring in enumerate(item['ordered_ring_axis']):
   rows.append({'kind':'exact child and enclosing parent state','group':group,'ring_axis_index':j,'ring':ring,'complete_child':item['exact_three_child_states'][j],'complete_parent':item['exact_three_parent_states'][j]})
  decoded[group]=item['exact_three_child_states'];decoded[item['parent_group']]=item['exact_three_parent_states']
chunks=[];cur=[];size=0
for row in rows:
 line=json.dumps(row,ensure_ascii=False)+'\n';n=len(line.encode())
 if cur and size+n>8500:chunks.append(cur);cur=[];size=0
 cur.append(line);size+=n
if cur:chunks.append(cur)
manifest=[];restored=[]
for i,lines in enumerate(chunks,1):
 p=O/f'scan026_source_sections04_12_state_review_v01_{i:02}.jsonl';raw=''.join(lines).encode();p.write_bytes(raw)
 restored.extend(json.loads(x) for x in lines);manifest.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
assert restored==rows
proof={'scope':'All selected candidate arrays only. Full authority and original objects remain in the bound state-map artifact; this display does not claim to reproduce unrelated metadata.',
 'candidate_sets_reconstructed':{k:len(v) for k,v in decoded.items()},'each_reading_map_forward_and_inverse_exact':True,
 'all_other_candidate_fields_in_original_order':True,'bounded_display_parse_concatenation_exact':True,'chunks':manifest,
 'state_map_sha256':hashlib.sha256((O/'scan026_source_sections04_12_state_maps_v01.json').read_bytes()).hexdigest()}
(O/'scan026_source_sections04_12_state_review_proof_v01.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(proof,ensure_ascii=False,indent=2))
