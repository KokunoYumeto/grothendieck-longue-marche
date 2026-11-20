"""Structural checks only; these cannot establish palaeographic correctness."""
from pathlib import Path
import re, json, hashlib
OUT=Path(__file__).resolve().parents[1]
errors=[];details=[]
pages=sorted((OUT/'pages').glob('*.tex'))
for p in pages+[OUT/'SP48_CW_104_transcription.tex']:
    if not p.exists():continue
    t=p.read_text()
    # Remove unescaped TeX comments for delimiter tests.
    t='\n'.join(re.split(r'(?<!\\)%',line,maxsplit=1)[0] for line in t.splitlines())
    brace=0
    for token in re.findall(r'\\.|[{}]',t):
        if token=='{':brace+=1
        elif token=='}':
            brace-=1
            if brace<0:errors.append(f'{p.name}: closing brace before opening');break
    if brace:errors.append(f'{p.name}: brace balance {brace}')
    stack=[]
    for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',t):
        direction,env=m.groups()
        if direction=='begin':stack.append(env)
        elif not stack or stack.pop()!=env:errors.append(f'{p.name}: mismatched environment {env}')
    if stack:errors.append(f'{p.name}: unclosed environments {stack}')
    # A row break followed by an optional gap, \\\\[-.3ex], is not a display opener.
    displays=re.findall(r'(?<!\\)\\\[|(?<!\\)\\\]',t);d=0
    for token in displays:
        d+=1 if token=='\\[' else -1
        if d not in (0,1):errors.append(f'{p.name}: display delimiter ordering');break
    if d:errors.append(f'{p.name}: display delimiter balance {d}')
    dollars=len(re.findall(r'(?<!\\)\$',t))
    if dollars%2:errors.append(f'{p.name}: odd dollar count {dollars}')
    for m in re.finditer(r'\\begin\{tikzcd\}(.*?)(?=\\end\{tikzcd\})',t,re.S):
        if 'ampersand replacement=\\&' not in m.group(1):errors.append(f'{p.name}: tikz-cd lacks ampersand replacement')
    details.append({'file':p.name,'scan_markers':re.findall(r'\\scanpage\{([^}]*)\}',t),'unsure':t.count('\\unsure{'),'illegible':t.count('\\illegible{'),'deleted':t.count('\\deleted{'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
combined=(OUT/'SP48_CW_104_transcription.tex').read_text()
if len(pages)==16:
    if re.findall(r'\\scanpage\{([^}]*)\}',combined)!=list(map(str,range(2,18))):errors.append('Combined scan order wrong')
    if combined.count('\\cotefile{104}')!=1:errors.append('Combined cote marker count wrong')
    if combined.strip()!='\n\n'.join(p.read_text().rstrip() for p in pages).strip():errors.append('Combined file does not equal ordered pages')
result={'pages':len(pages),'errors':errors,'details':details,'scope':'TeX delimiter and environment balance, ordered concatenation, SHA-256; not a compilation or reading check.'}
(OUT/'validation.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(result,ensure_ascii=False))
raise SystemExit(bool(errors))
