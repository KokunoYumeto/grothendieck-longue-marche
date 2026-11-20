"""Structural TeX checks only; no compilation or linguistic recognition."""
from pathlib import Path
import re,json
OUT=Path(__file__).resolve().parents[1]
results=[]
for p in sorted((OUT/'pages').glob('*.tex')):
    t='\n'.join(re.split(r'(?<!\\)%',x)[0] for x in p.read_text().splitlines())
    errors=[];depth=0
    if re.search(r'\\(?:newcommand|renewcommand|providecommand|def|gdef|DeclareMathOperator)\b',t):
        errors.append('page defines or redefines a macro; supplied conventions must remain unchanged')
    for m in re.finditer(r'(?<!\\)[{}]',t):
        depth+=1 if m.group()=='{' else -1
        if depth<0: errors.append('closing brace before opening');break
    if depth:errors.append('brace balance '+str(depth))
    for a,b in [(r'\[',r'\]'),(r'\(',r'\)')]:
        if t.count(a)!=t.count(b):errors.append('unbalanced '+a+b)
    if len(re.findall(r'(?<!\\)\$',t))%2:errors.append('odd number of $ delimiters')
    stack=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',t):
        if m[1]=='begin':stack.append(m[2])
        elif not stack or stack.pop()!=m[2]:errors.append('environment mismatch '+m[0])
    if stack:errors.append('unclosed environments '+str(stack))
    if '\\begin{tikzcd}' in t and 'ampersand replacement=\\&' not in t: errors.append('tikzcd missing ampersand replacement')
    results.append(dict(file=p.name,errors=errors,unsure=t.count('\\unsure{'),illegible=t.count('\\illegible{'),deleted=t.count('\\deleted{')))
(OUT/'syntax_check.json').write_text(json.dumps(results,indent=2))
print(json.dumps(dict(pages=len(results),errors=[r for r in results if r['errors']],marks={k:sum(r[k] for r in results) for k in ['unsure','illegible','deleted']})))
