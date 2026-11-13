#!/usr/bin/env python3
"""An individually specified integral class-two section excluded at seventeen.

The script constructs the actual saturated n-fixed/c-minus lattice in
Lambda^2 V, records its proper-wedge direction, and evaluates the
independently certified gluing maps on that integral cocycle.
"""
from itertools import combinations, product
from pathlib import Path
import json
import numpy as np
from sympy import Matrix, eye, zeros

HERE = Path(__file__).resolve().parent
names = ['e_P', 'e_Qc', 'e_A', 'e_Abar', 'e_B', 'e_Bbar',
         'e_C', 'e_Cbar', 't1_graph', 't2_graph']
labels = [(1, 0), (-1, 0), (-1, -1), (0, 1),
          (1, 1), (0, -1), (-1, 1), (1, -1)]
Psi = Matrix([[b, -a] for a, b in labels])
Pc = zeros(8)
for j, i in enumerate([0, 1, 3, 2, 5, 4, 7, 6]):
    Pc[i, j] = 1
CT = Matrix([[1, -1], [0, -1]])
TU = Matrix([[1, -3], [3, -2]])
TV = Matrix([[-2, 3], [-3, 1]])


def graph(w, t):
    off = (w * Psi - Psi * t) / 3
    assert all(a.q == 1 for a in off)
    return w.row_join(off).col_join(zeros(2, 8).row_join(t))


U = graph(7*eye(8), TU)
V = graph(7*eye(8), TV)
C = graph(-Pc, CT)
assert U*V == V*U and C*U*C == V
MV = U*V
NV = V*U.inv()
pairs = list(combinations(range(10), 2))
pair_index = {pair: i for i, pair in enumerate(pairs)}


def wedge(a):
    return Matrix([[a[i, k]*a[j, l]-a[i, l]*a[j, k]
                    for k, l in pairs] for i, j in pairs])


M2 = wedge(MV)
N2 = wedge(NV)
C2 = wedge(C)
assert M2*N2 == N2*M2 and M2*C2 == C2*M2
assert C2*N2*C2 == N2.inv()


def mod3(a):
    return np.array([[int(x.p) * pow(int(x.q), -1, 3) % 3 for x in row]
                     for row in Matrix(a).tolist()], dtype=np.int64)


def pivot_columns(a):
    r = 0
    a = np.asarray(a, dtype=np.int64).copy() % 3
    pivots = []
    for j in range(a.shape[1]):
        ids = np.flatnonzero(a[r:, j])
        if not len(ids):
            continue
        i = r + int(ids[0])
        a[[r, i]] = a[[i, r]]
        a[r] = a[r] * int(a[r, j]) % 3
        for k in range(a.shape[0]):
            if k != r and a[k, j]:
                a[k] = (a[k] - a[k, j] * a[r]) % 3
        pivots.append(j)
        r += 1
        if r == a.shape[0]:
            break
    return pivots


def solve_full_column(a, b):
    a = np.asarray(a, dtype=np.int64) % 3
    b = np.asarray(b, dtype=np.int64) % 3
    if b.ndim == 1:
        b = b[:, None]
    joined = np.hstack((a, b))
    n = a.shape[1]
    for j in range(n):
        i = j + int(np.flatnonzero(joined[j:, j])[0])
        joined[[j, i]] = joined[[i, j]]
        joined[j] = joined[j] * int(joined[j, j]) % 3
        for k in range(joined.shape[0]):
            if k != j and joined[k, j]:
                joined[k] = (joined[k] - joined[k, j] * joined[j]) % 3
    assert not np.any(joined[n:, n:])
    answer = joined[:n, n:]
    assert np.array_equal(a @ answer % 3, b)
    return answer


b0 = zeros(45, 1)
b0[pair_index[(8, 9)]] = 3
for i in range(8):
    b0[pair_index[(i, 8)]] = Psi[i, 1]
    b0[pair_index[(i, 9)]] = -Psi[i, 0]
