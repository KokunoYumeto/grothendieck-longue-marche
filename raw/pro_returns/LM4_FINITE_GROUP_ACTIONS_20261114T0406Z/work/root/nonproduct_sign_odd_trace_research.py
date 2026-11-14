#!/usr/bin/env python3
"""Exploratory exact odd-trace factorizations, with original source indices."""
from pathlib import Path
from hashlib import sha256
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
source = ROOT / 'work/part_a/code/affine_nonproduct_general_rank_one_pairings_stage_output.json'
raw = source.read_bytes()
data = json.loads(raw)
assert data['variables'] == ['r', 'h', 't', 'u', 'v', 'w', 'z']
variables = sp.symbols('r h t u v w z')
r, h, t, u, v, w, z = variables
rows = []
for item in data['records']:
    if item['index'] not in [2, 4, 6, 9]:
        continue
    terms = item['exact_laurent_coefficients']
    odd_terms = [(c, e) for c, e in terms if (e[0] + e[1]) % 2]
    odd = sp.Add(*(c * sp.prod(x ** n for x, n in zip(variables, e)) for c, e in odd_terms))
    factor = sp.factor(odd)
    assert sp.cancel(odd - factor) == 0
    row = {'source_index': item['index'], 'source_label': item['label'],
           'original_term_count': len(terms), 'odd_term_count': len(odd_terms),
           'odd_part': str(factor),
           'exact_definition': 'Sum of the original Laurent terms with odd exponent sum in r,h; half the trace difference under (r,h)->(-r,-h) in odd characteristic.'}
    rows.append(row)
    print(json.dumps(row), flush=True)
result = {
    'status': 'EXACT_EXPLORATORY_ODD_TRACE_FACTORIZATION',
    'input': {'path': str(source.relative_to(ROOT)), 'bytes': len(raw), 'sha256': sha256(raw).hexdigest()},
    'variables': data['variables'], 'records': rows,
    'scope': 'The exact bound producer polynomials are factored; this file does not rerun their original matrix derivation or assert a completed common-factor separation.'}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2) + '\n')
