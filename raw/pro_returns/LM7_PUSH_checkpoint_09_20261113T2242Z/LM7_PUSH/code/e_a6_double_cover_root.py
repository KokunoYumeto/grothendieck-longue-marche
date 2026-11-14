#!/usr/bin/env python3
"""Literal central double cover of the retained six-point A6.

We enumerate SL2(F9), construct its actual six-coset action, verify all
720 squared quotient products, and lift every retained A6 automorphism.
The only input is the already certified literal A6 group/Aut table.
No abstract exceptional isomorphism or Schur-multiplier assertion is used.
"""
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_double_cover_root'


def main():
    started = time.monotonic()
    old_path = HERE / 'de_ferrari_a6_kernels.npz'
    old_hash = sha256(old_path.read_bytes()).hexdigest()
    old = np.load(old_path)
    # Codes a+3b denote a+b*t, where t^2=-1 in F3.
    addition = np.empty((9, 9), dtype=np.uint8)
    field = np.empty((9, 9), dtype=np.uint8)
    for a in range(9):
        for b in range(9):
            addition[a, b] = (a % 3 + b % 3) % 3 + 3 * ((a // 3 + b // 3) % 3)
            field[a, b] = ((a % 3) * (b % 3) - (a // 3) * (b // 3)) % 3 + 3 * (
                ((a % 3) * (b // 3) + (a // 3) * (b % 3)) % 3)
    negative = np.array([(-a % 3) + 3 * (-(a // 3) % 3) for a in range(9)], dtype=np.uint8)
    inverse_field = np.array([0] + [int(np.flatnonzero(field[a] == 1)[0])
                                    for a in range(1, 9)], dtype=np.uint8)
    assert all(field[a, inverse_field[a]] == 1 for a in range(1, 9))
    for a in range(9):
        for b in range(9):
            for c in range(9):
                assert addition[addition[a, b], c] == addition[a, addition[b, c]]
                assert field[field[a, b], c] == field[a, field[b, c]]
                assert field[a, addition[b, c]] == addition[field[a, b], field[a, c]]
    all_codes = np.arange(9 ** 4, dtype=np.int64)
    matrices = ((all_codes[:, None] // (9 ** np.arange(4))) % 9).astype(np.uint8).reshape(-1, 2, 2)
    determinants = addition[field[matrices[:, 0, 0], matrices[:, 1, 1]],
                            negative[field[matrices[:, 0, 1], matrices[:, 1, 0]]]]
    cover = matrices[determinants == 1]
    assert len(cover) == 720

    def encode(value):
        value = np.asarray(value, dtype=np.int64)
        return value.reshape(value.shape[:-2] + (4,)) @ (9 ** np.arange(4))

    lookup = np.full(9 ** 4, -1, dtype=np.int16)
    lookup[encode(cover)] = np.arange(720)
    one = int(lookup[encode(np.eye(2, dtype=np.uint8))])
    z = int(lookup[encode(2 * np.eye(2, dtype=np.uint8))])
    products = np.empty((720, 720, 2, 2), dtype=np.uint8)
    for i in range(2):
        for j in range(2):
            products[:, :, i, j] = addition[
                field[cover[:, None, i, 0], cover[None, :, 0, j]],
                field[cover[:, None, i, 1], cover[None, :, 1, j]]]
    multiplication = lookup[encode(products)]
    assert np.all(multiplication >= 0)
    inverse = np.argmax(multiplication == one, axis=1).astype(np.int16)
    assert np.all(multiplication[np.arange(720), inverse] == one)
    assert np.all(multiplication[inverse, np.arange(720)] == one)
    assert z != one and multiplication[z, z] == one
    assert np.array_equal(multiplication[z], multiplication[:, z])

    # Construct the projective table solely to locate an actual subgroup.
    canonical = np.minimum(np.arange(720), multiplication[z])
    representatives = np.unique(canonical)
    assert len(representatives) == 360
    projective_index = np.full(720, -1, dtype=np.int16)
    projective_index[representatives] = np.arange(360)
    projection = projective_index[canonical]
    projective_mul = projection[multiplication[representatives[:, None], representatives[None, :]]]
    projective_one = int(projection[one])
    assert np.array_equal(projection[multiplication],
                          projective_mul[projection[:, None], projection[None, :]])
    projective_orders = []
    for g in range(360):
        value = projective_one
        order = 0
        while order == 0 or value != projective_one:
            value = int(projective_mul[value, g])
            order += 1
            assert order <= 360
        projective_orders.append(order)

    def closure(table, identity, generators):
        elements = [identity]
        found = {identity}
        for value in elements:
            for generator in generators:
                nxt = int(table[value, generator])
                if nxt not in found:
                    found.add(nxt)
                    elements.append(nxt)
        return elements

    trials = []
    subgroup = None
    for a in range(360):
        if projective_orders[a] != 2:
            continue
        for b in range(360):
            if projective_orders[b] != 3 or projective_orders[int(projective_mul[a, b])] != 5:
                continue
            projected_subgroup = closure(projective_mul, projective_one, [a, b])
            lifted_subgroup = closure(multiplication, one, representatives[[a, b]])
            trials.append({'projective_generators': [a, b],
                           'projective_subgroup_order': len(projected_subgroup),
                           'matrix_subgroup_order': len(lifted_subgroup)})
            if len(projected_subgroup) == 60 and len(lifted_subgroup) == 120:
                subgroup = np.array(sorted(lifted_subgroup), dtype=np.int16)
                subgroup_generators = representatives[[a, b]].copy()
                break
        if subgroup is not None:
            break
    assert subgroup is not None
    assert len(set(map(int, projection[subgroup]))) == 60
    assert one in subgroup and z in subgroup
    assert np.all(np.isin(multiplication[subgroup[:, None], subgroup[None, :]], subgroup))
    coset_index = np.full(720, -1, dtype=np.int16)
    coset_representatives = []
    cosets = []
    for g in range(720):
        if coset_index[g] >= 0:
            continue
        values = multiplication[g, subgroup]
        assert len(set(map(int, values))) == 120
        assert np.all(coset_index[values] < 0)
        coset_index[values] = len(cosets)
        coset_representatives.append(g)
        cosets.append(values)
    assert len(cosets) == 6 and np.all(coset_index >= 0)
    coset_representatives = np.array(coset_representatives, dtype=np.int16)
    action = coset_index[multiplication[:, coset_representatives]]
    assert np.array_equal(np.sort(action, axis=1), np.tile(np.arange(6), (720, 1)))
    old_index = {tuple(p): i for i, p in enumerate(old['A6_elements'])}
    assert len(old_index) == 360
    assert all(tuple(p) in old_index for p in action)
    quotient = np.array([old_index[tuple(p)] for p in action], dtype=np.int16)
    assert set(map(int, quotient)) == set(range(360))
    assert all(np.count_nonzero(quotient == i) == 2 for i in range(360))
    assert np.array_equal(quotient[multiplication],
                          old['A6_multiplication'][quotient[:, None], quotient[None, :]])
    section = np.array([int(np.flatnonzero(quotient == i)[0]) for i in range(360)], dtype=np.int16)
    base = old['Aut_generator_pairs'][int(old['Aut_one'])]
    generators = section[base]
    parent = np.full(720, -1, dtype=np.int16)
    letter = np.full(720, -1, dtype=np.int8)
    ab = np.zeros((720, 2), dtype=np.int8)
    parent[one] = one
    order = [one]
    for value in order:
        for j, generator in enumerate(generators):
            nxt = int(multiplication[value, generator])
            if parent[nxt] < 0:
                parent[nxt] = value
                letter[nxt] = j
                ab[nxt] = ab[value]
                ab[nxt, j] ^= 1
                order.append(nxt)
    assert len(order) == 720
    centre = np.flatnonzero(np.all(multiplication[:, generators] == multiplication[generators, :].T, axis=1))
    assert set(map(int, centre)) == {one, z}
    assert set(map(int, np.flatnonzero(quotient == quotient[one]))) == {one, z}
    a, b = map(int, generators)
    commutator = int(multiplication[multiplication[multiplication[a, b], inverse[a]], inverse[b]])
    conjugates = multiplication[multiplication[:, commutator], inverse]
    conjugating = {}
    for g, value in enumerate(conjugates):
        conjugating.setdefault(int(value), g)
    commutator_generators = sorted(conjugating)
    derived_parent = np.full(720, -1, dtype=np.int16)
    derived_letter = np.full(720, -1, dtype=np.int16)
    derived_parent[one] = one
    derived = [one]
    for value in derived:
        for j, generator in enumerate(commutator_generators):
            nxt = int(multiplication[value, generator])
            if derived_parent[nxt] < 0:
                derived_parent[nxt] = value
                derived_letter[nxt] = j
                derived.append(nxt)
    assert len(derived) == 720

    def word(value):
        result = []
        while value != one:
            result.append(int(letter[value]) + 1)
            value = int(parent[value])
        return result[::-1]

    factors = []
    value = z
    while value != one:
        factors.append(conjugating[commutator_generators[int(derived_letter[value])]])
        value = int(derived_parent[value])
    central_word = []
    for g in factors[::-1]:
        w = word(g)
        central_word += w + [1, 2, -1, -2] + [-j for j in w[::-1]]
    value = one
    for j in central_word:
        value = int(multiplication[value, generators[j - 1] if j > 0 else inverse[generators[-j - 1]]])
    assert value == z
    assert all(sum((j == i) - (j == -i) for j in central_word) == 0 for i in (1, 2))
    print('Matrix group, six-coset A6 map and complete perfectness PASS.', flush=True)

    # Every central change of both generator images is retained. Cayley
    # relations solve the unique valid shift for every quotient automorphism.
    zlog = np.full(720, -1, dtype=np.int8)
    zlog[[one, z]] = [0, 1]
    targets = multiplication[:, generators]
    relator_exponents = np.empty((720, 2, 2), dtype=np.int8)
    for j in range(2):
        unit = np.eye(2, dtype=np.int8)[j]
        relator_exponents[:, j] = (ab + unit - ab[targets[:, j]]) % 2
    D = relator_exponents.reshape(-1, 2)
    first = next(i for i, row in enumerate(D) if np.any(row))
    second = next(i for i, row in enumerate(D)
                  if (int(D[first, 0]) * int(row[1]) - int(D[first, 1]) * int(row[0])) % 2)
    A = D[[first, second]].astype(np.int64)
    Ainv = np.array([[A[1, 1], -A[0, 1]], [-A[1, 0], A[0, 0]]]) % 2
    assert np.array_equal(A @ Ainv % 2, np.eye(2, dtype=np.int64))
    lifted_generators = section[old['Aut_generator_pairs']]
    candidate = np.empty((1440, 720), dtype=np.int16)
    candidate[:, one] = one
    for value in order[1:]:
        candidate[:, value] = multiplication[candidate[:, parent[value]],
                                              lifted_generators[:, letter[value]]]
    defects = np.empty((1440, 720, 2), dtype=np.int8)
    for j in range(2):
        residual = multiplication[multiplication[candidate, lifted_generators[:, j, None]],
                                  inverse[candidate[:, targets[:, j]]]]
        defects[:, :, j] = zlog[residual]
    assert np.all(defects >= 0)
    defects = defects.reshape(1440, -1)
    shifts = (-defects[:, [first, second]].astype(np.int64) @ Ainv.T) % 2
    assert not np.any((defects + shifts @ D.T) % 2)
    twists = shifts @ ab.T % 2
    zpower = np.array([one, z], dtype=np.int16)
    automorphisms = multiplication[zpower[twists], candidate]
    assert np.array_equal(np.sort(automorphisms, axis=1), np.tile(np.arange(720), (1440, 1)))
    assert np.array_equal(quotient[automorphisms], old['Aut_maps'][:, quotient])
    for generator in generators:
        assert np.array_equal(automorphisms[:, multiplication[:, generator]],
                              multiplication[automorphisms, automorphisms[:, generator, None]])
    for i in range(1440):
        assert np.array_equal(automorphisms[old['Aut_multiplication'][i]][:, generators],
                              automorphisms[i, automorphisms[:, generators]])
    assert np.all(automorphisms[:, z] == z)
    character = np.ones(1440, dtype=np.int8)
    result = {
        'status': 'PASS_LITERAL_CENTRAL_DOUBLE_A6_COVER',
        'field_definition': 'F3[t]/(t^2+1), code a+3b for a+b*t',
        'all_field_associativity_and_distributivity_checks': 9 ** 3,
        'all_2x2_matrices_tested': 9 ** 4,
        'matrix_group_order': 720,
        'projective_group_order': 360,
        'subgroup_search_trials': trials,
        'selected_matrix_subgroup_order': 120,
        'selected_subgroup_matrix_generators': cover[subgroup_generators].tolist(),
        'actual_left_coset_count': 6,
        'actual_six_point_image_equals_retained_A6': True,
        'all_720_squared_quotient_products_checked': True,
        'central_kernel_order': 2,
        'full_centre_exactly_scalar_matrices': True,
        'original_cover_generator_indices': generators.tolist(),
        'original_A6_generator_indices': base.tolist(),
        'derived_normal_closure_order': 720,
        'cover_is_perfect': True,
        'central_generator_index': z,
        'central_generator_matrix': cover[z].tolist(),
        'literal_central_commutator_word': central_word,
        'all_1440_A6_automorphisms_lifted': True,
        'complete_automorphism_Cayley_edge_checks': 1440 * 720 * 2,
        'all_1440_squared_compositions_checked_on_both_generators': True,
        'all_four_generator_central_shifts_retained': True,
        'selected_two_relator_rows': [first, second],
        'selected_exponent_matrix_mod2': A.tolist(),
        'all_lifted_automorphisms_fix_the_centre': True,
        'input_sha256': {'de_ferrari_a6_kernels.npz': old_hash},
        'Ferrari_source_or_CM_fibre_conclusion': False,
        'seconds': round(time.monotonic() - started, 3),
    }
    np.savez_compressed(HERE / (STEM + '.npz'),
        field_addition=addition, field_multiplication=field,
        field_negative=negative, field_inverse=inverse_field,
        cover_matrices=cover, cover_multiplication=multiplication,
        cover_inverse=inverse, cover_one=np.array(one),
        cover_central_generator=np.array(z), actual_six_point_action=action,
        A6_quotient=quotient, A6_section=section, cover_generators=generators,
        selected_subgroup=subgroup, selected_subgroup_generators=subgroup_generators,
        coset_representatives=coset_representatives, coset_index=coset_index,
        source_Cayley_parent=parent, source_Cayley_letter=letter,
        source_Cayley_abelianization_mod2=ab,
        all_lifted_automorphisms=automorphisms,
        automorphism_central_character=character,
        all_automorphism_generator_central_shifts=shifts,
        full_Cayley_relator_exponent_matrix_mod2=D)
    (HERE / (STEM + '.json')).write_text(json.dumps(result, indent=2) + '\n')
    assert sha256(old_path.read_bytes()).hexdigest() == old_hash
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
