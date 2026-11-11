#!/usr/bin/env python3
"""Extend the explicit weight-seven witness in genuine (I),(II) through weight 12.
All products of log(f) terms begin in weight14, so this range is linear in
F=log(f), but substitutes the complete BCH logarithm log Z to required degree.
At each weight a rational solution with free coefficients set to zero is used.
This computes one compatible finite jet, not an infinite or integral lift.
"""
from pathlib import Path
from functools import cache
from math import factorial
import json,time
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from graded_dimensions import add,LB,words,lyndon,x,y,normalize
O=Path(__file__).resolve().parent;NMAX=12

def tmul(a,b,N):
 r={}
 for u,c in a.items():
  for v,d in b.items():
   if len(u)+len(v)<=N:
    w=u+v;r[w]=r.get(w,0)+c*d
 return {w:c for w,c in r.items() if c}
def tbr(a,b,N):return add(tmul(a,b,N),tmul(b,a,N),-1)
# log(exp x exp y), to degree6 suffices for any word of initial degree7.
M=NMAX-6
ex={(0,)*n:sp.Rational(1,factorial(n)) for n in range(M+1)}
ey={(1,)*n:sp.Rational(1,factorial(n)) for n in range(M+1)}
u=tmul(ex,ey,M);u.pop(())
bch={};v={():1}
for k in range(1,M+1):
 v=tmul(v,u,M);bch=add(bch,v,sp.Rational((-1)**(k+1),k))
z={w:-c for w,c in bch.items()}
@cache
def ev(w,mode,M):
 if len(w)==1:
  q=((x,y),(z,x),(y,z))[mode][w[0]]
  return {v:c for v,c in q.items() if len(v)<=M}
 k=next(k for k in range(1,len(w)) if lyndon(w[k:]));a,b=w[:k],w[k:]
 return tbr(ev(a,mode,M-len(b)),ev(b,mode,M-len(a)),M)
J=json.loads((O/'graded_witnesses.json').read_text());initial=J['7']['simple_witness']['lyndon_coefficients']
F={7:{tuple(0 if c=='x' else 1 for c in w):sp.Rational(a) for w,a in initial.items()}}
rows=[];success=True
for N in range(8,NMAX+1):
 start=time.time();R={}
 for n,coords in F.items():
  for w,c in coords.items():
   for mode in range(3):R=add(R,{v:a for v,a in ev(w,mode,N).items() if len(v)==N},c)
 W=words(N);A=[add(LB(w),LB(w,1)) for w in W];C=[add(add(LB(w),LB(w,2)),LB(w,3)) for w in W]
 mat=[[q.get(w,0) for q in A] for w in W]+[[q.get(w,0) for q in C] for w in W]
 rhs=[0]*len(W)+[-R.get(w,0) for w in W]
 dm=DomainMatrix.from_Matrix(sp.Matrix([r+[s] for r,s in zip(mat,rhs)])).convert_to(sp.QQ)
 rr,piv=dm.rref();rr=rr.to_Matrix();bad=len(W) in piv
 rank=len(piv)-int(bad)
 print('weight',N,'unknowns',len(W),'rank',rank,'augmented',len(piv),'solvable',not bad,'seconds',round(time.time()-start,3),flush=True)
 row={'weight':N,'unknowns':len(W),'rank':rank,'augmented_rank':len(piv),'solvable':not bad}
 if bad:success=False;rows.append(row);break
 sol=[sp.Rational(0)]*len(W)
 for i,p in enumerate(piv):sol[p]=rr[i,len(W)]
 assert all(sum(a*b for a,b in zip(r,sol))==s for r,s in zip(mat,rhs))
 F[N]={w:c for w,c in zip(W,sol) if c}
 row['lyndon_coefficients']={''.join('x' if i==0 else 'y' for i in w):str(c) for w,c in F[N].items()}
 row['nonzero_coefficients']=len(F[N]);row['denominator_lcm']=str(sp.ilcm(*[c.q for c in sol]))
 rows.append(row)
# Full equations re-evaluated in every degree, not just on pivot rows.
if success:
 total={};anti={}
 for n,coords in F.items():
  for w,c in coords.items():
   anti=add(anti,add(LB(w),LB(w,1)),c)
   for mode in range(3):total=add(total,ev(w,mode,NMAX),c)
 assert not anti
 assert not total,('nonzero full defect',total)
 print('Full associative-word checks through weight12: (I)=0, log(II)=0.')
 print('The first uncomputed correction is weight13; no pro-l or infinite lift is asserted.')
(O/'graded_greedy_jets.json').write_text(json.dumps({'initial_weight7':initial,'corrections':rows,'verified_through':rows[-1]['weight'] if success else rows[-1]['weight']-1,'success':success},indent=2))
