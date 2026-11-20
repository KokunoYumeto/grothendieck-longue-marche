"""Structural checks requested by the supplied conventions; no LaTeX compilation."""
from pathlib import Path
import re,json
w=Path(__file__).resolve().parents[1];results=[]
for p in sorted((w/'pages').glob('*.tex')):
    s=p.read_text();clean=re.sub(r'(?<!\\)%[^\n]*','',s)
    errors=[];stack=[]
    for i,c in enumerate(clean):
        if c in '{}':
            n=0;j=i-1
            while j>=0 and clean[j]=='\\':n+=1;j-=1
            if n%2:continue
            if c=='{':stack.append(i)
            elif not stack:errors.append(f'unmatched closing brace at {i}')
            else:stack.pop()
    if stack:errors.append(f'{len(stack)} unmatched opening braces')
    env=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
        op,x=m.groups()
        if op=='begin':env.append(x)
        elif not env or env.pop()!=x:errors.append(f'environment mismatch {x}')
    if env:errors.append('unclosed environments '+str(env))
    if clean.count('\\[')!=clean.count('\\]'):errors.append('display delimiters unbalanced')
    dollars=len(re.findall(r'(?<!\\)\$',clean))
    if dollars%2:errors.append('odd dollar delimiter count')
    if len(re.findall(r'\\scanpage\{\d+\}',clean))!=1:errors.append('scanpage marker count')
    results.append({'file':p.name,'errors':errors,'unsure':clean.count('\\unsure{'),'illegible':clean.count('\\illegible{'),'deleted':clean.count('\\deleted{'),'figures':clean.count('\\figure{'),'diagrams':clean.count('\\diagram{')})
out={'pages':len(results),'all_balanced':all(not r['errors'] for r in results),'results':results}
(w/'validation/tex_balance.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False))
