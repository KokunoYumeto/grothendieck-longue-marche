#!/usr/bin/env python3
"""Exact finite marking and tensor certificate for the C40 candidate.

No finite calculation here asserts the infinite lifting theorem.  The latter
is supplied separately by the source-centralization proof.
"""
from collections import deque
from pathlib import Path
import hashlib,json

I=(1,0,0,1);S=(0,1,1,0);R=(-1,-1,1,0)
def mm(a,b):
 return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
         a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])
def tr(a):return (a[0],a[2],a[1],a[3])
def inv(a):
 d=a[0]*a[3]-a[1]*a[2];assert d in (-1,1)
 return (a[3]//d,-a[1]//d,-a[2]//d,a[0]//d)
assert mm(S,S)==I and mm(mm(R,R),R)==I
E=mm(S,R);T=mm(R,S)
assert mm(T,T)==I and mm(mm(T,S),T)==E and mm(mm(T,E),T)==S
def pm(a,b):return tuple(mm(x,y) for x,y in zip(a,b))
def pi(a):return tuple(inv(x) for x in a)
one=(I,I,I);X=(S,inv(R),E);Y=(E,S,inv(R))
elements=[one];words=[()];index={one:0};q=deque([0])
while q:
 i=q.popleft()
 for j,g in enumerate((X,Y)):
  v=pm(elements[i],g)
  if v not in index:index[v]=len(elements);elements.append(v);words.append(words[i]+(j,));q.append(len(elements)-1)
assert len(elements)==108
def evaluate(w,a,b):
 v=one
 for j in w:v=pm(v,(a,b)[j])
 return v
def induced(a,b):
 out=tuple(index[evaluate(w,a,b)] for w in words)
 assert len(set(out))==108
 for i,v in enumerate(elements):
  for old,new in ((X,a),(Y,b)):
   assert out[index[pm(v,old)]]==index[pm(elements[out[i]],new)]
 return out
sigma=induced(Y,X);rho=induced(pi(pm(X,Y)),X)
def comp(a,b):return tuple(a[i] for i in b)
ident=tuple(range(108))
assert comp(sigma,sigma)==ident and comp(comp(rho,rho),rho)==ident
def inner(g):return tuple(index[pm(pm(g,v),pi(g))] for v in elements)
rs=comp(rho,sigma);sr=comp(sigma,rho)
assert comp(rs,rs)==inner(X) and comp(sr,sr)==inner(Y)
aut=[ident];seen={ident};q=deque([ident])
while q:
 a=q.popleft()
 for g in (sigma,rho):
  v=comp(a,g)
  if v not in seen:seen.add(v);aut.append(v);q.append(v)
assert len(aut)==648
assert len({inner(g) for g in elements})==108
assert sum(all(pm(g,h)==pm(h,g) for h in (X,Y)) for g in elements)==1
derived=pm(pm(pm(pi(X),pi(Y)),X),Y)
assert all(a!=I and mm(mm(a,a),a)==I for a in derived)
signs=sorted({tuple(0 if a[0]*a[3]-a[1]*a[2]==1 else 1 for a in g) for g in elements})
assert signs==[(0,0,0),(0,1,1),(1,0,1),(1,1,0)]
B=(2,-1,-1,2);C=mm(B,tr(T))
assert C==(-1,-1,-1,2) and tr(C)==C
for A in (S,R):
 assert mm(mm(A,B),tr(A))==B
 Ap=mm(mm(T,A),T)
 assert mm(mm(A,C),tr(Ap))==C
# Actual column action r:x->(xy)^-1,y->x is conjugated to R
# by the displayed integral basis matrix of determinant -3.
R_actual=(-1,1,-1,0);change=(1,2,2,1)
assert mm(R_actual,change)==mm(change,R) and mm(S,change)==mm(change,S)
report={'status':'PASS','scope':'Exact finite quotient, marking, and sibling tensor data only',
 'Q0_order':108,'Qtilde_order':648,'Q0_center_order':1,'inner_Q0_order':108,
 'S':S,'R':R,'E':E,'T':T,'X':X,'Y':Y,'Q0_signs':signs,
 'commutator_has_nonzero_each_C3_coordinate':derived,
 'actual_column_R':R_actual,'basis_change_det_minus3':change,
 'invariant_tensor_B':B,'sibling_tensor_C':C,'sibling_tensor_symmetric':True,
 'factor_exchange_on_H2':'minus transpose, hence -1 on the sibling invariant line',
 'Q0_elements':elements,'sigma_permutation':sigma,'rho_permutation':rho,
 'all_generator_edges_verified':True,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('Q0_elements','sigma_permutation','rho_permutation')},indent=2))
