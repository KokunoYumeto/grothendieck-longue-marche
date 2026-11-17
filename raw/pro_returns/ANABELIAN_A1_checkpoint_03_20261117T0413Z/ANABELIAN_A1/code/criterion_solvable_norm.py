"""Exhaustive Q8-module checks of the solvable norm theorem.
The nonconstant Frobenius has order three in characteristic three.
All subgroups and all vectors are enumerated independently.
"""
from itertools import product, permutations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
p = 3
I = (1, 0, 0, 1)
i = (0, 1, 2, 0)
j = (1, 1, 1, 2)
phi = (1, 1, 0, 1)


def mm(A, B):
    return tuple(sum(A[2*r+h]*B[2*h+s] for h in range(2)) % p
                 for r in range(2) for s in range(2))


def mv(A, v):
    return tuple(sum(A[2*r+s]*v[s] for s in range(2)) % p for r in range(2))


minus = lambda A: tuple(-a % p for a in A)
assert mm(i, i) == mm(j, j) == minus(I)
assert mm(i, j) == minus(mm(j, i))
assert mm(mm(phi, phi), phi) == I
group = []
labels = {}
for a, b, sign in product(range(2), repeat=3):
    A = mm(i if a else I, j if b else I)
    if sign:
        A = minus(A)
    group.append(A)
    labels[A] = (a, b, sign)
assert len(set(group)) == 8
index = {A: n for n, A in enumerate(group)}
identity = index[I]
table = [[index[mm(A, B)] for B in group] for A in group]
inverse = [next(b for b in range(8) if table[a][b] == identity) for a in range(8)]
phi_inverse = mm(phi, phi)
sigma = [index[mm(mm(phi, A), phi_inverse)] for A in group]
assert sorted(sigma) == list(range(8))


def generated(seed):
    H = set(seed) | {identity}
    changed = True
    while changed:
        new = {table[a][b] for a in H for b in H}
        changed = not new <= H
        H.update(new)
    return frozenset(H)


subgroups = set()
for bits in product(range(2), repeat=8):
    selected = frozenset(n for n, bit in enumerate(bits) if bit)
    if identity in selected and generated(selected) == selected:
        subgroups.add(selected)
normals = sorted([H for H in subgroups if all(
    table[table[g][h]][inverse[g]] in H for g in range(8) for h in H)],
    key=lambda H: (len(H), sorted(H)))
assert len(subgroups) == len(normals) == 6
chars = [(1, 0), (0, 1), (1, 1)]


def character(c, g):
    a, b, _ = labels[group[g]]
    return pow(2, c[0]*a+c[1]*b, 3)


permutation = next(perm for perm in permutations(range(3)) if all(
    character(chars[perm[r]], g) == character(chars[r], sigma[g])
    for r in range(3) for g in range(8)))


def action(g, v, module):
    out = []
    offset = 0
    if module in ("natural", "full"):
        out.extend(mv(group[g], v[:2]))
        offset = 2
    if module in ("characters", "full"):
        out.extend(character(c, g)*v[offset+r] % p for r, c in enumerate(chars))
    return tuple(out)


def frobenius(v, module, nonconstant):
    if not nonconstant:
        return v
    out = []
    offset = 0
    if module in ("natural", "full"):
        out.extend(mv(phi, v[:2]))
        offset = 2
    if module in ("characters", "full"):
        out.extend(v[offset+permutation[r]] for r in range(3))
    return tuple(out)


def norm(H, v, module):
    values = [action(h, v, module) for h in H]
    return tuple(sum(col) % p for col in zip(*values))


def stabilizer(v, module):
    return frozenset(g for g in range(8) if action(g, v, module) == v)


records = []
for module, dimension in (("natural", 2), ("characters", 3), ("full", 5)):
    vectors = list(product(range(p), repeat=dimension))
    for nonconstant in (False, True):
        if nonconstant:
            assert all(frobenius(action(g, v, module), module, True) ==
                       action(sigma[g], frobenius(v, module, True), module)
                       for g in range(8) for v in vectors)
        fixed = [v for v in vectors if frobenius(v, module, nonconstant) == v]
        tests = []
        for H in normals:
            common = frozenset.intersection(*(stabilizer(norm(H, v, module), module) for v in fixed))
            tests.append({"H_indices": sorted(H), "quotient_order": 8//len(H),
                          "common_stabilizer_indices": sorted(common), "exact": common == H})
        free = [v for v in fixed if all(stabilizer(norm(H, v, module), module) == H for H in normals)]
        assert bool(free) == all(t["exact"] for t in tests)
        records.append({"module": module, "dimension": dimension,
                        "nonconstant_Frobenius": nonconstant,
                        "fixed_count": len(fixed), "all_norm_free_count": len(free),
                        "example": free[0] if free else None, "normal_subgroup_tests": tests})
full = [r for r in records if r["module"] == "full"]
assert [(r["fixed_count"], r["all_norm_free_count"]) for r in full] == [(243, 64), (9, 4)]
assert all(r["all_norm_free_count"] == 0 for r in records if r["module"] != "full")
result = {"verified": True, "group": "Q8", "characteristic": p,
          "group_elements": group, "labels_a_b_sign": [labels[A] for A in group],
          "multiplication_table": table, "Frobenius_matrix": phi,
          "Frobenius_order": 3, "Frobenius_on_group": sigma,
          "Frobenius_on_character_components": permutation,
          "scope": "Finite-module verification; no claimed Jacobian realization", "tests": records}
(ROOT / "criterion_solvable_norm.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({"verified": True, "Frobenius_order": 3,
                  "characteristic": 3, "character_permutation": permutation,
                  "tests": [{k:r[k] for k in ("module", "nonconstant_Frobenius", "fixed_count", "all_norm_free_count")} for r in records]}, indent=2))
