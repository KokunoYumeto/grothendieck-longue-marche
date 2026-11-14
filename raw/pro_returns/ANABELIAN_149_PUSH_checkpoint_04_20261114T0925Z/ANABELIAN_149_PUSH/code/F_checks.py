#!/usr/bin/env python3
"""Finite certificates for Part F; the profinite proofs are in sections/F.tex.

Run from any directory.  This uses only Python's standard library and writes
F_checks_output.json next to this file.  Finite checks are not used to infer
injectivity in an inverse limit or the nonexistence of an integer representative.
"""

from itertools import product
from math import factorial, gcd
from pathlib import Path
import json


def lambda_residue(modulus):
    """CRT component of lambda_2=1, lambda_l=0 for every odd prime l."""
    assert modulus > 0
    two_part = 1
    odd_part = modulus
    while odd_part % 2 == 0:
        two_part *= 2
        odd_part //= 2
    if two_part == 1:
        return 0
    return (odd_part * pow(odd_part, -1, two_part)) % modulus


def multiply(x, y, modulus):
    """(Z/modulus) semidirect C_2, with the inversion action."""
    z, g = x
    w, h = y
    return ((z + (-1 if g else 1) * w) % modulus, (g + h) % 2)


def morphism(x, modulus, multiplicity, cocycle):
    z, g = x
    return ((multiplicity * z + (cocycle if g else 0)) % modulus, g)


def run():
    crt_rows = []
    for stage in range(2, 13):
        modulus = factorial(stage)
        residue = lambda_residue(modulus)
        if crt_rows:
            previous = crt_rows[-1]
            assert residue % previous["modulus"] == previous["residue"]
        crt_rows.append({"stage": stage, "modulus": modulus, "residue": residue})
    # More divisibility pairs, beyond the displayed factorial chain.
    crt_pairs = 0
    for n in range(1, 101):
        for m in range(n, 501, n):
            assert lambda_residue(m) % n == lambda_residue(n)
            crt_pairs += 1

    contact_rows = []
    for modulus in range(2, 25):
        kernel = [(a, b) for a, b in product(range(modulus), repeat=2)
                  if (a + b) % modulus == 0]
        assert set(kernel) == {(a, -a % modulus) for a in range(modulus)}
        diagonal_kernel = [a for a in range(modulus) if 2 * a % modulus == 0]
        assert len(kernel) == modulus
        assert len(diagonal_kernel) == gcd(2, modulus)
        contact_rows.append({"modulus": modulus, "kernel_size": len(kernel),
                             "diagonal_kernel_size": len(diagonal_kernel)})

    homomorphism_checks = 0
    finite_index_rows = []
    for modulus in range(2, 19):
        group = list(product(range(modulus), range(2)))
        for multiplicity in range(1, 6):
            for cocycle in sorted({0, 1, lambda_residue(modulus)}):
                images = {morphism(x, modulus, multiplicity, cocycle) for x in group}
                assert len(group) // len(images) == gcd(modulus, multiplicity)
                for x, y in product(group, repeat=2):
                    assert morphism(multiply(x, y, modulus), modulus,
                                    multiplicity, cocycle) == multiply(
                                        morphism(x, modulus, multiplicity, cocycle),
                                        morphism(y, modulus, multiplicity, cocycle),
                                        modulus)
                    homomorphism_checks += 1
        finite_index_rows.append({"modulus": modulus,
                                  "mu_3_index": gcd(modulus, 3)})

    root_rows = []
    for order in range(2, 9):
        source_order = factorial(8)
        assert source_order % order == 0
        kernel_count = sum(a % order == 0 for a in range(source_order))
        assert kernel_count == source_order // order
        root_rows.append({"source_order": source_order, "root_order": order,
                          "kernel_size": kernel_count})

    result = {
        "all_assertions_passed": True,
        "scope": "Finite certificates only; F.12 and F.13 prove the whole profinite statements.",
        "crt": {"definition": "lambda_2=1; lambda_l=0 for odd l",
                "factorial_stages": crt_rows,
                "compatibility_pairs_checked": crt_pairs,
                "nonintegrality_proof": "An integer with every odd-adic component zero is zero, contradicting its 2-adic component one."},
        "blowup_contact": {"matrix": [[1, 1]], "integer_kernel_generator": [1, -1],
                            "finite_reductions": contact_rows,
                            "profinite_diagonal": "Multiplication by two on Zhat is injective, although some finite reductions have a kernel."},
        "semidirect_product": {"action": "C2 acts by inversion on Z/n",
                                "map": "(z,g) -> (mu*z+a(g),g); a(0)=0 and a(1)=c",
                                "homomorphism_equalities_checked": homomorphism_checks,
                                "mu_3_indices": finite_index_rows,
                                "profinite_index": "mu, for positive integer mu; finite index is gcd(mu,n)."},
        "finite_root_stack_quotients": root_rows,
    }
    destination = Path(__file__).with_name("F_checks_output.json")
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"all_assertions_passed": True,
                      "crt_compatibility_pairs": crt_pairs,
                      "homomorphism_equalities": homomorphism_checks,
                      "output": str(destination)}, indent=2))


if __name__ == "__main__":
    run()
