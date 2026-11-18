"""Exact degree-seven four-branch Kummer search over F64.
Every nontrivial character has degree two, so sums over F64 and F4096
are sufficient. Test the complete supersingular factors over Q(zeta7).
"""
from pathlib import Path
import itertools,json,time,gzip,math
import numpy as np
r=Path(__file__).resolve().parent;start=time.time()
def table(n,mod):
 q=1<<n;lg=[-1]*q;ex=[];v=1
 for j in range(q-1):
  assert lg[v]<0;lg[v]=j;ex.append(v);v<<=1
  if v&q:v^=mod
 assert v==1
 return ex,lg
def red(v):
 a=[0]*7
 for j,c in enumerate(v):a[j%7]+=c
 return tuple(a[j]-a[6] for j in range(6))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def mul(a,b):
 v=[0]*11
 for i,x in enumerate(a):
  for j,y in enumerate(b):v[i+j]+=x*y
 return red(v)
zero=(0,)*6;one=(1,0,0,0,0,0);fields=[]
for n,mod in [(6,67),(12,4179)]:
 ex,lg=table(n,mod);q=1<<n
 if n==6:k=1;gamma=2
 else:
  k=next(k for k in range(1,63) if math.gcd(k,63)==1 and ex[(6*k*65)%(q-1)]^ex[k*65]^1==0)
  gamma=ex[k*65]
 gp=[1]+[ex[(j*lg[gamma])%(q-1)] for j in range(1,6)]
 embedded=[]
 for a in range(64):
  v=0
  for j in range(6):
   if a>>j&1:v^=gp[j]
  embedded.append(v)
 fields.append((q,np.array(lg,dtype=np.int32),embedded,pow(k,-1,7)))
exponents=[(1,a,b,(-1-a-b)%7) for a in range(1,7) for b in range(1,7) if (-1-a-b)%7]
assert len(exponents)==31
# Reciprocal minimal polynomials for 8 times roots of unity with
# relative cyclotomic degree <=2 over Q(zeta7), and all zeta7 phases.
templates=[(1,-8),(1,8),(1,8,64),(1,0,64),(1,-8,64)]
records=[];found=[]
for lam in range(2,64):
 mats=[]
 for q,lg,emb,chi in fields:
  bs=[0,1,emb[lam]];xs=np.array([x for x in range(q) if x not in bs],dtype=np.int32)
  mats.append(np.column_stack([lg[xs^b]*chi%7 for b in bs]).astype(np.int16))
 for es in exponents:
  counts=[np.bincount(M@np.array(es[:3],dtype=np.int16)%7,minlength=7).tolist() for M in mats]
  s1,s2=map(red,counts);a=[one,s1,tuple(v//2 for v in add(mul(s1,s1),s2))]
  assert all(v%2==0 for v in add(mul(s1,s1),s2))
  hits=[]
  for tp in templates:
   deg=len(tp)-1
   for phase in range(7):
    pp=[red([0]*((phase*j)%7)+[v]) for j,v in enumerate(tp)];quo=[]
    for j in range(3-deg):
     v=a[j]
     for i in range(1,min(j,deg)+1):v=add(v,neg(mul(pp[i],quo[j-i])))
     quo.append(v)
    ok=True
    for j in range(3-deg,3):
     v=zero
     for i in range(max(0,j-len(quo)+1),min(j,deg)+1):v=add(v,mul(pp[i],quo[j-i]))
     if v!=a[j]:ok=False;break
    if ok:hits.append({'template':tp,'phase':phase,'quotient':quo})
  rec={'lambda':lam,'exponents':es,'character_coefficients':a,'power_sum_residue_counts':counts,'hits':hits};records.append(rec)
  if hits:found.append(rec);print('FOUND',json.dumps(rec),flush=True)
with gzip.open(r/'b5_f64_fourbranch_polynomials.json.gz','wt') as f:json.dump(records,f,separators=(',',':'))
out={'checked':len(records),'found':found,'templates':templates,'base_modulus':67,'quadratic_modulus':4179,'embedding_gamma':fields[1][2][2],'norm_character_scale':fields[1][3],'seconds':time.time()-start}
(r/'b5_f64_fourbranch.json').write_text(json.dumps(out,indent=2)+'\n')
print('DONE checked',len(records),'found',len(found),'seconds',time.time()-start)
