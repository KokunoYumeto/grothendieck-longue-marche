"""Exact mod-two pure-sphere label test for the genus-two quotient square."""

from itertools import combinations, permutations
from pathlib import Path
import json

edges5 = list(combinations(range(1, 6), 2))
positions = {edge: i for i, edge in enumerate(edges5)}
full_twist = (1 << len(edges5)) - 1


def reduce_vector(v):
    # P Gamma_{0,6}=P_5/Z(P_5); the central full twist has all ten coordinates 1.
    if v & (1 << 9):
        v ^= full_twist
    assert v < 1 << 9
    return v


def pair_vector(i, j):
    i, j = sorted((i, j))
    if j <= 5:
        return reduce_vector(1 << positions[(i, j)])
    # The spherical peripheral relation gives e_{i6}=-sum_{j!=i, j<=5} e_{ij}.
    v = 0
    for k in range(1, 6):
        if k != i:
            v ^= 1 << positions[tuple(sorted((i, k)))]
    return reduce_vector(v)


edges6 = list(combinations(range(1, 7), 2))
vectors = {edge: pair_vector(*edge) for edge in edges6}
assert 0 not in vectors.values() and len(set(vectors.values())) == 15
inside = {1, 2, 3}
inside_edges = list(combinations(sorted(inside), 2))
span = {0}
for edge in inside_edges:
    span |= {v ^ vectors[edge] for v in tuple(span)}
assert len(span) == 8
intersection = [edge for edge in edges6 if vectors[edge] in span]
assert intersection == inside_edges
survivors = []
for perm in permutations(range(1, 7)):
    image = lambda edge: tuple(sorted(perm[i - 1] for i in edge))
    passes = vectors[image((1, 2))] in span and vectors[image((2, 3))] in span
    preserves = {perm[i - 1] for i in inside} == inside
    assert passes == preserves
    if passes:
        survivors.append(perm)
assert len(survivors) == 36
result = {
    "pure_homology_dimension": 9,
    "coordinate_edges_before_full_twist_quotient": edges5,
    "removed_coordinate": edges5[-1],
    "pair_vectors_as_nine_bit_integers": {f"{i}{j}": v for (i, j), v in vectors.items()},
    "first_triple_span_dimension": 3,
    "pair_vectors_in_first_triple_span": intersection,
    "permutations_checked": 720,
    "two_adjacent_pair_test_survivors": len(survivors),
    "survivor_group": "S3 on {1,2,3} times S3 on {4,5,6}",
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print("PASS: all 15 labelled pair vectors are distinct and nonzero in F2^9.")
print("PASS: the first-triple span contains exactly the pair vectors 12,13,23.")
print("PASS: all 720 permutations checked; the two-adjacent-pair test gives exactly S3 x S3 (36 elements).")
