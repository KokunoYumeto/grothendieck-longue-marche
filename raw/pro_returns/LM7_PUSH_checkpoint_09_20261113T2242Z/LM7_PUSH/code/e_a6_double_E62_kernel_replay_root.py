#!/usr/bin/env python3
"""Independent full-model replay over the actual A6/A5/E62 common base.

The complete lifted collector supplies the upper inclusion. This program
replays every retained kernel word, both source conjugates, every actual
base strong word, and all projected kernel-coordinate maps. It makes no
claim that the retained B words themselves lie in a deeper source subgroup.
"""
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np
from e_a6_double_model_root import FerrariA6Double
from de_ferrari_sl2_5_model import FerrariSL2Five
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_a6_triple_kernel_replay import selected_group
from de_a6_triple_base_prepare import evaluate
from de_ferrari_two_core import Span2, rref2, solve2
from de_a6_schreier_certificate import read_certificate, verify_words

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_double_E62_kernel_replay_root'


def rank(a):
    return len(rref2(a)[1])


def main():
    started = time.monotonic()
    names = [
        'e_a6_double_E62_kernel_root.json',
        'e_a6_double_E62_base_root.bin',
        'e_a6_double_E62_base_prepare_root.npz',
        'e_a6_double_kernel_replay_root.npz',
        'de_a6_gl_kernel_replay.npz',
        'de_a6_double_bridge_replay.npz',
        'e_a6_double_central_replay_root.npz',
        'de_a6_double_signed_replay.npz',
        'de_a6_double_signed_replay.json',
        'e_a6_double_kernel_root.json',
        'a_cm_gl23_joint.json',
        'a_cm_gl23_joint.npz',
        'e_a6_double_E62_kernel_root.cpp',
        'de_a6_double_signed_lifted.hpp',
    ]
    hashes = {name: sha256((HERE / name).read_bytes()).hexdigest() for name in names}
    raw = json.loads((HERE / names[0]).read_text())
    assert raw['all_Schreier_relators_evaluated']
    assert raw['lifted_relators_evaluated'] == raw['complete_base_relator_count'] == 1279851
    assert raw['full_base_chain_replayed']
    assert raw['base_degree'] == 15774 and raw['kernel_width'] == 7776
    cert = read_certificate(HERE / names[1])
    verify_words(cert)
    prep, binary, signed, bridge, abel, previous = (
        np.load(HERE / names[i]) for i in range(2, 8))
    assert cert['degree'] == 15774 and not cert['derived']
    assert np.array_equal(cert['original'], np.array([prep['s'], prep['r']]))
    extra = np.load(HERE / 'a_cm_gl23_joint.npz')['joint_B_generators']
    assert np.array_equal(cert['original'][:, 11010:] - 11010, extra)
    assert 1 in cert['words'] and 2 in cert['words']
    assert tuple(cert['nodes'][1]) == (1, 0, 0)
    assert tuple(cert['nodes'][2]) == (1, 1, 0)
    nodes = list(raw['literal_word_DAG'])
    targets = list(map(int, raw['kernel_basis_word_nodes']))
    ambient = np.zeros((7776, len(targets)), dtype=np.int64)
    for j, support in enumerate(raw['kernel_basis_supports']):
        ambient[support, j] = 1
    H2, H5 = FerrariA6Double(), FerrariSL2Five()
    data = load_data()
    W2, W5 = InducedCombined(H2, data), InducedCombined(H5, data)
    v2, n2 = selected_group(nodes, targets, W2, [W2.letters[0], W2.letters[1]])
    v5, n5 = selected_group(nodes, targets, W5, [W5.letters[0], W5.letters[1]])
    base_values = evaluate(nodes, cert['original'], targets)
    S2, S5 = Span2(5724), Span2(2052)
    for j, column in enumerate(binary['kernel_basis'].T):
        assert S2.add(column, j)
    for j, column in enumerate(signed['joint_kernel_basis'].T):
        assert S5.add(column, j)
    columns = []
    for j, word in enumerate(targets):
        assert np.array_equal(base_values[word], np.arange(15774))
        assert np.array_equal(v2[word][0], W2.id)
        assert np.array_equal(v5[word][0], W5.id)
        a2 = H2.relative_kernel_vector(v2[word][1]).ravel()
        a5 = H5.relative_kernel_vector(v5[word][1]).ravel()
        assert np.array_equal(np.r_[a2, a5], ambient[:, j])
        columns.append(np.r_[S2.coordinates(a2), S5.coordinates(a5)])
    matrix = np.array(columns).T
    k = rank(matrix)
    assert k == len(targets) == raw['kernel_dimension']
    S = Span2(170)
    for j, column in enumerate(matrix.T):
        assert S.add(column, j)
    actions = []
    for letter in range(2):
        action_columns = []
        for word in targets:
            a2 = H2.relative_kernel_vector(W2.conj(W2.letters[letter], v2[word])[1]).ravel()
            a5 = H5.relative_kernel_vector(W5.conj(W5.letters[letter], v5[word])[1]).ravel()
            combined = np.r_[S2.coordinates(a2), S5.coordinates(a5)]
            action_columns.append(S.coordinates(combined))
        actions.append(np.column_stack(action_columns))
    actions = np.array(actions)
    assert np.array_equal(actions[0] @ actions[0] % 2, np.eye(k, dtype=np.int64))
    assert np.array_equal(actions[1] @ actions[1] @ actions[1] % 2, np.eye(k, dtype=np.int64))
    new_projection_rank, old_projection_rank = rank(matrix[:128]), rank(matrix[128:])
    pure_coeff = solve2(matrix[128:], np.zeros(42, dtype=np.int64))[1]
    pure = matrix[:128] @ pure_coeff % 2
    assert rank(pure) == pure.shape[1] == k - old_projection_rank
    assert not np.any(matrix[128:] @ pure_coeff % 2)
    pure_nodes = []
    for coefficients in pure_coeff.T:
        word = 0
        for j in np.flatnonzero(coefficients):
            value = targets[int(j)]
            if word:
                nodes.append([2, word, value])
                word = len(nodes) - 1
            else:
                word = value
        pure_nodes.append(word)
    # Retain an exact inclusion in the previous full125-space, and check
    # the entire perfect122-space through the actual binary coordinates.
    previous_pure = previous['old_signed_identity_binary_basis']
    old_coordinates = []
    for column in pure.T:
        solved = solve2(previous_pure, column)
        assert solved is not None
        old_coordinates.append(solved[0])
    perfect_coeff = solve2(bridge['derived_kernel_to_actual_three_Schur_signs'],
                          np.zeros(3, dtype=np.int64))[1]
    perfect_kernel = bridge['derived_binary_kernel_basis'] @ perfect_coeff % 2
    assert rank(perfect_kernel) == 122
    perfect_coordinates = [solve2(pure, column) for column in perfect_kernel.T]
    perfect_contained = all(value is not None for value in perfect_coordinates)
    pure_ab = abel['kernel_to_preimage_abelianization'] @ pure % 2
    base_order = int(raw['base_order'])
    old_meta = json.loads((HERE / 'de_a6_double_signed_replay.json').read_text())
    initial = json.loads((HERE / 'e_a6_double_kernel_root.json').read_text())
    E62 = json.loads((HERE / 'a_cm_gl23_joint.json').read_text())
    X2_order = int(initial['base_order']) * 2**128
    E62_order = int(E62['exact_groups']['joint_SL23_B']['order'])
    J2_order = int(old_meta['new_double_GL_joint_order'])
    enlarged_order = base_order * 2**k
    common_numerator = J2_order * E62_order
    assert common_numerator % enlarged_order == 0
    assert X2_order % 2**pure.shape[1] == 0
    result = {
        'status': 'PASS_INDEPENDENT_COMPLETE_DOUBLE_SIGNED_E62_SOURCE',
        'base_degree': 15774,
        'complete_base_relations': 1279851,
        'all_actual_base_strong_words_replayed': len(cert['words']),
        'all_basis_words_replayed_in_both_full_models_and_entire_E62_base': True,
        'word_ancestor_counts': [n2, n5],
        'joint_kernel_dimension': k,
        'binary_kernel_projection_rank': new_projection_rank,
        'signed_kernel_projection_rank': old_projection_rank,
        'kernel_over_entire_old_J_and_E62_dimension': pure.shape[1],
        'all_B_normal_conjugations_rechecked': 2*k,
        'old_J_and_E62_identity_word_count': len(pure_nodes),
        'perfect122_kernel_contained': perfect_contained,
        'new_kernel_image_in_E2_abelianization_rank': rank(pure_ab),
        'base_order': str(base_order),
        'entire_joint_order': str(enlarged_order),
        'actual_J2_E62_maximum_common_quotient_order': str(common_numerator // enlarged_order),
        'actual_X2_old_J_and_E62_maximum_common_quotient_order': str(X2_order // 2**pure.shape[1]),
        'scope': 'Exact finite common source and literal B-word kernels; deeper correction-domain membership is a separate proof.',
        'input_sha256': hashes,
        'seconds': round(time.monotonic() - started, 6),
    }
    np.savez_compressed(
        HERE / (STEM + '.npz'), joint_kernel_ambient_basis=ambient,
        joint_kernel_product_coordinates=matrix, joint_kernel_B_actions=actions,
        old_J_E62_identity_coefficient_basis=pure_coeff,
        old_J_E62_identity_binary_basis=pure,
        old_J_E62_identity_in_previous_coordinates=np.column_stack(old_coordinates),
        old_J_E62_identity_E2_abelianization=pure_ab,
        perfect_common_kernel_binary_basis=perfect_kernel,
        perfect_common_kernel_in_new_coordinates=(np.column_stack([v[0] for v in perfect_coordinates])
                                                  if perfect_contained else np.zeros((0, 0), dtype=np.int64)),
        literal_B_word_DAG=np.array(nodes, dtype=np.int64),
        joint_kernel_basis_word_nodes=np.array(targets, dtype=np.int64),
        old_J_E62_identity_word_nodes=np.array(pure_nodes, dtype=np.int64))
    (HERE / (STEM + '.json')).write_text(json.dumps(result, indent=2) + '\n')
    assert all(sha256((HERE / name).read_bytes()).hexdigest() == digest
               for name, digest in hashes.items())
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
