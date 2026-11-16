#!/usr/bin/env python3
"""Exact finite coefficient identities supporting the D.81 candidate.

The actual Fox multiplier and beta coefficients are used through degree three.
The group cohomology, annihilator calculation, and common finite-level argument
are proved in the written draft, not inferred from these computations.
"""
from pathlib import Path
from fractions import Fraction
import json
import sympy as sp

q, c, u, v = sp.symbols("q c u v")
MON = [(i, d-i) for d in range(4) for i in range(d+1)]
PRIMITIVE = [0, 2, 4, 0, 2, 1, 0, 0, 2, 0]
DIM = len(MON)


def choose(x, n):
    result = sp.Integer(1)
    for j in range(n):
        result = result*(x-j)/sp.Integer(j+1)
    return sp.expand(result)


def trunc(expr):
    poly = sp.Poly(sp.expand(expr), u, v)
    return sp.expand(sum(coef*u**i*v**j for (i, j), coef in poly.terms()
                         if i+j <= 3))


def functional(expr):
    poly = sp.Poly(sp.expand(expr), u, v)
    return sp.expand(sum(a*poly.coeff_monomial(u**i*v**j)
                         for a, (i, j) in zip(PRIMITIVE, MON)))


S_u = sum(choose(q, j+1)*u**j for j in range(4))
S_v = sum(choose(q, j+1)*v**j for j in range(4))
phi_u = sum(choose(q, j)*u**j for j in range(1, 4))
phi_v = sum(choose(q, j)*v**j for j in range(1, 4))
beta = (1+(q*q-1)*u*v/sp.Integer(24)
        +(c-(q*q-1))*(u*u*v+u*v*v)/sp.Integer(48))
multiplier = trunc(S_u*S_v*beta)
columns = [trunc(multiplier*trunc(phi_u**i*phi_v**j))
           for i, j in MON]

# Cartier action is q times inverse transpose.  The coboundary identity
# is equivalently q*m = rho^t(m+c*epsilon_00).
gb = sp.groebner([q**4-1], q, c, modulus=5)
symbolic = []
for index, ((i, j), column) in enumerate(zip(MON, columns)):
    residual = sp.expand(q*PRIMITIVE[index]-functional(column)
                         -c*q*q*(1 if (i, j) == (0, 0) else 0))
    numerator, denominator = sp.together(residual).as_numer_denom()
    assert denominator.is_Integer and int(denominator) % 5
    remainder = sp.expand(gb.reduce(sp.expand(numerator))[1])
    assert remainder == 0, ((i, j), residual, remainder)
    symbolic.append({"monomial": [i, j], "rational_residual": str(residual),
                     "denominator": int(denominator),
                     "remainder_mod_5_and_q4_minus_1": 0})


def mod5(x):
    x = Fraction(x)
    assert x.denominator % 5
    return x.numerator*pow(x.denominator, -1, 5) % 5


residual_cases = []
for chi in range(1, 5):
    for cv in range(5):
        matrix = [[mod5(sp.Poly(column.subs({q: chi, c: cv}), u, v)
                         .coeff_monomial(u**i*v**j))
                   for column in columns] for i, j in MON]
        right = [sum(matrix[j][i]*(PRIMITIVE[j]+(cv if j == 0 else 0))
                     for j in range(DIM)) % 5 for i in range(DIM)]
        left = [chi*x % 5 for x in PRIMITIVE]
        assert left == right
        residual_cases.append({"chi": chi, "c": cv, "common_primitive": True})

partition = []
for alpha in range(5):
    for bet in range(5):
        eps = int((alpha, bet) == (0, 0)
                  or alpha*bet*(alpha-bet) % 5 != 0)
        partition.append({"alpha": alpha, "beta": bet,
                          "epsilon": eps})
assert sum(row["epsilon"] for row in partition) == 13


def valuation(x, p=5):
    assert x
    count = 0
    while x % p == 0:
        x //= p
        count += 1
    return count


examples = []
for n in range(3, 33):
    A, B = 5, 5*(1+5**(n-3))
    depths = [valuation(A), valuation(B), valuation(A-B)]
    assert depths == [1, 1, n-2]
    assert sum(depths) == n
    examples.append({"free_rank": n, "A": str(A), "B": str(B),
                     "local_depths": depths, "finite_factor_order": 5})

assert all(sp.isprime(prime) for prime in [7, 31, 43])
unit_checks = {str(prime): pow(prime, 4, 25) for prime in [7, 31, 43]}
assert unit_checks == {"7": 1, "31": 21, "43": 1}
lambda31_mod5 = ((unit_checks["31"]-1)//5)*pow(4, -1, 5) % 5
assert lambda31_mod5 == 1

result = {
    "status": "PASS",
    "scope": "Exact actual degree-three Cartier identity and explicit parameter checks; continuous cohomology and the complete annihilator bound are proved in D.81.",
    "monomial_order": MON,
    "finite_cartier_dimension": DIM,
    "single_untwisted_primitive": PRIMITIVE,
    "symbolic_identity_ring": "F5[q,c]/(q^4-1)",
    "symbolic_monomial_checks": symbolic,
    "all_actual_residual_cases": residual_cases,
    "residual_partition": partition,
    "order_five_residual_vectors": 13,
    "zero_finite_factor_residual_vectors": 12,
    "explicit_finite_free_examples": examples,
    "prime_fourth_powers_mod25": unit_checks,
    "lambda31_mod5": lambda31_mod5,
    "global_inertia_determinant_at_7_43": 1,
    "zero_local_vector_has_countable_product": "Structural consequence in the written proof; no finite test substitutes for it.",
}

if __name__ == "__main__":
    Path(__file__).with_suffix(".json").write_text(
        json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))
