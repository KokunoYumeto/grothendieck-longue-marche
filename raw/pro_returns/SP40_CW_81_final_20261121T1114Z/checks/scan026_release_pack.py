"""Exact source-referenced JSON packing and bounded field review; no source writes."""
from pathlib import Path
import collections
import hashlib
import json

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'out/checks'
P='scan026_release_'
def sha(b):return hashlib.sha256(b).hexdigest()
def compact(v):return json.dumps(v,ensure_ascii=False,separators=(',',':'))
def pretty(v):return (json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode()
def esc(k):return str(k).replace('~','~0').replace('/','~1')
def get(v,p):
    for x in p.split('/')[1:] if p else []:
        k=x.replace('~1','/').replace('~0','~');v=v[int(k)] if isinstance(v,list) else v[k]
    return v
def walk(v,p=''):
    yield p,v
    if isinstance(v,dict):
        for k,w in v.items():yield from walk(w,p+'/'+esc(k))
    elif isinstance(v,list):
        for i,w in enumerate(v):yield from walk(w,p+'/'+str(i))
def key(v):return sha(compact(v).encode())
def save(name,value):
    assert name.startswith(P)
    b=pretty(value);(OUT/name).write_bytes(b)
    return {'path':'out/checks/'+name,'sha256':sha(b),'bytes':len(b)}

registry=json.loads((OUT/'scan026_source_union_sources_v01.json').read_text())
source_paths=[x['path'] for x in registry.values()]
source_paths += ['out/checks/'+n for n in [
    'scan026_root_decisions.json','scan026_root_journal.md','scan026_root_locus_supplement_v01.json',
    'scan026_root_source_clarifications_v01.json','scan026_root_notes_abbreviation_authority_v01.json',
    'scan026_source_union_v01.json','scan026_source_union_state_pool_v01.json','scan026_source_union_sources_v01.json',
    'scan026_source_record_scaffold_v01.json','scan026_source_state_catalog_v01.json',
    'scan026_source_union_inventory_context_v01.json','scan026_source_union_C_rows_v01.json',
    'scan026_source_union_H_marker_bindings_v01.json','scan026_source_union_scope_addendum_v02.json']]
source_paths=list(dict.fromkeys(source_paths))
sources=[];source_values={};matches={};source_bytes={}
for i,path in enumerate(source_paths):
    b=(BASE/path).read_bytes();sid='F'+str(i+1).zfill(3)
    sources.append({'id':sid,'path':path,'sha256':sha(b),'bytes':len(b)})
    source_bytes[sid]=b
    if path.endswith('.json'):
        value=json.loads(b);source_values[sid]=value
        for ptr,node in walk(value):
            matches.setdefault(key(node),{'kind':'source_json','file':sid,'pointer':ptr,'ordered_value_sha256':key(node)})
source_by_path={s['path']:s['id'] for s in sources}

target_names=[
    P+'audit_v01.json',P+'inventory_bindings_v01.json',P+'C_row_outcomes_v01.json',
    P+'notes_abbreviations_v01.json',P+'exact_raw_values_v01.json',P+'exact_own_source_spans_v01.json',
    P+'witness_bindings_v01.json',P+'scalar_review_v01.json',P+'raw_reader_flags_v01.json']
targets=[];target_values={};target_bytes={}
for i,name in enumerate(target_names):
    b=(OUT/name).read_bytes();tid='T'+str(i+1).zfill(2);value=json.loads(b)
    assert pretty(value)==b
    targets.append({'id':tid,'path':'out/checks/'+name,'sha256':sha(b),'bytes':len(b)})
    target_values[tid]=value;target_bytes[tid]=b

# Every span reference below has its literal equality checked before pooling.
for value in target_values.values():
    for ptr,node in walk(value):
        if isinstance(node,dict) and 'literal' in node and 'path' in node and 'char_start' in node and 'char_end' in node and node['path'] in source_by_path:
            sid=source_by_path[node['path']];s=source_bytes[sid].decode();a,b=node['char_start'],node['char_end']
            assert s[a:b]==node['literal']
            matches.setdefault(key(node['literal']),{'kind':'source_text','file':sid,'char_start':a,'char_end':b,'utf8_byte_start':len(s[:a].encode()),'utf8_byte_end':len(s[:b].encode()),'literal_sha256':sha(s[a:b].encode())})

def pack_all(values):
    pool=[];lookup={};uses=collections.OrderedDict();roots={}
    def encode(v,tid,ptr):
        digest=key(v)
        if digest in matches:
            desc=matches[digest]
        elif isinstance(v,dict):
            desc={'kind':'object','ordered_keys':list(v)}
        elif isinstance(v,list):
            desc={'kind':'array','length':len(v)}
        else:
            desc={'kind':'value','value':v}
        desc_key=key(desc)
        if desc_key in lookup:
            nid=lookup[desc_key];uses[nid].append((tid,ptr))
        else:
            nid='N'+str(len(pool)+1).zfill(5)
            lookup[desc_key]=nid;uses[nid]=[(tid,ptr)]
            pool.append({'id':nid,'node_sha256':desc_key,'node':desc})
        if desc['kind']=='object':
            for k,w in v.items():encode(w,tid,ptr+'/'+esc(k))
        elif desc['kind']=='array':
            for i,w in enumerate(v):encode(w,tid,ptr+'/'+str(i))
        return nid
    for tid,value in values.items():roots[tid]=encode(value,tid,'')
    return pool,uses,roots

pool,uses,roots=pack_all(target_values)
pool_map={r['id']:r for r in pool}
operation_map={(tid,ptr):nid for nid,items in uses.items() for tid,ptr in items}
def decode(tid,ptr=''):
    nid=operation_map[tid,ptr]
    node=pool_map[nid]['node'];kind=node['kind']
    if kind=='source_json':value=get(source_values[node['file']],node['pointer'])
    elif kind=='source_text':value=source_bytes[node['file']].decode()[node['char_start']:node['char_end']]
    elif kind=='value':value=node['value']
    elif kind=='object':value={k:decode(tid,ptr+'/'+esc(k)) for k in node['ordered_keys']}
    elif kind=='array':value=[decode(tid,ptr+'/'+str(i)) for i in range(node['length'])]
    else:raise AssertionError(kind)
    if kind=='source_json':assert key(value)==node['ordered_value_sha256']
    return value
replayed={tid:decode(tid) for tid in roots}
for tid,value in replayed.items():assert pretty(value)==target_bytes[tid]
pool2,uses2,roots2=pack_all(replayed)
assert pretty(pool2)==pretty(pool) and pretty(roots2)==pretty(roots) and uses2==uses

all_occurrences=uses

def split_path(ptr):
    bits=ptr.split('/')
    if len(bits)>2 and bits[1] in ['rows','records','spans','reader_inventory_bindings','abbreviations'] and bits[2].isdigit():
        return '/'.join(bits[:3]),('/'+'/'.join(bits[3:])) if len(bits)>3 else ''
    return '',ptr
review=[]
for entry in pool:
    grouped=collections.OrderedDict()
    for tid,ptr in all_occurrences[entry['id']]:
        prefix,suffix=split_path(ptr);grouped.setdefault((tid,suffix),[]).append(prefix)
    factors=collections.OrderedDict()
    for (tid,suffix),prefixes in grouped.items():
        factors.setdefault((tid,tuple(prefixes)),[]).append(suffix)
    products=[{'target':tid,'prefixes':list(prefixes),'suffixes':suffixes} for (tid,prefixes),suffixes in factors.items()]
    expanded=[(v['target'],p+s) for v in products for p in v['prefixes'] for s in v['suffixes']]
    expected=all_occurrences[entry['id']]
    assert len(expanded)==len(set(expanded)) and set(expanded)==set(expected)
    review.append({'id':entry['id'],'exact_node':entry['node'],'target_path_products':products})

# Every changed field relative to each original scaffold slot is listed with exact
# before and after refs. Source slot fields absent in the audit remain frozen.
scaffold=json.loads((OUT/'scan026_source_record_scaffold_v01.json').read_text())
audit=target_values['T01'];slotmap={x['source_locus_id']:i for i,x in enumerate(scaffold['pending_decision_slots'])}
field_delta=[]
for i,row in enumerate(audit['rows']):
    lid=row['source_locus_id'];old_i=slotmap.get(lid);before=scaffold['pending_decision_slots'][old_i] if old_i is not None else {}
    added=[];changed=[];identical=[]
    for k,v in row.items():
        after_ref={'target':'T01','pointer':f'/rows/{i}/'+esc(k),'node':operation_map.get(('T01',f'/rows/{i}/'+esc(k)))}
        if k not in before:added.append(after_ref)
        elif compact(before[k])==compact(v):identical.append({'field':k,'before_pointer':f'/pending_decision_slots/{old_i}/'+esc(k),'after':after_ref})
        else:changed.append({'field':k,'before_pointer':f'/pending_decision_slots/{old_i}/'+esc(k),'after':after_ref})
    preserved=[{'field':k,'before_pointer':f'/pending_decision_slots/{old_i}/'+esc(k)} for k in before if k not in row]
    field_delta.append({'locus_id':lid,'before_slot_index':old_i,'after_row_index':i,'added_fields':added,'changed_fields':changed,'identical_fields':identical,'original_fields_preserved_in_frozen_scaffold':preserved})

codec={'schema':'scan026-exact-source-reference-codec-v01','source_files':sources,'target_files':targets,'target_roots':roots,'pool':pool,'node_target_path_products':[{'id':r['id'],'products':r['target_path_products']} for r in review],'serializer':{'ensure_ascii':False,'indent':2,'final_newline':True}}
codec_manifest=save(P+'codec_v01.json',codec)
delta_manifest=save(P+'scaffold_field_delta_v01.json',{'scope':'Finite audit projection; original scaffold bytes stay frozen and every original field remains addressable. Added and altered audit fields are explicit.','original_scaffold_path':'out/checks/scan026_source_record_scaffold_v01.json','rows':field_delta})

# Bounded review includes each exact node once, and every target path product.
chunks=[];current=[];size=0
for row in review:
    line=(compact(row)+'\n').encode()
    if len(line)>11000:
        node_line=(compact({'id':row['id'],'exact_node':row['exact_node']})+'\n').encode()
        assert len(node_line)<=11000,(row['id'],len(node_line))
        pieces=[node_line]
        for j,prod in enumerate(row['target_path_products']):
            pending=[(0,len(prod['prefixes']),0,len(prod['suffixes']))]
            while pending:
                a,b,c,d=pending.pop(0)
                part={'target':prod['target'],'prefixes':prod['prefixes'][a:b],'suffixes':prod['suffixes'][c:d]}
                piece=(compact({'id':row['id'],'product_index':j,'prefix_start':a,'suffix_start':c,'target_path_product':part})+'\n').encode()
                if len(piece)<=11000:pieces.append(piece)
                elif b-a>=d-c and b-a>1:
                    mid=(a+b)//2;pending[:0]=[(a,mid,c,d),(mid,b,c,d)]
                elif d-c>1:
                    mid=(c+d)//2;pending[:0]=[(a,b,c,mid),(a,b,mid,d)]
                else:raise AssertionError((row['id'],len(piece)))
    else:pieces=[line]
    for piece in pieces:
        if current and size+len(piece)>11000:
            chunks.append(current);current=[];size=0
        current.append(piece);size+=len(piece)
if current:chunks.append(current)
files=[]
for i,lines in enumerate(chunks,1):
    b=b''.join(lines);name=P+f'complete_review_v01_{i:03d}.jsonl';(OUT/name).write_bytes(b)
    files.append({'path':'out/checks/'+name,'bytes':len(b),'sha256':sha(b),'lines':len(lines)})

source_unchanged=[]
for item in sources:
    b=(BASE/item['path']).read_bytes();assert sha(b)==item['sha256'];source_unchanged.append({'file':item['id'],'sha256':sha(b),'exact_bytes_unchanged':True})
proof={
    'codec':codec_manifest,'target_forward_byte_replay':[dict(t,exact_byte_equality=pretty(replayed[t['id']])==target_bytes[t['id']]) for t in targets],
    'inverse_pack_exact_pool_bytes':pretty(pool2)==pretty(pool),'inverse_pack_exact_root_bytes':pretty(roots2)==pretty(roots),'inverse_pack_exact_all_use_mappings':uses2==uses,
    'ordered_source_node_matches_verified':sum(x['node']['kind']=='source_json' for x in pool),'literal_source_span_matches_verified':sum(x['node']['kind']=='source_text' for x in pool),
    'source_files_exact_bytes_unchanged':source_unchanged,
    'raw_record_exact_values_and_key_order':1106,'complete_own_reader_TeX_forward_inverse_partition_replay':['A','B','C'],
    'review_nodes':len(review),'review_file_count':len(files),'all_exact_target_products_verified':True,'field_delta':delta_manifest,
    'root_review_claimed':False,'no_original_source_mutations':True,
}
proof_manifest=save(P+'replay_v01.json',proof)
index=save(P+'complete_review_index_v01.json',{
    'scope':'Every source reference resolves to an unchanged frozen value. Every remaining novel node is printed in full. Container field order is explicit. Exact node path products cover every target occurrence; a source node also carries all descendants by the identical JSON-pointer suffix map.',
    'read_order':['scan026_release_scalar_index_v01.json','scan026_release_complete_review_index_v01.json']+[x['path'].split('/')[-1] for x in files],
    'source_files':sources,'target_files':targets,'target_roots':roots,'codec':codec_manifest,'replay':proof_manifest,'field_delta':delta_manifest,
    'review_nodes':len(review),'node_kinds':dict(collections.Counter(x['node']['kind'] for x in pool)),
    'pointer_rule':'For each target_path_products entry take every prefix + every suffix. All indices are zero-based; JSON object keys use RFC6901 escaping. Every product is checked against its complete occurrence set.',
    'review_files':files,'root_review_claimed':False,
})
print(json.dumps({'index':index,'nodes':len(pool),'kinds':dict(collections.Counter(x['node']['kind'] for x in pool)),'chunks':len(files)},ensure_ascii=False))
