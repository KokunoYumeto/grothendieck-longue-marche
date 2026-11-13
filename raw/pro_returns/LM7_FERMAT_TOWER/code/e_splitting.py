#!/usr/bin/env python3
"""Exact class-two obstruction for C2*C3 -> S3.

No group-system dependency is used.  We construct the regular permutation
representation of the order-162 quotient with kernel the exponent-three
Heisenberg group, prove closure of all normal forms under the generators,
and check every possible pair of section-generator images.  All assertions
are exhaustive finite calculations; the accompanying E.26 gives the
integral and pro-p proofs.
"""
from itertools import product
import json
from pathlib import Path

P = 3
H = list(product(range(P), repeat=3))
STATES = [(*n, i, j) for n in H for i in range(3) for j in range(2)]
INDEX = {g: i for i, g in enumerate(STATES)}
ONE = (0, 0, 0, 0, 0)
ONE_I = INDEX[ONE]


def hm(a, b):
    """x^a0 y^a1 c^a2, c=[x,y]; integral Hall law reduced mod3."""
    return ((a[0]+b[0]) % P, (a[1]+b[1]) % P,
            (a[2]+b[2]-b[0]*a[1]) % P)


XH, YH, CH = (1, 0, 0), (0, 1, 0), (0, 0, 1)
RX = [XH, YH, (P-1, P-1, 0)]


def right_r(g):
    a, b, k, i, j = g
    if j == 0:
        return (a, b, k, (i+1) % 3, 0)
    return (*hm((a, b, k), RX[i]), (i+2) % 3, 1)


def right_s(g):
    a, b, k, i, j = g
    return (a, b, k, i, 1-j)


def inverse_word(w):
    return "".join("rr" if a == "r" else "s" for a in reversed(w))


X = "srsr"
Y = "rsrs"
C = X + Y + inverse_word(X) + inverse_word(Y)


def evaluate(g, word):
    for a in word:
        g = right_r(g) if a == "r" else right_s(g)
    return g


def normal_word(g):
    a, b, k, i, j = g
    return X*a + Y*b + C*k + "r"*i + "s"*j


WORDS = [normal_word(g) for g in STATES]
PERMS = [tuple(INDEX[evaluate(g, w)] for g in STATES) for w in WORDS]
LOOKUP = {v: i for i, v in enumerate(PERMS)}
assert len(LOOKUP) == 162
assert all(evaluate(ONE, w) == g for g, w in zip(STATES, WORDS))
assert all(evaluate(g, "rrr") == g and evaluate(g, "ss") == g
           for g in STATES)
for perm in PERMS:
    for letter in "rs":
        next_perm = tuple(INDEX[evaluate(STATES[i], letter)] for i in perm)
        assert next_perm in LOOKUP
# The 162 distinct normal forms are closed under generators and their
# inverses (r^-1=r^2, s^-1=s), hence give the entire permutation group.

MULT = [[perm[i] for perm in PERMS] for i in range(162)]
assert all(MULT[ONE_I][i] == i and MULT[i][ONE_I] == i for i in range(162))
assert all(MULT[MULT[a][b]][c] == MULT[a][MULT[b][c]]
           for a in range(162) for b in range(162) for c in range(162))


def power(g, n):
    out = ONE_I
    for _ in range(n):
        out = MULT[out][g]
    return out


def order(g):
    a = ONE_I
    for n in range(1, 163):
        a = MULT[a][g]
        if a == ONE_I:
            return n
    raise AssertionError("order exceeds group order")


def ab_state(g):
    a, b, k, i, j = STATES[g]
    return (a, b, i, j)


R_I = INDEX[evaluate(ONE, "r")]
S_I = INDEX[evaluate(ONE, "s")]
X_I = INDEX[evaluate(ONE, X)]
Y_I = INDEX[evaluate(ONE, Y)]
C_I = INDEX[evaluate(ONE, C)]
RP_I = MULT[X_I][R_I]
assert STATES[C_I] == (0, 0, 1, 0, 0)
assert power(RP_I, 3) == C_I
assert power(MULT[RP_I][S_I], 2) == ONE_I
assert power(C_I, 3) == ONE_I
assert order(RP_I) == 9

R_LIFTS = [INDEX[g] for g in STATES if g[3:] == (1, 0)]
S_LIFTS = [INDEX[g] for g in STATES if g[3:] == (0, 1)]
GOOD_PAIRS = []
ABELIAN_PAIRS = set()
ABELIAN_GOOD_LIFTS = []
for rr, ss in product(R_LIFTS, S_LIFTS):
    relations = (power(rr, 3), power(ss, 2), power(MULT[rr][ss], 2))
    if all(g == ONE_I for g in relations):
        GOOD_PAIRS.append((rr, ss))
    if all(ab_state(g) == (0, 0, 0, 0) for g in relations):
        ABELIAN_PAIRS.add((ab_state(rr), ab_state(ss)))
        ABELIAN_GOOD_LIFTS.append((rr, ss))
