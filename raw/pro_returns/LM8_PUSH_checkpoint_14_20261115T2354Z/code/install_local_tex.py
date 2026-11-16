#!/usr/bin/env python3
"""Install the minimal TeX Live packages for this paper inside the workspace.

This bootstrap writes no system files. Sources: TeX Live's public package
database and matching package archives. Its output is a reproducible package
inventory; the third-party runtime is not part of the research archive.
"""
import concurrent.futures, hashlib, json, lzma, os, pathlib, tarfile, urllib.request, threading
ROOT=pathlib.Path(__file__).resolve().parents[2]/'tex-runtime'
ROOT.mkdir(exist_ok=True)
BASE='https://ctan.math.illinois.edu/systems/texlive/tlnet/'
db=ROOT/'texlive.tlpdb'
if not db.exists():
    db.write_bytes(lzma.decompress(urllib.request.urlopen(BASE+'tlpkg/texlive.tlpdb.xz',timeout=60).read()))
entries={b.splitlines()[0][5:]:b for b in db.read_text().split('\n\n') if b.startswith('name ')}
wanted=set()
extract_lock=threading.Lock()
def add(n):
    n=n.replace('.ARCH','.x86_64-linux')
    if n in wanted: return
    if n not in entries: raise RuntimeError('missing package '+n)
    wanted.add(n)
    for l in entries[n].splitlines():
        if l.startswith('depend '): add(l[7:].strip())
for n in ['latex-bin','fontspec','amsfonts','amscls','mathtools','geometry','booktabs','enumitem','microtype','natbib','hyperref','xurl','tools','xcolor','kpathsea']:
    add(n)
print('Packages:',len(wanted),flush=True)
def fetch(n):
    archive=ROOT/'archives'/(n+'.tar.xz');archive.parent.mkdir(exist_ok=True)
    if not archive.exists():
        data=urllib.request.urlopen(BASE+'archive/'+n+'.tar.xz',timeout=90).read()
        archive.write_bytes(data)
    data=archive.read_bytes()
    expected=next((l.split()[1] for l in entries[n].splitlines() if l.startswith('containerchecksum ')),None)
    digest=hashlib.sha512(data).hexdigest()
    if expected is not None and digest!=expected: raise RuntimeError('checksum mismatch '+n)
    with extract_lock, tarfile.open(archive) as t:
        target=ROOT/'texmf-dist' if '\nrelocated 1\n' in '\n'+entries[n]+'\n' else ROOT
        target.mkdir(exist_ok=True)
        t.extractall(target,filter='data')
    print('installed',n,len(data),flush=True)
    return {'package':n,'bytes':len(data),'sha512':digest,'source':BASE+'archive/'+n+'.tar.xz'}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    results=list(pool.map(fetch,sorted(wanted)))
out=pathlib.Path(__file__).with_suffix('.manifest.json')
out.write_text(json.dumps(results,indent=2)+'\n')
print('Wrote',out,flush=True)
