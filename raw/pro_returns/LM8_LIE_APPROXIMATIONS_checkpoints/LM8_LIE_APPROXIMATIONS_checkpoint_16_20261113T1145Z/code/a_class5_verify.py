#!/usr/bin/env python3
"""Independent exact linear and full-parameter projection certificate for A.25.

This verifier does not import the Magnus/Hall series construction. It checks
the complete saved 1428 by 428 rational system, all ninety kernel vectors,
integrality at five, a modular rank certificate, and the projection to the
entire twenty-parameter class-four family.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import time

HERE = Path(__file__).resolve().parent
START = time.monotonic()


def mod5(x):
    x = F(x)
    return x.numerator * pow(x.denominator, -1, 5) % 5


def rank5(rows):
    a = [[mod5(x) for x in row] for row in rows]
    at = 0
    for j in range(len(a[0])):
        k = next((i for i in range(at, len(a)) if a[i][j]), None)
        if k is None:
            continue
        a[k], a[at] = a[at], a[k]
        u = pow(a[at][j], -1, 5)
        a[at] = [x*u % 5 for x in a[at]]
        for i in range(at+1, len(a)):
            if a[i][j]:
                t = a[i][j]
                a[i] = [(x-t*y) % 5 for x, y in zip(a[i], a[at])]
        at += 1
    return at


def row_basis(rows):
    # Pivot only on five-adic units; an ordinary rational RREF can choose
    # an unnecessary nonunit pivot even for a saturated integral image.
    a = [list(row) for row in rows]
    at, pivots = 0, []
    for j in range(len(a[0])):
        k = next((i for i in range(at, len(a)) if mod5(a[i][j])), None)
        if k is None:
            continue
        a[k], a[at] = a[at], a[k]
        t = a[at][j]
        a[at] = [x/t for x in a[at]]
        for i in range(len(a)):
            if i != at and a[i][j]:
                t = a[i][j]
                a[i] = [x-t*y for x, y in zip(a[i], a[at])]
        pivots.append(j)
        at += 1
    assert all(not any(row) for row in a[at:])
    return list(zip(pivots, a[:at]))


d = json.loads((HERE/"a_metabelian_lift_class5.json").read_text())
raw = (HERE/Path(d["system_file"]).name).read_bytes()
assert hashlib.sha256(raw).hexdigest() == d["system_sha256"]
s = json.loads(raw)
m, n = s["shape"]
assert (m, n) == (1428, 428)
rows = [[] for _ in range(m)]
dense = [[F(0)]*n for _ in range(m)]
for i, j, x in s["matrix_sparse_entries"]:
    t = F(x)
    rows[i].append((j, t))
    dense[i][j] = t
b = list(map(F, s["right_hand_side"]))
p = list(map(F, d["affine_particular_solution"]))
kernel = [list(map(F, v)) for v in d["affine_kernel_basis"]]
free = d["affine_free_columns"]
assert len(p) == n and len(kernel) == len(free) == 90
assert all(x.denominator % 5 for row in rows for _, x in row)
assert all(x.denominator % 5 for x in b+p)
assert all(x.denominator % 5 for v in kernel for x in v)


def apply(v):
    return [sum((x*v[j] for j, x in row if v[j]), F(0)) for row in rows]


assert apply(p) == b
assert all(not any(apply(v)) for v in kernel)
assert all(v[j] == int(i == j) for v, i in zip(kernel, free) for j in free)
r5 = rank5(dense)
assert r5 == n-len(kernel) == d["rational_rank"] == 338
assert all(F(x).denominator % 5 for x in d["f_Hall_coordinates"]+d["h_Hall_coordinates"])

# Columns 0,...,19 are the *original* complete class-four parameters.
# The projection is checked on every class-five nullspace vector.
projected = [v[:20] for v in kernel]
basis = row_basis(projected)
image_rows = [v for _, v in basis]
image_rank5 = rank5(projected)
assert image_rank5 == len(image_rows)
assert all(x.denominator % 5 for v in image_rows for x in v)
for vector in projected:
    rest = list(vector)
    for j, v in basis:
        t = rest[j]
        rest = [x-t*y for x, y in zip(rest, v)]
    assert not any(rest)

c4 = json.loads((HERE/"a_metabelian_lift_class4_rational.json").read_text())
names = [c4["unknown_coordinates"][j] for j in c4["affine_free_columns"]]
offset = p[:20]
image_pivots = [j for j, _ in basis]
complement = [j for j in range(20) if j not in image_pivots]
# Affine equations q_j-offset_j=sum_i (q_pivot_i-offset_pivot_i)*basis_i[j].
equations = [{
    "coordinate": j,
    "constant": offset[j]-sum(offset[i]*v[j] for i, v in basis),
    "pivot_coefficients": [[i, v[j]] for i, v in basis if v[j]],
} for j in complement]
for vector in projected:
    assert all(vector[e["coordinate"]] == sum(vector[i]*v for i, v in e["pivot_coefficients"])
               for e in equations)
assert all(offset[e["coordinate"]] == e["constant"]+sum(offset[i]*v for i, v in e["pivot_coefficients"])
           for e in equations)
result = {
    "source_system_sha256": d["system_sha256"],
    "matrix_shape": [m, n],
    "rational_rank_certified_by_kernel_and_mod5_minor": r5,
    "full_affine_Z5_dimension": len(kernel),
    "all_matrix_rhs_particular_and_kernel_coefficients_five_integral": True,
    "all_ninety_exact_kernel_equations_verified": True,
    "identity_free_column_minor_verified": True,
    "particular_actual_Hall_coordinates_five_integral": True,
    "class5_to_class4_projection": {
        "rank_over_Q_and_F5": len(image_rows),
        "kernel_rank": len(kernel)-len(image_rows),
        "coordinate_names": names,
        "affine_offset": offset,
        "image_basis": image_rows,
        "image_pivots": image_pivots,
        "complete_affine_equations": equations,
        "original_class4_zero_parameter_point_extends": all(not e["constant"] for e in equations),
    },
    "finite_parameter_equation_counts": {
        "solutions_mod_5n": f"5^({len(kernel)}n)",
        "extendible_class4_parameter_points_mod_5n": f"5^({len(image_rows)}n)",
        "fibre_mod_5n": f"5^({len(kernel)-len(image_rows)}n)",
    },
    "finite_count_scope": "Residue solutions of the integral affine parameter equations; no assertion that naive Hall-coordinate reduction modulo5^n is a group quotient in class5.",
    "full_free_profinite_lift_asserted": False,
    "elapsed_seconds": time.monotonic()-START,
}
(HERE/"a_class5_verify.json").write_text(json.dumps(result, indent=2, default=str)+"\n")
text = "\n".join([
    "PASS: exact full1428x428 integral parameter system and its hash.",
    "PASS: complete particular solution and all90 nullspace vectors, with identity free-column minor.",
    "PASS: independent rank338 modulo5 proves rational rank338 and unit nonzero Smith factors.",
    "PASS: actual Hall coordinates of the particular pair are integral at5.",
    f"Class5 full affine Z5 dimension90; projection to class4 rank{len(image_rows)}; fibre rank{90-len(image_rows)}.",
    "Every prior parameter was retained; complete image equations and basis are saved.",
    "Finite counts refer to parameter-equation residues, not naive class5 group-coordinate quotients.",
])+"\n"
(HERE/"a_class5_verify.out").write_text(text)
print(text, end="")
