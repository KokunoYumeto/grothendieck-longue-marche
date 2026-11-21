#!/usr/bin/env python3
"""Finite reader mappings and novel values after root's recorded prior reads."""
from pathlib import Path
from collections import defaultdict
import ast,hashlib,json,re
ROOT=Path(__file__).resolve().parents[2];O=ROOT/'out/checks'
sha=lambda x:hashlib.sha256(x.encode()if isinstance(x,str)else x).hexdigest()
compact=lambda x:json.dumps(x,ensure_ascii=False,separators=(',',':'))
dump=lambda x:json.dumps(x,ensure_ascii=False,indent=2)+'\n'
RP='out/checks/scan025_record_draft.json';MP='out/checks/scan025_final_source_map.json';R=json.loads((ROOT/RP).read_text());M=json.loads((ROOT/MP).read_text())
assert sha((ROOT/RP).read_bytes())=='74abd9b6e3779e1cd7e051027574bfc6436aa62b395737b2a6dbbcdc454768d7'
assert sha((ROOT/MP).read_bytes())=='c4895161d5aa8caf7f3a1767a3de67546f6290ed7d25d92cec937fdc6067849f'
C=json.loads((O/'scan025_source_selected_review_pool_v03.json').read_text());REF=R['provenance']['source_reference_pool'];FR=R['provenance']['complete_own_source_frames']
builder=(O/'scan025_source_build_record.py').read_text();assert sha(builder)=='e0ec9330724767abe6ef10db8a9ca0d851fb3ac5dd17f07989e1d4b2e054d1fe'
assign={n.targets[0].id:n.value for n in ast.parse(builder).body if isinstance(n,ast.Assign)and isinstance(n.targets[0],ast.Name)}
GROUP_META=ast.literal_eval(assign['GROUP_META']);OWN_KEYS=ast.literal_eval(assign['OWN_KEYS'])
TEXT={};JSON={};USED=set()
def text(path):
    if path not in TEXT:TEXT[path]=(ROOT/path).read_text()
    return TEXT[path]
def get(v,p):
    for k in p[1:].split('/')if p else[]:
        k=k.replace('~1','/').replace('~0','~');v=v[int(k)]if isinstance(v,list)else v[k]
    return v
def refvalue(rid,json_value=False):
    USED.add(rid);x=REF[rid];t=text(x['path']);assert sha(t)==x['sha256'];a,b=x['char_start'],x['char_end'];literal=t[a:b];assert literal==x['literal']and sha(literal)==x['body_sha256']
    assert len(t[:a].encode())==x['utf8_byte_start']and len(t[:b].encode())==x['utf8_byte_end']
    if json_value:
        if x['path']not in JSON:JSON[x['path']]=json.loads(t)
        value=get(JSON[x['path']],x['json_pointer']);assert json.loads(literal)==value;return value
    return literal
