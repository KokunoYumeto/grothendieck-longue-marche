#!/usr/bin/env python3
"""Bounded QA authority refresh for root section21 abbreviation apparatus."""
from pathlib import Path
from copy import deepcopy
import hashlib
import json
import re
import shutil

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'out/checks'
path=OUT/'scan025_qa_assembly_authority_map.json'
old_raw=path.read_bytes();old=json.loads(old_raw)
snapshot=OUT/'scan025_qa_assembly_authority_map_before21.json'
assert not snapshot.exists()
shutil.copyfile(path,snapshot)
sha=lambda value:hashlib.sha256(value if isinstance(value,bytes) else value.encode('utf-8')).hexdigest()
journal_path='out/checks/scan025_root_journal.md'
journal=(BASE/journal_path).read_text()
current_hash=sha(journal)
assert current_hash=='74d43b997bb80adecb31a7bf6cb6b7f81b3af350955475c6d87b0d2ad858afb1'
old_end=old['root_sections']['20']['source_ref']['char_end_exclusive']
assert sha(journal[:old_end])==old['authority']['journal_sha256_utf8']
(OUT/'scan025_qa_root_journal_before21.md').write_text(journal[:old_end])
m=re.search(r'(?m)^## 21 — (.+)$',journal);assert m
a,b=m.start(),len(journal)
new_ref={'path':journal_path,'sha256_utf8':current_hash,'char_start':a,'char_end_exclusive':b,'utf8_byte_start':len(journal[:a].encode('utf-8')),'utf8_byte_end_exclusive':len(journal[:b].encode('utf-8')),'line_start':journal.count('\n',0,a)+1,'line_end':journal.count('\n',0,b-1)+1,'literal_sha256_utf8':sha(journal[a:b])}
new=deepcopy(old)
def refresh(value):
    if isinstance(value,dict):
        if value.get('path')==journal_path and 'sha256_utf8' in value:
            assert value['sha256_utf8']==old['authority']['journal_sha256_utf8']
            assert sha(journal[value['char_start']:value['char_end_exclusive']])==value['literal_sha256_utf8']
            value['sha256_utf8']=current_hash
        for child in value.values():refresh(child)
    elif isinstance(value,list):
        for child in value:refresh(child)
refresh(new)
new['authority']['journal_sha256_utf8']=current_hash
new['root_sections']['21']={'section':'21','title':m.group(1),'source_ref':new_ref,'source_only':True,'root_ink_choice_applied':False,'root_source_audit_choice_applied':True,'crop_audit_reference':None}
new['authorized_abbreviations']=[{'form':'mut\\textsuperscript{t}.','expansion':'mutuellement','expansion_status':'probable expansion in apparatus only','root_section':'21','root_authority_ref':deepcopy(new_ref)},{'form':'i.e.','expansion':'id est','expansion_status':'authorized apparatus gloss only','root_section':'21','root_authority_ref':deepcopy(new_ref)}]
new['section21_bounded_closure']={'prior_authority_map':'out/checks/scan025_qa_assembly_authority_map_before21.json','prior_authority_map_sha256_utf8':sha(old_raw),'prior_journal_snapshot':'out/checks/scan025_qa_root_journal_before21.md','prior_journal_sha256_utf8':old['authority']['journal_sha256_utf8'],'closure_file':'out/checks/scan025_qa_authority_section21_closure.json','root_source_audit_choice_applied':True,'root_ink_choice_applied':False}
def esc(key):return str(key).replace('~','~0').replace('/','~1')
def diff(left,right,pointer=''):
    if type(left)!=type(right):return [{'path':pointer,'op':'replace','old':left,'new':right}]
    if isinstance(left,dict):
        ops=[]
        for key in left:
            p=pointer+'/'+esc(key)
            ops.extend(diff(left[key],right[key],p) if key in right else [{'path':p,'op':'remove','old':left[key]}])
        for key in right:
            if key not in left:ops.append({'path':pointer+'/'+esc(key),'op':'add','new':right[key]})
        return ops
    if isinstance(left,list):
        if len(left)!=len(right):return [{'path':pointer,'op':'replace','old':left,'new':right}]
        return [op for i,(a,b) in enumerate(zip(left,right)) for op in diff(a,b,pointer+'/'+str(i))]
    return [] if left==right else [{'path':pointer,'op':'replace','old':left,'new':right}]
ops=diff(old,new)
def replay(value,inverse=False):
    result=deepcopy(value)
    for op in reversed(ops) if inverse else ops:
        keys=[k.replace('~1','/').replace('~0','~') for k in op['path'][1:].split('/')]
        parent=result
        for key in keys[:-1]:parent=parent[int(key)] if isinstance(parent,list) else parent[key]
        key=int(keys[-1]) if isinstance(parent,list) else keys[-1]
        if op['op']=='replace':parent[key]=deepcopy(op['old' if inverse else 'new'])
        elif (op['op']=='add')!=inverse:parent[key]=deepcopy(op['new' if op['op']=='add' else 'old'])
        else:del parent[key]
    return result
assert replay(old)==new and replay(new,True)==old
new_raw=(json.dumps(new,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
path.write_bytes(new_raw)
closure={'scan':25,'scope':'QA authority map update for root section21 apparatus only; no original reader/source, root journal/audit, draft/record, notation or cumulative file changed.','old_map_sha256_utf8':sha(old_raw),'new_map_sha256_utf8':sha(new_raw),'old_journal_sha256_utf8':old['authority']['journal_sha256_utf8'],'new_journal_sha256_utf8':current_hash,'exact_changed_fields':ops,'forward_inverse_replay_equal':True,'root_counts_C_H':[25,27],'authorized_abbreviations':new['authorized_abbreviations']}
(OUT/'scan025_qa_authority_section21_closure.json').write_text(json.dumps(closure,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in closure.items() if k not in ['exact_changed_fields','authorized_abbreviations']},ensure_ascii=False,indent=2))
print('Exact changed fields:',len(ops))
