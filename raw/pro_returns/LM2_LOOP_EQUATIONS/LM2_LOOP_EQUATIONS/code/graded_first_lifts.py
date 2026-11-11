#!/usr/bin/env python3
"""First higher-weight test for the genuine group two-/three-cycle equations.
Write X=exp x,Y=exp y,Z=(XY)^(-1), log Z=z0+z2+..., with
z0=-x-y,z2=-[x,y]/2. If F starts in weight n>=3, products of F
have weight >=2n. Hence extending f=exp(F) through weight n+1 amounts
exactly to the linear rational system implemented below.
"""
from pathlib import Path
import json
import sympy as sp
from graded_dimensions import *
O=Path(__file__).resolve().parent
J=json.loads((O/'graded_witnesses.json').read_text())
z2={w:sp.Rational(-c,2) for w,c in bracket(x,y).items()}
def variation(p,imgs,corrections):
 r={}
 for w,c in p.items():
  for k,t in enumerate(w):
   if not corrections[t]:continue
   q={():c}
   for j,s in enumerate(w):q=mul(q,corrections[s] if j==k else imgs[s])
   r=add(r,q)
 return r

def from_coords(c):
 p={}
 for w,k in c.items():p=add(p,LB(tuple(0 if t=='x' else 1 for t in w)),k)
 return p
out={}
for n,coords in [(4,J['4']['special_obstruction']['witness']),(7,J['7']['simple_witness']['lyndon_coefficients'])]:
 p=from_coords(coords);R=add(variation(p,(z,x),(z2,{})),variation(p,(y,z),({},z2)))
 W=words(n+1);B=[LB(w) for w in W]
 A=[add(LB(w),LB(w,1)) for w in W]
 C=[add(add(LB(w),LB(w,2)),LB(w,3)) for w in W]
 M=sp.Matrix([[q.get(w,0) for q in A] for w in W]+[[q.get(w,0) for q in C] for w in W])
 rhs=sp.Matrix([0]*len(W)+[-R.get(w,0) for w in W])
 rank=M.rank();ra=M.row_join(rhs).rank()
 print('leading weight',n,'next weight',n+1,'unknowns',len(W),'rank',rank,'augmented rank',ra,'solvable',rank==ra)
 record={'leading_weight':n,'next_weight':n+1,'unknowns':len(W),'rank':rank,'augmented_rank':ra,'solvable':rank==ra}
 if rank==ra:
  vec,params=M.gauss_jordan_solve(rhs)
  vec=vec.subs({s:0 for s in params})
  q={}
  for c,b in zip(vec,B):q=add(q,b,c)
  assert not add(q,substitute(q,y,x))
  assert not add(add(add(q,substitute(q,y,z)),substitute(q,z,x)),R)
  record['next_lyndon_coefficients']={''.join('x' if t==0 else 'y' for t in w):str(v) for w,v in zip(W,vec) if v}
  print('one exact next coefficient:',record['next_lyndon_coefficients'])
 else:
  # Certificate: a left-kernel vector annihilates M but not rhs.
  for ell in M.T.nullspace():
   c=(ell.T*rhs)[0]
   if c:
    record['inconsistency_certificate']={'row_coefficients':[str(a) for a in ell],'rhs_pairing':str(c),'row_indexing':'Lyndon coefficients of antisymmetry, then three-cycle, each in lexicographic order'}
    print('left-kernel certificate rhs pairing:',c);break
  assert 'inconsistency_certificate' in record
 out[str(n)]=record
(O/'graded_first_lifts.json').write_text(json.dumps(out,indent=2))
print('Exact rational jet checks completed. No full pro-lift is asserted.')
