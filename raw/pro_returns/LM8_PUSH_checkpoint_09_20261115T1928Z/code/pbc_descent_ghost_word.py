#!/usr/bin/env python3
"""An explicit word preserving the old parity frame and killing all descended frames."""
from itertools import permutations
from pathlib import Path
import json

def mm(a,b,m): return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%m for i in range(2) for j in range(2))
def inv(a,m):return (a[3],-a[1]%m,-a[2]%m,a[0])
I=(1,0,0,1)
def power(a,k,m):
 r=I
 for _ in range(k):r=mm(r,a,m)
 return r
def comm(a,b,m):return mm(mm(a,b,m),mm(inv(a,m),inv(b,m),m),m)
U=(1,1,0,1);S=(0,1,2,0)
R=inv(mm(U,S,3),3)
x0=power(U,2,3);y0=mm(mm(S,x0,3),inv(S,3),3)
triple=[U,S,R]
pairs=[(x0,y0)]+list(permutations(triple,2))
def ev(w,pair,m=3):
 a,b=pair;v=I
 for c in w:v=mm(v,{'x':a,'y':b,'X':inv(a,m),'Y':inv(b,m)}[c],m)
 return v
words=['']
for _ in range(4):
 words += [w+c for w in list(words) if len(w)==_ for c in 'xyXY' if not w or c!=w[-1].swapcase()]
vals={w:[ev(w,p) for p in pairs] for w in words}
basis={};certificate=None
for u in words:
 for v in words:
  mats=[power(comm(power(a,4,3),power(b,4,3),3),2,3) for a,b in zip(vals[u],vals[v])]
  assert all(a in (I,(2,0,0,2)) for a in mats)
  bits=sum((a!=I)<<i for i,a in enumerate(mats)); row=[(u,v)]; r=bits
  while r:
   j=r.bit_length()-1
   if j in basis:r^=basis[j][0];row+=basis[j][1]
   else:basis[j]=(r,row);break
  target=1;ts=[]
  while target:
   j=target.bit_length()-1
   if j not in basis:break
   target^=basis[j][0];ts+=basis[j][1]
  if target==0:
   certificate=ts;break
 if certificate is not None:break
assert certificate is not None
# Cancel duplicate blocks; all evaluated blocks are central.
certificate=sorted(p for p in set(certificate) if certificate.count(p)%2)
def factor_word(u,v):return f'[({u})^4,({v})^4]^2'
mats=[I]*len(pairs)
for u,v in certificate:
 for i,(a,b) in enumerate(zip(vals[u],vals[v])):
  mats[i]=mm(mats[i],power(comm(power(a,4,3),power(b,4,3),3),2,3),3)
assert mats==[(2,0,0,2)]+[I]*6
# Independently verify the universal mod4 identity on all 48^2 matrix pairs.
g4=[(a,b,c,d) for a in range(4) for b in range(4) for c in range(4) for d in range(4) if (a*d-b*c)%4==1]
assert len(g4)==48
assert all(power(comm(power(a,4,4),power(b,4,4),4),2,4)==I for a in g4 for b in g4)
block_values=[[power(comm(power(vals[u][i],4,3),power(vals[v][i],4,3),3),2,3) for i in range(len(pairs))] for u,v in certificate]
out=dict(block_values_mod3=block_values,old_pair_mod3=[x0,y0],phi_triple_mod3=triple,pairs_mod3=pairs,blocks=certificate,word=' * '.join(factor_word(u,v) for u,v in certificate),values_mod3=mats,universal_mod4_pairs=len(g4)**2,conclusion='The word belongs to F prime, has q_orig value [5I], and is killed by all six signed q_phi sigma maps modulo12.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
