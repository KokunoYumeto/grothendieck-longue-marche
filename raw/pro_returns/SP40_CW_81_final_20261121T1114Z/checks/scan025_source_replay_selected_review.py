#!/usr/bin/env python3
"""Decode and prove the bounded selected-record projection, without images."""
from pathlib import Path
from functools import lru_cache
import hashlib,json,bisect,re,sys
ROOT=Path(__file__).resolve().parents[2];O=ROOT/'out/checks';V=sys.argv[1]if len(sys.argv)>1 else'v03'
sha=lambda b:hashlib.sha256(b.encode()if isinstance(b,str)else b).hexdigest()
dump=lambda x:json.dumps(x,ensure_ascii=False,indent=2)+'\n'
MANP=O/f'scan025_source_selected_review_manifest_{V}.json';MAN=json.loads(MANP.read_text());CP=ROOT/MAN['codec']['path'];assert sha(CP.read_bytes())==MAN['codec']['sha256'];C=json.loads(CP.read_text())
BP=ROOT/C['base_pool']['path'];assert sha(BP.read_bytes())==C['base_pool']['sha256'];B=json.loads(BP.read_text());BF={x['id']:x for x in B['files']};BS={x['id']:x for x in B['strings']};BSP={x['id']:x for x in B['spans']}
BT={}
for fid,f in BF.items():
    BT[fid]=''.join(BS[x['string_ref']]['literal']for x in f['payload']['text_chunks'])if f['kind']=='text'else(ROOT/f['path']).read_text()
    assert sha(BT[fid])==f['sha256_utf8']
BJ={fid:json.loads(BT[fid])for fid,f in BF.items()if f['kind']=='json'};BY_PATH={f['path']:fid for fid,f in BF.items()}
def get(v,p):
    for k in p[1:].split('/')if p else[]:
        k=k.replace('~1','/').replace('~0','~');v=v[int(k)]if isinstance(v,list)else v[k]
    return v
def base_json(ref):
    v=get(BJ[ref['file']],ref['pointer']);s=BSP[ref['span']];assert s['source_file']==ref['file'];assert json.loads(BT[ref['file']][s['char_start']:s['char_end_exclusive']])==v;return v
ST={x['id']:x for x in C['source_table']};TEXT={};LINES={};NONASCII={};EXTRAS={}
for q,s in ST.items():
    t=BT[BY_PATH[s['path']]]if s['path']in BY_PATH else(ROOT/s['path']).read_text();assert sha(t)==s['sha256'];TEXT[q]=t;LINES[q]=[m.start()for m in re.finditer('\n',t)];NONASCII[q]=[];EXTRAS[q]=[];n=0
    for i,ch in enumerate(t):
        if ord(ch)>127:n+=len(ch.encode())-1;NONASCII[q].append(i);EXTRAS[q].append(n)
def byte_at(q,a):
    i=bisect.bisect_left(NONASCII[q],a);return a+(EXTRAS[q][i-1]if i else 0)
def bounds(q,a,b):return [a,b,byte_at(q,a),byte_at(q,b),bisect.bisect_left(LINES[q],a)+1,bisect.bisect_left(LINES[q],max(a,b-1))+1]
@lru_cache(None)
def external_document(q):return json.loads(TEXT[q])
def external_json(ref):
    q=ref['source'];a,b=ref['bounds'][:2];assert bounds(q,a,b)==ref['bounds'];v=json.loads(TEXT[q][a:b]);assert v==get(external_document(q),ref['pointer']);return v
S={x['id']:x for x in C['strings']};OBJ={x['id']:x for x in C['containers']}
def decode(x):
    if isinstance(x,dict)and set(x)=={'$t'}:return string(x['$t'])
    if isinstance(x,dict)and set(x)=={'$o'}:return container(x['$o'])
    assert not isinstance(x,(dict,list));return x
@lru_cache(None)
def string(sid):
    entry=S[sid];r=entry['recipe']
    if 'literal'in r:v=r['literal']
    elif 'base_json_string'in r:v=base_json(r['base_json_string'])
    elif 'external_json_string'in r:v=external_json(r['external_json_string'])
    elif 'base_pool_string'in r:
        z=BS[r['base_pool_string']]['literal']
        if isinstance(z,str):v=z
        else:s=BSP[z['span_ref']];v=BT[s['source_file']][s['char_start']:s['char_end_exclusive']]
    elif 'source_span'in r:
        ref=r['source_span'];q=ref['source'];a,b=ref['bounds'][:2];assert bounds(q,a,b)==ref['bounds'];v=TEXT[q][a:b]
    elif 'concatenate'in r:v=''.join(decode(p)for p in r['concatenate'])
    elif 'json_serialization'in r:
        z=r['json_serialization'];v=json.dumps(decode(z['value']),ensure_ascii=z['ensure_ascii'],separators=tuple(z['separators']))
    else:raise AssertionError(r)
    assert isinstance(v,str)and len(v)==entry['characters']and len(v.encode())==entry['utf8_bytes']and sha(v)==entry['sha256'];return v
