#!/usr/bin/env python3
"""Exact certificate for the candidate A.C2.13, using only the standard library."""
from pathlib import Path
import json
from math import gcd


def ff_mul(a, b, modulus, degree):
    q, out = 1 << degree, 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & q:
            a ^= modulus
    return out


def ff_pow(a, n, modulus, degree):
    out = 1
    while n:
        if n & 1:
            out = ff_mul(out, a, modulus, degree)
        a = ff_mul(a, a, modulus, degree)
        n >>= 1
    return out


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def add4(a, b):
    out = [0] * max(len(a), len(b))
    for i, c in enumerate(a):
        out[i] ^= c
    for i, c in enumerate(b):
        out[i] ^= c
    return trim(out)


def mul4(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i+j] ^= ff_mul(u, v, 7, 2)
    return trim(out)


def power4(a, n):
    out = [1]
    while n:
        if n & 1:
            out = mul4(out, a)
        a = mul4(a, a)
        n >>= 1
    return out


def value4(a, x):
    out = 0
    for c in reversed(a):
        out = ff_mul(out, x, 7, 2) ^ c
    return out


def addz(a, b):
    out = [0] * max(len(a), len(b))
    for i, c in enumerate(a):
        out[i] += c
    for i, c in enumerate(b):
        out[i] += c
    return trim(out)


def mulz(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i+j] += u * v
    return trim(out)


def divmonic(a, b):
    assert b[-1] == 1
    r = trim(a)
    q = [0] * max(0, len(r)-len(b)+1)
    while len(r) >= len(b):
        d, c = len(r)-len(b), r[-1]
        q[d] = c
        for i, v in enumerate(b):
            r[i+d] -= c*v
        r = trim(r)
    return trim(q), r


def count_points(degree, modulus):
    q = 1 << degree
    mul = lambda a, b: ff_mul(a, b, modulus, degree)
    power = lambda a, n: ff_pow(a, n, modulus, degree)
    alpha = next(a for a in range(q) if mul(a, a) ^ a == 1)
    alpha2 = mul(alpha, alpha)
    traces, count = {}, 3
    for x in range(2, q):
        rhs = x ^ mul(alpha, power(x, q-2)) ^ mul(alpha2, power(x ^ 1, q-2))
        tr, v = 0, rhs
        for _ in range(degree):
            tr ^= v
            v = mul(v, v)
        assert tr in (0, 1)
        traces[str(x)] = tr
        count += 2 * (tr == 0)
    return {"degree": degree, "modulus_binary": modulus, "alpha": alpha,
            "point_count": count, "branch_points_counted_separately": 3,
            "unramified_trace_values": traces}


def main():
    # F4 = F2[alpha]/(alpha^2+alpha+1), alpha=2, alpha^2=3.
    alpha, alpha2 = 2, 3
    u, a, b, F = [0, 1, 1], [alpha2, 1], [alpha2, 0, 1], [alpha, 1, 1, 1]
    lhs = add4(mul4(u, add4(mul4(a, a), mul4(a, b))),
               mul4(mul4(b, b), add4(F, mul4([alpha], u))))
    rhs = power4([alpha2, 1], 7)
    assert lhs == rhs == [3, 1, 2, 3, 1, 2, 3, 1]
    assert value4(a, alpha2) == 0
    assert value4(b, alpha2) == 1
    assert value4(b, 0) == alpha2 and value4(b, 1) == alpha
    assert value4(u, alpha2) == 1
    assert value4(F, alpha2) == alpha
    assert ff_mul(alpha, alpha2, 7, 2) == 1
    assert 1 ^ alpha ^ alpha2 == 0

    # beta in F16: beta^4+beta+1=0 and alpha=beta^2+beta.
    beta, modulus16, degree16 = 2, 19, 4
    alpha16 = ff_mul(beta, beta, modulus16, degree16) ^ beta
    assert ff_pow(beta, 4, modulus16, degree16) ^ beta ^ 1 == 0
    assert ff_mul(alpha16, alpha16, modulus16, degree16) ^ alpha16 ^ 1 == 0
    assert alpha16 not in (0, 1)
    assert ff_mul(alpha, alpha, 7, 2) ^ alpha == 1  # absolute trace is one.

    counts = [count_points(2, 7), count_points(4, 19)]
    n1, n2 = [d["point_count"] for d in counts]
    assert (n1, n2) == (3, 15)
    q, a1 = 4, n1-5
    assert (a1*a1+n2-17) % 2 == 0
    a2 = (a1*a1+n2-17)//2
    P = [q*q, q*a1, a2, a1, 1]
    assert P == [16, -8, 1, -2, 1]
    R = [-1, 0, 0, 0, 0, 1]
    first_quotient, first_remainder = divmonic(R, P)
    assert first_quotient == [2, 1]
    assert first_remainder == [-33, 0, 6, 3]
    assert all(c % 3 == 0 for c in first_remainder)
    A = [856, 248, -57, -207]
    B = [-2575, -1303, -487, -471, -207]
    assert addz(mulz(A, R), [-40344]) == mulz(P, B)
    assert 40344 == 3*13448 and gcd(13448, 3) == 1

    remaining, orbits = set(range(1, 7)), []
    while remaining:
        start, orbit = min(remaining), []
        i = start
        while i not in orbit:
            orbit.append(i)
            remaining.remove(i)
            i = 2*i % 7
        assert i == start
        orbits.append(orbit)
    assert orbits == [[1, 2, 4], [3, 6, 5]]
    assert {-i % 7 for i in orbits[0]} == set(orbits[1])

    result = {
        "status": "PASS",
        "curve": "y^2+y=x+alpha/x+alpha^2/(x+1), alpha^2+alpha+1=0",
        "F4_encoding": {"1": 1, "alpha": 2, "alpha^2": 3},
        "norm_identity_coefficients_low_first": lhs,
        "a_coefficients_low_first": a, "b_coefficients_low_first": b,
        "local_values": {"a(alpha^2)": 0, "b(alpha^2)": 1,
                         "b(0)": alpha2, "b(1)": alpha},
        "beta_polynomial": "X^4+X+1",
        "point_counts": counts,
        "frobenius_polynomial_low_first": P,
        "X5_minus_1_remainder": first_remainder,
        "X5_minus_1_quotient": first_quotient,
        "annihilator_multiplier_low_first": A,
        "annihilator_constant": 40344,
        "annihilator_quotient_low_first": B,
        "three_primary_theta_exponent_bound": 3,
        "doubling_orbits_mod7": orbits,
        "degree7_cover_genus": 8,
        "degree7_cover_two_rank_from_proved_orbit_argument": 2,
        "scope": "The audit proves the divisor, all-abelian-three-group ordinariness, and section-separation implications. This finite certificate verifies the exact algebra and counts."
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

