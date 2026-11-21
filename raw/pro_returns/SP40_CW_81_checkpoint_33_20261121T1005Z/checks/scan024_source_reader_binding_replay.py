"""Pure independent replay entry point for root; reads text and prints a summary.

Source clerk supplies this recipe interpreter without executing it. It does not
write files, open images, render, compile, or select readings/approvals.
"""
from pathlib import Path
import json,hashlib
B=Path('/workspace/scratch/94548b74fbe0')
P=json.loads((B/'out/checks/scan024_source_reader_binding_plan_v01.json').read_text())
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes) else x.encode()).hexdigest()
T={};J={}
for fid,f in P['frozen_source_files'].items():
    raw=(B/f['path']).read_bytes();assert sha(raw)==f['sha256_utf8'],f['path'];T[fid]=raw.decode()
def value(ref):
    t=T[ref['file']];a,b=ref['chars'];fragment=t[a:b]
    assert sha(fragment)==ref['sha256_utf8'],ref
    assert [len(t[:a].encode()),len(t[:b].encode())]==ref['utf8_bytes'],ref
    if 'json_pointer' in ref:
        if ref['file'] not in J:J[ref['file']]=json.loads(t)
        x=J[ref['file']]
        for k in ref['json_pointer'].split('/')[1:]:
            k=k.replace('~1','/').replace('~0','~');x=x[int(k)] if isinstance(x,list) else x[k]
        assert json.loads(fragment)==x,ref
        return x
    return fragment
dump=lambda x:json.dumps(x,ensure_ascii=False,separators=(',',':'))
def selected(fields):return {x['name']:value(x['source']) for x in fields}
def inventory(key):
    recipe=P['restored_inventory_clauses'][key];obj=value(recipe['source']);f=P['frozen_source_files'][recipe['source']['file']]
    return 'Own inventory component scope (verbatim fields): '+dump({k:obj[k] for k in recipe['ordered_fields']})+'; exact own source '+f['path']+'#'+recipe['source']['json_pointer']+', SHA '+f['sha256_utf8']+'.'
group_text={}
for gid,g in P['group_description_recipes'].items():
    f=P['frozen_source_files'][g['literal_group_source']['file']];a,b=g['literal_group_source']['chars']
    s='Own candidate/state fields: '+dump(selected(g['ordered_fields']))
    comments=[value(x) for x in g['comment_line_sources']]
    if comments:s+='\nOwn literal source comments: '+'\n'.join(comments)
    for child in g['contained_group_fields']:s+='\nOwn contained group '+child['group']+': '+dump(selected(child['ordered_fields']))
    for key in g['inventory_clauses']:s+='\n'+inventory(key)
    s='[Editorial own-source group description '+gid+'; '+s+'; exact literal group '+f['path']+' chars['+str(a)+','+str(b)+'), SHA '+f['sha256_utf8']+'.]'
    assert s==value(g['expected_public_source']),gid
    assert sha(s)==g['expected_public_sha256_utf8'],gid
    group_text[gid]=s
projection=json.loads((B/P['projection']['path']).read_text());record=json.loads((B/P['record']['path']).read_text())
assert sha((B/P['projection']['path']).read_bytes())==P['projection']['sha256_utf8']
assert sha((B/P['record']['path']).read_bytes())==P['record']['sha256_utf8']
existing=json.loads((B/P['existing_frame_projection']['path']).read_text())['frames'];covered=set()
for f in P['existing_frame_bindings']:
    old=existing[f['frame']]
    for sub in f['group_substitutions']:
        a,b=sub['public_range_in_projected_literal'];assert old['projected_literal'][a:b]==group_text[sub['group']]
    if f['archive_inventory_clause']:assert inventory(f['archive_inventory_clause']) in old['public']
    for pid in f['public_pool_ids']:assert projection['values'][pid]==old['public'];covered.add(pid)
for pid,a in P['appendix_recipes'].items():
    objects=[]
    for entry in a['source_entries']:
        original=value(entry['source']);obj={k:original[k] for k in entry['ordered_fields']}
        if entry['duplicate_existing_value']:assert objects[entry['emitted_object_index']]==obj
        else:assert entry['emitted_object_index']==len(objects);objects.append(obj)
    s=a['leading_editorial_literal']+dump(objects)
    assert s==projection['values'][pid],pid
    assert sha(s)==a['expected_value_sha256_utf8'],pid;covered.add(pid)
for pid,o in P['other_chunk_recipes'].items():assert o['value']==projection['values'][pid];covered.add(pid)
for f in P['reader_field_bindings']:
    x=record
    for k in f['record_pointer'].split('/')[1:]:x=x[int(k)] if isinstance(x,list) else x[k]
    s=''.join(projection['values'][pid] for pid in f['pool_ids'])
    assert s==x and sha(s)==f['expected_reader_sha256_utf8'],f['record_pointer']
    assert set(f['pool_ids'])<=covered,f['record_pointer']
assert not P['mapping_issues'],P['mapping_issues']
print(json.dumps(dict(scan=24,source_only=True,counts=P['counts'],exact_original_group_metadata_and_comments=True,exact_all151_original_local_appendices=True,all_twelve_inventory_scopes_bound=True,A_D29_scope=P['A_D29_focus'],all_reader_pool_chunks_covered=len(covered),all_current_reader_fields_exact=True,images_opened=0,files_written=0,approval_performed=False),ensure_ascii=False,indent=2))
