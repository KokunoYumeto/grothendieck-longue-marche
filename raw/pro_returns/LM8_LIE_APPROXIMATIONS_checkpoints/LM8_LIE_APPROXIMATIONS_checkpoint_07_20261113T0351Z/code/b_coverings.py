#!/usr/bin/env python3
"""Exact witnesses and uniformly proved covering invariants.

This is not a SmallGroups enumeration. The universal formulas apply to every
two-generator finite quotient; the explicit catalogue is cyclic and
two-generated abelian groups plus the S3 monodromy witness.
"""
from pathlib import Path
from itertools import permutations
import json
import sympy as S

def compose(a,b): return tuple(a[b[i]] for i in range(len(a)))
def inverse(a):
    r=[0]*len(a)
    for i,j in enumerate(a):r[j]=i
    return tuple(r)
def comm(a,b): return compose(compose(compose(inverse(a),inverse(b)),a),b)
def orbit(gens):
    n=len(gens[0]);seen=set();out=[]
    for i in range(n):
        if i in seen:continue
        o={i};todo=[i]
        for j in todo:
            for g in gens:
                if g[j] not in o:o.add(g[j]);todo.append(g[j])
        seen|=o;out.append(sorted(o))
    return out
def main():
    t=S.Symbol('t');rows=[]
    for m in range(2,25):
        R=[t**(m-1)]+[t**-1]*(m-1)
        M=S.zeros(m)
        for i in range(m):
            M[i,i]=2;M[i,(i-1)%m]-=1
        det=int(M.det());assert det==2**m-1
        met=S.expand(1-(t**(m-1)-1)*(t**-1-1)**(m-1))
        terms=S.Poly(S.expand(t**(m-1)*met),t)
        assert terms.degree()==2*(m-1) and terms.nth(0)!=0
        if m<=8:
            J=S.zeros(m)
            for i in range(m):
                J[i,i]=R[i];J[i,(i-1)%m]-=R[i]-1
            assert S.cancel(J.det()-met)==0
        rows.append({'cyclic_degree':m,'abelian_kernel_rank':m-1,
                     'nilpotent_pullback_H1_determinant':det,
                     'metabelian_Jacobian_min_exponent':-(m-1),
                     'metabelian_Jacobian_max_exponent':m-1,
                     'metabelian_Jacobian_nonzero_terms':len(terms.terms())})
    x=(1,0,2);y=(2,1,0);fy=compose(y,comm(x,y))
    assert fy==x
    ab=[]
    for a in range(1,25):
        for b in range(a,25):
            if b%a or a*b>24:continue
            n=a*b
            ab.append({'group':f'C{a}xC{b}','order':n,'N_ab_rank':n+1,
                       'abelian_comparison_kernel_rank':n-1,
                       'metabelian_kernel_nontrivial':n>1,
                       'nilpotent_comparison_isomorphism':n==1})
    report={'cyclic_cover_witnesses':rows,'abelian_quotients_order_at_most24':ab,
            'S3':{'x':x,'y':y,'phi_y':fy,'before_orbits':orbit([x,y]),'after_orbits':orbit([x,fy])},
            'scope':'All formulas proved uniformly in paper; catalogue is not all nonabelian groups of order <=24.'}
    print(json.dumps(report,indent=2))
    Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2))
if __name__=='__main__':main()
