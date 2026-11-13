#!/usr/bin/env python3
"""Exact free-Lie special-derivation images in the second-derived quotient.
All matrix ranks/nullspaces are over QQ, not finite-field estimates.
"""
from itertools import product
from functools import cache
from pathlib import Path
import json,time
import sympy as s
from sympy.polys.matrices import DomainMatrix
OUT=Path(__file__).resolve().parent

def add(p,q,c=1):
 r=p.copy()
 for w,a in q.items():
  r[w]=r.get(w,0)+c*a
  if not r[w]:del r[w]
 return r

def mul(p,q):
 r={}
 for w,a in p.items():
  for v,b in q.items():r[w+v]=r.get(w+v,0)+a*b
 return {w:a for w,a in r.items() if a}
def bracket(p,q):return add(mul(p,q),mul(q,p),-1)
x={(0,):1};y={(1,):1};z={(0,):-1,(1,):-1}
@cache
def is_lyndon(w):return all(w<w[i:]+w[:i] for i in range(1,len(w)))
@cache
def words(n):return tuple(w for w in product((0,1),repeat=n) if is_lyndon(w))
@cache
def split(w):return next(i for i in range(1,len(w)) if is_lyndon(w[i:]))
@cache
def LB(w,mode=0):
 imgs=((x,y),(y,x),(z,y))
 if len(w)==1:return imgs[mode][w[0]]
 k=split(w);return bracket(LB(w[:k],mode),LB(w[k:],mode))
@cache
def meta(w):
 if len(w)<2:raise ValueError('generators separate')
 if len(w)==2:return {(0,0):1}
 k=split(w);u,v=w[:k],w[k:]
 if len(u)>1 and len(v)>1:return {}
 if len(u)==1:
  d=(1,0) if u[0]==0 else (0,1)
  return {(a+d[0],b+d[1]):c for (a,b),c in meta(v).items()}
 d=(1,0) if v[0]==0 else (0,1)
 return {(a+d[0],b+d[1]):-c for (a,b),c in meta(u).items()}
def null(cols):
 A=s.Matrix.hstack(*[s.Matrix(c) for c in cols])
 return DomainMatrix.from_Matrix(A).convert_to(s.QQ).nullspace().to_Matrix()
def rank(A):return DomainMatrix.from_Matrix(A).convert_to(s.QQ).rref()[0].shape[0] if False else A.rank()
def rnk(A):
 if not A.rows or not A.cols:return 0
 return len(DomainMatrix.from_Matrix(A).convert_to(s.QQ).rref()[1])
def mat_meta(W,n):return s.Matrix([[meta(w).get((a,n-2-a),0) for w in W] for a in range(n-1)])
def polynomial(v,n):
 X,Y=s.symbols('X Y');return str(s.expand(sum(v[a]*X**a*Y**(n-2-a) for a in range(n-1))))
def normalized(v):
 vals=[s.Rational(t) for t in v];den=s.ilcm(*[t.q for t in vals]) if len(vals)>1 else vals[0].q
 vals=[int(t*den) for t in vals];g=s.igcd(*vals) if len(vals)>1 else abs(vals[0]);vals=[t//g for t in vals] if g else vals
 if next((t for t in vals if t),1)<0:vals=[-t for t in vals]
 return vals

def main():
 # Weight1: after fixing x, D(y)=[a*x+b*y,y]=a*[x,y].
 # Its one-dimensional image equals the inner derivations ad(a*x).
 weight1=s.Matrix([[1,0]]).rank()-s.Matrix([[1]]).rank()
 assert weight1==0
 first={'weight':1,'outer_special_free_lie':weight1,'metabelian_image_all':weight1,'S3_invariant_free_lie':weight1,'metabelian_image_S3_invariant':weight1,'all_special_of_metabelian_lie':weight1}
 rows=[first];witness={'1':{'all_image_basis':[],'S3_image_basis':[],'all_source_witnesses':[],'S3_source_witnesses':[]}}
 print(first,'computed as rank(D)-rank(inner)',flush=True)
 for n in range(2,11):
  start=time.time();W=words(n);V=words(n+1);d=len(W);basis=[LB(w) for w in W]
  cols=[]
  for f in basis:cols.append([bracket(f,y).get(w,0) for w in V])
  for f in basis:cols.append([-bracket(f,add(x,y)).get(w,0) for w in V])
  K=null(cols);M=mat_meta(W,n);image=M*K[:,:d].T
  # Precisely LM2's infinitesimal centralizer equations (I) and cabling J.
  cols2=[]
  for w,f in zip(W,basis):
   anti=add(f,LB(w,1));J=add(bracket(x,f),bracket(add(x,y),LB(w,2)),-1)
   cols2.append([anti.get(t,0) for t in W]+[J.get(t,0) for t in V])
  KI=null(cols2);imI=M*KI.T
  dim=n-2 if n>=3 else 0
  row={'weight':n,'outer_special_free_lie':K.rows,'metabelian_image_all':rnk(image),'S3_invariant_free_lie':KI.rows,'metabelian_image_S3_invariant':rnk(imI),'all_special_of_metabelian_lie':dim}
  rows.append(row)
  _,pivs=DomainMatrix.from_Matrix(image).convert_to(s.QQ).rref()
  _,pivsi=DomainMatrix.from_Matrix(imI).convert_to(s.QQ).rref()
  witness[str(n)]={'all_image_basis':[polynomial(normalized(image[:,j]),n) for j in pivs],'S3_image_basis':[polynomial(normalized(imI[:,j]),n) for j in pivsi], 'all_source_witnesses':[{'f_lyndon':{''.join('xy'[a] for a in w):str(K[j,i]) for i,w in enumerate(W) if K[j,i]},'g_lyndon':{''.join('xy'[a] for a in w):str(K[j,d+i]) for i,w in enumerate(W) if K[j,d+i]}} for j in pivs], 'S3_source_witnesses':[{''.join('xy'[a] for a in w):str(KI[j,i]) for i,w in enumerate(W) if KI[j,i]} for j in pivsi]}
  print(row,'seconds',round(time.time()-start,3),flush=True)
 (OUT/'d_metabelian.json').write_text(json.dumps({'rows':rows,'image_bases':witness},indent=2))
 print('All dimensions computed over QQ. They concern leading special derivations; no profinite lift is asserted.')
if __name__=='__main__':main()
