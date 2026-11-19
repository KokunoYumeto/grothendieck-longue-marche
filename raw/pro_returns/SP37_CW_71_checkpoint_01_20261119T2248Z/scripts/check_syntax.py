#!/usr/bin/env python3
"""Check fragment delimiters and exact concatenation without compiling or changing readings."""
from pathlib import Path
import re,json,hashlib
root=Path(__file__).resolve().parents[1]
results=[]
for p in sorted((root/'pages').glob('*.tex')):
    text=p.read_text();clean=re.sub(r'(?<!\\)%[^\n]*','',text);errors=[]
    depth=0
    for match in re.finditer(r'(?<!\\)[{}]',clean):
        depth+=1 if match.group()=='{' else -1
        if depth<0:errors.append('closing brace before opener');depth=0
    if depth:errors.append(f'brace balance {depth}')
    if len(re.findall(r'(?<!\\)\$',clean))%2:errors.append('odd number of dollar delimiters')
    for a,b in [(r'\[',r'\]'),(r'\(',r'\)')]:
        if clean.count(a)!=clean.count(b):errors.append(f'{a}/{b} mismatch')
    stack=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
        if m[1]=='begin':stack.append(m[2])
        elif not stack or stack.pop()!=m[2]:errors.append('environment mismatch at '+m[0])
    if stack:errors.append('unclosed environments '+str(stack))
    results.append({'page':p.name,'errors':errors,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
combined=root/'SP37_CW_71_transcription.tex'
expected='\n'.join(p.read_text().rstrip() for p in sorted((root/'pages').glob('*.tex')))+'\n'
summary={'results':results,'concatenation_exact':combined.exists() and combined.read_text()==expected,'unsure':expected.count('\\unsure{'),'illegible':expected.count('\\illegible{'),'deleted':expected.count('\\deleted{'),'cotefile_count':expected.count('\\cotefile{71}'),'scan_numbers':re.findall(r'\\scanpage\{(\d+)\}',expected)}
(root/'syntax_check.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False))
