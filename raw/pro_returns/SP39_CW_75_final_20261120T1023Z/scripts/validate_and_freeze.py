#!/usr/bin/env python3
"""Syntax-only checks and an explicit freeze; does not edit transcription."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re, sys

root=Path(__file__).resolve().parents[1]
scans=[26,27,28,30,31,32,33]
paths=[root/f'pages/J75-04_75_scan{s:03}.tex' for s in scans]
combined=root/'SP39_CW_75_transcription.tex'
mode=sys.argv[1] if len(sys.argv)>1 else 'check'

def utc():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def uncomment(s):return re.sub(r'(?<!\\)%[^\n]*','',s)
def check(path):
    s=uncomment(path.read_text()); errors=[]; depth=0
    for i,ch in enumerate(s):
        if ch in '{}':
            count=0;j=i-1
            while j>=0 and s[j]=='\\':count+=1;j-=1
            if count%2:continue
            depth+=1 if ch=='{' else -1
            if depth<0:errors.append(f'extra close brace at {i}');depth=0
    if depth:errors.append(f'unclosed brace depth {depth}')
    tokens=re.findall(r'\\begin\{([^}]+)\}|\\end\{([^}]+)\}',s);stack=[]
    for begin,end in tokens:
        if begin:stack.append(begin)
        elif not stack or stack.pop()!=end:errors.append('environment mismatch '+end)
    if stack:errors.append('unclosed environments '+repr(stack))
    if len(re.findall(r'(?<!\\)\$',s))%2:errors.append('odd inline dollar count')
    # A line break with optional spacing, \\[...], is not display math.
    display_tokens=['\\'+bracket for slashes,bracket in re.findall(r'(\\+)([\[\]])',s) if len(slashes)%2];d=0
    for t in display_tokens:
        d+=1 if t=='\\[' else -1
        if d not in (0,1):errors.append('display nesting/ordering')
    if d:errors.append('display imbalance')
    for env in re.findall(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',s,re.S):
        if 'ampersand replacement=\\&' not in env:errors.append('tikz-cd missing ampersand replacement')
        if re.search(r'(?<!\\)&',env):errors.append('bare tikz-cd ampersand')
    if re.search(r'\\(?:newcommand|renewcommand|documentclass)\b',s):errors.append('fragment contains forbidden definition/preamble')
    return errors

if mode=='verify':
    saved=json.loads((root/'frozen_hashes.json').read_text())
    errors=[name for name,digest in saved.items() if sha(root/name)!=digest]
    assert not errors,'Frozen transcription changed: '+repr(errors)
    with (root/'progress.log').open('a') as f:f.write('frozen hashes unchanged '+utc()+'; all seven page files and combined transcription verified\n')
    print('All 8 frozen SHA-256 values unchanged.')
    sys.exit()

assert all(p.exists() for p in paths),'Missing page files'
if mode=='freeze':combined.write_text('\n'.join(p.read_text().rstrip() for p in paths)+'\n')
assert combined.exists(),'Combined file missing'
errors={str(p.relative_to(root)):check(p) for p in paths+[combined]}
errors={k:v for k,v in errors.items() if v}
assert not errors,json.dumps(errors,ensure_ascii=False)
s=combined.read_text()
assert re.findall(r'\\scanpage\{(\d+)\}',s)==list(map(str,scans))
assert s.count('\\cotefile{75}')==1
inventory=list(csv.DictReader((root/'SP39_CW_75_inventory.csv').open()))
assert {int(r['scan']) for r in inventory}==set(scans)
assert all(r['transcribed']=='yes' for r in inventory)
collation=list(csv.DictReader((root/'SP39_CW_75_collation.tsv').open(),delimiter='\t'))
assert all(int(r['our_scan'])!=30 for r in collation)
assert all(int(r['their_page'])==int(r['our_scan'])-1 for r in collation)
allowed_kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
assert all(r['kind'] in allowed_kinds for r in collation)
assert all(r['marked_in_H'] in {'yes','no'} for r in collation)
assert all(r['confidence'] in {'high','medium','low'} for r in collation)
counts={m:s.count('\\'+m+'{') for m in ['unsure','illegible','deleted','inserted','margin','diagram','figure']}
report={'utc':utc(),'status':'passed','scope':'braces, dollar parity, display delimiters, environments, diagram separators, scan order, cote count, inventory completion, H page numbering; final consolidated fragment checked statically; no final LaTeX compilation','mark_counts':counts,'inventory_rows':len(inventory),'collation_rows':len(collation)}
(root/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
if mode=='freeze':
    hashes={str(p.relative_to(root)):sha(p) for p in paths+[combined]}
    (root/'frozen_hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
    with (root/'progress.log').open('a') as f:
        f.write('syntax balance checks passed '+utc()+'; no final compilation performed\n')
        f.write('transcription frozen '+utc()+'\n')
        for name,h in hashes.items():f.write('SHA-256 '+h+'  '+name+'\n')
print(json.dumps(report,ensure_ascii=False))