LOOKUP={(v['path'],v.get('json_pointer')):k for k,v in REF.items()if 'json_pointer'in v}
FRAME_ROWS=[];PARTS={};PART_IDS={};FRAME_TEXT={};GROUP_ROWS={}
for fid,f in FR.items():
    parts=[];source_parts=[];public_parts=[]
    for part in f['parts']:
        original=refvalue(part['source_ref']);source_parts.append(original)
        if part['kind']=='literal_companion':public=original;plan=dict(kind='literal_companion',source_ref=part['source_ref'])
        else:
            metadata=[]
            for item in part['metadata']:
                gid=item['id'];raw=refvalue(item['original_map_ref'],True);meta={k:raw[k]for k in GROUP_META if k in raw}
                meta['exact_source_comments']=[ln for ln in raw['literal_source'].splitlines()if ln.startswith('%')];meta['original_map_ref']=item['original_map_ref'];assert meta==item;metadata.append(meta)
                GROUP_ROWS[gid]=dict(id=gid,original_map_ref=item['original_map_ref'],original_field_order=[k for k in GROUP_META if k in raw],comment_rule='Every original literal_source line beginning with %, in order; no rewriting.')
            public='[Reader '+f['reader']+' complete own graphical group '+part['group_ids'][0]+'; editorial descriptor of original fields: '+compact(metadata)+']'
            plan=dict(kind='complete_own_group_descriptor',source_ref=part['source_ref'],group_ids=part['group_ids'])
        assert public==part['public_literal'];public_parts.append(public);key=compact(plan)
        if key not in PART_IDS:
            pid=f'FP{len(PARTS)+1:03d}';PART_IDS[key]=pid;PARTS[pid]=dict(id=pid,**plan,public_sha256=sha(public),source_sha256=sha(original))
        parts.append(PART_IDS[key])
    inventory=[]
    for rid in f['original_inventory_refs']:inventory.append(dict(original_json_pointer=REF[rid]['json_pointer'],value=refvalue(rid,True)))
    reconstructed='Reader '+f['reader']+' complete own '+f['scope']+' frame, in original source order. Bracketed graphical descriptors below contain only this reader\'s own fields; every replaced source group is exactly recoverable from its source reference.\n'+''.join(public_parts)+'\nComplete own inventory fields in this frame, with their original hand and local candidate scopes:\n'+compact(inventory)
    assert reconstructed==f['public'];assert ''.join(source_parts)==refvalue(f['complete_source_ref']);FRAME_TEXT[fid]=reconstructed
    FRAME_ROWS.append(dict(id=fid,reader=f['reader'],scope=f['scope'],complete_source_ref=f['complete_source_ref'],ordered_part_ids=parts,original_inventory_refs=f['original_inventory_refs'],group_ids=f['group_ids'],public_sha256=sha(reconstructed),complete_source_sha256=f['source_reconstruction_sha256']))

SUFFIXES={};SUFFIX_IDS={};ALIASES={};ROW_MAPPINGS=[]
for doc,root in [('record',R),('map',M)]:
    collections=['decisions','source_locus_coverage']if doc=='record'else['source_locus_coverage']
    for coll in collections:
        for i,row in enumerate(root[coll]):
            for reader,detail in row['reader_source_details'].items():
                suffix=detail['public_local_suffix'];prefix,payload=suffix.rsplit('\n',1);local=json.loads(payload);plans=[];reconstructed_local=[]
                reportpath=f'out/readers/025/{reader}/report.json'
                for item in local:
                    ptr=item['original_json_pointer'];rid=LOOKUP[(reportpath,ptr)];raw=refvalue(rid,True)
                    if 'original_row_id'in item:
                        fields={k:v for k,v in raw.items()if k in OWN_KEYS};rebuilt=dict(original_row_id=item['original_row_id'],original_json_pointer=ptr,own_proposal_fields=fields);kind='own main report/doubt fields'
                    else:
                        excluded={'raw_source_row','literal_source_row','original_row_literal','source_file','source_heading'};fields={k:v for k,v in raw.items()if k not in excluded};rebuilt=dict(original_C_row_identity=item['original_C_row_identity'],original_json_pointer=ptr,original_reader_scope_and_status_fields=fields);kind='this reader original canonical C scope/status report'
                    assert rebuilt==item;reconstructed_local.append(rebuilt);plans.append(dict(kind=kind,source_ref=rid,original_identity=item.get('original_row_id',item.get('original_C_row_identity')),field_order=list(fields)))
                rebuilt_suffix=prefix+'\n'+compact(reconstructed_local);assert rebuilt_suffix==suffix
                if suffix not in SUFFIX_IDS:
                    sid=f'LS{len(SUFFIXES)+1:03d}';SUFFIX_IDS[suffix]=sid;SUFFIXES[sid]=dict(id=sid,prefix_literal=prefix+'\n',ordered_local_projections=plans,public_sha256=sha(suffix))
                fid=detail['complete_own_frame_id'];sid=SUFFIX_IDS[suffix];full=FRAME_TEXT[fid]+suffix;assert full==row['readers'][reader]
                key=(reader,fid,sid);pointer=f'/{coll}/{i}/readers/{reader}'
                if key not in ALIASES:ALIASES[key]=dict(reader=reader,frame_id=fid,suffix_id=sid,public_sha256=sha(full),occurrences=[])
                ALIASES[key]['occurrences'].append(dict(document=doc,json_pointer=pointer,local_details_pointer=f'/{coll}/{i}/reader_source_details/{reader}'))
                ROW_MAPPINGS.append(dict(document=doc,row_id=row.get('id',row['source_locus_id']),source_locus_id=row['source_locus_id'],reader=reader,frame=fid,suffix=sid))

