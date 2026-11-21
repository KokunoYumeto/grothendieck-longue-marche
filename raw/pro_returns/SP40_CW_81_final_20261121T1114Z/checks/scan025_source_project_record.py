#!/usr/bin/env python3
"""Lossless, bounded final-record review; exact originals are reused by reference."""
from pathlib import Path
from collections import defaultdict
import hashlib,json,re,bisect,sys
VERSION=sys.argv[1] if len(sys.argv)>1 else 'v03'
assert VERSION in ['v01','v03']
ROOT=Path(__file__).resolve().parents[2];O=ROOT/'out/checks'
sha=lambda v:hashlib.sha256(v.encode('utf-8') if isinstance(v,str) else v).hexdigest()
dump=lambda v:json.dumps(v,ensure_ascii=False,indent=2)+'\n'
compact=lambda v:json.dumps(v,ensure_ascii=False,separators=(',',':'))
P=json.loads((O/'scan025_source_pool_v01.json').read_text())
BF={f['id']:f for f in P['files']};BS={s['id']:s for s in P['strings']};BP={s['id']:s for s in P['spans']}
base_text={}
for fid,f in BF.items():
    if f['kind']=='text':
        base_text[fid]=''.join(BS[x['string_ref']]['literal'] for x in f['payload']['text_chunks'])
    else:base_text[fid]=(ROOT/f['path']).read_text()
    assert sha(base_text[fid])==f['sha256_utf8']
def base_string(sid):
    v=BS[sid]['literal']
    if isinstance(v,str):return v
    s=BP[v['span_ref']];return base_text[s['source_file']][s['char_start']:s['char_end_exclusive']]
BASE_LOOKUP={base_string(sid):sid for sid in BS}
BASE_JSON={fid:json.loads(base_text[fid]) for fid,f in BF.items() if f['kind']=='json'}
BASE_OBJECTS={};BASE_STRING_FIELDS={}
def collect_base(value,fid,ptr=''):
    ref=dict(file=fid,pointer=ptr,span=P['json_pointer_spans'][fid][ptr])
    if isinstance(value,(dict,list)):
        BASE_OBJECTS.setdefault(compact(value),ref)
        entries=value.items() if isinstance(value,dict) else enumerate(value)
        for k,v in entries:collect_base(v,fid,ptr+'/'+str(k).replace('~','~0').replace('/','~1'))
    elif isinstance(value,str):BASE_STRING_FIELDS.setdefault(value,ref)
for fid,value in BASE_JSON.items():collect_base(value,fid)
sources={f['path']:dict(path=f['path'],sha256=f['sha256_utf8'],text=base_text[fid],reviewed_basis='Frozen original source, losslessly projected and already read before root images.') for fid,f in BF.items()}
for name,basis in [('scan025_final_draft.tex','Root complete 434-line selected-page read.'),('scan025_root_journal.md','Root-authored journal through §21.'),('scan025_source_record_values.py','Root complete static-value table read.'),('scan025_root_record_field_clarifications.json','Root seven-leaf current-record authority, fully read and independently replayed.')]:
    path='out/checks/'+name;t=(ROOT/path).read_text();sources[path]=dict(path=path,sha256=sha(t),text=t,reviewed_basis=basis)
upath='out/checks/scan025_source_union_v01.json';utext=(ROOT/upath).read_text();sources[upath]=dict(path=upath,sha256=sha(utext),text=utext,reviewed_basis='Frozen stage1 union; its original values and locus correspondence were reviewed and replayed before root images.')
for i,s in enumerate(sources.values(),1):
    s['id']=f'Q{i:03d}';s['newlines']=[m.start() for m in re.finditer('\n',s['text'])]
    s['nonascii']=[];s['extra_bytes']=[];extra=0
    for pos,ch in enumerate(s['text']):
        if ord(ch)>127:extra+=len(ch.encode())-1;s['nonascii'].append(pos);s['extra_bytes'].append(extra)
def byte_at(s,p):
    i=bisect.bisect_left(s['nonascii'],p);return p+(s['extra_bytes'][i-1]if i else 0)
