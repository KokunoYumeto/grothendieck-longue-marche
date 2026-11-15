#!/usr/bin/env python3
"""Exact residue certificates used in D.59; no numerical root approximation."""

from fractions import Fraction
from itertools import product
import json
from pathlib import Path


def certificate(ell):
    modulus = ell * ell
    units = [a for a in range(modulus) if a % ell]
    powers = sorted({pow(a, ell, modulus) for a in units})
    zero_triples = [abc for abc in product(powers, repeat=3)
                    if sum(abc) % modulus == 0]
    assert not zero_triples
    primitive_counts = {}
    for xyz in product(range(modulus), repeat=3):
        if all(a % ell == 0 for a in xyz):
            continue
        if sum(pow(a, ell, modulus) for a in xyz) % modulus:
            continue
        nonunits = sum(a % ell == 0 for a in xyz)
        primitive_counts[nonunits] = primitive_counts.get(nonunits, 0) + 1
    assert set(primitive_counts) == {1}
    radius_examples = []
    for r in range(1, 9):
        n = ell ** r
        assert (n - ell) % (ell * (ell - 1)) == 0
        assert sorted({pow(a, n, modulus) for a in units}) == powers
        rho = (Fraction(r) + Fraction(1, ell - 1)) / n
        assert rho < 1
        radius_examples.append({"r": r, "n": n, "rho": str(rho)})
    return {
        "ell": ell,
        "modulus": modulus,
        "unit_ell_power_residues": powers,
        "all_unit_triples_checked": len(powers) ** 3,
        "all_unit_zero_sum_triples": zero_triples,
        "primitive_solution_count_by_nonunit_coordinates": primitive_counts,
        "exact_branch_radius_examples": radius_examples,
    }


def main():
    result = {
        "statement": "D.59",
        "purpose": "Every local Fermat point for ell=3,5 has exactly one nonunit coordinate",
        "general_exponent_proof": (
            "ell^r and ell are congruent modulo ell(ell-1); "
            "this is the exponent of (Z/ell^2)^*."
        ),
        "general_radius_proof": (
            "rho=(r+1/(ell-1))/ell^r<1: it holds at r=1, "
            "and multiplying the right side by ell increases its excess."
        ),
        "certificates": [certificate(3), certificate(5)],
    }
    stem = Path(__file__).with_suffix("")
    text = json.dumps(result, indent=2) + "\n"
    stem.with_suffix(".json").write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
