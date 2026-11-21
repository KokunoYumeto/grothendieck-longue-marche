#!/usr/bin/env python3
"""Recover the first emitted pending bytes without touching current artifacts."""
from pathlib import Path
from copy import deepcopy
import hashlib,json,sys
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent;ROOT=O.parents[1]
sys.path.insert(0,str(O));sha=lambda b:hashlib.sha256(b.encode()if isinstance(b,str)else b).hexdigest()
current={n:sha((O/n).read_bytes())for n in ['scan025_record_draft.json','scan025_final_source_map.json']}
script=(O/'scan025_source_build_record.py').read_text()
a=script.index('        original_C_report_refs=[]\n');b=script.index("        suffix='\\nLocal",a);script=script[:a]+script[b:]
script=script.replace('original_C_reader_scope_refs=original_C_report_refs,stage1_locus_reader_mapping=','stage1_locus_reader_mapping=')
script='\n'.join(line for line in script.split('\n')if not line.startswith('C_PART_CONF='))
script=script.replace("confidence=C_PART_CONF[raw['source_id']]","confidence=DOUBT_CONFIDENCE.get(int(d['id'][-2:]),d['confidence'])")
a=script.index('authority_rebindings=[]\n');b=script.index('MAPHASH=write(MP,M)',a);script=script[:a]+script[b:]
script=script.replace("for g in record['selected_graphical_groups']:g['source']=deepcopy(g['source_attachments'][0])\n",'')
a=script.index('def write(p,obj):\n');b=script.index("UP='out/checks/",a)
script=script[:a]+"CAPTURE={}\ndef write(p,obj):\n    text=dump(obj);CAPTURE[p]=text;return sha(text)\n"+script[b:]
env={'__file__':str(O/'scan025_source_build_record.py'),'__name__':'recovery_only'}
exec(script,env)
captures=env['CAPTURE']
expected={'out/checks/scan025_record_draft.json':'18679288b58e1ff15940e71e03779898fb8edbb41129d1d5c042faeee2390b98','out/checks/scan025_final_source_map.json':'72f44cb7bc4ac4884bad41909b83d47c2777441e2e16388732977349cca82c9c'}
paths={'out/checks/scan025_record_draft.json':'scan025_source_record_initial_v01.json','out/checks/scan025_final_source_map.json':'scan025_source_record_initial_map_v01.json','out/checks/scan025_source_record_construction_audit_v01.json':'scan025_source_record_initial_construction_audit_v01.json'}
for p,h in expected.items():assert sha(captures[p])==h,(p,sha(captures[p]))
for p,n in paths.items():
    target=O/n
    if target.exists():assert target.read_text()==captures[p]
    else:target.write_text(captures[p])
for n,h in current.items():assert sha((O/n).read_bytes())==h
def ptr(k):return str(k).replace('~','~0').replace('/','~1')
def differences(a,b,path=''):
    if type(a)!=type(b):return [dict(pointer=path,op='replace')]
    if isinstance(a,dict):
        out=[]
        for k in a:
            if k not in b:out.append(dict(pointer=path+'/'+ptr(k),op='remove'))
            else:out+=differences(a[k],b[k],path+'/'+ptr(k))
        for k in b:
            if k not in a:out.append(dict(pointer=path+'/'+ptr(k),op='add'))
        return out
    if isinstance(a,list):
        if len(a)!=len(b):return [dict(pointer=path,op='replace')]
        return [x for i,(v,w)in enumerate(zip(a,b))for x in differences(v,w,path+'/'+str(i))]
    return []if a==b else[dict(pointer=path,op='replace')]
closures=[]
def get(v,p):
    for k in p[1:].split('/')if p else[]:
        k=k.replace('~1','/').replace('~0','~');v=v[int(k)]if isinstance(v,list)else v[k]
    return v
def orders(a,b,path=''):
    out=[]
    if isinstance(a,dict)and isinstance(b,dict):
        if list(a)!=list(b):out.append(dict(pointer=path,old=list(a),new=list(b)))
        for k in a.keys()&b.keys():out+=orders(a[k],b[k],path+'/'+ptr(k))
    elif isinstance(a,list)and isinstance(b,list)and len(a)==len(b):
        for i,(v,w)in enumerate(zip(a,b)):out+=orders(v,w,path+'/'+str(i))
    return out
def replay(source,target,changes,keyorders,inverse=False):
    result=deepcopy(source)
    for change in changes:
        p=change['pointer'];op=change['op'];op=({'add':'remove','remove':'add','replace':'replace'}[op]if inverse else op)
        if not p:result=deepcopy(target);continue
        parent,key=p.rsplit('/',1);key=key.replace('~1','/').replace('~0','~');obj=get(result,parent)
        if isinstance(obj,list):key=int(key)
        if op=='remove':del obj[key]
        else:obj[key]=deepcopy(get(target,p))
    for row in sorted(keyorders,key=lambda x:x['pointer'].count('/'),reverse=True):
        obj=get(result,row['pointer']);keys=row['old'if inverse else'new'];assert set(obj)==set(keys);temp={k:obj[k]for k in keys};obj.clear();obj.update(temp)
    return result
for p,n in list(paths.items())[:2]:
    old=json.loads(captures[p]);new=json.loads((ROOT/p).read_text());changes=differences(old,new);keyorders=orders(old,new)
    forward=replay(old,new,changes,keyorders);inverse=replay(new,old,changes,keyorders,True)
    assert json.dumps(forward,ensure_ascii=False,indent=2)+'\n'==(ROOT/p).read_text()
    assert json.dumps(inverse,ensure_ascii=False,indent=2)+'\n'==captures[p]
    closures.append(dict(old_path='out/checks/'+n,old_sha256=sha(captures[p]),new_path=p,new_sha256=current[Path(p).name],changed_leaf_or_added_container_count=len(changes),changes=changes,
        key_orders=keyorders,forward_and_inverse_byte_replay_passed=True,values='Each old/new value is the exact JSON value at this pointer in the separately frozen old/new file; key-order changes are explicit.'))
old=json.loads(captures['out/checks/scan025_record_draft.json'])['provenance']['source_reference_pool'];new=json.loads((O/'scan025_record_draft.json').read_text())['provenance']['source_reference_pool'];lookup={json.dumps(v,sort_keys=True,ensure_ascii=False):k for k,v in new.items()}
morphism={k:lookup[json.dumps(v,sort_keys=True,ensure_ascii=False)]for k,v in old.items()}
result=dict(scan=25,status='Initial emitted pending bytes recovered exactly; current frozen artifacts unchanged',recovery_script_sha256=sha(script),closures=closures,old_to_new_exact_original_reference_ids=morphism,
    semantic_additions=['Original reader-specific canonical C scope/status fields in public own-proposal suffixes','Original C part confidence tied to its exact predecessor/index scope','Current exact journal/hash attachments rebound after the §21 append','Current selected group source uses the gate-supported relative attachment path'],
    page_change=False,count_change=False,root_ink_change=False,initial_record_was_not_read_by_root=True)
(O/'scan025_source_record_initial_to_pending_v02_delta.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'recovered':{paths[k]:sha(v)for k,v in captures.items()},'delta_counts':[x['changed_leaf_or_added_container_count']for x in closures],'reference_id_morphism':len(morphism)},indent=2))
