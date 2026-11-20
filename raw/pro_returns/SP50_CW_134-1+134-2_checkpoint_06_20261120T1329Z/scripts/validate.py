"""Required structural checks only; no compiler and no text recognition."""
from pathlib import Path
import re,json,csv,hashlib,argparse
from datetime import datetime,timezone
O=Path(__file__).resolve().parents[1];P='SP50_CW_134-1+134-2'
p=argparse.ArgumentParser();p.add_argument('--partial',action='store_true');p.add_argument('--freeze',action='store_true');p.add_argument('--verify-frozen',action='store_true');a=p.parse_args()
pages=json.loads((O/'page_order.json').read_text());errors=[];rows=[];allfiles=[]
def escaped(t,i):
    n=0;i-=1
    while i>=0 and t[i]=='\\':n+=1;i-=1
    return bool(n%2)
def uncomment(t):
    out=[];i=0
    while i<len(t):
        if t[i]=='%' and not escaped(t,i):
            j=t.find('\n',i)
            if j<0:break
            i=j
        out.append(t[i]);i+=1
    return ''.join(out)
def check(path):
    text=path.read_text();s=uncomment(text);stack=[]
    for m in re.finditer(r'[{}]',s):
        if escaped(s,m.start()):continue
        if m.group()=='{':stack.append(m.start())
        elif stack:stack.pop()
        else:errors.append(f'{path.name}: unmatched closing brace at {m.start()}')
    if stack:errors.append(f'{path.name}: {len(stack)} unmatched opening braces')
    if sum(not escaped(s,m.start()) for m in re.finditer(r'\$',s))%2:errors.append(f'{path.name}: odd dollar delimiter count')
    ds=[]
    for m in re.finditer(r'\\([\[\]])',s):
        if m.group(1)=='[':ds.append(m.start())
        elif ds:ds.pop()
        else:errors.append(f'{path.name}: unmatched display end')
    if ds:errors.append(f'{path.name}: unclosed displays')
    es=[]
    for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',s):
        if m.group(1)=='begin':es.append(m.group(2))
        elif not es or es.pop()!=m.group(2):errors.append(f'{path.name}: environment nesting at {m.group()}')
    if es:errors.append(f'{path.name}: unclosed environments {es}')
    for forbidden in ['documentclass','newcommand','def','uncertain','struck','marginal','note','ill','add','page']:
        if re.search(r'\\'+forbidden+r'(?![A-Za-z])',s):errors.append(f'{path.name}: forbidden or foreign macro {forbidden}')
    for diagram in re.finditer(r'\\begin\{tikzcd\}(.*?)(?=\\end\{tikzcd\})',s,re.S):
        if 'ampersand replacement=\\&' not in diagram.group():errors.append(f'{path.name}: tikzcd missing ampersand replacement')
    return [len(re.findall(r'\\'+macro+r'\{',s)) for macro in ['unsure','illegible','deleted']]

for page in pages:
    path=O/'pages'/Path(page['codex_file']).name
    if not path.exists():
        if not a.partial:errors.append(f'Missing {path.name}')
        continue
    allfiles.append(path);counts=check(path);rows.append([path.name,*counts])
    plain=uncomment(path.read_text())
    nums=re.findall(r'\\scanpage\{(\d+)\}',plain)
    if nums!=[str(int(page['our_scan']))]:errors.append(path.name+': wrong or repeated scanpage marker')
    cotes=re.findall(r'\\cotefile\{([^{}]+)\}',plain)
    expected_cote=[page['cote']] if int(page['our_scan']) in [2,146] else []
    if cotes!=expected_cote:errors.append(path.name+': wrong or repeated cotefile marker')
combined=O/(P+'_transcription.tex')
if combined.exists():
    check(combined);allfiles.append(combined)
    expected='\n'.join(p.read_text().rstrip()+'\n' for p in allfiles[:-1])
    if combined.read_text()!=expected:errors.append('Combined transcription is not ordered page concatenation')
else:errors.append('Combined transcription missing')
for f in [O/(P+'_inventory.csv'),O/(P+'_collation.tsv'),O/'CHECK_EVENTS.tsv']:
    with f.open() as h:
        data=list(csv.DictReader(h,delimiter='\t' if f.suffix=='.tsv' else ','))
    if 'inventory' in f.name:
        for x in data:
            if x['transcribed']!='yes':errors.append(f'Untranscribed inventory element: {x}')
    if 'collation' in f.name and any(x['our_scan']=='2' for x in data):errors.append('H rows for scan 002 despite absent H text')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
summary={'utc':now,'scope':'partial' if a.partial else 'complete','pages':len(rows),'counts':dict(zip(['unsure','illegible','deleted'],[sum(r[i] for r in rows) for i in range(1,4)])),'errors':errors,'page_counts':rows}
(O/'validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
if a.freeze:
    assert not a.partial
    assert not errors,errors
    assert len(rows)==29
    hashes={str(p.relative_to(O)):hashlib.sha256(p.read_bytes()).hexdigest() for p in allfiles}
    (O/'FROZEN_SHA256.json').write_text(json.dumps(hashes,indent=2)+'\n')
    with (O/'progress.log').open('a') as f:
        f.write('transcription frozen '+now+'\n')
        for name,h in hashes.items():f.write('SHA-256 '+h+' '+name+'\n')
if a.verify_frozen:
    hashes=json.loads((O/'FROZEN_SHA256.json').read_text())
    changed=[name for name,h in hashes.items() if hashlib.sha256((O/name).read_bytes()).hexdigest()!=h]
    assert not changed,changed
    with (O/'progress.log').open('a') as f:f.write('frozen hashes verified unchanged '+now+f' ({len(hashes)} files)\n')
print(json.dumps({k:v for k,v in summary.items() if k!='page_counts'},ensure_ascii=False))
if errors:raise SystemExit(1)
