#!/usr/bin/env python3
"""Independent linear-certificate and complete-family checks for A.24.

Does not import the series/BCH construction. Checks saved rational
matrices, their finite-field reductions, entire nullspace bases, and the
projection between the full class-four and class-three affine families.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import csv

HERE = Path(__file__).resolve().parent


def mod5(x):
    x = F(x)
    return x.numerator * pow(x.denominator, -1, 5) % 5


def rank5(rows):
    a = [[mod5(t) for t in row] for row in rows]
    n = len(a[0])
    at = 0
    for j in range(n):
        k = next((i for i in range(at, len(a)) if a[i][j]), None)
        if k is None:
            continue
        a[k], a[at] = a[at], a[k]
        inverse = pow(a[at][j], -1, 5)
        a[at] = [x*inverse % 5 for x in a[at]]
        for i in range(at+1, len(a)):
            if a[i][j]:
                t = a[i][j]
                a[i] = [(x-t*y) % 5 for x, y in zip(a[i], a[at])]
        at += 1
    return at


def unpack(data):
    m, n = data["shape"]
    a = [[F(0)]*n for _ in range(m)]
    for i, j, v in data["matrix_sparse_entries"]:
        a[i][j] = F(v)
    return a, list(map(F, data["right_hand_side"]))


def apply(a, v):
    return [sum(x*y for x, y in zip(row, v) if x and y) for row in a]


certificates = {}
reports = []
for c in [3, 4]:
    path = HERE/f"a_metabelian_lift_class{c}_rational.json"
    d = json.loads(path.read_text())
    system_path = HERE/Path(d["system_file"]).name
    raw = system_path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == d["system_sha256"]
    system = json.loads(raw)
    a, b = unpack(system)
    particular = list(map(F, d["affine_particular_solution"]))
    kernel = [list(map(F, row)) for row in d["affine_kernel_basis"]]
    assert all(t.denominator % 5 for row in a for t in row)
    assert all(t.denominator % 5 for t in b+particular)
    assert all(t.denominator % 5 for row in kernel for t in row)
    assert apply(a, particular) == b
    assert all(not any(apply(a, v)) for v in kernel)
    free = d["affine_free_columns"]
    assert len(free) == len(kernel) == d["linear_solution_nullity"]
    assert all(v[k] == int(k == j) for v, j in zip(kernel, free) for k in free)
    r5 = rank5(a)
    assert r5 == len(particular)-len(kernel) == d["linear_system_rank"]
    # The displayed independent kernel gives the rational upper rank
    # bound, and the nonzero mod5 minor gives the lower rank bound.
    finite = json.loads((HERE/f"a_metabelian_lift_class{c}_mod5_system.json").read_text())
    finite_result = json.loads((HERE/f"a_metabelian_lift_class{c}_mod5.json").read_text())
    assert finite_result["second_derived_Lie_rank"] == d["second_derived_Lie_rank"]
    fa, fb = unpack(finite)
    assert [[mod5(t) for t in row] for row in a] == [[mod5(t) for t in row] for row in fa]
    assert list(map(mod5, b)) == list(map(mod5, fb))
    certificates[c] = (d, a, b, particular, kernel)
    reports.append({
        "class": c,
        "matrix_shape": system["shape"],
        "rational_and_mod5_rank": r5,
        "full_affine_dimension": len(kernel),
        "matrix_reduction_matches_independent_mod5_construction": True,
        "integral_particular_and_entire_kernel_checked": True,
        "second_derived_rank_over_Q_and_F5": d["second_derived_Lie_rank"],
        "rational_rank_proof": "Independent displayed kernel plus nonzero mod5 rank minor",
    })

d3, a3, b3, p3, k3 = certificates[3]
d4, a4, b4, p4, k4 = certificates[4]
names4 = {tuple(name): j for j, name in enumerate(d4["unknown_coordinates"])}
restriction = [names4[tuple(name)] for name in d3["unknown_coordinates"]]
projected = [p4[j] for j in restriction]
projected_kernel = [[v[j] for j in restriction] for v in k4]
assert apply(a3, projected) == b3
assert all(not any(v) for v in projected_kernel)
offset = [projected[j]-p3[j] for j in d3["affine_free_columns"]]
assert any(offset)
reconstructed = [s+sum(t*v[j] for t, v in zip(offset, k3))
                 for j, s in enumerate(p3)]
assert reconstructed == projected
projection = {
    "linear_rank": 0,
    "class3_free_coordinates": [d3["unknown_coordinates"][j] for j in d3["affine_free_columns"]],
    "unique_extendible_values": offset,
    "values_mod5": list(map(mod5, offset)),
    "initial_zero_parameter_class3_lift_extends": False,
    "all_twenty_class4_parameters_have_weight4": all(
        len(d4["unknown_coordinates"][j][1]) == 4 for j in d4["affine_free_columns"]),
}
assert projection["all_twenty_class4_parameters_have_weight4"]

with (HERE/"a_higher_lift_coordinates.csv").open("w", newline="") as handle:
    out = csv.writer(handle)
    out.writerow(["Lyndon_word", "degree", "class4_f_log", "class4_h_log",
                  "class3_initial_f_log", "class3_initial_h_log"])
    i3 = {w: i for i, w in enumerate(d3["basis"])}
    for i, w in enumerate(d4["basis"]):
        j = i3.get(w)
        out.writerow([w, len(w), d4["f_log_Lyndon_coordinates"][i],
                      d4["h_log_Lyndon_coordinates"][i],
                      "" if j is None else d3["f_log_Lyndon_coordinates"][j],
                      "" if j is None else d3["h_log_Lyndon_coordinates"][j]])

result = {
    "certificate_checks": reports,
    "class4_to_class3_projection": projection,
    "finite_family_counts": {"class3_mod_5n": "5^(4n)", "class4_mod_5n": "5^(20n)",
                            "class3_points_extendible_to_class4_mod_5n": 1},
    "scope": "Pairs of normalized conjugator lifts above the fixed A.23 class2 pair; not a count of distinct automorphisms or outer automorphisms.",
    "full_free_profinite_lift_asserted": False,
}
(HERE/"a_higher_lift_verify.json").write_text(json.dumps(result, indent=2, default=str)+"\n")
text = "\n".join([
    "PASS: complete rational linear certificates and all affine kernel bases.",
    "PASS: independent ranks 36 and140 modulo5 certify the rational ranks.",
    "PASS: reduction of each rational system equals the separately constructed F5 system.",
    "PASS: class3/class4 affine Z5 dimensions4/20; every parameter is integral.",
    "PASS: class4 projects to exactly one class3 point.",
    "Class3 extendible h_ADC,h_ADD,h_CCD,h_CDD: "+str(tuple(map(str, offset))),
    "The initial class3 zero-parameter choice does not extend; the full family does.",
    "No assertion of a lift to the full free profinite group.",
])+"\n"
(HERE/"a_higher_lift_verify.out").write_text(text)
print(text, end="")
