#!/usr/bin/env python3
"""Exact rational cycle/cabling equations, supplying candidates for direct t4 tests."""
import sys,json,time
from pathlib import Path
from functools import lru_cache
import sympy as S
from ab_lie import lyndon,expand,is_lyndon,add,mul,bracket,coords,gen

@lru_cache(None)
def subst_tree(w,which):
 x,y=gen(0),gen(1)
 X,Y=[(y,x),(y,{ (0,):-1,(1,):-1}),({(0,):-1,(1,):-1},x),({(0,):-1,(1,):-1},y)][which]
 if len(w)==1:return (X,Y)[w[0]]
 for i in range(1,len(w)):
  if is_lyndon(w[i:]):return bracket(subst_tree(w[:i],which),subst_tree(w[i:],which))

def main(N=12):
 out={}
 for n in range(1,N+1):
  t=time.time();ws=lyndon(2,n);r=len(ws); rr=len(lyndon(2,n+1)); cols=[]
  for w in ws:
   p=expand(w)
   anti=coords(add(p,subst_tree(w,0)),2,n)
   cyc=coords(add(add(p,subst_tree(w,1)),subst_tree(w,2)),2,n)
   cab=coords(add(bracket(gen(0),p),bracket(add(gen(0),gen(1)),subst_tree(w,3)),-1),2,n+1)
   col={**anti,**{k+r:v for k,v in cyc.items()},**{k+2*r:v for k,v in cab.items()}}
   cols.append(col)
  M=S.zeros(2*r+rr,r)
  for j,c in enumerate(cols):
   for i,v in c.items():M[i,j]=v
  # All three equation sets are integral; rational nullspace is exact.
  ker=M.nullspace()
  ints=[]
  for v in ker:
   den=S.ilcm(*[int(x.q) for x in v]) if len(v)>1 else int(v[0].q)
   a=[int(x*den) for x in v]; g=S.igcd(*a) if len(a)>1 else abs(a[0]);a=[x//int(g) for x in a];ints.append(a)
  out[str(n)]={'words':[''.join(map(str,w)) for w in ws],'kernel':ints,'dimension':len(ints)}
  Path(__file__).with_name('fg_candidates.json').write_text(json.dumps(out))
  print(n,r,len(ints),'seconds',round(time.time()-t,3),flush=True)
if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 12)
