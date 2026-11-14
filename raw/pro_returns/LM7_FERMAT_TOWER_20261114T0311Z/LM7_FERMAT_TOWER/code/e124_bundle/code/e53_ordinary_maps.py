#!/usr/bin/env python3
"""Independent exact maps for E124; no import of another mathematical program.

Reads the literal GP presentation and independently checks every Smith map,
all finite class elements, the ordinary-unit residue inverse and the exact
normal-form changes used in the all-level proof. Rational matrices are
serialized as rational strings and decoded entrywise before export.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
import hashlib
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "code"


def records(path):
    return [json.loads(x) for x in path.read_text().splitlines() if x.startswith("{")]


def integers(m):
    m = S.Matrix(m)
    assert all(S.denom(x) == 1 for x in m)
    a = [[int(x) for x in row] for row in m.tolist()]
    assert S.Matrix(a) == m
    return a


def rationals(m):
    m = S.Matrix(m)
    a = [[str(x) for x in row] for row in m.tolist()]
    assert S.Matrix([[S.Rational(x) for x in row] for row in a]) == m
    return a


def points(moduli):
    return list(product(*(range(n) for n in moduli)))


def apply(m, x, moduli):
    y = S.Matrix(m) * S.Matrix(x)
    assert all(S.denom(v) == 1 for v in y)
    return tuple(int(v) % n for v, n in zip(y, moduli))


def multiple(x, k, moduli):
    return tuple(k * a % n for a, n in zip(x, moduli))


def add(x, y, moduli):
    return tuple((a + b) % n for a, b, n in zip(x, y, moduli))


def subgroup(generators, moduli):
    out = {tuple(0 for _ in moduli)}
    for g in generators:
        cyc = {multiple(g, k, moduli) for k in range(max(moduli))}
        out = {add(a, b, moduli) for a in out for b in cyc}
    return out


r = records(CODE / "e53_ordinary_genus.out")
assert r[-1]["status"] == "PASS"
g = r[0]
R = S.Matrix(g["idele_relations"])
phi = S.Matrix([g["restriction"]])
K = S.Matrix(g["kernel_lattice"])
KR = S.Matrix(g["kernel_relations"])
U = S.Matrix(g["smith_left"])
V = S.Matrix(g["smith_right"])
diag = g["smith_diagonal"]
assert R == K * KR
assert abs(K.det()) == 3 and abs(U.det()) == abs(V.det()) == 1
assert U * KR * V == S.diag(*diag)
assert all(x % 3 == 0 for x in phi * K)
assert abs(R.det()) == 2187 and abs(KR.det()) == 729
forward, backward = U * K.inv(), K * U.inv()
assert forward * backward == backward * forward == S.eye(5)
assert all(S.denom(x) == 1 for x in backward)
qraw = S.Matrix(g["three_prime_raw"])
qfull = apply(forward, qraw, diag)
assert list(qfull) == g["three_prime_smith"]

upper = (27, 9, 3)
lower = (9, 9, 3)
US, LS = points(upper), points(lower)
N = S.Matrix([[8, 1, 0], [1, 0, 0], [2, 1, 1]])
J = S.Matrix([[0, 3, 0], [3, 3, 0], [0, 0, 0]])
assert N == S.Matrix(g["actual_norm_full"])[:, :3]
q2, q3 = (6, 3, 1), qfull[:3]
assert q3 == (21, 0, 1)
assert apply(N, q3, lower) == q2
assert apply(J, q2, upper) == multiple(q3, 3, upper)
assert {apply(N, x, lower) for x in US} == set(LS)
for x in US:
    assert apply(J, apply(N, x, lower), upper) == multiple(x, 3, upper)
for y in LS:
    assert apply(N, apply(J, y, upper), lower) == multiple(y, 3, lower)
kn = {x for x in US if apply(N, x, lower) == (0, 0, 0)}
kj = {y for y in LS if apply(J, y, upper) == (0, 0, 0)}
assert kn == subgroup([(9, 0, 0)], upper)
assert kj == subgroup([(3, 0, 0), (0, 0, 1)], lower)
assert len(kn) == 3 and len(kj) == 9
all_lifts = 0
for y in LS:
    lifts = [x for x in US if apply(N, x, lower) == y]
    assert len(lifts) == 3
    for x in lifts:
        assert multiple(x, 3, upper) == apply(J, y, upper)
        all_lifts += 1

P2 = S.Matrix([[7, 7, 0], [2, 4, 3]])
P3 = S.Matrix([[0, 7, 0], [8, 5, 3]])
assert all(int(x) % 9 == 0 for x in P2 * N - P3)
q2sub, q3sub = subgroup([q2], lower), subgroup([q3], upper)
assert len(q2sub) == 3 and len(q3sub) == 9
assert {x for x in LS if apply(P2, x, (9, 9)) == (0, 0)} == q2sub
assert {x for x in US if apply(P3, x, (9, 9)) == (0, 0)} == q3sub
assert {apply(P3, x, (9, 9)) for x in US} == set(points((9, 9)))
st = subgroup([apply(J, y, upper) for y in LS] + [q3], upper)
assert len(st) == 81
defect = S.Matrix([[1, 0, 0], [0, 1, 0]])
assert {x for x in US if apply(defect, x, (3, 3)) == (0, 0)} == st
assert {apply(defect, x, (3, 3)) for x in US} == set(points((3, 3)))

# The actual coherent-quotient basis at level three.
B = S.diag(7, 1, 1)
Binv = S.diag(4, 1, 1)  # 7*4=1 modulo27.
assert apply(B, (3, 0, 1), upper) == q3
for x in US:
    assert apply(Binv, apply(B, x, upper), upper) == x
    assert apply(B, apply(Binv, x, upper), upper) == x
assert apply(P3 * B, (1, 0, 0), (9, 9)) == (0, 2)
assert apply(P3 * B, (0, 1, 0), (9, 9)) == (7, 5)

# Localized integral changes for the actual all-level relation calculation.
# For a>=2, 9x=3u q, 9y=3v q, with u=1 mod3 and v=0 mod3.
# P's columns are X=x/u, Y=y-v*x/u, Z=q-3*x/u.
relation_checks = []
for a, u, v in product(range(2, 7), (1, 4, 7, 10), (0, 3, 6, 9)):
    old = S.Matrix([[3**a, -3*u, -3*v], [0, 9, 0], [0, 0, 9]])
    P = S.Matrix([[0, 0, 1], [S.Rational(1, u), -S.Rational(v, u), -S.Rational(3, u)], [0, 1, 0]])
    new = S.diag(3**(a+1), 9, 3)
    left = (P * new).inv() * old
    right = old.inv() * P * new
    assert left * right == right * left == S.eye(3)
    assert all(int(S.denom(t)) % 3 for t in list(left) + list(right))
    assert abs(S.numer(left.det())) % 3 and abs(S.denom(left.det())) % 3
    relation_checks.append([a, u, v])

sat = json.loads((CODE / "e53_ordinary_saturation.json").read_text())
F, Fi = S.Matrix(sat["residue_matrix"]), S.Matrix(sat["inverse_mod3"])
assert F.shape == (9, 9)
assert all(int(x) % 3 == 0 for x in F * Fi - S.eye(9))
assert all(int(x) % 3 == 0 for x in Fi * F - S.eye(9))
assert int(F.det()) % 3 != 0

inputs = ["e53_ordinary_genus.out", "e53_ordinary_genus_chars.json", "e53_ordinary_saturation.json"]
out = {
    "status": "PASS",
    "full_ambient_forward_rational": rationals(forward),
    "full_ambient_inverse_integral": integers(backward),
    "smith_left": integers(U), "smith_right": integers(V),
    "upper_type": upper, "lower_type": lower,
    "norm": integers(N), "extension": integers(J),
    "upper_three_prime": q3, "lower_three_prime": q2,
    "norm_kernel": sorted(kn), "extension_kernel": sorted(kj),
    "all_lift_extension_checks": all_lifts,
    "upper_elements_checked": len(US), "lower_elements_checked": len(LS),
    "S_projection_lower": integers(P2), "S_projection_upper": integers(P3),
    "strongly_ambiguous_order": len(st),
    "ordinary_unit_defect_projection": integers(defect),
    "ordinary_unit_defect_type": [3, 3],
    "level_three_normal_form": integers(B),
    "level_three_normal_form_inverse": integers(Binv),
    "localized_relation_checks": relation_checks,
    "saturated_unit_residue_rank": 9,
    "saturated_unit_residue_determinant": int(F.det()),
    "input_hashes": {p: hashlib.sha256((CODE / p).read_bytes()).hexdigest() for p in inputs},
    "scope": "Every finite class map and its inverse is checked on every element. The localized relation checks verify the algebraic basis change, not values of higher arithmetic prime orders. The eventual valuation exponent h remains unevaluated."
}
s = json.dumps(out, indent=2) + "\n"
(CODE / "e53_ordinary_maps.json").write_text(s)
print(s, end="")