# Exact references are displayed once; literals resolve to already-read originals.
REFERENCE_ROWS=[]
for rid in sorted(USED):
    x=REF[rid];REFERENCE_ROWS.append(dict(id=rid,path=x['path'],sha256=x['sha256'],bounds=[x[k]for k in ['char_start','char_end','utf8_byte_start','utf8_byte_end','line_start','line_end']],literal_sha256=x['body_sha256'],json_pointer=x.get('json_pointer'),literal_recipe='Exact source-file slice at the declared character bounds.'))

# Deduplicate values already covered by the precise root public-read bookmark.
KNOWN={}
def remember(value,path):
    if isinstance(value,str):KNOWN.setdefault(value,path)
    elif isinstance(value,list):
        for i,v in enumerate(value):remember(v,path+'/'+str(i))
    elif isinstance(value,dict):
        for k,v in value.items():remember(v,path+'/'+k.replace('~','~0').replace('/','~1'))
bookmark=json.loads((O/'scan025_root_public_record_preliminary_read.json').read_text())
keys=bookmark['physical_decision_keys_fully_read']
for i,d in enumerate(R['decisions']):
    for k in keys+['S_id','S_status','source_only_scope','proof_event','qualification','count_status','root_ink_choice_applied','root_source_audit_choice_applied','main_approved','log_decision']:
        if k in d:remember(d[k],f'/decisions/{i}/{k}')
for coll in ['doubts','inventory','C_source_rows','abbreviations']:
    for i,row in enumerate(R[coll]):
        for k,v in row.items():
            if k not in ['source_attachments','root_crop_evidence','provenance','reader_reported_scopes','original_row_reference','root_authority','raw_reader_proposal_refs','H_supplied_letters_ref']:remember(v,f'/{coll}/{i}/{k}')
for k in ['notes','workflow_note','brief_version','counts','count_status','root_approval_status','root_actions_pending','pending_root_decision_ids','source_attachment_status']:remember(R[k],'/'+k)
NOVEL=[];KNOWN_ALIASES=[]
for s in C['strings']:
    if 'literal'not in s['recipe']:continue
    v=s['recipe']['literal']
    if v in KNOWN:KNOWN_ALIASES.append(dict(string_id=s['id'],already_read_record_json_pointer=KNOWN[v],sha256=s['sha256']))
    else:NOVEL.append(dict(string_id=s['id'],literal=v,sha256=s['sha256']))

# All distinct selected source spans, with every current occurrence pointer.
SELECTED={}
def scan_refs(v,doc,path=''):
    if isinstance(v,dict):
        p=v.get('workspace_path')or v.get('path')or v.get('source_path')
        if p in ['out/checks/scan025_final_draft.tex','checks/scan025_final_draft.tex']and 'char_start'in v:
            a=v['char_start'];b=v.get('char_end',v.get('char_end_exclusive'));key=(a,b);lit=v.get('literal');page=text('out/checks/scan025_final_draft.tex');assert lit==page[a:b]
            if key not in SELECTED:SELECTED[key]=dict(bounds=[a,b,len(page[:a].encode()),len(page[:b].encode()),page.count('\n',0,a)+1,page.count('\n',0,max(a,b-1))+1],literal_sha256=sha(lit),occurrences=[])
            SELECTED[key]['occurrences'].append(dict(document=doc,json_pointer=path))
        for k,x in v.items():scan_refs(x,doc,path+'/'+k.replace('~','~0').replace('/','~1'))
    elif isinstance(v,list):
        for i,x in enumerate(v):scan_refs(x,doc,path+'/'+str(i))
