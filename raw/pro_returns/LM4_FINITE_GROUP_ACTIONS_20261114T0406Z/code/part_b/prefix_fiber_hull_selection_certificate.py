#!/usr/bin/env python3
"""Exact certificate for the full-prefix fiber-hull selection obstruction."""
from pathlib import Path
import json
import sympy as sp

R = sp.Rational
q = sp.symbols('q', positive=True)
data = [
    (R(0), R(1), R(0), R(0)),
    (R(1, 6), R(5, 4), R(1), R(2)),
    (R(1, 3), R(3, 4), R(1), R(3)),
    (R(1, 2), R(3, 2), R(1), R(2)),
    (R(2, 3), R(3, 2), R(1), R(3)),
    (R(5, 6), R(1), R(3), R(3)),
    (R(1), R(1), R(0), R(0)),
]
checks = []

def check(label, condition):
    assert condition, label
    checks.append(label)

def eq(a, b):
    return sp.simplify(a - b) == 0

def affine_sign(expr):
    """Exact strict sign on 0 < q < 1/4 of an affine polynomial."""
    expr = sp.expand(expr)
    check(f'affine sign degree: {expr}', sp.Poly(expr, q).degree() <= 1)
    if expr == 0:
        return 0
    left, right = expr.subs(q, 0), expr.subs(q, R(1, 4))
    if left >= 0 and right >= 0 and (left > 0 or right > 0):
        return 1
    if left <= 0 and right <= 0 and (left < 0 or right < 0):
        return -1
    raise AssertionError(f'Unresolved sign: {expr}')

check('based initial parameter', data[0][1:] == (1, 0, 0))
check('based final parameter', data[-1][1:] == (1, 0, 0))
check('all affine scales positive', all(row[1] > 0 for row in data))

records = []
for side in (1, -1):
    v = side * q
    target = 1 + v + q / 4
    base = [sp.expand(lam * v + c) for _, lam, c, _ in data]
    diffs = [sp.expand(value - target) for value in base[:6]]
    signs = [affine_sign(expr) for expr in diffs]
    check(f'prefix maximum side {side}', max(signs[:3]) == 0)
    check(f'chosen endpoint above maximum side {side}', signs[5] == 1)
    crossings = []
    for i in range(5):
        lo, hi = signs[i], signs[i+1]
        if lo == 0:
            crossings.append(data[i][3])
        if hi == 0:
            crossings.append(data[i+1][3])
        check(f'no full level segment away from zero: {side},{i}', not (lo == hi == 0))
        if lo * hi == -1:
            theta = sp.factor(-diffs[i] / (diffs[i+1] - diffs[i]))
            fiber = sp.simplify(data[i][3] + theta * (data[i+1][3] - data[i][3]))
            check(f'exact crossing equation: {side},{i}', eq((1-theta)*base[i] + theta*base[i+1], target))
            crossings.append(fiber)
    check(f'all crossing shifts rational side {side}', all(value.is_Rational for value in crossings))
    unique = sorted(set(crossings))
    expected = [R(2), R(7, 3)] if side == 1 else [R(3)]
    check(f'complete crossing shifts side {side}', unique == expected)
    records.append({'side': side, 'level': str(target), 'segment_endpoint_signs': signs,
                    'crossing_fiber_shifts': [str(value) for value in unique]})

zero_base = [c for _, _, c, _ in data[:6]]
check('zero-level plateau endpoints', zero_base[1:5] == [1, 1, 1, 1])
check('zero-level plateau shift range', min(row[3] for row in data[1:5]) == 2 and max(row[3] for row in data[1:5]) == 3)
check('strict one-sided separation', R(7, 3) < 3)

x, p, r, lam = sp.symbols('x p r lam', nonzero=True)
dilation_product = p + lam * ((r + (x-r)/lam) - p)
check('two-center translation identity', eq(dilation_product, x + (1-lam)*(p-r)))
check('first center minus four', all(eq(c, 4*(l-1)) for _, l, c, _ in data[:2]))
check('pure vertical segment', data[3][1:3] == data[4][1:3] and data[4][3]-data[3][3] == 1)

result = {'status': 'PASS', 'exact_checks': len(checks), 'arithmetic': 'symbolic rational',
          'crossing_records': records, 'one_sided_hulls': {'positive': ['2', '7/3'], 'negative': ['3', '3'], 'zero': ['2', '3']},
          'scope': 'No continuous selection from the full-prefix fiber hull; the explicit centralizer loop itself contracts.'}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
