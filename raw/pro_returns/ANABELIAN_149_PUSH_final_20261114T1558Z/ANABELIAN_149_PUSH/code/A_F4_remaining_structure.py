#!/usr/bin/env python3
"""Exact arithmetic certificates for the two unresolved ordinary F4 classes.
Checks point counts, full Weil polynomial, geometric-simplicity root ratios,
and the actualF4 Frobenius packet congruences. No A1 conclusion is asserted.
"""
from pathlib import Path
from itertools import product
import json
import sympy as sp
from A_theta_F4_moduli_witnesses import Base,Tower
import A_F4_remaining_frobenius_packets as packet

def count(q,F):
    # alpha is encoded2 inF4, and6 inF16 with binarymodulus19.
    alpha=2 if q==4 else 6;alpha2=F.mul(alpha,alpha);N=1
    for z in range(q):
        den=F.mul(z,z)^z^alpha
        if not den:N+=1;continue
        value=z^F.mul(alpha2,F.mul(z^1,F.inv(den)))
        tr=0;v=value
        for _ in range(q.bit_length()-1):tr^=v;v=F.mul(v,v)
        assert tr in [0,1];N+=2*(tr==0)
    return N

def main():
    F4=Base(2,7);F16=Base(4,19)
    counts={4:count(4,F4),16:count(16,F16)};assert counts=={4:7,16:15}
    x,z=sp.symbols('x z');s1=5-counts[4];s2=(s1*s1-(17-counts[16]))//2
    P=sp.Poly(x**4-s1*x**3+s2*x**2-4*s1*x+16,x)
    assert P.as_expr()==x**4+2*x**3+x**2+8*x+16
    assert sp.Poly(P,x,modulus=3).is_irreducible
    raw=sp.Poly(sp.resultant(P.as_expr(),P.as_expr().subs(x,z*x),x),z).monic()
    nontrivial=raw.exquo(sp.Poly((z-1)**4,z));ratio=nontrivial.sqf_part().monic();assert ratio.degree()==8
    den,integer=ratio.clear_denoms(convert=True);content,primitive=integer.primitive()
    cyclo_orders=[]
    for a,b,c,d in product(range(5),range(3),range(2),range(2)):
        n=2**a*3**b*5**c*7**d
        if sp.totient(n)<=8:cyclo_orders.append(n)
    cyclo_orders=sorted(set(cyclo_orders))
    assert cyclo_orders==[1,2,3,4,5,6,7,8,9,10,12,14,15,16,18,20,24,30]
    cyclo_checks=[]
    for n in cyclo_orders:
        gcd=sp.gcd(ratio,sp.Poly(sp.cyclotomic_poly(n,z),z));assert gcd.degree()==0
        cyclo_checks.append({'n':n,'phi':int(sp.totient(n)),'gcd_degree':0})
    # Re-run certificates with the actual fourth-power Frobenius. Passing to
    # its square may enlarge the integral order and weaken the bound at7.
    packet.P=sp.Poly(packet.X**4+2*packet.X**3+packet.X**2+8*packet.X+16,packet.X)
    packet.M=[[0,0,0,-16],[1,0,0,-8],[0,1,0,-1],[0,0,1,-2]]
    rows=[packet.packet(ell) for ell in [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73]]
    out={'status':'PASS','point_counts':counts,'Weil_polynomial_coefficients_ascending':[int(P.nth(i)) for i in range(5)],'irreducible_modulo':3,'primitive_integer_root_ratio_polynomial_coefficients_ascending':[int(primitive.nth(i)) for i in range(9)],'squarefree_root_ratio_degree':8,'cyclotomic_checks':cyclo_checks,'field_size':4,'packets':rows,'geometric_interpretation':'No root ratio is a root of unity. AllFrobeniuspowers have minimal degree4; Jacobian geometrically simple. Geometric rational endomorphism algebra isQ(pi), by theTate-module injection and centralizer dimension. These are method obstructions, notA1 conclusions.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS counts',counts,'P',P.as_expr(),'ratio',primitive.as_expr(),flush=True)
    print('entire-primary exclusion candidates',[r['ell'] for r in rows if r['theta_exponent_bound']==1],flush=True)
if __name__=='__main__':main()
