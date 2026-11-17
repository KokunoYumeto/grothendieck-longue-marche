#!/usr/bin/env python3
"""Exact central refinement of the actual 432-element mixed-braid image.

The only input is the two saved 52x52 matrices.  All 432 elements, their
literal positive words and generator transitions are independently rebuilt.
The cyclic join and its central quotient are then computed as finite sets.
"""
from collections import deque
import hashlib
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
INPUT = HERE.parent / 'tower_code' / 'local_mixed_quaternion_census.npz'
data = np.load(INPUT)
generators = np.asarray(data['mixed_matrices'], dtype=np.int64) % 3
dimension = generators.shape[1]
identity = np.eye(dimension, dtype=np.int64)


def key(matrix):
    return np.asarray(matrix, dtype=np.uint8).tobytes()


elements = [identity]
words = [()]
indices = {key(identity): 0}
edges = []
position = 0
while position < len(elements):
    row = []
    for letter, generator in enumerate(generators, 1):
        matrix = elements[position] @ generator % 3
        encoded = key(matrix)
        if encoded not in indices:
            indices[encoded] = len(elements)
            elements.append(matrix)
            words.append(words[position] + (letter,))
        row.append(indices[encoded])
    edges.append(row)
    position += 1
assert len(elements) == 432
edges = np.asarray(edges, dtype=np.int32)
print('PASS independent mixed-image census:432 matrices', flush=True)


def evaluate(word, start=0):
    for letter in word:
        start = int(edges[start, letter - 1])
    return start


z_word = (1, 2, 1, 2)
z_index = evaluate(z_word)
z_matrix = elements[z_index]
assert all(np.array_equal(z_matrix @ g % 3, g @ z_matrix % 3) for g in generators)
z_powers = [0]
current = z_index
while current:
    z_powers.append(current)
    current = evaluate(z_word, current)
assert len(z_powers) == 6
n = len(z_powers)
modulus = 2 * n
z_translation = np.array([evaluate(z_word, i) for i in range(432)], dtype=np.int32)
print('PASS z=(DV)^2 is central of exact order6', flush=True)

# Join q with chi(u)=1, chi(v)=0 modulo12.
joined = [(0, 0)]
join_words = [()]
join_index = {(0, 0): 0}
join_edges = []
position = 0
while position < len(joined):
    q_element, coordinate = joined[position]
    row = []
    for j in range(2):
        target = (int(edges[q_element, j]), (coordinate + (j == 0)) % modulus)
        if target not in join_index:
            join_index[target] = len(joined)
            joined.append(target)
            join_words.append(join_words[position] + (j + 1,))
        row.append(join_index[target])
    join_edges.append(row)
    position += 1
assert len(joined) == 1296
join_edges = np.asarray(join_edges, dtype=np.int32)
assert all(sum(q == i for q, c in joined) == 3 for i in range(432))
print('PASS cyclic join order1296, with three lifts of every mixed element', flush=True)


def central_next(index):
    q_element, coordinate = joined[index]
    return join_index[(int(z_translation[q_element]), (coordinate + 2) % modulus)]


quotient = np.full(len(joined), -1, dtype=np.int32)
cosets = []
for initial in range(len(joined)):
    if quotient[initial] >= 0:
        continue
    orbit, current = [], initial
    while not orbit or current != initial:
        assert current not in orbit
        orbit.append(current)
        current = central_next(current)
    assert len(orbit) == n
    assert len({joined[i][1] for i in orbit}) == n
    for i in orbit:
        quotient[i] = len(cosets)
    cosets.append(orbit)
assert len(cosets) == 216
quotient_edges = np.array([[int(quotient[join_edges[c[0], j]]) for j in range(2)]
                           for c in cosets], dtype=np.int32)
for i in range(len(joined)):
    for j in range(2):
        assert quotient[join_edges[i, j]] == quotient_edges[quotient[i], j]
for start in range(216):
    current = start
    for letter in z_word:
        current = int(quotient_edges[current, letter - 1])
    assert current == start
print('PASS capped image order216, exact generator maps, and (uv)^2=1', flush=True)


def finite_word(edges_here, word, start=0):
    for letter in word:
        start = int(edges_here[start, letter - 1])
    return start


def element_order(edges_here, word):
    current, order = finite_word(edges_here, word), 1
    while current:
        current = finite_word(edges_here, word, current)
        order += 1
    return order


assert element_order(quotient_edges, (1,)) == 12
assert element_order(quotient_edges, (2,)) == 4
assert element_order(quotient_edges, (1, 2)) == 2

