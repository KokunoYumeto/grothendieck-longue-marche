from pathlib import Path
import json,re
R=Path('/workspace/scratch/94548b74fbe0/out/readers/016/B')
s=(R/'reading.tex').read_text()
r=json.loads((R/'report.json').read_text())
body='\n'.join(line.split('%',1)[0] for line in s.splitlines())
errors=[]
stack=[]
for i,ch in enumerate(body):
    if ch in '{}':
        n=0;j=i-1
        while j>=0 and body[j]=='\\': n+=1;j-=1
        if n%2: continue
        if ch=='{':stack.append(i)
        elif not stack: errors.append(f'unmatched closing brace at {i}')
        else:stack.pop()
if stack:errors.append(f'unclosed braces: {len(stack)}')
envs=[]
for match in re.finditer(r'\\(begin|end)\{([^}]+)\}',body):
    op,env=match.groups()
    if op=='begin':envs.append(env)
    elif not envs or envs[-1]!=env:errors.append(f'environment mismatch: {op} {env}')
    else:envs.pop()
if envs:errors.append(f'unclosed environments: {envs}')
if body.count(r'\[')!=body.count(r'\]'):errors.append('display delimiter count mismatch')
if len(re.findall(r'(?<!\\)\$',body))%2:errors.append('odd dollar count')
allowed={'scanpage','Sigma','cup','deleted','unsure','setminus','figure','begin','end','path','node','inserted','small','draw','rlap','displaystyle','overbrace','underbrace','phantom','amalg','underset','hspace','cdot','text','overset','cap','subset','subsetneq','overline','makebox','linewidth','fill','quad','ne','varnothing','big'}
macros=set(re.findall(r'\\([A-Za-z]+)',body))
unknown=sorted(macros-allowed)
if unknown:errors.append(f'unlisted macros: {unknown}')
for d in r['differences']:
    if d['readers_crop'] and not (R/d['readers_crop']).is_file():errors.append(f'missing crop for {d["id"]}')
for c in r['crops']:
    if not (R/c['path']).is_file():errors.append(f'missing crop {c["path"]}')
rows={x['source_row_id'] for x in r['source_doubt_rows']}
if rows!={f'CD{i:02d}' for i in range(1,14)}:errors.append('source doubt identity mismatch')
local=sum(len(x['local_decisions']) for x in r['source_doubt_rows'])
if local!=21:errors.append('local C status count mismatch')
for row in r['source_doubt_rows']:
    for d in row['local_decisions']:
        if d['status'] not in ('resolved','retained'):errors.append('missing local C status')
required=[r'\unsure{égal|égale}',r'\unsure{:|à}',r'\unsure{qfd|cqfd}',r'\deleted{E}\Sigma_{12}',r'\inserted{\unsure{en|on} conclurait}',r'\deleted{\amalg}\cup',r'\unsure{\big]}',r'% archive sheet number: 15']
for token in required:
    if token not in s:errors.append(f'missing chosen token {token}')
for component in ['G01','G02a1','G02a2','G02b','G02c','G03','M01','M02a','M02b','M03']:
    if component not in s:errors.append(f'missing component {component}')
    if not any(component in d.get('source_components',[]) for d in r['differences']):errors.append(f'unreported component {component}')
    if not any(component in d.get('source_components',[]) for d in r['inventory']):errors.append(f'uninventoried component {component}')
if r['check_events']!=[]:errors.append('unexpected mathematical check events')
if r['notes']['model_effort']!='No claim is made about model effort settings.':errors.append('model effort record altered')
result=dict(errors=errors,passed=not errors,display_pairs=body.count(r'\['),dollar_count=len(re.findall(r'(?<!\\)\$',body)),macro_names=sorted(macros),difference_rows=len(r['differences']),source_doubt_rows=len(rows),local_C_decisions=local,crop_files=len(r['crops']),inventory_items=len(r['inventory']),actual_mathematical_checks=0,compile_attempts=0,render_attempts=0)
(R/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
