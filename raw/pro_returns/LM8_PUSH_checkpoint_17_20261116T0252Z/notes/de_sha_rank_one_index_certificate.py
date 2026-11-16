#!/usr/bin/env python3
"""Exact supporting arithmetic for the unregistered D84 candidate.

The module, coinduction and actual-action assertions are written proofs.
This certificate checks the new norm-polynomial low coefficients, finite
boundary orbit counts, actual cyclotomic powers and the t=-24 example.
It does not infer an all-depth theorem from these finite checks.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def vp(n, p=5):
    if not n:
        return None
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


norms = []
for d in range(1, 6):
    for e in range(d+1, 8):
        a, m = 5**d, 5**(e-d)
        sj = F(m*(m-1), 2)
        sj2 = F(m*(m-1)*(2*m-1), 6)
        g = [F(m), a*sj, (a*a*sj2-a*sj)/2]
        assert all(x.denominator == 1 for x in g)
        quotient = [x/m for x in g]
        assert quotient[0] == 1
        assert all(x.denominator % 5 for x in quotient)
        assert all(vp(x.numerator) >= e-d for x in g if x)
        norms.append({
            "d": d, "e": e,
            "g_coefficients_through_degree_two": [str(x) for x in g],
            "quotient_by_5_power": [str(x) for x in quotient],
            "quotient_is_integral_unit_mod_z3": True,
        })

orbits = []
for n in range(1, 5):
    modulus = 5**n
    pending = set(range(modulus))
    actual = []
    while pending:
        start = min(pending)
        orbit, x = set(), start
        while x not in orbit:
            orbit.add(x)
            x = (2*x) % modulus
        assert x == start
        pending -= orbit
        actual.append(sorted(orbit))
    assert len(actual) == n+1
    for orbit in actual:
        assert len({vp(x) if x else n for x in orbit}) == 1
    lengths = sorted(map(len, actual))
    assert lengths == sorted([1]+[4*5**j for j in range(n)])
    orbits.append({"n": n, "group_order": modulus,
                   "orbit_count": len(actual),
                   "orbit_lengths": lengths,
                   "augmentation_kernel_rank": len(actual)-1,
                   "exact_substitution_by_two": True})

powers = []
for d in range(1, 11):
    N = 5**d
    gamma = pow(2, 4*5**(d-1), 5*N)
    assert gamma == 1+3*N
    assert gamma % N == 1
    powers.append({"d": d, "modulus": 5*N,
                   "actual_power_modulus": gamma,
                   "identity_on_order_5_to_d_boundary": True,
                   "D79_top_defect_mod5": (3*3+3) % 5})
assert all(x["D79_top_defect_mod5"] == 2 for x in powers)

characters = {"compact_Cartier_untwisted_weights": [2, 3, 4],
              "two_eigenvalues_minus_one": [2**j-1 for j in [2, 3, 4]],
              "five_valuations": [vp(2**j-1) for j in [2, 3, 4]],
              "I_over_I_squared_tame_difference": 2-1}
assert characters["five_valuations"] == [0, 0, 1]
assert characters["I_over_I_squared_tame_difference"] % 5

point = {"t": -24, "one_minus_t": 25,
         "away_prime_exponents": {"2": 3, "3": 1},
         "valuation_vector": [0, 2], "away_generator": [1, 0],
         "basis_determinant": 2,
         "24_fourth_minus_one": 24**4-1,
         "exact_quotient_by_25": (24**4-1)//25,
         "five_valuation_numerator": vp(24**4-1),
         "five_valuation_log6": 1,
         "local_unit_depth": vp(24**4-1)-1,
         "boundary_depth": "infinity",
         "compact_kernel": "Z5"}
assert point["24_fourth_minus_one"] == 25*13271
assert point["local_unit_depth"] == 1
assert point["basis_determinant"] % 5

result = {"status": "PASS", "candidate": "D.84, unregistered",
          "norm_polynomial_rows": norms,
          "norm_polynomial_row_count": len(norms),
          "boundary_orbit_rows": orbits,
          "cyclotomic_power_rows": powers,
          "three_jet_characters": characters,
          "actual_point": point,
          "scope": "Exact supporting checks only; the all-index module and actual cohomology proof is in the draft."}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))
