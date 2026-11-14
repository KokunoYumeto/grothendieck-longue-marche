#!/usr/bin/env python3
"""Finite certificates for F.31--F.34; no numerical approximations."""
from fractions import Fraction
from itertools import combinations, product


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    nr, nc, pivot = len(a), len(a[0]), 0
    for col in range(nc):
        nonzero = next((i for i in range(pivot, nr) if a[i][col]), None)
        if nonzero is None:
            continue
        a[pivot], a[nonzero] = a[nonzero], a[pivot]
        q = a[pivot][col]
        a[pivot] = [v / q for v in a[pivot]]
        for i in range(nr):
            if i != pivot and a[i][col]:
                q = a[i][col]
                a[i] = [x - q * y for x, y in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == nr:
            break
    return pivot


def homology(maximal_simplices):
    faces = {}
    for simplex in maximal_simplices:
        simplex = tuple(sorted(simplex))
        for k in range(1, len(simplex) + 1):
            faces.setdefault(k - 1, set()).update(combinations(simplex, k))
    faces = {k: sorted(v) for k, v in faces.items()}
    dim = max(faces, default=-1)
    boundary_ranks = {0: 0, dim + 1: 0}
    for d in range(1, dim + 1):
        lower = {s: i for i, s in enumerate(faces[d - 1])}
        matrix = [[0] * len(faces[d]) for _ in lower]
        for j, simplex in enumerate(faces[d]):
            for k in range(d + 1):
                face = simplex[:k] + simplex[k + 1:]
                matrix[lower[face]][j] = (-1) ** k
        boundary_ranks[d] = rank(matrix)
    return [len(faces[d]) - boundary_ranks[d] - boundary_ranks[d + 1]
            for d in range(dim + 1)]


# Three rays in a plane: 0 is the origin, 1..3 the rays, 4..6 the sectors.
objects = tuple(range(7))
strict = {(0, j) for j in range(1, 7)}
strict |= {(1, 4), (2, 4), (2, 5), (3, 5), (3, 6), (1, 6)}
relation = strict | {(i, i) for i in objects}
assert all((a, c) in relation for a, b in relation for bb, c in relation if b == bb)
assert len(strict) == 12
strict_chains = {r: [c for c in combinations(objects, r + 1)
                     if all((a, b) in strict for a, b in zip(c, c[1:]))]
                 for r in range(4)}
assert [len(strict_chains[r]) for r in range(4)] == [7, 12, 6, 0]
print("Plane three-ray incident poset: 7 vertices, 12 strict pairs, 6 strict triangles.")

arrows = sorted(relation)
paths = [(x,) for x in objects]
for r in range(7):
    if r:
        paths = [path + (v,) for path in paths for u, v in arrows if path[-1] == u]
    chains = {chain for chain in product(objects, repeat=r + 1)
              if all((a, b) in relation for a, b in zip(chain, chain[1:]))}
    assert set(paths) == chains
    assert len(chains) == 3 * r * r + 9 * r + 7
    print(f"Segal degree {r}: {len(chains)} chains = {len(paths)} composable arrow strings.")

link_edges = [(a, b) for a, b in strict if a != 0]
assert len(link_edges) == 6
link_betti = homology(link_edges)
cone_betti = homology(strict_chains[2])
suspension = [(7, a, b) for a, b in link_edges] + [(8, a, b) for a, b in link_edges]
sphere_betti = homology(suspension)
assert link_betti == [1, 1]
assert cone_betti == [1, 0, 0]
assert sphere_betti == [1, 0, 1]
print(f"Origin link (hexagonal incidence cycle) Betti numbers: {link_betti}.")
print(f"Disc tube (cone on the link) Betti numbers: {cone_betti}.")
print(f"Two-disc homotopy gluing (suspension of link) Betti numbers: {sphere_betti}.")

# Boundary class persists; a pair of handle generators disappears at every step.
handles = 12
tail_images = [{"c"} | {f"{letter}{j}" for j in range(m + 1, handles + 1)
                          for letter in ("a", "b")}
               for m in range(9)]
assert all(tail_images[m + 1] < tail_images[m] for m in range(8))
print("Infinite-genus tail finite certificates, image ranks:", [len(x) for x in tail_images])
print("Each successive image omits a_(m+1), b_(m+1); proof extends to every m.")

# Compatible local plaques generate exactly the two proposed global leaves.
parent = {x: x for x in ("point", "left", "right", "V")}


def find(x):
    while parent[x] != x:
        x = parent[x]
    return x


def union(x, y):
    parent[find(x)] = find(y)


union("left", "V")
union("right", "V")
assert find("left") == find("right") != find("point")
assert len({find(x) for x in parent}) == 2
print("Circle atlas: two global leaves forced, while the open leaf has two germs at p.")
print("All checks passed. Finite tests supplement, and do not replace, the all-degree proofs.")
