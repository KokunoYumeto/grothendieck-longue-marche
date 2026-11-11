#!/usr/bin/env python3
"""Extend the explicit weight-seven witness in genuine (I),(II) through weight 12.
All products of log(f) terms begin in weight14, so this range is linear in
F=log(f), but substitutes the complete BCH logarithm log Z to required degree.
We impose the extra ansatz that the coefficients in even weights vanish,
and solve the odd coefficients in weights 9 and 11 with all equations through12.
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
initial_coords={tuple(0 if c=='x' else 1 for c in w):sp.Rational(a) for w,a in initial.items()}
unknowns=[(n,w) for n in (9,11) for w in words(n)]
rowkeys=[(kind,n,w) for kind in (0,1) for n in range(8,NMAX+1) for w in words(n)]
index={key:i for i,key in enumerate(rowkeys)}
entries={};rhs={}
for w,c in initial_coords.items():
 for mode in range(3):
  for v,a in ev(w,mode,NMAX).items():
   key=(1,len(v),v)
   if key in index:rhs[index[key]]=rhs.get(index[key],0)-c*a
for j,(n,w) in enumerate(unknowns):
 for v,c in add(LB(w),LB(w,1)).items():
  key=(0,n,v)
  if key in index and c:entries[index[key],j]=c
 q={}
 for mode in range(3):q=add(q,ev(w,mode,NMAX))
 for v,c in q.items():
  key=(1,len(v),v)
  if key in index and c:entries[index[key],j]=c
 if j%100==0:print('columns built',j,'of',len(unknowns),flush=True)
for i,c in rhs.items():
 if c:entries[i,len(unknowns)]=c
print('global system',len(rowkeys),'equations',len(unknowns),'unknowns','nonzeros',len(entries),flush=True)
# Solve by weight while retaining every free parameter from previous weights.
# This is exact block elimination of the simultaneous system, not greedy choice.
constant=sp.zeros(0,1);param=sp.zeros(0,0);kprev=0;stages=[]
for n in (9,11):
 ids=[index[key] for key in rowkeys if key[1] in (n,n+1)]
 new=[j for j,(d,w) in enumerate(unknowns) if d==n]
 pcount=param.cols;k=len(new)
 old=sp.SparseMatrix(len(ids),kprev,{(i,j):entries[row,j] for i,row in enumerate(ids) for j in range(kprev) if (row,j) in entries})
 cur=sp.SparseMatrix(len(ids),k,{(i,h):entries[row,j] for i,row in enumerate(ids) for h,j in enumerate(new) if (row,j) in entries})
 rhsvec=sp.Matrix([rhs.get(row,0) for row in ids])-old*constant
 A=(old*param).row_join(cur)
 aug=DomainMatrix.from_Matrix(A.row_join(rhsvec)).convert_to(sp.QQ)
 rr,piv=aug.rref();rr=rr.to_Matrix();bad=A.cols in piv
 print('weight block',n,'variables',A.cols,'rank',len(piv)-int(bad),'consistent',not bad,flush=True)
 assert not bad,('inconsistent weight',n)
 free=[j for j in range(A.cols) if j not in piv]
 particular=sp.zeros(A.cols,1);K=sp.zeros(A.cols,len(free))
 for j,f in enumerate(free):K[f,j]=1
 for i,p in enumerate(piv):
  particular[p]=rr[i,A.cols]
  for j,f in enumerate(free):K[p,j]=-rr[i,f]
 assert A*particular==rhsvec
 assert A*K==sp.zeros(A.rows,K.cols)
 oldconstant=constant+param*particular[:pcount,:]
 oldparam=param*K[:pcount,:]
 constant=oldconstant.col_join(particular[pcount:,:])
 param=oldparam.col_join(K[pcount:,:]);kprev+=k
 stages.append({'weight':n,'variables':A.cols,'rank':len(piv),'remaining_parameters':len(free)})
 print('compatible jet free parameters',param.cols,flush=True)
sol=list(constant)
print('global rank',len(unknowns)-param.cols,'unknowns',len(unknowns),'solvable True',flush=True)
F={7:initial_coords}
for (n,w),c in zip(unknowns,sol):
 if c:F.setdefault(n,{})[w]=c
total={};anti={}
for n,coords in F.items():
 for w,c in coords.items():
  anti=add(anti,add(LB(w),LB(w,1)),c)
  for mode in range(3):total=add(total,ev(w,mode,NMAX),c)
assert not anti
assert not total,('nonzero full defect',total)
corrections=[]
for n in range(8,NMAX+1):
 c=F.get(n,{})
 den=sp.ilcm(*[a.q for a in c.values()]) if len(c)>1 else next(iter(c.values())).q if c else 1
 corrections.append({'weight':n,'nonzero_coefficients':len(c),'denominator_lcm':str(den),'lyndon_coefficients':{''.join('x' if i==0 else 'y' for i in w):str(a) for w,a in c.items()}})
 print('weight',n,'nonzero coefficients',len(c),'denominator lcm',den,flush=True)
print('Full associative-word checks through weight12: (I)=0, log(II)=0.')
print('The first uncomputed correction is weight13; no pro-l or infinite lift is asserted.')
(O/'graded_rational_jets.json').write_text(json.dumps({'initial_weight7':initial,'corrections':corrections,'verified_through':12,'rank':len(unknowns)-param.cols,'stages':stages,'unknowns':len(unknowns),'success':True},indent=2))
