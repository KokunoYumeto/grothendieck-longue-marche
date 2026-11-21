"""Narrow replay of scan024 alternatives-only closure; text/source metadata only."""
from pathlib import Path
import copy,hashlib,json,re
BASE=Path('out/checks');CACHE={};ERRORS=[];REFS=0
def tx(p):
    p=str(p)
    if p not in CACHE:CACHE[p]=Path(p).read_bytes().decode('utf-8')
    return CACHE[p]
def sha(t):return hashlib.sha256(t.encode('utf-8')).hexdigest()
def js(p):return json.loads(tx(p))
def ck(ok,label):
    if not ok:ERRORS.append(label)
def bits(p):return [k.replace('~1','/').replace('~0','~') for k in p.split('/')[1:]]
def ptr(o,p):
    for k in bits(p):o=o[int(k)] if isinstance(o,list) else o[k]
    return o
def setv(o,p,v,delete=False):
    q=bits(p)
    for k in q[:-1]:o=o[int(k)] if isinstance(o,list) else o[k]
    k=int(q[-1]) if isinstance(o,list) else q[-1]
    if delete:del o[k]
    else:o[k]=copy.deepcopy(v)
def diff(a,b,p=''):
    if type(a)!=type(b):return [p]
    if isinstance(a,dict):
        out=[]
        for k in a.keys()|b.keys():
            np=p+'/'+k.replace('~','~0').replace('/','~1')
            out.extend([np] if k not in a or k not in b else diff(a[k],b[k],np))
        return out
    if isinstance(a,list):
        if len(a)!=len(b):return [p]
        return [v for i,(x,y) in enumerate(zip(a,b)) for v in diff(x,y,p+'/'+str(i))]
    return [] if a==b else [p]
def exact(f,v):
    global REFS
    t=tx(f['path']);s=t[f['char_start']:f['char_end']]
    ck(sha(t)==f['sha256'],'ref_file:'+f['json_pointer'])
    ck(sha(s)==f['body_sha256'],'ref_body:'+f['json_pointer'])
    ck(json.loads(s)==v,'ref_value:'+f['json_pointer']);REFS+=1
C=js(BASE/'scan024_source_bounded_closure_v02.json')
A=js(C['authority']['path']);O=js(C['initial_record']['path']);N=js(C['current_record']['path'])
for k in ['authority','initial_record','current_record','previous_closure']:
    ck(sha(tx(C[k]['path']))==C[k]['sha256'],'binding:'+k)
ck(set(diff(O,N))=={x['path'] for x in C['changes']},'complete_change_set')
forward=copy.deepcopy(O);inverse=copy.deepcopy(N)
for x in C['changes']:
    p=x['path'];new=x['new_value'];old=x.get('old_value')
    ck(ptr(N,p)==new,'new_value:'+p)
    if x.get('old_present',True):
        ck(ptr(O,p)==old,'old_value:'+p);exact(x['old_exact_value'],old)
        setv(inverse,p,old)
    else:
        ck(p=='/root_doubt_alternatives_authorization','only_addition');setv(inverse,p,None,delete=True)
    exact(x['new_exact_value'],new);setv(forward,p,new)
    if 'root_authority_pointer' in x:ck(ptr(A,x['root_authority_pointer'])==new,'authority_value:'+p)
ck(forward==N and inverse==O,'structural_forward_inverse')
ck(json.dumps(forward,ensure_ascii=False,indent=2)+'\n'==tx(C['current_record']['path']),'forward_exact_UTF8')
ck(json.dumps(inverse,ensure_ascii=False,indent=2)+'\n'==tx(C['initial_record']['path']),'inverse_exact_UTF8')
D={d['id']:d for d in N['decisions']}
ck(set(A['alternatives_by_doubt_id'])=={x['id'] for x in N['doubts']},'all39_ids')
for q in N['doubts']:
    expected=A['alternatives_by_doubt_id'][q['id']]
    ck(q['alternatives']==expected,'doubt_alternatives:'+q['id'])
    ck(D[q['decision_id']]['alternatives']==expected,'decision_alternatives:'+q['id'])
ck(sum(bool(q['alternatives']) for q in N['doubts'])==29,'nonempty29')
ck(O['counts']==N['counts'],'counts_unchanged')
release=js(BASE/'scan024_source_record_release_v02.json')
for path,h in release['files'].items():ck(sha(tx(path))==h,'release:'+path)
P0=js(BASE/'scan024_source_public_projection.json');P1=js(BASE/'scan024_source_public_projection_v02.json')
PD=js(BASE/'scan024_source_public_projection_delta_v02.json')
ck(all(P1['values'][k]==v for k,v in P0['values'].items()),'prior950_values_unchanged')
extra={k:v for k,v in P1['values'].items() if k not in P0['values']}
ck(extra==PD['new_pool_values'] and len(extra)==49,'new49_values_exact')
paths=diff(P0['public_fields'],P1['public_fields'])
ck(len(paths)==58 and all(re.fullmatch(r'/(decisions|doubts)/\d+/alternatives',p) for p in paths),'only58_public_bindings')
def restore(x):
    if isinstance(x,dict) and set(x)=={'concat'}:return ''.join(P1['values'][k] for k in x['concat'])
    if isinstance(x,list):return [restore(v) for v in x]
    if isinstance(x,dict):return {k:restore(v) for k,v in x.items()}
    return x
for p in paths:
    ck(restore(ptr(P1['public_fields'],p))==ptr(N,p),'public_alternatives_exact:'+p)
ck(P1['record_sha256']==C['current_record']['sha256'],'projection_record_hash')
ck(PD['prior_projection']['sha256']==sha(tx(PD['prior_projection']['path'])),'prior_projection_binding')
ck(PD['new_projection']['sha256']==sha(tx(PD['new_projection']['path'])),'new_projection_binding')
out=BASE/'scan024_qa_bounded_closure_v02.json'
report=dict(scan=24,scope='Alternatives-only changed-field replay, following completed first closure; no page/source rerun or ink/hand/math decision.',
    closure=dict(path=str(BASE/'scan024_source_bounded_closure_v02.json'),sha256=sha(tx(BASE/'scan024_source_bounded_closure_v02.json'))),
    current_record=C['current_record'],authority=C['authority'],exact_changed_value_refs=REFS,changed_arrays=58,added_authority_bindings=1,
    mapped_doubts=39,nonempty_alternatives=29,prior_pool_values_preserved=len(P0['values']),added_pool_values=len(extra),errors=ERRORS,
    counts=N['counts'],root_approval=False)
if out.exists():raise FileExistsError(str(out))
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(path=str(out),sha256=sha(tx(out)),exact_changed_value_refs=REFS,errors=ERRORS),ensure_ascii=False))
