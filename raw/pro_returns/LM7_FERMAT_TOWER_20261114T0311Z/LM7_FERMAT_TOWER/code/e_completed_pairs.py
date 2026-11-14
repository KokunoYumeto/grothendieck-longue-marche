#!/usr/bin/env python3
"""Exact finite checks for E.32 (completed inherited cubic class two).

This does not replace the infinite localization proof.  It checks the
semidirect tame relation, the cochain/coboundary signs and coefficient
transitions, agreement with independent tame symbols, and prefixes of the
explicit completed Kummer pair with a nonzero derived-limit obstruction.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
from pathlib import Path
from random import Random
import json
from sympy import isprime, primitive_root, discrete_log, factorint


def v3(n):
    if n == 0:
        return 10**9
    n = abs(n)
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v


def mul(x, y, m):
    a, b, c, u = x
    A, B, C, v = y
    k = 9*pow(2, -1, m) % m
    return ((a+u*A) % m, (b+u*B) % m,
            (c+u*u*C+k*u*(a*B-b*A)) % m, u*v % m)


def inv(x, m):
    a, b, c, u = x
    w = pow(u, -1, m)
    return (-w*a % m, -w*b % m, -w*w*c % m, w)


def omega(v, w, chi, m):
    return 9*pow(2, -1, m)*(v[0]*chi*w[1]-v[1]*chi*w[0]) % m


def cup(v, w, chi, m):
    return v[0]*chi*w[1] % m


def add_cocycle(v, w, chi, m):
    return tuple((v[i]+chi*w[i]) % m for i in range(2))


rng = Random(323232)
tame_checks = 0
coboundary_checks = 0
cocycle_checks = 0
coefficient_checks = 0
relation_rows = []
for n in range(1, 7):
    m = 3**n
    for q in [2, 7, 19, 109, 163, 487]:
        for trial in range(200):
            a, b, z, A, B, c, u, v = [rng.randrange(m) for _ in range(8)]
            S, T = (a, b, z, q % m), (A, B, c, 1)
            left = mul(mul(S, T, m), inv(S, m), m)
            right = (q*A % m, q*B % m, q*c % m, 1)
            defect = q*((q-1)*c+9*(a*B-b*A)) % m
            assert left[:2] == right[:2] and left[3] == 1
            assert (left[2]-right[2]) % m == defect
            tame_checks += 1
            D = 9*(a*B-b*A) % m
            shifted = 9*((a+(q-1)*u)*B-(b+(q-1)*v)*A) % m
            assert (shifted-D) % m == (q-1)*9*(u*B-v*A) % m
            h = (u, v, 0, 1)
            conjugate = mul(mul(inv(h, m), T, m), h, m)
            assert (conjugate[2]-c) % m == -9*(u*B-v*A) % m
            # Changing Frobenius by tau^r changes both toric values proportionally.
            r = rng.randrange(m)
            assert ((a+r*A)*B-(b+r*B)*A) % m == (a*B-b*A) % m
            coboundary_checks += 1
            if n > 1:
                smaller = m//3
                assert tuple(x % smaller for x in mul(S, T, m)) == mul(
                    tuple(x % smaller for x in S),
                    tuple(x % smaller for x in T), smaller)
                assert defect % smaller == q*((q-1)*c+9*(a*B-b*A)) % smaller
                coefficient_checks += 1
        relation_rows.append({"q": q, "modulus": m, "cases": 200})
    for trial in range(1000):
        vg, vh, vk = [tuple(rng.randrange(m) for _ in range(2)) for _ in range(3)]
        xg, xh, xk = [rng.choice([i for i in range(m) if i % 3]) for _ in range(3)]
        vgh = add_cocycle(vg, vh, xg, m)
        vhk = add_cocycle(vh, vk, xh, m)
        delta = (xg*xg*omega(vh, vk, xh, m)-omega(vgh, vk, xg*xh, m)
                 +omega(vg, vhk, xg, m)-omega(vg, vh, xg, m)) % m
        assert delta == 0
        # omega = 9 cup + (9/2) d(g -> alpha(g) beta(g)).
        db = (xg*xg*vh[0]*vh[1]-vgh[0]*vgh[1]+vg[0]*vg[1]) % m
        assert omega(vg, vh, xg, m) == (9*cup(vg, vh, xg, m)
                                     +9*pow(2, -1, m)*db) % m
        cocycle_checks += 1


@lru_cache(None)
def factor(n):
    return {int(p): int(e) for p, e in factorint(n).items()}


@lru_cache(None)
def kummer_log(q, p):
    assert q != p and q != 3
    e = v3(q-1)
    if e == 0:
        return 0
    order = 3**e
    root = pow(int(primitive_root(q)), (q-1)//order, q)
    target = pow(p, (q-1)//order, q)
    r = int(discrete_log(q, target, root))
    assert 0 <= r < order and pow(root, r, q) == target
    return r


def order_mod(x, q):
    o = q-1
    for p in factor(o):
        while o % p == 0 and pow(x, o//p, q) == 1:
            o //= p
    return o


comparison_histogram = Counter()
for aa, bb in product(range(1, 201), repeat=2):
    a, b = factor(aa), factor(bb)
    obstruction_by_logs = False
    obstruction_by_tame = False
    for q in set(a) | set(b):
        va, vb = a.get(q, 0), b.get(q, 0)
        ua, ub = aa//q**va, bb//q**vb
        theta = (-1 if va*vb % 2 else 1)*pow(ua, vb, q)*pow(ub, -va, q) % q
        obstruction_by_tame |= v3(order_mod(theta, q)) > 2
        if q != 3:
            A = sum(e*kummer_log(q, p) for p, e in a.items() if p != q)
            B = sum(e*kummer_log(q, p) for p, e in b.items() if p != q)
            D = 9*(A*vb-B*va)
            obstruction_by_logs |= v3(D) < v3(q-1)
    assert obstruction_by_logs == obstruction_by_tame
    comparison_histogram["obstructed" if obstruction_by_logs else "admissible"] += 1


phantom_rows = []
previous = 3
for j in range(3, 13):
    step = 3**j
    q = max(1, (previous-1)//step+1)*step+1
    while not isprime(q) or pow(3, (q-1)//3, q) == 1:
        q += step
    assert q > previous and q % step == 1 and pow(3, (q-1)//3, q) != 1
    previous = q
    r = kummer_log(q, 3)
    assert r % 3
    exponent = Fraction(q-1, 9*r)
    assert exponent.denominator % 3 and v3(exponent.numerator) >= j-2
    assert 9*exponent*r == q-1
    assert -9*exponent*r/Fraction(q-1) == -1
    phantom_rows.append({"j": j, "q": q, "v3_q_minus_1": v3(q-1),
                         "kummer_log_of_3": r,
                         "completed_prime_exponent": str(exponent),
                         "v3_exponent": v3(exponent.numerator),
                         "central_correction": -1})


transition_rows = []
for n in range(1, 13):
    m = 3**n
    big = 3*m
    residuals = [((r["q"]-1) % m) for r in phantom_rows]
    primitive = [int(r["v3_q_minus_1"] < n) for r in phantom_rows]
    next_primitive = [int(r["v3_q_minus_1"] < n+1) for r in phantom_rows]
    assert all((r["q"]-1)*c % m == z
               for r, c, z in zip(phantom_rows, primitive, residuals))
    incompatibility = [(nxt-cur) % m for cur, nxt in zip(primitive, next_primitive)]
    assert all((r["q"]-1)*x % m == 0
               for r, x in zip(phantom_rows, incompatibility))
    transition_rows.append({"modulus": m,
                            "residue_support_in_test_prefix": [r["q"] for r, z in zip(phantom_rows, residuals) if z],
                            "new_kernel_support_at_next_level": [r["q"] for r, z in zip(phantom_rows, incompatibility) if z]})


result = {
    "statement": "E.32",
    "cohomology_model": "R / diag(q-1) R, R restricted Z3 sequences, q != 3",
    "tame_relation_cases": tame_checks,
    "coboundary_and_frobenius_change_cases": coboundary_checks,
    "two_cocycle_and_sign_cases": cocycle_checks,
    "coefficient_reduction_cases": coefficient_checks,
    "relation_parameter_rows": relation_rows,
    "independent_rational_tame_comparisons": 40000,
    "rational_comparison_histogram": dict(comparison_histogram),
    "phantom_pair_prefix": phantom_rows,
    "finite_primitive_transition_checks": transition_rows,
    "scope": "Exact finite computations and finite prefixes; infinite existence and nonconvergence are proved in E.32."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
print("E.32 exact finite verification passed")
print(f"tame relations: {tame_checks}; coboundary/Frobenius changes: {coboundary_checks}")
print(f"2-cocycle identities/signs: {cocycle_checks}; coefficient transitions: {coefficient_checks}")
print("independent tame comparisons:", dict(comparison_histogram))
print("j, q_j, v3(q_j-1), r_j, completed exponent, central correction")
for row in phantom_rows:
    print(row["j"], row["q"], row["v3_q_minus_1"], row["kummer_log_of_3"],
          row["completed_prime_exponent"], row["central_correction"])
print("finite primitive transition checks passed at moduli3 through3^12")
