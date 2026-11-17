#!/usr/bin/env python3
"""Exact finite matrix checks for the full harmonic-character formula.

The enumerated group is the actual matrix normalizer of the signed
harmonic matrix.  No assertion that every matrix is attained by GT0
is used or made.  The source-frame realization is proved separately.
"""
from pathlib import Path
from itertools import product
import json


def mul(a, b, p):
    return ((a[0]*b[0]+a[1]*b[2]) % p,
            (a[0]*b[1]+a[1]*b[3]) % p,
            (a[2]*b[0]+a[3]*b[2]) % p,
            (a[2]*b[1]+a[3]*b[3]) % p)


def det(a, p):
    return (a[0]*a[3]-a[1]*a[2]) % p


def scale(a, t, p):
    return tuple(t*v % p for v in a)


def inv(a, p):
    return scale((a[3], -a[1], -a[2], a[0]),
                 pow(det(a, p), -1, p), p)


def power(a, n, p):
    value = (1, 0, 0, 1)
    while n:
        if n & 1:
            value = mul(value, a, p)
        a = mul(a, a, p)
        n >>= 1
    return value


def legendre_bit(a, p):
    value = pow(a % p, (p-1)//2, p)
    assert value in (1, p-1)
    return int(value == p-1)


results = []
for p in (3, 5, 7, 11, 13, 17, 19, 29, 37):
    identity = (1, 0, 0, 1)
    minus_identity = (p-1, 0, 0, p-1)
    s = (0, p-1, 1, 0)
    j = (p-1, 0, 0, 1)
    n = p - (1 if p % 4 == 1 else -1)
    cartan = [(a, -b % p, b, a)
              for a, b in product(range(p), repeat=2)
              if (a*a+b*b) % p]
    torus = [z for z in cartan if det(z, p) == 1]
    assert len(torus) == n and n % 4 == 0

    def epsilon(t):
        assert t in torus_set
        value = power(t, n//2, p)
        assert value in (identity, minus_identity)
        return int(value == minus_identity)

    torus_set = set(torus)
    eps = {t: epsilon(t) for t in torus}
    assert eps[minus_identity] == 0
    normalizer = []
    for z in cartan:
        d = det(z, p)
        c = scale(mul(z, z, p), pow(d, -1, p), p)
        assert c in torus_set
        assert eps[c] == legendre_bit(d, p)
        assert mul(z, mul(j, mul(inv(z, p), j, p), p), p) == c
        for e in (0, 1):
            m = z if e == 0 else mul(z, j, p)
            assert mul(m, mul(s, inv(m, p), p), p) == scale(s, (-1)**e, p)
            lam = det(m, p)
            q = legendre_bit(lam, p) ^ (e & legendre_bit(-1, p))
            assert q == eps[c]
            arithmetic_target = mul(j, mul(m, j, p), p)
            difference = mul(m, inv(arithmetic_target, p), p)
            assert difference == c
            assert eps[difference] ^ q == 0
            assert eps[identity] ^ q == q
            normalizer.append((m, e, q))
    assert len({m for m, _, _ in normalizer}) == 2*len(cartan)
    for m, e, q in normalizer:
        for t in torus:
            mt = mul(m, mul(t, inv(m, p), p), p)
            assert mt in torus_set and eps[mt] == eps[t]
    for t, u in product(torus, repeat=2):
        assert eps[mul(t, u, p)] == eps[t] ^ eps[u]

    # At the two smallest primes, exhaust the entire actual pair group:
    # (m,n) with equal determinant and equal signed normalizer component.
    pair_checks = 0
    pair_order = None
    if p in (3, 5):
        pair_group = []
        values = {}
        for m, e, q in normalizer:
            for t in torus:
                target = mul(inv(t, p), m, p)
                key = (m, target)
                assert det(target, p) == det(m, p)
                assert mul(target, mul(s, inv(target, p), p), p) == scale(s, (-1)**e, p)
                assert mul(m, inv(target, p), p) == t
                values[key] = eps[t] ^ q
                pair_group.append(key)
        assert len(values) == len(pair_group) == len(normalizer)*n
        for a, b in product(pair_group, repeat=2):
            ab = (mul(a[0], b[0], p), mul(a[1], b[1], p))
            assert ab in values and values[ab] == values[a] ^ values[b]
            pair_checks += 1
        pair_order = len(pair_group)
    row = {"prime": p, "torus_order": n,
           "cartan_GL2_order": len(cartan),
           "signed_normalizer_order": len(normalizer),
           "all_normalizer_torus_conjugations_checked": len(normalizer)*n,
           "full_pair_group_order": pair_order,
           "full_pair_products_checked": pair_checks}
    results.append(row)
    print("PASS", json.dumps(row, sort_keys=True), flush=True)

output = {
    "scope": "Exact signed matrix normalizers and their actual pair groups; no GT0 image exhaustion claim.",
    "checks": results,
    "status": "PASS"
}
Path(__file__).with_suffix(".json").write_text(json.dumps(output, indent=2)+"\n")
print("PASS full signed harmonic covariance, Cartan commutator, arithmetic correction and fixed-diagonal formulas")
