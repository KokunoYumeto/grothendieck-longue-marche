"""Replay only the released scan024 bounded field changes; source-only QA."""
from pathlib import Path
import collections,copy,hashlib,json

BASE=Path('out/checks')
CACHE={}
ERRORS=[]
COUNTS=collections.Counter()

def text(p):
    p=str(p)
    if Path(p).suffix.lower() in {'.png','.jpg','.jpeg','.pdf'}:raise ValueError('Text only')
    if p not in CACHE:CACHE[p]=Path(p).read_bytes().decode('utf-8')
    return CACHE[p]
def sha(t):return hashlib.sha256(t.encode('utf-8')).hexdigest()
def js(p):return json.loads(text(p))
def ck(ok,label):
    if not ok:ERRORS.append(label)
def bits(ptr):return [x.replace('~1','/').replace('~0','~') for x in ptr.split('/')[1:]]
def ptr(obj,p):
    for bit in bits(p):obj=obj[int(bit)] if isinstance(obj,list) else obj[bit]
    return obj
def present(obj,p):
    try:return True,ptr(obj,p)
    except (KeyError,IndexError):return False,None
def put(obj,p,exists,v):
    q=bits(p);base=obj
    for x in q[:-1]:base=base[int(x)] if isinstance(base,list) else base[x]
    x=int(q[-1]) if isinstance(base,list) else q[-1]
    if exists:base[x]=copy.deepcopy(v)
    else:del base[x]
def diff(a,b,p=''):
    if type(a)!=type(b):return [p]
    if isinstance(a,dict):
        out=[]
        for k in a.keys()|b.keys():
            path=p+'/'+k.replace('~','~0').replace('/','~1')
            out.extend([path] if k not in a or k not in b else diff(a[k],b[k],path))
        return out
    if isinstance(a,list):
        if len(a)!=len(b):return [p]
        return [z for i,(x,y) in enumerate(zip(a,b)) for z in diff(x,y,p+'/'+str(i))]
    return [] if a==b else [p]
def ordered_like(value,model):
    if isinstance(model,dict):return {k:ordered_like(value[k],v) for k,v in model.items()}
    if isinstance(model,list):return [ordered_like(v,m) for v,m in zip(value,model)]
    return value
def exact_ref(f,expected):
    if f is None:return
    t=text(f['path']);a,b=f['char_start'],f['char_end'];body=t[a:b]
    ck(sha(t)==f['sha256'],'ref_file:'+f['json_pointer'])
    ck(sha(body)==f['body_sha256'],'ref_body:'+f['json_pointer'])
    ck(len(t[:a].encode('utf-8'))==f['utf8_byte_start'],'ref_byte_start:'+f['json_pointer'])
    ck(len(t[:b].encode('utf-8'))==f['utf8_byte_end'],'ref_byte_end:'+f['json_pointer'])
    ck(json.loads(body)==expected,'ref_value:'+f['json_pointer'])
    COUNTS['exact_changed_value_refs']+=1
def replay(label,meta,old_binding,new_binding,changes):
    oldtext,newtext=text(old_binding['path']),text(new_binding['path'])
    ck(sha(oldtext)==old_binding['sha256'],label+':old_hash')
    ck(sha(newtext)==new_binding['sha256'],label+':new_hash')
    old,new=json.loads(oldtext),json.loads(newtext)
    ck(set(diff(old,new))=={x['path'] for x in changes},label+':complete_delta_set')
    forward=copy.deepcopy(old);inverse=copy.deepcopy(new)
    for c in changes:
        path=c['path'];op,ov=present(old,path);np,nv=present(new,path)
        ck(op==c['old_present'] and np==c['new_present'],label+':presence:'+path)
        if 'old_value' in c:ck(c['old_value']==ov,label+':inline_old:'+path)
        if 'new_value' in c:ck(c['new_value']==nv,label+':inline_new:'+path)
        if op:exact_ref(c.get('old_exact_value'),ov)
        if np:exact_ref(c.get('new_exact_value'),nv)
        put(forward,path,np,nv)
        put(inverse,path,op,ov)
    ck(forward==new,label+':forward_structure')
    ck(inverse==old,label+':inverse_structure')
    ck(json.dumps(ordered_like(forward,new),ensure_ascii=False,indent=2)+'\n'==newtext,label+':forward_UTF8')
    ck(json.dumps(ordered_like(inverse,old),ensure_ascii=False,indent=2)+'\n'==oldtext,label+':inverse_UTF8')
    COUNTS[label+'_changed_fields']=len(changes)
    return old,new

C=js(BASE/'scan024_source_bounded_closure_v01.json')
O,N=replay('record',C,C['initial_record'],C['current_record'],C['record_changes'])
OM,NM=replay('map',C,C['initial_map'],C['current_map'],C['map_changes'])
ck(sha(text(C['unchanged_page']['path']))==C['unchanged_page']['sha256'],'page_unchanged')
for a in C['authorities']:ck(sha(text(a['path']))==a['sha256'],'authority:'+a['path'])
ck(O['counts']==N['counts'],'counts_unchanged')
ck(O['check_events']==N['check_events']==[],'events_empty')
ck(N['brief_version']=='v22 / source-record v07','brief_label')
D={d['id']:d for d in N['decisions']}
K=js(BASE/'scan024_root_public_kind_authorization.json')
for od,nd in zip(O['decisions'],N['decisions']):
    did=nd['id']
    for k in ['id','source_locus_id','H','evidence','confidence','diff_C','diff_H','physical_count_parent','root_count_basis','qualification','marked_in_H','reader_source_details']:
        if k in od:ck(od[k]==nd[k],'unchanged_'+k+':'+did)
    if did!='SRC024-L64':ck(od['C']==nd['C'],'unchanged_C:'+did)
    if did not in ['SRC024-L38','SRC024-L39']:ck(od['final']==nd['final'],'unchanged_final:'+did)
    ck(nd['kind']==K['kind_by_decision_id'].get(did,'other'),'kind:'+did)
