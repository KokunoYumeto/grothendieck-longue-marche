#!/usr/bin/env python3
"""The literal 630-state induced capped mixed quotient of M_{0,[10]}.

Input: the checked actual 216-element capped target, with its D,V edges.
Output: all nine generator transitions and weights, the actual sphere
relations, and every pure pair-twist projection and C4 character.

Products use the right-word convention
 (x,sigma)(y,tau)=(x_i*y_sigma(i), tau o sigma).
No finite-pentagon or centralizer-image assertion is made by this program.
"""
from collections import deque
from itertools import combinations
from pathlib import Path
import hashlib
import json
import numpy as np

HERE = Path(__file__).resolve().parent
INPUT = HERE / "check_main_mixed_capping.npz"
data = np.load(INPUT)
edges = np.asarray(data["capped_edges"], dtype=np.int64)
assert edges.shape == (216, 2)
words = [None] * 216
words[0] = ()
todo = deque([0])
while todo:
    i = todo.popleft()
    for k in range(2):
        j = int(edges[i, k])
        if words[j] is None:
            words[j] = words[i] + (k + 1,)
            todo.append(j)
assert all(w is not None for w in words)
table = np.zeros((216, 216), dtype=np.int64)
for j, word in enumerate(words):
    column = np.arange(216)
    for letter in word:
        column = edges[column, letter - 1]
    table[:, j] = column
assert np.array_equal(table[0], np.arange(216))
assert np.array_equal(table[:, 0], np.arange(216))
inverse = np.array([np.flatnonzero(table[i] == 0)[0]
                    for i in range(216)], dtype=np.int64)
assert np.array_equal(table[inverse, np.arange(216)], np.zeros(216))
for k in range(216):
    assert np.array_equal(table[table, k], table[:, table[:, k]])
D, V = (int(j) for j in edges[0])


def mul(*items):
    out = 0
    for item in items:
        out = int(table[out, item])
    return out


def comm(a, b):
    return mul(a, b, inverse[a], inverse[b])


def subgroup(seed):
    seed = tuple(int(x) for x in seed)
    found, pending = {0}, deque([0])
    while pending:
        x = pending.popleft()
        for y in seed:
            z = int(table[x, y])
            if z not in found:
                found.add(z)
                pending.append(z)
    return found


assert mul(D, V, D, V) == 0
assert len(subgroup([D, V])) == 216
D2 = mul(D, D)
pure = subgroup([D2, V])
assert len(pure) == 108
character = np.full(216, -1, dtype=np.int64)
character[0] = 0
pending = deque([0])
while pending:
    i = pending.popleft()
    for generator, value in ((D2, 2), (V, 1)):
        j, target = int(table[i, generator]), int(character[i] + value) % 4
        if character[j] < 0:
            character[j] = target
            pending.append(j)
        else:
            assert character[j] == target
assert set(np.flatnonzero(character >= 0)) == pure
for x in pure:
    for y in pure:
        assert character[table[x, y]] == (character[x] + character[y]) % 4
heisenberg = {int(i) for i in np.flatnonzero(character == 0)}
assert len(heisenberg) == 27
derived = subgroup({comm(x, y) for x in pure for y in pure})
assert derived == heisenberg
center = {x for x in heisenberg
          if all(table[x, y] == table[y, x] for y in heisenberg)}
assert len(center) == 3
assert subgroup({comm(x, y) for x in heisenberg for y in heisenberg}) == center
assert all(mul(x, x, x) == 0 for x in heisenberg)
assert all(mul(V, x, inverse[V]) in heisenberg for x in heisenberg)
V2 = mul(V, V)
assert all(mul(V2, x, inverse[V2], x) in center for x in heisenberg)
print("PASS actual capped216 table and pure108 = Heisenberg27 by C4, with exact character", flush=True)

# Local cosets are the three pairings12|34,13|24,14|23.
# The maps are the induced A.4.26 source maps with cap(DV)^2=1.
local_u_permutation = np.array([0, 2, 1], dtype=np.int64)
local_w_permutation = np.array([1, 0, 2], dtype=np.int64)
local_u_weights = np.array([D, 0, mul(inverse[D], V, D)], dtype=np.int64)
local_w_weights = np.array([0, V, D], dtype=np.int64)


def wreath_product(left, right):
    lp, lw = left
    rp, rw = right
    return rp[lp], table[lw, rw[lp]]


def wreath_inverse(element):
    p, w = element
    ip = np.argsort(p)
    return ip, inverse[w[ip]]


def wreath_word(generators, word):
    size = len(generators[0][0])
    out = (np.arange(size), np.zeros(size, dtype=np.int64))
    inverses = [wreath_inverse(g) for g in generators]
    for letter in word:
        out = wreath_product(out, generators[letter - 1] if letter > 0
                             else inverses[-letter - 1])
    return out


def is_identity(element):
    p, w = element
    return np.array_equal(p, np.arange(len(p))) and not np.any(w)


local = [(local_u_permutation, local_u_weights),
         (local_w_permutation, local_w_weights)]
assert is_identity(wreath_word(local, [1, 2, 1, -2, -1, -2]))
assert is_identity(wreath_word(local, [1, 2] * 3))
print("PASS exact three-state local B3 braid relation and killed center", flush=True)

