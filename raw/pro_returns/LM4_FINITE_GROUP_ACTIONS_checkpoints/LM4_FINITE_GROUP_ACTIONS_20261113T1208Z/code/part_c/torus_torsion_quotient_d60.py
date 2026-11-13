#!/usr/bin/env python3
"""Exact finite coefficient checks for D.60; no full-group recognition."""
from __future__ import annotations

import json
from pathlib import Path


def check_case(n: int, a: int) -> dict[str, int | str]:
    points = [(r, t) for r in range(n) for t in range(n)]
    image = {(a * z % n, -2 * z % n) for z in range(n)}
    for r, t in points:
        ar, at = ((r + a * t) % n, -t % n)
        assert ((ar + a * at) % n, -at % n) == (r, t)
    if n % 2 == 0 and a % 2 == 0:
        b = a // 2

        def q(r: int, t: int) -> tuple[int, int]:
            return ((r + b * t) % n, t % 2)

        expected_size = 2 * n
        transporter = (1, 0)
        kind = "split_dyadic"
    elif n % 2 == 0:

        def q(r: int, t: int) -> tuple[int]:
            return ((2 * r + a * t) % n,)

        expected_size = n
        transporter = (2 % n,)
        kind = "nonsplit_dyadic"
    else:
        half_a = a * pow(2, -1, n) % n

        def q(r: int, t: int) -> tuple[int]:
            return ((r + half_a * t) % n,)

        expected_size = n
        transporter = (1,)
        kind = "odd_coefficient"
    target = {q(r, t) for r, t in points}
    zero = q(0, 0)
    kernel = {(r, t) for r, t in points if q(r, t) == zero}
    assert kernel == image
    assert len(target) == expected_size
    assert len(kernel) * len(target) == n * n
    assert q(1, 0) == transporter
    for r, t in points:
        assert q((r + a * t) % n, -t % n) == q(r, t)
    return {
        "modulus": n,
        "a": a,
        "kind": kind,
        "domain_size": n * n,
        "image_A_minus_I": len(image),
        "quotient_size": len(target),
    }


def main() -> None:
    moduli = [4, 8, 16, 32, 64, 3, 5, 7, 9, 15]
    rows = [check_case(n, a) for n in moduli for a in range(2 * n)]
    output = {
        "claim": "D.60",
        "status": "PASS",
        "coefficient_cases": len(rows),
        "coefficient_points": sum(int(r["domain_size"]) for r in rows),
        "moduli": moduli,
        "checks": [
            "A squared equals the identity",
            "the displayed quotient kernel equals the image of A-I",
            "the displayed quotient is onto its stated finite target",
            "kernel size times quotient size equals the domain size",
            "the chosen fixed-line generator has quotient coordinate one or two",
            "the quotient map is invariant under the actual matrix action",
        ],
        "rows": rows,
        "scope": (
            "Finite coefficient identities only. The full profinite quotient "
            "and section labels are established by the written universal maps "
            "and D58's actual character, not by these finite checks."
        ),
    }
    target = Path(__file__).with_name("torus_torsion_quotient_d60_output.json")
    target.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in output.items() if k != "rows"}, indent=2))


if __name__ == "__main__":
    main()
