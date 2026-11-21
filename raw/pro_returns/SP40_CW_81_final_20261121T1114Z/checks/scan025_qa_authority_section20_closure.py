#!/usr/bin/env python3
"""Bound only root section20's five printing corrections into the QA map."""
from pathlib import Path
from copy import deepcopy
import hashlib
import json
import re
import shutil

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'out/checks'
path=OUT/'scan025_qa_assembly_authority_map.json'
old_raw=path.read_bytes()
old=json.loads(old_raw)
snapshot=OUT/'scan025_qa_assembly_authority_map_before20.json'
assert not snapshot.exists()
shutil.copyfile(path,snapshot)
journal_path='out/checks/scan025_root_journal.md'
journal=(BASE/journal_path).read_text()
sha=lambda v:hashlib.sha256(v if isinstance(v,bytes) else v.encode('utf-8')).hexdigest()
old_end=old['root_sections']['19']['source_ref']['char_end_exclusive']
assert sha(journal[:old_end])==old['authority']['journal_sha256_utf8']
(OUT/'scan025_qa_root_journal_before20.md').write_text(journal[:old_end])
m=re.search(r'(?m)^## 20 — (.+)$',journal)
assert m
a,b=m.start(),len(journal)
new_hash=sha(journal)
section20={'section':'20','title':m.group(1),'source_ref':{'path':journal_path,'sha256_utf8':new_hash,'char_start':a,'char_end_exclusive':b,'utf8_byte_start':len(journal[:a].encode('utf-8')),'utf8_byte_end_exclusive':len(journal[:b].encode('utf-8')),'line_start':journal.count('\n',0,a)+1,'line_end':journal.count('\n',0,b-1)+1,'literal_sha256_utf8':sha(journal[a:b])},'source_only':True,'root_ink_choice_applied':False,'root_source_audit_choice_applied':True,'crop_audit_reference':None}
new=deepcopy(old)


def refresh_authority_refs(v):
    if isinstance(v,dict):
        if v.get('path')==journal_path and 'sha256_utf8' in v:
            assert v['sha256_utf8']==old['authority']['journal_sha256_utf8']
            assert sha(journal[v['char_start']:v['char_end_exclusive']])==v['literal_sha256_utf8']
            v['sha256_utf8']=new_hash
        for child in v.values():refresh_authority_refs(child)
    elif isinstance(v,list):
        for child in v:refresh_authority_refs(child)


refresh_authority_refs(new)
new['authority']['journal_sha256_utf8']=new_hash
new['root_sections']['20']=section20
keys=['C025-E02','C025-S04','C025-S05','C025-S06','C025-S07']
assert new['wrapper_only_groups']==keys
new['wrapper_only_groups']=[]
new['exact_source_recurring_groups']=keys
loci=set()
for row in new['expected_authorized_clusters']:
    if row['qa_selection_key'] in keys:
        assert row['authorized_transform']=='one new outer unsure wrapper only'
        row['authorized_transform']='exact original source group; later primary remains unmarked under root section20'
        row['authorized_printed_qualifier']=False
        row['source_printing_authority_ref']=deepcopy(section20['source_ref'])
        row['source_printing_scope']='Only the added wrapper instruction is superseded. Complete local candidates and hand/role scopes remain required in selected record and notation.'
        loci.add(row['source_locus'])
assert len(loci)==5
for row in new['source_row_coverage']:
    if row['source_locus'] in loci:
        row['selected_source_printing_authority_ref']=deepcopy(section20['source_ref'])
new['section20_bounded_closure']={'prior_authority_map':'out/checks/scan025_qa_assembly_authority_map_before20.json','prior_authority_map_sha256_utf8':sha(old_raw),'prior_journal_snapshot':'out/checks/scan025_qa_root_journal_before20.md','prior_journal_sha256_utf8':old['authority']['journal_sha256_utf8'],'closure_file':'out/checks/scan025_qa_authority_section20_closure.json','root_source_audit_choice_applied':True,'root_ink_choice_applied':False}


def esc(k):return str(k).replace('~','~0').replace('/','~1')
def differences(x,y,p=''):
    if type(x)!=type(y):return [{'path':p,'op':'replace','old':x,'new':y}]
    if isinstance(x,dict):
        out=[]
        for k in x:
            q=p+'/'+esc(k)
            if k not in y:out.append({'path':q,'op':'remove','old':x[k]})
            else:out.extend(differences(x[k],y[k],q))
        for k in y:
            if k not in x:out.append({'path':p+'/'+esc(k),'op':'add','new':y[k]})
        return out
    if isinstance(x,list):
        if len(x)!=len(y):return [{'path':p,'op':'replace','old':x,'new':y}]
        return [z for i,(a,b) in enumerate(zip(x,y)) for z in differences(a,b,p+'/'+str(i))]
    return [] if x==y else [{'path':p,'op':'replace','old':x,'new':y}]


changes=differences(old,new)
def replay(source,operations,inverse=False):
    result=deepcopy(source)
    for op in reversed(operations) if inverse else operations:
        parts=[x.replace('~1','/').replace('~0','~') for x in op['path'][1:].split('/')]
        target=result
        for key in parts[:-1]:target=target[int(key)] if isinstance(target,list) else target[key]
        key=int(parts[-1]) if isinstance(target,list) else parts[-1]
        action=op['op']
        if action=='replace':target[key]=deepcopy(op['old' if inverse else 'new'])
        elif (action=='add')!=inverse:target[key]=deepcopy(op['new' if action=='add' else 'old'])
        else:del target[key]
    return result


assert replay(old,changes)==new
assert replay(new,changes,True)==old
new_raw=(json.dumps(new,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
path.write_bytes(new_raw)
closure={'scan':25,'scope':'Bounded QA-authority-map update for root section20 only; no original reader/source, root journal/audit, draft, record or global output changed.','old_map_sha256_utf8':sha(old_raw),'new_map_sha256_utf8':sha(new_raw),'old_journal_sha256_utf8':old['authority']['journal_sha256_utf8'],'new_journal_sha256_utf8':new_hash,'exact_changed_fields':changes,'forward_inverse_replay_equal':True,'root_counts_C_H':[25,27],'exact_source_recurring_groups':keys,'wrapper_only_groups':[]}
(OUT/'scan025_qa_authority_section20_closure.json').write_text(json.dumps(closure,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in closure.items() if k!='exact_changed_fields'},ensure_ascii=False,indent=2))
print('Exact changed fields:',len(changes))
