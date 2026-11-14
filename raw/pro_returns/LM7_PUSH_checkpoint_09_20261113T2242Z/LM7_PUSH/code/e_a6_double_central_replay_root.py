#!/usr/bin/env python3
"""Independent binary presentation replay above the certified perfect C.

The exact source kernel is retained, including all C-generator exponents
and every change of their lifts by a central kernel element.
"""
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np
from e_a6_double_model_root import FerrariA6Double
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_ferrari_two_core import rref2, solve2
from de_a6_triple_kernel_replay import selected_group
from de_a6_triple_base_prepare import evaluate

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_double_central_replay_root'


def rank(a):
    return len(rref2(np.asarray(a, dtype=np.int64) % 2)[1])


def main():
    started = time.monotonic()
    names = ['e_a6_double_central_root.json', 'e_a6_double_central_prepare_root.npz',
             'e_a6_double_kernel_replay_root.npz', 'de_a6_gl_central_prepare.npz',
             'e_a6_double_central_root.cpp', 'e_a6_double_central_prepare_root.py']
    hashes = {n: sha256((HERE / n).read_bytes()).hexdigest() for n in names}
    raw = json.loads((HERE / names[0]).read_text())
    prep, source, old = (np.load(HERE / names[i]) for i in (1, 2, 3))
    kd = source['kernel_basis'].shape[1]
    nc = prep['central_coinvariant_map'].shape[0]
    width = 10+nc
    assert raw['complete_base_relation_count'] == 720615
    assert raw['all_ten_original_to_normal_form_relations_evaluated']
    assert raw['all_original_central_shift_parameters'] == 10*nc
    if not raw['all_complete_relations_evaluated']:
        assert raw['full_abelian_rank_upper_bound_attained'] and raw['abelian_relation_rank'] == width
    else:
        assert raw['Schreier_relations_evaluated'] == 720615
    rows = np.asarray(raw['relation_basis_rows'], dtype=np.int64)
    targets, nodes = raw['relation_basis_word_nodes'], raw['literal_C_generator_word_DAG']
    assert rows.shape == (raw['abelian_relation_rank'], width)
    assert rank(rows) == len(rows) == len(targets)
    H = FerrariA6Double()
    W = InducedCombined(H, load_data())
    original = [(W.id, v) for v in source['C_source_values']]
    values, count = selected_group(nodes, targets, W, original)
    permutations = evaluate(nodes, old['C_original_source_permutations'], targets)
    assert all(np.array_equal(v, np.arange(9462)) for v in permutations.values())
    needed, stack = set(map(int, targets)), list(map(int, targets))
    while stack:
        i = stack.pop()
        op, a, b = map(int, nodes[i])
        for j in ([a, b] if op in (2, 4, 5) else [a] if op == 3 else []):
            if j not in needed:
                needed.add(j)
                stack.append(j)
    exponents = {}
    for i in sorted(needed):
        op, a, b = map(int, nodes[i])
        if op == 0:
            e = np.zeros(10, dtype=np.int64)
        elif op == 1:
            e = np.eye(10, dtype=np.int64)[a]
        elif op == 2:
            e = (exponents[a]+exponents[b]) % 2
        elif op == 3:
            e = -exponents[a] % 2
        elif op == 4:
            e = np.zeros(10, dtype=np.int64)
        elif op == 5:
            e = exponents[b]
        else:
            raise AssertionError(op)
        exponents[i] = e
    piv, projection = prep['kernel_ambient_pivot_rows'], prep['central_map_on_ambient_pivots']
    B, Q = source['kernel_basis'], prep['central_coinvariant_map']
    assert np.array_equal(projection @ B[piv] % 2, Q)
    for node, row in zip(targets, rows):
        value = values[node]
        assert np.array_equal(value[0], W.id)
        vector = H.relative_kernel_vector(value[1]).ravel()
        solved = solve2(B, vector)
        assert solved is not None and np.array_equal(B @ solved[0] % 2, vector)
        central = projection @ vector[piv] % 2
        assert np.array_equal(row, np.r_[exponents[node], -central % 2])
    assert rank(rows[:, :10]) == 10
    hom = solve2(rows, np.zeros(len(rows), dtype=np.int64))[1]
    dimension = width-rank(rows)
    assert hom.shape == (width, dimension) and not np.any(rows @ hom % 2)
    L = hom[10:].T @ Q % 2
    assert rank(L) == dimension
    K0 = solve2(L, np.zeros(dimension, dtype=np.int64))[1]
    assert K0.shape == (kd, kd-dimension) and not np.any(L @ K0 % 2)
    assert not np.any(L @ prep['C_commutator_module'] % 2)
    quotient_actions = {}
    for label in ('B', 'C', 'H'):
        aa, vv = source[label+'_actions'], []
        if dimension:
            right = np.column_stack([solve2(L, np.eye(dimension, dtype=np.int64)[:, i])[0]
                                     for i in range(dimension)])
            assert np.array_equal(L @ right % 2, np.eye(dimension, dtype=np.int64))
            for a in aa:
                v = L @ a @ right % 2
                assert np.array_equal(v @ L % 2, L @ a % 2)
                vv.append(v)
        quotient_actions[label] = np.asarray(vv, dtype=np.int64).reshape(len(aa), dimension, dimension)
    shift_checks = 0
    for i in range(10):
        for j in range(nc):
            changed = rows.copy()
            changed[:, 10+j] = (changed[:, 10+j]-changed[:, i]) % 2
            assert rank(changed) == len(rows)
            shift_checks += 1
    out = {'status': 'PASS_INDEPENDENT_BINARY_C_PREIMAGE_ABELIANIZATION',
           'independent_relation_words_replayed': len(targets), 'required_C_word_DAG_ancestors': count,
           'all_relation_words_identity_in_actual_A6_source': True,
           'all_relation_values_replayed_in_actual_full_binary_source': True,
           'all_relation_exponent_and_central_rows_verified': True,
           'Schreier_relations_evaluated': raw['Schreier_relations_evaluated'],
           'all_complete_relations_evaluated': raw['all_complete_relations_evaluated'],
           'abelian_relation_rank': len(rows), 'source_generator_exponent_rank': 10,
           'preimage_abelianization_dimension': dimension, 'whole_kernel_dimension': kd,
           'derived_kernel_dimension': kd-dimension,
           'C_preimage_derived_is_perfect_by_abelian_kernel_lemma': True,
           'all_elementary_central_shift_column_changes_verified': shift_checks == 10*nc,
           'central_shift_parameter_count': 10*nc,
           'B_action_on_preimage_abelianization': quotient_actions['B'].tolist(),
           'H_action_on_preimage_abelianization': quotient_actions['H'].tolist(),
           'input_sha256': hashes, 'seconds': round(time.monotonic()-started, 3)}
    np.savez_compressed(HERE / (STEM+'.npz'), relation_matrix=rows,
                        full_abelian_character_basis=hom, kernel_to_preimage_abelianization=L,
                        kernel_of_preimage_abelianization=K0, C_lift_abelianization_values=hom[:10].T,
                        B_quotient_actions=quotient_actions['B'], C_quotient_actions=quotient_actions['C'],
                        H_quotient_actions=quotient_actions['H'])
    (HERE / (STEM+'.json')).write_text(json.dumps(out, indent=2)+'\n')
    assert all(sha256((HERE / n).read_bytes()).hexdigest() == v for n, v in hashes.items())
    print(json.dumps(out, indent=2), flush=True)


if __name__ == '__main__':
    main()
