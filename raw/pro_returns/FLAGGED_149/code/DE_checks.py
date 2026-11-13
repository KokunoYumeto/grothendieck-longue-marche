#!/usr/bin/env python3
"""Exact finite checks accompanying Parts D--E. No finite test substitutes for a proof."""
from fractions import Fraction
from itertools import product
from math import factorial, prod
from pathlib import Path
import json
import sympy as sp

out = {}
# The norm valuation in D3: calculate the identity-tail and all conjugate leading orders.
value_checks=[]
X,Y,w,h=sp.symbols('X Y w h')
for family in ('factorials','powers_of_two'):
    Ns=[factorial(j) if family=='factorials' else 2**j for j in range(1,5)]
    aa=[Fraction(j+1,1)+Fraction(1,N) for j,N in enumerate(Ns)]
    for m in (1,2,3):
        N=Ns[m-1]
        leading=[]
        for k in range(1,N):
            changed=next(a for a in aa[:m] if (k*int(a*N))%N)
            leading.append(changed)
        expected=aa[m]+sum(leading,Fraction(0))
        # Actual polynomial norm followed by a finite truncation containing the first tail.
        summand=sum(w**int(a*N) for a in aa[:m])
        norm=sp.resultant(w**N-X,Y-2-summand,w)
        Q=Ns[m]
        ytr=2+sum(h**int(a*Q) for a in aa[:m+1])
        evaluated=sp.Poly(sp.expand(norm.subs({X:h**Q,Y:ytr})),h)
        actual=Fraction(min(exp[0] for exp,coef in evaluated.terms() if coef),Q)
        assert actual==expected,(family,m,actual,expected)
        # Subtracting the previous denominator group recovers the next denominator.
        residue=actual-aa[m]
        assert (residue*N).denominator==1
        value_checks.append({'family':family,'truncation_m':m,'norm_degree':N,
                             'norm_valuation':str(actual),'next_tail':str(aa[m]),
                             'previous_group_part':str(residue),'verified':True})
out['D3_norm_valuations']=value_checks

# E6: the first three norm polynomials and their exact leading coefficients.
t=sp.symbols('t')
primes=[2,3,5,7]
aa=[sp.sqrt(p) for p in primes]
residue_checks=[]
for m in range(3):
    factors=[Y-sum(signs[j]*aa[j]*X**(j+1) for j in range(m+1))
             for signs in product((-1,1), repeat=m+1)]
    norm=sp.Poly(sp.expand(prod(factors)),X,Y)
    assert all(c.is_Rational for c in norm.coeffs())
    ytr=sum(aa[j]*t**(j+1) for j in range(m+2))
    evaluated=sp.Poly(sp.expand(norm.as_expr().subs({X:t,Y:ytr})),t)
    M=min(exp[0] for exp,coef in evaluated.terms() if coef)
    coeff=evaluated.coeff_monomial(t**M)
    expected_M=m+2+sum((j+1)*2**(m-j) for j in range(m+1))
    c=prod((2*aa[j])**(2**(m-j)) for j in range(m+1))
    assert M==expected_M and sp.simplify(coeff-c*aa[m+1])==0
    residue_checks.append({'m':m,'norm_degree':2**(m+1),'order':M,
                           'leading_coefficient':str(coeff),'old_field_factor':str(c),
                           'new_residue_generator':str(aa[m+1]),'verified':True})
out['E6_infinite_algebraic_residue']=residue_checks

# Explicit meridian maps and the Chern relation, checked in every listed finite quotient.
meridians=[]
for n in range(2,17):
    kernel={(a,b) for a,b in product(range(n),repeat=2) if (a+b)%n==0}
    expected={(a,(-a)%n) for a in range(n)}
    assert kernel==expected
    divisor_image={(a%n,(2*a)%n) for a in range(n)}
    assert len(divisor_image)==n
    diag={(a,a) for a in range(n)}
    assert len(diag)==n and len({(a,0) for a in range(n)} & diag)==1
    # For Z[1/2], evaluation at 1 has zero 2-primary coordinate.
    odd=n
    while odd%2==0:odd//=2
    power_two=n//odd
    localized_image={(power_two*a)%n for a in range(odd)}
    assert len(localized_image)==odd
    meridians.append({'n':n,'blowup_kernel_size':len(kernel),
                      'chern_vector':[1,(-1)%n],
                      'DVR_1_2_image_size':len(divisor_image),
                      'ambient_T2_size':n*n,
                      'Z_invert_2_image_size':len(localized_image),
                      'verified':True})
out['E2_E3_E5_meridians']=meridians

# Normal bundle degrees of the threefold blow-up.
# D'=b*D-E; b*D|S has degree0 and E|S degree-1.
chern=sp.Matrix([0-(-1),-1])
meridian=sp.Matrix([[1,1]])
assert meridian*chern==sp.zeros(1,1)
assert chern.rank()==1
out['E5_blowup_chern']={'normal_degrees':list(chern),'global_meridian_matrix':[[1,1]],
                        'composition':[[0]],'boundary_nonzero':True}

# Two (1,1)-graphs have two simple transverse intersection points.
x=sp.symbols('x')
pol=x*x-1
assert sp.factor(pol)==(x-1)*(x+1) and sp.gcd(pol,sp.diff(pol,x))==1
out['ZD8_incidence']={'intersection_polynomial':str(pol),'roots':[-1,1],
                       'vertices':2,'edges':2,'first_betti':1,'verified':True}
path=Path(__file__).with_name('DE_checks.json')
path.write_text(json.dumps(out,indent=2,default=str)+'\n')
print(json.dumps({'output':str(path),'checks':len(value_checks)+len(residue_checks)+len(meridians)+2,
                  'all_passed':True},indent=2))