assert N2*b0 == b0
b = (eye(45)-C2)*b0
assert N2*b == b and C2*b == -b
assert b[44] == 6
assert all(a.q == 1 for a in b)

# Fifteen actual toric anti-invariants and the extra integral direction.
toric_indices = [i for i, pair in enumerate(pairs) if pair[1] < 8]
toric_inclusion = eye(45)[:, toric_indices]
toric_anti = (eye(45)-C2)*toric_inclusion
toric_pivots = pivot_columns(mod3(toric_anti))
assert len(toric_pivots) == 15
toric_basis = toric_anti[:, toric_pivots]
L0 = toric_basis.row_join(b)
assert N2*L0 == L0 and C2*L0 == -L0
assert len(pivot_columns(mod3(L0))) == 16
assert (N2-eye(45)).col_join(C2+eye(45)).rank() == 29
row_pivots = pivot_columns(mod3(L0).T)
minor = L0[row_pivots, :]
assert int(minor.det()) % 3 != 0
M_L0 = minor.inv()*(M2*L0)[row_pivots, :]
assert L0*M_L0 == M2*L0
assert all(int(a.q) % 3 for a in M_L0)
assert all(int(a.q) % 3 for a in M_L0.inv())

# A compact exact expansion of b, checked against every wedge coordinate.
d = zeros(10, 1)
e = zeros(10, 1)
for i, coefficient in ((2, -1), (3, 1), (4, 1), (5, -1)):
    d[i] = coefficient
e[6], e[7] = 1, -1
toric_piece = Matrix([d[i]*e[j]-d[j]*e[i] for i, j in pairs])
assert b == 2*b0 + toric_piece

# The actual unimodular A.7-to-Schreier comparison.
lattice = json.loads((HERE/'a_ihara_lattice.json').read_text())
P = Matrix(lattice['A7_to_Schreier_basis'])
assert abs(P.det()) == 1
P2 = wedge(P)
assert all(a.q == 1 for a in P2.inv())
schreier_L0 = mod3(P2*L0)
small = np.load(HERE/'a_ihara_gamma2_action_certificate.npz')
for label, original in (('m', M2), ('n', N2), ('c', C2)):
    actual = small['action_'+label][:45, :45].astype(np.int64)
    assert np.array_equal(actual @ mod3(P2) % 3, mod3(P2*original))

glue = np.load(HERE/'a_frobenius17_mixed_gluing_local_certificate.npz')
source_n_basis = glue['source_n'][:45, 21:45].astype(np.int64)
n_coordinates = solve_full_column(source_n_basis, schreier_L0)
source_coordinates = np.vstack((np.zeros((21, 16), dtype=np.int64), n_coordinates))
assert not np.any(source_coordinates[:21])

audit = np.load(HERE/'bc_gluing_audit_certificate.npz')
known = audit['known'].astype(np.int64)
unknown = audit['unknown'].astype(np.int64)
remove_h = audit['common_local_quotient'].astype(np.int64)
values = remove_h @ known[:, :45] @ source_coordinates % 3
changes = np.stack([remove_h @ a[:, :45] @ source_coordinates % 3 for a in unknown])
assert not np.any(values[:, :15])
assert not np.any(changes)
explicit_value = values[:, 15]
assert np.count_nonzero(explicit_value) == 87
case_values = []
for coefficients in product(range(3), repeat=3):
    total = values[:, 15].copy()
    for coefficient, index in zip(coefficients, (0, 1, 4)):
        total += coefficient*changes[index, :, 15]
    total %= 3
    assert np.array_equal(total, explicit_value)
    case_values.append({'coefficients': list(coefficients),
                        'same_nonzero_vector': True})

