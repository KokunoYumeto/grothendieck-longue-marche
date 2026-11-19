#!/usr/bin/env python3
"""Check delivered fragments and record integrity; does not compile or read ink."""
from pathlib import Path
import argparse,re,json,hashlib,datetime,csv
O=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--freeze',action='store_true');p.add_argument('--verify-frozen',action='store_true');a=p.parse_args()
files=sorted((O/'pages').glob('*.tex'))
results=[];errors=[]
for f in files:
    text=f.read_text();clean=re.sub(r'(?<!\\)%[^\n]*','',text)
    depth=0
    for m in re.finditer(r'(?<!\\)[{}]',clean):
        depth+=1 if m.group()=='{' else -1
        if depth<0:errors.append(f'{f.name}: negative brace depth');break
    if depth:errors.append(f'{f.name}: brace depth {depth}')
    env=[]
    for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',clean):
        if m[1]=='begin':env.append(m[2])
        elif not env or env.pop()!=m[2]:errors.append(f'{f.name}: mismatched environment {m[0]}')
    if env:errors.append(f'{f.name}: open environments {env}')
    for left,right in [(r'\[',r'\]'),(r'\(',r'\)')]:
        if clean.count(left)!=clean.count(right):errors.append(f'{f.name}: {left}/{right} mismatch')
    if len(re.findall(r'(?<!\\)\$',clean))%2:errors.append(f'{f.name}: odd dollar count')
    if re.search(r'\\(?:newcommand|renewcommand|def|documentclass|usepackage)\b',clean):errors.append(f'{f.name}: fragment defines commands or preamble')
    results.append({'file':f.name,'unsure':clean.count(r'\unsure{'),'illegible':clean.count(r'\illegible{'),'deleted':clean.count(r'\deleted{'),'inserted':clean.count(r'\inserted{'),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
combined=O/'SP34_CW_156-5_transcription.tex'
if combined.exists():
    expected='\n\n'.join(f.read_text().rstrip() for f in files)+'\n'
    if combined.read_text()!=expected:errors.append('Combined fragment differs from ordered page concatenation')
now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
report={'checked_utc':now,'pages':len(files),'results':results,'errors':errors,'scope':'Structural validation only, not visual or mathematical verification; no LaTeX compilation attempted.'}
(O/'documentation/structural_audit.json').write_text(json.dumps(report,indent=2)+'\n')
if a.freeze:
    if len(files)!=24 or errors:raise SystemExit('Cannot freeze: incomplete page set or structural errors')
    hashes={str(f.relative_to(O)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files+[combined]}
    (O/'documentation/frozen_sha256.json').write_text(json.dumps(hashes,indent=2)+'\n')
    with (O/'progress.log').open('a') as log:
        log.write('transcription frozen '+now+'\n')
        for f,h in hashes.items():log.write('SHA-256 '+h+'  '+f+'\n')
if a.verify_frozen:
    hashes=json.loads((O/'documentation/frozen_sha256.json').read_text())
    bad=[f for f,h in hashes.items() if hashlib.sha256((O/f).read_bytes()).hexdigest()!=h]
    if bad:raise SystemExit('Frozen hashes changed: '+str(bad))
    with (O/'progress.log').open('a') as log:log.write('frozen hashes unchanged '+now+' ('+str(len(hashes))+' files)\n')
print(json.dumps({'pages':len(files),'errors':errors,'marks':{k:sum(r[k] for r in results) for k in ['unsure','illegible','deleted','inserted']}}))
if errors:raise SystemExit(1)
