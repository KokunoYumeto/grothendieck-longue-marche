#!/usr/bin/env python3
"""Exact linear elimination in the retained degree-27 relation data.

This certifies a statement about these finite rows.  It computes no
ordinary class group, class bound, or nonprincipality result.
"""
from pathlib import Path
import ast
import hashlib
import json
import re
import sympy as sp

base = Path(__file__).resolve().parent
path = base / 'two_inert_level3_target_relations_pari_output.txt'
raw = path.read_text()
inside = [(2, 1), (2, 2), (2, 3), (2, 4), (3, 1),
          (11, 1), (11, 2), (59, 1), (59, 2)]
rows = []
for line in raw.splitlines():
    match = re.match(r'REL (\d+) TARGET (\d+) JFACT (\[.*?\]) COEFF', line)
    if not match:
        continue
    target = int(match[2])
    c11 = target - 5
    c59 = (4*c11 + 3 + 4) % 9 - 4
    # The retained generator has literal relation I=(generator)*J.
    row = {(2, 1): 1, (11, 1): -2*c11, (11, 2): c11,
           (59, 1): -2*c59, (59, 2): c59}
    for prime, label, exponent in ast.literal_eval(match[3]):
        key = (prime, label)
        row[key] = row.get(key, 0) - exponent
    rows.append(row)

assert len(rows) == 47
outside = sorted(set().union(*(row.keys() for row in rows)) - set(inside))
outside_matrix = sp.Matrix([[row.get(key, 0) for row in rows] for key in outside])
inside_matrix = sp.Matrix([[row.get(key, 0) for row in rows] for key in inside])
basis = outside_matrix.nullspace()
kernel_matrix = sp.Matrix.hstack(*basis)
assert outside_matrix * kernel_matrix == sp.zeros(len(outside), len(basis))
assert len(basis) + outside_matrix.rank() == len(rows)
projected = inside_matrix * kernel_matrix
assert all(x == 0 for x in projected[0, :] - projected[1, :])
assert len(outside) == 77
assert outside_matrix.rank() == 16
assert len(basis) == 31 and projected.rank() == 6

data = {
    'source_sha256': hashlib.sha256(raw.encode()).hexdigest(),
    'retained_rows': len(rows), 'outside_prime_labels': outside,
    'outside_rank': outside_matrix.rank(), 'rational_kernel_dimension': len(basis),
    'inside_prime_labels': inside, 'projected_rank': projected.rank(),
    'kernel_basis': [[str(x) for x in v] for v in basis],
    'projected_basis': [[str(x) for x in v] for v in projected.columnspace()],
    'exact_annihilator': 'coefficient(P0)-coefficient(P2)',
    'scope': 'Every S-supported rational combination of these47 retained rows '
             'has equal P0 and P2 coefficients.  This gives no ideal-class '
             'bound and no arithmetic nonprincipality conclusion.'
}
(base / 'two_inert_retained_relation_projection_data.json').write_text(
    json.dumps(data, indent=2) + '\n')
lines = [
    'PASS: 47 retained rows, 77 outside-S prime labels, outside rank 16',
    'PASS: complete rational kernel dimension 31; projected S-divisor rank 6',
    'PASS: P0 and P2 coefficients are equal in every projected combination',
    'SCOPE: this is a complete elimination of the retained finite rows; '
    'no ordinary class-group or nonprincipality assertion is made.'
]
for line in lines:
    print(line)
(base / 'two_inert_retained_relation_projection_output.txt').write_text('\n'.join(lines) + '\n')
