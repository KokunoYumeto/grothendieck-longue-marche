#!/usr/bin/env python3
"""Independent finite-image certificate for the normalized A.38 action.

The inputs are the actual 55-dimensional matrices retained in the
arithmetic certificate.  This program reconstructs their input maps,
computes the full normal commutator module, enumerates the image group,
and evaluates the actual D3/D4 Frobenius word from A.31.
"""
from collections import deque
from itertools import product
from pathlib import Path
import hashlib
import importlib.util
import json
import numpy as np

HERE = Path(__file__).resolve().parent
INPUT = HERE / 'a_ihara_gamma2_action_certificate.npz'
data = np.load(INPUT)
small = {name: data['small_' + name].astype(np.int64)
         for name in ('u', 'v', 'c', 'm', 'n')}
I = np.eye(55, dtype=np.int64)
I10 = np.eye(10, dtype=np.int64)
PAIRS = [(i, j) for i in range(10) for j in range(i + 1, 10)]


def mm(a, b):
    return a @ b % 3


def power(a, n):
    out = np.eye(a.shape[0], dtype=np.int64)
    while n:
        if n & 1:
            out = mm(out, a)
        a = mm(a, a)
        n //= 2
    return out


def inverse(a):
    n = a.shape[0]
    aug = np.hstack((a, np.eye(n, dtype=np.int64))) % 3
    for col in range(n):
        pivot = next(row for row in range(col, n) if aug[row, col])
        aug[[col, pivot]] = aug[[pivot, col]]
        aug[col] = aug[col] * int(aug[col, col]) % 3
        for row in range(n):
            if row != col and aug[row, col]:
                aug[row] = (aug[row] - aug[row, col] * aug[col]) % 3
    result = aug[:, n:]
    assert np.array_equal(mm(a, result), np.eye(n, dtype=np.int64))
    return result


def comm(a, b):
    return mm(mm(mm(a, b), inverse(a)), inverse(b))


def order3(a):
    b = a.copy()
    order = 1
    while not np.array_equal(b, np.eye(a.shape[0], dtype=np.int64)):
        b = power(b, 3)
        order *= 3
        assert order <= 3**8
    return order


