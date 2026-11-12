#!/usr/bin/env python3
"""Independent finite algebra checks for Part D and the 019/031 audits.

Run: python dg_checks.py
Dependencies: Python >=3.10 and SymPy.
These computations are sanity checks for the stated finite algebra. They do not
certify an infinite Galois representation, a lifting theorem, or an analytic proof.
"""
import json
from fractions import Fraction
from math import gcd
import sympy as s


def heisenberg_check(q):
    def mul(u, v):
        a, b, c = u
        aa, bb, cc = v
        return ((a + aa) % q, (b + bb) % q, (c + cc + a * bb) % q)

    def inv(u):
        a, b, c = u
        return (-a % q, -b % q, (-c + a * b) % q)

    def conj(v, u):
        return mul(mul(v, u), inv(v))

    count = 0
    for alpha in range(q):
        if gcd(alpha, q) != 1:
            continue
        for t in range(q):
            b = t * pow(alpha, -1, q) % q
            assert conj((0, b, 0), (alpha, 0, t)) == (alpha, 0, 0)
            count += 1
    roots = [r for r in range(q) if (r * r + 1) % q == 0]
    assert len(roots) == 2
    r = roots[0]
    J = s.Matrix([[0, -1], [1, 0]])
    M = s.Matrix([[r, -r], [1, 1]])
    assert gcd(int(M.det()), q) == 1
    assert all(int(x) % q == 0 for x in J * M - M * s.diag(r, -r))
    return {"modulus": q, "unit_exponent_central_terms_checked": count,
            "square_roots_of_minus_one": roots,
            "CM_eigenbasis_determinant_unit": True}


def tripod_rigidity():
    x, y, z = s.symbols("x y z")
    fs = [z, 1-z, 1/z, 1/(1-z), z/(z-1), (z-1)/z]
    ans = []
    for f in fs:
        defect = s.factor(f.subs(z, y-x) - f.subs(z, y) + f.subs(z, x))
        ans.append({"mobius": str(f), "difference_identity": defect == 0,
                    "defect": str(defect)})
    assert sum(a["difference_identity"] for a in ans) == 1
    return ans


def pfaffian_check():
    v = s.symbols("m0:16")
    M = s.Matrix(4, 4, v)
    J = s.diag(s.Matrix([[0, 1], [-1, 0]]), s.Matrix([[0, 1], [-1, 0]]))
    A = M * J * M.T
    pf = A[0, 1]*A[2, 3] - A[0, 2]*A[1, 3] + A[0, 3]*A[1, 2]
    assert s.expand(pf-M.det()) == 0
    return {"generic_matrix_size": 4, "identity_over_Z": True,
            "division_by_2_used": False}


def exponent_check():
    count = 0
    minimum = None
    for n in range(2, 51):
        m = n*(n-1)+1
        for r in range(1, n):
            margin = Fraction(n, r)-1-Fraction(n, m)
            assert margin > 0
            minimum = margin if minimum is None else min(minimum, margin)
            count += 1
    return {"n_range": [2, 50], "m": "n(n-1)+1", "cases": count,
            "minimum_margin_in_this_range": str(minimum),
            "larger_m_increases_margin": True}


def cyclic_multiplicity_check():
    X = s.symbols("X")
    count = 0
    for d in range(1, 31):
        phi = s.Poly(s.cyclotomic_poly(d, X), X, domain=s.QQ)
        for h in s.divisors(d):
            for j in range(d):
                f = s.Poly(sum(X**((j*(d//h)*k) % d) for k in range(h)), X, domain=s.QQ)
                expected = h if j % h == 0 else 0
                assert f.rem(phi).as_expr() == expected
                count += 1
    return {"cyclic_group_orders": [1, 30], "subgroup_character_cases": count,
            "multiplicity_per_orbit_at_most_one": True}


if __name__ == "__main__":
    output = {"heisenberg": [heisenberg_check(q) for q in (5, 25, 125)],
              "tripod_rigidity": tripod_rigidity(),
              "pfaffian": pfaffian_check(),
              "logarithm_rank_exponents": exponent_check(),
              "cyclic_character_multiplicity": cyclic_multiplicity_check()}
    print(json.dumps(output, indent=2))
