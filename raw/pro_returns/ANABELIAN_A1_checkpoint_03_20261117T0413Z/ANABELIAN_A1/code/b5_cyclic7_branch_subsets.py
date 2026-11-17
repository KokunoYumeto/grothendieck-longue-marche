#!/usr/bin/env python3
"""Search all seven nonzero F8 branch points for supersingular elliptic factors.
Every model y^7=prod_i(x-alpha^i)^e_i, all e_i in1..6, e0=1,
sum e_i=0 mod7. Compute complete degree5 character L-polynomial
from exact character sums over F8^m, m1..5. Not a proof before review.
"""
import json,time,itertools
from pathlib import Path
import numpy as np
mods={3:11,6:67,9:529,12:4179,15:32771}
def table(n,mod):
 q=1<<n;ex=[];lg=[-1]*q;x=1
 for i in range(q-1):
  assert lg[x]==-1
  lg[x]=i;ex.append(x);x<<=1
  if x&q:x^=mod
 assert x==1
 return ex,lg
# Z[zeta7] basis1,zeta,...,zeta5.
def red(a):
 a=list(a)+[0]*max(0,7-len(a))
 for i in range(len(a)-1,6,-1):a[i%7]+=a[i]
 c=a[6]
 return tuple(a[i]-c for i in range(6))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(a,n):return tuple(n*x for x in a)
def mul(a,b):
 c=[0]*11
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return red(c)
zero=(0,)*6;one=(1,0,0,0,0,0)
start=time.monotonic();mats=[];bmats=[];emb=[]
for m in range(1,6):
 n=3*m;q=1<<n;ex,lg=table(n,mods[n]);per=q-1
 kk=next(i for i in range(1,7) if ex[(3*i*(per//7))%per]^ex[i*(per//7)]^1==0)
 alpha=ex[kk*(per//7)];branches=[ex[(kk*i*(per//7))%per] for i in range(7)]
 xs=np.array([x for x in range(q) if x not in branches],dtype=np.int32)
 logs=np.array(lg,dtype=np.int32)
 mat=np.column_stack([((logs[xs^b]%7)*pow(kk,-1,7))%7 for b in branches]).astype(np.int16)
 mats.append(mat)
 branchlogs=np.array([[0 if u==v else ((lg[u^v]%7)*pow(kk,-1,7))%7 for v in branches] for u in branches],dtype=np.int16)
 bmats.append(branchlogs)
 emb.append(dict(m=m,modulus=mods[n],alpha=alpha))
print('tables',time.monotonic()-start,flush=True)
found=[];checked=0
for tail in itertools.product(range(7),repeat=6):
 es=(1,)+tail
 if sum(es)%7:continue
 rank=sum(e!=0 for e in es)-2
 if rank<2:continue
 checked+=1;ev=np.array(es,dtype=np.int16);sums=[];a=[one];counts=[]
 for k,mat in enumerate(mats[:rank],start=1):
  residues=(mat@ev)%7
  cc=np.bincount(residues,minlength=7).tolist();cc[0]+=1
  bres=(bmats[k-1]@ev)%7
  for pos in range(7):
   if es[pos]==0:cc[int(bres[pos])]+=1
  sums.append(red(cc));counts.append(cc)
  val=zero
  for i in range(1,k+1):val=add(val,mul(sums[i-1],a[k-i]))
  assert all(x%k==0 for x in val),(es,k,val)
  a.append(tuple(x//k for x in val))
 templates=[(1,0,-8),(1,0,8),(1,4,8),(1,-4,8),
            (1,0,8,0,64),(1,0,-8,0,64),
            (1,4,8,32,64),(1,-4,8,-32,64)]
 for tp in templates:
  deg=len(tp)-1
  if deg>rank:continue
  for j in range(7):
   pp=[red([0]*((j*k)%7)+[c]) for k,c in enumerate(tp)]
   b=[]
   for k in range(rank+1-deg):
    v=a[k]
    for i in range(1,min(k,deg)+1):v=add(v,scale(mul(pp[i],b[k-i]),-1))
    b.append(v)
   ok=True
   for k in range(rank+1-deg,rank+1):
    v=zero
    for i in range(max(0,k-len(b)+1),min(k,deg)+1):v=add(v,mul(pp[i],b[k-i]))
    if v!=a[k]:ok=False;break
   if ok:
    rec=dict(exponents=es,supersingular_template=tp,phase=j,character_coefficients=a,quotient_coefficients=b,counts=counts)
    found.append(rec);print('FOUND',json.dumps(rec),flush=True)
 if checked%500==0:print('checked',checked,'found',len(found),'seconds',time.monotonic()-start,flush=True)
 if found:break
out=dict(models='y^7=prod_i(x-alpha^i)^e_i, alpha^3+alpha+1=0; exponents may be zero',embeddings=emb,checked=checked,found=found,seconds=time.monotonic()-start)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('DONE',json.dumps(out),flush=True)
