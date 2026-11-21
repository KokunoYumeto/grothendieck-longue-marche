"""Root-authorized exact Alternatives-column patch, with preserved pool IDs."""
from pathlib import Path
import json,hashlib,copy,sys
sys.dont_write_bytecode=True
BASE=Path('/workspace/scratch/94548b74fbe0');D=BASE/'out/checks'
sys.path.insert(0,str(D));import scan024_source_support as support
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes) else x.encode()).hexdigest()
def read(p):return (BASE/p).read_text()
def load(p):return json.loads(read(p))
def save(p,v):
    s=json.dumps(v,ensure_ascii=False,indent=2)+'\n';(BASE/p).write_text(s);return sha(s)
OLD='out/checks/scan024_source_record_repaired_v01.json';CAN='out/checks/scan024_record_draft.json';NEW='out/checks/scan024_source_record_repaired_v02.json'
AUTH='out/checks/scan024_root_doubt_alternatives_authorization.json'
assert sha(read(OLD))=='20111253e313ed1a710a64c002bf9d547fa5bf31705545c07d58704803a20df0'
assert read(CAN)==read(OLD)
assert sha(read(AUTH))=='7ab2ffb4e0b15a03981bea6ce98225e7f00825240eab125a27b17221f3354733'
assert not (BASE/NEW).exists()
old=load(OLD);new=copy.deepcopy(old);a=load(AUTH);values=a['alternatives_by_doubt_id'];changes=[]
byid={d['id']:(i,d) for i,d in enumerate(new['decisions'])}
for i,d in enumerate(new['doubts']):
    v=values[d['id']];di,decision=byid[d['decision_id']]
    for path,obj in [(f'/doubts/{i}/alternatives',d),(f'/decisions/{di}/alternatives',decision)]:
        before=copy.deepcopy(obj['alternatives']);obj['alternatives']=copy.deepcopy(v)
        if before!=v:changes.append(dict(path=path,old_value=before,new_value=v,semantic_role='current selected non-primary alternatives',root_authority_pointer='/alternatives_by_doubt_id/'+d['id']))
new['root_doubt_alternatives_authorization']=dict(path=AUTH,sha256=sha(read(AUTH)),scope=a['scope'],common_scope=a['common_scope'],empty_list_scope=a['empty_list_scope'])
changes.append(dict(path='/root_doubt_alternatives_authorization',operation='add',old_present=False,new_value=new['root_doubt_alternatives_authorization'],semantic_role='exact root authority binding'))
for x,y in zip(old['decisions'],new['decisions']):
    for k in x:
        if k!='alternatives':assert x[k]==y[k],(x['id'],k)
for x,y in zip(old['doubts'],new['doubts']):
    for k in x:
        if k!='alternatives':assert x[k]==y[k],(x['id'],k)
for k in old:
    if k not in ['decisions','doubts']:assert old[k]==new[k],k
newhash=save(NEW,new);assert save(CAN,new)==newhash
oldprojection='out/checks/scan024_source_public_projection.json'
p=load(oldprojection);assert p['record_sha256']==sha(read(OLD))
prior_values=copy.deepcopy(p['values']);pool=p['values'];reverse={json.dumps(v,ensure_ascii=False,sort_keys=True):k for k,v in pool.items()}
def intern(v):
    key=json.dumps(v,ensure_ascii=False,sort_keys=True)
    if key not in reverse:
        rid=f'V{len(pool)+1:04d}';reverse[key]=rid;pool[rid]=v
    return {'concat':[reverse[key]]}
for i,d in enumerate(new['decisions']):p['public_fields']['decisions'][i]['alternatives']=[intern(x) for x in d['alternatives']]
for i,d in enumerate(new['doubts']):p['public_fields']['doubts'][i]['alternatives']=[intern(x) for x in d['alternatives']]
p.update(record_path=NEW,canonical_record_path=CAN,record_sha256=newhash,predecessor_projection=dict(path=oldprojection,sha256=sha(read(oldprojection))),pool_identity_rule='All prior pool IDs/values remain unchanged; only exact root-authorized alternatives add values and current alternative-field bindings.')
assert all(pool[k]==v for k,v in prior_values.items())
def restore(x):
    if isinstance(x,dict) and set(x)=={'concat'}:return ''.join(pool[k] for k in x['concat'])
    if isinstance(x,dict):return {k:restore(v) for k,v in x.items()}
    if isinstance(x,list):return [restore(v) for v in x]
    return x
restored=restore(p['public_fields'])
pubkeys=p['public_field_selection']
assert restored['decisions']==[{k:d[k] for k in pubkeys if k in d} for d in new['decisions']]
for i,d in enumerate(new['doubts']):assert restored['doubts'][i]=={k:d[k] for k in restored['doubts'][i]}
for i,x in enumerate(new['inventory']):assert restored['inventory'][i]=={k:x[k] for k in restored['inventory'][i]}
assert restored['notes']==new['notes'] and restored['counts']==new['counts']
P='out/checks/scan024_source_public_projection_v02.json';ph=save(P,p)
lines=[json.dumps(dict(kind='metadata',**{k:v for k,v in p.items() if k not in ['values','public_fields']}),ensure_ascii=False)]
lines.extend(json.dumps(dict(kind='value',id=k,value=v),ensure_ascii=False) for k,v in pool.items())
for section,items in p['public_fields'].items():
    if isinstance(items,list):lines.extend(json.dumps(dict(kind='public_row',section=section,index=i,value=v),ensure_ascii=False) for i,v in enumerate(items))
    else:lines.append(json.dumps(dict(kind='public_field',section=section,value=items),ensure_ascii=False))