def sqrt_pro3(a):
    order = order3(a)
    result = power(a, (order + 1) // 2)
    assert np.array_equal(mm(result, result), a)
    return result


def exterior(a):
    return np.asarray([
        [((a[i, k] * a[j, l] - a[i, l] * a[j, k]) % 3)
         for k, l in PAIRS]
        for i, j in PAIRS], dtype=np.int64)


def action(a, j):
    return np.block([[a, np.zeros((10, 45), dtype=np.int64)],
                     [j, exterior(a)]]) % 3


def independent_columns(a):
    """Return actual original columns forming a basis, with exact elimination."""
    a = np.asarray(a, dtype=np.int64) % 3
    if a.shape[1] == 0:
        return a
    reduced = a.copy()
    row = 0
    pivots = []
    for col in range(a.shape[1]):
        candidates = np.flatnonzero(reduced[row:, col])
        if not len(candidates):
            continue
        pivot = row + int(candidates[0])
        reduced[[row, pivot]] = reduced[[pivot, row]]
        reduced[row] = reduced[row] * int(reduced[row, col]) % 3
        for other in range(a.shape[0]):
            if other != row and reduced[other, col]:
                reduced[other] = (reduced[other]
                                  - reduced[other, col] * reduced[row]) % 3
        pivots.append(col)
        row += 1
        if row == a.shape[0]:
            break
    return a[:, pivots]


def kernel_matrix(a):
    """Identify an actual identity-linear automorphism with its additive J block."""
    assert np.array_equal(a[:10, :10], I10)
    assert not np.any(a[:10, 10:])
    assert np.array_equal(a[10:, 10:], np.eye(45, dtype=np.int64))
    return a[10:, :10].copy()


def kernel_element(j):
    out = I.copy()
    out[10:, :10] = j % 3
    return out


def adjoint(a, columns):
    aa = a[:10, :10]
    wa = exterior(aa)
    ia = inverse(aa)
    if columns.shape[1] == 0:
        return columns.copy()
    return np.stack([(wa @ columns[:, j].reshape(45, 10) @ ia % 3).reshape(-1)
                     for j in range(columns.shape[1])], axis=1)


def normal_span(columns):
    basis = independent_columns(columns)
    while True:
        larger = independent_columns(np.hstack((basis, adjoint(M, basis),
                                                adjoint(N, basis))))
        if larger.shape[1] == basis.shape[1]:
            return larger
        basis = larger


# Reconstruct the genuine input actions from the separately saved A.38 word.
spec = importlib.util.spec_from_file_location('bc_fermat_collector',
                                             HERE / 'de_fermat_schreier.py')
collector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(collector)
raw = json.loads((HERE / 'a_ihara_final_parameters.json').read_text())
ua, uj = collector.generator_images(np.array(raw['base_fa'], dtype=np.int64),
                                    np.array(raw['base_fz'], dtype=np.int64), 7)
ca, cj = collector.generator_images(*collector.zero(), chi=8)
U = action(ua, uj)
C = action(ca, cj)
V = mm(mm(C, U), C)
assert np.array_equal(mm(C, C), I)
assert all(np.array_equal(a, small[name]) for name, a in
           (('u', U), ('v', V), ('c', C)))
UV = mm(U, V)
d0 = mm(mm(U, C), inverse(sqrt_pro3(UV)))
h0 = sqrt_pro3(mm(d0, C))
M = mm(mm(inverse(h0), UV), h0)
N = mm(V, inverse(U))
assert np.array_equal(M, small['m']) and np.array_equal(N, small['n'])
assert np.array_equal(mm(C, M), mm(M, C))
assert np.array_equal(mm(mm(C, N), C), inverse(N))

for a in (U, V, M, N, C):
    assert not np.any(a[:10, 10:])
    assert np.array_equal(a[10:, 10:], exterior(a[:10, :10]))
assert np.array_equal(mm(M[:10, :10], N[:10, :10]),
                      mm(N[:10, :10], M[:10, :10]))
assert np.array_equal(power(M[:10, :10], 3), I10)
assert np.array_equal(power(N[:10, :10], 3), I10)
linear_images = {mm(power(M[:10, :10], i), power(N[:10, :10], j)).tobytes()
                 for i, j in product(range(3), repeat=2)}
assert len(linear_images) == 9

mn = comm(M, N)
mn_j = kernel_matrix(mn)
gamma2 = normal_span(mn_j.reshape(450, 1))
lower_central = [gamma2]
while lower_central[-1].shape[1]:
    previous = lower_central[-1]
    images = np.hstack(((adjoint(M, previous) - previous) % 3,
                        (adjoint(N, previous) - previous) % 3))
    lower_central.append(normal_span(images))
assert [a.shape[1] for a in lower_central] == [2, 1, 0]

power_seeds = np.stack([kernel_matrix(power(M, 3)).reshape(-1),
                        kernel_matrix(power(N, 3)).reshape(-1)], axis=1)
kernel = normal_span(np.hstack((gamma2, power_seeds)))
assert kernel.shape[1] == 3
assert np.array_equal(power(N, 3), I)
assert not np.array_equal(power(M, 3), I)
Z0 = kernel_matrix(power(M, 3)).reshape(-1)
Z1 = kernel_matrix(comm(M, N)).reshape(-1)
Z2 = kernel_matrix(comm(M, comm(M, N))).reshape(-1)
Z = np.stack((Z0, Z1, Z2), axis=1)
assert independent_columns(Z).shape[1] == 3
ad_m = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1]], dtype=np.int64)
ad_n = np.eye(3, dtype=np.int64)
assert np.array_equal(adjoint(M, Z), Z @ ad_m % 3)
assert np.array_equal(adjoint(N, Z), Z @ ad_n % 3)

# Every represented normal form is an actual group element: the basis vectors
# are sums of conjugated commutator/power words, and their matrices commute.
normal_forms = {}
for i, j in product(range(3), repeat=2):
    coset = mm(power(M, i), power(N, j))
    for coefficients in product(range(3), repeat=kernel.shape[1]):
        kj = (kernel @ np.array(coefficients, dtype=np.int64) % 3).reshape(45, 10)
        element = mm(kernel_element(kj), coset)
        normal_forms[element.astype(np.int8).tobytes()] = element
assert len(normal_forms) == 243

# Independent literal generator traversal of the complete finite matrix image.
key_i = I.astype(np.int8).tobytes()
generated = {key_i: I}
todo = deque([I])
while todo:
    element = todo.popleft()
    for generator in (M, N):
        nxt = mm(element, generator)
        key = nxt.astype(np.int8).tobytes()
        if key not in generated:
            generated[key] = nxt
            todo.append(nxt)
