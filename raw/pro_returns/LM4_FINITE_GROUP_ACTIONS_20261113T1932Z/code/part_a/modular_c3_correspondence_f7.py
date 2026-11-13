#!/usr/bin/env python3
"""Exact Schreier and filling maps for the two orbit-20 F.7 detectors.

This constructs actual presentations and substitutions.  It makes no
faithfulness claim for the induced GT0 correspondence.
"""
from itertools import permutations
from pathlib import Path
from collections import Counter
import json

import modular_a5_gt0_f7 as finite


def reduce_word(word):
    out = []
    for value in word:
        if out and out[-1] == -value:
            out.pop()
        else:
            out.append(value)
    return tuple(out)


def inverse_word(word):
    return tuple(-value for value in reversed(word))


def substitute(word, images):
    return reduce_word(value for letter in word
                       for value in (images[letter] if letter > 0 else
                                     inverse_word(images[-letter])))


def cyclic_reduce(word):
    word = reduce_word(word)
    while len(word) >= 2 and word[0] == -word[-1]:
        word = word[1:-1]
    return word


def canonical_relator(word):
    word = cyclic_reduce(word)
    if not word:
        return ()
    inverse = inverse_word(word)
    return min(word[i:]+word[:i] for i in range(len(word))) if word < inverse else min(
        inverse[i:]+inverse[:i] for i in range(len(inverse)))


def simplify_presentation(generators, relators, protected=()):
    current = set(generators)
    images = {g: (g,) for g in current}
    relators = {canonical_relator(r) for r in relators} - {()}
    steps = []
    while True:
        options = []
        for relator in relators:
            counts = Counter(abs(a) for a in relator)
            for generator, count in counts.items():
                if count == 1 and generator not in protected:
                    options.append((len(relator), generator, relator))
        if not options:
            break
        _, generator, relation = min(options)
        place = next(i for i, a in enumerate(relation) if abs(a) == generator)
        rotated_tail = relation[place+1:]+relation[:place]
        replacement = inverse_word(rotated_tail) if relation[place] > 0 else rotated_tail
        substitution = {g: ((g,) if g != generator else replacement) for g in current}
        relators = {canonical_relator(substitute(r, substitution)) for r in relators} - {()}
        images = {g: substitute(w, substitution) for g, w in images.items()}
        current.remove(generator)
        steps.append({'eliminated': generator, 'relation': relation,
                      'replacement': replacement})
    return sorted(current), sorted(relators), images, steps


def factor_reduce(word, orders):
    out = []
    for letter in word:
        factor = abs(letter)
        value = 1 if letter > 0 else orders[factor]-1
        if out and abs(out[-1]) == factor:
            previous = out.pop()
            value = (value + (1 if previous > 0 else orders[factor]-1)) % orders[factor]
        if value:
            assert value in (1, orders[factor]-1)
            out.append(factor if value == 1 else -factor)
    return tuple(out)


def factor_cyclic_core(word, orders):
    word = factor_reduce(word, orders)
    while len(word) > 1 and abs(word[0]) == abs(word[-1]):
        word = factor_reduce(word[1:] + word[:1], orders)
    return word


