#!/usr/bin/env python3
"""Portable exact PBCBIN01 decoder. Input may be .xz; output is original JSONL."""
import argparse,gzip,hashlib,io,lzma,re,sys
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);ap.add_argument('output',type=Path)
ap.add_argument('--sha256');a=ap.parse_args()
if a.output.exists():raise SystemExit('Refusing to overwrite '+str(a.output))
raw=lzma.open(a.input,'rb') if a.input.suffix=='.xz' else a.input.open('rb')
inp=io.BufferedReader(raw,1<<20)
def exact(n):
 b=inp.read(n)
 if len(b)!=n:raise ValueError('truncated binary proof stream')
 return b
def uv():
 n=s=0
 while True:
  c=exact(1)[0];n|=(c&127)<<s
  if c<128:return n
  s+=7
  if s>63:raise ValueError('invalid varint')
def big():return int.from_bytes(exact(uv()),'little')
assert exact(8)==b'PBCBIN01';N=big();previous=0;h=hashlib.sha256();count=0
a.output.parent.mkdir(parents=True,exist_ok=True)
base=a.output.open('xb');out=gzip.GzipFile(filename='',mode='wb',fileobj=base,compresslevel=1,mtime=0) if a.output.suffix=='.gz' else base
while True:
 tag=inp.read(1)
 if not tag:break
 op=tag[0]
 if op==0:
  line=exact(uv())
  m=re.match(rb'^\["leaf",(0|[1-9][0-9]*),',line)
  if m and int(m[1])<2**64:previous=int(m[1])
 else:
  assert op in (1,2,3);idx=previous+uv();x=idx-uv();y=uv() if op==1 else None
  if op!=3:
   t=exact(1)[0];assert t<=5;v=big();q=(t//2-1)*N+(-v if t&1 else v)
  if op==1:line=f'["sub",{idx},{x},{q},{y}]\n'.encode()
  elif op==2:line=f'["mul",{idx},{q},{x}]\n'.encode()
  else:line=f'["neg",{idx},{x}]\n'.encode()
  previous=idx
 out.write(line);h.update(line);count+=len(line)
out.close()
if out is not base:base.close()
inp.close()
if a.sha256:assert h.hexdigest()==a.sha256,(h.hexdigest(),a.sha256)
print('RESTORED',count,'bytes SHA256',h.hexdigest())
