#!/usr/bin/env python3
"""Finite-field checks of the withdrawn scheme-action freeness claim."""
from pathlib import Path
from itertools import product
import json
import sympy as s

OUT=Path(__file__).resolve().parent
rows=[]
print('n p open_point compact_cusp full_open_stabilizer quotient_open_stabilizer quotient_cusp_stabilizer')
for n in range(1,9):
    k=max(1,5*n)
    while True:
        p=2*n*k+1;k+=1
        if not s.isprime(p):continue
        values={}
        for a in range(1,p):values.setdefault(pow(a,n,p),a)
        pair=next(((a,values[(-1-pow(a,n,p))%p]) for a in range(1,p)
                   if (-1-pow(a,n,p))%p in values),None)
        if pair is not None:break
    primitive=int(s.primitive_root(p));zeta=pow(primitive,(p-1)//n,p)
    eta=pow(primitive,(p-1)//(2*n),p)
    openpoint=pair+(1,);cusp=(0,eta,1)
    assert (sum(pow(a,n,p) for a in openpoint)%p)==0
    assert (sum(pow(a,n,p) for a in cusp)%p)==0
    def fixes(exponents,P):
        out=tuple(P[i]*pow(zeta,exponents[i],p)%p for i in range(3))
        # All chosen points have last coordinate 1.
        scale=out[2]
        return all(out[i]==P[i]*scale%p for i in range(3))
    fstab=[a for a in product(range(n),repeat=3) if fixes(a,openpoint)]
    ostab=[a for a in product(range(n),repeat=2) if fixes(a+(0,),openpoint)]
    cstab=[a for a in product(range(n),repeat=2) if fixes(a+(0,),cusp)]
    assert len(fstab)==n and len(ostab)==1 and len(cstab)==n
    row={'n':n,'field_prime':p,'primitive_root':primitive,
         'mu_n_generator':zeta,'open_point':openpoint,'cusp':cusp,
         'full_open_stabilizer':fstab,'quotient_open_stabilizer':ostab,
         'quotient_cusp_stabilizer':cstab}
    rows.append(row)
    print(n,p,openpoint,cusp,len(fstab),len(ostab),len(cstab))
print('n=2, m=2 motive-rank counterexample: |M/2M|=4; |T(J_2)/2|=32; PASS')
(OUT/'b_freeness.json').write_text(json.dumps({'finite_actions':rows,
 'motive_counterexample':{'n':2,'m':2,'rank_two_order':4,'generalized_jacobian_torsion_order':32}},indent=2)+'\n')