def source_bounds(s,a,b):return [a,b,byte_at(s,a),byte_at(s,b),bisect.bisect_left(s['newlines'],a)+1,bisect.bisect_left(s['newlines'],max(a,b-1))+1]
def lexical_bounds(text):
    dec=json.JSONDecoder();out={};n=len(text)
    def white(i):
        while i<n and text[i].isspace():i+=1
        return i
    def parse(i,ptr):
        i=white(i);a=i
        if text[i]=='{':
            i=white(i+1)
            if text[i]!='}':
                while True:
                    k,e=dec.raw_decode(text,i);i=white(e);assert text[i]==':';i=parse(i+1,ptr+'/'+k.replace('~','~0').replace('/','~1'));i=white(i)
                    if text[i]=='}':break
                    assert text[i]==',';i=white(i+1)
            i+=1
        elif text[i]=='[':
            i=white(i+1);j=0
            if text[i]!=']':
                while True:
                    i=parse(i,ptr+'/'+str(j));j+=1;i=white(i)
                    if text[i]==']':break
                    assert text[i]==',';i=white(i+1)
            i+=1
        else:_,i=dec.raw_decode(text,i)
        out[ptr]=(a,i);return i
    assert white(parse(0,''))==n;return out
UB=lexical_bounds(utext);UV=json.loads(utext);EXT_OBJECTS={};EXT_STRINGS={}
def collect_external(value,ptr=''):
    a,b=UB[ptr];ref=dict(source=sources[upath]['id'],pointer=ptr,bounds=source_bounds(sources[upath],a,b))
    if isinstance(value,(dict,list)):
        EXT_OBJECTS.setdefault(compact(value),ref)
        entries=value.items()if isinstance(value,dict)else enumerate(value)
        for k,v in entries:collect_external(v,ptr+'/'+str(k).replace('~','~0').replace('/','~1'))
    elif isinstance(value,str):EXT_STRINGS.setdefault(value,ref)
collect_external(UV)
RPATH='out/checks/scan025_record_draft.json';MPATH='out/checks/scan025_final_source_map.json';APATH='out/checks/scan025_source_assembly_record_audit_v03.json' if VERSION=='v03'else'out/checks/scan025_source_record_construction_audit_v01.json'
DOCS={p:json.loads((ROOT/p).read_text()) for p in [RPATH,MPATH,APATH]}
R=DOCS[RPATH]
STRINGS={};SIDS={};CONTAINERS={};OIDS={};TEMPLATES={};TEMPLATE_IDS={}
def add_string(text,recipe=None):
    if text in SIDS:return {'$t':SIDS[text]}
    sid=f'T{len(STRINGS)+1:06d}';SIDS[text]=sid
    entry=dict(id=sid,characters=len(text),utf8_bytes=len(text.encode()),sha256=sha(text))
    if recipe is None:
        if text in BASE_STRING_FIELDS:recipe=dict(base_json_string=BASE_STRING_FIELDS[text])
        elif text in BASE_LOOKUP:recipe=dict(base_pool_string=BASE_LOOKUP[text])
        elif text in EXT_STRINGS:recipe=dict(external_json_string=EXT_STRINGS[text])
        elif len(text)>=12:
            for p,s in sources.items():
                a=s['text'].find(text)
                if a<0:continue
                b=a+len(text);recipe=dict(source_span=dict(source=s['id'],bounds=source_bounds(s,a,b)));break
        if recipe is None:recipe=dict(literal=text)
    entry['recipe']=recipe;STRINGS[sid]=entry;return {'$t':sid}
def exact_reference_body(v):
    if not isinstance(v,dict):return None
    p=v.get('workspace_path')or v.get('source_path')or v.get('path')
    if p and p.startswith('checks/'):p='out/'+p
    s=sources.get(p);a=v.get('char_start');b=v.get('char_end',v.get('char_end_exclusive'))
    if s is None or not isinstance(a,int)or not isinstance(b,int)or not 0<=a<=b<=len(s['text']):return None
    bounds=source_bounds(s,a,b);literal=s['text'][a:b]
    derived={'path':p,'workspace_path':p,'source_path':p,'sha256':s['sha256'],'sha256_utf8':s['sha256'],'source_sha256_utf8':s['sha256'],
             'char_start':a,'char_end':b,'char_end_exclusive':b,'utf8_byte_start':bounds[2],'utf8_byte_end':bounds[3],'utf8_byte_end_exclusive':bounds[3],
             'line_start':bounds[4],'line_end':bounds[5],'line_start_1based':bounds[4],'line_end_1based':bounds[5],
             'body_sha256':sha(literal),'literal_sha256_utf8':sha(literal),'literal':literal}
    rules=[];extras=[];found=0
    for k,x in v.items():
        if k in derived and x==derived[k]:rules.append([k,k]);found+=1
        elif k=='path'and p.startswith('out/')and x==p[4:]:rules.append([k,'out_relative_path']);found+=1
        else:rules.append([k,'extra']);extras.append(x)
    if found<6:return None
    key=compact(rules)
    if key not in TEMPLATE_IDS:
        tid=f'Z{len(TEMPLATES)+1:03d}';TEMPLATE_IDS[key]=tid;TEMPLATES[tid]=rules
    return dict(kind='source_span_object',source=s['id'],bounds=[a,b],template=TEMPLATE_IDS[key],extra_values=[encode(x)for x in extras])
