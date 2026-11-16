#!/usr/bin/env python3
"""Exact finite identities for A.202; the Chebotarev recursion is proved in text.

No external services and no simulated large-prime search are used.  Integer
samples certify stated finite identities alongside the general proofs of LTE,
the closed subgroup limit, and the actual finite-cover comparison.
"""
from fractions import Fraction
from math import factorial
from pathlib import Path
import json
import sympy as sp


def v2(n):
    if isinstance(n, Fraction):
        return v2(n.numerator) - v2(n.denominator)
    n = abs(int(n))
    assert n
    return (n & -n).bit_length() - 1


first_depth_cases = later_depth_cases = partial_product_cases = 0
for multiplier in range(1, 17):
    N0 = 24 * multiplier
    n0, n1, n2 = (N0 * factorial(j + 4) for j in range(3))
    # This numerical lower bound is the dyadic part of A.72.13.  The
    # separate cover-continuation precision can only increase L.
    base = max(2, v2(n1), 1 + 2*v2(n2) + 4)
    for extra in range(8):
        L = base + extra
        E = L + v2(n0)
        assert E >= 6
        modulus = 1 << (E + 2)
        for odd in (1, 3, 5, 7, 15, 31):
            q0 = 1 + (1 << L) * odd
            assert q0 % (1 << (L+1)) == 1 + (1 << L)
            assert q0 % (1 << v2(n1)) == 1
            first = (pow(q0, n0, modulus)-1) % modulus
            assert v2(first) == E
            first_depth_cases += 1
            a1 = 3 * pow(q0, n0, modulus) % modulus
            running = a1
            for j in range(1, 13):
                n = N0*factorial(j+4)
                following = N0*factorial(j+6)
                Lj = max(2, E+1-v2(n), 1+2*v2(following)+j+4)
                # Every original precision condition may be increased.
                assert Lj + v2(n) >= E+1
                assert Lj-1 > 2*v2(N0*factorial(j+5))
                qj = 1 + (1 << Lj)*(2*j+1)
                factor = pow(qj, n, modulus)
                assert factor % (1 << (E+1)) == 1
                running = running*factor % modulus
                assert v2((running-3) % modulus) == E
                later_depth_cases += 1
                partial_product_cases += 1

x, z, t = sp.symbols('x z t')
tf = x**4/(x**4-54)
factor = -2*(x-3)*(x+3)*(x*x+9)/(x**4-54)
assert sp.cancel(tf-3-factor) == 0
assert sp.cancel(x**4-54*tf/(tf-1)) == 0
xi, yi = -6*z*z/(1-t), -18*z/(1-t)
assert sp.cancel(xi.subs(z,-z)-xi) == 0
assert sp.cancel(yi.subs(z,-z)+yi) == 0
cover_relation = sp.together(yi**2-xi**5+54*xi)
assert sp.rem(sp.fraction(cover_relation)[0],
              24*z**8+t*(1-t)**3,z) == 0

sheet_depth_cases = finite_detector_cases = 0
for e in range(3, 22):
    for odd in range(-127, 128, 2):
        xx = 3 + (1 << e)*odd
        assert xx % 8 == 3 and (xx**5-54*xx) % 8 == 1
        tt = Fraction(xx**4, xx**4-54)
        assert v2(xx+3) == 1 and v2(xx*xx+9) == 1
        assert v2(xx**4-54) == 0
        E = e+3
        assert v2(tt-3) == E
        # A.193's exact finite condition is n <= e.  The indicated
        # later quotient chooses the first integer failing that test.
        n = E-2
        assert n == e+1 and n > e
        assert 4*n+3 == 4*E-5 and 4*n == 4*E-8
        sheet_depth_cases += 1
        finite_detector_cases += 1

data = dict(
    first_depth_cases=first_depth_cases,
    later_depth_cases=later_depth_cases,
    partial_product_cases=partial_product_cases,
    sheet_depth_cases=sheet_depth_cases,
    finite_detector_cases=finite_detector_cases,
    exact_map="t=x^4/(x^4-54)",
    exact_depth="v2(t-3)=v2(x-3)+3",
    detector="n=E-2, order=2^(4E-5), class=4E-8",
    execution_scope="Finite identities and precision checks; no prime recursion executed."
)
lines = [
    "A.202 exact finite certificate: PASS",
    f"First-prime exact-depth cases: {first_depth_cases}",
    f"Later precision/partial-product cases: {later_depth_cases}/{partial_product_cases}",
    "Literal cover/factorization/deck identities: PASS",
    f"All-sheet depth and detector-index cases: {sheet_depth_cases}/{finite_detector_cases}",
    "The general prime recursion, infinite limit, and local section comparison are proved in the source.",
    "No large first prime search was executed or simulated."
]
base = Path(__file__).with_suffix("")
base.with_name(base.name+"_data.json").write_text(json.dumps(data,indent=2)+"\n")
output = "\n".join(lines)+"\n"
base.with_name(base.name+"_output.txt").write_text(output)
print(output,end="")