@lru_cache(None)
def container(oid):
    o=OBJ[oid];kind=o['kind']
    if kind=='object':return {k:decode(v)for k,v in o['items']}
    if kind=='array':return [decode(v)for v in o['items']]
    if kind=='base_json_value':return base_json(o['source'])
    if kind=='external_json_value':return external_json(o['source'])
    assert kind=='source_span_object';q=o['source'];p=ST[q]['path'];a,b=o['bounds'];z=bounds(q,a,b);literal=TEXT[q][a:b];h=ST[q]['sha256']
    values={'path':p,'workspace_path':p,'source_path':p,'out_relative_path':p[4:],'sha256':h,'sha256_utf8':h,'source_sha256_utf8':h,
            'char_start':a,'char_end':b,'char_end_exclusive':b,'utf8_byte_start':z[2],'utf8_byte_end':z[3],'utf8_byte_end_exclusive':z[3],
            'line_start':z[4],'line_end':z[5],'line_start_1based':z[4],'line_end_1based':z[5],'body_sha256':sha(literal),'literal_sha256_utf8':sha(literal),'literal':literal}
    extra=iter(o['extra_values']);result={}
    for key,rule in C['source_span_object_templates'][o['template']]:result[key]=decode(next(extra))if rule=='extra'else values[rule]
    assert next(extra,None)is None;return result

DOCS={};checks=[]
for d in C['documents']:
    value=decode(d['root']);text=dump(value);assert sha(text)==d['sha256'];assert text==(ROOT/d['path']).read_text();DOCS[d['id']]=(d,value,text)
    checks.append(dict(path=d['path'],sha256=d['sha256'],exact_utf8_reconstruction=True,json_pointer_count=len(C['document_pointer_bounds'][d['path']])))
for sid in S:string(sid)
for oid in OBJ:container(oid)
seen_s=set();seen_o=set();field_count=0
def require_known(v):
    if isinstance(v,dict):
        if '$t'in v:assert v['$t']in seen_s
        elif '$o'in v:assert v['$o']in seen_o
def dependencies(obj):
    if obj['kind']=='object':return [v for k,v in obj['items']]
    if obj['kind']=='array':return obj['items']
    if obj['kind']=='source_span_object':return obj['extra_values']
    return []
for page in MAN['pages']:
    raw=(ROOT/page['path']).read_bytes();assert sha(raw)==page['sha256']
    for line in raw.decode().splitlines():
        row=json.loads(line)
        if 't'in row:
            sid=row['t'];assert sid not in seen_s and row['recipe']==S[sid]['recipe'];r=row['recipe']
            for v in r.get('concatenate',[]):require_known(v)
            if 'json_serialization'in r:require_known(r['json_serialization']['value'])
            seen_s.add(sid)
        elif 'o'in row:
            oid=row['o'];assert oid not in seen_o;assert {k:v for k,v in row.items()if k!='o'}=={k:v for k,v in OBJ[oid].items()if k!='id'}
            for v in dependencies(OBJ[oid]):require_known(v)
            seen_o.add(oid)
        else:
            did,ptr=row['field'];d,value,text=DOCS[did];z=C['document_pointer_bounds'][d['path']][ptr];assert row['span']==[z[k]for k in ['char_start','char_end','utf8_byte_start','utf8_byte_end','line_start','line_end']]
            require_known(row['value']);assert decode(row['value'])==get(value,ptr);assert json.loads(text[z['char_start']:z['char_end']])==get(value,ptr);field_count+=1
assert seen_s==set(S)and seen_o==set(OBJ)
result=dict(scan=25,status='lossless selected review replay passed',manifest=dict(path=str(MANP.relative_to(ROOT)),sha256=sha(MANP.read_bytes())),codec=dict(path=str(CP.relative_to(ROOT)),sha256=sha(CP.read_bytes())),documents=checks,
    strings_checked=len(S),containers_checked=len(OBJ),projection_fields_checked=field_count,all_first_use_dependencies_precede_references=True,all_new_literal_string_values_exposed_once=True,original_source_references_preserve_roles=True,
    source_table_files_checked=len(ST),no_images_opened=True,no_render_or_ink_validation=True,main_approved=False)
path=O/f'scan025_source_selected_review_replay_{V}.json';path.write_text(dump(result));print(dump(result))
