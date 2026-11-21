#!/usr/bin/env python3
"""Add only the two documented inline A commands to the QA inventory."""
from pathlib import Path
from copy import deepcopy
import hashlib
import importlib.util
import json
import shutil

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'out/checks'
path=OUT/'scan025_qa_sourcecoverage_inventory.json'
old_raw=path.read_bytes()
snapshot=OUT/'scan025_qa_sourcecoverage_inventory_r1.json'
assert not snapshot.exists()
shutil.copyfile(path,snapshot)
shutil.copyfile(OUT/'scan025_qa_sourcecoverage_inventory.md',OUT/'scan025_qa_sourcecoverage_inventory_r1.md')
data=json.loads(old_raw)
spec=importlib.util.spec_from_file_location('scan025_qa_source_inventory',OUT/'scan025_qa_source_inventory.py')
helper=importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
tex_path='out/readers/025/A/reading.tex'
text=(BASE/tex_path).read_text()
old_commands=deepcopy(data['literal_drawing_command_inventory'])
old_a=[x for x in old_commands if x['reader']=='A']
old_by_start={x['source_ref']['char_start']:x for x in old_a}
literal_commands=helper.drawing_commands(text)
new_starts={a for _,a,_ in literal_commands}-set(old_by_start)
assert new_starts=={9044,16535}
assert set(old_by_start)<=set(a for _,a,_ in literal_commands)
new_a=[]
additions=[]
ordinal_changes=[]
for ordinal,(command,start,end) in enumerate(literal_commands):
    if start in old_by_start:
        row=deepcopy(old_by_start[start])
        assert row['source_ref']['char_end_exclusive']==end
        if row['ordinal0']!=ordinal:
            ordinal_changes.append({'source_char_start':start,'old_ordinal0':row['ordinal0'],'new_ordinal0':ordinal})
        row['ordinal0']=ordinal
    else:
        owners=[g['id'] for g in data['group_span_inventory'] if g['reader']=='A' and g['tex_ref']['char_start']<=start and end<=g['tex_ref']['char_end_exclusive']]
        row={'reader':'A','ordinal0':ordinal,'command':command,'source_ref':helper.text_ref(tex_path,text,start,end),'group_ids':owners}
        additions.append({'source_char_start':start,'new_array_index':ordinal,'entry':deepcopy(row),'literal':text[start:end]})
    new_a.append(row)
new_commands=new_a+[deepcopy(x) for x in old_commands if x['reader']!='A']
# Explicit inverse: remove the two inserted starts; restore saved original
# ordinals. All remaining rows must exactly equal the initial inventory list.
inverse=[deepcopy(x) for x in new_commands if not(x['reader']=='A' and x['source_ref']['char_start'] in new_starts)]
for row in inverse:
    if row['reader']=='A':
        row['ordinal0']=old_by_start[row['source_ref']['char_start']]['ordinal0']
assert inverse==old_commands
data['literal_drawing_command_inventory']=new_commands
old_count=data['source_counts']['A']['literal_drawing_command_rows']
assert old_count==143
data['source_counts']['A']['literal_drawing_command_rows']=145
closure={
    'prior_inventory_path':'out/checks/scan025_qa_sourcecoverage_inventory_r1.json',
    'prior_inventory_sha256_utf8':helper.digest(old_raw),
    'source_path':tex_path,'source_sha256_utf8':helper.digest(text),
    'reason':'The original line-start scan omitted two literal coordinate commands following path semicolons on the same line. No reader/source change was made.',
    'added_exact_commands':additions,'ordinal_leaf_changes':ordinal_changes,
    'count_leaf_change':{'json_pointer':'/source_counts/A/literal_drawing_command_rows','old':143,'new':145},
    'forward_and_inverse_replay_equal':True,'source_files_changed':[],
}
data['inline_command_inventory_closure']=closure
new_raw=(json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
path.write_bytes(new_raw)
md=OUT/'scan025_qa_sourcecoverage_inventory.md'
text_md=md.read_text().replace('| A | 21 | 14 | 29 | 21 | 19 | 143 |','| A | 21 | 14 | 29 | 21 | 19 | 145 |').replace('443 literal drawing-command references','445 literal drawing-command references')
text_md+='\nThe bounded inline-command closure adds A source characters 9044 and 16535 to the command inventory. Both exact coordinate commands, their original source-group containment, and the forward/inverse inventory replay are recorded; the prior inventory remains frozen.\n'
md.write_text(text_md)
summary={k:v for k,v in closure.items() if k!='ordinal_leaf_changes'}
summary['ordinal_leaf_change_count']=len(ordinal_changes)
summary['corrected_inventory_sha256_utf8']=helper.digest(new_raw)
(OUT/'scan025_qa_inline_command_closure.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
