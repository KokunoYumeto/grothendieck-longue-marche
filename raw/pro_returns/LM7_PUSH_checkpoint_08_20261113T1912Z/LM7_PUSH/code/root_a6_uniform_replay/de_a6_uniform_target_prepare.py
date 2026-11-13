#!/usr/bin/env python3
"""Actual A6 Nielsen / level-five projective symplectic target comparison."""
from pathlib import Path
from hashlib import sha256
import json, time
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup
from de_ferrari_a6_model import FerrariA6

HERE = Path(__file__).resolve().parent
STEM = 'de_a6_uniform_target'


def main():
    started = time.time()
    names = ['de_ferrari_a6_model.py', 'de_ferrari_a6_model.json',
             'de_ferrari_sl2_5_model.json']
    hashes = {n: sha256((HERE / n).read_bytes()).hexdigest() for n in names}
    A = FerrariA6()
    # In the exact E56 conjugation by J^{-1}, the right transvections become
    # T_a(-1), T_b(-1), T_{c-a}(-1). Their quotient on W is U(-1),L(1),U(-1).
    matrices = [np.array([[1, -1], [0, 1]]), np.array([[1, 0], [1, 1]]),
                np.array([[1, -1], [0, 1]])]
    points = [(1, j) for j in range(5)] + [(0, 1)]
    def canonical(v):
        v = np.array(v) % 5
        if v[0]:
            return 1, int(v[1] * pow(int(v[0]), -1, 5) % 5)
        assert v[1]
        return 0, 1
    projected = []; joint = []; base = []
    for name, matrix in zip(('a', 'b', 'c'), matrices):
        inverse = np.array([[matrix[1, 1], -matrix[0, 1]],
                            [-matrix[1, 0], matrix[0, 0]]]) % 5
        p = np.array([points.index(canonical(inverse @ v)) for v in points], dtype=np.int64)
        actual = np.array(A.permutation(getattr(A, name), True).array_form, dtype=np.int64)
        assert len(actual) == 530
        projected.append(p); base.append(actual); joint.append(np.r_[actual, 530 + p])
    assert int(PermutationGroup([Permutation(p) for p in projected]).order()) == 60
    for generators in (projected, joint):
        a, b, c = generators
        assert np.array_equal(a[b[a]], b[a[b]])
        assert np.array_equal(b[c[b]], c[b[c]])
        assert np.array_equal(a[c], c[a])
    with (HERE / (STEM + '.input')).open('w') as f:
        f.write('536 3\n')
        for p in joint:
            f.write(' '.join(map(str, p)) + '\n')
    np.savez_compressed(HERE / (STEM + '_prepare.npz'),
                        actual_A6_Nielsen_generators=np.array(base),
                        actual_projective_generators=np.array(projected),
                        actual_joint_generators=np.array(joint),
                        actual_W_matrices=np.array(matrices))
    out = {'status': 'PASS_LITERAL_TARGET_INPUT', 'degree': 536,
           'specified_projective_map': 'E56 right convention, conjugation by J^-1, quotient c-perp/Tc, modulo5 and scalar quotient',
           'A6_Nielsen_order': json.loads((HERE / names[1]).read_text())['Nielsen_image_order'],
           'projective_matrix_image_order': 60,
           'actual_projective_generator_permutations': [p.tolist() for p in projected],
           'all_braid_relations_verified': True, 'input_sha256': hashes,
           'seconds': round(time.time() - started, 3)}
    (HERE / (STEM + '_prepare.json')).write_text(json.dumps(out, indent=2) + '\n')
    assert all(sha256((HERE / n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps(out, indent=2), flush=True)


if __name__ == '__main__':
    main()
