#!/usr/bin/env python3
"""Exact finite checks supporting the universal two-torsion branch proof.

The proof, including the unbounded assertions, is in
audit/A_two_torsion_branch_candidate.md.  This program uses only integer
arithmetic and polynomials over F_2.  It checks odd/composite degrees,
partial branch coefficients, and the low-even-order prime-degree class.
"""
from __future__ import annotations

import json
from math import gcd
from pathlib import Path


def orbits(n: int) -> list[set[int]]:
    unused = set(range(1, n))
    out = []
    while unused:
        a = min(unused)
        orbit = set()
        while a not in orbit:
            orbit.add(a)
            a = 2 * a % n
        assert orbit <= unused
        unused -= orbit
        out.append(orbit)
    return out


def bad_indices(n: int, d: int) -> set[int]:
    assert d % 2 == 0
    return {
        j for j in range(1, n)
        if ((j // 2) if j % 2 == 0 else ((n - j) // 2)) % d == d // 2
    }


def is_prime(n: int) -> bool:
    return n >= 2 and all(n % a for a in range(2, int(n ** 0.5) + 1))


def xor_poly(a: set[tuple[int, int]], b: set[tuple[int, int]]) -> set[tuple[int, int]]:
    return a ^ b


def mul_poly(a: set[tuple[int, int]], b: set[tuple[int, int]]) -> set[tuple[int, int]]:
    # Monomials are (s-exponent, b-exponent), or (w-exponent, b-exponent).
    out: set[tuple[int, int]] = set()
    for i, j in a:
        for k, l in b:
            monomial = (i + k, j + l)
            if monomial in out:
                out.remove(monomial)
            else:
                out.add(monomial)
    return out


def main() -> None:
    degree_count = orbit_count = partial_count = 0
    orbit_witnesses = []
    for n in range(3, 256, 2):
        degree_count += 1
        for orbit in orbits(n):
            orbit_count += 1
            j = min(orbit)
            assert j % 2 == 1 and 2 * j < n
            assert 2 * j in orbit and 2 * j in bad_indices(n, 2)
            orbit_witnesses.append({"n": n, "minimum": j, "killed_index": 2 * j, "length": len(orbit)})
        assert 1 + sum(len(o) for o in orbits(n) if not (o & bad_indices(n, 2))) == 1
        for a in range(1, n):
            d = gcd(n, a)
            e = n // d
            b = a // d
            assert e > 1 and e % 2 and gcd(b, e) == 1
            assert b * (n // e) == a
            assert a * (e + 1) % n == a
            assert n // gcd(n, a * (e + 1)) == e
            # Image of the e-character inside mu_n is exactly the original inertia.
            image = {(d * b * t) % n for t in range(e)}
            inertia = {(d * t) % n for t in range(e)}
            assert image == inertia
            partial_count += 1

    prime_records = []
    low_even_cases = 0
    for ell in range(3, 128, 2):
        if not is_prime(ell):
            continue
        first = next(o for o in orbits(ell) if 1 in o)
        if first | {(-x) % ell for x in first} != set(range(1, ell)):
            continue
        tested_d = []
        for d in range(2, ell, 2):
            assert gcd(ell, d) == 1
            bad = bad_indices(ell, d)
            assert bad and bad == {(-x) % ell for x in bad}
            assert all(o & bad for o in orbits(ell))
            low_even_cases += 1
            tested_d.append(d)
        prime_records.append({"ell": ell, "orbit_lengths": sorted(len(o) for o in orbits(ell)), "even_orders": tested_d})

    # Dickson recurrence and its Laurent substitution, both over F_2.
    d0: set[tuple[int, int]] = set()
    d1 = {(1, 0)}
    l0: set[tuple[int, int]] = set()
    l1 = {(1, 0), (-1, 1)}
    s = {(1, 0)}
    b = {(0, 1)}
    substituted_s = {(1, 0), (-1, 1)}
    dickson_count = 0
    for n in range(2, 256):
        d2 = xor_poly(mul_poly(s, d1), mul_poly(b, d0))
        l2 = xor_poly(mul_poly(substituted_s, l1), mul_poly(b, l0))
        assert l2 == {(n, 0), (-n, n)}
        assert (n, 0) in d2 and all(i <= n for i, j in d2)
        assert all(i + 2 * j == n for i, j in d2)
        if n % 2:
            assert all(i % 2 for i, j in d2)
            dickson_count += 1
        d0, d1 = d1, d2
        l0, l1 = l1, l2

    result = {
        "status": "passed",
        "scope": "Finite consistency checks; the accompanying manuscript proves the universal statements.",
        "odd_degrees": degree_count,
        "doubling_orbits": orbit_count,
        "partial_branch_coefficients": partial_count,
        "low_even_prime_cases": low_even_cases,
        "dickson_odd_degrees": dickson_count,
        "prime_cases": prime_records,
        "minimum_orbit_witnesses": orbit_witnesses,
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k not in {"prime_cases", "minimum_orbit_witnesses"}}))


if __name__ == "__main__":
    main()