def encode(value):
    if isinstance(value,str):return add_string(value)
    if isinstance(value,(dict,list)) and compact(value) in BASE_OBJECTS:body=dict(kind='base_json_value',source=BASE_OBJECTS[compact(value)])
    elif isinstance(value,(dict,list)) and compact(value) in EXT_OBJECTS:body=dict(kind='external_json_value',source=EXT_OBJECTS[compact(value)])
    elif isinstance(value,dict)and (body:=exact_reference_body(value)) is not None:pass
    elif isinstance(value,dict):body=dict(kind='object',items=[[k,encode(v)] for k,v in value.items()])
    elif isinstance(value,list):body=dict(kind='array',items=[encode(v) for v in value])
    else:return value
    k=compact(body)
    if k not in OIDS:
        oid=f'O{len(CONTAINERS)+1:06d}';OIDS[k]=oid;CONTAINERS[oid]=dict(id=oid,**body)
    return {'$o':OIDS[k]}
def serial_string(text,obj):
    assert text==compact(obj)
    return add_string(text,dict(json_serialization=dict(value=encode(obj),ensure_ascii=False,separators=[',',':'])))
def concat_string(text,parts):
    assert text==''.join(parts)
    refs=[add_string(p) for p in parts];return add_string(text,dict(concatenate=refs))

# Predeclare precise composition rules for every long own-reader public string.
for f in R['provenance']['complete_own_source_frames'].values():
    for p in f['parts']:
        value=p['public_literal']
        if p['kind']=='complete_own_group_descriptor':
            meta=compact(p['metadata']);assert value.endswith(meta+']')
            serial_string(meta,p['metadata']);concat_string(value,[value[:-len(meta)-1],meta,']'])
        else:add_string(value)
    label='\nComplete own inventory fields in this frame, with their original hand and local candidate scopes:\n'
    before,inventory_text=f['public'].rsplit(label,1);inventory=json.loads(inventory_text);serial_string(inventory_text,inventory)
    body=''.join(p['public_literal'] for p in f['parts']);assert before.endswith(body)
    prefix=before[:-len(body)] if body else before
    concat_string(f['public'],[prefix]+[p['public_literal'] for p in f['parts']]+[label,inventory_text])
for d in R['decisions']+R['source_locus_coverage']:
    for r,detail in d['reader_source_details'].items():
        suffix=detail['public_local_suffix'];prefix,payload=suffix.rsplit('\n',1);obj=json.loads(payload);serial_string(payload,obj);concat_string(suffix,[prefix+'\n',payload])
        concat_string(d['readers'][r],[detail['public_frame_value'],suffix])

def at(obj,ptr):
    for k in ptr[1:].split('/') if ptr else []:
        k=k.replace('~1','/').replace('~0','~');obj=obj[int(k)] if isinstance(obj,list) else obj[k]
    return obj