# Select a compact, explicit linear functional detecting this obstruction.
Q = glue['target_quotient'].astype(np.int64)
functionals = remove_h @ Q % 3
candidates = [i for i, value in enumerate(explicit_value) if value]
chosen = min(candidates, key=lambda i: (np.count_nonzero(functionals[i]), i))
normalization = int(explicit_value[chosen])  # its own inverse in F3
functional = normalization*functionals[chosen] % 3
row_on_149 = normalization*remove_h[chosen] % 3
x = source_coordinates[:, 15]
assert int(row_on_149 @ known[:, :45] @ x % 3) == 1
assert all(int(row_on_149 @ a[:, :45] @ x % 3) == 0 for a in unknown)
assert not np.any(row_on_149 @ known[:, 45:] % 3)
assert all(not np.any(row_on_149 @ a[:, 45:] % 3) for a in unknown)
old = json.loads((HERE/'a_frobenius17_eval_m3.json').read_text())
global_image = (small['A7_to_Schreier_M3'].astype(np.int64)
                @ np.array(old['evaluation_image_mod3_basis'], dtype=np.int64)) % 3
assert not np.any(functional @ global_image % 3)
C3 = small['action_c'][45:, 45:].astype(np.int64)
assert np.array_equal(functional @ C3 % 3, functional)
M3_basis = json.loads((HERE/'a_ihara_gamma2_action.json').read_text())['basis_M3']
functional_terms = [{'index': i, 'coefficient': int(a), 'basis': M3_basis[i]}
                    for i, a in enumerate(functional) if a]

nonzero_b = [{'pair': list(pairs[i]), 'basis_names': [names[j] for j in pairs[i]],
              'coefficient': int(a)} for i, a in enumerate(b) if a]
out = {
    'ordered_A7_basis': names,
    'Weil_graph_matrix': Psi.tolist(),
    'b0_coordinates': list(b0),
    'b_coordinates': list(b),
    'b_nonzero_entries': nonzero_b,
    'b_proper_wedge_coefficient': 6,
    'exact_cocycle_values': {'m': '0', 'n': 'b', 'c': '0'},
    'integral_lattice_rank': 16,
    'toric_anti_invariant_rank': 15,
    'toric_basis_columns': toric_pivots,
    'full_integral_lattice_basis': L0.tolist(),
    'm_action_on_integral_lattice': [[str(a) for a in row] for row in M_L0.tolist()],
    'n_action_on_integral_lattice': 'identity',
    'c_action_on_integral_lattice': 'minus identity',
    'primitive_mod3_rank': 16,
    'A7_to_Schreier_basis': P.tolist(),
    'Schreier_b_mod3': schreier_L0[:, 15].tolist(),
    'normalized_source_coordinates_mod3': x.tolist(),
    'gluing_vector_dimension': 143,
    'gluing_vector': explicit_value.tolist(),
    'gluing_vector_nonzero_entries': int(np.count_nonzero(explicit_value)),
    'all_unknown_maps_vanish_on_entire_rank16_lattice_mod3': True,
    'toric_rank15_known_map_vanishes': True,
    'all_27_cases': case_values,
    'detector_functional_terms': functional_terms,
    'detector_value': 1,
    'detector_kills_global_M3_image': True,
    'detector_kills_all_local_conjugator_parameters': True,
    'detector_kills_all_unknown_word_values_on_b': True,
    'scope': ('An actual integral normalized cocycle in R, defined by its generator '
              'values. Its class-two target has exactly the local O-cusp packet '
              'at17, and its first gluing obstruction has detector value1. '
              'A40 therefore excludes every lift to N/gamma5 and the full, '
              'metabelian, and marked quotients.'),
    'status': 'PASS'
}
encoded = json.dumps(out, indent=2, default=int) + '\n'
print(encoded, end='')
Path(__file__).with_suffix('.json').write_text(encoded)
np.savez_compressed(HERE/'bc_explicit17_certificate.npz',
                    source_coordinates=source_coordinates.astype(np.int8),
                    gluing_on_lattice=values.astype(np.int8),
                    detector_functional=functional.astype(np.int8),
                    detector_row_on_gluing_target=row_on_149.astype(np.int8))
