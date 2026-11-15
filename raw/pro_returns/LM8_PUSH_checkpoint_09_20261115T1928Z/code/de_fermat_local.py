#!/usr/bin/env python3
"""Exact certificates for the cusp-constant correction and Fermat proof.

No numerical approximation to q is used: q=j^{-1}+O(j^{-2}), so its
leading coefficient is exactly the leading coefficient of j^{-1}.
The local finite-flat and Galois arguments are proved in D.23.
"""
import json
from fractions import Fraction
from pathlib import Path
import sympy as s

z = s.symbols('z')
def j(lam):
    return 256 * (lam**2 - lam + 1)**3 / (lam**2 * (1-lam)**2)

leading = {}
for cusp, lam in [('zero',-z),('one',1+z),('infinity',-1/z)]:
    a = s.limit(1 / (j(lam) * z**2), z, 0)
    assert a == s.Rational(1,256)
    leading[cusp] = str(a)

X,Y,Z = s.symbols('X Y Z')
u = -3*Z/(X+Y)
v = (9*(X-Y)/(X+Y)-1)/2
identity = s.cancel((v*v+v-u**3+7)*(X+Y)**3)
assert s.expand(identity-27*(X**3+Y**3+Z**3)) == 0
uu,vv = s.symbols('u v')
weierstrass = s.expand((8*vv+4)**2-(4*uu)**3+432)
assert s.expand(weierstrass - 64*(vv*vv+vv-uu**3+7)) == 0

counts = {}
for p in (5,7):
    points = [(a,b) for a in range(p) for b in range(p)
              if (b*b+b-a**3+7)%p == 0]
    counts[str(p)] = {'affine': points, 'projective_count': len(points)+1}
assert counts['5']['projective_count'] == 6
assert counts['7']['projective_count'] == 9

def gamma0_genus(N):
    index = Fraction(N)
    for p in s.factorint(N):
        index *= Fraction(p+1,p)
    cusps = sum(int(s.totient(s.gcd(d,N//d))) for d in s.divisors(N))
    e2 = sum((x*x+1)%N == 0 for x in range(N))
    e3 = sum((x*x+x+1)%N == 0 for x in range(N))
    genus = 1 + index/12 - Fraction(e2,4)-Fraction(e3,3)-Fraction(cusps,2)
    assert genus.denominator == 1
    return {'level':N,'index':int(index),'cusps':cusps,'e2':e2,'e3':e3,'genus':int(genus)}

genera = [gamma0_genus(N) for N in (1,2,20,28,44,52,68,76,92)]
for row in genera:
    N=row['level']
    if N > 2:
        ell=N//4
        assert row['genus'] == (ell-3)//2
    else:
        assert row['genus'] == 0

out={
 'statements':['D.22','D.23'],
 'all_three_cusp_leading_constants':leading,
 'fermat_substitution':'z=t^n, hence q=(1/256)*t^(2n)*(1+O(t^n))',
 'v2_constant':-8,
 'odd_prime_residues':{str(ell):(-8)%ell for ell in (3,5,7,11)},
 'cubic_identity':str(s.factor(identity)),
 'weierstrass_identity':str(s.factor(weierstrass)),
 'point_counts':counts,
 'modular_genera':genera,
 'scope':'Exact algebra and finite counts; arithmetic proof, local conductor, and finite-flat arguments in D.tex.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
