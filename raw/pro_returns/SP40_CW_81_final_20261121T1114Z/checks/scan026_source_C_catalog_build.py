"""Frozen C source catalogue. References preserve full raw scopes and order."""
import hashlib
import json
from pathlib import Path

BASE=Path('/workspace/scratch/94548b74fbe0')
ROOT=BASE/'out/readers/026/C';OUT=BASE/'out/checks';P='scan026_source_C_catalog_'
names=['reading.tex','reading.md','report.json','source_map.json','crop_plan.json','crop_audit.json','frozen_manifest.json']
raw={n:(ROOT/n).read_bytes() for n in names};sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(raw['reading.tex'])=='7c05f3fc0f28985e2cd66c3fbe6486eaf7d38ab20a4a2f7fbf29b1742868b951'
assert sha(raw['report.json'])=='b7d7ef133f3b8943075e860c2ecc60249db0f9eb0afc10d15edc3a18d499c621'
tex=raw['reading.tex'].decode();r=json.loads(raw['report.json']);s=json.loads(raw['source_map.json'])


def esc(v):return str(v).replace('~','~0').replace('/','~1')
def ref(n,p=''):return {'path':'out/readers/026/C/'+n,'sha256':sha(raw[n]),'json_pointer':p}
def span(a,b):return {'path':'out/readers/026/C/reading.tex','file_sha256':sha(raw['reading.tex']),'start_char':a,'end_char_exclusive':b,'start_utf8_byte':len(tex[:a].encode()),'end_utf8_byte_exclusive':len(tex[:b].encode()),'line_start':tex.count('\n',0,a)+1,'line_end':tex.count('\n',0,max(a,b-1))+1,'span_sha256':sha(tex[a:b].encode())}
def write(n,v):(OUT/(P+n+'.json')).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')


display_keys={'id','location','reading','alternatives','complete_qualified_reading','candidate_states','confidence','kind','diff_C','diff_H','C_doubt_status','source_rows','source_part','source_groups','physical_cluster','H_count_parent','C_count_parent','physical_count_parent','raw_diff_C','raw_diff_H','hand','candidate_hand','role','attachment','element','position','first_words_or_objects','bbox','readers_crop','crop','qualification','status','local_parts','source_group','connection','printed_head_qualifier','evidence_view','complete_scope','difference_ids','count_source_row_once'}
records=[]
for key,entries in r.items():
 if not isinstance(entries,list):continue
 for i,v in enumerate(entries):
  ptr='/'+esc(key)+'/'+str(i);item={'section':key,'index':i,'raw_ref':ref('report.json',ptr)}
  if isinstance(v,dict):
   item['ordered_field_references']=[{'key':k,'ref':ref('report.json',ptr+'/'+esc(k))} for k in v]
   item['display']={k:x for k,x in v.items() if k in display_keys}
   assert list(v)==[f['key'] for f in item['ordered_field_references']]
  else:item['display']=v
  records.append(item)

groups=[]
for i,g in enumerate(s['groups']):
 a,b=g['source_span']['start_character'],g['source_span']['end_character_exclusive']
 assert tex[a:b]==g['source_exact'];assert sha(tex[a:b].encode())==g['source_sha256']
 item={k:v for k,v in g.items() if k!='source_exact'};item['raw_ref']=ref('source_map.json','/groups/'+str(i));item['exact_source_span']=span(a,b)
 item['enclosing_source_group_ids']=[other['id'] for other in s['groups'] if other['source_span']['start_character']<=a and b<=other['source_span']['end_character_exclusive'] and other['id']!=g['id']]
 restored={k:(tex[a:b] if k=='source_exact' else item[k]) for k in g};assert json.dumps(restored,ensure_ascii=False)==json.dumps(g,ensure_ascii=False)
 groups.append(item)

bounds=sorted({0,len(tex)}|{v for g in groups for v in (g['exact_source_span']['start_char'],g['exact_source_span']['end_char_exclusive'])})
partition=[]
for a,b in zip(bounds,bounds[1:]):
 owners=[g['id'] for g in groups if g['exact_source_span']['start_char']<=a and b<=g['exact_source_span']['end_char_exclusive']]
 item={'start_char':a,'end_char':b,'owners':owners,'exact_source_span':span(a,b)}
 if not owners:item['exact_text']=tex[a:b]
 partition.append(item)
assert ''.join(tex[p['start_char']:p['end_char']] for p in partition).encode()==raw['reading.tex']
manifest={'source_only':True,'scope':'Frozen C source catalogue; raw wording, candidate, role, hand and source-annotation scopes remain separate.',
 'files':{n:{'path':'out/readers/026/C/'+n,'sha256':sha(b),'bytes':len(b)} for n,b in raw.items()},
 'report_top_level_key_order':list(r),'report_nonarray_refs':{k:ref('report.json','/'+esc(k)) for k,v in r.items() if not isinstance(v,list)},
 'source_map_top_level_refs':{k:ref('source_map.json','/'+esc(k)) for k in s},
 'counts':{'report_array_records':len(records),'source_groups':len(groups),'partition_pieces':len(partition),'Sigma_records':len(s['all_Sigma_occurrences']),'ring_records':len(s['recurring_ring_occurrences'])},
 'inverse_rule':'Dereference each ordered raw JSON field in the frozen file; restore the literal group from its exact TeX character span. All group objects and the complete partition have exact replay checks. Raw files remain necessary inputs.'}
write('manifest_v01',manifest);write('report_records_v01',records);write('groups_v01',groups);write('partition_v01',partition)
write('replay_v01',{'source_only':True,'all_group_spans_and_key_order_roundtrips_exact':True,'complete_partition_exact_bytes':True,'raw_files_unchanged':all((ROOT/n).read_bytes()==b for n,b in raw.items()),'images_read':0,'root_decisions':0})
print(json.dumps(manifest['counts'],indent=2))