ck(D['SRC024-L64']['C']==K['C64_field_repair']['new_value'],'C64_exact_authority')

# Each cited omission is now printed with its own exact source scope.
F=js(BASE/'scan024_qa_coverage_followup_v01.json')
missing=next(f for f in F['findings'] if f['id']=='QA024-F03')['components']
for x in missing:
    s=D[x['local_decision_id']]['readers'][x['reader']]
    r=x['source_reference'];old=ptr(js(r['source_path']),r['json_pointer'])
    ck(x['inventory_id'] in s and r['source_path']+'#'+r['json_pointer'] in s,'restored_inventory_identity:'+x['inventory_id'])
    for k,v in x['source_fields'].items():
        ck(json.dumps({k:v},ensure_ascii=False,separators=(',',':'))[1:-1] in s,'restored_inventory_field:'+x['inventory_id']+'/'+k)
    COUNTS['restored_reported_inventory_hand_scopes']+=1
for role in ['A','C']:
    report=js(f'out/readers/024/{role}/report.json')
    for d in N['decisions'][:65]:
        details=d['reader_source_details'][role]
        pool=N['provenance']['source_reference_pool']
        for rid in details['raw_own_difference_refs']+details['raw_own_doubt_refs']:
            f=pool[rid]['exact_source_ref'];v=ptr(report,f['json_pointer'])
            for k in ['mark_hand','mark_role','separate_scope','hand','hand_scope','role','attachment','surface_origin','role_confidence']:
                if k in v:
                    needle=json.dumps({k:v[k]},ensure_ascii=False,separators=(',',':'))[1:-1]
                    ck(needle in d['readers'][role],'own_local_field:'+d['id']+'/'+role+'/'+rid+'/'+k)

ck('undetermined hand specifically in the independent-run candidate' in D['SRC024-L38']['final'],'L38_narrow_hand')
ck('his-hand attribution' in D['SRC024-L39']['final'] and 'undetermined' not in D['SRC024-L39']['final'],'L39_selected_hand')
for g in N['selected_graphical_groups']:
    for did,v in g['selected_readings'].items():
        if did in ['SRC024-L38','SRC024-L39']:ck(v==D[did]['final'],'selected_group_mirror:'+g['id']+'/'+did)
for cov in N['source_locus_coverage']:
    for did,v in cov['selected_readings'].items():
        if did in ['SRC024-L38','SRC024-L39']:ck(v==D[did]['final'],'coverage_mirror:'+did)
for q in N['doubts']:
    if q['decision_id'] in ['SRC024-L38','SRC024-L39']:
        ck(q['reading']==D[q['decision_id']]['final'],'doubt_mirror:'+q['id'])
        ck(D[q['decision_id']]['final'] in q['reason'],'doubt_reason_scope:'+q['id'])
for ident in ['A024.30','024.C.31a','A024.44','A024.47']:
    inv=next(x for x in N['inventory'] if x['element']==ident)
    ck(inv['hand']=='his hand','inventory_hand:'+ident)
for ident,gid in [('024.C.30a','A024-G13'),('024.C.31a','A024-G14')]:
    inv=next(x for x in N['inventory'] if x['element']==ident)
    ck(inv['position']=='detached upper run of selected '+gid,'inventory_position:'+ident)
for old,new in zip(O['C_source_rows'],N['C_source_rows']):
    ck(old['source_id']==new['source_id'] and old['literal']==new['literal'],'C_identity:'+old['source_id'])
    for op,np in zip(old['source_parts'],new['source_parts']):
        ck(op['part_id']==np['part_id'] and op['selected_outcome']==np['selected_outcome'],'C_part_identity:'+op['part_id'])
        ck(np['decision_status']=='Root selected '+np['selected_outcome']+'; final record approval pending.','C_status:'+op['part_id'])
        ck(np['original_source_decision_status']==op['decision_status'],'C_history:'+op['part_id'])
        ck(np['main_approved'] is False,'C_approval:'+op['part_id'])

REPORT=dict(scan=24,scope='Changed fields only: first bounded closure. No broad page/source replay, images, rendering, compilation or ink/math decisions.',
    closure=dict(path=str(BASE/'scan024_source_bounded_closure_v01.json'),sha256=sha(text(BASE/'scan024_source_bounded_closure_v01.json'))),
    inputs={x['path']:x['sha256'] for x in [C['initial_record'],C['current_record'],C['initial_map'],C['current_map'],C['unchanged_page']]},
    counters=dict(COUNTS),errors=ERRORS,manual_review='Read new L38/L39 finals, own-reader hand additions, current statuses, position labels, brief label, C64 editorial label, kind authority, notes disclosure and candidate ordering. No additional source defect found in those values.',
    counts=N['counts'],root_approval=False,second_alternatives_closure_pending=True)
out=BASE/'scan024_qa_bounded_closure_v01.json'
if out.exists():raise FileExistsError(str(out))
out.write_text(json.dumps(REPORT,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(path=str(out),sha256=sha(text(out)),counters=dict(COUNTS),errors=ERRORS),ensure_ascii=False))
