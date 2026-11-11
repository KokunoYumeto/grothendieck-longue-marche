#!/usr/bin/env python3
"""Independent finite algebra checks of OpenAI (2026), Lemma 3.3 and §4.
These checks verify the displayed source formulas and the integral deletion
representation in bounded word length. They do not replace the all-weight
arguments stated in the audit.
"""
from itertools import product,combinations
from math import gcd
from pathlib import Path
from graded_dimensions import add,bracket

def mod(p):return {w:v%2 for w,v in p.items() if v%2}
def plus(a,b):return mod(add(a,b))
def br(a,b):return mod(bracket(a,b))
def deriv(p,D):
 r={}
 for w,c in p.items():
  for j,k in enumerate(w):
   for v,a in D[k].items():
    t=w[:j]+v+w[j+1:];r[t]=r.get(t,0)+c*a
 return mod(r)
g=[{(i,):1} for i in range(4)];X=g[0];U=g[1:];H={(0,0):1};V=[br(X,u) for u in U]
R=[br(H,u) for u in U];Q=[br(plus(H,v),u) for v,u in zip(V,U)]
deltas=[]
for i in range(3):
 d=[{}, {}, {}, {}];d[0]=V[i];d[i+1]=V[i];deltas.append(d)
checks=0
for i in range(3):
 delta=lambda p:deriv(p,deltas[i])
 sq=lambda p:delta(delta(p))
 assert sq(H)==plus(br(H,V[i]),br(R[i],U[i]));checks+=1
 for k in range(3):
  assert sq(U[k])==(Q[i] if k==i else {});checks+=1
  rhs=plus(br(H,V[i]),br(br(V[i],U[i]),U[i])) if k==i else br(Q[i],U[k])
  assert sq(V[k])==rhs;checks+=1
for i,j in combinations(range(3),2):
 e=[{}, {}, {}, {}];e[i+1]=e[j+1]=br(U[i],U[j])
 eps=lambda p:deriv(p,e)
 delta=lambda p:deriv(p,deltas[i])
 vv=lambda p:plus(delta(eps(p)),eps(delta(p)))
 W=plus(br(V[i],U[j]),br(U[i],V[j]))
 assert eps(H)=={};checks+=1
 assert vv(H)==br(H,br(U[i],U[j]));checks+=1
 for k in range(3):
  assert eps(U[k])==(br(U[i],U[j]) if k in (i,j) else {});checks+=1
  assert eps(V[k])==(W if k in (i,j) else {});checks+=1
  rhs=br(U[i],V[j]) if k==i else br(U[j],V[i]) if k==j else {}
  assert vv(U[k])==rhs;checks+=1
  rhs=plus(plus(br(V[i],V[j]),br(W,U[i])),br(U[i],R[j])) if k==i else plus(plus(br(V[i],V[j]),br(W,U[j])),br(U[j],R[i])) if k==j else br(W,U[k])
  assert vv(V[k])==rhs;checks+=1
print('OpenAI Lemma 3.3 source identities checked in F2 associative words:',checks)

# Exact integer edge valuations on the nine distinct characteristic-zero hyperplanes.
planes={'a1':(1,0,0),'a2':(0,1,0),'a3':(0,0,1),'p12':(1,-1,0),'m12':(1,1,0),'p13':(1,0,-1),'m13':(1,0,1),'p23':(0,1,-1),'m23':(0,1,1)}
edges={frozenset(('0','p')):{'p23':1,'m23':-1},frozenset(('0','w')):{'p12':1,'m12':-1},frozenset(('e','p')):{'a3':1,'m23':-1},frozenset(('e','w')):{'a1':1,'m12':-1},frozenset(('p','w')):{'a2':1,'p13':1,'m12':-1,'m23':-1}}
def val(h,a,b):return edges.get(frozenset((a,b)),{}).get(h,0) if a!=b else 0
def delete(h,w):
 r={};ww=('0',)+w+('w',)
 for k in range(1,len(ww)-1):
  c=val(h,ww[k],ww[k+1])-val(h,ww[k-1],ww[k]);v=w[:k-1]+w[k:]
  if c:r[v]=r.get(v,0)+c
 return {w:c for w,c in r.items() if c}
def apply(h,p):
 r={}
 for w,c in p.items():r=add(r,delete(h,w),c)
 return r
def cross(u,v):
 a=(u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]);d=0
 for k in a:d=gcd(d,abs(k))
 a=tuple(k//d for k in a)
 return a if next(k for k in a if k)>0 else tuple(-k for k in a)
flats={cross(planes[h],planes[k]) for h,k in combinations(planes,2)}
inc={f:[h for h,v in planes.items() if sum(a*b for a,b in zip(f,v))==0] for f in flats}
checks=0
for n in range(6):
 for w in product(('0','e','p'),repeat=n):
  for f,hs in inc.items():
   for h in hs:
    q={}
    for k in hs:q=add(q,add(apply(h,delete(k,w)),apply(k,delete(h,w)),-1))
    assert not q,(w,f,h,q);checks+=1
print('Distinct codimension-two B3 flats:',len(flats))
print('Integral deletion incidence relations, word lengths 0 through 5:',checks)
# Repeated-letter endpoints are included. Plus and minus planes are never merged.
print('All checks passed; these finite checks are supporting evidence, not all-weight certification.')
