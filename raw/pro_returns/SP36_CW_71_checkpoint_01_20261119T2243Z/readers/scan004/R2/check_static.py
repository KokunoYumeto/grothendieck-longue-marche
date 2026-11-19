from pathlib import Path
import json,re
p=Path('/workspace/scratch/17347c1714f0/out/readers/scan004/R2')
s=(p/'reading.tex').read_text(encoding='utf-8')
report=json.loads((p/'report.json').read_text(encoding='utf-8'))
s_clean='\n'.join(line.split('%',1)[0] for line in s.splitlines())
stack=[]
for i,c in enumerate(s_clean):
    if c=='{' and (i==0 or s_clean[i-1]!='\\'): stack.append(i)
    elif c=='}' and (i==0 or s_clean[i-1]!='\\'):
        assert stack, f'Unmatched closing brace at {i}'
        stack.pop()
assert not stack, f'Unmatched opening braces: {stack}'
envs=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s_clean):
    act,env=m.groups()
    if act=='begin': envs.append(env)
    else:
        assert envs and envs[-1]==env,(envs,env)
        envs.pop()
assert not envs
assert len(re.findall(r'(?<!\\)\$',s_clean))%2==0
assert len(re.findall(r'(?<!\\)\\\[',s_clean))==len(re.findall(r'(?<!\\)\\\]',s_clean))
assert len(re.findall(r'(?<!\\)\\\(',s_clean))==len(re.findall(r'(?<!\\)\\\)',s_clean))
assert s_clean.count(r'\begingroup')==s_clean.count(r'\endgroup')
for finding in report['findings']:
    assert finding['reading'] in s, finding['id']
assert all(x['h'] is None and not x['diff_h'] for x in report['findings'])
assert not any(x['unresolved'] and not x['reading'] for x in report['findings'])
result='PASS: JSON validity; TeX brace, environment, group and math-delimiter balance; findings occur verbatim in reading.tex; no invented H comparison.\n'
result+=f"Inventory blocks: {len(report['inventory'])}; findings: {len(report['findings'])}; crops: {len(report['crops'])}.\n"
(p/'static_check.txt').write_text(result,encoding='utf-8')
print(result)
