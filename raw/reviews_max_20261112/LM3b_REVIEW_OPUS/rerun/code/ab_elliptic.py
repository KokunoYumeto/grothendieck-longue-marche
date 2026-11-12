#!/usr/bin/env python3
"""Independent exact elliptic calculations, using ab_lie's own Lyndon engine.
Derivation degree n means images of a,b have bracket length n+1.
The epsilon normalization is Hain--Matsumoto (2020), equation (22.3).
"""
from ab_lie import *
from functools import lru_cache
from math import gcd
from functools import reduce
from pathlib import Path

a,b=gen(0),gen(1)
omega=bracket(a,b)

@lru_cache(None)
def B(j):
 return b if j==0 else bracket(a,B(j-1))

@lru_cache(None)
def epsilon(k):
 assert k>=2 and k%2==0
 da=bracket(B(k-1),a)
 db=bracket(B(k-1),b)
 for j in range(1,k-1):
  h=k-1-j
  if j>h>0:db=add(db,bracket(B(j),B(h)),-(-1)**j)
 D=(da,db)
 assert not derivative(D,omega)
 return D

lower=(b,{})
@lru_cache(None)
def eps_orbit(k):
 out=[epsilon(k)]
 for j in range(k-2):out.append(dbracket(lower,out[-1]))
 assert not any(dbracket(lower,out[-1]))
 assert column_matrix(out,2,k).rank()==k-1
 return tuple(out)

@lru_cache(None)
def geom(n):
 if n<4 or n%2:return ()
 candidates=list(eps_orbit(n))
 for k in range(4,n,2):
  if k>n-k:break
  A,C=geom(k),geom(n-k)
  candidates.extend(dbracket(x,y) for i,x in enumerate(A) for j,y in enumerate(C) if k!=n-k or i<j)
 out=independent_derivations(candidates,2,n)
 for D in out:assert not derivative(D,omega)
 return tuple(out)

def symplectic_basis(n):
 bas=tuple(expand(w) for w in lyndon(2,n+1))
 columns=[coords(bracket(u,b),2,n+2) for u in bas]+[coords(bracket(a,v),2,n+2) for v in bas]
 M=sp.zeros(len(lyndon(2,n+2)),2*len(bas))
 for j,c in enumerate(columns):
  for i,v in c.items():M[i,j]=v
 out=[]
 for v in M.nullspace():
  den=sp.ilcm(*[sp.denom(q) for q in v]);v=[int(q*den) for q in v]
  g=reduce(gcd,v);v=[q//g for q in v]
  D=(lincomb(v[:len(bas)],bas),lincomb(v[len(bas):],bas))
  assert not derivative(D,omega)
  out.append(D)
 return out

def lyndon_terms(p,n):
 return [{'coefficient':int(c),'word':''.join('ab'[j] for j in lyndon(2,n)[i])} for i,c in coords(p,2,n).items()]

def tree(w):
 if len(w)==1:return 'ab'[w[0]]
 for i in range(1,len(w)):
  if is_lyndon(w[i:]):return [tree(w[:i]),tree(w[i:])]

def descriptor(D,n):
 ans=[]
 for p in D:
  ans.append([{'coefficient':int(c),'word':''.join('ab'[j] for j in lyndon(2,n+1)[i]),'bracket_tree':tree(lyndon(2,n+1)[i])} for i,c in coords(p,2,n+1).items()])
 return ans

def main():
 out={'normalization':'Hain--Matsumoto equation (22.3); degree of epsilon_k is k','geometric':[]}
 for n in range(1,13):
  start=time.time();d=len(geom(n));r={'degree':n,'ambient_outer':2*len(lyndon(2,n+1))-len(lyndon(2,n+2))-(n==2),'geometric':d}
  out['geometric'].append(r);print(r,'seconds',round(time.time()-start,4),flush=True)
 ds=symplectic_basis(7)
 assert len(ds)==4
 # Select a primitive basis element with fewest Lyndon terms.
 D=min(ds,key=lambda d:sum(len(coords(p,2,8)) for p in d))
 inner=[tuple(bracket(expand(w),x) for x in (a,b)) for w in lyndon(2,7)]
 assert column_matrix(inner+[D],2,7).rank()==len(inner)+1
 # -I conjugates every odd-degree derivation to its negative.
 assert all(all(len(w)==8 for w in p) for p in D)
 out['degree7_witness']={'images':descriptor(D,7),'boundary_defect':[],'inner_rank':len(inner),'rank_after_adjoining':len(inner)+1}
 print('DEGREE7_WITNESS',json.dumps(out['degree7_witness'],indent=2),flush=True)
 Path(__file__).with_name('ab_elliptic_results.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
