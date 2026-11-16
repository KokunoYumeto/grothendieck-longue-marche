#!/usr/bin/env python3
"""Exact identities and tail coefficients for the actual A54 Heisenberg curve."""
from pathlib import Path
from fractions import Fraction
import json
import sympy as s

x,a,t,U,V,eta,pi,u=s.symbols('x a t U V eta pi u')
psi=5*x**12-62*x**10-105*x**8+300*x**6-125*x**4+50*x**2+1
g=3*x*x+1
h=x**12-61*x**10-102*x**8+6*x**6-43*x**4+7*x*x
assert s.expand(g**5+5*h-psi)==0
factor=2*x*(x*x-2)**3*(x*x-x+1)*(x*x+x+1)
assert s.Poly(s.diff(h,x)-factor,x,modulus=5).is_zero


def modp(z,P=None):
    z=s.Poly(s.expand(z),a,modulus=5)
    return z.rem(s.Poly(P,a,modulus=5)).as_expr() if P is not None else z.as_expr()


def nonbranch_chart(P,k):
    ga=g.subs(x,a)
    ha=h.subs(x,a)
    # Work with an integral numerator of N; ga^5 is a 5-adic unit.
    M=s.expand((h*ga**5-ha*g**5).subs(x,a+t))
    coefficients=[]
    for j in range(13):
        c=s.Poly(M,t).nth(j)
        integral_remainder=s.rem(c,P,a)
        assert all(q.q==1 for q in s.Poly(integral_remainder,a).all_coeffs())
        coefficients.append(modp(integral_remainder,P))
    assert all(coefficients[j]==0 for j in range(k))
    assert s.gcd(s.Poly(coefficients[k],a,modulus=5),s.Poly(P,a,modulus=5)).degree()==0
    assert s.gcd(s.Poly(ga,a,modulus=5),s.Poly(P,a,modulus=5)).degree()==0
    # LHS residue is ga^5, and the integral numerator M has another ga^5.
    inv=s.invert(s.Poly(ga**10,a,modulus=5),s.Poly(P,a,modulus=5)).as_expr()
    tail_c=modp(coefficients[k]*inv,P)
    assert tail_c!=0
    return {'x_polynomial':str(P),'points':2*s.degree(P,a),'k':k,
            'tail_genus':2*(k-1),'reduced_tail_coefficient':str(tail_c),
            'lower_coefficients_divisible_by_5':True}


def twotorsion_chart(a0,k):
    ga=g.subs(x,a0)
    ha=h.subs(x,a0)
    M=s.expand((h*ga**5-ha*g**5).subs(x,a0+t))
    coefficients=[int(s.Poly(M,t).nth(j))%5 for j in range(13)]
    r=k//2
    assert all(coefficients[j]==0 for j in range(r))
    assert coefficients[r]
    delta=(3*a0*a0-1)%5
    c=coefficients[r]*pow(int(ga),-10,5)*pow(delta,-r,5)%5
    assert c
    return {'point':[a0,0],'points':1,'k':k,'tail_genus':2*(k-1),
            'reduced_tail_coefficient':c,'lower_coefficients_divisible_by_5':True}


def main():
    # Exact binomial identities, before any reduction or asymptotic truncation.
    lhs=s.expand(((1+eta*V)**5-1)/(5*eta))
    rhs=V+2*eta*V**2+2*eta**2*V**3+eta**3*V**4-V**5
    assert s.rem(lhs-rhs,eta**4+5,eta)==0
    main_lhs=s.expand(((g+pi*u)**5-g**5)/5)
    main_rhs=u**5+pi*g**4*u+2*pi**2*g**3*u**2+2*pi**3*g**2*u**3+pi**4*g*u**4
    assert s.rem(main_lhs-main_rhs,pi**5-5,pi)==0
    charts=[twotorsion_chart(0,4),nonbranch_chart(a*a-2,4),
            twotorsion_chart(1,2),twotorsion_chart(-1,2),
            nonbranch_chart(a**4+a*a+1,2)]
    assert sum(int(c['points']) for c in charts)==15
    assert sum(int(c['points'])*c['tail_genus'] for c in charts)==50
    assert 1+sum(int(c['points'])*c['tail_genus'] for c in charts)==51
    # Distinct centres, simple x-roots, and separation from the reduced branch support.
    critical=[x,x*x-2,x*x-1,x**4+x*x+1]
    for j,P in enumerate(critical):
        assert s.gcd(s.Poly(P,x,modulus=5),s.Poly(s.diff(P,x),x,modulus=5)).degree()==0
        assert s.gcd(s.Poly(P,x,modulus=5),s.Poly(g,x,modulus=5)).degree()==0
        for Q in critical[:j]:
            assert s.gcd(s.Poly(P,x,modulus=5),s.Poly(Q,x,modulus=5)).degree()==0
    assert s.Poly(psi-g**5,x,modulus=5).is_zero
    assert s.Poly((x**3-x)**2,x).nth(4)%5!=0
    # Valuations after the two kinds of exact substitutions.
    inequalities=[]
    for k in (2,4):
        lower=[Fraction(1)+Fraction(j-k,4*k) for j in range(1,k)]
        higher=[Fraction(j-k,4*k) for j in range(k+1,13)]
        assert all(v>0 for v in lower+higher)
        inequalities.append({'k':k,'lower_positive_bounds':list(map(str,lower)),
                             'higher_positive_bounds':list(map(str,higher)),
                             'different':4*(k+1),'genus':2*(k-1)})
    data={'status':'PASS','identity_h':str(h),'dh_mod5':str(factor),
          'exact_main_and_AS_binomial_identities':True,'tail_charts':charts,
          'tail_component_count':15,'tail_genus_sum':50,'main_genus':1,
          'proper_genus':51,'reduction_is_compact_type_by_genus_exhaustion':True,
          'all_centres_disjoint_from_reduced_E5':True,
          'ordinary_base_Cartier_coefficient':3,'cusp_clusters':5,
          'cusps_per_cluster':5,'valuation_checks':inequalities,
          'scope':'Exact finite algebra verifies formulas. Component persistence and all-prime fixed groups use the full written proof and A41--42.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2,default=int)+'\n')
    print('A58 exact wild-model certificate PASS')
    print('Exact main and Artin--Schreier binomial equations checked.')
    for c in charts:print(c)
    print('Positive genera: 1 + 5*6 + 10*2 = 51; fifteen distinct tail centres.')
    print('Every tail centre is disjoint from reduced E[5]; ordinary Cartier coefficient = 3 mod5.')
    print('Lower and higher coefficient valuations strictly exceed the retained scale.')


if __name__=='__main__':main()
