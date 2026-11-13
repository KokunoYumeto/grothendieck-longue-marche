#!/usr/bin/env python3
"""Exact integral Frobenius/Smith bound for the saturated local kernel R.

This reconstructs the A.7 graph lattice directly from its eight cusp
labels and computes the c-fixed exterior-square operator at norm289.
It does not assign the still unevaluated cochain matrix E_phi mod243.
"""
from itertools import combinations
from pathlib import Path
import json
from sympy import Matrix, eye, zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form

labels = [(1, 0), (-1, 0), (-1, -1), (0, 1),
          (1, 1), (0, -1), (-1, 1), (1, -1)]
Psi = Matrix([[b, -a] for a, b in labels])
permutation = [0, 1, 3, 2, 5, 4, 7, 6]
Pc = zeros(8)
for j, i in enumerate(permutation):
    Pc[i, j] = 1
CT = Matrix([[1, -1], [0, -1]])


def graph_action(w, t):
    off = (w * Psi - Psi * t) / 3
    assert all(a.q == 1 for a in off)
    return w.row_join(off).col_join(zeros(2, 8).row_join(t))


C = graph_action(-Pc, CT)
F = graph_action(289 * eye(8), -17 * eye(2))
assert F[:8, 8:] == 102 * Psi
assert C * C == eye(10) and F * C == C * F

# y^2+y=x^3-7 has eighteen points over F17, hence trace zero.
points = [(x, y) for x in range(17) for y in range(17)
          if (y*y+y-x*x*x+7) % 17 == 0]
assert len(points) + 1 == 18
assert len({pow(x, 3, 17) for x in range(17)}) == 17

pairs = list(combinations(range(10), 2))


def wedge(a):
    return Matrix([[a[i, k] * a[j, l] - a[i, l] * a[j, k]
                    for k, l in pairs] for i, j in pairs])


C2 = wedge(C)
F2 = wedge(F)
assert C2 * C2 == eye(45) and C2 * F2 == F2 * C2
projector_twice = eye(45) + C2
mod3 = [[int(a) % 3 for a in row] for row in projector_twice.tolist()]
pivots = []
r = 0
for j in range(45):
    pivot = next((i for i in range(r, 45) if mod3[i][j]), None)
    if pivot is None:
        continue
    mod3[r], mod3[pivot] = mod3[pivot], mod3[r]
    factor = mod3[r][j]
    mod3[r] = [a * factor % 3 for a in mod3[r]]
    for i in range(45):
        if i != r:
            factor = mod3[i][j]
            mod3[i] = [(a - factor * b) % 3
                       for a, b in zip(mod3[i], mod3[r])]
    pivots.append(j)
    r += 1
assert len(pivots) == 21
S = projector_twice[:, pivots]
assert C2 * S == S
assert not any(S[44, :])  # the proper exterior-square coordinate is c-minus
B_rectangular = (F2 - eye(45)) * S
row_indices = list(S.T.rref()[1])
S_minor = S[row_indices, :]
assert S_minor.det() % 3 != 0
B = S_minor.inv() * B_rectangular[row_indices, :]
assert all(a.q == 1 for a in B)
assert S * B == B_rectangular


def v3_integer(n):
    n = abs(int(n))
    assert n
    value = 0
    while n % 3 == 0:
        value += 1
        n //= 3
    return value


diagonal = smith_normal_form(B, domain=ZZ)
values = [v3_integer(diagonal[i, i]) for i in range(21)]
assert values == [1]*6 + [2]*7 + [3]*2 + [4]*6
rectangular_diagonal = smith_normal_form(B_rectangular, domain=ZZ)
assert [v3_integer(rectangular_diagonal[i, i]) for i in range(21)] == values
assert B.det() == 83520**13 * 4914**8
assert sum(values) == 50

B_inverse = B.inv()
denominator_valuations = [v3_integer(a.q) for a in B_inverse if a]
assert max(denominator_valuations) == 4
assert all((81*a).q % 3 != 0 for a in B_inverse)
assert any((27*a).q % 3 == 0 for a in B_inverse)
assert B * B_inverse == eye(21)

# A second Smith calculation, by pivoting modulo 3^8, independently checks
# the valuations without using integer Smith transformations.
precision = 8
modulus = 3**precision
work = [[int(a) % modulus for a in row] for row in B.tolist()]
modular_values = []


def valuation_mod(n):
    if n == 0:
        return precision
    return v3_integer(n)


for k in range(21):
    valuation, i, j = min((valuation_mod(work[i][j]), i, j)
                          for i in range(k, 21) for j in range(k, 21))
    assert valuation < precision
    work[k], work[i] = work[i], work[k]
    for row in work:
        row[k], row[j] = row[j], row[k]
    pivot = 3**valuation
    scale = pow(work[k][k] // pivot, -1, modulus)
    work[k] = [a * scale % modulus for a in work[k]]
    assert work[k][k] == pivot
    for i in range(k + 1, 21):
        assert work[i][k] % pivot == 0
        factor = work[i][k] // pivot
        work[i] = [(a - factor*b) % modulus
                   for a, b in zip(work[i], work[k])]
        assert work[i][k] == 0
    for j in range(k + 1, 21):
        assert work[k][j] % pivot == 0
        factor = work[k][j] // pivot
        for i in range(21):
            work[i][j] = (work[i][j] - factor*work[i][k]) % modulus
        assert work[k][j] == 0
    modular_values.append(valuation)
assert modular_values == values

output = {
    'curve': 'y^2+y=x^3-7',
    'F17_point_count': len(points) + 1,
    'F17_trace': 0,
    'proper_norm289_Frobenius': '-17 times identity',
    'Weil_graph_matrix': Psi.tolist(),
    'V_norm289_Frobenius': F.tolist(),
    'V_complex_conjugation': C.tolist(),
    'M2_c_plus_basis_columns': pivots,
    'M2_c_plus_basis_matrix': S.tolist(),
    'coordinate_row_indices': row_indices,
    'Frobenius_minus_one_on_c_plus': B.tolist(),
    'Smith_3adic_exponents': values,
    'Smith_multiplicities': {str(a): values.count(a) for a in sorted(set(values))},
    'determinant_formula': '83520^13 * 4914^8',
    'determinant_3adic_valuation': 50,
    'maximum_inverse_denominator_3adic_valuation': 4,
    'modular_Smith_check_precision': precision,
    'sufficient_E_phi_precision': 5,
    'sufficient_E_phi_modulus': 243,
    'exact_R_mod3_formula': 'image modulo3 of ker(E_phi:D/243D -> M2^c/243M2^c)',
    'exact_correction': 'h=(F_phi-1)^(-1)E_phi(d) in3 M2^c; gamma=d-delta(h)',
    'scope': ('The exact integral precision bound and its matrix are computed. '
              'The separate arithmetic matrix E_phi modulo243 is not assigned.'),
    'status': 'PASS'
}
encoded = json.dumps(output, indent=2, default=int) + '\n'
print(encoded, end='')
Path(__file__).with_suffix('.json').write_text(encoded)
