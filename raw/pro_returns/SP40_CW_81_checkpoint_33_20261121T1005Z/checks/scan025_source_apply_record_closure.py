#!/usr/bin/env python3
"""Apply exactly the seven root-authorized current record leaves, with inverse."""
from pathlib import Path
from copy import deepcopy
import hashlib,json
O=Path(__file__).resolve().parent;ROOT=O.parents[1]
sha=lambda b:hashlib.sha256(b.encode()if isinstance(b,str)else b).hexdigest()
dump=lambda x:json.dumps(x,ensure_ascii=False,indent=2)+'\n'
authority_path='out/checks/scan025_root_record_field_clarifications.json';authbytes=(ROOT/authority_path).read_bytes()
assert sha(authbytes)=='d015ee50059678082d89d76c26c2e8c288152bb53fed82a3e86b53a1eebdcb76'
A=json.loads(authbytes);oldbytes=(O/'scan025_source_record_pending_v02.json').read_bytes();old=json.loads(oldbytes)
assert sha(oldbytes)==A['before_record_sha256']
assert sha((O/'scan025_final_source_map.json').read_bytes())==A['before_source_map_sha256']
assert sha((O/'scan025_final_draft.tex').read_bytes())==A['unchanged_selected_page_sha256']
assert sha((O/'scan025_root_journal.md').read_bytes())==A['unchanged_root_journal_sha256']
def target(v,p):
    keys=[k.replace('~1','/').replace('~0','~')for k in p[1:].split('/')]
    for k in keys[:-1]:v=v[int(k)]if isinstance(v,list)else v[k]
    return v,int(keys[-1])if isinstance(v,list)else keys[-1]
new=deepcopy(old)
for c in A['changes']:
    obj,k=target(new,c['path']);assert obj[k]==c['old'];obj[k]=c['new']
newtext=dump(new);inverse=deepcopy(new)
for c in reversed(A['changes']):
    obj,k=target(inverse,c['path']);assert obj[k]==c['new'];obj[k]=c['old']
assert dump(inverse).encode()==oldbytes
def leaves(a,b,p=''):
    if isinstance(a,dict):
        assert list(a)==list(b)
        return [x for k in a for x in leaves(a[k],b[k],p+'/'+k.replace('~','~0').replace('/','~1'))]
    if isinstance(a,list):
        assert len(a)==len(b)
        return [x for i,(v,w)in enumerate(zip(a,b))for x in leaves(v,w,p+'/'+str(i))]
    return []if a==b else[p]
changed=leaves(old,new);assert set(changed)=={x['path']for x in A['changes']}and len(changed)==7
for path in ['scan025_record_draft.json','scan025_source_record_pending_v03.json']:
    p=O/path
    if p.exists():assert sha(p.read_bytes())in[A['before_record_sha256'],sha(newtext)]
    p.write_text(newtext)
mapbytes=(O/'scan025_final_source_map.json').read_bytes();(O/'scan025_source_record_pending_map_v03.json').write_bytes(mapbytes)
closure=dict(scan=25,status='seven authorized current leaves applied; pending root final approval',authority=dict(path=authority_path,sha256=sha(authbytes)),
    before=dict(record_path='out/checks/scan025_source_record_pending_v02.json',record_sha256=sha(oldbytes),source_map_path='out/checks/scan025_source_record_pending_map_v02.json',source_map_sha256=sha(mapbytes)),
    after=dict(record_path='out/checks/scan025_record_draft.json',record_snapshot='out/checks/scan025_source_record_pending_v03.json',record_sha256=sha(newtext),source_map_path='out/checks/scan025_final_source_map.json',source_map_sha256=sha(mapbytes)),
    exact_leaf_delta=deepcopy(A['changes']),changed_leaf_paths=changed,forward_and_inverse_byte_replay_passed=True,
    mirror_scope='All three note text mirrors are the explicit authorized leaves. The two selected inventory hand fields occur only at their named current rows. The selected map contains inventory associations and exact sources, with no current inventory hand or note-text mirror; its bytes and every map hash binding remain unchanged.',
    page_sha256=A['unchanged_selected_page_sha256'],journal_sha256=A['unchanged_root_journal_sha256'],counts=new['counts'],
    all_decision_readers_unchanged=old['decisions']==new['decisions'],all_current_doubts_unchanged=old['doubts']==new['doubts'],all_raw_provenance_unchanged=old['provenance']==new['provenance'],original_C_rows_unchanged=old['C_source_rows']==new['C_source_rows'],
    no_images_or_rendering=True,no_new_ink_or_count_choices=True,no_mathematical_check_events=True,main_approved=False)
closurepath='out/checks/scan025_source_record_closure_v03.json';(ROOT/closurepath).write_text(dump(closure))
audit=dict(scan=25,status='current source-only record binding after the bounded root closure; final QA replay pending',current_record_sha256=sha(newtext),current_source_map_sha256=sha(mapbytes),current_root_journal_sha256=A['unchanged_root_journal_sha256'],selected_page_sha256=A['unchanged_selected_page_sha256'],
    historical_page_assembly_audit=dict(path='out/checks/scan025_source_assembly_audit_v02.json',sha256=sha((O/'scan025_source_assembly_audit_v02.json').read_bytes()),scope='Historical page assembly through §20; exact original execution artifact preserved.'),
    historical_record_construction_audit=dict(path='out/checks/scan025_source_record_pending_construction_audit_v02.json',sha256=sha((O/'scan025_source_record_pending_construction_audit_v02.json').read_bytes()),scope='Historical record construction through §21 before seven authorized field clarifications; preserved.'),
    bounded_closure=dict(path=closurepath,sha256=sha((ROOT/closurepath).read_bytes()),leaf_count=7,forward_and_inverse_byte_replay_passed=True),
    page_or_map_bytes_changed=False,counts=new['counts'],original_C_outcomes={'retained':7,'resolved':1},selected_groups=25,selected_commands=172,reversible_page_replacements=7,added_outer_unsure_wrappers=0,
    source_scope_S_confidence='high solely for seven verified source-scope assignments, no local correction',all_marked_in_H_false=True,proof_events=0,source_only=True,main_adjudicated=False,main_approved=False)
auditpath='out/checks/scan025_source_assembly_record_audit_v03.json';(ROOT/auditpath).write_text(dump(audit))
freeze=dict(scan=25,status='frozen corrected pending record and unchanged selected page/map; projection derivatives pending',record=dict(path='out/checks/scan025_record_draft.json',snapshot='out/checks/scan025_source_record_pending_v03.json',sha256=sha(newtext)),
    source_map=dict(path='out/checks/scan025_final_source_map.json',snapshot='out/checks/scan025_source_record_pending_map_v03.json',sha256=sha(mapbytes)),selected_page=dict(path='out/checks/scan025_final_draft.tex',sha256=A['unchanged_selected_page_sha256']),
    closure=dict(path=closurepath,sha256=sha((ROOT/closurepath).read_bytes())),current_audit=dict(path=auditpath,sha256=sha((ROOT/auditpath).read_bytes())),approval=False)
(O/'scan025_source_record_pending_freeze_v03.json').write_text(dump(freeze));print(dump(freeze))
