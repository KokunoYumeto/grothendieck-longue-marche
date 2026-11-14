#!/usr/bin/env python3
"""Literal whole-J preimages of every new common-source/kernel basis value."""
from pathlib import Path
import hashlib
import json
import time
import numpy as np

from a_cm_kn23_witnesses import Words
from de_a6_schreier_certificate import read_certificate, verify_words

HERE = Path(__file__).resolve().parent
STEM = 'bc_gaussian_kn_words'


def main():
    start = time.monotonic()
    inputs = ['bc_gaussian_kn_common.py', 'bc_gaussian_kn_common.json',
              'bc_gaussian_kn_common.npz', 'bc_gaussian_kn_common_N_derived.bin',
              'bc_gaussian_kn_common_J_projected.bin',
              'bc_gaussian_kn_common_old_kernel.bin',
              'a_cm_kn23_ab_lattice.npz', 'a_cm_kn23_witnesses.py',
              'a_cm_kn23_model.npz']
    hashes = {n: hashlib.sha256((HERE / n).read_bytes()).hexdigest() for n in inputs}
    meta = json.loads((HERE / 'bc_gaussian_kn_common.json').read_text())
    data = np.load(HERE / 'bc_gaussian_kn_common.npz')
    lattice = np.load(HERE / 'a_cm_kn23_ab_lattice.npz')
    upper = read_certificate(HERE / 'bc_gaussian_kn_common_N_derived.bin')
    joint = read_certificate(HERE / 'bc_gaussian_kn_common_J_projected.bin')
    kernel = read_certificate(HERE / 'bc_gaussian_kn_common_old_kernel.bin')
    for c in (upper, joint, kernel):
        verify_words(c)
    source = data['actual_common_N']
    points = data['retained_projection_points']
    inverse = np.full(source.shape[1], -1, dtype=np.int64)
    inverse[points] = np.arange(len(points))
    indices = meta['actual_N_source']['selected_original_indices']
    assert np.array_equal(upper['original'], source[indices])
    assert np.array_equal(inverse[upper['strong'][:, points]],
                          data['actual_projected_Nprime_generators'])
    W = Words()
    originals = [W.make(1, i) for i in range(97)]
    upper_nodes = W.substitute(upper, [originals[i] for i in indices])
    extra_nodes = []
    for j in range(2, 97):
        n = 0
        for i, exponent in enumerate(lattice['unimodular_columns'][:, j]):
            if exponent:
                n = W.product(n, W.power(originals[i], int(exponent)))
        extra_nodes.append(W.power(n, 6))
    assert np.array_equal(joint['original'], data['whole_J_input_generators'])
    assert len(joint['original']) == len(upper_nodes) + 95
    joint_nodes = W.substitute(joint, upper_nodes + extra_nodes)
    kernel_indices = data['kernel_strong_indices_in_joint']
    assert np.array_equal(kernel['original'],
                          joint['strong'][kernel_indices, 7501:] - 7501)
    kernel_nodes = W.substitute(kernel, [joint_nodes[int(i)] for i in kernel_indices])
    checks = {}
    for kind, nodes in [('joint', joint_nodes), ('kernel', kernel_nodes), ('extra', extra_nodes)]:
        for j, node in enumerate(nodes):
            checks.setdefault(node, []).append((kind, j))
    ancestors = set(checks)
    todo = list(ancestors)
    while todo:
        op, a, b = W.nodes[todo.pop()]
        for node in ([a, b] if op in (2, 4, 5) else [a] if op == 3 else []):
            if node not in ancestors:
                ancestors.add(node)
                todo.append(node)
    refs = np.zeros(len(W.nodes), dtype=np.int64)
    for node in ancestors:
        op, a, b = W.nodes[node]
        for i in ([a, b] if op in (2, 4, 5) else [a] if op == 3 else []):
            refs[i] += 1
    one = np.arange(source.shape[1], dtype=np.uint16)
    exponent_matrix = lattice['integral_exponent_matrix']
    original_ab = np.eye(97, dtype=np.int8)
    values, exponents, abelian = {}, {}, {}
    checked = 0
    peak = 0

    def pinv(p):
        q = np.empty_like(p)
        q[p] = one
        return q

    for node in sorted(ancestors):
        op, a, b = W.nodes[node]
        if op == 0:
            p, e, v = one, (0, 0), np.zeros(97, dtype=np.int8)
        elif op == 1:
            p = source[a]
            e = tuple(map(int, exponent_matrix[:, a]))
            v = original_ab[a]
        elif op == 2:
            p = values[b][values[a]]
            e = tuple(x+y for x, y in zip(exponents[a], exponents[b]))
            v = (abelian[a]+abelian[b]) % 6
        elif op == 3:
            p, e, v = pinv(values[a]), tuple(-x for x in exponents[a]), -abelian[a] % 6
        elif op == 4:
            p = pinv(values[b])[pinv(values[a])[values[b][values[a]]]]
            e, v = (0, 0), np.zeros(97, dtype=np.int8)
        elif op == 5:
            p = pinv(values[a])[values[b][values[a]]]
            e, v = exponents[b], abelian[b]
        else:
            raise AssertionError(op)
        values[node], exponents[node], abelian[node] = p, e, v
        if node in checks:
            projected = inverse[p[points]]
            assert np.all(projected >= 0)
            for kind, j in checks[node]:
                assert e == (0, 0) and not np.any(v), (kind, j)
                if kind == 'joint':
                    assert np.array_equal(projected, joint['strong'][j])
                elif kind == 'kernel':
                    assert np.array_equal(projected[:7501], np.arange(7501))
                    assert np.array_equal(projected[7501:]-7501, kernel['strong'][j])
                else:
                    assert np.array_equal(p[:11691], lattice['kernel_basis_sixth_full_values'][j])
                    assert np.array_equal(p[11691:]-11691, data['actual_gaussian_sixth_values'][j])
                checked += 1
        peak = max(peak, len(values))
        for i in ([a, b] if op in (2, 4, 5) else [a] if op == 3 else []):
            refs[i] -= 1
            if refs[i] == 0:
                values.pop(i)
                exponents.pop(i)
                abelian.pop(i)
        if refs[node] == 0:
            values.pop(node)
            exponents.pop(node)
            abelian.pop(node)
    out = {'status': 'PASS_ALL_LITERAL_WHOLE_J_COMMON_AND_KERNEL_WORDS',
           'source_degree': int(source.shape[1]),
           'retained_degree': len(points), 'literal_N_generator_count': 97,
           'joint_basis_words_checked': len(joint_nodes),
           'kernel_basis_words_checked': len(kernel_nodes),
           'additional_lattice_sixth_words_checked': 95,
           'all_checked_words': checked, 'global_word_DAG_nodes': len(W.nodes),
           'actual_ancestors_replayed': len(ancestors), 'peak_retained_permutations': peak,
           'all_checked_words_have_zero_integral_F_exponents': True,
           'all_checked_words_have_zero_N_exponents_mod_six': True,
           'old_kernel_words_kill_entire_retained_E71_image': True,
           'unretained_E71_coordinates_not_assigned_identity': True,
           'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'input_sha256': hashes, 'seconds': round(time.monotonic()-start, 6)}
    np.savez_compressed(HERE / (STEM + '.npz'),
                        literal_N_word_DAG=np.array(W.nodes, dtype=np.uint32),
                        joint_strong_word_nodes=np.array(joint_nodes, dtype=np.uint32),
                        old_kernel_strong_word_nodes=np.array(kernel_nodes, dtype=np.uint32),
                        extra_sixth_word_nodes=np.array(extra_nodes, dtype=np.uint32))
    (HERE / (STEM + '.json')).write_text(json.dumps(out, indent=2) + '\n')
    assert all(hashlib.sha256((HERE / n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
