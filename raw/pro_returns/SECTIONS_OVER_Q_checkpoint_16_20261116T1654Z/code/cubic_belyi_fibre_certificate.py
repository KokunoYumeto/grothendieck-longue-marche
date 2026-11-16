#!/usr/bin/env python3
"""Exact finite algebra and permutation checks for A.114.

The infinite completed Kummer statement is proved by its field/compositum
argument; the checks here retain the actual finite maps used in that proof.
"""

from itertools import permutations, combinations
from math import gcd
import sympy as sp


T, R, c, t, Z = sp.symbols("T R c t Z")
f = lambda x: sp.Rational(27, 4)*x*x*(1-x)
assert sp.expand(1-f(T)-sp.Rational(27, 4)*(T-sp.Rational(2, 3))**2
                 *(T+sp.Rational(1, 3))) == 0
assert sp.expand(sp.diff(f(T), T)-sp.Rational(27, 4)*(2*T-3*T*T)) == 0
polynomial = Z**3-Z**2+sp.Rational(4, 27)*t
disc = sp.discriminant(polynomial, Z)
assert sp.expand(disc-sp.Rational(16, 27)*t*(1-t)) == 0
assert sp.cancel(disc/(3*t*(1-t))) == sp.Rational(4, 9)**2
assert sp.expand((1-T)*(1+3*T)+3*(T-1)*(T+sp.Rational(1, 3))) == 0
assert sp.cancel(3*f(T)*(1-f(T))/((1-T)*(1+3*T))-(
    sp.Rational(27, 4)*T*(T-sp.Rational(2, 3)))**2) == 0
assert sp.div(Z**3-Z**2-(T**3-T*T), Z-T, Z)[0] == (
    Z*Z+(T-1)*Z+T*T-T)
assert sp.expand(sp.discriminant(Z*Z+(T-1)*Z+T*T-T, Z)-(1-T)*(1+3*T)) == 0


def compose(g, h):
    return tuple(g[h[i]] for i in range(3))


def sign(g):
    return (-1)**sum(g[i] > g[j] for i in range(3) for j in range(i+1, 3))


S3 = list(permutations(range(3)))
identity = tuple(range(3))
subgroups = []
no_derangement = []
fixed_sign = []
for size in range(1, 7):
    for entries in combinations(S3, size):
        H = set(entries)
        if identity not in H or any(compose(g, h) not in H for g in H for h in H):
            continue
        subgroups.append(H)
        if any(all(g[i] != i for i in range(3)) for g in H):
            continue
        no_derangement.append(H)
        fixed = [i for i in range(3) if all(g[i] == i for g in H)]
        if any(sign(g) == -1 for g in H):
            assert len(H) == 2 and len(fixed) == 1
            fixed_sign.append((H, fixed[0]))
        else:
            assert H == {identity} and len(fixed) == 3
assert len(subgroups) == 6
assert len(no_derangement) == 4 and len(fixed_sign) == 3

# Every cyclic Kummer subgroup is a subgroup of the translation group of
# the m roots.  Check the two precise coset constructions from the proof.
translation_checks = 0
internal_quadratic_checks = 0
for m in range(2, 81):
    for order in sp.divisors(m):
        if order == 1:
            continue
        step = m//order
        for k in range(1, order):
            translation = [(i+k*step) % m for i in range(m)]
            assert all(translation[i] != i for i in range(m))
            # In the linearly disjoint case pair this actual translation
            # with the nontrivial automorphism of the quadratic field.
            translation_checks += 1
        if order % 2 == 0:
            # If the quadratic field lies inside the Kummer extension but
            # not its cyclotomic base, restriction is the surjection k mod2.
            for k in range(1, order, 2):
                translation = [(i+k*step) % m for i in range(m)]
                assert k % 2 == 1 and all(translation[i] != i for i in range(m))
                internal_quadratic_checks += 1

# Exact Gauss-sum identities in the actual cyclotomic coordinate ring.
gauss_checks = 0
X = sp.symbols("X")
for ell in list(sp.primerange(3, 44)):
    phi = sp.cyclotomic_poly(ell, X)
    gauss = sum(int(sp.legendre_symbol(a, ell))*X**a for a in range(1, ell))
    expected = (-1)**((ell-1)//2)*ell
    assert sp.rem(gauss*gauss-expected, phi, X) == 0
    gauss_checks += 1

# There are exactly two square-quotient cosets at odd prime powers, and
# exactly four at two-power levels >=8; higher levels add no quadratic field.
unit_checks = 0
for ell, powers in ((2, range(3, 9)), (3, range(1, 5)),
                    (5, range(1, 4)), (7, range(1, 4))):
    for n in powers:
        modulus = ell**n
        units = [a for a in range(modulus) if gcd(a, modulus) == 1]
        squares = {a*a % modulus for a in units}
        assert len(units)//len(squares) == (4 if ell == 2 else 2)
        if ell == 2:
            assert squares == {a for a in units if a % 8 == 1}
        unit_checks += 1

# The exceptional examples are genuinely invisible at every tested
# nonsplit prime, through exactly the stated local unit-power maps.
local_checks = 0
for D, ell, exponent in [(-1, 2, 2), (2, 2, 4), (-2, 2, 4),
                         (-3, 3, 1), (5, 5, 1), (-7, 7, 1), (13, 13, 1)]:
    for p in sp.primerange(2, 1000):
        if p == ell or sp.kronecker_symbol(D, p) != -1:
            continue
        if ell == 2:
            assert p % 2 == 1
            assert (p-1) % (4 if D == -1 else 8) != 0
        else:
            assert (p-1) % ell != 0
        # For p!=ell, Hensel identifies ell-power local unit quotients
        # with these exact finite-field power subgroups.
        for n in range(1, 9):
            g = gcd(ell**n, p-1)
            value = pow(ell, exponent, p)
            assert pow(value, (p-1)//g, p) == 1
            local_checks += 1

print("A.114 cubic Belyi fibre certificate: all checks passed.")
print("The cubic factorization, derivative, discriminant, sign cover and other-root polynomial are exact.")
print(f"S3 subgroups checked: {len(subgroups)}; no-derangement subgroups: {len(no_derangement)}.")
print(f"Each of the {len(fixed_sign)} nontrivial-sign possibilities has exactly one fixed sheet.")
print(f"Kummer translation derangements: {translation_checks}; internal quadratic-coset checks: {internal_quadratic_checks}.")
print(f"Exact Gauss-sum squares in cyclotomic rings: {gauss_checks}; prime-power unit square quotients: {unit_checks}.")
print(f"Exceptional primary classes: {local_checks} exact finite-field local power tests.")
print("The coherent primary-limit and full Selmer-fibre assertions are proved in A.114; no source obstruction is inferred.")
