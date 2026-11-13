#!/usr/bin/env python3
"""A certified nonzero pentagon obstruction for a weight-seven loop solution.
The infinitesimal braid algebra t4 acts on its free fiber Lie(a,b,c).
We verify every defining braid relation, evaluate the pentagon under this
representation, and print a nonzero associative coefficient. A nonzero image
is a sufficient witness; no faithfulness assumption is made.
"""
from functools import cache
from pathlib import Path
from itertools import combinations
import json
from b_tripod14 import add,mul,bracket,lyndon,LB,coordinates,special,test_two_three
O=Path(__file__).resolve().parent
G=[{(i,):1} for i in range(3)]
ZERO=({}, {}, {})
def da(A,B,s=1):return tuple(add(a,b,s) for a,b in zip(A,B))
def derive(p,D):
 r={}
 for w,c in p.items():
  for j,g in enumerate(w):
   for v,a in D[g].items():
    t=w[:j]+v+w[j+1:];r[t]=r.get(t,0)+c*a
 return {w:c for w,c in r.items() if c}
def db(A,B):return tuple(add(derive(b,A),derive(a,B),-1) for a,b in zip(A,B))
def inner(p):return tuple(bracket(p,g) for g in G)
T={}
for i,j in combinations(range(4),2):
 if j==3:T[i,j]=inner(G[i])
 else:
  d=[{}, {}, {}];d[i]=bracket(G[i],G[j]);d[j]=bracket(G[j],G[i]);T[i,j]=tuple(d)
def tt(i,j):return T[tuple(sorted((i,j)))]
checks=0
for i,j in combinations(range(4),2):
 for k in range(4):
  if k not in (i,j):
   assert db(tt(i,j),da(tt(i,k),tt(j,k)))==ZERO;checks+=1
 for k,h in combinations([v for v in range(4) if v not in (i,j)],2):
  assert db(tt(i,j),tt(k,h))==ZERO;checks+=1
print('t4 defining braid identities checked:',checks)
pairs=[(tt(0,1),da(tt(1,2),tt(1,3))), (da(tt(0,2),tt(1,2)),tt(2,3)), (tt(1,2),tt(2,3)), (da(tt(0,1),tt(0,2)),da(tt(1,3),tt(2,3))), (tt(0,1),tt(1,2))]
@cache
def evalword(w,k):
 if len(w)==1:return pairs[k][w[0]]
 i=next(i for i in range(1,len(w)) if lyndon(w[i:]))
 return db(evalword(w[:i],k),evalword(w[i:],k))
def pent(coords):
 r=ZERO
 for s,c in coords.items():
  w=tuple(0 if ch=='x' else 1 for ch in s)
  for k,sgn in enumerate((1,1,-1,-1,-1)):
   e=evalword(w,k);r=da(r,e,c*sgn)
 return r
J=json.loads((O/'b_tripod_witnesses.json').read_text())
out=[]
for k,v in enumerate(J['7']['special_basis']+[J['7']['simple_witness']]):
 p={tuple(0 if t=='x' else 1 for t in w):c for w,c in v['associative_coefficients'].items()}
 test_two_three(p);assert not special(p)
 r=pent(v['lyndon_coefficients'])
 entries=[]
 for g,q in enumerate(r):
  for w,c in sorted(q.items()):
   entries.append({'generator':'abc'[g],'word':''.join('abc'[i] for i in w),'coefficient':c})
 assert entries
 out.append({'basis_index':k,'lyndon_coefficients':v['lyndon_coefficients'],'nonzero_terms':len(entries),'first_nonzero':entries[0],'pentagon_image':entries})
 print('basis',k,'nonzero image terms',len(entries),'first nonzero',entries[0])
(O/'b_pentagon_witness.json').write_text(json.dumps(out,indent=2))
print('Each printed vector satisfies the two-cycle, three-cycle and special identities, but fails the pentagon.')
