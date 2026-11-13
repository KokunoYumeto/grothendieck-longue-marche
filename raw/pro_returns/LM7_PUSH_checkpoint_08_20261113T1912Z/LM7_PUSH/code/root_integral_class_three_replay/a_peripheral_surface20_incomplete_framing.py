#!/usr/bin/env python3
"""Literal surface presentation and peripheral transport for the degree20 cover.

Faces are merged by exact Tietze eliminations.  Handles are extracted by
an explicit invertible free-word substitution, leaving each based boundary
generator unchanged.  The script then records the actual order-five
source characters and the local conjugator outer values.
"""

from collections import Counter
from functools import reduce
from pathlib import Path
import argparse
import json
import sympy as sp

HERE = Path(__file__).resolve().parent


def red(word):
    out = []
    for a in word:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return out


def inv(word):
    return [-a for a in reversed(word)]


def substitute(word, images):
    return red([a for letter in word for a in
                (images[abs(letter)] if letter > 0 else inv(images[abs(letter)]))])


def apply(columns, vector):
    return reduce(int.__xor__, (column for i, column in enumerate(columns) if (vector >> i) & 1), 0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--configuration', type=Path)
    parser.add_argument('--prefix', default='a_peripheral_surface20')
    args = parser.parse_args()
    raw = json.loads(HERE.joinpath('a_peripheral_a5_deleted.json').read_text())
    boundaries = raw['boundary_words_in_Schreier_basis']
    assert len(boundaries) == 12
    counts = Counter(a for word in boundaries for a in word)
    assert all(counts[j] == counts[-j] == 1 for j in range(1, 22))
    images = {j: [j] for j in range(1, 22)}
    images.update({22+i: word for i, word in enumerate(boundaries)})
    relations = [word+[-(22+i)] for i, word in enumerate(boundaries)]
    eliminations = []
    while len(relations) > 1:
        chosen = None
        for a in range(1, 22):
            plus = next((i for i, word in enumerate(relations) if a in word), None)
            minus = next((i for i, word in enumerate(relations) if -a in word), None)
            if plus is not None and minus is not None and plus != minus:
                chosen = a, plus, minus
                break
        assert chosen is not None
        a, i, j = chosen
        R, S = relations[i], relations[j]
        at, bt = R.index(a), S.index(-a)
        R = R[at:]+R[:at]
        S = S[bt:]+S[:bt]
        U, V = R[1:], S[1:]
        assert substitute([a]+U, images) == []
        assert substitute([-a]+V, images) == []
        merged = U+V
        assert substitute(merged, images) == []
        eliminations.append({'eliminated_generator': a, 'first_rotated_relation': R,
                             'second_rotated_relation': S, 'replacement': inv(U),
                             'merged_relation': merged})
        relations = [r for k, r in enumerate(relations) if k not in (i, j)]+[merged]
    relation = relations[0]
    original_polygon = relation[:]
    remaining = {abs(a) for a in relation if abs(a) <= 21}
    assert len(remaining) == 10
    handles, steps = [], []
    while remaining:
        found = None
        for a in sorted(remaining):
            at = relation.index(a)
            prefix = relation[:at]
            rotated = relation[at:]+prefix
            ia = rotated.index(-a)
            for ib in range(1, ia):
                b = rotated[ib]
                if abs(b) not in remaining or abs(b) == a:
                    continue
                jb = rotated.index(-b)
                if jb > ia:
                    found = a, b, prefix, rotated, ib, ia, jb
                    break
            if found is not None:
                break
        assert found is not None
        a, b, prefix, rotated, ib, ia, jb = found
        U, V = rotated[1:ib], rotated[ib+1:ia]
        W, Z = rotated[ia+1:jb], rotated[jb+1:]
        C = W+V+U
        A, B = red(inv(C)+[a]+U), red([b]+V+U)
        # Literal extraction: C^-1 R_rot C = [A,B] Z W V U.
        next_relation = Z+W+V+U
        lhs = red(inv(C)+rotated+C)
        rhs = red(A+B+inv(A)+inv(B)+next_relation)
        assert lhs == rhs
        conjugator = prefix+C
        handles = [(red(inv(conjugator)+h+conjugator),
                    red(inv(conjugator)+k+conjugator)) for h, k in handles]
        handles.append((A, B))
        steps.append({'first_variable': a, 'second_signed_variable': b,
                      'cyclic_prefix': prefix, 'U': U, 'V': V, 'W': W, 'Z': Z,
                      'new_handle': [A, B], 'next_relation': next_relation})
        relation = next_relation
        remaining -= {a, abs(b)}
    assert len(handles) == 5 and sorted(relation) == list(range(-33, -21))
    final_relation = [a for A, B in handles for a in A+B+inv(A)+inv(B)]+relation
    assert substitute(final_relation, images) == []
    handle_words = [[substitute(A, images), substitute(B, images)] for A, B in handles]
    basis_words = [word for pair in handle_words for word in pair]
    omitted_boundary = abs(relation[-1])-22
    basis_words += [word for i, word in enumerate(boundaries) if i != omitted_boundary]
    abelian_matrix = [[sum(1 if a == j+1 else -1 if a == -(j+1) else 0 for a in word)
                       for word in basis_words] for j in range(21)]
    determinant = int(sp.Matrix(abelian_matrix).det())
    assert abs(determinant) == 1
    print('PASS: eleven exact face eliminations and five invertible handle extractions', flush=True)
    print('Retained boundary order:', relation, '; integral basis determinant', determinant, flush=True)

    H = [tuple(p) for p in raw['A5_elements']]
    hindex = {p: i for i, p in enumerate(H)}
    one = hindex[tuple(range(5))]

    def hmul(a, b):
        return hindex[tuple(H[a][H[b][j]] for j in range(5))]

    hinv = [next(b for b in range(60) if hmul(a, b) == one) for a in range(60)]
    hgens = dict(zip((1, 2), raw['A5_source_indices'][:2]))
    hgens.update({-a: hinv[g] for a, g in list(hgens.items())})
    matrices = raw['module_action_columns']

    def big_action(h, v):
        return sum(apply(matrices[h], (v >> (4*j)) & 15) << (4*j) for j in range(4))

    def evaluate_h(word):
        h = one
        for letter in word:
            h = hmul(h, hgens[letter])
        return h

    vx, vy = raw['source_big_vectors']
    gx, gy = hgens[1], hgens[2]
    vz = big_action(hinv[hmul(gx, gy)], vx ^ big_action(gx, vy))
    peripheral_vectors = [vx, vy, vz]
    witness = (json.loads(args.configuration.read_text()) if args.configuration
               else raw['cup_pattern_witness'])
    T = witness['multiplicity_matrix_columns']
    powers = [[1, 2, 4, 8]]
    for _ in range(4):
        powers.append([apply(T, column) for column in powers[-1]])

    def multiplicity_action(t, v):
        blocks = [(v >> (4*j)) & 15 for j in range(4)]
        return sum(reduce(int.__xor__, (blocks[j] for j in range(4) if (t[j] >> i) & 1), 0)
                   << (4*i) for i in range(4))

    forms = [f << (4*j) for f in raw['C3_invariant_dual_basis'] for j in range(4)]
    f, g = [reduce(int.__xor__, (forms[k] for k in range(8) if (coordinate >> k) & 1), 0)
            for coordinate in (witness['first_form_coordinates'], witness['second_form_coordinates'])]

    def epsilon(v):
        return ((v & f).bit_count() & 1) | (((v & g).bit_count() & 1) << 1)

    def global_outer(word):
        return reduce(int.__xor__, (1 if abs(a) == 1 else 2 for a in word), 0)

    source_characters = []
    for t in powers:
        row = [epsilon(multiplicity_action(t, v)) ^ global_outer(word)
               for (v, h), word in zip(raw['schreier_values'], raw['schreier_words'])]
        source_characters.append(row)

    def word_character(word, row):
        return reduce(int.__xor__, (row[abs(a)-1] for a in word), 0)

    boundary_characters = [[word_character(word, row) for word in boundaries]
                           for row in source_characters]
    assert all(row == [1]*4+[2]*4+[3]*4 for row in boundary_characters)
    handle_characters = [[[word_character(A, row), word_character(B, row)]
                          for A, B in handle_words] for row in source_characters]
    # All local base conjugators are actual module vectors solving
    # (1-h_i)u_i=(T^j-1)v_i; 1-h_i is invertible for the order-five h_i.
    local_conjugators = []
    conjugator_outer_values = []
    starts = [min(cycle) for cycles in raw['peripheral_cycles'] for cycle in cycles]
    tree_words = {int(k): v for k, v in raw['tree_words'].items()}
    start_h = [evaluate_h(tree_words[start]) for start in starts]
    base_boundary_path_outer = [global_outer(tree_words[start]) for start in starts]
    for t in powers:
        us = []
        for h, v in zip(raw['A5_source_indices'], peripheral_vectors):
            target = multiplicity_action(t, v) ^ v
            u = sum(next(w for w in range(16) if w ^ apply(matrices[h], w) ==
                         ((target >> (4*j)) & 15)) << (4*j) for j in range(4))
            assert u ^ big_action(h, u) == target
            us.append(u)
        local_conjugators.append(us)
        conjugator_outer_values.append([epsilon(big_action(h, us[i//4])) for i, h in enumerate(start_h)])
    print('Exact handle outer characters for powers0..4:', handle_characters, flush=True)
    print('Actual local conjugator outer values:', conjugator_outer_values, flush=True)
    payload = {'status': 'PASS_EXACT_SURFACE_AND_LOCAL_TRANSPORT',
               'face_eliminations': eliminations, 'merged_polygon': original_polygon,
               'handle_extractions': steps,
               'handle_words_in_Schreier_basis': handle_words,
               'final_boundary_word': relation, 'omitted_boundary_in_basis': omitted_boundary,
               'abelian_basis_matrix': abelian_matrix, 'abelian_basis_determinant': determinant,
               'source_characters_on_Schreier_basis': source_characters,
               'handle_outer_characters': handle_characters,
               'boundary_outer_characters': boundary_characters,
               'boundary_start_cosets': starts, 'boundary_start_words': [tree_words[s] for s in starts],
               'boundary_base_path_outer': base_boundary_path_outer,
               'local_base_conjugator_module_vectors': local_conjugators,
               'local_conjugator_outer_values': conjugator_outer_values,
               'outer_module_forms': [f, g],
               'scope': 'Exact surface presentation and prescribed local conjugator transport; no A6 lift count is asserted here.'}
    HERE.joinpath(args.prefix+'.json').write_text(json.dumps(payload, indent=2)+'\n')
    print(payload['status'])


if __name__ == '__main__':
    main()
