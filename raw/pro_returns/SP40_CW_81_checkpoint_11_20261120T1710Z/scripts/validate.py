"""Structural validation only: no OCR, TeX compilation, or reading substitution."""
from pathlib import Path
import re,json,csv,hashlib,collections
R=Path(__file__).resolve().parents[1]
expected=[2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
def uncomment(t):
    return '\n'.join(re.split(r'(?<!\\)%',l,maxsplit=1)[0] for l in t.splitlines())
def check_tex(p):
    raw=p.read_text();s=uncomment(raw);errors=[];depth=0
    for m in re.finditer(r'\\.|[{}]',s):
        tok=m.group()
        if tok=='{':depth+=1
        elif tok=='}':
            depth-=1
            if depth<0:errors.append('unmatched closing brace');depth=0
    if depth:errors.append(f'unclosed braces: {depth}')
    stack=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
        typ,name=m.groups()
        if typ=='begin':stack.append(name)
        elif not stack or stack.pop()!=name:errors.append('environment mismatch at '+m.group())
    if stack:errors.append('unclosed environments '+repr(stack))
    for a,b in [('\\[','\\]'),('\\(','\\)')]:
        seq=[tok for tok in re.findall(r'\\(?:[A-Za-z]+|.)',s) if tok in (a,b)];d=0
        for tok in seq:
            d+=1 if tok==a else -1
            if d<0:errors.append('math delimiter order '+a);d=0
        if d:errors.append('math delimiters '+a)
    if len(re.findall(r'(?<!\\)\$',s))%2:errors.append('odd dollar count')
    forbidden=re.findall(r'\\(?:documentclass|usepackage|newcommand|renewcommand|input|include|includegraphics)\b',s)
    if forbidden:errors.append('non-fragment commands '+repr(forbidden))
    return {'file':str(p.relative_to(R)),'errors':errors,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'marks':{k:len(re.findall(r'\\'+k+r'\{',s)) for k in ['unsure','illegible','deleted','inserted','margin','figure','diagram']}}
records=[json.loads(p.read_text()) for p in sorted((R/'records').glob('scan*.json'))]
pages=[R/'pages'/r['filename'] for r in records]
results=[check_tex(p) for p in pages]
combined=R/'SP40_CW_81_transcription.tex'
if combined.exists():results.append(check_tex(combined))
issues=[]
scans=[r['scan'] for r in records]
if scans!=expected[:len(scans)]:issues.append('Scan sequence is not the expected prefix')
if len(scans)!=24:issues.append(f'Only {len(scans)} of 24 scans complete')
if combined.exists():
    target='\n'.join(p.read_text().rstrip()+'\n' for p in pages)
    if combined.read_text()!=target:issues.append('Combined transcription differs from concatenated pages')
    c=uncomment(combined.read_text())
    if len(re.findall(r'\\cotefile\{81\}',c))!=1:issues.append('Cote marker count differs from one')
    if [int(x) for x in re.findall(r'\\scanpage\{(\d+)\}',c)]!=scans:issues.append('Scan markers differ from decided scans')
for r in records:
    inventory_kinds={'text','display','diagram','drawing','margin note','insertion','deletion'}
    collation_kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
    for role in ['A','B','C']:
        p=R/'readers'/f"{r['scan']:03d}"/role/'report.json'
        if not p.exists():issues.append(f"scan {r['scan']} reader {role} absent");continue
        d=json.loads(p.read_text())
        if not all(d.get(k) for k in ['full_image_viewed','halves_viewed','complete_visual_read']):issues.append(f"scan {r['scan']} reader {role} does not attest complete image reading")
    if not r.get('main_adjudicated'):issues.append(f"scan {r['scan']} main adjudication not complete")
    for i in r['inventory']:
        if i['transcribed']!='yes':issues.append(f"scan {r['scan']} untranscribed inventory element")
        if i['kind'] not in inventory_kinds:issues.append(f"scan {r['scan']} invalid inventory kind {i['kind']}")
    ids=[d['id'] for d in r['decisions']]
    if len(ids)!=len(set(ids)):issues.append(f"scan {r['scan']} duplicate decision IDs")
    for d in r['decisions']:
        if set(d['readers'])!={'A','B','C'}:issues.append(f"scan {r['scan']} missing reader alternative at {d['id']}")
        if d['kind'] not in collation_kinds:issues.append(f"scan {r['scan']} invalid collation kind at {d['id']}")
        if d.get('diff_H') and r['hua_has']!='text':issues.append(f"scan {r['scan']} H row on a page without H text")
        if d['confidence'] not in {'high','medium','low'}:issues.append(f"scan {r['scan']} invalid confidence at {d['id']}")
        if d.get('C_doubt_status') not in {None,'resolved','retained'}:issues.append(f"scan {r['scan']} invalid C doubt status at {d['id']}")
out={'complete_scans':scans,'structural_results':results,'record_issues':issues,'tex_ok':all(not x['errors'] for x in results)}
(R/'checks/structural_validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
