#!/usr/bin/env python3
"""Exact reversible packing of retained JSONL source/leaf records.

Sorted sparse indices are delta-coded, integer coefficients use signed
varints, and original compact/GAP list formatting is retained explicitly.
Every other record is stored verbatim. This changes no mathematical data.
"""
from pathlib import Path
import argparse,hashlib,io,json,lzma,sys,time
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
KINDS=['target','modulus','coordinate','extra','identity']
def uvslow(n):
 out=bytearray()
 while n>=128:out.append((n&127)|128);n>>=7
 out.append(n);return bytes(out)
CACHE=[uvslow(n) for n in range(16384)]
def uv(n):return CACHE[n] if n<16384 else uvslow(n)
def zz(n):return 2*n if n>=0 else -2*n-1
def gap(v):return '[ '+', '.join(map(str,v))+' ]'
def formatted(r,style):
 if style==1:return ('["leaf",'+str(r[1])+',"'+r[2]+'",'+gap(r[3])+','+gap(r[4])+']\n').encode()
 return (json.dumps(r,separators=(',',':'))+'\n').encode()
def encode(source,target):
 h=hashlib.sha256();count=records=packed=0
 with source.open('rb') as inp,lzma.LZMAFile(target,'wb',filters=[{'id':lzma.FILTER_LZMA2,'preset':3,'dict_size':64<<20}]) as out:
  out.write(b'PBCLEAF1')
  for line in inp:
   h.update(line);count+=len(line);records+=1;r=json.loads(line);style=0
   if r[0]=='leaf' and len(r)==5 and r[2] in KINDS and len(r[4])%2==0:
    inds=r[4][::2]
    if inds==sorted(set(inds)) and (not inds or inds[0]>0):
     if formatted(r,1)==line:style=1
     elif formatted(r,2)==line:style=2
   if not style:out.write(b'\0'+uv(len(line))+line);continue
   b=bytearray([style,KINDS.index(r[2])]);b+=uv(r[1]);b+=uv(len(r[3]))
   for n in r[3]:b+=uv(zz(n))
   b+=uv(len(r[4])//2);prev=0
   for i,c in zip(r[4][::2],r[4][1::2]):b+=uv(i-prev);b+=uv(zz(c));prev=i
   out.write(b);packed+=1
 return {'original_bytes':count,'original_sha256':h.hexdigest(),'records':records,'packed_records':packed}
def decoded_lines(source):
 with lzma.open(source,'rb') as raw:
  inp=io.BufferedReader(raw,1<<20)
  def exact(n):
   b=inp.read(n)
   if len(b)!=n:raise ValueError('truncated leaf codec')
   return b
  def get():
   n=s=0
   while True:
    b=exact(1)[0];n|=(b&127)<<s
    if b<128:return n
    s+=7
  def signed():
   n=get();return -(n//2)-1 if n&1 else n//2
  assert exact(8)==b'PBCLEAF1'
  while True:
   t=inp.read(1)
   if not t:return
   style=t[0]
   if style==0:yield exact(get());continue
   assert style in (1,2);kind=KINDS[exact(1)[0]];idx=get();meta=[signed() for _ in range(get())];v=[];prev=0
   for _ in range(get()):
    prev+=get();v.extend((prev,signed()))
   yield formatted(['leaf',idx,kind,meta,v],style)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['encode','decode']);ap.add_argument('source',type=Path);ap.add_argument('target',type=Path);ap.add_argument('--sha256');a=ap.parse_args();start=time.time()
 if a.target.exists():raise SystemExit('Refusing to overwrite '+str(a.target))
 if a.mode=='encode':
  report=encode(a.source,a.target);h=hashlib.sha256();n=0
  for b in decoded_lines(a.target):h.update(b);n+=len(b)
  assert n==report['original_bytes'] and h.hexdigest()==report['original_sha256']
  report.update({'codec':'PBC_LEAF01','stored_bytes':a.target.stat().st_size,'stored_sha256':hashlib.sha256(a.target.read_bytes()).hexdigest(),'entire_decoded_hash_verified':True,'seconds':time.time()-start})
  Path(str(a.target)+'.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2),flush=True)
 else:
  h=hashlib.sha256();n=0
  with a.target.open('xb') as out:
   for b in decoded_lines(a.source):out.write(b);h.update(b);n+=len(b)
  if a.sha256:assert h.hexdigest()==a.sha256
  print('RESTORED',n,'bytes SHA256',h.hexdigest())
if __name__=='__main__':main()