subsets = list(combinations(range(10), 4))
states = [(S, pairing) for S in subsets for pairing in range(3)]
state_index = {state: i for i, state in enumerate(states)}
assert len(states) == 630
pairings = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
generators = []
local_indices = []
for k in range(9):
    permutation = np.empty(630, dtype=np.int64)
    weights = np.zeros(630, dtype=np.int64)
    recorded = np.zeros(630, dtype=np.int64)
    for index, (S, pairing) in enumerate(states):
        if k in S and k + 1 in S:
            r = S.index(k) + 1
            assert r in (1, 2, 3)
            p, w = local[1 if r == 2 else 0]
            target = (S, int(p[pairing]))
            weights[index] = w[pairing]
            recorded[index] = r
        else:
            target_S = tuple(sorted(k + 1 if x == k else k if x == k + 1 else x
                                    for x in S))
            target = (target_S, pairing)
        permutation[index] = state_index[target]
    assert len(set(permutation.tolist())) == 630
    generators.append((permutation, weights))
    local_indices.append(recorded)
generator_permutations = np.array([g[0] for g in generators])
generator_weights = np.array([g[1] for g in generators])
print("PASS all5670 actual generator state transitions and local weights constructed", flush=True)

relations = []
for i in range(1, 10):
    for j in range(i + 2, 10):
        relations.append(("far_%d_%d" % (i, j), [i, j, -i, -j]))
for i in range(1, 9):
    relations.append(("braid_%d_%d" % (i, i + 1),
                      [i, i + 1, i, -(i + 1), -i, -(i + 1)]))
relations.extend([
    ("sphere", list(range(1, 9)) + [9, 9] + list(range(8, 0, -1))),
    ("full_twist", list(range(1, 10)) * 10),
])
assert len(relations) == 38
relation_outputs = []
for name, word in relations:
    answer = wreath_word(generators, word)
    assert is_identity(answer), name
    relation_outputs.append({"name": name, "word": word,
                             "checked_states": 630,
                             "identity_permutation": True,
                             "identity_weights": True})
print("PASS all28 far,8 adjacent braid and2 global sphere relations in all630 states", flush=True)

# Pairing states are literal labelled pair partitions of each four-set.
# Check the full S10 action, not only the cardinality of its orbit.
for k, (permutation, weights) in enumerate(generators):
    swap = lambda x: k + 1 if x == k else k if x == k + 1 else x
    for index, (S, pairing) in enumerate(states):
        source_pairs = {tuple(sorted((S[a], S[b]))) for a, b in pairings[pairing]}
        target_pairs = {tuple(sorted((swap(a), swap(b)))) for a, b in source_pairs}
        target_S, target_pairing = states[int(permutation[index])]
        actual_pairs = {tuple(sorted((target_S[a], target_S[b])))
                        for a, b in pairings[target_pairing]}
        assert actual_pairs == target_pairs
print("PASS permutation projection is the literal S10 action on labelled pair partitions", flush=True)

pair_words = []
pure_weights = []
pure_characters = []
all_pairs = list(combinations(range(10), 2))
for i, j in all_pairs:
    word = list(range(j, i + 1, -1)) + [i + 1, i + 1] + [-r for r in range(i + 2, j + 1)]
    permutation, weights = wreath_word(generators, word)
    assert np.array_equal(permutation, np.arange(630))
    assert np.all(character[weights] >= 0)
    expected = np.zeros(630, dtype=np.int64)
    for index, (S, pairing) in enumerate(states):
        if i in S and j in S:
            paired = {tuple(sorted((S[a], S[b]))) for a, b in pairings[pairing]}
            expected[index] = 2 if (i, j) in paired else 1
    assert np.array_equal(character[weights], expected), (i, j)
    pair_words.append(word)
    pure_weights.append(weights)
    pure_characters.append(expected)
pure_weights = np.array(pure_weights)
pure_characters = np.array(pure_characters)
projection_orders = []
for index in range(630):
    projection = subgroup(set(pure_weights[:, index].tolist()))
    assert projection == pure
    projection_orders.append(len(projection))
print("PASS all45 literal pure pair twists fix630 states and have the exact C4 edge characters", flush=True)
print("PASS each of630 pure-coordinate projections is the full actual108-element subgroup", flush=True)

result = {
    "scope": "Actual M_0,[10] quotient in capped216 wr S630; all source relations and pure-character maps, no centralizer or finite-pentagon implication asserted.",
    "input_file": str(INPUT), "input_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
    "capped_order": 216, "capped_generator_indices": [D, V],
    "capped_positive_words": words,
    "pure_capped_order": 108, "pure_capped_indices": sorted(pure),
    "pure_character": character.tolist(),
    "heisenberg_indices": sorted(heisenberg), "heisenberg_center_indices": sorted(center),
    "states": [[list(S), pairing + 1] for S, pairing in states],
    "pair_partition_convention": pairings,
    "generator_source_names": ["sigma_%d" % i for i in range(1, 10)],
    "generator_permutations": generator_permutations.tolist(),
    "generator_weights": generator_weights.tolist(),
    "generator_local_indices": np.array(local_indices).tolist(),
    "relation_checks": relation_outputs,
    "pure_pair_labels": all_pairs, "pure_pair_words": pair_words,
    "pure_pair_weights": pure_weights.tolist(),
    "pure_pair_characters": pure_characters.tolist(),
    "pure_coordinate_projection_orders": projection_orders,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
np.savez_compressed(Path(__file__).with_suffix(".npz"),
                    capped_multiplication=table, capped_inverse=inverse,
                    capped_character=character,
                    generator_permutations=generator_permutations,
                    generator_weights=generator_weights,
                    generator_local_indices=np.array(local_indices),
                    pure_pair_weights=pure_weights,
                    pure_pair_characters=pure_characters)
print("PASS complete630-state induced capped quotient certificate", flush=True)
