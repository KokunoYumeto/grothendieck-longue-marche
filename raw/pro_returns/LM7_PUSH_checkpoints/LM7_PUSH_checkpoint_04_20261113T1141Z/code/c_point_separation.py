#!/usr/bin/env python3
"""Exact tangent-line measurement certificate for the Fermat cubic.

This verifies the finite linear algebra used in C.8--C.9. It is not
a numerical test of Kummer classes or of the geometric section conjecture.
"""
import json
from pathlib import Path
import sympy as sp

I = sp.I
z = (-1 + I * sp.sqrt(3)) / 2
rows = []
cusps = []
for first, second in [(0, 1), (1, 2), (2, 0)]:
    for a in range(3):
        row = [sp.Integer(0)] * 3
        row[first], row[second] = 1, sp.expand_complex(z**a)
        d = [sp.Integer(0)] * 3
        d[first], d[second] = 1, -sp.expand_complex(z**(-a))
        rows.append(sp.Matrix([row]))
        cusps.append(sp.Matrix(d))

def simp(m):
    return m.applyfunc(sp.simplify)

projectors = [simp(row.conjugate().T * row / 2) for row in rows]
zero = sp.zeros(3)
identity = sp.eye(3)
assert simp(sum(projectors, zero) - 3 * identity) == zero
gram = sp.Matrix(9, 9, lambda i, j:
                 sp.simplify(sp.trace(projectors[i] * projectors[j])))
assert gram == (3 * sp.eye(9) + sp.ones(9)) / 4

diagonal = sp.symbols('d0:3', real=True)
real = sp.symbols('r0:3', real=True)
imag = sp.symbols('s0:3', real=True)
unknowns = list(diagonal) + list(real) + list(imag)
H = sp.diag(*diagonal)
for k, (i, j) in enumerate([(0, 1), (0, 2), (1, 2)]):
    H[i, j] = real[k] + I * sp.sqrt(3) * imag[k]
    H[j, i] = real[k] - I * sp.sqrt(3) * imag[k]
measurements = [sp.expand(sp.trace(p * H)).simplify() for p in projectors]
matrix = sp.Matrix([[sp.expand(expr).coeff(v) for v in unknowns]
                    for expr in measurements])
assert matrix.rank() == 9
dual_checks = 0
for i, (p, d) in enumerate(zip(projectors, cusps)):
    dual = 4 * p - identity
    assert sp.simplify((rows[i] * d)[0]) == 0
    assert sp.simplify(sum(x**3 for x in d)) == 0
    assert simp(p * d) == sp.zeros(3, 1)
    assert dual.eigenvals() == {sp.Integer(3): 1, sp.Integer(-1): 2}
    for j, q in enumerate(projectors):
        assert sp.simplify(sp.trace(q * dual)) == (3 if i == j else 0)
        dual_checks += 1

output = {
    'measurement_rank_over_Q': matrix.rank(),
    'measurement_determinant': str(sp.factor(matrix.det())),
    'projector_sum': '3 I_3',
    'projector_gram_diagonal': 1,
    'projector_gram_off_diagonal': '1/4',
    'dual_operator': '4 P_d - I_3',
    'dual_eigenvalues': {'3': 1, '-1': 2},
    'exact_dual_pairings_checked': dual_checks,
    'tangent_lines_annihilate_corresponding_cusps': len(cusps),
    'fermat_cubic_equations_checked': len(cusps),
    'all_assertions_passed': True,
    'measurement_matrix': [[str(x) for x in row] for row in matrix.tolist()],
}
print(json.dumps(output, indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2) + '\n')
