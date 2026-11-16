"""Independent audit of the full 24-line boundary normalization.

Uses the saved exact representation, not the other agent's group-order
or nilpotency code. Signed permutation inversion is simply transposition.
"""
from pathlib import Path
import json
import numpy as np

root = Path(__file__).resolve().parents[2] / 'agent_five'
data = np.load(root / 'ferrari_open_prym72.npz')
X = data['X'].astype(np.int64)
n = len(data['character_list'])
assert n == 24
boundary = [matrix[::3, ::3] % 3 for matrix in X]
I = np.eye(n, dtype=np.int64)


def product(*matrices):
    out = I
    for matrix in matrices:
        out = out @ matrix % 3
    return out


records = []
for i, j in ((0, 1), (1, 2), (2, 3), (4, 0), (3, 4)):
    A, B = boundary[i], boundary[j]
    assert np.array_equal(A @ A.T % 3, I)
    assert np.array_equal(B @ B.T % 3, I)
    W = product(A, B, A.T, B.T)
    assert np.array_equal(W @ A % 3, A @ W % 3)
    assert np.array_equal(W @ B % 3, B @ W % 3)
    records.append({'pair': [i+1, j+1],
                    'commutator_central_on_all_24_lines': True})

normalized = np.load(root / 'ferrari_open_prym_affine72.npz')['X'].astype(np.int64)
assert np.array_equal(normalized[2], normalized[0])
assert np.array_equal(normalized[4], normalized[3])
assert np.array_equal(normalized[3] @ normalized[0] % 3,
                      normalized[0] @ normalized[3] % 3)
assert np.array_equal(normalized[3] @ normalized[1] % 3,
                      normalized[1] @ normalized[3] % 3)

print(json.dumps({'boundary_dimension': n,
                  'pair_checks': records,
                  'normalized_X3_equals_X1': True,
                  'normalized_X5_equals_X4': True,
                  'normalized_X4_centralizes_X1_X2': True,
                  'logical_scope': 'The boundary-line twist preserves gamma_3(F) evaluations. For actual gentle f, the normalized pentagon is the two-cycle identity. The linear homology conclusion does not kill the affine D/(D_prime*D_cubes) class.'},
                 indent=2))
