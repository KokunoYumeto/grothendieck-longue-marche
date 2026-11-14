#!/usr/bin/env python3
"""Ordinary peripheral obstruction from the9-versus6 A6 Nielsen families.

Use the actual common-Out fibre products.  All fifteen source kernels
are separated on ker(F2->C2^2) by saved literal relators.  The full
12-coordinate conjugators and complete centralizer-image unions are
computed.  Large product generation then follows from the exact simple
subdirect-product argument, not an infeasible group enumeration.
"""

from collections import deque
from itertools import combinations
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('finite_count', HERE/'a_peripheral_count.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def main():
    raw = json.loads(HERE.joinpath('a_peripheral_a6_outer.json').read_text())
    nielsen = json.loads(HERE.joinpath('a_peripheral_a6_nielsen.json').read_text())
    pairs = [tuple(p) for p in raw['automorphism_generator_pairs']]
    maps = {p: tuple(v) for p, v in zip(pairs, raw['automorphism_maps'])}
    a, b = raw['A6_generators']
    G = module.Group('Aut(A6)', pairs,
                     lambda x, y: (maps[x][y[0]], maps[x][y[1]]), (a, b))
    inner = frozenset(raw['inner_indices'])
    outer = raw['outer_coordinates']
    classes = [frozenset(c) for c in raw['relative_classes']]
    class_of = {g: i for i, c in enumerate(classes) for g in c}
    high = [tuple(t) for t in nielsen['profiles'][0]['proper_orbit_representatives']]
    low = [tuple(t) for t in nielsen['profiles'][1]['proper_orbit_representatives']]
    assert len(high) == 9 and len(low) == 6
    all_triples = high+low
    assert all(t[0] == 0 and len(G.generated(t[:2])) == 1440
               and G.mul[G.mul[t[0]][t[1]]][t[2]] == G.one
               and [outer[g] for g in t] == [1, 2, 3] for t in all_triples)
    assert all([class_of[g] for g in t] == [0, 7, 5] for t in high)
    assert all([class_of[g] for g in t] == [0, 7, 9] for t in low)

    def evaluate(word, triple):
        value = G.one
        for letter in word:
            image = triple[abs(letter)-1]
            value = G.mul[value][image if letter > 0 else G.inv[image]]
        return value

    def inverse_word(word):
        return [-x for x in reversed(word)]

    def witness(first, second):
        """A Cayley-tree edge relation in ker(first), not ker(second)."""
        tree = {G.one: []}
        shadows = {G.one: G.one}
        todo = deque([G.one])
        while todo:
            g = todo.popleft()
            for letter in (1, 2, -1, -2):
                u, v = first[abs(letter)-1], second[abs(letter)-1]
                if letter < 0:
                    u, v = G.inv[u], G.inv[v]
                h = G.mul[g][u]
                target = G.mul[shadows[g]][v]
                if h not in tree:
                    tree[h] = tree[g]+[letter]
                    shadows[h] = target
                    todo.append(h)
                elif shadows[h] != target:
                    word = tree[g]+[letter]+inverse_word(tree[h])
                    assert evaluate(word, first) == G.one
                    assert evaluate(word, second) != G.one
                    assert outer[evaluate(word, second)] == 0
                    parity = 0
                    for x in word:
                        parity ^= 1 if abs(x) == 1 else 2
                    assert parity == 0
                    return word
        raise AssertionError('The two literal source kernels unexpectedly coincide')

    witnesses = []
    for i, j in combinations(range(15), 2):
        word = witness(all_triples[i], all_triples[j])
        witnesses.append({'i': i, 'j': j, 'word': word,
                          'first_value': evaluate(word, all_triples[i]),
                          'second_value': evaluate(word, all_triples[j])})
    assert len(witnesses) == 105
    print('PASS: all15 actual source epimorphisms; all105 K-kernel differences have literal relator witnesses')

    base = [t for pair in zip(high[:6], low) for t in pair]
    original = [high[6]]+base
    base_swap = [i ^ 1 for i in range(12)]
    swapped = [base[i] for i in base_swap]
    assert len(base) == 12 and all(base_swap[base_swap[i]] == i for i in range(12))
    h = [[], [], []]
    h[0] = [G.one]*12
    for j in range(6):
        even = next(g for g in inner if G.conjugate(g, high[j][1]) == low[j][1])
        odd_outer = next(g for g in range(G.size) if outer[g] == 1
                         and G.conjugate(g, high[j][2]) == low[j][2])
        h[1] += [even, G.inv[even]]
        h[2] += [odd_outer, G.inv[odd_outer]]
    assert all({outer[g] for g in row} == {bit} for row, bit in zip(h, (0, 0, 1)))
    assert all(G.conjugate(h[i][j], base[j][i]) == swapped[j][i]
               for i in range(3) for j in range(12))
    print('PASS: actual12-coordinate conjugators have common outer coordinates0,0,1 and realize the pair-swap')

    # Compute the whole base-centralizer image, with actual product
    # centralizers witnessing both possible values in each peripheral.
    centralizer_records = []
    for i in range(3):
        coordinate_centralizers = [G.centralizer(t[i]) for t in base]
        images = [{outer[g] for g in C} for C in coordinate_centralizers]
        intersection = set.intersection(*images)
        assert intersection == {0, i+1}
        actual_vectors = []
        for bit in sorted(intersection):
            vector = [next(g for g in C if outer[g] == bit) for C in coordinate_centralizers]
            assert all(G.conjugate(vector[j], base[j][i]) == base[j][i] for j in range(12))
            actual_vectors.append({'outer': bit, 'coordinates': vector})
        new_outer_coset = {x ^ (1 if i == 2 else 0) for x in intersection}
        first_class_union = {
            class_of[G.conjugate(g, high[6][i])]
            for g in range(G.size) if outer[g] in new_outer_coset
        }
        assert first_class_union == {[0, 7, 9][i]}
        old_class_union = {
            class_of[G.conjugate(g, high[6][i])]
            for g in range(G.size) if outer[g] in intersection
        }
        assert old_class_union == {[0, 7, 5][i]}
        centralizer_records.append({
            'peripheral': i+1, 'coordinate_outer_images': [sorted(x) for x in images],
            'complete_base_centralizer_image': sorted(intersection),
            'actual_centralizer_vectors': actual_vectors,
            'new_conjugator_outer_coset': sorted(new_outer_coset),
            'new_first_class_union': sorted(first_class_union),
            'old_first_class_union': sorted(old_class_union)})
    print('PASS: complete centralizer unions force the original first profile high and the swapped profile low')

    # Every low Nielsen representative occurs in a swapped base coordinate.
    # The corresponding literal lift is the graph of that coordinate.
    graph_indices = []
    for j, triple in enumerate(low):
        k = next(k for k, t in enumerate(swapped) if t == triple)
        assert k == 2*j
        graph_indices.append(k)
    # All360 inner conjugates of every low representative give distinct
    # first triples, and exhaust the exact2160 allowed triples.
    low_triples = {tuple(G.conjugate(g, t0) for t0 in t) for t in low for g in inner}
    high_triples = {tuple(G.conjugate(g, t0) for t0 in t) for t in high for g in inner}
    assert len(low_triples) == 2160 and len(high_triples) == 3240
    assert len({t for t in high_triples if any(t == tuple(G.conjugate(g, t0) for t0 in s)
                                              for s in high[:6] for g in inner)}) == 2160
    print('PASS: swapped ordinary fibre has2160 graph lifts and0 proper lifts')
    print('PASS: original ordinary fibre has3240 weak lifts:2160 graphs and1080 proper lifts')

    def automorphism_description(g):
        return {'index': g, 'images_of_a_b': [raw['A6_elements'][j] for j in pairs[g]]}

    payload = {
        'status': 'PASS_A6_ORDINARY_CHIEF_OBSTRUCTION',
        'common_outer_source': {'x1': 1, 'x2': 2, 'x3': 3, 'addition': 'bitwise XOR'},
        'high_triples': high, 'low_triples': low,
        'all15_automorphism_descriptions': [[automorphism_description(g) for g in t] for t in all_triples],
        'all105_K_kernel_witnesses': witnesses,
        'base_source_triples': base, 'extension_source_triples': original,
        'base_automorphism': {'coordinate_permutation': base_swap, 'order': 2},
        'base_peripheral_conjugators': h,
        'complete_centralizer_comparisons': centralizer_records,
        'new_graph_base_coordinates_zero_based': graph_indices,
        'source_generation_proof_data': {
            'simple_kernel_order': 360, 'common_outer_order': 4,
            'base_factor_count': 12, 'extension_factor_count': 13,
            'base_order': str(4*360**12), 'extension_order': str(4*360**13),
            'method': 'All K-coordinate maps are onto A6 and have pairwise distinct kernels; exact simple subdirect-product argument.'},
        'ordinary_counts': {'original': {'weak': 3240, 'proper': 1080, 'complements': 2160},
                            'swapped': {'weak': 2160, 'proper': 0, 'complements': 2160}},
        'maximal_pro5_quotient_orders': {'base': 1, 'extension': 1},
        'scope': 'An ordinary peripheral generating-lift obstruction for a split A6 chief extension. '
                 'Products with a finite five-group retain an obstructed finite branch and an admitted '
                 'branch over the same prescribed pro-five shadow; no rational leading-image restriction follows alone.'}
    HERE.joinpath('a_peripheral_a6_ordinary.json').write_text(json.dumps(payload, indent=2)+'\n')
    print(payload['status'])


if __name__ == '__main__':
    main()
