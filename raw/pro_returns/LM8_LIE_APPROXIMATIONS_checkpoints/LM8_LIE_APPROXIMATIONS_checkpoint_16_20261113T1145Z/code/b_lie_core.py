#!/usr/bin/env python3
"""LM8 rerun of supplied LM3b exact calculations, audited and extended.
All arithmetic is rational/integer. Lyndon bases are built from scratch.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product
from collections import defaultdict
from fractions import Fraction
import json, math, sys, time
import sympy as sp

def add(a,b,k=1):
 c=dict(a)
 for w,v in b.items():
  c[w]=c.get(w,0)+k*v
  if not c[w]: del c[w]
 return c

def mul(a,b):
 c=defaultdict(int)
 for u,x in a.items():
  for v,y in b.items():c[u+v]+=x*y
 return {u:v for u,v in c.items() if v}

def bracket(a,b):return add(mul(a,b),mul(b,a),-1)

def gen(i):return {(i,):1}

def is_lyndon(w):return all(w<w[i:] for i in range(1,len(w)))

@lru_cache(None)
def lyndon(r,n):return tuple(w for w in product(range(r),repeat=n) if is_lyndon(w))

@lru_cache(None)
def expand(w):
 if len(w)==1:return {w:1}
 for i in range(1,len(w)):
  if is_lyndon(w[i:]):return bracket(expand(w[:i]),expand(w[i:]))
 raise ValueError(w)

def coords(p,r,n):
 p=dict(p); ans={}
 for i,w in enumerate(lyndon(r,n)):
  v=p.get(w,0)
  if v:
   ans[i]=v;p=add(p,expand(w),-v)
 if p:raise ValueError(('not Lie',r,n,next(iter(p.items()))))
 return ans

def lincomb(v,basis):
 out={}
 for a,p in zip(v,basis):
  if a:out=add(out,p,a)
 return out

def derivative(D,p):
 out=defaultdict(int)
 for w,c in p.items():
  for j,i in enumerate(w):
   for v,a in D[i].items():out[w[:j]+v+w[j+1:]]+=c*a
 return {w:c for w,c in out.items() if c}

def dbracket(D,E):return tuple(add(derivative(D,e),derivative(E,d),-1) for d,e in zip(D,E))

@lru_cache(None)
def special(r,n):
 # Gauge a_0=0, i.e. D(sum x_i)=0. At n=1 quotient inner ad(sum x_i).
 bas=tuple(expand(w) for w in lyndon(r,n)); cols=[]
 for i in range(r):
  for a in bas:cols.append(coords(bracket(a,gen(i)),r,n+1))
 M=sp.zeros(len(lyndon(r,n+1)),r*len(bas))
 for j,c in enumerate(cols):
  for i,v in c.items():M[i,j]=v
 null=M.nullspace(); ds=[]
 for v in null:
  D=tuple(bracket(lincomb(v[i*len(bas):(i+1)*len(bas)],bas),gen(i)) for i in range(r))
  if any(D):ds.append(D)
 if n==1:
  # Quotient via linear algebra, including the one residual inner derivation first.
  S={ (i,):1 for i in range(r)}
  inn=tuple(bracket(S,gen(i)) for i in range(r))
  ds=independent_derivations([inn]+ds,r,n)[1:]
 return tuple(ds)

def dcoords(D,r,n):
 ans={}; m=len(lyndon(r,n+1))
 for i,p in enumerate(D):
  for j,c in coords(p,r,n+1).items():ans[i*m+j]=c
 return ans

def column_matrix(ds,r,n):
 M=sp.zeros(r*len(lyndon(r,n+1)),len(ds))
 for j,D in enumerate(ds):
  for i,c in dcoords(D,r,n).items():M[i,j]=c
 return M

def independent_derivations(ds,r,n):
 if not ds:return []
 piv=column_matrix(ds,r,n).rref()[1]
 return [ds[i] for i in piv]

@lru_cache(None)
def pointpush(n):
 # Standard sphere-(0,4) infinitesimal point pushes; their sum-zero gauges already hold.
 x,y,z=map(gen,range(3))
 u=(bracket(y,x),bracket(x,y),{})
 v=(bracket(z,x),{},bracket(x,z))
 @lru_cache(None)
 def ev(w):
  if len(w)==1:return (u,v)[w[0]]
  for j in range(1,len(w)):
   if is_lyndon(w[j:]):return dbracket(ev(w[:j]),ev(w[j:]))
 return tuple(ev(w) for w in lyndon(2,n))

def mobius(n):
 return int(sp.mobius(n))

def lie_character(n,chi_power):
 return sum(mobius(d)*chi_power(d)**(n//d) for d in sp.divisors(n))//n

def s3_table(N=12):
 rows=[]
 for n in range(1,N+1):
  if n==1:rows.append(dict(weight=1,dimension=0,trivial=0,sign=0,standard=0));continue
  ce=2*lie_character(n,lambda d:2)-lie_character(n+1,lambda d:2)
  ct=-lie_character(n+1,lambda d:2 if d%2==0 else 0)
  cc=-lie_character(n,lambda d:2 if d%3==0 else -1)-lie_character(n+1,lambda d:2 if d%3==0 else -1)
  assert (ce+3*ct+2*cc)%6==0 and (ce-3*ct+2*cc)%6==0 and (ce-cc)%3==0
  rows.append(dict(weight=n,dimension=ce,transposition_trace=ct,cycle_trace=cc,trivial=(ce+3*ct+2*cc)//6,sign=(ce-3*ct+2*cc)//6,standard=(ce-cc)//3))
 return rows

def fill(D):
 return tuple({tuple(i-1 for i in w):c for w,c in p.items() if 0 not in w} for p in D[1:])

def normalizer(n):
 # Degree-n normalized SD which bracket the two point-push generators into PP_(n+1).
 ds=special(3,n); pp=pointpush(n+1); pg=pointpush(1)
 C=column_matrix(pp,3,n+1)
 # The n+1 degree is >=2, so there is no remaining inner ambiguity.
 A=column_matrix([dbracket(D,pg[0]) for D in ds],3,n+1)
 B=column_matrix([dbracket(D,pg[1]) for D in ds],3,n+1)
 # rank([C A])-rank C isn't enough simultaneously; eliminate by pivot row minors.
 piv=C.T.rref()[1]; Cp=C[list(piv),:]; inv=Cp.inv()
 A=A-C*inv*A[list(piv),:]; B=B-C*inv*B[list(piv),:]
 rows=[]
 for M in (A,B):
  for i in range(M.rows):
   row=[M[i,j] for j in range(M.cols)]
   if any(row):rows.append(row)
 R=sp.Matrix(rows) if rows else sp.zeros(0,len(ds))
 return len(ds)-R.rank(),len(ds),len(pp)

def main():
 result={'S3':s3_table()};print(json.dumps({'S3':result['S3']},indent=2),flush=True)
 result['sphere4']=[]
 for n in range(1,7):
  t=time.time();ds=special(3,n); pp=pointpush(n)
  rankpp=column_matrix(pp,3,n).rank()
  # At n=1 filling is outer-zero; at higher degrees use sum-zero gauge and no residual inner.
  fi=0 if n==1 else column_matrix([fill(D) for D in ds],2,n).rank()
  row=dict(weight=n,special_outer=len(ds),pointpush=rankpp,fill_image=fi,fill_kernel=len(ds)-fi,theta_kernel=len(ds)-fi-rankpp)
  print(row,'elapsed',time.time()-t,flush=True);result['sphere4'].append(row)
 result['normalizers']=[]
 maxn=int(sys.argv[1]) if len(sys.argv)>1 else 4
 for n in range(1,maxn+1):
  t=time.time();z,a,p=normalizer(n)
  row=dict(weight=n,normalizer=z,geometric=len(pointpush(n)),quotient=z-len(pointpush(n)))
  print(row,'elapsed',time.time()-t,flush=True);result['normalizers'].append(row)
 with open(Path(__file__).with_name('b_sphere_tables.json'),'w') as f:json.dump(result,f,indent=2)
if __name__=='__main__':main()
