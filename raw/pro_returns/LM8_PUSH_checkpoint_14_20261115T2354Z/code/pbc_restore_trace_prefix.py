#!/usr/bin/env python3
"""Restore an exactly verified decoded prefix of another restored gzip log."""
from pathlib import Path
import argparse,gzip,hashlib,json
ap=argparse.ArgumentParser();ap.add_argument('recipe',type=Path);ap.add_argument('source',type=Path);ap.add_argument('target',type=Path);a=ap.parse_args()
m=json.loads(a.recipe.read_text());assert m['entire_decoded_byte_hash_verified']
if a.target.exists():raise SystemExit('Refusing to overwrite '+str(a.target))
a.target.parent.mkdir(parents=True,exist_ok=True)
h=hashlib.sha256();n=records=0;left=m['decoded_bytes'];last=b''
with gzip.open(a.source,'rb') as inp,a.target.open('xb') as raw,gzip.GzipFile(filename='',mode='wb',fileobj=raw,compresslevel=1,mtime=0) as out:
 while left:
  b=inp.read(min(left,1<<20));assert b,'source shorter than verified prefix'
  h.update(b);out.write(b);n+=len(b);records+=b.count(b'\n');left-=len(b);last=b[-1:]
assert last==b'\n' and n==m['decoded_bytes'] and records==m['decoded_records'] and h.hexdigest()==m['decoded_sha256']
print('RESTORED exact prefix',n,'bytes',records,'records SHA256',h.hexdigest())
