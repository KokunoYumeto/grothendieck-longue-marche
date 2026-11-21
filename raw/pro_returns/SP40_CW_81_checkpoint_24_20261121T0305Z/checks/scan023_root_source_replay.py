from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,collections
BASE=Path('/workspace/scratch/94548b74fbe0');OUT=BASE/'out';MAP=OUT/'checks/scan023_final_source_map.json'
m=json.loads(MAP.read_text()); cache={}; checked=[]
sha=lambda b:hashlib.sha256(b).hexdigest()
def get(path):
 p=Path(path)
 if not p.is_absolute():p=(BASE if path.startswith(('out/','packets/','source/')) else OUT)/p
 assert p.suffix.lower() in ('.tex','.json','.md','.txt','.tsv','.py'),str(p)
 if str(p) not in cache:
  b=p.read_bytes();cache[str(p)]=(b,b.decode('utf-8'))
 return cache[str(p)]
def walk(x,at=''):
 if isinstance(x,dict):
  path=x.get('path'); a=x.get('char_start_zero_based',x.get('char_start'));z=x.get('char_end_exclusive',x.get('char_end'))
  if isinstance(path,str) and isinstance(a,int) and isinstance(z,int):
   b,t=get(path);assert 0<=a<=z<=len(t),(at,path,a,z)
   s=t[a:z];sb=s.encode('utf-8')
   for key in ('file_sha256_utf8',):
    if key in x:assert x[key]==sha(b),(at,key)
   if 'literal' in x:assert x['literal']==s,(at,'literal')
   for key in ('span_sha256_utf8','body_sha256'):
    if key in x:assert x[key]==sha(sb),(at,key)
   for key,value in (('utf8_byte_start',len(t[:a].encode())),('start_byte_utf8',len(t[:a].encode())),('utf8_byte_end_exclusive',len(t[:z].encode())),('end_byte_utf8',len(t[:z].encode()))):
    if key in x:assert x[key]==value,(at,key)
   checked.append((path,a,z,sha(sb)))
  for k,v in x.items():walk(v,at+'/'+k)
 elif isinstance(x,list):
  for i,v in enumerate(x):walk(v,at+'/'+str(i))
walk(m)
draft=(OUT/'checks/scan023_final_draft.tex').read_text()
assert sha(draft.encode())==m['draft_sha256_utf8']=='b9a1249d12916f42eb5694e4e2433f2c95d5435083078cdb5f71db5ea7b69a1f'
assert sha(MAP.read_bytes())=='5c11242ea3f4fe19b14b70a8fb5707f7e36a6911cbce6525850a3201d86c41e3'
parts=m['complete_selected_source_partition'];assert ''.join(p['selected_source']['literal'] for p in parts)==draft
for i,p in enumerate(parts):
 assert p['selected_start']==(0 if not i else parts[i-1]['selected_end'])
 assert p['selected_source']['literal']==draft[p['selected_start']:p['selected_end']]
leaf=[]
for c in m['exact_command_ownership']:
 if c['command'] in ('draw','fill'):
  assert c['donor_exact_matches'],c['command_id']
  assert all(c['selected_source']['literal']==d['source']['literal'] for d in c['donor_exact_matches']),c['command_id']
  leaf.append(c['command_id'])
assert len(leaf)==75
assert len(m['source_locus_coverage'])==62
assert [x['locus_id'] for x in m['source_locus_coverage']]==[f'U023-{i:02d}' for i in range(1,63)]
group_ids={g['group_id'] for g in m['selected_groups']}
for g in m['selected_groups']:
 assert g['complete_exact_source']==g['selected_source']['literal']
 assert all(x in group_ids for x in g['child_group_ids'])
 if g['parent_group']:assert g['parent_group'] in group_ids
result={'scan':23,'reviewed_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'scope':'Root read the complete selected TeX in three bounded slices. This replay binds all stored character/byte slices and literal drawing commands to those read bytes and the frozen donor text. No image, rendering, compilation or coordinate computation.','draft_sha256':m['draft_sha256_utf8'],'map_sha256':sha(MAP.read_bytes()),'reference_occurrences':len(checked),'distinct_references':len(set(checked)),'text_files':len(cache),'selected_groups':len(group_ids),'literal_draw_fill_commands':len(leaf),'complete_commands':len(m['exact_command_ownership']),'layout_contexts':len(m['layout_contexts']),'wrappers':len(m['exact_wrapper_ownership']),'complete_partition_parts':len(parts),'source_loci':62,'errors':[],'root_approval':False}
p=OUT/'checks/scan023_root_source_replay.json';p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
