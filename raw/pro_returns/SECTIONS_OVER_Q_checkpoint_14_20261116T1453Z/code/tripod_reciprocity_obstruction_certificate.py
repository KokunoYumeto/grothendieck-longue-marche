#!/usr/bin/env python3
"""Finite exact arithmetic for A142's changed fixed-local tuple.

Only the retained rational centre data are imported.  All arithmetic
helpers are implemented here using the standard library.  This does
not execute the infinite mixed-cover or Chebotarev recursion, nor the
initial choice at every prime up to 1,065,024; those choices are proved
to exist by the explicit bounds and exact root maps in the source.
"""
from fractions import Fraction as F
from pathlib import Path
from math import gcd, isqrt
from itertools import product
import json


def factor(n):
    n = abs(n)
    assert n
    result = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def support(q):
    q = F(q)
    return set(factor(q.numerator)) | set(factor(q.denominator))


def vu(q, p, modulus=None):
    q = F(q)
    assert q
    num, den = q.numerator, q.denominator
    val = 0
    while num % p == 0:
        num //= p
        val += 1
    while den % p == 0:
        den //= p
        val -= 1
    m = modulus if modulus is not None else p
    return val, num * pow(den, -1, m) % m


def nonsquare(u, p):
    return int(pow(u, (p - 1) // 2, p) == p - 1)


def hilbert(a, b, p):
    va, ua = vu(a, p, 8 if p == 2 else p)
    vb, ub = vu(b, p, 8 if p == 2 else p)
    if p == 2:
        return (((ua - 1) // 2) * ((ub - 1) // 2)
                + va * ((ub * ub - 1) // 8)
                + vb * ((ua * ua - 1) // 8)) % 2
    return (va * vb * ((p - 1) // 2)
            + va * nonsquare(ub, p) + vb * nonsquare(ua, p)) % 2


def fourth(q, p):
    v, u = vu(q, p, 16 if p == 2 else p)
    return v % 4 == 0 and (u == 1 if p == 2 else
                           pow(u, (p - 1) // gcd(4, p - 1), p) == 1)


def f(t):
    return 4 * t * (1 - t)


def main():
    data = json.loads(Path(__file__).with_name("harmonic_twist_repair_data.json").read_text())
    a = tuple(F(x) for x in data["a"])
    centres = {int(p): F(t) for p, t in data["local_T"].items()}
    old = (F(0), F(1), F(1, 2))
    R, c = F(529, 382), F(-338, 191)
    cp, d, star = 1 - c, 18512174429, 4679
    b, tstar = f(c), cp + star
    assert cp == F(529, 191) and b == F(-715208, 36481)
    assert tstar == F(894218, 191)
    assert star % 24 == 23
    assert all(star % j for j in range(2, isqrt(star) + 1))
    assert star not in centres
    assert f(R) == F(-77763, 36481)
    assert f(R) - b == F(637445, 36481) > 0 and d > 0
    print("PASS: all literal constants, the new prime4679 and the actual real signs.")

    alpha_nonzero, beta_nonzero, base_nonzero = [], [], []
    root_count = 0
    for p, t in sorted(centres.items()):
        assert t not in (*old, c, cp)
        assert f(t) - b == -4 * (t - c) * (t - cp)
        for i, ai in zip(old, a):
            assert fourth((t - i) / ai, p)
            root_count += 1
        alpha = hilbert(t - c, d, p)
        beta = hilbert(t - cp, d, p)
        base = hilbert(f(t) - b, d, p)
        const = hilbert(-4, d, p)
        assert base == (alpha + beta + const) % 2
        if alpha: alpha_nonzero.append(p)
        if beta: beta_nonzero.append(p)
        if base: base_nonzero.append(p)
    assert len(centres) == 611 and root_count == 1833
    assert alpha_nonzero == [2]
    assert beta_nonzero == [2, 7, 139]
    assert not base_nonzero
    constant_support = {2} | support(d)
    assert [p for p in sorted(constant_support) if hilbert(-4, d, p)] == [7, 139]
    print("PASS: all611 original fixed centres and1833 actual fourth-power conditions.")
    print("Original alpha bits:", alpha_nonzero, "; beta bits:", beta_nonzero,
          "; base-function bits:", base_nonzero)

    expected_rad = (F(2), F(676, 147), F(867, 2 * (13 * 155564491) ** 2))
    roots = (2304, 2961, 4466)
    for i, ai, rad, root in zip(old, a, expected_rad, roots):
        assert (cp - i) / ai == rad
        val, unit = vu((tstar - i) / ai, star)
        assert val == 0 and pow(root, 4, star) == unit
        assert 4 * pow(root, 3, star) % star
        assert fourth((tstar - i) / ai, star)
    assert vu(d, star)[0] == 0 and nonsquare(vu(d, star)[1], star) == 1
    assert vu(tstar - cp, star)[0] == 1
    assert vu(tstar - c, star)[0] == 0
    assert vu(f(tstar) - b, star)[0] == 1
    assert hilbert(tstar - c, d, star) == 0
    assert hilbert(tstar - cp, d, star) == 1
    assert hilbert(f(tstar) - b, d, star) == 1
    print("PASS: literal new residue roots", roots, "and their nonzero Hensel derivatives.")
    print("PASS: the new base-function Hilbert bit is1 at4679; its valuation is exactly1.")

    boundaries = ((-1146, -382), (382,), (191, -573))
    for root, generators in zip(roots, boundaries):
        for character in generators:
            assert star not in support(character)
            assert hilbert(root, character, star) == 0
    initial_support = {2}
    for q in (*a, d, *(c - i for i in old), *(cp - i for i in old)):
        initial_support |= support(q)
    assert initial_support == {2, 3, 7, 13, 17, 23, 139, 191, 1119169}
    assert support(cp - c) == {3, 17, 191}
    assert set().union(*(support(i - cp) for i in old)) == {2, 3, 13, 17, 23, 191}
    print("PASS: new root symbols vanish and all old/new boundary support exclusions are exact.")

    # This strict base bound proves an old ordinary point at every additional
    # initial good prime.  The source chooses a p^2 displacement if needed.
    assert (4500 - 63) ** 2 - 66 ** 2 * 4500 == 84969 > 0
    B0 = (8 * 128 + 8) ** 2
    assert B0 == 1065024 and 4500 < star < B0 < 1119169
    tested = 0
    for ns in product((4, 8, 12, 16, 24, 48), repeat=3):
        D = ns[0] * ns[1] * ns[2]
        N = 1
        for n in ns:
            N = N * n // gcd(N, n)
        twice_g = -2 * D + sum(D - D // n for n in ns) + D - D // N + 2
        boundary = sum(D // n for n in ns) + D // N + 2 * D
        assert twice_g <= 2 * D + 2 and boundary <= 6 * D
        root_bound = 8 * D + 8
        assert root_bound ** 2 + 1 - (2 * D + 2) * root_bound - 6 * D == 48 * D * D + 90 * D + 49
        assert root_bound ** 2 + 1 - twice_g * root_bound - boundary > 0
        tested += 1
    print("PASS: strict initial good-prime bound and", tested, "mixed bounds with both fibres removed.")
    print("FINITE CERTIFICATE PASSED: total quadratic invariant is1/2 after the one changed place.")
    print("The source proves the cofinal construction and permanent unit condition; no infinite recursion was executed.")
    Path(__file__).with_name("tripod_reciprocity_obstruction_data.json").write_text(
        json.dumps({"prime": star, "T": str(tstar), "new_puncture": str(b),
                    "character": d, "residue_roots": roots, "initial_bound": B0,
                    "original_alpha_nonzero": alpha_nonzero,
                    "original_beta_nonzero": beta_nonzero,
                    "original_base_nonzero": base_nonzero,
                    "new_base_nonzero": [star], "mixed_bound_cases": tested}, indent=2) + "\n")


if __name__ == "__main__":
    main()