def pointer_escape(k):return str(k).replace('~','~0').replace('/','~1')
def index_document(value):
    chunks=[];bounds={};pos=byte=line=0
    def append(t):
        nonlocal pos,byte,line
        chunks.append(t);pos+=len(t);byte+=len(t.encode());line+=t.count('\n')
    def emit(v,level,ptr):
        start,bs,ls=pos,byte,line+1
        if isinstance(v,dict) and v:
            append('{\n')
            for i,(k,x) in enumerate(v.items()):
                if i:append(',\n')
                append('  '*(level+1)+json.dumps(k,ensure_ascii=False)+': ');emit(x,level+1,ptr+'/'+pointer_escape(k))
            append('\n'+'  '*level+'}')
        elif isinstance(v,list) and v:
            append('[\n')
            for i,x in enumerate(v):
                if i:append(',\n')
                append('  '*(level+1));emit(x,level+1,ptr+'/'+str(i))
            append('\n'+'  '*level+']')
        else:append(json.dumps(v,ensure_ascii=False))
        bounds[ptr]=dict(char_start=start,char_end=pos,utf8_byte_start=bs,utf8_byte_end=byte,line_start=ls,line_end=line+1)
    emit(value,0,'');append('\n');return ''.join(chunks),bounds
INDEX={};documents=[]
for p,d in DOCS.items():
    text,bounds=index_document(d);assert text==(ROOT/p).read_text();INDEX[p]=bounds
    documents.append(dict(id=f'D{len(documents)+1}',path=p,sha256=sha(text),characters=len(text),utf8_bytes=len(text.encode()),serializer=dict(ensure_ascii=False,indent=2,ending='\n'),root=encode(d)))

SEEN_T=set();SEEN_O=set();LINES=[];ROW_INDEX=[]
def expose(v):
    if isinstance(v,dict) and '$t'in v:
        sid=v['$t']
        if sid in SEEN_T:return
        x=STRINGS[sid];recipe=x['recipe']
        for child in recipe.get('concatenate',[]):expose(child)
        if 'json_serialization'in recipe:expose(recipe['json_serialization']['value'])
        SEEN_T.add(sid);LINES.append(dict(t=sid,recipe=recipe))
    elif isinstance(v,dict) and '$o'in v:
        oid=v['$o']
        if oid in SEEN_O:return
        x=CONTAINERS[oid]
        for child in ([pair[1] for pair in x['items']] if x['kind']=='object' else x['items'] if x['kind']=='array' else x['extra_values']if x['kind']=='source_span_object'else []):expose(child)
        SEEN_O.add(oid);LINES.append(dict(o=oid,**{k:v for k,v in x.items() if k!='id'}))
def review_field(p,ptr,role):
    b=INDEX[p][ptr];value=encode(at(DOCS[p],ptr));expose(value);row=dict(field=[next(d['id'] for d in documents if d['path']==p),ptr],span=[b[k]for k in ['char_start','char_end','utf8_byte_start','utf8_byte_end','line_start','line_end']],value=value)
    LINES.append(row);ROW_INDEX.append(dict(document=p,json_pointer=ptr,role=role,line_sequence=len(LINES)))
PUBKEY=['id','source_locus_id','location','C','H','final','alternatives','readers','evidence','qualification','confidence','kind','diff_C','diff_H','physical_count_parent','root_count_basis','count_status','marked_in_H','H_marker_ids','C_doubt_status','C_source_row_ids','C_source_part_ids','original_C_contextual_row_ids','crop','root_ink_choice_applied','root_source_audit_choice_applied','main_approved','log_decision','selected_group_ids','S_id','S_status','source_only_scope','proof_event']
for i,d in enumerate(R['decisions']):
    for k in PUBKEY:
        if k in d:review_field(RPATH,f'/decisions/{i}/{k}','current selected decision / '+k)
    review_field(RPATH,f'/decisions/{i}/H_marker_basis/scope','exact local H apparatus reason')
for coll,keys in [('doubts',['id','decision_id','location','reading','alternatives','confidence','reason','selected_group_ids','main_approved']),('inventory',['sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed','main_approved','selection_status','hand_status','decision_ids','selected_group_ids','source_original_C_inventory_ids','page_order']),('C_source_rows',['source_id','source_parts','selected_outcome','decision_ids']),('abbreviations',['form','expansion','scope','decision_ids','main_approved'])]:
    for i,obj in enumerate(R[coll]):
        for k in keys:
            if k in obj:review_field(RPATH,f'/{coll}/{i}/{k}','current '+coll+' / '+k)