(D/'scan024_source_public_projection_v02.jsonl').write_text('\n'.join(lines)+'\n')
delta=dict(scan=24,prior_projection=dict(path=oldprojection,sha256=sha(read(oldprojection))),new_projection=dict(path=P,sha256=ph),preserved_pool_ids=len(prior_values),new_pool_values={k:v for k,v in pool.items() if k not in prior_values},new_alternative_bindings=dict(decisions={d['id']:p['public_fields']['decisions'][i]['alternatives'] for i,d in enumerate(new['decisions']) if any(c['path']==f'/decisions/{i}/alternatives' for c in changes)},doubts={d['id']:p['public_fields']['doubts'][i]['alternatives'] for i,d in enumerate(new['doubts']) if any(c['path']==f'/doubts/{i}/alternatives' for c in changes)}),all_other_public_bindings_unchanged=True)
save('out/checks/scan024_source_public_projection_delta_v02.json',delta)
# Exact forward/inverse replay uses only the recorded current-role changes.
def setpath(obj,path,value,remove=False):
    keys=path.split('/')[1:]
    for k in keys[:-1]:obj=obj[int(k)] if isinstance(obj,list) else obj[k]
    k=keys[-1]
    if remove:del obj[k]
    elif isinstance(obj,list):obj[int(k)]=copy.deepcopy(value)
    else:obj[k]=copy.deepcopy(value)
fwd=copy.deepcopy(old)
for c in changes:setpath(fwd,c['path'],c['new_value'])
assert json.dumps(fwd,ensure_ascii=False,indent=2)+'\n'==read(NEW)
inv=copy.deepcopy(new)
for c in reversed(changes):setpath(inv,c['path'],c.get('old_value'),remove=c.get('operation')=='add')
assert json.dumps(inv,ensure_ascii=False,indent=2)+'\n'==read(OLD)
oldsp=support.JSONSpans(read(OLD));newsp=support.JSONSpans(read(NEW))
for c in changes:
    for label,path,sp in [('old',OLD,oldsp),('new',NEW,newsp)]:
        if c['path'] not in sp.spans:continue
        st,en=sp.spans[c['path']];c[label+'_exact_value']=dict(path=path,sha256=sha(read(path)),json_pointer=c['path'],char_start=st,char_end=en,body_sha256=sha(read(path)[st:en]))
closure=dict(scan=24,source_only=True,main_approved=False,authority=dict(path=AUTH,sha256=sha(read(AUTH))),initial_record=dict(path=OLD,sha256=sha(read(OLD))),current_record=dict(path=NEW,canonical_path=CAN,sha256=newhash),previous_closure=dict(path='out/checks/scan024_source_bounded_closure_v01.json',sha256=sha(read('out/checks/scan024_source_bounded_closure_v01.json'))),changes=changes,change_count=len(changes),nonempty_doubt_alternatives=sum(bool(x['alternatives']) for x in new['doubts']),all39_authorized_rows_applied=True,exact_forward_UTF8=True,exact_inverse_UTF8=True,all_finals_readings_reasons_evidence_hands_and_counts_unchanged=True,page_unchanged=True,map_unchanged=True,public_projection=dict(path=P,sha256=ph,old_pool_preserved=True,new_values=len(pool)-len(prior_values),reconstruction_exact=True))
CH=save('out/checks/scan024_source_bounded_closure_v02.json',closure)
audit=dict(scan=24,main_approved=False,draft_sha256=sha((D/'scan024_final_draft.tex').read_bytes()),map_sha256=sha((D/'scan024_final_source_map.json').read_bytes()),record_sha256=newhash,closure_v01_sha256=closure['previous_closure']['sha256'],closure_v02_sha256=CH,projection_sha256=ph,counts=new['counts'],canonical_C_outcomes={'resolved':2,'mixed':1,'retained':15},remaining_root_actions=['Bounded independent QA and root approval.'])
AH=save('out/checks/scan024_source_record_audit_v05.json',audit)
files=[CAN,NEW,'out/checks/scan024_final_draft.tex','out/checks/scan024_final_source_map.json',P,'out/checks/scan024_source_public_projection_v02.jsonl','out/checks/scan024_source_public_projection_delta_v02.json','out/checks/scan024_source_bounded_closure_v02.json','out/checks/scan024_source_record_audit_v05.json','out/checks/scan024_source_patch_alternatives_v02.py']
release=dict(scan=24,main_approved=False,files={f:sha((BASE/f).read_bytes()) for f in files},counts=new['counts'],canonical_C_outcomes={'resolved':2,'mixed':1,'retained':15},prior_release=dict(path='out/checks/scan024_source_record_release_v01.json',sha256=sha(read('out/checks/scan024_source_record_release_v01.json'))),current_public_projection=P,pending=['Bounded QA and root final approval.'])
RH=save('out/checks/scan024_source_record_release_v02.json',release)
print(json.dumps(dict(record_sha256=newhash,map_sha256=audit['map_sha256'],public_projection_sha256=ph,closure_sha256=CH,audit_sha256=AH,release_sha256=RH,new_pool_values=len(pool)-len(prior_values),changed_fields=len(changes)),indent=2))
