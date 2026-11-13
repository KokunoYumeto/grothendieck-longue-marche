#!/usr/bin/env python3
"""Exact field and finite-group certificates for E.31.

The arithmetic map, rational generalized-Jacobian point, its affine
tangential shift, and the local tame argument are proved in
sections/E_intrinsic_obstruction.tex.
"""
from pathlib import Path
import json
import sympy as sp
from e_cubic_abelian import K

OUT=Path(__file__).resolve().parent
MOD=3
HALF=2
ONE=(0,0,0)

def mul(g,h):
    a,b,c=g;d,e,f=h
    return ((a+d)%3,(b+e)%3,(c+f+HALF*(a*e-b*d))%3)

def inv(g):return tuple(-a%3 for a in g)

def power(g,n):
    r=ONE
    for _ in range(n):r=mul(r,g)
    return r

def comm(g,h):return mul(mul(mul(g,h),inv(g)),inv(h))

def residue(q,p=7):
    # At pi=3+zeta, zeta=-3=4 modulo7.
    return ((q.a.numerator*pow(q.a.denominator,-1,p))
            +4*q.b.numerator*pow(q.b.denominator,-1,p))%p

def main():
    zeta=K(0,1);lam=1-zeta;pi=3+zeta;barpi=2-zeta
    assert pi*barpi==7 and pi.norm()==7
    assert lam**2==-3*zeta
    leading=-1/(3*lam)
    assert leading==zeta*lam**-3
    char_h=barpi**-3;char_g=7*barpi**-3
    total_h=leading*char_h;total_g=char_g
    assert total_h==zeta*(lam*barpi)**-3
    assert total_g==7*barpi**-3
    toric=(K(7)/pi.norm(),K(7)/pi.norm())
    assert toric==(K(1),K(1))
    assert residue(zeta)==4 and residue(lam)==4 and residue(barpi)==5
    # Use the unit expression at pi. Expanding barpi^-3 in the Q-basis
    # introduces rational denominators divisible by7 that cancel only
    # after localizing at pi, so direct coefficient reduction is invalid.
    total_h_residue=residue(leading)*pow(residue(barpi),-3,7)%7
    assert residue(leading)==4 and total_h_residue==3
    frob_ratio=pow(total_h_residue,2,7)
    assert frob_ratio==pow(4,2,7)==2
    s,w=sp.symbols('s w')
    branch=1+s**3/3-s**6/9
    h=(1-branch)/(1-w*branch)
    assert sp.simplify(sp.limit(h/s**3,s,0)+1/(3*(1-w)))==0
    elements=[(a,b,c) for a in range(3) for b in range(3) for c in range(3)]
    for g in elements:
        assert power(g,3)==ONE and power(g,7)==g
        for k in range(3):
            x=(k,0,0)
            actual=mul(mul(x,g),inv(x))
            expected=(g[0],g[1],(g[2]+k*g[1])%3)
            assert actual==expected
    checks=[]
    for c in range(3):
        for d in range(3):
            sig=(2,0,c);tau=(0,1,d)
            value=comm(sig,tau)
            assert value==(0,0,2)
            assert mul(mul(sig,tau),inv(sig))!=power(tau,7)
            checks.append({'frobenius_center':c,'inertia_center':d,
                           'commutator':value,'tame_relation_satisfied':False})
    data={
        'statement':'E.31','point_t':['7','7','1','1','3+zeta'],
        'norm_pi':7,'toric_retraction':['1','1'],
        'morphism_h':'(x+y)/(x+zeta*y)',
        'divisor_h':'3O-3C2',
        'divisor_1_minus_h':'B0+B1+B2-3C2',
        'character_h':char_h.data(),'character_1_minus_h':char_g.data(),
        'tangential_leading_constant':leading.data(),
        'tangential_constant_simplified':'zeta*lambda^-3',
        'total_h':total_h.data(),'total_1_minus_h':total_g.data(),
        'total_Kummer_classes_mod3':['zeta','7'],
        'local_residues':{'zeta':4,'lambda':4,'barpi':5,
                          'leading_h':4,'total_h':3},
        'frobenius_kummer_exponent':2,'tame_inertia_kummer_exponent':1,
        'group_order':27,'exponent':3,
        'based_action_shear':'(a,b,c) -> (a,b,c+kappa3(zeta)(g)*b)',
        'shear_checks':81,'lift_pairs_checked':9,
        'lift_checks':checks,'tame_relation_successes':0,
        'proof_location':'sections/E_intrinsic_obstruction.tex'}
    (OUT/'e_intrinsic_obstruction.json').write_text(json.dumps(data,indent=2)+'\n')
    print('E.31 intrinsic cubic class-two obstruction')
    print('Rational torus point: (7,7,1,1,3+zeta); norm(pi)=7')
    print('Toric minimum: (1,1), hence zero Kummer class')
    print('Tangent leading constant: zeta*lambda^-3')
    print('Target total Kummer pair modulo3: (zeta,7)')
    print('At pi over7: zeta=4, lambda=4, barpi=5, total h=3 modulo7')
    print('Frobenius/inertia exponents: (2,0), (0,1)')
    print('All 27 elements have exponent3; 81 shear checks PASS')
    print('All 9 lift pairs have commutator (0,0,2)')
    print('Tame relation successes: 0')
    print('All exact certificates: PASS')

if __name__=='__main__':main()
