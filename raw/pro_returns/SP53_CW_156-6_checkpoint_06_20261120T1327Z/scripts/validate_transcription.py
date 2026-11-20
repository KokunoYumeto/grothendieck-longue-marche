"""Structural LaTeX validation only; no compilation or reading decisions."""
from pathlib import Path
import re,json,hashlib
OUT=Path(__file__).resolve().parents[1]
def no_comments(s):return '\n'.join(re.split(r'(?<!\\)%',line)[0] for line in s.splitlines())
results=[]
for p in sorted((OUT/'pages').glob('*.tex')):
    s=no_comments(p.read_text());errors=[];depth=0
    for match in re.finditer(r'(?<!\\)[{}]',s):
        depth+=1 if match[0]=='{' else -1
        if depth<0:errors.append('closing brace without opening');break
    if depth:errors.append(f'brace depth {depth}')
    controls=re.findall(r'\\(?:[A-Za-z]+|.)',s)
    if controls.count(r'\[')!=controls.count(r'\]'):errors.append('display delimiter imbalance')
    if len(re.findall(r'(?<!\\)\$',s))%2:errors.append('dollar delimiter imbalance')
    stack=[]
    for x in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
        if x[1]=='begin':stack.append(x[2])
        elif not stack or stack.pop()!=x[2]:errors.append('environment mismatch '+x[2])
    if stack:errors.append('unclosed environment(s): '+','.join(stack))
    if re.search(r'\\(?:newcommand|renewcommand|def)\b',s):errors.append('macro definition in fragment')
    results.append({'file':p.name,'errors':errors,'unsure':s.count(r'\unsure{'),'illegible':s.count(r'\illegible{'),'deleted':s.count(r'\deleted{'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
print(json.dumps(results,ensure_ascii=False,indent=2))
raise SystemExit(any(x['errors'] for x in results))