assert generated.keys() == normal_forms.keys()
assert len(generated) == 243

# The linear image has exponent three; cubes therefore lie in the additive
# identity-linear kernel, which itself has exponent three.
cube_columns = []
for element in generated.values():
    cube = power(element, 3)
    cube_columns.append(kernel_matrix(cube).reshape(-1))
    assert np.array_equal(power(element, 9), I)
cube_span = independent_columns(np.stack(cube_columns, axis=1))
assert cube_span.shape[1] == 2
assert independent_columns(np.hstack((cube_span, Z[:, [0, 2]]))).shape[1] == 2
D2 = independent_columns(np.hstack((gamma2, cube_span)))
D3 = independent_columns(np.hstack((lower_central[1], cube_span)))
assert [D2.shape[1], D3.shape[1], lower_central[2].shape[1]] == [3, 2, 0]

triple_nnm = comm(N, comm(N, M))
assert np.array_equal(triple_nnm, I)
W17 = mm(power(M, 6), triple_nnm)
assert np.array_equal(W17, power(M, 6)) and not np.array_equal(W17, I)
W17_j = kernel_matrix(W17)
assert independent_columns(W17_j).shape[1] == 2
assert np.array_equal(power(W17, 3), I)
assert np.array_equal(mm(M, W17), mm(W17, M))
assert np.array_equal(mm(N, W17), mm(W17, N))

# The action fixes every actual cusp vector at its first central correction.
cusp_values = W17_j @ collector.CUSP_VECTORS % 3
assert not np.any(cusp_values)

np.savez_compressed(HERE / 'bc_ihara_finite_image_certificate.npz',
                    m=M.astype(np.int8), n=N.astype(np.int8),
                    identity_linear_kernel=kernel.astype(np.int8),
                    Z0_Z1_Z2=Z.astype(np.int8),
                    conjugation_m=ad_m.astype(np.int8),
                    conjugation_n=ad_n.astype(np.int8),
                    gamma2=gamma2.astype(np.int8),
                    gamma3=lower_central[1].astype(np.int8),
                    D2=D2.astype(np.int8), D3=D3.astype(np.int8),
                    W17=W17.astype(np.int8), W17_Johnson=W17_j.astype(np.int8))
output = {
    'input_certificate': INPUT.name,
    'input_sha256': hashlib.sha256(INPUT.read_bytes()).hexdigest(),
    'input_reconstruction': 'A38 word and actual c-equivariant square-root source maps',
    'image_order': len(generated),
    'linear_image_order': len(linear_images),
    'identity_linear_kernel_dimension': kernel.shape[1],
    'kernel_basis': ['J(M^3)', 'J([M,N])', 'J([M,[M,N]])'],
    'conjugation_m_on_kernel_basis': ad_m.tolist(),
    'conjugation_n_on_kernel_basis': ad_n.tolist(),
    'commutator_lower_central_dimensions': [a.shape[1] for a in lower_central],
    'Zassenhaus_D2_D3_D4_dimensions': [D2.shape[1], D3.shape[1], 0],
    'nilpotency_class': 3,
    'exponent': 9,
    'm_order': order3(M),
    'n_order': order3(N),
    'm_cubed_nontrivial': True,
    'n_cubed_identity': True,
    'triple_nnm_identity': True,
    'W17_word': 'm^6 [n,[n,m]]',
    'W17_value': 'M^6',
    'W17_order': order3(W17),
    'W17_Johnson_rank': independent_columns(W17_j).shape[1],
    'W17_Johnson_nonzero_entries': int(np.count_nonzero(W17_j)),
    'W17_Johnson_matrix': W17_j.tolist(),
    'W17_Johnson_kills_all_nine_cusp_vectors': True,
    'exact_killed_source_subgroup': 'D4(P3) = gamma4(P3) gamma2(P3)^3 P3^9',
    'scope': ('The full finite image of the actual normalized A38 action on '
              'N/(N^3 gamma3 N); A31 therefore evaluates the entire W17 action '
              'at this quotient. No assertion is made about higher geometric quotients.'),
    'status': 'PASS'
}
encoded = json.dumps(output, indent=2) + '\n'
print(encoded, end='')
Path(__file__).with_suffix('.json').write_text(encoded)
