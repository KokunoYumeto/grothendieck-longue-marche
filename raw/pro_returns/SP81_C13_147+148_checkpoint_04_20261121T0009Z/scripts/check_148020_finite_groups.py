"""Finite, explicit morphisms for the arithmetic group note on 148_scan020.

Only the displayed finite matrix/affine models are checked. No identification
of the manuscript's Teichmueller groups, or source glyph, follows from this.
"""
from itertools import product, permutations
from collections import deque
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]

def mul(a, b, n):
    x, y, z, w = a
    p, q, r, s = b
    return ((x*p+y*r)%n, (x*q+y*s)%n,
            (z*p+w*r)%n, (z*q+w*s)%n)

def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))

def sl(n):
    return [a for a in product(range(n), repeat=4)
            if (a[0]*a[3]-a[1]*a[2])%n == 1]

points = tuple(product(range(2), repeat=2))
mat2, mat4 = sl(2), sl(4)
affine = []
for a in mat2:
    for t in points:
        p = tuple(points.index(((a[0]*x+a[1]*y+t[0])%2,
                                (a[2]*x+a[3]*y+t[1])%2))
                  for x, y in points)
        affine.append((a, t, p))
assert len(mat2) == 6 and len(mat4) == 48
assert {p for a, t, p in affine} == set(permutations(range(4)))
for a, t, p in affine:
    for b, u, q in affine:
        c = mul(a, b, 2)
        v = ((a[0]*u[0]+a[1]*u[1]+t[0])%2,
             (a[2]*u[0]+a[3]*u[1]+t[1])%2)
        image = next(r for d, w, r in affine if d == c and w == v)
        assert compose(p, q) == image

nonzero = points[1:]
linear = {a: tuple(nonzero.index(((a[0]*x+a[1]*y)%2,
                                   (a[2]*x+a[3]*y)%2))
                   for x, y in nonzero) for a in mat2}
assert set(linear.values()) == set(permutations(range(3)))
assert all(linear[mul(a, b, 2)] == compose(linear[a], linear[b])
           for a in mat2 for b in mat2)

def cls(a):
    return min(a, tuple((-x)%4 for x in a))

classes = sorted({cls(a) for a in mat4})
identity = cls((1, 0, 0, 1))
s = cls((0, 3, 1, 0))
t = cls((1, 1, 0, 1))
image_s = (1, 0, 2, 3)
image_t = (1, 2, 3, 0)
images = {identity: (0, 1, 2, 3)}
words = {identity: ""}
queue = deque([identity])
while queue:
    a = queue.popleft()
    for g, p, label in [(s, image_s, "S"), (t, image_t, "T")]:
        b = cls(mul(a, g, 4))
        q = compose(images[a], p)
        if b in images:
            assert images[b] == q
        else:
            images[b], words[b] = q, words[a]+label
            queue.append(b)
assert set(images) == set(classes)
assert len(classes) == 24
assert set(images.values()) == set(permutations(range(4)))
assert all(images[cls(mul(a, b, 4))] == compose(images[a], images[b])
           for a in classes for b in classes)

reduction = {a: tuple(x%2 for x in a) for a in classes}
assert set(reduction.values()) == set(mat2)
assert all(reduction[cls(mul(a, b, 4))] == mul(reduction[a], reduction[b], 2)
           for a in classes for b in classes)
kernel = [a for a in classes if reduction[a] == (1, 0, 0, 1)]
assert len(kernel) == 4
assert all(cls(mul(a, a, 4)) == identity for a in kernel)

matchings = (((0,1),(2,3)), ((0,2),(1,3)), ((0,3),(1,2)))
def pair_key(m):
    return tuple(sorted(tuple(sorted(pair)) for pair in m))
def action_matching(p):
    return tuple(matchings.index(pair_key(tuple(tuple(p[v] for v in pair)
                                                for pair in m)))
                 for m in matchings)
matching_images = {a: action_matching(images[a]) for a in classes}
assert [a for a in classes if matching_images[a] == (0,1,2)] == kernel
# Explicit relabeling between the three pair partitions and three nonzero vectors.
relabelings = []
for f in permutations(range(3)):
    if all(tuple(f[matching_images[a][i]] for i in range(3)) ==
           tuple(linear[reduction[a]][f[i]] for i in range(3)) for a in classes):
        relabelings.append(f)
assert len(relabelings) == 1

result = {
    "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
    "F2_points_in_order": points,
    "affine_action_full_table": [{"matrix":a,"translation":t,"permutation":p}
                                 for a,t,p in affine],
    "affine_action_all_576_products_verified": True,
    "nonzero_points_in_order": nonzero,
    "linear_action_full_table": [{"matrix":a,"permutation":p} for a,p in linear.items()],
    "linear_action_all_36_products_verified": True,
    "SL2_Z4_cardinality": len(mat4),
    "quotient_by_plus_minus_I_cardinality": len(classes),
    "quotient_generators": {"S":{"matrix":s,"image":image_s},
                            "T":{"matrix":t,"image":image_t}},
    "quotient_isomorphism_full_table": [{"class_representative":a,"word":words[a],
                                         "permutation":images[a]} for a in classes],
    "quotient_all_576_products_verified": True,
    "reduction_all_576_products_verified": True,
    "reduction_kernel": kernel,
    "pair_partitions_in_order": matchings,
    "pair_partition_to_nonzero_point_indices": relabelings[0],
    "kernel_permutations": [images[a] for a in kernel],
    "scope": "Explicit finite affine, matrix and pair-partition actions only. No identification of manuscript curve or Teichmueller groups; no uncertain glyph selected."
}
(root/"work/148020_finite_groups_check.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2)+"\n")
print(json.dumps({"checked_at":result["checked_at"],"SL2_Z4":len(mat4),
                  "quotient":len(classes),"kernel_permutations":result["kernel_permutations"],
                  "relabeling":relabelings[0],"all_product_checks_passed":True}))
