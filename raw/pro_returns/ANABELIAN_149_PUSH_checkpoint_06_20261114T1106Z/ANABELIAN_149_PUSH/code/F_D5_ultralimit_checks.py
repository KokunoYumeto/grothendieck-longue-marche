#!/usr/bin/env python3
"""Exact finite certificates for the CRT input to D.12--D.14.

This verifies the explicitly constructed rational points and their independent
square classes. It does not approximate or compute the nonprincipal
ultrafilter, and it is not a finite-level substitute for the proofs.
"""

from __future__ import annotations

import argparse
import json
from math import factorial, isqrt, prod
from pathlib import Path


def primes():
    n = 2
    while True:
        if all(n % d for d in range(2, isqrt(n) + 1)):
            yield n
        n += 1


def liouville_residue(n: int) -> int:
    modulus = 3**n
    result = 1
    r = 1
    while factorial(r) < n:
        result += 3 ** factorial(r)
        r += 1
    return result % modulus


def crt(congruences: list[tuple[int, int]]) -> tuple[int, int]:
    residue, modulus = 0, 1
    for value, next_modulus in congruences:
        step = ((value - residue) * pow(modulus, -1, next_modulus)) % next_modulus
        residue += modulus * step
        modulus *= next_modulus
        residue %= modulus
    return residue, modulus


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def certificate(count: int) -> dict:
    points: list[int] = []
    witnesses: list[int] = []
    rows = []
    for n in range(1, count + 1):
        q = next(q for q in primes() if q != 3 and all(x % q for x in points))
        congruences = [(liouville_residue(n), 3**n), (q, q*q)]
        congruences += [(1, old_q) for old_q in witnesses]
        x, modulus = crt(congruences)
        assert x >= 2
        assert all(x % m == value % m for value, m in congruences)
        points.append(x)
        witnesses.append(q)
        rows.append({
            "n": n, "q_n": q, "x_n": str(x),
            "a_mod_3n": liouville_residue(n), "modulus": str(modulus),
            "congruences": [{"residue": r, "modulus": str(m)} for r, m in congruences],
        })
    matrix = [[valuation(x, q) for x in points] for q in witnesses]
    identity = [[int(i == j) for j in range(count)] for i in range(count)]
    assert matrix == identity
    assert len(set(witnesses)) == count
    return {
        "construction": "a = 1 + sum_{r>=1} 3^(r!); x_n by the CRT in D.12",
        "count": count,
        "rows": rows,
        "valuation_matrix": matrix,
        "valuation_matrix_is_identity": True,
        "all_3adic_congruences_verified": True,
        "scope": "Finite arithmetic input only; ultrafilter and absence of fixed propoints are proved in the manuscript.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=12)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("F_D5_ultralimit_output.json"))
    args = parser.parse_args()
    result = certificate(args.count)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "count": result["count"],
        "first_four": result["rows"][:4],
        "valuation_matrix_is_identity": True,
        "all_3adic_congruences_verified": True,
        "output": str(args.output.resolve()),
    }, indent=2))


if __name__ == "__main__":
    main()
