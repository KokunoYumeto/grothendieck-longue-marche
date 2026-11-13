#!/usr/bin/env python3
"""Exact finite certificates for the proved norm-divisor maps in E.72.

The all-level membership theorem is proved in the accompanying TeX.
This program does not evaluate any uncomputed higher class group.
"""
from __future__ import annotations

import ast
import json
from collections import Counter
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent


def v3(n: int) -> int:
    assert n
    e = 0
    while n % 3 == 0:
        n //= 3
        e += 1
    return e


def cycles(q: int, b: int, n: int) -> tuple[list[list[int]], list[int]]:
    modulus = 3**n
    labels = [-1] * modulus
    out: list[list[int]] = []
    for x in range(modulus):
        if labels[x] >= 0:
            continue
        orbit: list[int] = []
        y = x
        while labels[y] < 0:
            labels[y] = len(out)
            orbit.append(y)
            y = (q * y + b) % modulus
        assert y == x
        out.append(orbit)
    return out, labels


def valuation_order(a: int, p: int) -> int:
    order = int(sp.n_order(a % p, p))
    return 0 if order % 3 else v3(order)


def fixed_point(q: int, b: int, n: int) -> int | None:
    s = v3(q - 1)
    if b % (3**s):
        return None
    modulus = 3**n
    return (-b // (3**s) * pow((q - 1) // (3**s), -1, modulus)) % modulus


def transition(q: int, b: int, low: int, high: int) -> tuple[list[int], int]:
    """Minimum 3-adic norm divisibility in each lower prime orbit."""
    lo, labels = cycles(q, b, low)
    hi, _ = cycles(q, b, high)
    exponents = [10**9] * len(lo)
    modulus = 3**low
    for orbit in hi:
        target = labels[orbit[0] % modulus]
        assert all(labels[x % modulus] == target for x in orbit)
        assert len(orbit) % len(lo[target]) == 0
        weight = len(orbit) // len(lo[target])
        exponents[target] = min(exponents[target], v3(weight))
    assert all(e < 10**9 for e in exponents)
    return exponents, len(hi)


def main() -> None:
    raw = (HERE / "e_norm_divisors_gp.out").read_text()
    assert "user error" not in raw and "Error" not in raw
    rows = [ast.literal_eval(s[5:]) for s in raw.splitlines() if s.startswith("DATA ")]
    assert len(rows) == 69
    primes: dict[int, dict[str, object]] = {}
    factor_checks = 0
    transition_checks = 0
    cofinal_divisibility_checks = 0
    for p, d, b, q, logs, pure_degrees, complex_degrees in rows:
        pure, _ = cycles(p, b, d)
        assert sorted(map(len, pure)) == pure_degrees
        complex_orbits = [cycles(q, t, d)[0] for t in logs]
        multiplier = 1 if p % 3 == 1 else 2
        assert sorted(multiplier * len(o) for os in complex_orbits for o in os) == complex_degrees
        factor_checks += 2
        order_v = valuation_order(17, p)
        pure_ok = b % (3**v3(p - 1)) == 0
        complex_ok = [t % (3**v3(q - 1)) == 0 for t in logs]
        assert pure_ok == (order_v == 0)
        assert sum(complex_ok) == (1 if order_v == 1 else 0)
        assert not (pure_ok and any(complex_ok))
        if p % 3 == 2:
            assert pure_ok and not any(complex_ok)
        if d == 1:
            primes[p] = {
                "v3_order_17": order_v,
                "pure_fixed_branch": pure_ok,
                "complex_fixed_branches": sum(complex_ok),
                "pure_frobenius": [p, b],
                "complex_frobenius": [q, logs],
            }
        for qq, bb in [(p, b)] + [(q, t) for t in logs]:
            lo, labels = cycles(qq, bb, d)
            point = fixed_point(qq, bb, d)
            # Squaring a Frobenius with q=-1 mod3 removes its order-two part.
            s = v3(qq - 1) if qq % 3 == 1 else v3(qq * qq - 1)
            hi = d + s + 3
            vals, higher_orbits = transition(qq, bb, d, hi)
            for index, exponent in enumerate(vals):
                if point is not None and index == labels[point]:
                    assert lo[index] == [point]
                    assert exponent == 0
                else:
                    assert exponent >= 3
                    cofinal_divisibility_checks += 1
            transition_checks += 1

    # The full positional norm on the persistent branches at 3 and 17.
    norm = sp.Matrix([[1, 1, 1, 0, 0], [0, 0, 0, 1, 2]])
    kernel = sp.Matrix([[1, 1, 0], [-1, 0, 0], [0, -1, 0],
                        [0, 0, -2], [0, 0, 1]])
    sections = sp.Matrix([[1, 0], [0, 0], [0, 0], [0, 1], [0, 0]])
    assert norm * kernel == sp.zeros(2, 3)
    assert norm * sections == sp.eye(2)
    unimodular = kernel.row_join(sections)
    assert abs(int(unimodular.det())) == 1

    # An actual finite first-layer correction from E.57 cannot persist.
    # At p=7 the roots of beta^3=17*zeta are 3,5,6 for zeta=2.
    # The unique prime-to-three root is 6, so the other two coefficients
    # must be divisible by 3 after one further norm.
    roots = [r for r in range(7) if pow(r, 3, 7) == (17 * 2) % 7]
    assert roots == [3, 5, 6]
    fixed = [r for r in roots if int(sp.n_order(r, 7)) % 3]
    assert fixed == [6]
    # The displayed E.57 divisor is 4*p(beta=3)-2*p(beta=6)-2*p(beta=5).
    finite_correction = {3: 4, 6: -2, 5: -2}
    assert all(finite_correction[r] % 3 for r in [3, 5])

    result = {
        "status": "PASS",
        "actual_polynomial_factorizations": factor_checks,
        "rational_primes": len(primes),
        "finite_weighted_transition_systems": transition_checks,
        "nonfixed_lower_orbits_with_at_least_three_further_factors_of_3":
            cofinal_divisibility_checks,
        "pure_eligible_primes": [p for p, r in primes.items() if r["pure_fixed_branch"]],
        "complex_eligible_primes": [p for p, r in primes.items() if r["complex_fixed_branches"]],
        "ineligible_primes": [p for p, r in primes.items()
                              if not r["pure_fixed_branch"] and not r["complex_fixed_branches"]],
        "positional_norm_matrix": [list(map(int, norm.row(i))) for i in range(2)],
        "saturated_kernel_columns": [list(map(int, kernel.col(j))) for j in range(3)],
        "kernel_completion_determinant": int(unimodular.det()),
        "finite_E57_root_correction": {
            "prime": 7, "beta_roots": roots, "surviving_root": 6,
            "divisor_coefficients": finite_correction,
            "failure": "The two nonsurviving first-layer coefficients are not divisible by3."
        },
        "prime_records": primes,
        "higher_class_groups": "Not computed by this certificate.",
        "universal_norm_exponent_h": "Not evaluated; E69 and E72 retain its exact meaning."
    }
    (HERE / "e_norm_divisors.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "prime_records"}, indent=2))


if __name__ == "__main__":
    main()
