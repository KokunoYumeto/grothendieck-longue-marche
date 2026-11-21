"""Exact bounded forward/inverse closure of root-authorized source repairs."""
from pathlib import Path
import json,hashlib,copy,collections,sys
sys.dont_write_bytecode=True
BASE=Path('/workspace/scratch/94548b74fbe0');D=BASE/'out/checks'
sys.path.insert(0,str(D));import scan024_source_support as support
sha=lambda b:hashlib.sha256(b if isinstance(b,bytes) else b.encode()).hexdigest()
def load(p):return json.loads((BASE/p).read_text())
def save(p,x):
    (BASE/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
OLD='out/checks/scan024_source_record_initial_v01.json'
NEW='out/checks/scan024_record_draft.json'
FROZEN='out/checks/scan024_source_record_repaired_v01.json'
assert not (BASE/FROZEN).exists()
(BASE/FROZEN).write_bytes((BASE/NEW).read_bytes())
FMAP='out/checks/scan024_source_record_repaired_map_v01.json'
assert not (BASE/FMAP).exists()
(BASE/FMAP).write_bytes((D/'scan024_final_source_map.json').read_bytes())
def pointer_part(k):return str(k).replace('~','~0').replace('/','~1')
def pointer_get(x,p):
    for k in p.split('/')[1:]:
        k=k.replace('~1','/').replace('~0','~');x=x[int(k)] if isinstance(x,list) else x[k]
    return x
def pointer_set(x,p,value,present=True):
    parts=p.split('/')[1:]
    for k in parts[:-1]:
        k=k.replace('~1','/').replace('~0','~');x=x[int(k)] if isinstance(x,list) else x[k]
    k=parts[-1].replace('~1','/').replace('~0','~')
    if isinstance(x,list):x[int(k)]=copy.deepcopy(value)
    elif present:x[k]=copy.deepcopy(value)
    else:del x[k]
def order_like(x,template):
    if isinstance(x,dict):return {k:order_like(x[k],template[k]) for k in template}
    if isinstance(x,list):return [order_like(v,t) for v,t in zip(x,template)]
    return x
def source_ref(path,spans,p):
    t=(BASE/path).read_text();a,b=spans.spans[p]
    return dict(path=path,sha256=sha(t),json_pointer=p,char_start=a,char_end=b,
      utf8_byte_start=len(t[:a].encode()),utf8_byte_end=len(t[:b].encode()),body_sha256=sha(t[a:b]))
def compare(old,new,oldpath,newpath):
    os=support.JSONSpans((BASE/oldpath).read_text());ns=support.JSONSpans((BASE/newpath).read_text());changes=[]
    def walk(a,b,p=''):
        if type(a)!=type(b):add(p,a,b,True,True)
        elif isinstance(a,dict):
            for k in list(a)+[k for k in b if k not in a]:
                q=p+'/'+pointer_part(k)
                if k not in a:add(q,None,b[k],False,True)
                elif k not in b:add(q,a[k],None,True,False)
                else:walk(a[k],b[k],q)
        elif isinstance(a,list):
            if len(a)!=len(b):add(p,a,b,True,True)
            else:
                for i,(x,y) in enumerate(zip(a,b)):walk(x,y,p+'/'+str(i))
        elif a!=b:add(p,a,b,True,True)
    def add(p,a,b,ap,bp):
        c=dict(path=p,operation='replace' if ap and bp else 'add' if bp else 'remove',old_present=ap,new_present=bp)
        if ap:c['old_exact_value']=source_ref(oldpath,os,p)
        if bp:c['new_exact_value']=source_ref(newpath,ns,p)
        for label,value,present in [('old',a,ap),('new',b,bp)]:
            if present and (not isinstance(value,(dict,list,str)) or isinstance(value,str) and len(value)<260):c[label+'_value']=value
        changes.append(c)
    walk(old,new)
    replay=copy.deepcopy(old)
    for c in changes:pointer_set(replay,c['path'],pointer_get(new,c['path']) if c['new_present'] else None,c['new_present'])
    assert replay==new
    fwd=json.dumps(order_like(replay,new),ensure_ascii=False,indent=2)+'\n'
    assert fwd==(BASE/newpath).read_text()
    inverse=copy.deepcopy(new)
    for c in reversed(changes):pointer_set(inverse,c['path'],pointer_get(old,c['path']) if c['old_present'] else None,c['old_present'])
    assert inverse==old
    inv=json.dumps(order_like(inverse,old),ensure_ascii=False,indent=2)+'\n'
    assert inv==(BASE/oldpath).read_text()
    return changes,dict(forward_structural_exact=True,inverse_structural_exact=True,forward_UTF8_exact=True,inverse_UTF8_exact=True,key_order_rule='JSON object key order is restored from the corresponding frozen source parser; no field values are copied for this ordering step.')
old=load(OLD);new=load(FROZEN)
changes,replay=compare(old,new,OLD,FROZEN)
assert old['counts']==new['counts']
assert all(a['H']==b['H'] and a['evidence']==b['evidence'] for a,b in zip(old['decisions'],new['decisions']))
assert [b['id'] for a,b in zip(old['decisions'],new['decisions']) if a['C']!=b['C']]==['SRC024-L64']
assert [b['id'] for a,b in zip(old['decisions'],new['decisions']) if a['final']!=b['final']]==['SRC024-L38','SRC024-L39']
for a,b in zip(old['decisions'],new['decisions']):
    for k in ['diff_C','diff_H','confidence','physical_count_parent','marked_in_H']:assert a[k]==b[k],(b['id'],k)
def role(p):
    if '/readers/A' in p:return 'reader_A_own_source'
    if '/readers/B' in p:return 'reader_B_own_source'
    if '/readers/C' in p:return 'reader_C_own_source'
    if p.endswith('/C'):return 'public_witness_C_quotation_label'
    if '/source_map_reference/' in p or p=='/selected_source_map/sha256':return 'necessary_current_map_hash_binding'
    if p.endswith('/kind') or '/root_public_kind_authorization' in p:return 'root_authorized_collation_kind'
    if p.startswith('/C_source_rows/'):return 'canonical_original_C_status_and_historical_provenance'
    if p.startswith('/inventory/'):return 'selected_inventory_role_or_binding'
    if p.startswith('/notes') or p.startswith('/attributed_content_note/') or p.startswith('/root_selected_content_note/'):return 'current_attributed_note_or_binding'
    if p=='/brief_version':return 'workflow_reader_and_source_brief_label'
    return 'selected_role_mirror_or_authority_binding'
for c in changes:c['semantic_role']=role(c['path'])
om='out/checks/scan024_source_record_initial_map_v01.json';nm=FMAP
mc,mreplay=compare(load(om),load(nm),om,nm)
authorities=['out/checks/scan024_root_count_authorization_v2.json','out/checks/scan024_root_selected_hand_scope_clarification.json','out/checks/scan024_root_public_kind_authorization.json','out/checks/scan024_qa_coverage_followup_v01.json']
closure=dict(scan=24,source_only=True,main_approved=False,scope='Bounded source-role completeness repairs after initial review; selected page/count/confidence/H/evidence bytes and values remain unchanged.',
 initial_record=dict(path=OLD,sha256=sha((BASE/OLD).read_bytes())),current_record=dict(path=FROZEN,canonical_path=NEW,sha256=sha((BASE/FROZEN).read_bytes())),
 initial_map=dict(path=om,sha256=sha((BASE/om).read_bytes())),current_map=dict(path=nm,canonical_path='out/checks/scan024_final_source_map.json',sha256=sha((BASE/nm).read_bytes())),
 unchanged_page=dict(path='out/checks/scan024_final_draft.tex',sha256=sha((D/'scan024_final_draft.tex').read_bytes())),
 authorities=[dict(path=p,sha256=sha((BASE/p).read_bytes())) for p in authorities],
 direct_root_authorizations=dict(own_reader_scope_repair='Restore exact own inventory and report hand/role/separate-scope fields; do not change other semantic roles.',brief_version="v22 / source-record v07",canonical_part_status='Retain original pending ink adjudication in original_source_decision_status and provenance; current decision_status names existing selected outcome and final approval pending.',canonical_parent_flags='Remove only the redundant parent main_approved fields; keep all canonical part flags false.',notes='Append the exact root-authorized A context-for-location/B p-bar separation disclosure and the selected local Sigma/U candidate ordering; keep events empty.'),
 record_change_count=len(changes),record_changes=changes,record_replay=replay,map_change_count=len(mc),map_changes=mc,map_replay=mreplay,
 role_counts=dict(collections.Counter(c['semantic_role'] for c in changes)),counts_unchanged=True,confidence_flags_and_physical_parents_unchanged=True,
 all_H_and_evidence_fields_unchanged=True,changed_C_fields=['SRC024-L64 quotation label only'],changed_selected_finals=['SRC024-L38 candidate-specific hand','SRC024-L39 selected his-hand scope'],
 public_projection=dict(path='out/checks/scan024_source_public_projection.json',sha256=sha((D/'scan024_source_public_projection.json').read_bytes()),record_sha256=sha((BASE/NEW).read_bytes())),
 initial_audit=dict(path='out/checks/scan024_source_record_initial_audit_v01.json',sha256=sha((D/'scan024_source_record_initial_audit_v01.json').read_bytes())),
 current_audit=dict(path='out/checks/scan024_source_record_audit_v04.json',sha256=sha((D/'scan024_source_record_audit_v04.json').read_bytes())),
 limits='Exact text/source validation only; no images, new ink decisions, source normalisation, physical coordinate conversion, rendering, compilation or mathematical check.')
CP='out/checks/scan024_source_bounded_closure_v01.json';save(CP,closure)
with (D/'scan024_source_bounded_changes_v01.jsonl').open('w') as f:
    f.write(json.dumps(dict(kind='metadata',closure=CP,closure_sha256=sha((BASE/CP).read_bytes()),record_change_count=len(changes),map_change_count=len(mc)),ensure_ascii=False)+'\n')
    for c in changes:f.write(json.dumps(dict(kind='record_change',**c),ensure_ascii=False)+'\n')
    for c in mc:f.write(json.dumps(dict(kind='map_change',**c),ensure_ascii=False)+'\n')
files=['scan024_final_draft.tex','scan024_final_source_map.json','scan024_record_draft.json','scan024_source_record_repaired_v01.json','scan024_source_record_repaired_map_v01.json','scan024_source_public_projection.json','scan024_source_public_projection.jsonl','scan024_source_reader_frame_projection.json','scan024_source_bounded_closure_v01.json','scan024_source_bounded_changes_v01.jsonl','scan024_source_record_audit_v04.json','scan024_source_build_record.py','scan024_source_public_values.py','scan024_source_close_record.py']
release=dict(scan=24,main_approved=False,status='Frozen for bounded independent QA and root review.',files={str(D/p).removeprefix(str(BASE)+'/'):sha((D/p).read_bytes()) for p in files},counts=new['counts'],canonical_C_outcomes={'resolved':2,'mixed':1,'retained':15},pending=['Independent bounded QA and root final review/approval.'])
save('out/checks/scan024_source_record_release_v01.json',release)
print(json.dumps(dict(closure_sha256=sha((BASE/CP).read_bytes()),record_sha256=sha((BASE/NEW).read_bytes()),map_sha256=sha((D/'scan024_final_source_map.json').read_bytes()),projection_sha256=sha((D/'scan024_source_public_projection.json').read_bytes()),release_sha256=sha((D/'scan024_source_record_release_v01.json').read_bytes()),record_changes=len(changes),map_changes=len(mc),role_counts=closure['role_counts']),ensure_ascii=False,indent=2))
