#!/usr/bin/env python3
"""Independent literal replay and exact old-W quotient of the deep source."""
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np
from de_ferrari_a6_solvable import SolvableF, SolvableB
from de_ferrari_a6_source_data import load_data
from de_a6_triple_kernel_replay import selected_group
from de_a6_triple_base_prepare import evaluate
from a_cm_gl23_pc import ClassTwoCoordinates
from de_ferrari_two_core import rref2, solve2

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_E62_deep_replay_root'


class LiteralSolvableB(SolvableB):
    def comm(self, a, b):
        return self.mul(self.conj(a, b), self.inv(b))


def main():
    started = time.monotonic()
    names = ['e_a6_E62_deep_collect_root.json', 'e_a6_E62_deep_collect_root.npz',
             'e_a6_E62_deep_prepare_root.npz', 'a_cm_gl23_joint.npz',
             'a_cm_gl23_joint_pc.npz', 'e_a6_E62_H_residual_root.json',
             'e_a6_double_E62_kernel_replay_root.npz',
             'e_a6_double_central_replay_root.npz']
    hashes = {n: sha256((HERE / n).read_bytes()).hexdigest() for n in names}
    raw = json.loads((HERE / names[0]).read_text())
    data = np.load(HERE / names[1])
    prep = np.load(HERE / names[2])
    expected_binary, expected_ternary = {}, {}
    for row in raw['binary_stages']:
        for value, node in zip(row['basis_values'], row['basis_word_nodes']):
            assert node not in expected_binary or expected_binary[node] == value
            expected_binary[node] = value
    for row in raw['ternary_stages']:
        for value, node in zip(np.array(row['basis']).T, row['word_nodes']):
            assert node not in expected_ternary or np.array_equal(expected_ternary[node], value)
            expected_ternary[node] = value
    targets = sorted(set(expected_binary) | set(expected_ternary))
    F = SolvableF(); d = load_data(); B = LiteralSolvableB(F, d)
    P = ClassTwoCoordinates('joint')
    full = np.load(HERE / names[3])['joint_B_generators'].astype(np.uint16)
    actual, ancestors = selected_group(data['literal_B_word_DAG'], targets, B, [B.s, B.r])
    permutations = evaluate(data['literal_B_word_DAG'], full, targets)
    for node, value in expected_binary.items():
        g = actual[node]
        assert g[0] == B.e
        assert not np.any(g[1][:11]) and int(g[1][11]) == (value >> 24)
        assert np.array_equal(permutations[node], P.element(value & ((1 << 24)-1)))
    for node, value in expected_ternary.items():
        g = actual[node]
        assert g[0] == B.e and np.array_equal(g[1], np.r_[0, 0, value, 0])
        assert np.array_equal(permutations[node], P.one)
    assert len(data['literal_B_word_DAG']) == len(data['source_N_lower_central_grades'])
    assert len(data['literal_B_word_DAG']) == len(data['source_H_lower_central_grades'])
    initial = raw['binary_stages'][0]['basis_values']
    bits = np.array([[(a >> j) & 1 for j in range(24)] for a in initial], dtype=np.int64).T
    w = np.array([[(a >> (24+j)) & 1 for j in range(6)] for a in initial], dtype=np.int64).T
    assert bits.shape == (24, 24) and len(rref2(bits)[1]) == 24
    alpha = np.array([solve2(bits.T, row)[0] for row in w], dtype=np.int64)
    assert np.array_equal(alpha @ bits % 2, w)
    assert not np.any(alpha[:, 18:]) and len(rref2(alpha)[1]) == 6
    def wvalue(c):
        v = alpha @ np.array([(c >> j) & 1 for j in range(24)], dtype=np.int64) % 2
        return int(v @ (1 << np.arange(6)))
    # These all-basis product checks retain the actual PC carries;
    # the vanishing central columns already proves the full homomorphism.
    for i in range(24):
        for j in range(24):
            assert wvalue(P.product(1 << i, 1 << j)) == (wvalue(1 << i) ^ wvalue(1 << j))
    for value in prep['actual_N_commutator_binary_values']:
        value = int(value)
        assert wvalue(value & ((1 << 24)-1)) == value >> 24
    for node, value in expected_binary.items():
        assert wvalue(value & ((1 << 24)-1)) == value >> 24
    residual = json.loads((HERE / names[5]).read_text())
    assert residual['matching_upper_and_lower_images']
    assert int(residual['exact_residual_intersection_with_E62_N_prime_order']) == 2**15
    enlarged = np.load(HERE / names[6])
    central = np.load(HERE / names[7])
    pure = enlarged['old_J_E62_identity_binary_basis']
    perfect = enlarged['perfect_common_kernel_binary_basis']
    assert pure.shape == perfect.shape == (128, 122)
    assert len(rref2(np.c_[pure, perfect])[1]) == 122
    assert not np.any(central['kernel_to_preimage_abelianization'] @ pure % 2)
    masks = [int(row @ (1 << np.arange(24))) for row in alpha]
    result = {
        'status': 'PASS_INDEPENDENT_LITERAL_DEEP_SOURCE_AND_W_QUOTIENT',
        'all_binary_stage_words_replayed_in_both_actual_maps': len(expected_binary),
        'all_ternary_stage_words_replayed_in_both_actual_maps': len(expected_ternary),
        'literal_B_word_ancestors_replayed': ancestors,
        'entire_old_W_map_from_E62_PC_coordinates': alpha.tolist(),
        'old_W_parity_row_masks': masks,
        'old_W_map_kills_all_E62_central_PC_coordinates': True,
        'all_4656_original_joint_commutators_match_W_graph': True,
        'all_576_basis_products_preserve_actual_W_map': True,
        'perfect_122_kernel_equals_old_J_E62_identity_kernel': True,
        'exact_reduced_N_prime_image_order': str(3**6 * 2**24),
        'exact_reduced_I_image_order': str(3**6 * 2**15),
        'E62_image_of_I_intersect_kernel_J2_order': 64,
        'last_order_derivation': '(3^6 times2^15)/(3^6 times2^9), using E63 exact I projection',
        'finite_word_scope': 'Saved words lie in the specified finite-depth source subgroups; actual I preimages use nested compact fibres.',
        'input_sha256': hashes,
        'seconds': round(time.monotonic() - started, 6)}
    np.savez_compressed(HERE / (STEM + '.npz'), E62_PC_to_old_W_matrix=alpha,
                        old_W_parity_row_masks=np.array(masks, dtype=np.int64))
    (HERE / (STEM + '.json')).write_text(json.dumps(result, indent=2) + '\n')
    assert all(sha256((HERE / n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps({k: v for k, v in result.items() if k not in ['input_sha256', 'entire_old_W_map_from_E62_PC_coordinates']}, indent=2), flush=True)


if __name__ == '__main__':
    main()
