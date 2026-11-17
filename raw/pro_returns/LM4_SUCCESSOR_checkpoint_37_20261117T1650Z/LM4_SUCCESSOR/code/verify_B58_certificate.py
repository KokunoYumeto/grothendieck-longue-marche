#!/usr/bin/env python3
"""Independent integer and permutation verification of the B.58 witness."""
from pathlib import Path
from collections import deque
import json

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "work_DE/rigid7_subsets.json").read_text())
certificate = json.loads((root / "work_DE/ambient_rigid7_abelian_certificate.json").read_text())
identity = tuple(range(12))


def compose(a, b):
    return tuple(a[b[i]] for i in range(12))


def power(a, n):
    answer = identity
    for _ in range(n):
        answer = compose(answer, a)
    return answer


generators = [tuple(p) for p in data["T_permutations"]] + [tuple(data["D_permutation"])]
group = {identity}
queue = deque([identity])
while queue:
    a = queue.popleft()
    for b in generators:
        c = compose(a, b)
        if c not in group:
            group.add(c)
            queue.append(c)
assert len(group) == 60
five_subgroups = {
    frozenset(power(g, j) for j in range(5))
    for g in group if g != identity and power(g, 5) == identity
}
assert len(five_subgroups) == 6
rigid_sets = set()
for subgroup in five_subgroups:
    g = next(x for x in subgroup if x != identity)
    fixed = {i for i in range(12) if g[i] == i}
    assert len(fixed) == 2
    remaining = set(range(12)) - fixed
    orbits = []
    while remaining:
        i = min(remaining)
        orbit = {power(g, j)[i] for j in range(5)}
        assert len(orbit) == 5
        remaining -= orbit
        orbits.append(orbit)
        rigid_sets.add(tuple(sorted(j + 1 for j in fixed | orbit)))
    assert len(orbits) == 2
assert rigid_sets == {tuple(s) for s in data["rigid7"]}
print("PERMUTATION_CHECK: group order60; six order5 subgroups; twelve fixed-pair-plus-pentagon subsets")
print("SUBSET_CHECK: exactly the twelve subsets used in the ambient H1 certificate")

matrix = certificate["forgetful_matrix"]
rows = certificate["independent_row_indices"]
inverse = certificate["unimodular_minor_inverse"]
assert len(matrix) == 168 and all(len(r) == 54 for r in matrix)
assert len(rows) == len(set(rows)) == 54
minor = [matrix[i] for i in rows]
for i in range(54):
    for j in range(54):
        assert sum(inverse[i][k] * minor[k][j] for k in range(54)) == int(i == j)
        assert sum(minor[i][k] * inverse[k][j] for k in range(54)) == int(i == j)
print("INTEGER_CHECK: supplied inverse multiplies the selected54-row minor to identity on both sides")
print("CONCLUSION: the combined forgetful H1 map has an integral left inverse")
print("SCOPE: no nonabelian injectivity or triviality of the residual centralizer is inferred")
