"""Finite source-only consistency inspection. No TeX engine or image work."""
from pathlib import Path
import json,re
P=Path('/workspace/scratch/94548b74fbe0/out/readers/018/B')
t=(P/'reading.tex').read_text()
r=json.loads((P/'report.json').read_text())
code='\n'.join(line.split('%',1)[0] for line in t.splitlines())
depth=0
for pos,ch in enumerate(code):
    if ch in '{}':
        n=0;j=pos-1
        while j>=0 and code[j]=='\\':n+=1;j-=1
        if n%2:continue
        depth += 1 if ch=='{' else -1
        assert depth>=0,('early close brace',pos)
assert depth==0,('unclosed braces',depth)
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',code):
    if m[1]=='begin':stack.append(m[2])
    else:assert stack and stack.pop()==m[2],('environment mismatch',m.group())
assert not stack,stack
assert code.count('$')%2==0,'unpaired dollar delimiter'
required=['id','location','C','H','reading','evidence','confidence','kind','diff_C','diff_H','C_doubt_status','readers_crop','bbox']
ids=[x['id'] for x in r['differences']]
assert len(ids)==len(set(ids)),'duplicate difference identifier'
for x in r['differences']:
    assert all(k in x for k in required),x['id']
    if x['readers_crop']:assert (P/x['readers_crop']).is_file(),x['readers_crop']
for x in r['doubts']:assert (P/x['crop']).is_file(),x['crop']
for x in r['crops']:
    assert (P/x['path']).is_file(),x['path']
    assert x['viewed'] is True and x['successful_visual_deliveries']==1
assert len(r['C_doubt_source_map'])==14
for row in r['C_doubt_source_map']:
    assert row['count_original_row_once'] is True
    assert all(i in ids for i in row['local_difference_ids'])
commands=sorted(set(re.findall(r'\\([A-Za-z]+)',code)))
allowed={'scanpage','operatorname','unsure','begin','end','path','coordinate','node','inserted','draw','figure','rlap','phantom','uline','Pi','deleted','circ','Sigma','setminus','alpha','ne','in','pi','fill','subset'}
assert set(commands)<=allowed,sorted(set(commands)-allowed)
paths=len(re.findall(r'\\(?:draw|fill)\b',code))
reported=sum(len(g['paths']) for g in r['graphical_components'])
assert paths==reported,(paths,reported)
for chosen in [r'\unsure{rècurrence|récurrence}',r'\unsure{des|de}',r'\unsure{composante|composant}',r'\unsure{élêment|élément}',r'\deleted{\unsure{OK|cela|et}}',r'\unsure{â|à}',r'\pi_0(X\setminus\Sigma_i)']:
    assert chosen in t,chosen
assert r['check_events']==[]
result={
 'brace_balance':'passed','environment_nesting':'passed','dollar_pair_parity':'passed',
 'macro_names':commands,'all_difference_and_doubt_crop_references_exist':True,
 'C_source_doubt_rows':14,'difference_records':len(ids),'crop_records':len(r['crops']),
 'literal_draw_fill_commands':paths,'documented_path_components':reported,
 'selected_reading_report_agreement':'checked at the named qualified lexical/formula source anchors',
 'validation_scope':'Source strings/JSON/file existence only. No compiler, renderer, OCR, image reopening, mathematical result, pixel comparison, geometry or font measurement.',
}
(P/'source_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
