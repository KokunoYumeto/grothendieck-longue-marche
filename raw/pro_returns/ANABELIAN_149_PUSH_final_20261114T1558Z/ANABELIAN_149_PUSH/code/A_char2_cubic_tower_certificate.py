#!/usr/bin/env python3
"""Exact F_3^4/group-ring checks for the first cubic genus-two tower."""
from itertools import product
from pathlib import Path
import json

G = list(product(range(3), repeat=4))
zero = (0, 0, 0, 0)
index = {g: i for i, g in enumerate(G)}

def add(a, b):
    return tuple((x + y) % 3 for x, y in zip(a, b))

def neg(a):
    return tuple(-x % 3 for x in a)

def dot(a, b):
    return sum(x * y for x, y in zip(a, b)) % 3

reps = [a for a in G if a != zero and next(x for x in a if x) == 1]
planes = [{g for g in G if dot(a, g) == 0} for a in reps]
assert len(reps) == len(planes) == 40
assert all(len(K) == 27 for K in planes)
assert all(len(K & L) == 9 for i, K in enumerate(planes)
           for L in planes[i + 1:])
incidences = [sum(g in K for K in planes) for g in G]
assert incidences[0] == 40
assert all(v == 13 for v in incidences[1:])

# These are 81*(e_K-e_G), and 81*e_G, as integer group-ring vectors.
vG = [1] * 81
vectors = [[3 * int(g in K) - 1 for g in G] for K in planes]
sums = [vG[j] + sum(v[j] for v in vectors) for j in range(81)]
assert sums == [81] + [0] * 80
sum_index = [[index[add(a, b)] for b in G] for a in G]

def conv(a, b):
    ans = [0] * 81
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    ans[sum_index[i][j]] += ai * bj
    return ans

assert conv(vG, vG) == [81] * 81
assert all(conv(vG, v) == [0] * 81 for v in vectors)
for i, vi in enumerate(vectors):
    for j, vj in enumerate(vectors[i:], i):
        expected = [81 * a for a in vi] if i == j else [0] * 81
        assert conv(vi, vj) == expected

pairs = [{a, neg(a)} for a in reps]
assert set.union(*pairs) == set(G) - {zero}
assert sum(map(len, pairs)) == 80
assert set.intersection(*planes) == {zero}
fixed_counts = []
for c in G:
    fixed = [g for g in G if add(c, neg(g)) == g]
    fixed_counts.append(len(fixed))
assert fixed_counts == [1] * 81

out = {
    "status": "PASS",
    "group": "(Z/3)^4",
    "group_order": 81,
    "hyperplanes": 40,
    "hyperplane_order": 27,
    "distinct_hyperplane_intersection_order": 9,
    "nonzero_element_hyperplane_incidence": 13,
    "orthogonal_idempotent_factors": 41,
    "integer_convolution_checks": 861,
    "nonzero_character_pairs": 40,
    "common_character_kernel_order": 1,
    "affine_inversions_checked": 81,
    "fixed_points_per_affine_inversion": 1,
    "base_genus": 2,
    "cover_genus": 82,
    "factor_dimension_sum": 2 + 40 * 2,
    "reflection_quotient_genus": (2 * 82 - 2 - 6 + 4) // 4,
    "limitations": "Group-ring certificate; actual Jacobian identification and ordinariness use the accompanying proof and A.C2.2."
}
assert out["reflection_quotient_genus"] == 40
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
