#!/usr/bin/env python3
"""Restore an old encoded payload using an exact prefix and retained byte tail."""
from pathlib import Path
import argparse,hashlib,json
ap=argparse.ArgumentParser()
ap.add_argument('recipe',type=Path)
ap.add_argument('target',type=Path)
ap.add_argument('--sha256')
a=ap.parse_args()
root=Path(__file__).resolve().parents[1]
m=json.loads(a.recipe.read_text())
assert m['codec']=='PBC_PREFIX_PATCH01' and m['entire_original_byte_comparison']
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()
source=root/m['source_path'];tail=root/m['tail_path']
assert source.stat().st_size==m['source_bytes'] and sha(source)==m['source_sha256']
assert tail.stat().st_size==m['tail_bytes'] and sha(tail)==m['tail_sha256']
if a.target.exists():raise SystemExit('Refusing to overwrite '+str(a.target))
a.target.parent.mkdir(parents=True,exist_ok=True)
h=hashlib.sha256();count=0
with source.open('rb') as inp,a.target.open('xb') as out:
    left=m['prefix_bytes']
    while left:
        b=inp.read(min(left,1<<20));assert b
        out.write(b);h.update(b);count+=len(b);left-=len(b)
    with tail.open('rb') as inp_tail:
        for b in iter(lambda:inp_tail.read(1<<20),b''):
            out.write(b);h.update(b);count+=len(b)
assert count==m['original_bytes'] and h.hexdigest()==m['original_sha256']
if a.sha256:assert h.hexdigest()==a.sha256
print('RESTORED exact prefix patch',count,'bytes SHA256',h.hexdigest())

