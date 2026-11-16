"""Exact Cartier certificates for odd Fermat cyclic covers in characteristic 2.

The mathematical derivation of the basis and operator is in AG.11/AG.12.
This program enumerates the entire finite Cartier graph, not sampled points.
"""
from collections import Counter
from math import gcd
import json


def cartier_certificate(n):
    assert n > 1 and n % 2 == 1
    basis = {(a, b) for a in range(1, n) for b in range(1, n - a)}
    inv2 = (n + 1) // 2
    operator = {
        pair: None if pair[0] % 2 and pair[1] % 2
        else ((inv2 * pair[0]) % n, (inv2 * pair[1]) % n)
        for pair in basis
    }
    assert all(target is None or target in basis for target in operator.values())
    assert len(basis) == (n - 1) * (n - 2) // 2
    nonzero_targets = [v for v in operator.values() if v is not None]
    assert len(nonzero_targets) == len(set(nonzero_targets))
    stable = basis
    image_dimensions = [len(stable)]
    while True:
        next_image = {operator[v] for v in stable if operator[v] is not None}
        assert next_image <= stable
        if next_image == stable:
            break
        stable = next_image
        image_dimensions.append(len(stable))
    coherent = Counter((b - a) % n for a, b in basis)
    ranks = Counter((b - a) % n for a, b in stable)
    assert coherent[0] == (n - 1) // 2
    assert all(coherent[i] == (n - 3) // 2 for i in range(1, n))
    assert ranks[0] == 0
    primitive_rank = sum(v for i, v in ranks.items() if gcd(i, n) == 1)
    return {
        "n": n,
        "base_genus": (n - 1) // 2,
        "cover_genus": len(basis),
        "cover_two_rank": len(stable),
        "primitive_two_rank": primitive_rank,
        "successive_Cartier_image_dimensions": image_dimensions,
        "stable_pairs": sorted(stable),
        "coherent_character_multiplicities": dict(sorted(coherent.items())),
        "stable_character_multiplicities": dict(sorted(ranks.items())),
        "full_Cartier_graph": [
            {"basis_pair": pair, "image": operator[pair]}
            for pair in sorted(basis)
        ],
    }


seven = cartier_certificate(7)
assert seven["cover_two_rank"] == seven["primitive_two_rank"] == 6
assert all(seven["stable_character_multiplicities"][i] == 1 for i in range(1, 7))
thirty_five = cartier_certificate(35)
assert thirty_five["cover_two_rank"] == 6
assert thirty_five["primitive_two_rank"] == 0
assert thirty_five["stable_pairs"] == sorted(
    (5 * a, 5 * b) for a, b in seven["stable_pairs"]
)
semiprimitive_examples = []
for n, r in [(5, 2), (9, 3), (11, 5), (13, 6), (17, 4), (33, 5)]:
    assert (2**r + 1) % n == 0
    cert = cartier_certificate(n)
    assert cert["cover_two_rank"] == 0
    semiprimitive_examples.append({
        "n": n, "r": r, "genus": cert["cover_genus"], "two_rank": 0
    })

print(json.dumps({
    "method": "Complete Cartier graph in the adjunction differential basis",
    "seventh_degree_counterexample": seven,
    "thirty_fifth_degree_primitive_only_example": thirty_five,
    "zero_rank_Fermat_examples": semiprimitive_examples,
    "assertions": "all passed",
}, indent=2))