for k in ['notes','counts','count_status','root_approval_status','root_actions_pending','pending_root_decision_ids','workflow_note']:review_field(RPATH,'/'+k,'current record public summary')
public_end=len(LINES);public_fields=len(ROW_INDEX)
# Every remaining field and every source attachment is exposed by each complete document root.
for p in DOCS:review_field(p,'','complete lossless structural document; all prior public values reused exactly')
STRINGS={k:v for k,v in STRINGS.items() if k in SEEN_T}
CONTAINERS={k:v for k,v in CONTAINERS.items() if k in SEEN_O}

prefix='scan025_source_selected_'+VERSION
pages=[]
for phase,a,b in [('public',0,public_end),('structure',public_end,len(LINES))]:
    buffers=[];buf=[];size=0
    for row in LINES[a:b]:
        line=compact(row)+'\n';n=len(line.encode())
        if buf and size+n>28500:buffers.append(''.join(buf));buf=[];size=0
        buf.append(line);size+=n
    if buf:buffers.append(''.join(buf))
    for i,text in enumerate(buffers,1):
        path=f'out/checks/{prefix}_{phase}_review_{i:02d}.jsonl';(ROOT/path).write_text(text)
        pages.append(dict(path=path,phase=phase,sha256=sha(text),utf8_bytes=len(text.encode()),lines=text.count('\n')))
CODEC=dict(scan=25,schema='scan025-selected-lossless-codec-v01',base_pool=dict(path='out/checks/scan025_source_pool_v01.json',sha256=sha((O/'scan025_source_pool_v01.json').read_bytes())),documents=documents,source_table=[{k:v for k,v in s.items()if k not in ['text','newlines','nonascii','extra_bytes']} for s in sources.values()],source_span_object_templates=TEMPLATES,
    rules=dict(t='A sole $t resolves the exact string recipe.',o='A sole $o resolves ordered object items or array items.',strings='Literal, exact already-reviewed source span, base-pool string, ordered concatenation, or deterministic JSON serialization. Roles remain at their original document pointers.',reconstruction='Decode each document root; json.dumps ensure_ascii=False indent=2, plus one newline, exactly reproduces the frozen original bytes.'),
    strings=list(STRINGS.values()),containers=list(CONTAINERS.values()),document_pointer_bounds=INDEX)
CP=f'out/checks/scan025_source_selected_review_pool_{VERSION}.json';(ROOT/CP).write_text(dump(CODEC))
MAN=dict(scan=25,schema='scan025-selected-review-manifest-v01',status='Frozen pending selected record; root final review and approval pending',codec=dict(path=CP,sha256=sha((ROOT/CP).read_bytes())),documents=documents,pages=pages,
    public_review_field_count=public_fields,total_review_field_count=len(ROW_INDEX),string_count=len(STRINGS),container_count=len(CONTAINERS),first_use_strings_exposed=len(SEEN_T),first_use_containers_exposed=len(SEEN_O),
    all_strings_exposed=SEEN_T==set(STRINGS),all_containers_exposed=SEEN_O==set(CONTAINERS),review_order='Read public pages in numerical order, then structural pages in numerical order. t defines an exact string; o defines an ordered container; field gives document ID and original JSON pointer. A span tuple is [char start,end,UTF8 start,end,line start,end]. Dependencies precede referencing fields. Original JSON/source references reuse the already-read frozen source pool.',
    field_index=ROW_INDEX,no_images_or_rendering=True,main_approved=False)
assert MAN['all_strings_exposed'] and MAN['all_containers_exposed']
MANP=f'out/checks/scan025_source_selected_review_manifest_{VERSION}.json';(ROOT/MANP).write_text(dump(MAN))
TABLES=dict(schema=CODEC['schema'],base_pool=CODEC['base_pool'],documents=documents,source_table=CODEC['source_table'],source_span_object_templates=TEMPLATES,codec=MAN['codec'])
(O/f'scan025_source_selected_review_tables_{VERSION}.json').write_text(dump(TABLES))
print(compact(dict(manifest=MANP,manifest_sha256=sha((ROOT/MANP).read_bytes()),codec=CP,codec_bytes=(ROOT/CP).stat().st_size,public_pages=sum(x['phase']=='public'for x in pages),public_bytes=sum(x['utf8_bytes']for x in pages if x['phase']=='public'),structural_pages=sum(x['phase']=='structure'for x in pages),structural_bytes=sum(x['utf8_bytes']for x in pages if x['phase']=='structure'),strings=len(STRINGS),containers=len(CONTAINERS))))
