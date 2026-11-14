#!/usr/bin/env python3
"""Exact relative two-character phase search for the order-five source.

The phase is evaluated directly from the saved surface handles and the
actual local conjugator vectors.  Any count inference is subsequently
checked by the complete Aut(A6) class algebra and proper-image subtraction.
"""

from functools import reduce
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def apply(columns, vector):
    return reduce(int.__xor__, (column for i, column in enumerate(columns) if (vector >> i) & 1), 0)


def parity(x):
    return x.bit_count() & 1


def main():
    raw = json.loads(HERE.joinpath('a_peripheral_a5_deleted.json').read_text())
    surf = json.loads(HERE.joinpath('a_peripheral_surface20.json').read_text())
    H = [tuple(p) for p in raw['A5_elements']]
    hindex = {p: i for i, p in enumerate(H)}
    one = hindex[tuple(range(5))]
    hmul = lambda a, b: hindex[tuple(H[a][H[b][i]] for i in range(5))]
    hinv = [next(b for b in range(60) if hmul(a, b) == one) for a in range(60)]
    gens = dict(zip((1, 2), raw['A5_source_indices'][:2]))
    gens.update({-a: hinv[g] for a, g in list(gens.items())})
    matrices = raw['module_action_columns']
    forms = [f << (4*j) for f in raw['C3_invariant_dual_basis'] for j in range(4)]
    T = raw['cup_pattern_witness']['multiplicity_matrix_columns']
    powers = [[1, 2, 4, 8]]
    for _ in range(4):
        powers.append([apply(T, column) for column in powers[-1]])

    def big_action(h, v):
        return sum(apply(matrices[h], (v >> (4*j)) & 15) << (4*j) for j in range(4))

    def multiplicity_action(t, v):
        blocks = [(v >> (4*j)) & 15 for j in range(4)]
        return sum(reduce(int.__xor__, (blocks[j] for j in range(4) if (t[j] >> i) & 1), 0)
                   << (4*i) for i in range(4))

    def source_word_outer(word):
        return reduce(int.__xor__, (1 if abs(a) == 1 else 2 for a in word), 0)

    def word_value(word, row):
        return reduce(int.__xor__, (row[abs(a)-1] for a in word), 0)

    source_q_row = [source_word_outer(word) for word in raw['schreier_words']]
    q_handles = [[word_value(A, source_q_row), word_value(B, source_q_row)]
                 for A, B in surf['handle_words_in_Schreier_basis']]
    handle_rows = []
    for t in powers:
        source_row = [sum(parity(f & multiplicity_action(t, v)) << k for k, f in enumerate(forms))
                      for v, h in raw['schreier_values']]
        handle_rows.append([[word_value(A, source_row), word_value(B, source_row)]
                            for A, B in surf['handle_words_in_Schreier_basis']])
    start_h = []
    for word in surf['boundary_start_words']:
        h = one
        for a in word:
            h = hmul(h, gens[a])
        start_h.append(h)
    conjugator_rows = [[sum(parity(f & big_action(h, us[i//4])) << k for k, f in enumerate(forms))
                        for i, h in enumerate(start_h)]
                       for us in surf['local_base_conjugator_module_vectors']]

    def phase(j, f, g):
        out = 0
        for (qa, qb), (la, lb) in zip(q_handles, handle_rows[j]):
            a0, a1 = (qa & 1) ^ parity(f & la), (qa >> 1) ^ parity(g & la)
            b0, b1 = (qb & 1) ^ parity(f & lb), (qb >> 1) ^ parity(g & lb)
            out ^= (a0 & b1) ^ (a1 & b0)
        for i, row in enumerate(conjugator_rows[j]):
            outer = 1+i//4
            out ^= (parity(f & row) & (outer >> 1)) ^ (parity(g & row) & (outer & 1))
        return out

    original = [raw['cup_pattern_witness'][key] for key in ('first_form_coordinates', 'second_form_coordinates')]
    original_phases = [phase(j, *original) for j in range(5)]
    print('Original exact relative phase sequence:', original_phases, flush=True)

    def actual_form(f):
        return reduce(int.__xor__, (forms[k] for k in range(8) if (f >> k) & 1), 0)

    def invariant_stabilizer(f, g):
        f, g = actual_form(f), actual_form(g)
        return [h for h in range(60)
                if all(parity(f & big_action(h, 1 << i)) == ((f >> i) & 1)
                       and parity(g & big_action(h, 1 << i)) == ((g >> i) & 1)
                       for i in range(16))]

    solutions = []
    for f in range(1, 256):
        baseline = [phase(j, f, 0) for j in range(5)]
        coefficients = [sum((phase(j, f, 1 << k) ^ baseline[j]) << k for k in range(8))
                        for j in range(5)]
        for g in range(1, 256):
            if g == f:
                continue
            values = [baseline[j] ^ parity(coefficients[j] & g) for j in range(5)]
            if values not in ([0, 1, 1, 1, 1], [1, 0, 0, 0, 0]):
                continue
            assert values == [phase(j, f, g) for j in range(5)]
            stabilizer = invariant_stabilizer(f, g)
            if len(stabilizer) != 3:
                continue
            fa, ga = actual_form(f), actual_form(g)
            conjugacy = []
            for j, k in product(range(5), repeat=2):
                witnesses = [h for h in range(60)
                             if all(parity(fa & multiplicity_action(powers[j], big_action(h, 1 << i))) ==
                                    parity(fa & multiplicity_action(powers[k], 1 << i)) and
                                    parity(ga & multiplicity_action(powers[j], big_action(h, 1 << i))) ==
                                    parity(ga & multiplicity_action(powers[k], 1 << i))
                                    for i in range(16))]
                conjugacy.append({'first': j, 'second': k, 'conjugators': witnesses})
            if any(row['conjugators'] for row in conjugacy if row['first'] != row['second']):
                continue
            solutions.append({'multiplicity_matrix_columns': T,
                              'first_form_coordinates': f, 'second_form_coordinates': g,
                              'actual_forms': [fa, ga], 'relative_phase_sequence': values,
                              'common_A5_stabilizer': stabilizer,
                              'all_ordered_outer_character_conjugator_sets': conjugacy})
            print('Unique-phase witness:', solutions[-1], flush=True)
            break
        if solutions:
            break
    payload = {'status': 'PASS_EXACT_RELATIVE_PHASE_SEARCH',
               'original_forms': original, 'original_relative_phases': original_phases,
               'q_handle_characters': q_handles,
               'module_handle_rows': handle_rows, 'local_conjugator_rows': conjugator_rows,
               'solutions': solutions,
               'scope': 'Exact F2 phase and outer-character search; actual generating counts must be computed separately.'}
    HERE.joinpath('a_peripheral_boundary_phase.json').write_text(json.dumps(payload, indent=2)+'\n')
    if solutions:
        HERE.joinpath('a_peripheral_boundary_configuration.json').write_text(json.dumps(solutions[0], indent=2)+'\n')
    print(payload['status'])


if __name__ == '__main__':
    main()