assert not GOOD_PAIRS
assert len(ABELIAN_PAIRS) == 9
assert all(order(rr) == 9 for rr, ss in ABELIAN_GOOD_LIFTS)

# The inverse image of the particular abelian complement is D_18.
dihedral = set()
for i, j in product(range(9), range(2)):
    dihedral.add(MULT[power(RP_I, i)][power(S_I, j)])
assert len(dihedral) == 18
assert all(MULT[a][b] in dihedral for a in dihedral for b in dihedral)
assert MULT[MULT[S_I][RP_I]][S_I] == power(RP_I, 8)

# Carry cocycle on S3 with values in the sign module.
S3 = list(product(range(3), range(2)))
S3_ONE = (0, 0)


def sign(h):
    return (-1)**h[1]


def smul(h, k):
    return ((h[0] + sign(h)*k[0]) % 3, (h[1]+k[1]) % 2)


def carry(h, k):
    return (h[0] + sign(h)*k[0]) // 3


assert all(sign(h)*carry(k, l)-carry(smul(h, k), l)
           +carry(h, smul(k, l))-carry(h, k) == 0
           for h, k, l in product(S3, repeat=3))
assert all(h[0]+sign(h)*k[0]-smul(h, k)[0] == 3*carry(h, k)
           for h, k in product(S3, repeat=2))

nonidentity = [g for g in S3 if g != S3_ONE]
coboundary_solutions = 0
for values in product(range(3), repeat=5):
    b = {S3_ONE: 0, **dict(zip(nonidentity, values))}
    if all((b[h]+sign(h)*b[k]-b[smul(h, k)]-carry(h, k)) % 3 == 0
           for h, k in product(S3, repeat=2)):
        coboundary_solutions += 1
assert coboundary_solutions == 0

local_parameter_checks = []
for prime in (2, 3, 5, 7):
    for exponent in range(1, 5):
        modulus = prime**exponent
        a_values = [a for a in range(modulus) if (1+3*a) % modulus == 0]
        central_conjugacy_orbit = {2*u % modulus for u in range(modulus)}
        classes = len(a_values)*(modulus//len(central_conjugacy_orbit))
        expected = 0 if prime == 3 else (2 if prime == 2 else 1)
        assert classes == expected
        local_parameter_checks.append({
            "prime": prime, "exponent": exponent, "modulus": modulus,
            "solutions_of_1_plus_3a": len(a_values),
            "section_parameter_classes_under_b_plus_2u": classes,
        })

data = {
    "group_order": 162,
    "kernel_order": 27,
    "kernel": "exponent-three Heisenberg group F/(gamma_3(F) F^3)",
    "quotient": "S3",
    "normal_forms": "x^a y^b c^k r^i s^j, a,b,k,i in {0,1,2}, j in {0,1}",
    "generator_closed_normal_forms": len(LOOKUP),
    "associativity_triples_checked": 162**3,
    "all_section_generator_pairs_checked": len(R_LIFTS)*len(S_LIFTS),
    "section_pairs": len(GOOD_PAIRS),
    "abelian_quotient_order": 54,
    "abelian_quotient_sections": len(ABELIAN_PAIRS),
    "pairs_lifting_abelian_sections": len(ABELIAN_GOOD_LIFTS),
    "order_of_r_lift_for_all_such_pairs": sorted(set(order(rr) for rr, ss in ABELIAN_GOOD_LIFTS)),
    "chosen_lift_r_prime": "x r",
    "chosen_lift_cube": "c=[x,y]",
    "chosen_lift_order": order(RP_I),
    "chosen_complement_preimage_order": len(dihedral),
    "chosen_complement_preimage": "D_18 = C9 semidirect C2 (inversion)",
    "carry_cocycle_triples_checked": 6**3,
    "normalized_mod3_one_cochains_checked": 3**5,
    "carry_coboundary_solutions_mod3": coboundary_solutions,
    "integral_cohomology_class": "1 in H^2(S3,Z(sign))=Z/3",
    "relative_pro_p_section_conjugacy_classes": {"2": 2, "3": 0, "p>=5": 1},
    "finite_checks_of_normalized_central_parameter_equations": local_parameter_checks,
    "rational_section": "r -> c^(-1/3) x r; s -> s",
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(data, indent=2)+"\n")
print(json.dumps(data, indent=2))