scan_refs(R,'record');scan_refs(M,'map')
rows=[dict(type='group_metadata_rule',**v)for v in GROUP_ROWS.values()]+[dict(type='part',**v)for v in PARTS.values()]+[dict(type='frame',**v)for v in FRAME_ROWS]+[dict(type='local_suffix',**v)for v in SUFFIXES.values()]+[dict(type='reader_aliases',**v)for v in ALIASES.values()]
groups=[('reader_mapping',rows),('source_references',[dict(type='exact_original_reference',**v)for v in REFERENCE_ROWS]),('novel_metadata',[dict(type='first_use_novel_literal',**v)for v in NOVEL]),('selected_bindings',[dict(type='selected_span',**v)for k,v in sorted(SELECTED.items())])]
pages=[]
for kind,items in groups:
    buffers=[];buf=[];size=0
    for item in items:
        line=compact(item)+'\n'
        if buf and size+len(line.encode())>26500:buffers.append(''.join(buf));buf=[];size=0
        buf.append(line);size+=len(line.encode())
    if buf:buffers.append(''.join(buf))
    for i,content in enumerate(buffers,1):
        path=f'out/checks/scan025_source_compact_{kind}_v03_{i:02d}.jsonl';(ROOT/path).write_text(content);pages.append(dict(path=path,phase=kind,sha256=sha(content),bytes=len(content.encode()),lines=content.count('\n')))
aliaspath='out/checks/scan025_source_compact_known_value_aliases_v03.json';(ROOT/aliaspath).write_text(dump(KNOWN_ALIASES))
result=dict(scan=25,status='Finite mappings reconstructed every complete public reader field from exact original sources; no source or selected artifact changed',record=dict(path=RP,sha256=sha((ROOT/RP).read_bytes())),source_map=dict(path=MP,sha256=sha((ROOT/MP).read_bytes())),
    builder=dict(path='out/checks/scan025_source_build_record.py',sha256=sha(builder),root_complete_read=True),prior_root_public_read=dict(path='out/checks/scan025_root_public_record_preliminary_read.json',sha256=sha((O/'scan025_root_public_record_preliminary_read.json').read_bytes())),
    bounded_root_closure=dict(path='out/checks/scan025_source_record_closure_v03.json',sha256=sha((O/'scan025_source_record_closure_v03.json').read_bytes())),
    full_codec=dict(path='out/checks/scan025_source_selected_review_pool_v03.json',sha256=sha((O/'scan025_source_selected_review_pool_v03.json').read_bytes())),
    counts=dict(frames=len(FRAME_ROWS),unique_parts=len(PARTS),original_group_metadata_rules=len(GROUP_ROWS),unique_local_suffixes=len(SUFFIXES),unique_reader_alias_groups=len(ALIASES),current_reader_field_occurrences=len(ROW_MAPPINGS),exact_original_source_references=len(REFERENCE_ROWS),novel_literal_values=len(NOVEL),already_read_literal_aliases=len(KNOWN_ALIASES),unique_selected_source_spans=len(SELECTED)),
    reader_prefix_and_suffix_reconstruction_passed=True,all_full_original_frames_reconstructed_exactly=True,all_own_inventory_fields_reconstructed_exactly=True,all_original_own_group_fields_and_comments_reconstructed_exactly=True,all_own_main_and_canonical_report_subscopes_reconstructed_exactly=True,
    new_value_coverage='Every direct literal string in the full codec is either printed once in novel_metadata or mapped exactly to an already-read current public value. Other string recipes resolve exact already-read original values/spans or the completely verified reader composition templates.',
    known_value_aliases=dict(path=aliaspath,sha256=sha((ROOT/aliaspath).read_bytes())),pages=pages,review_order='reader_mapping, source_references, novel_metadata, selected_bindings; each phase in numerical order. The fully read builder and decoder define the exact templates and inverse rules.',main_approved=False)
path=O/'scan025_source_compact_review_manifest_v03.json';path.write_text(dump(result));print(dump({'manifest':'out/checks/'+path.name,'sha256':sha(path.read_bytes()),'counts':result['counts'],'page_counts':{k:sum(x['phase']==k for x in pages)for k,_ in groups},'total_bytes':sum(x['bytes']for x in pages)}))
