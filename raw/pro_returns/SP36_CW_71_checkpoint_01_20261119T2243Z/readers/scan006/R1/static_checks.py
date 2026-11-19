from pathlib import Path
from datetime import datetime, timezone
import re, json
P=Path('/workspace/scratch/17347c1714f0/out/readers/scan006/R1')
s=(P/'reading.tex').read_text()
r=json.loads((P/'report.json').read_text())
for f in r['findings']:
    if f['kind']=='readable ink left as \\\\ill{}':
        f['kind']='readable ink left as \\ill{}'
# Strip comments without treating escaped percent signs as comments.
u='\n'.join(re.split(r'(?<!\\)%',line,1)[0] for line in s.splitlines())
stack=[]
for i,ch in enumerate(u):
    if ch not in '{}': continue
    k=i-1
    while k>=0 and u[k]=='\\': k-=1
    if (i-1-k)%2: continue
    if ch=='{': stack.append(i)
    else:
        assert stack, ('unmatched closing brace',i)
        stack.pop()
assert not stack, ('unmatched opening braces',stack)
envs=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',u):
    op,env=m.groups()
    if op=='begin': envs.append(env)
    else:
        assert envs and envs.pop()==env, ('environment mismatch',m.group())
assert not envs,envs
assert len(re.findall(r'(?<!\\)\\\[',u))==len(re.findall(r'(?<!\\)\\\]',u)), 'display delimiters'
assert len(re.findall(r'(?<!\\)\\\(',u))==len(re.findall(r'(?<!\\)\\\)',u)), 'inline delimiters'
# All display dollars introduced by resizebox are paired; no literal currency occurs.
dollars=len(re.findall(r'(?<!\\)\$',u))
assert dollars%2==0,dollars
for f in r['findings']:
    assert not f['reading'] or f['reading'] in s, f['id']
for d in r['doubts']:
    assert d['reading'] in s,d['place']
assert sum(f['c_doubt'] for f in r['findings'])==24
assert len(r['crops'])==17
for c in r['crops']:
    assert Path(c['file']).exists()
    assert c['observed']
r['finished_utc']=datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
r['static_validation']={'brace_balance':'pass','environment_balance':'pass','display_delimiters':'pass','inline_math_delimiter_counts':'pass','dollar_delimiter_count':dollars,'exact_report_readings_in_tex':'pass','c_doubt_count':24,'compilation':'not attempted as instructed'}
(P/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
result={'brace_balance':'pass','environment_balance':'pass','display_delimiters':'pass','dollar_count':dollars,'all_findings_and_doubts_exact_in_tex':True,'c_doubts':24,'findings':len(r['findings']),'crops':len(r['crops']),'finished_utc':r['finished_utc']}
(P/'static_check_result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
