#!/usr/bin/env python3
"""Exact images of two distinct actual pure sources in the retained cap216."""
import numpy as np,json
from pathlib import Path
p=Path(__file__);C=np.load(p.parent.parent/'ghost_code/check_main_mixed_capping.npz');E=C['capped_edges'];n=len(E)
words=[None]*n;words[0]=();queue=[0]
for a in queue:
 for j in range(2):
  b=int(E[a,j])
  if words[b] is None:words[b]=words[a]+(j,);queue.append(b)
assert len(queue)==n
M=np.empty((n,n),dtype=np.int16)
for a in range(n):
 for b,w in enumerate(words):
  c=a
  for j in w:c=int(E[c,j])
  M[a,b]=c
Inv=[int(np.flatnonzero(M[a]==0)[0]) for a in range(n)]
def power(a,k):
 o=0
 for _ in range(k):o=int(M[o,a])
 return o
def comm(a,b):return int(M[M[M[a,b],Inv[a]],Inv[b]])
def subgroup(gs):
 out=[0];seen={0}
 for a in out:
  for b in gs:
   c=int(M[a,b])
   if c not in seen:seen.add(c);out.append(c)
 return sorted(out)
def order(a):
 k=1;b=a
 while b:b=int(M[b,a]);k+=1
 return k
D,V=map(int,E[0]);N=subgroup([comm(a,b) for a in range(n) for b in (D,V)])
assert len(N)==27
Pstd=subgroup([V,power(D,2)])
Psq=subgroup(N+[power(D,2),power(V,2)])
assert len(Pstd)==108 and len(Psq)==54
assert set(N)<=set(Psq)<=set(Pstd)
# Their binary quotient orders, retaining actual quotient cosets.
def cosets(S,K):
 seen={};blocks=[]
 for a in S:
  if a in seen:continue
  block=sorted(int(M[a,k]) for k in K);z=len(blocks)
  for b in block:seen[b]=z
  blocks.append(block)
 return seen,blocks
stdcos,stdblocks=cosets(Pstd,N);sqcos,sqblocks=cosets(Psq,N)
assert len(stdblocks)==4 and len(sqblocks)==2
assert len({stdcos[power(V,j)] for j in range(4)})==4
assert stdcos[power(D,2)]==stdcos[power(V,2)]
Z=[a for a in N if all(M[a,b]==M[b,a] for b in N)];assert len(Z)==3
_,NZ=cosets(N,Z);ntoc={a:j for j,row in enumerate(NZ) for a in row}
two=power(D,6);assert order(two)==2
assert all(ntoc[M[M[two,a],two]]==ntoc[Inv[a]] for a in N)
assert any(M[two,a]!=M[a,two] for a in N)
print('PASS cap216 derivedHeisenberg27; full standard pure F(v,d²) image108 with cyclicC4 quotient')
print('PASS actual centralizer-pure F2′F2² image54 with cyclicC2 quotient')
print('PASS Dcap^6 has order2 and acts as−I on Heisenberg27/center; both images are nonnilpotent')
p.with_suffix('.json').write_text(json.dumps({'scope':'Two literal source subgroups in the actual cap216; no claim that pure mod4 is necessary for every centralizer-only factorization',
 'D':D,'V':V,'derived':N,'standard_pure_image':Pstd,'centralizer_pure_image':Psq,
 'standard_pure_binary_cosets':stdblocks,'centralizer_pure_binary_cosets':sqblocks,
 'involution':two,'heisenberg_center':Z,'heisenberg_central_cosets':NZ},indent=2)+'\n')
