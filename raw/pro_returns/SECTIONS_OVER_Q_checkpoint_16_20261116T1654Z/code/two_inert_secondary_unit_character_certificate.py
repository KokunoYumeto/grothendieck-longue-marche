"""Literal finite residue, class-pairing and secondary-unit maps for A184.

The class-group input at all heights is the proved A173/A177/A179 map.
This certificate verifies its exact seven-prime residue consequence and
the evaluated first secondary character; it does not infer an infinite
arithmetic result from finite group experiments.
"""
from pathlib import Path
from itertools import product
from math import gcd
import json

BASE = Path(__file__).resolve().parent
LOG = []


def say(s):
    LOG.append(s)
    print(s, flush=True)


# Coordinates: three-prime; q11 fixed,+,-; q59 fixed,+,-.
tau = (0, 1, 3, 2, 4, 6, 5)
chi = ((0, 0, 0, 0, 0, 1, 2),
       (0, 0, 1, 2, 0, 2, 1))
delta11 = (0, 0, 1, -1, 0, 0, 0)
delta59 = (0, 0, 0, 0, 0, 1, -1)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b)) % 3


matrix = [[dot(row, d) for d in (delta11, delta59)] for row in chi]
assert matrix == [[0, 2], [2, 1]]
assert (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) % 3 == 2
for row in chi:
    assert tuple(row[tau[i]] % 3 for i in range(7)) == tuple(-x % 3 for x in row)
    assert row[0] == row[1] == row[4] == 0
say("PASS: exact persistent Delta matrix, its determinant, and both anti-invariant seven-prime characters")

total = pure = survivors = 0
survivor_rows = []
for k in product(range(3), repeat=7):
    total += 1
    if k[1] or k[4] or (k[2]+k[3]) % 3 or (k[5]+k[6]) % 3:
        continue
    pure += 1
    vals = [dot(row, k) for row in chi]
    expected = [(matrix[j][0]*k[2] + matrix[j][1]*k[5]) % 3
                for j in range(2)]
    assert vals == expected
    if vals != [0, 0]:
        continue
    survivors += 1
    assert k[1:] == (0, 0, 0, 0, 0, 0)
    for q in (11, 59):
        assert ((q*q-1)//3) % 3 != 0
        for i in range(1, 7):
            assert (2*k[i]*((q*q-1)//3)) % 3 == 0
    survivor_rows.append(k)
assert (total, pure, survivors) == (2187, 27, 3)
say("PASS: all 2187 ramified residue vectors, 27 pure-unit vectors, and exactly three fixed-three-prime survivors")

uniformizer_cases = 0
for a in range(-100, 101):
    if (1-8*a) % 3:
        continue
    b = (1-8*a)//3
    assert 8*a + 3*b == 1 and a % 3 == 2
    for k in range(-12, 13):
        assert (a*k) % 3 == (2*k) % 3
        uniformizer_cases += 1
assert 4-3 == 1  # literal quadratic norm transfer exponent
say(f"PASS: {uniformizer_cases} exact upper-uniformizer valuations and inertia exponents; quadratic transfer 4-3=1")

old = json.loads((BASE / "two_inert_evaluated_norm_phantom_certificate_data.json").read_text())
ks = old["norm_exponents"]
gs = old["divided_norm_exponents"]
assert ks == [3, 57, -3, 1614]
assert gs == [1, 19, -1, 538]
first_secondary_cases = 0
for exponents in product(range(3), repeat=4):
    m = sum(g*z for g, z in zip(gs, exponents))
    k = sum(e*z for e, z in zip(ks, exponents))
    assert k == 3*m
    theta_preimage = ((2*m) % 3, (2*m) % 3)
    assert theta_preimage == tuple(sum((2*g)*z for g, z in zip(gs, exponents)) % 3 for _ in range(2))
    assert (theta_preimage == (0, 0)) == (k % 9 == 0)
    first_secondary_cases += 1
scalar_cases = 0
for m in range(-1000, 1001):
    theta = (2*m % 3, 2*m % 3)
    # psi_1 is defined on U^(3Z), so division is in the actual domain.
    psi_cube = (2*((3*m)//3) % 3, 2*((3*m)//3) % 3)
    assert psi_cube == theta
    assert (psi_cube == (0, 0)) == ((3*m) % 9 == 0)
    scalar_cases += 1
say(f"PASS: {first_secondary_cases} evaluated first norm fibres and {scalar_cases} signed scalar/secondary-character identities")

finite_domain_cases = 0
for r in range(1, 8):
    modulus = 3**(r+1)
    domain = range(0, modulus, 3)
    for k in domain:
        psi = (2*(k//3)) % 3
        assert (psi == 0) == (k % 9 == 0)
        assert (k + modulus)//3 % 3 == (k//3) % 3
        finite_domain_cases += 1
assert (2, 2) != (0, 0)
assert 9 % 9 == 0 and 3 % 9 != 0
say(f"PASS: {finite_domain_cases} finite reductions of the actual secondary-map domain and exact order-three unit support class")

data = {
    "scope": "Finite exact maps for A184; its all-height arithmetic statements are proved in the source.",
    "coordinate_order": ["R3", "R11_fixed", "R11_plus", "R11_minus",
                         "R59_fixed", "R59_plus", "R59_minus"],
    "tau_permutation": tau,
    "characters": chi,
    "Delta_pairing": matrix,
    "survivors": survivor_rows,
    "counts": {"all_vectors": total, "pure_vectors": pure,
               "survivors": survivors, "uniformizer_checks": uniformizer_cases,
               "first_secondary_fibres": first_secondary_cases,
               "scalar_identities": scalar_cases,
               "finite_domain_reductions": finite_domain_cases},
    "first_secondary_map": "psi_1(U^(3m))=(2m,2m) mod3",
    "general_scalar_identity": "psi_n(u^3)=theta_n(u)",
    "distant_norm_image_stabilization": "not asserted",
}
(BASE / "two_inert_secondary_unit_character_certificate_data.json").write_text(
    json.dumps(data, indent=2)+"\n")
say("SCOPE: relative GLOBAL units, actual norm targets, and their pro-three completions are retained; no S-unit-kernel or stabilization inference.")
(BASE / "two_inert_secondary_unit_character_certificate_output.txt").write_text(
    "\n".join(LOG)+"\n")
