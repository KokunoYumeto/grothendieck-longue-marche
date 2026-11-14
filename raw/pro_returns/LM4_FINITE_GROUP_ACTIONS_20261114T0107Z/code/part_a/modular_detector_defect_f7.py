#!/usr/bin/env python3
"""Exact word certificates for F.7.42--48.

The universal formulas are proved in the text.  The finite word checks
below certify their stated conventions and the explicit subgroup words.
They do not establish faithfulness of a GT0 filling detector.
"""
from pathlib import Path
import json

import modular_a5_gt0_f7 as finite
from modular_c3_correspondence_f7 import (
    reduce_word, inverse_word, substitute, factor_reduce,
)


def integer_power(letter, exponent):
    return (letter if exponent >= 0 else -letter,) * abs(exponent)


def abelianization(word):
    return tuple(sum((1 if a > 0 else -1) for a in word if abs(a) == g)
                 for g in (1, 2))


def normalized_coordinate(word):
    aa, bb = abelianization(word)
    return reduce_word(integer_power(2, bb) + inverse_word(word)
                       + integer_power(1, aa))


def main():
    directory = Path(__file__).resolve().parent
    data = json.loads((directory / 'modular_c3_correspondence_f7_output.json').read_text())
    assert data['all_assertions_passed']
    transitions = {
        (row['coset'], row['generator']): row['target']
        for row in data['coset_transition_table']
    }
    schreier = {
        (row['coset'], row['generator']): tuple(row['Schreier_generator'])
        for row in data['coset_transition_table']
    }
    backward = {(target, letter): state
                for (state, letter), target in transitions.items()}
    final_images = {
        int(g): tuple(word)
        for g, word in data['B_initial_to_final_generator_map'].items()
    }

    def rewrite_b(word):
        state, value = 0, []
        for letter in word:
            if letter > 0:
                value.extend(schreier[state, letter])
                state = transitions[state, letter]
            else:
                state = backward[state, -letter]
                value.extend(inverse_word(schreier[state, -letter]))
        assert state == 0
        return substitute(value, final_images)

    def fill(word, keep):
        mapping = {
            int(g): tuple(value)
            for g, value in data['fillings'][keep]['images_of_B_generators'].items()
        }
        in_factors = substitute(rewrite_b(word), mapping)
        return factor_reduce(
            substitute(in_factors, {1: (2,), 21: (1, 2, 1)}),
            {1: 2, 2: 3},
        )

    xword, yword = (1, 2)*2, (2, 1)*2
    c0, c1 = (1, 2)*5, (2, 1)*5
    assert fill(c0, 0) == factor_reduce(xword, {1: 2, 2: 3})
    assert fill(c1, 0) == factor_reduce(yword, {1: 2, 2: 3})
    assert not factor_reduce(
        c1 + inverse_word((2,)+c0+(-2,)), {1: 2, 2: 3})

    tau = tuple(data['tau_word_in_E'])
    iota_images = {1: tau, 2: (2,)}
    proposed_x = (1, 2, -1, -2, -1, 2, 1)
    proposed_y = (2, -1, -2, 1, -2, -1)
    actual_values = {}
    for name, word, proposed in (
            ('x', xword, proposed_x), ('y', yword, proposed_y)):
        actual = factor_reduce(substitute(word, iota_images), {1: 2, 2: 3})
        proposed_e = factor_reduce(
            substitute(proposed, {1: xword, 2: yword}), {1: 2, 2: 3})
        assert actual == proposed_e
        actual_values[name] = actual
        for keep in range(4):
            assert fill(actual, keep) == factor_reduce(word, {1: 2, 2: 3})
    matrix = [[abelianization(proposed_x)[0], abelianization(proposed_y)[0]],
              [abelianization(proposed_x)[1], abelianization(proposed_y)[1]]]
    assert matrix == [[0, -1], [1, -1]]
    assert matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0] == 1

    def evaluate(word, images, degree):
        value = tuple(range(degree))
        for letter in word:
            image = images[abs(letter)]
            if letter < 0:
                image = finite.inverse(image)
            value = finite.multiply(value, image)
        return value

    a5, b5 = (1, 0, 3, 2, 4), (2, 1, 4, 3, 0)
    a3, b3 = (0, 2, 1), (1, 2, 0)
    q5 = {1: a5, 2: b5}
    q3 = {1: a3, 2: b3}
    for word in actual_values.values():
        assert evaluate(word, q5, 5) == tuple(range(5))
        assert evaluate(word, q3, 3) == tuple(range(3))
    x5, y5 = evaluate(xword, q5, 5), evaluate(yword, q5, 5)
    assert len(finite.generated([x5, y5], 5)) == 60

    words = [()]
    current = [()]
    for length in range(1, 8):
        current = [word+(letter,) for word in current
                   for letter in (1, -1, 2, -2)
                   if not word or word[-1] != -letter]
        assert all(len(word) == length for word in current)
        words.extend(current)
    assert len(words) == 4373
    lift_checks = 0
    for word in words:
        aa, bb = abelianization(word)
        ff = normalized_coordinate(word)
        assert abelianization(ff) == (0, 0)
        normalized_y = reduce_word(inverse_word(ff)+(2,)+ff)
        conjugated_y = reduce_word(
            integer_power(1, -aa)+word+(2,)+inverse_word(word)
            +integer_power(1, aa))
        assert normalized_y == conjugated_y
        assert (not ff) == (
            word == reduce_word(integer_power(1, aa)+integer_power(2, bb)))
        for mm in range(-3, 4):
            changed = reduce_word(integer_power(1, -mm)+word
                                  +integer_power(2, mm))
            assert abelianization(changed) == (aa-mm, bb+mm)
            assert normalized_coordinate(changed) == ff
            lift_checks += 1

    result = {
        'scope': 'Exact based subgroup and normalization identities; no GT0 detector faithfulness claim.',
        'based_cusp_images': {'p0_d5': fill(c0, 0), 'p0_e5': fill(c1, 0)},
        'common_section_basis_checks': 8,
        'iota_K_basis_words': {'x': proposed_x, 'y': proposed_y},
        'iota_K_abelianization_matrix': matrix,
        'iota_K_A5_images': {
            name: evaluate(word, q5, 5) for name, word in actual_values.items()
        },
        'iota_K_S3_images': {
            name: evaluate(word, q3, 3) for name, word in actual_values.items()
        },
        'q5_K_image_order': len(finite.generated([x5, y5], 5)),
        'reduced_words_checked': len(words),
        'maximum_word_length': 7,
        'normalization_conjugacy_checks': len(words),
        'zero_abelianization_checks': len(words),
        'exact_kernel_word_checks': len(words),
        'lift_independence_checks': lift_checks,
        'all_assertions_passed': True,
    }
    (directory / 'modular_detector_defect_f7_output.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
