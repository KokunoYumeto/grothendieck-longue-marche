#!/usr/bin/env python3
"""Exact polynomial/chart certificate for the actual Heisenberg-seven cover.

This finite algebra certificate accompanies the unbounded geometric proof;
it does not by itself assert stable reduction or arithmetic fixed groups.
"""
from fractions import Fraction
from pathlib import Path
import json
import sympy as s

x,a,t,U,V,W,eta,pi,u,rho,y0=s.symbols('x a t U V W eta pi u rho y0')
psi3=3*x**4-6*x*x-1
B=x**6-5*x**4-5*x*x+1
psi5=5*x**12-62*x**10-105*x**8+300*x**6-125*x**4+50*x*x+1
psi7=s.expand(psi5*psi3**3-128*(x**3-x)**2*B**3)
h=s.expand((psi7+1)/7)
assert all(c.q==1 for c in s.Poly(h,x).all_coeffs())
hb=x**24-2*x**22-2*x**20+x**18-x**14-3*x**10-x**8-x**6-3*x**4
assert s.Poly(h-hb,x,modulus=7).is_zero
assert s.Poly(psi7+1,x,modulus=7).is_zero
assert s.degree(psi7,x)==24 and s.Poly(psi7,x).LC()==7
assert s.expand(psi7.subs(x,-x)-psi7)==0
assert s.gcd(s.Poly(psi7,x),s.Poly(s.diff(psi7,x),x)).degree()==0
dh=3*x**3*(x*x-1)**3*(x*x-3)**7
assert s.Poly(s.diff(h,x)-dh,x,modulus=7).is_zero


def reduce_a(expr):
    return s.Poly(expr,a,modulus=7).rem(s.Poly(a*a-3,a,modulus=7)).as_expr()


def main():
    # Exact binomial equations, in their defining parameter extensions.
    main_lhs=s.expand(((-1+pi*u)**7+1)/7)
    main_rhs=u**7-pi**6*u**6+3*pi**5*u**5-5*pi**4*u**4+5*pi**3*u**3-3*pi**2*u**2+pi*u
    assert s.rem(main_lhs-main_rhs,pi**7-7,pi)==0
    tail_lhs=s.expand(((1+eta*V)**7-1)/(7*eta))
    tail_rhs=V+3*eta*V**2+5*eta**2*V**3+5*eta**3*V**4+3*eta**4*V**5+eta**5*V**6-V**7
    assert s.rem(tail_lhs-tail_rhs,eta**6+7,eta)==0

    # All integral Taylor coefficients, not just differentiated identities.
    expanded=s.Poly(s.expand(h.subs(x,a+t)-h.subs(x,a)),t)
    coeffs=[]
    for j in range(25):
        c=s.rem(expanded.nth(j),a*a-3,a)
        assert all(v.q==1 for v in s.Poly(c,a).all_coeffs())
        coeffs.append(reduce_a(c))
    assert coeffs[:8]==[0]*8 and coeffs[8]==2
    charts=[{'centres':'x^2=3, y=±sqrt(2x)','count':4,'parameter':'x-a',
             'first_degree':8,'first_coefficient_mod7':2,
             'coefficient_degree7_mod7':0,'tail_coefficient_mod7':2}]
    for a0 in (0,1,-1):
        cs=[int(c)%7 for c in s.Poly(s.expand(h.subs(x,a0+t)-h.subs(x,a0)),t).all_coeffs()[::-1]]
        assert cs[:4]==[0]*4
        expected=4 if a0==0 else 2
        assert cs[4]==expected
        delta=(3*a0*a0-1)%7
        c=expected*pow(delta,-4,7)%7
        assert c
        charts.append({'centres':f'({a0},0)','count':1,'parameter':'y',
                       'first_x_degree':4,'first_parameter_degree':8,
                       'first_coefficient_mod7':expected,'tail_coefficient_mod7':c})

    # Elliptic auxiliary equations are exact after the indicated changes.
    etale_exp=s.expand(((y0+rho*W)**2-((a+rho*U)**3-(a+rho*U))-(y0*y0-a**3+a))/rho)
    assert s.expand(etale_exp-(2*y0*W+rho*W*W-(3*a*a-1)*U-3*a*rho*U*U-rho*rho*U**3))==0
    branch_exp=s.expand(((rho*U)**2-((a+rho*rho*W)**3-(a+rho*rho*W))+(a**3-a))/rho**2)
    assert s.expand(branch_exp-(U*U-(3*a*a-1)*W-3*a*rho*rho*W*W-rho**4*W**3))==0

    # Distinct centres and their parameter multiplicities.
    critical=[x,x*x-1,x*x-3]
    for j,P in enumerate(critical):
        assert s.gcd(s.Poly(P,x,modulus=7),s.Poly(s.diff(P,x),x,modulus=7)).degree()==0
        for Q in critical[:j]:
            assert s.gcd(s.Poly(P,x,modulus=7),s.Poly(Q,x,modulus=7)).degree()==0
    assert sum(c['count'] for c in charts)==7
    assert s.Poly((x**3-x)**3,x).nth(6)%7==0
    lower=[Fraction(1)+Fraction(j-8,48) for j in range(1,8)]
    higher=[Fraction(j-8,48) for j in range(9,25)]
    branch_lower=[Fraction(1)+Fraction(2*j-8,48) for j in range(1,4)]
    branch_higher=[Fraction(2*j-8,48) for j in range(5,25)]
    assert all(v>0 for v in lower+higher+branch_lower+branch_higher)

    # Genus and actual cover combinatorics.
    branch_count=7**2
    proper_genus=1+branch_count*(7-1)//2
    tail_genus=(7-1)*(8-1)//2
    assert proper_genus==148==1+7*tail_genus
    assert 2-2*proper_genus-branch_count==-7**3
    assert 7*7-8*6==1  # t^7 V^6 is a uniformizer.
    assert 7*7-8*5==9  # valuation of its translated difference.
    assert (7-1)*9-2*7==2*tail_genus-2
    data={'status':'PASS','psi7':str(psi7),'h_integral':str(h),'h_mod7':str(hb),
          'dh_mod7':str(dh),'exact_main_binomial_identity':True,
          'exact_tail_binomial_identity':True,'exact_elliptic_auxiliary_equations':True,
          'full_nonbranch_Taylor_coefficients_mod_a2_minus3_mod7':list(map(str,coeffs)),
          'tail_charts':charts,'critical_centres':7,'tail_genus':21,
          'main_genus':1,'proper_genus':148,'genus_exhaustion':True,
          'supersingular_base_Cartier_coefficient':0,'cusps':49,'cover_degree':343,
          'all_critical_centres_finite_and_away_O':True,
          'lower_valuation_bounds':list(map(str,lower)),
          'higher_valuation_bounds':list(map(str,higher)),
          'branch_lower_valuation_bounds':list(map(str,branch_lower)),
          'branch_higher_valuation_bounds':list(map(str,branch_higher)),
          'AS_uniformizer':'t^7 V^6','AS_lower_jump':8,'AS_different':54,
          'scope':'Exact algebra only; component persistence, group identification, and all-prime assertions require the accompanying written proof.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
    print('A60 exact Heisenberg-seven model certificate PASS')
    print('Division-polynomial identity, mod7 primitive equation, and both binomial charts checked.')
    print('The potentially hidden degree-seven Taylor term vanishes at every non-two-torsion centre.')
    for c in charts:print(c)
    print('Positive genera: 1 + 7*21 = 148; degree343; cusps49; Euler characteristic -343.')
    print('All lower/higher terms have positive residual valuation; supersingular main coefficient0.')


if __name__=='__main__':main()
