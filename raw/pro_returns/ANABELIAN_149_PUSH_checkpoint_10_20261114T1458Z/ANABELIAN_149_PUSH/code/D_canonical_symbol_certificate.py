#!/usr/bin/env python3
"""Exact arithmetic certificate for the non-section tuple in Claim D.27.

This checks a Hilbert symbol, not the existence or nonexistence of a section.
The unrestricted places are handled exactly because their first symbol entry
is 1; no finite sample is used to infer an all-place assertion.
"""
import json
from fractions import Fraction
from pathlib import Path


def valuation_and_unit(a, p):
    assert a != 0
    value = 0
    while a % p == 0:
        a //= p
        value += 1
    return value, a % p


def legendre(unit, p):
    residue = pow(unit % p, (p - 1) // 2, p)
    assert residue in (1, p - 1)
    return 1 if residue == 1 else -1


def hilbert_odd_positive_integers(a, b, p):
    """(p^alpha*u,p^beta*v)_p, for an odd prime p and a,b>0."""
    assert p > 2 and all(p % d for d in range(2, int(p**0.5) + 1))
    alpha, u = valuation_and_unit(a, p)
    beta, v = valuation_and_unit(b, p)
    return ((-1) ** (alpha * beta * ((p - 1) // 2))
            * legendre(u, p) ** beta * legendre(v, p) ** alpha)


assert 3 not in (0, 1, 2) and 4 not in (0, 1, 2)
unit_squares_mod_3 = sorted({x*x % 3 for x in (1, 2)})
assert unit_squares_mod_3 == [1] and 2 not in unit_squares_mod_3
symbol = hilbert_odd_positive_integers(2, 3, 3)
assert symbol == -1
invariant = Fraction(1, 2) if symbol == -1 else Fraction(0)

# Q_3(sqrt(3)) is ramified quadratic.  Modulo 3 its unit norm
# x^2 - 3*y^2 is x^2, confirming the nonsquare-unit obstruction.
unit_norm_residues = sorted({(x*x - 3*y*y) % 3
                            for x in range(9) for y in range(9)
                            if (x*x - 3*y*y) % 3 != 0})
assert unit_norm_residues == [1]
assert invariant == Fraction(1, 2)

result = {
    "claim": "D.27",
    "scope": "Exact one-prime reciprocity obstruction for an explicitly "
             "non-section tuple; this is not a counterexample to a section theorem.",
    "field": "Q",
    "new_puncture": 2,
    "local_points": {"at_3": 4, "at_every_other_place": 3},
    "translated_kummer_values": {"at_3": 2, "at_every_other_place": 1},
    "dual_character": "Q(sqrt(3))/Q",
    "unit_squares_mod_3": unit_squares_mod_3,
    "unit_norm_residues_mod_3": unit_norm_residues,
    "hilbert_symbol_at_3": symbol,
    "invariant_at_3": str(invariant),
    "all_other_invariants": "0, because the first Hilbert-symbol entry is 1; "
                            "this includes the real place.",
    "sum_of_invariants_in_Q_mod_Z": str(invariant),
    "integrality": "The points are integral on P1 minus {0,1,2,infinity} "
                   "outside {2,3}; this follows from 3*(3-1)*(3-2)=6.",
    "conclusion": "No global squareclass has precisely these localizations.",
}
output = (Path(__file__).resolve().parent.parent / "audit"
          / "D_canonical_symbol_certificate.json")
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"output": str(output), "hilbert_symbol": symbol,
                  "invariant_sum": str(invariant)}, indent=2))
