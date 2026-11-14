#!/usr/bin/env python3
"""Exact exploratory sign-annihilator vectors in the original six coordinates."""
from pathlib import Path
from hashlib import sha256
import json
import runpy
import sys
import sympy as sp

# The retained exact source7 polynomial has more than one thousand summands.
# This changes only the recursion allowance of the inherited AST verifier.
sys.setrecursionlimit(20000)

ROOT = Path(__file__).resolve().parents[2]
FOLDER = ROOT / 'work/part_a/code'
paths = {key: FOLDER / name for key, name in {
    'matrices': 'affine_nonproduct_boundary_quotient_stage_output.json',
    'factors': 'affine_nonproduct_source_zero_stage_output.json',
    'parser': 'affine_four_parameter_extension_independent_audit.py',
    'arithmetic': 'affine_full_product_one_independent_audit.py',
}.items()}
matrices = json.loads(paths['matrices'].read_text())
factors = json.loads(paths['factors'].read_text())
parser = runpy.run_path(str(paths['parser']))
arithmetic = runpy.run_path(str(paths['arithmetic']))
names = ['r', 'h', 't', 'u', 'v', 'w', 'z']
parser['configure'](names, [[int(i == j) for i in range(7)] for j in range(7)])
parse, pm = parser['parse'], parser['parse_matrix']
parse.__globals__['UNITS']['s'] = parse('h/(r*t*u*v*w*z)')
plus, mul, mm = arithmetic['plus'], arithmetic['times'], arithmetic['mm']
variables = sp.symbols(' '.join(names))
column = pm([[a] for a in factors['column_a']])
one = parse('1')

def change(terms):
    ans = {}
    for c, (a, b, d, e, f, g, j) in terms:
        ans = plus(ans, {(a-b, b, d-b, e-b, f-b, g-b, j-b): c})
    return ans

def expr(poly):
    return sp.Add(*(c*sp.prod(x**e for x, e in zip(variables, exponents))
                    for exponents, c in poly.items()))

def subtract_scalar(matrix, scalar):
    return [[plus(p, {e: -c for e, c in scalar.items()}) if i == j else p
             for j, p in enumerate(row)] for i, row in enumerate(matrix)]

records = []
for index, root_expr in [
    (2, ['r*t', '1/(r*t)', 'r*t/(u*v)', 'r*t/(w*z)']),
    (7, ['t/h', 'h/t', 't/(h*u*v)', 't/(h*w*z)']),
]:
    record = next(a for a in matrices['records'] if a['index'] == index)
    T = [[change(p) for p in row] for row in record['boundary_quotient_matrix_6']]
    roots = [parse(a) for a in root_expr]
    identity = [[one if i == j else {} for j in range(6)] for i in range(6)]
    product = identity
    for root in roots:
        product = mm(subtract_scalar(T, root), product)
    assert not any(p for row in product for p in row)
    e1 = {}
    e3 = {}
    for root in roots:
        e1 = plus(e1, root)
    for omitted in range(4):
        term = one
        for i, root in enumerate(roots):
            if i != omitted:
                term = mul(term, root)
        e3 = plus(e3, term)
    T2a = mm(T, mm(T, column))
    vector = [plus(mul(e1, T2a[i][0]), mul(e3, column[i][0])) for i in range(6)]
    values = []
    for i, p in enumerate(vector):
        factor = sp.factor(expr(p))
        assert parse(str(factor)) == p
        values.append({'coordinate': i+1, 'terms': len(p), 'factor': str(factor),
                       'coefficients': parser['serialize'](p)})
        print(json.dumps({'index': index, **{k:v for k,v in values[-1].items() if k != 'coefficients'}}), flush=True)
    records.append({'index': index, 'label': record['label'], 'roots': root_expr,
                    'full_matrix_annihilator_verified': True,
                    'e1': str(sp.factor(expr(e1))), 'e3': str(sp.factor(expr(e3))),
                    'vector_definition': '(e1*T^2+e3*I)*a', 'coordinates': values})
result = {'status': 'EXACT_EXPLORATORY_SIGN_ANNIHILATOR_VECTORS',
          'producer_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
          'input_bindings': {str(p.relative_to(ROOT)): {'bytes': p.stat().st_size,
                            'sha256': sha256(p.read_bytes()).hexdigest()} for p in paths.values()},
          'variables': names, 'coefficient_map': 's=h/(r*t*u*v*w*z)',
          'records': records,
          'scope': 'Full source2/source7 degree-four matrix annihilators and the indicated vectors are verified exactly. No complete quadratic-sign separation is asserted.'}
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'output': str(output.relative_to(ROOT)), 'bytes': output.stat().st_size,
                  'sha256': sha256(output.read_bytes()).hexdigest()}), flush=True)
