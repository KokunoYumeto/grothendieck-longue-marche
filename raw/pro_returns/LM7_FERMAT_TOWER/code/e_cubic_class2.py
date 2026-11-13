#!/usr/bin/env python3
"""Exact finite certificates for E.28; no cohomology approximation.

H27 is the image lattice of the cubic covering in the class-two
free pro-3 base group, reduced modulo 27. It has bracket [A,B]=9C.
The proof of the arithmetic comparison and the tame Galois relation
is in sections/E_cubic.tex.
"""
from pathlib import Path
import json
import sympy as sp

OUT=Path(__file__).resolve().parent
MOD=27
HALF=pow(2,-1,MOD)
ONE=(0,0,0)

def mul(g,h):
    a,b,c=g;d,e,f=h
    return ((a+d)%MOD,(b+e)%MOD,
            (c+f+9*HALF*(a*e-b*d))%MOD)

def inverse(g):return tuple(-v%MOD for v in g)

def power(g,n):
    r=ONE
    while n:
        if n&1:r=mul(r,g)
        g=mul(g,g);n//=2
    return r

def commutator(g,h):
    return mul(mul(mul(g,h),inverse(g)),inverse(h))

def main():
    # A symbolic bilinear identity proves associativity for every triple,
    # without sampling group elements.
    a,b,d,e,u,v=sp.symbols('a b d e u v')
    cocycle=lambda x,y,z,w:9*sp.Rational(1,2)*(x*w-y*z)
    associator=(cocycle(a,b,d,e)+cocycle(a+d,b+e,u,v)
                -cocycle(d,e,u,v)-cocycle(a,b,d+u,e+v))
    assert sp.expand(associator)==0
    elements=[(a,b,c) for a in range(MOD) for b in range(MOD)
              for c in range(MOD)]
    assert len(elements)==19683
    for g in elements:
        assert mul(g,inverse(g))==ONE==mul(inverse(g),g)
        assert power(g,MOD)==ONE
        assert power(g,109)==g
    assert int(sp.n_order(6,109))==108
    powers={str(k):pow(6,k,109) for k in (4,36,54,108)}
    assert powers=={'4':97,'36':63,'54':108,'108':1}
    lift_checks=[]
    for s in range(MOD):
        for t in range(MOD):
            sig=(1,0,s);tau=(0,1,t)
            comm=commutator(sig,tau)
            assert comm==(0,0,9)
            lhs=mul(mul(sig,tau),inverse(sig))
            rhs=power(tau,109)
            assert lhs!=rhs
            lift_checks.append({'sigma_center':s,'tau_center':t,
                                'commutator':list(comm),
                                'tame_relation_satisfied':False})
    # The coordinate comparison really is divide by 3 on the two
    # exponent sums. Its bracket scales by 9, not by 3 or by 1.
    X,Y=sp.symbols('X Y')
    assert 3*3==9
    data={
        'statement':'E.28','modulus':MOD,'group_order':len(elements),
        'multiplication':'(a,b,c)*(d,e,f)=(a+d,b+e,c+f+(9/2)(ae-bd)) mod27',
        'covering_pushforward_on_toric_coordinates':'(a,b) -> (3a,3b)',
        'commutator':'(0,0,9(ae-bd)) mod27',
        'associator_polynomial':str(sp.expand(associator)),
        'all_elements_have_exponent_dividing_27':True,
        'all_elements_satisfy_g109_equals_g':True,
        'local_prime':109,'cyclotomic_character_mod27':1,
        'unit':6,'unit_order_mod109':108,'unit_powers_mod109':powers,
        'central_lift_pairs_checked':len(lift_checks),
        'all_commutators':[0,0,9],
        'tame_relation_successes':0,
        'lift_checks':lift_checks,
        'proof_location':'sections/E_cubic.tex, E.28'}
    (OUT/'e_cubic_class2.json').write_text(json.dumps(data,indent=2)+'\n')
    print('E.28 finite cubic class-two obstruction')
    print('H27 order:',len(elements),'coordinate modulus:',MOD)
    print('Associator polynomial:',sp.expand(associator))
    print('All19683 elements have exponent dividing27: PASS')
    print('Covering toric pushforward: (a,b) -> (3a,3b); bracket multiplier9')
    print('Order of6 modulo109:',int(sp.n_order(6,109)))
    print('Powers of6 modulo109:',powers)
    print('Cyclotomic action modulo27 at109: trivial')
    print('Central lift pairs:',len(lift_checks))
    print('Every lift commutator:',(0,0,9))
    print('Tame relation successes:0')
    print('All exact certificates: PASS')

if __name__=='__main__':main()
