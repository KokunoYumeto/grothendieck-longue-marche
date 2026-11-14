#!/usr/bin/env python3
"""Literal pure-projective kernel words and the uniform target comparison."""
from pathlib import Path
from hashlib import sha256
import json, math, time
import numpy as np
import sympy as sp
from sympy.combinatorics import Permutation, PermutationGroup
from de_a6_schreier_certificate import read_certificate, verify_words
from de_ferrari_a6_model import FerrariA6
from de_ferrari_sl2_5_model import FerrariSL2Five

HERE = Path(__file__).resolve().parent
STEM = 'de_a6_uniform_target_certificate'


def main():
    started = time.time()
    names = ['de_a6_uniform_target.bin', 'de_a6_uniform_target.out',
             'de_a6_uniform_target_prepare.npz', 'de_a6_uniform_target_prepare.json',
             'de_ferrari_a6_model.json', 'de_ferrari_sl2_5_model.json']
    hashes = {n: sha256((HERE / n).read_bytes()).hexdigest() for n in names}
    d = read_certificate(HERE / names[0]); verify_words(d)
    raw = json.loads((HERE / names[1]).read_text().splitlines()[-1])
    saved = np.load(HERE / names[2]); a6 = json.loads((HERE / names[4]).read_text())
    assert np.array_equal(d['original'], saved['actual_joint_generators'])
    assert d['degree'] == 536 and not d['derived']
    assert raw['status'] == 'PASS' and math.prod(raw['orbit_lengths']) == int(raw['order'])
    assert int(raw['order']) == 60 * a6['Nielsen_image_order']
    rows = [i for i, p in enumerate(d['strong'])
            if np.array_equal(p[:530], np.arange(530)) and
            np.any(p[530:] != np.arange(530, 536))]
    projected = np.array([d['strong'][i, 530:] - 530 for i in rows])
    assert len(rows) == 4
    assert int(PermutationGroup([Permutation(p) for p in projected]).order()) == 60

    # Reconstruct the exact four-dimensional source comparison, without
    # relying solely on the six-point abstract permutation group.
    J = sp.zeros(4)
    for i in range(3):
        J[i, i + 1] = 1; J[i + 1, i] = -1
    e = [sp.eye(4)[:, i] for i in range(4)]
    basis = sp.Matrix.hstack(e[0], e[1], e[0] + e[2], e[3])
    plane_records = []
    for i in range(3):
        T = sp.eye(4) + e[i] * e[i].T * J
        M = T.T
        column = J.inv() * M * J
        assert column == sp.eye(4) - e[i] * e[i].T * J
        in_basis = basis.inv() * column * basis
        assert in_basis[:, 2] == sp.eye(4)[:, 2]
        assert in_basis[3, 0] == in_basis[3, 1] == 0
        plane = in_basis[:2, :2]
        assert plane == sp.Matrix(saved['actual_W_matrices'][i])
        plane_records.append([[int(x) for x in row] for row in plane.tolist()])

    orders = []
    for name, model in [('A6', FerrariA6()), ('signed', FerrariSL2Five())]:
        for generator in ('a', 'b', 'c'):
            value = getattr(model, generator)
            assert np.array_equal(model.power(value, 60), model.one)
            assert all(not np.array_equal(model.power(value, 60 // p), model.one) for p in (2, 3, 5))
            orders.append({'target': name, 'generator': generator, 'exact_order': 60})
    result = {
        'status': 'PASS_EXACT_UNIFORM_TARGET_COMPARISON',
        'joint_quotient_degree': 536,
        'complete_final_Schreier_relations': raw['complete_final_Schreier_relations'],
        'A6_Nielsen_order': a6['Nielsen_image_order'], 'actual_joint_order': int(raw['order']),
        'index_over_A6_Nielsen': 60,
        'all_word_DAG_values_independently_replayed': True,
        'pure_projective_strong_rows': rows,
        'pure_projective_word_nodes': [int(d['words'][i]) for i in rows],
        'pure_projective_kernel_image_order': 60,
        'actual_W_quotient_matrices': plane_records,
        'all_full_braid_generator_exact_orders': orders,
        'actual_finite_target_product': 'A6 Nielsen target times the specified PSL2(F5) quotient',
        'uniform_inference_scope': 'E56 simple-quotient maps and the literal braid-generator order60 exclude every common parabolic quotient; the proof is in E57.',
        'input_sha256': hashes, 'all_protected_inputs_unchanged': True,
        'seconds': round(time.time() - started, 3),
    }
    np.savez_compressed(HERE / (STEM + '.npz'),
                        pure_projective_generator_values=projected,
                        pure_projective_full_values=d['strong'][rows],
                        pure_projective_word_nodes=d['words'][rows],
                        original_generator_values=d['original'],
                        complete_literal_word_DAG=d['nodes'])
    (HERE / (STEM + '.json')).write_text(json.dumps(result, indent=2) + '\n')
    assert all(sha256((HERE / n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