def main():
    group = {g for g in permutations(range(5)) if finite.parity(g) == 0}
    one = tuple(range(5))
    a, b = (1, 0, 3, 2, 4), (2, 1, 4, 3, 0)
    d = finite.multiply(a, b)
    subgroup = finite.generated([b], 5)
    assert len(subgroup) == 3

    # Right cosets T g, with prefix-closed positive BFS representatives.
    start = frozenset(subgroup)
    cosets = [start]
    representatives = [()]
    representatives_q = [one]
    positions = {start: 0}
    transitions = {}
    tree_edges = set()
    for i, coset in enumerate(cosets):
        for letter, permutation in ((1, a), (2, b)):
            target = frozenset(finite.multiply(g, permutation) for g in coset)
            if target not in positions:
                positions[target] = len(cosets)
                cosets.append(target)
                representatives.append(representatives[i]+(letter,))
                representatives_q.append(finite.multiply(representatives_q[i], permutation))
                tree_edges.add((i, letter))
            transitions[i, letter] = positions[target]
    assert len(cosets) == 20 and len(tree_edges) == 19
    backward = {(transitions[i, letter], letter): i
                for i in range(20) for letter in (1, 2)}
    schreier = {}
    generator_words = {}
    for i in range(20):
        for letter in (1, 2):
            if (i, letter) in tree_edges:
                schreier[i, letter] = ()
            else:
                generator = len(generator_words)+1
                schreier[i, letter] = (generator,)
                target = transitions[i, letter]
                generator_words[generator] = (representatives[i]+(letter,)+
                                              inverse_word(representatives[target]))
    assert len(generator_words) == 21

    def rewrite(word, initial=0):
        state, result = initial, []
        for letter in word:
            if letter > 0:
                result.extend(schreier[state, letter])
                state = transitions[state, letter]
            else:
                state = backward[state, -letter]
                result.extend(inverse_word(schreier[state, -letter]))
        return reduce_word(result), state

    relations = []
    for state in range(20):
        for relation in ((1, 1), (2, 2, 2)):
            word, end = rewrite(relation, state)
            assert end == state
            relations.append(word)
    cone_states = [i for i in range(20) if transitions[i, 2] == i]
    assert len(cone_states) == 2
    cones = [schreier[i, 2][0] for i in cone_states]
    generators, relators, images, steps = simplify_presentation(
        generator_words, relations, cones)
    assert len(generators) == 5
    assert set(relators) == {(-r, -r, -r) for r in cones}
    assert set(cones) <= set(generators)

    # Four width-five cusp cycles in T\A5/<d>, with actual peripheral words.
    d_transition = {i: transitions[transitions[i, 1], 2] for i in range(20)}
    unseen = set(range(20))
    cusps = []
    # The source's twelve labels are the same BFS left-coset labels as F7.
    all_words, queue = finite.quotient_transversal(group, a, b)
    dgroup = finite.generated([d], 5)
    vertex_cosets = []
    for g in queue:
        coset = frozenset(finite.multiply(g, h) for h in dgroup)
        if coset not in vertex_cosets:
            vertex_cosets.append(coset)
    vertex_indices = {c: i for i, c in enumerate(vertex_cosets)}
    while unseen:
        state = min(unseen)
        cycle = [state]
        while d_transition[cycle[-1]] != state:
            cycle.append(d_transition[cycle[-1]])
        assert len(cycle) == 5
        unseen -= set(cycle)
        word_e = representatives[state] + (1, 2)*5 + inverse_word(representatives[state])
        word_schreier, end = rewrite(word_e)
        assert end == 0
        word_b = substitute(word_schreier, images)
        coset_g = representatives_q[state]
        vertices = sorted({vertex_indices[frozenset(
            finite.multiply(finite.multiply(t, coset_g), h) for h in dgroup)]
                           for t in subgroup})
        assert len(vertices) == 3
        cusps.append({'coset_cycle': cycle, 'E_peripheral_word': word_e,
                      'B_peripheral_word': word_b, 'retained_H_triple': vertices})
    assert len(cusps) == 4

    fillings = []
    for keep in range(4):
        filled_relations = relators + [c['B_peripheral_word']
                                      for i, c in enumerate(cusps) if i != keep]
        final_generators, final_relators, filling_map, filling_steps = simplify_presentation(
            generators, filled_relations, cones)
        assert final_generators == sorted(cones)
        assert set(final_relators) == {(-r, -r, -r) for r in cones}
        orders = {r: 3 for r in cones}
        for i, cusp in enumerate(cusps):
            value = factor_reduce(substitute(cusp['B_peripheral_word'], filling_map), orders)
            if i != keep:
                assert not value
        retained_word = factor_reduce(substitute(cusps[keep]['B_peripheral_word'], filling_map), orders)
        core = factor_cyclic_core(retained_word, orders)
        assert len(core) == 2 and set(core) == set(cones)
        fillings.append({
            'retained_cusp': keep,
            'retained_H_triple': cusps[keep]['retained_H_triple'],
            'quotient_generators': final_generators,
            'quotient_relators': final_relators,
            'images_of_B_generators': {str(g): filling_map[g] for g in generators},
            'retained_peripheral_word': retained_word,
            'retained_peripheral_cyclic_core': core,
            'Tietze_steps': filling_steps,
        })

    cone_images = []
    for cone in cones:
        value = one
        for letter in generator_words[cone]:
            permutation = a if abs(letter) == 1 else b
            if letter < 0:
                permutation = finite.inverse(permutation)
            value = finite.multiply(value, permutation)
        cone_images.append(value)
    assert cone_images == [b, finite.inverse(b)]

    # Explicit compact E words for the five final B generators.
    hword = (1, 2, 1, -2)
    tau = hword + (1,) + inverse_word(hword)
    uword = (1, -2)*4 + (1,)
    vword = (1, 2) + uword + (2, 1)
    wword = (1, 2, 1, -2, 1) + (2, 1)*3 + (-2, 1, 2, 1)
    compact_words = {1: (2,), 9: uword, 14: vword, 18: wword,
                     21: tau + (2,) + inverse_word(tau)}
    assert set(compact_words) == set(generators)
    for generator in generators:
        assert factor_reduce(generator_words[generator], {1: 2, 2: 3}) == \
            factor_reduce(compact_words[generator], {1: 2, 2: 3})
    assert not factor_reduce(tau+tau, {1: 2, 2: 3})
    tau_image = one
    for letter in tau:
        value = a if abs(letter) == 1 else b
        if letter < 0:
            value = finite.inverse(value)
        tau_image = finite.multiply(tau_image, value)
    assert finite.order(tau_image) == 2
    assert finite.conjugate(tau_image, b) == finite.inverse(b)
    assert len(finite.generated([tau_image, b], 5)) == 6

    # The E endomorphism a->tau,b->b restricts to a common actual section.
    def iota(word):
        return substitute(word, {1: tau, 2: (2,)})

    section_checks = []
    xword, yword = (1, 2)*2, (2, 1)*2
    for filling in fillings:
        mapping = {int(k): tuple(v) for k, v in filling['images_of_B_generators'].items()}
        for name, word in (('x', xword), ('y', yword)):
            rewritten, state = rewrite(iota(word))
            assert state == 0
            value = substitute(substitute(rewritten, images), mapping)
            value_in_E = substitute(value, {1: (2,), 21: (1, 2, 1)})
            assert factor_reduce(value_in_E, {1: 2, 2: 3}) == factor_reduce(word, {1: 2, 2: 3})
            section_checks.append({'filling': filling['retained_cusp'],
                                   'basis_generator': name, 'verified': True})

    # A source-group common-kernel word, with an actual finite detector.
    k0, k1 = cusps[0]['B_peripheral_word'], cusps[1]['B_peripheral_word']
    common_word = reduce_word(k0+k1+inverse_word(k0)+inverse_word(k1))
    assert common_word == (-9, 1, -14, -1, 9, 14)
    for filling in fillings:
        mapping = {int(k): tuple(v) for k, v in filling['images_of_B_generators'].items()}
        assert not factor_reduce(substitute(common_word, mapping), {1: 3, 21: 3})
    sigma, upsilon = (1, 0, 2), (0, 2, 1)
    source_detector = {1: (0, 1, 2), 21: (0, 1, 2), 9: sigma,
                       14: upsilon, 18: (0, 1, 2)}
    detected = (0, 1, 2)
    for letter in common_word:
        value = source_detector[abs(letter)]
        if letter < 0:
            value = finite.inverse(value)
        detected = finite.multiply(detected, value)
    assert finite.order(detected) == 3

    result = {
        'scope': 'Exact index-20 orbifold subgroup and the four filling maps to C3 coproduct C3; no faithfulness assertion for a GT0 detector.',
        'subgroup_index': 20,
        'coset_representatives_in_E': representatives,
        'coset_transition_table': [
            {'coset': i, 'generator': letter, 'target': transitions[i, letter],
             'tree_edge': (i, letter) in tree_edges,
             'Schreier_generator': schreier[i, letter]}
            for i in range(20) for letter in (1, 2)],
        'initial_Schreier_generator_count': 21,
        'initial_Schreier_generator_words_in_E': {
            str(g): generator_words[g] for g in sorted(generator_words)},
        'initial_orbifold_relator_count': 40,
        'initial_Schreier_relators': relations,
        'B_free_product_generators': generators,
        'B_free_product_relators': relators,
        'B_generator_words_in_E': {str(g): generator_words[g] for g in generators},
        'cone_generators': cones,
        'cone_generator_A5_images': cone_images,
        'B_initial_to_final_generator_map': {str(g): images[g] for g in sorted(images)},
        'B_Tietze_steps': steps,
        'cusps': cusps,
        'fillings': fillings,
        'compact_E_words_for_B_generators': {str(g): w for g, w in compact_words.items()},
        'tau_word_in_E': tau,
        'tau_A5_image': tau_image,
        'iota_E_A5_image_order': 6,
        'common_section_checks': section_checks,
        'common_source_group_kernel_word': common_word,
        'source_word_S3_detector': {'generator_images': source_detector,
                                    'word_image': detected, 'word_image_order': 3},
        'all_assertions_passed': True,
    }
    Path(__file__).with_name('modular_c3_correspondence_f7_output.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
