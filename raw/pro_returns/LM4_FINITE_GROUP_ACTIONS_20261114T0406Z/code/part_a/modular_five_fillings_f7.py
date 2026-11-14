#!/usr/bin/env python3
"""Exact H presentations and the five based three-cusp quotient maps.

Every presentation elimination and inverse basis substitution is recorded.
The proof of full endomorphism surjectivity is in the accompanying text;
no finite computation supplies it or detector faithfulness.
"""
from pathlib import Path
import json

import modular_a5_gt0_f7 as finite
from modular_c3_correspondence_f7 import (
    reduce_word, inverse_word, substitute, simplify_presentation,
)


def power(word, exponent):
    return (word if exponent >= 0 else inverse_word(word))*abs(exponent)


def main():
    directory = Path(__file__).resolve().parent
    previous = json.loads((directory / 'modular_a5_gt0_f7_output.json').read_text())
    assert previous['all_assertions_passed']
    a, b = (1, 0, 3, 2, 4), (2, 1, 4, 3, 0)
    identity = tuple(range(5))
    states, representatives, positions = [identity], [()], {identity: 0}
    transitions, tree_edges = {}, set()
    for state, value in enumerate(states):
        for letter, permutation in ((1, a), (2, b)):
            target = finite.multiply(value, permutation)
            if target not in positions:
                positions[target] = len(states)
                states.append(target)
                representatives.append(representatives[state]+(letter,))
                tree_edges.add((state, letter))
            transitions[state, letter] = positions[target]
    assert len(states) == 60 and len(tree_edges) == 59
    backward = {(target, letter): state
                for (state, letter), target in transitions.items()}
    schreier, generator_words = {}, {}
    for state in range(60):
        for letter in (1, 2):
            if (state, letter) in tree_edges:
                schreier[state, letter] = ()
            else:
                number = len(generator_words)+1
                schreier[state, letter] = (number,)
                generator_words[number] = (
                    representatives[state]+(letter,)
                    +inverse_word(representatives[transitions[state, letter]]))
    assert len(generator_words) == 61

    def rewrite(word, initial=0):
        state, value = initial, []
        for letter in word:
            if letter > 0:
                value.extend(schreier[state, letter])
                state = transitions[state, letter]
            else:
                state = backward[state, -letter]
                value.extend(inverse_word(schreier[state, -letter]))
        return reduce_word(value), state

    relations = []
    for state in range(60):
        for relation in ((1, 1), (2, 2, 2)):
            rewritten, end = rewrite(relation, state)
            assert end == state
            relations.append(rewritten)
    generators, final_relations, h_images, steps = simplify_presentation(
        generator_words, relations)
    assert len(generators) == 11 and not final_relations and len(steps) == 50
    cusp_rows = previous['three_cusp_detector_orbits']['cusp_labels']
    cusp_words = []
    for row in cusp_rows:
        word, end = rewrite(row['peripheral_word'])
        assert end == 0
        cusp_words.append(substitute(word, h_images))

    expected = [
        ((0, 1, 2), (59, 60), {59: (2, 1), 60: (-2,)}),
        ((0, 1, 4), (51, 60), {51: (-2,), 60: (1,)}),
        ((0, 1, 8), (59, 60), {59: (2, 1), 60: (-2,)}),
        ((0, 1, 10), (51, 60), {51: (-2,), 60: (1,)}),
        ((0, 4, 9), (60, 61), {60: (1,), 61: (1, 2)}),
    ]
    fillings = []
    for retained, surviving, to_xy in expected:
        quotient_gens, quotient_rels, q_images, q_steps = simplify_presentation(
            generators, [word for label, word in enumerate(cusp_words)
                         if label not in retained])
        assert tuple(quotient_gens) == surviving
        assert not quotient_rels and len(q_steps) == 9
        q_cusps = [substitute(word, q_images) for word in cusp_words]
        first, second = q_cusps[0], q_cusps[retained[1]]
        assert substitute(first, to_xy) == (1,)
        assert substitute(second, to_xy) == (2,)
        from_xy = {1: first, 2: second}
        for generator, word in to_xy.items():
            assert substitute(word, from_xy) == (generator,)
        normalized = {g: substitute(word, to_xy) for g, word in q_images.items()}
        normalized_cusps = [substitute(word, normalized) for word in cusp_words]
        for label, word in enumerate(normalized_cusps):
            if label not in retained:
                assert word == ()
        assert normalized_cusps[0] == (1,)
        assert normalized_cusps[retained[1]] == (2,)
        fillings.append({
            'retained_labels': retained,
            'target_full_basis_cusp_labels': [0, retained[1]],
            'surviving_H_Schreier_generators': surviving,
            'quotient_generator_words_in_E': {
                str(g): generator_words[g] for g in surviving},
            'quotient_relators': quotient_rels,
            'H_basis_to_quotient': q_images,
            'quotient_to_xy': to_xy,
            'xy_to_quotient': from_xy,
            'H_basis_to_xy': normalized,
            'all_cusp_words_in_quotient': q_cusps,
            'all_cusp_words_in_xy': normalized_cusps,
            'nine_Tietze_eliminations': q_steps,
        })

    # The fourth cusp uses the exact original y=e^2 whisker.
    y_e = (2, 1)*2
    c0_e = (1, 2)*5
    from modular_c3_correspondence_f7 import factor_reduce
    assert factor_reduce(tuple(cusp_rows[4]['peripheral_word']), {1: 2, 2: 3}) == \
        factor_reduce(y_e+c0_e+inverse_word(y_e), {1: 2, 2: 3})

    # Finite quotient input for the unique H cone conjugator.
    group = finite.generated([a, b], 5)
    centralizer_b = [g for g in group if finite.conjugate(g, b) == b]
    assert set(centralizer_b) == finite.generated([b], 5)
    assert len(centralizer_b) == 3

    # Universal group word recovery in the free alphabet d,b,g.
    dd, bb, gg = (1,), (2,), (3,)
    ee = bb+dd+inverse_word(bb)
    hh = reduce_word(gg+bb+inverse_word(gg)+inverse_word(bb))
    recovery = []
    for jj in range(5):
        uu = power(dd, jj)+gg
        ff = reduce_word(bb+uu+inverse_word(bb)+inverse_word(uu))
        recovered_h = reduce_word(
            power(dd, -jj)+inverse_word(ff)+power(ee, jj))
        assert recovered_h == hh
        recovery.append({'j': jj, 'f_word_in_d_b_g': ff,
                         'recovered_h1': recovered_h})

    # The final cusp conjugator is [h1,y], with y outside H.
    # This verifies the whole source word before applying a filling map.
    hh, yy, cc = (1,), (2,), (3,)
    kk = hh+yy+inverse_word(hh)+inverse_word(yy)
    c4 = yy+cc+inverse_word(yy)
    lhs = hh+yy+inverse_word(hh)+cc+hh+inverse_word(yy)+inverse_word(hh)
    rhs = kk+c4+inverse_word(kk)
    assert reduce_word(lhs) == reduce_word(rhs)

    result = {
        'scope': 'Exact five full profinite filling presentations and word conventions; no detector faithfulness or finite-lift sufficiency assertion.',
        'index_of_H': 60,
        'coset_representatives': representatives,
        'coset_transition_table': [
            {'coset': state, 'generator': letter,
             'target': transitions[state, letter],
             'Schreier_generator': schreier[state, letter],
             'tree_edge': (state, letter) in tree_edges}
            for state in range(60) for letter in (1, 2)],
        'initial_generator_count': 61,
        'initial_generator_words_in_E': generator_words,
        'initial_relator_count': len(relations),
        'initial_relators': relations,
        'H_free_basis': generators,
        'H_final_relators': final_relations,
        'initial_generators_to_H_basis': h_images,
        'H_Tietze_eliminations': steps,
        'H_cusp_words_in_free_basis': cusp_words,
        'five_fillings': fillings,
        'total_filling_eliminations': sum(
            len(row['nine_Tietze_eliminations']) for row in fillings),
        'A5_centralizer_of_b': centralizer_b,
        'f_recovery_word_checks': recovery,
        'c4_exact_whisker_and_conjugator_checks': True,
        'all_assertions_passed': True,
    }
    (directory / 'modular_five_fillings_f7_output.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
