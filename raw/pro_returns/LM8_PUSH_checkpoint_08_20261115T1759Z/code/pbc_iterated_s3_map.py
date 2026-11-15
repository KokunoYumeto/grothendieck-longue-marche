#!/usr/bin/env python3
"""Recover the exact marked S3 quotient from the cached consistent pc source.

First solve the sign character over F2.  Then the rotation coordinates are
linear 1-cocycles with values in F3(sign).  All pc relations and the marked
images of s,r are checked again by direct S3 multiplication.
"""
from pathlib import Path
import json
P=Path(__file__).parent
D=json.loads((P/'pbc_iterated_joint_pc.json').read_text())
n=len(D['relative_orders'])
def parity(w):
 a=0
 for i,e in zip(w[::2],w[1::2]):
  if e%2:a^=1<<(i-1)
 return a
rows=[]
for i,(p,w) in enumerate(zip(D['relative_orders'],D['powers'])):rows.append(((p%2)<<i)^parity(w))
for i,j,w in D['conjugates']:rows.append((1<<(i-1))^parity(w))
rows += [parity(D['s'])^(1<<n),parity(D['r'])]
basis={}
for a in rows:
 while a&((1<<n)-1):
  k=(a&-a).bit_length()-1
  if k not in basis:basis[k]=a;break
  a^=basis[k]
 else:assert a==0
assert len(basis)==n
sol=0
for k in range(n-1,-1,-1):
 v=((basis[k]>>n)&1)^((basis[k]&sol).bit_count()%2)
 if v:sol|=1<<k
B=[(sol>>i)&1 for i in range(n)]
def linword(w):
 c=[0]*n;sgn=1
 for i,e in zip(w[::2],w[1::2]):
  i-=1
  q=e if B[i]==0 else e%2
  c[i]=(c[i]+sgn*q)%3
  if B[i]*e%2:sgn=-sgn
 return c
r3=[]
for i,(p,w) in enumerate(zip(D['relative_orders'],D['powers'])):
 c=[-x%3 for x in linword(w)];c[i]=(c[i]+(p if B[i]==0 else p%2))%3;r3.append((c,0))
for i,j,w in D['conjugates']:
 i-=1;j-=1;c=[-x%3 for x in linword(w)];sgn=1-2*B[j]
 c[i]=(c[i]+sgn)%3;c[j]=(c[j]+sgn*((1-2*B[i])-1))%3;r3.append((c,0))
r3 += [(linword(D['s']),0),(linword(D['r']),1)]
mask=(1<<(n+1))-1
unknown=(1<<n)-1
def add(a,b):
 a1,a2=a;b1,b2=b;a0=mask^(a1|a2);b0=mask^(b1|b2)
 return ((a0&b1)|(a1&b0)|(a2&b2),(a0&b2)|(a2&b0)|(a1&b1))
b3={}
for c,target in r3:
 c=c+[target];a=(sum(1<<i for i,v in enumerate(c) if v==1),sum(1<<i for i,v in enumerate(c) if v==2))
 while (a[0]|a[1])&unknown:
  k=(((a[0]|a[1])&unknown)&-((a[0]|a[1])&unknown)).bit_length()-1
  if k not in b3:
   if (a[1]>>k)&1:a=a[::-1]
   b3[k]=a;break
  row=b3[k]
  a=add(a,row[::-1] if (a[0]>>k)&1 else row)
 else:assert a==(0,0)
assert len(b3)==n
A=[0]*n
for k in range(n-1,-1,-1):
 u,v=b3[k];rhs=((u>>n)&1)+2*((v>>n)&1)
 A[k]=(rhs-sum(A[j]*(((u>>j)&1)+2*((v>>j)&1)) for j in range(k+1,n)))%3
for c,target in r3:assert sum(x*y for x,y in zip(c,A))%3==target
I=(0,0)
def mul(g,h):return ((g[0]+(-1 if g[1] else 1)*h[0])%3,g[1]^h[1])
def inv(g):return ((g[0] if g[1] else -g[0])%3,g[1])
def powg(g,k):
 if k<0:return powg(inv(g),-k)
 out=I
 while k:
  if k&1:out=mul(out,g)
  g=mul(g,g);k>>=1
 return out
images=list(zip(A,B))
def ev(w):
 out=I
 for i,e in zip(w[::2],w[1::2]):out=mul(out,powg(images[i-1],e))
 return out
for i,(p,w) in enumerate(zip(D['relative_orders'],D['powers'])):assert powg(images[i],p)==ev(w)
for i,j,w in D['conjugates']:assert mul(mul(inv(images[j-1]),images[i-1]),images[j-1])==ev(w)
assert ev(D['s'])==(0,1) and ev(D['r'])==(1,0)
R={'source_order':D['order'],'rotation':A,'sign':B,'s_image':[0,1],'r_image':[1,0],
   'all_pc_relations_verified':True,'sign_linear_rank':len(basis),'twisted_linear_rank':len(b3)}
(P/'pbc_iterated_s3_map.json').write_text(json.dumps(R,indent=2)+'\n')
print(json.dumps({'sign_nonzero':[i+1 for i,x in enumerate(B) if x], 'rotation_nonzero':[[i+1,x] for i,x in enumerate(A) if x], 'all_pc_relations_verified':True,'linear_ranks':[len(basis),len(b3)]},indent=2))
