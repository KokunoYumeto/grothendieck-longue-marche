#!/usr/bin/env python3
"""SL2 characters and a rigorous finite upper bound on the elliptic normalizer.
Full normalizer equality in degree 10 additionally uses the known nonzero
arithmetic class (Hain--Matsumoto 2020, Proposition 29.1 and Remark 29.3).
"""
from b_elliptic_geom import *
from collections import Counter

def weights(D):
 s=set()
 for i,p in enumerate(D):
  for w in p:s.add(len(w)-2*w.count(1)-(1-2*i))
 assert len(s)==1,s
 return next(iter(s))

def decomposition(C):
 return {k:C[k]-C[k+2] for k in range(max(C,default=0)+1) if C[k]-C[k+2]}

def main():
 out={'characters':[]}
 for n in range(1,13):
  A=Counter(n+1-2*w.count(1) for w in lyndon(2,n+1));B0=Counter(n+2-2*w.count(1) for w in lyndon(2,n+2))
  C=Counter({k:A[k-1]+A[k+1]-B0[k]-(1 if n==2 and k==0 else 0) for k in range(-n-2,n+3)})
  G=Counter(weights(D) for D in geom(n))
  row={'degree':n,'ambient_SL2':decomposition(C),'geometric_SL2':decomposition(G),'normalizer_quotient_upper_bound':C[0]-C[2]-G[0]+G[2]}
  print(row,flush=True);out['characters'].append(row)
 n=10;start=time.time();ds=symplectic_basis(n);print('ambient basis',len(ds),'seconds',time.time()-start,flush=True)
 upper=({},a)
 M=column_matrix([dbracket(lower,D) for D in ds],2,n).col_join(column_matrix([dbracket(upper,D) for D in ds],2,n))
 null=M.nullspace();iv=[tuple(lincomb(v,[D[i] for D in ds]) for i in range(2)) for v in null]
 assert len(iv)==3
 print('invariant basis',len(iv),'seconds',time.time()-start,flush=True)
 g14=geom(14);print('geometric degree14',len(g14),'seconds',time.time()-start,flush=True)
 targets=[dbracket(D,epsilon(4)) for D in iv]
 rank=len(independent_derivations(list(g14)+targets,2,14))
 out['degree10_constraint']={'ambient_invariants':len(iv),'geometric_degree14':len(g14),'rank_after_adjoining_brackets':rank,'bracket_constraint_rank':rank-len(g14),'normalizer_quotient_upper_bound':len(iv)-(rank-len(g14))}
 print(out['degree10_constraint'],'seconds',time.time()-start,flush=True)
 Path(__file__).with_name('b_elliptic_normalizer_results.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
