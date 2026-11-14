#!/usr/bin/env python3
"""Exact finite certificate for Claim D.29 (not a section).

All primality checks use trial division up to the integer square root.
The all-place/all-character assertions are proved in Claim D.29; these finite calculations do not establish those assertions.
"""
import json
from math import factorial, isqrt, lcm, prod
from pathlib import Path


def first_divisor(n):
    if n < 2:
        return 1
    if n % 2 == 0:
        return None if n == 2 else 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return d
    return None


def val_unit(a, p):
    assert a
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    return v, a


def prime_factors(a):
    a = abs(a)
    out = set()
    d = 2
    while d * d <= a:
        if a % d == 0:
            out.add(d)
            while a % d == 0:
                a //= d
        d = 3 if d == 2 else d + 2
    if a > 1:
        out.add(a)
    return out


def legendre(a, p):
    z = pow(a % p, (p - 1) // 2, p)
    assert z in (1, p - 1)
    return 1 if z == 1 else -1


def hilbert(a, b, p):
    alpha, u = val_unit(a, p)
    beta, v = val_unit(b, p)
    if p == 2:
        exponent = ((u - 1) * (v - 1) // 4
                    + alpha * (v * v - 1) // 8
                    + beta * (u * u - 1) // 8)
        return (-1) ** (exponent % 2)
    return ((-1) ** (alpha * beta * ((p - 1) // 2))
            * legendre(u, p) ** beta * legendre(v, p) ** alpha)


prefix = []
P, M, previous_q = 1, 1, 1
# E_1=Q, E_2=Q(i), E_3=E_4=Q(zeta_24), E_5=Q(zeta_120).
constant_conductors = [1, 4, 24, 24, 120]
for j, p in enumerate([2, 3, 5, 7, 11], 1):
    R = 1 + max(val_unit(P + 1, p)[0], val_unit(P + 2, p)[0])
    M = lcm(M, factorial(j) ** j, p ** R)
    assert all(M % c == 0 for c in constant_conductors[:j])
    bound = max(2 ** j, previous_q, p)
    multiplier = max(1, (bound - 1) // M + 1)
    rejected = []
    while True:
        q = 1 + multiplier * M
        divisor = first_divisor(q)
        if divisor is None:
            break
        rejected.append({"candidate": q, "proper_divisor": divisor})
        multiplier += 1
    assert q > bound and q % M == 1
    old_P = P
    P *= q
    prefix.append({
        "j": j, "p_j": p, "R_j": R, "M_j": M, "q_j": q,
        "multiplier": multiplier, "P_j": P,
        "P_previous": old_P, "rejected_progression_candidates": rejected,
        "primality_method": "exact trial division through isqrt(q_j)",
        "primality_trial_bound": isqrt(q),
    })
    previous_q = q

assert [r["q_j"] for r in prefix] == [5, 37, 2161, 58060801, 17244057600001]
assert P == 400266259882177832253327785

avoidance = []
for row in prefix:
    p, R, before = row["p_j"], row["R_j"], row["P_previous"]
    assert (P - before) % (p ** R) == 0
    values = {str(c): val_unit(P + c, p)[0] for c in (1, 2)}
    assert all(values[str(c)] == val_unit(before + c, p)[0] < R for c in (1, 2))
    avoidance.append({"p": p, "R": R, "P5_mod_pR": P % (p ** R),
                      "v_p_P5_plus_c": values,
                      "excludes_Ap_equal_minus_1_or_minus_2": True})

symbols = []
for n in range(1, 6):
    factors = [r["q_j"] for r in prefix[:n]]
    a = prod(factors)
    for d in [-1, 2, 3, 5, -3, -5, 6, 7, 15]:
        places = sorted({2, *factors, *prime_factors(d)})
        local = {str(p): hilbert(a, d, p) for p in places}
        local["infinity"] = 1  # a>0, irrespective of d.
        assert prod(local.values()) == 1
        symbols.append({"N": n, "P_N": a, "d": d, "local_symbols": local,
                        "product": 1,
                        "all_unlisted_places": "symbol 1: both entries are odd-prime units"})

result = {
    "claim": "D.29, unrestricted reciprocity versus admissibility",
    "scope": "Finite arithmetic certificate only. No tuple is asserted to come from a section.",
    "prime_prefix": prefix,
    "tripod_avoidance_checks": avoidance,
    "global_quadratic_reciprocity_cases": symbols,
    "reciprocity_case_count": len(symbols),
    "prime_count": len(prefix),
    "all_checks_passed": True,
}
target = Path(__file__).with_suffix(".json")
target.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"output": str(target), "primes": [r["q_j"] for r in prefix],
                  "reciprocity_cases": len(symbols), "all_checks_passed": True}, indent=2))
