#!/usr/bin/env python3
"""Characteristic-zero verification of the independently built pentagon map.

Re-evaluates every polynomial with integer arithmetic, recomputes the entire
special invariant space over QQ, and verifies one exact kernel vector in
every associative coefficient. A nonzero 3x3 minor certifies the rank.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy,time,math
import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.matrices.normalforms import smith_normal_form

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_pentagon9.py'))
G=d['lie'].__wrapped__.__globals__
def add(a,b,c=1):
    r=a.copy()
    for w,v in b.items():
        r[w]=r.get(w,0)+c*v
        if not r[w]:del r[w]
    return r
def scale(a,c):return {w:c*v for w,v in a.items() if c*v}
def mul(a,b):
    r={}
    for w,c in a.items():
        for v,e in b.items():r[w+v]=r.get(w+v,0)+c*e
    return {w:c for w,c in r.items() if c}
def br(a,b):return add(mul(a,b),mul(b,a),-1)
def deriv(q,D):
    out={}
    for w,c in q.items():
        for i,a in enumerate(w):
            for v,b in D[a].items():
                t=w[:i]+v+w[i+1:];out[t]=out.get(t,0)+c*b
    return {w:c for w,c in out.items() if c}
G.update(add=add,scale=scale,mul=mul,br=br,deriv=deriv,z={(0,):-1,(1,):-1})
X=G['X'];G['Da']=(br(X[0],X[1]),br(X[1],X[0]),{});G['Db']=({},br(X[1],X[2]),br(X[2],X[1]))
for name in ('lie','DL','evalq'):G[name].cache_clear()
W=G['W'];cols=[]
for w in W:
    f=G['lie'](w);anti=add(f,G['lie'](w,1));cab=add(br(G['x'],f),br(add(G['x'],G['y']),G['lie'](w,2)),-1)
    cols.append([anti.get(t,0) for t in G['rows9']]+[cab.get(t,0) for t in G['rows10']])
C=sp.Matrix(cols).T;raw=DomainMatrix.from_Matrix(C).convert_to(sp.QQ).nullspace().to_Matrix()
assert raw.shape==(4,56)
def primitive(values):
    values=[sp.Rational(x) for x in values];den=sp.ilcm(*[x.q for x in values]);ints=[int(x*den) for x in values]
    g=math.gcd(*ints);return [x//g for x in ints]
basis=np.array([primitive(row) for row in raw.tolist()],dtype=np.int64).T
assert not np.any(np.array(C.tolist(),dtype=np.int64)@basis)
pent=[{} for _ in range(4)];start=time.time()
for i,w in enumerate(W):
    q=add(add(add(G['evalq'](w,0),G['evalq'](w,1)),G['evalq'](w,2),-1),G['evalq'](w,3),-1)
    for j in range(4):pent[j]=add(pent[j],q,int(basis[i,j]))
rows=G['rows3'];P=np.array([[q.get(w,0) for q in pent] for w in rows],dtype=np.int64)
_,ind=G['rref'](P.T);assert len(ind)==3
small=sp.Matrix(P[ind].tolist());kernel=primitive(small.nullspace()[0]);kernel=np.array(kernel,dtype=np.int64)
assert not np.any(P@kernel)
_,colind=small.rref();minor=small[:,list(colind)];det=int(minor.det());assert det
M=np.array([[G['meta'](w).get((i,7-i),0) for w in W] for i in range(8)],dtype=np.int64)
image=M@basis;mk=image@kernel;gamma=np.array([math.comb(9,i+1) for i in range(8)])
assert sp.Matrix(image.tolist()).rank()==2 and sp.Matrix(np.column_stack((mk,gamma)).tolist()).rank()==1
smith_basis=smith_normal_form(sp.Matrix(basis.tolist()),domain=sp.ZZ)
basis_factors=[abs(int(smith_basis[i,i])) for i in range(4)]
smith_constraints=smith_normal_form(C,domain=sp.ZZ)
constraint_factors=[abs(int(smith_constraints[i,i])) for i in range(56) if smith_constraints[i,i]]
smith_metabelian=smith_normal_form(sp.Matrix(image.tolist()),domain=sp.ZZ)
metabelian_factors=[abs(int(smith_metabelian[i,i])) for i in range(4) if smith_metabelian[i,i]]
np.savez_compressed(here/'de_pentagon9_rational_certificate.npz',special_basis=basis,pentagon=P,kernel=kernel,metabelian=image)
out={'field':'QQ','special_invariant_dimension':4,'pentagon_rank':3,'pentagon_kernel_dimension':1,
     'special_metabelian_image_dimension':2,'pentagon_metabelian_image_dimension':1,'kernel_is_gamma_line':True,
     'kernel_in_special_basis':kernel.tolist(),'kernel_metabelian_vector':mk.tolist(),'gamma_vector':gamma.tolist(),
     'nonzero_rank_minor_determinant':det,'rank_minor_columns':list(colind),
     'rank_minor_word_rows':[''.join(str(a+1) for a in rows[i]) for i in ind],
     'maximum_absolute_integer_coefficient':int(abs(P).max()),'all_19683_coefficients_of_kernel_verified_zero':True,
     'special_basis_smith_factors':basis_factors,'special_constraint_smith_factors':constraint_factors,
     'special_metabelian_smith_factors':metabelian_factors,'special_metabelian_matrix':image.tolist(),
     'pentagon_rank_minor_matrix':[[int(c) for c in row] for row in small.tolist()],
     'special_basis_lyndon':[{''.join('xy'[a] for a in w):int(basis[i,j]) for i,w in enumerate(W) if basis[i,j]} for j in range(4)],
     'elapsed_integer_pentagon_seconds':round(time.time()-start,3)}
(here/'de_pentagon9_rational.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='special_basis_lyndon'},indent=2),flush=True)