# Retain both colored readings simultaneously.  This is an actual
# quotient of R_0=<u,v|(uv)^2=1> with the swap u<->v as an automorphism.
symmetric = [(0, 0)]
symmetric_index = {(0, 0): 0}
symmetric_edges = []
position = 0
while position < len(symmetric):
    left, right = symmetric[position]
    row = []
    for j in range(2):
        target = (int(quotient_edges[left, j]), int(quotient_edges[right, 1 - j]))
        if target not in symmetric_index:
            symmetric_index[target] = len(symmetric)
            symmetric.append(target)
        row.append(symmetric_index[target])
    symmetric_edges.append(row)
    position += 1
symmetric_edges = np.asarray(symmetric_edges, dtype=np.int32)
swap = np.array([symmetric_index[(right, left)] for left, right in symmetric], dtype=np.int32)
assert len(symmetric) == 648
assert all(swap[swap[i]] == i for i in range(len(symmetric)))
for i in range(len(symmetric)):
    for j in range(2):
        assert swap[symmetric_edges[i, j]] == symmetric_edges[swap[i], 1 - j]
assert len({x for x, y in symmetric}) == len({y for x, y in symmetric}) == 216
assert element_order(symmetric_edges, (1,)) == element_order(symmetric_edges, (2,)) == 12
assert element_order(symmetric_edges, (1, 2)) == 2
print('PASS symmetric colored target order648 with both216 projections and literal swap', flush=True)

# Form the full432 multiplication and inverse tables from recorded source
# words, then independently compute the derived subgroup and its commutator.
multiplication = np.zeros((432, 432), dtype=np.int32)
for j, word in enumerate(words):
    for i in range(432):
        multiplication[i, j] = evaluate(word, i)
inverse = np.array([int(np.flatnonzero(multiplication[i] == 0)[0]) for i in range(432)])


def multiply(*factors):
    result = 0
    for factor in factors:
        result = int(multiplication[result, factor])
    return result


def commutator(left, right):
    return multiply(left, right, inverse[left], inverse[right])


def generated(seed):
    seed = tuple(seed)
    known = {0}
    todo = deque([0])
    while todo:
        current = todo.popleft()
        for generator in seed:
            target = multiply(current, generator)
            if target not in known:
                known.add(target)
                todo.append(target)
    return known


derived = generated({commutator(i, j) for i in range(432) for j in range(432)})
assert len(derived) == 27
derived_commutator = generated({commutator(i, j) for i in derived for j in derived})
assert len(derived_commutator) == 3
assert all(multiply(i, i, i) == 0 for i in derived)
assert all(multiply(c, i) == multiply(i, c) for c in derived_commutator for i in derived)
assert all((i, 0) in join_index for i in derived)
derived_quotient = {int(quotient[join_index[(i, 0)]]) for i in derived}
assert len(derived_quotient) == 27
print('PASS full Heisenberg27 derived subgroup injects into capped216', flush=True)

# On the kernel of the added character, the cap has zero kernel.  Thus
# the mixed TA.2 defect, which has zero u,v exponent sums, is detected
# without losing the central order-three coordinate.
assert [i for i in cosets[0] if joined[i][1] == 0] == [0]
print('PASS central cap is injective on the zero-character kernel', flush=True)

json_result = {
    'scope': 'Actual central refinement of the mixed432 target; exact C2*Z quotient and zero-character recovery, no finite pentagon implication asserted.',
    'input': str(INPUT),
    'input_sha256': hashlib.sha256(INPUT.read_bytes()).hexdigest(),
    'mixed_order': 432,
    'mixed_generator_names': ['D', 'V'],
    'mixed_words': words,
    'central_word': z_word,
    'central_index': z_index,
    'central_order': n,
    'character_modulus': modulus,
    'character_values': [1, 0],
    'joined_order': len(joined),
    'joined_coordinates': joined,
    'joined_words': join_words,
    'capped_order': len(cosets),
    'capped_generator_orders': [12, 4],
    'central_cosets': cosets,
    'symmetric_colored_order': len(symmetric),
    'symmetric_colored_coordinates': symmetric,
    'symmetric_swap': swap.tolist(),
    'mixed_derived_indices': sorted(derived),
    'mixed_second_derived_indices': sorted(derived_commutator),
    'capped_derived_order': len(derived_quotient),
    'mixed_defect_u_v_exponent_sums': [0, 0],
}
Path(__file__).with_suffix('.json').write_text(json.dumps(json_result, indent=2) + '\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),
                    mixed_matrices=np.asarray(elements, dtype=np.uint8),
                    mixed_edges=edges, multiplication=multiplication,
                    joined_edges=join_edges, quotient_map=quotient,
                    capped_edges=quotient_edges, symmetric_edges=symmetric_edges,
                    symmetric_swap=swap)
print('PASS complete finite central-refinement certificate', flush=True)
