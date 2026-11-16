#!/usr/bin/env python3
"""Exact rational kernels for special S3-invariant degree-nine derivations."""
from itertools import product
from pathlib import Path
import json
import sympy as sp
from check_lie_witnesses import L,lyndon,add,scale,bracket,var,substitute

def coeff_meta(p):
    out={}
    for w,c in p.items():
        if w.endswith('y'):
            key=(w.count('x')-1,w.count('y')-1)
            out[key]=out.get(key,0)+c
    return {k:v for k,v in out.items() if v}

def main():
    words=[''.join(w) for w in product('xy',repeat=9) if lyndon(''.join(w))]
    x=var('x');y=var('y');z=add(scale(x,-1),scale(y,-1))
    cols=[]
    for w in words:
        h=L(w)
        antisym=add(h,substitute(h,{'x':y,'y':x}))
        cabling=add(bracket(x,h),scale(bracket(add(x,y),substitute(h,{'x':z,'y':y})),-1))
        cycle=add(h,substitute(h,{'x':y,'y':z}),substitute(h,{'x':z,'y':x}))
        cols.append({(i,t):c for i,p in enumerate((antisym,cabling,cycle)) for t,c in p.items()})
    rows=sorted({key for col in cols for key in col})
    M=sp.Matrix([[col.get(key,0) for col in cols] for key in rows])
    ns=M.nullspace()
    print('degree9 Lyndon dimension',len(words),'constraint shape',M.shape,'kernel dimension',len(ns))
    assert len(ns)==4
    metas=[]
    for v in ns:
        h=add(*(scale(L(w),c) for w,c in zip(words,v) if c))
        metas.append(coeff_meta(h))
    monomials=[(a,7-a) for a in range(8)]
    F=sp.Matrix([[p.get(m,0) for p in metas] for m in monomials])
    print('metabelian image rank',F.rank())
    assert F.rank()==2
    G=sp.Matrix([sp.binomial(9,a+1) for a in range(8)])
    P=sp.Matrix([1 if a in(2,5) else 3 if a in(3,4) else 0 for a in range(8)])
    assert sp.Matrix.hstack(G,P).rank()==2
    assert sp.Matrix.hstack(F,G,P).rank()==2
    print('metabelian image equals span(G9,P9): YES')
    coeffs=F.gauss_jordan_solve(G)[0]
    params=set().union(*(c.free_symbols for c in coeffs))
    coeffs=coeffs.subs({p:0 for p in params})
    hG=sum((v*c for v,c in zip(ns,coeffs)),sp.zeros(len(words),1))
    assert F*coeffs==G
    den=sp.ilcm(*[c.q for c in hG])
    print('explicit invariant G9 lift common denominator',den)
    print('G9 lift nonzero Lyndon coefficients',[(w,str(c)) for w,c in zip(words,hG) if c])
    # Purely metabelian upper bound: symmetry and cabling on degree7 polynomials.
    X,Y=sp.symbols('X Y');Z=-X-Y
    variables=sp.symbols('v0:8')
    p=sum(variables[a]*X**a*Y**(7-a) for a in range(8))
    equations=[]
    for expr in (p-p.xreplace({X:Y,Y:X}),X*p+(X+Y)*p.xreplace({X:Z,Y:Y}),
                 p+p.xreplace({X:Y,Y:Z})+p.xreplace({X:Z,Y:X})):
        equations.extend(sp.Poly(sp.expand(expr),X,Y).coeffs())
    C,_=sp.linear_eq_to_matrix(equations,variables)
    print('metabelian constraint rank',C.rank(),'kernel dimension',len(C.nullspace()))
    assert len(C.nullspace())==2
    assert C*G==sp.zeros(C.rows,1) and C*P==sp.zeros(C.rows,1)
    out={'lyndon_words':words,'constraint_shape':list(M.shape),'kernel_dimension':len(ns),
        'metabelian_rank':int(F.rank()),'kernel_basis':[[str(c) for c in v] for v in ns],
        'G9_lift':{w:str(c) for w,c in zip(words,hG) if c},'G9_lift_denominator':int(den),
        'meta_monomials':monomials,'meta_basis':[[str(x) for x in F.col(i)] for i in range(F.cols)]}
    (Path(__file__).resolve().parent.parent/'records'/'invariant_dimensions.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__': main()
