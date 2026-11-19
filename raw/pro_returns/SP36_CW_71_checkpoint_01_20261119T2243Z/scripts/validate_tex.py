"""Static LaTeX delimiter checks only; no compilation or recognition."""
from pathlib import Path
import re,sys,json,hashlib
OUT=Path(__file__).resolve().parents[1]
def check(p):
    raw=p.read_text();s=re.sub(r'(?<!\\)%[^\n]*','',raw);errors=[]
    for opening,closing,label in [('{','}','braces')]:
        level=0
        for m in re.finditer(r'(?<!\\)[{}]',s):
            level+=1 if m[0]=='{' else -1
            if level<0:errors.append('unexpected closing brace');break
        if level:errors.append(f'brace balance {level}')
    ds=[]
    for m in re.finditer(r'(?<!\\)(?:\\\[|\\\])',s):
        if m[0]=='\\[':ds.append(m.start())
        elif ds:ds.pop()
        else:errors.append('unexpected \\]')
    if ds:errors.append('unclosed \\[')
    if len(re.findall(r'(?<!\\)\$',s))%2:errors.append('odd dollar count')
    es=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
        if m[1]=='begin':es.append(m[2])
        elif not es or es.pop()!=m[2]:errors.append('environment mismatch '+m[2])
    if es:errors.append('unclosed environments '+repr(es))
    return {'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'errors':errors,'unsure':raw.count('\\unsure{'),'illegible':raw.count('\\illegible{'),'deleted':raw.count('\\deleted{')}
results=[check(p) for p in sorted((OUT/'pages').glob('*.tex'))]
combined=OUT/'SP36_CW_71_transcription.tex'
if combined.exists():results.append(check(combined))
(OUT/'validation.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
sys.exit(bool(any(r['errors'] for r in results)))
