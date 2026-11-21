"""Frozen B source references and exact local scopes. No images are read."""
import hashlib
import json
from pathlib import Path

BASE = Path('/workspace/scratch/94548b74fbe0')
ROOT = BASE / 'out/readers/026/B'
OUT = BASE / 'out/checks'
P = 'scan026_source_B_catalog_'
files = ['reading.tex','reading.md','report.json','source_map.json','crop_plan.json','crop_audit.json','FREEZE.json']
raw = {n: (ROOT/n).read_bytes() for n in files}
digest = lambda b: hashlib.sha256(b).hexdigest()
assert digest(raw['reading.tex']) == '1c36f765e58e84962435ac4afe055eb55e561b9f6927f8d09cc139d0562e7289'
tex = raw['reading.tex'].decode()
r = json.loads(raw['report.json'])
s = json.loads(raw['source_map.json'])


def ref(name, pointer=''):
    return {'path':'out/readers/026/B/'+name,'sha256':digest(raw[name]),'json_pointer':pointer}


def esc(k):
    return str(k).replace('~','~0').replace('/','~1')


def span(start,end):
    return {'path':'out/readers/026/B/reading.tex','file_sha256':digest(raw['reading.tex']),
            'start_char':start,'end_char_exclusive':end,'start_utf8_byte':len(tex[:start].encode()),
            'end_utf8_byte_exclusive':len(tex[:end].encode()),'line_start':tex.count('\n',0,start)+1,
            'line_end':tex.count('\n',0,max(start,end-1))+1,'span_sha256':digest(tex[start:end].encode())}


def write(name,data):
    (OUT/(P+name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')


display_keys = {'id','location','reading','alternatives','complete_candidates','confidence','kind','diff_C','diff_H',
                'C_doubt_status','physical_cluster','source_group','local_parts','local_recurrences','H_count_parent',
                'hand','role','attachment','element','position','first_words_or_objects','bbox','readers_crop','crop','C','H',
                'qualification','status','scope_note','source_row','graphic_id','selected_source_reading','source_comment_candidates',
                'complete_candidate_states','printed_qualifier','retained_later_qualification','states','source_row_id',
                'aggregate_status','count_scope','qualified_difference','marked_in_H'}
records=[]
for key,array in r.items():
    if not isinstance(array,list): continue
    for i,value in enumerate(array):
        ptr='/'+esc(key)+'/'+str(i)
        item={'section':key,'index':i,'raw_ref':ref('report.json',ptr)}
        if isinstance(value,dict):
            item['ordered_field_references']=[{'key':k,'ref':ref('report.json',ptr+'/'+esc(k))} for k in value]
            item['display']={k:v for k,v in value.items() if k in display_keys}
            assert list(value)==[f['key'] for f in item['ordered_field_references']]
        else: item['display']=value
        records.append(item)

groups=[]
for i,g in enumerate(s['source_groups']):
    a,b=g['start_char'],g['end_char']
    assert tex[a:b]==g['literal_source']
    assert digest(tex[a:b].encode())==g['source_sha256']
    item={k:v for k,v in g.items() if k!='literal_source'}
    item['raw_ref']=ref('source_map.json','/source_groups/'+str(i))
    item['exact_source_span']=span(a,b)
    item['enclosing_source_group_ids']=[o['id'] for o in s['source_groups'] if o['start_char']<=a and b<=o['end_char'] and o['id']!=g['id']]
    item['candidate_record_refs']=[ref('report.json','/candidate_records/'+str(j)) for j,c in enumerate(r['candidate_records']) if c['graphic_id']==g['id']]
    item['special_component_refs']=[ref('report.json','/special_component_candidates/'+str(j)) for j,c in enumerate(r['special_component_candidates']) if c['source_group']==g['id']]
    restored={k:(tex[a:b] if k=='literal_source' else item[k]) for k in g}
    assert json.dumps(restored,ensure_ascii=False)==json.dumps(g,ensure_ascii=False)
    groups.append(item)

parts=[]
cursor=0
for i,part in enumerate(s['ordered_source_partition']):
    a,b=part['start_char'],part['end_char']
    assert a==cursor and tex[a:b]==part['source'];cursor=b
    item={k:v for k,v in part.items() if k!='source'}
    item['raw_ref']=ref('source_map.json','/ordered_source_partition/'+str(i))
    item['exact_source_span']=span(a,b)
    if not part['owners']: item['exact_text']=part['source']
    parts.append(item)
assert cursor==len(tex)
assert ''.join(tex[p['start_char']:p['end_char']] for p in parts).encode()==raw['reading.tex']

manifest={'source_only':True,'scope':'Frozen B source catalogue; no other reader state is imported.',
          'files':{n:{'path':'out/readers/026/B/'+n,'sha256':digest(b),'bytes':len(b)} for n,b in raw.items()},
          'report_top_level_key_order':list(r),'source_map_top_level_refs':{k:ref('source_map.json','/'+esc(k)) for k in s},
          'report_nonarray_refs':{k:ref('report.json','/'+esc(k)) for k,v in r.items() if not isinstance(v,list)},
          'counts':{'report_array_records':len(records),'source_groups':len(groups),'partition_pieces':len(parts),'candidate_records':len(r['candidate_records']),'special_component_records':len(r['special_component_candidates'])},
          'inverse_rule':'Dereference ordered fields in the frozen raw JSON; replace each source span by its exact TeX character slice. Every group and partition has been replayed exactly. Raw files remain necessary inputs.',
          'sigma_numbering_scope':'B source ids S01-S37 cover the 37 named main-text Sigma groups; the diagram contains its own two lower Sigma labels. B S15 is the first lower-pair Sigma; it is not A S15.'}
write('manifest_v01',manifest);write('report_records_v01',records);write('groups_v01',groups);write('partition_v01',parts)
write('replay_v01',{'source_only':True,'all_group_exact_spans_and_key_order_roundtrips':True,'partition_exact_bytes':True,
                    'raw_files_unchanged':all((ROOT/n).read_bytes()==b for n,b in raw.items()),'images_read':0,'C_read':False,'root_review_claimed':False})
print(json.dumps(manifest['counts'],indent=2))
