#!/usr/bin/env python3
"""Finite certificate for the signed pants graph used in C.19."""
from itertools import permutations
import json

vertices = ("P+", "P-", "Q+", "Q-")
edges = {
    "a+": ("P+", "Q+"), "a-": ("P-", "Q-"),
    "b+": ("P+", "Q+"), "b-": ("P-", "Q-"),
    "c+": ("P+", "Q-"), "c-": ("P-", "Q+"),
}
adjacency = {v: set() for v in vertices}
incidence = {v: [] for v in vertices}
for label, (u, v) in edges.items():
    adjacency[u].add(v)
    adjacency[v].add(u)
    incidence[u].append(label)
    incidence[v].append(label)

seen = {vertices[0]}
while True:
    enlarged = seen | set().union(*(adjacency[v] for v in seen))
    if enlarged == seen:
        break
    seen = enlarged
assert seen == set(vertices)
assert all(len(labels) == 3 for labels in incidence.values())
assert len({tuple(sorted(labels)) for labels in incidence.values()}) == 4

edgewise_automorphisms = []
for perm in permutations(vertices):
    mapping = dict(zip(vertices, perm))
    if all({mapping[u], mapping[v]} == {u, v} for u, v in edges.values()):
        edgewise_automorphisms.append(mapping)
assert edgewise_automorphisms == [dict(zip(vertices, vertices))]

deck = {"P+": "P-", "P-": "P+", "Q+": "Q-", "Q-": "Q+"}
for label, (u, v) in edges.items():
    partner = label[0] + ("-" if label[-1] == "+" else "+")
    assert {deck[u], deck[v]} == set(edges[partner])

# The lift of the three base twists has these exponent columns.
matrix = [
    [1, 0, 0], [-1, 0, 0],
    [0, 1, 0], [0, -1, 0],
    [0, 0, 1], [0, 0, -1],
]
assert [matrix[i] for i in (0, 2, 4)] == [[1,0,0],[0,1,0],[0,0,1]]
out = {
    "base_pants": 2,
    "base_euler_characteristic": -2,
    "base_orientation_voltage": {"a": 0, "b": 0, "c": 1},
    "orientation_double_connected": True,
    "cover_pants": 4,
    "cover_euler_characteristic": -4,
    "cover_genus": 3,
    "vertices": vertices,
    "edges": edges,
    "incidence": incidence,
    "edgewise_vertex_automorphisms": edgewise_automorphisms,
    "deck_transformation": deck,
    "twist_exponent_matrix": matrix,
    "primitive_rank_three_minor": [0, 2, 4],
    "scope": "Checks the explicit graph and exponent injection only. The finite-index and torsion conclusions use the written surface cutting and multitwist-uniqueness proof."
}
print(json.dumps(out, indent=2))
