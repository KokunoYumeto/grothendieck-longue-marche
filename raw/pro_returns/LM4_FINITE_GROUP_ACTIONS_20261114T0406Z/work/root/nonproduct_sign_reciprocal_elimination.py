#!/usr/bin/env python3
"""Retain exact reciprocal-coordinate trace polynomials for the sign branch."""
from pathlib import Path
from hashlib import sha256
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
source = ROOT / 'work/part_a/code/affine_nonproduct_general_rank_one_pairings_stage_output.json'
raw = source.read_bytes()
data = json.loads(raw)
R, d, A, B, C, D, E = sp.symbols('R d A B C D E')
reciprocals = [E, A, B, C, D]
variables = [R, d, A, B, C, D, E]
records = []
for row in data['records']:
    index = row['index']
    if index not in [1, 2, 4, 6, 8, 9, 10]:
        continue
    terms = []
    for coefficient, exponent in row['exact_laurent_coefficients']:
        a, b, *powers = exponent
        if (a+b) % 2:
            terms.append((coefficient, ((a+b+1)//2, -b, *powers)))
    minima = [min(e[i] for _, e in terms) for i in range(2)]
    maxima = [max(e[i] for _, e in terms) for i in range(2, 7)]
    poly = sp.Poly(sp.Add(*(coefficient*R**(exponent[0]-minima[0])
                    *d**(exponent[1]-minima[1])
                    *sp.prod((1-x)**(maximum-power)
                             for x, maximum, power in zip(reciprocals, maxima, exponent[2:]))
                    for coefficient, exponent in terms)), *variables, domain=sp.ZZ)
    expression = poly.as_expr()
    factor = sp.factor(expression)
    assert sp.Poly(factor, *variables) == poly
    branches = []
    for branch, substitution in [('C=0', {C: 0}), ('C=1-d', {C: 1-d})]:
        specialized = sp.factor(expression.subs(substitution))
        branches.append({'stratum': branch, 'polynomial': str(specialized)})
        if index in [1, 8, 10]:
            # This additional chart is A!=0 and R+d!=0; the relation EA+BD=0
            # comes from F4 in these two C strata, and is not asserted globally.
            substitution2 = dict(substitution)
            substitution2[E] = -B*D/A
            rational = sp.cancel(expression.subs(substitution2))
            numerator, denominator = sp.fraction(rational)
            specialized2 = sp.factor(numerator)
            assert sp.cancel(rational-specialized2/denominator) == 0
            branches.append({'stratum': branch+'; A!=0; E=-BD/A',
                             'polynomial': str(specialized2),
                             'denominator': str(denominator)})
    item = {'source_index': index, 'source_label': row['label'],
            'original_odd_terms': len(terms), 'polynomial_terms': len(poly.terms()),
            'R_d_minima': minima, 't_u_v_w_z_exponent_maxima': maxima,
            'polynomial': str(factor), 'branches': branches}
    records.append(item)
    print(json.dumps({'index': index, 'terms': len(poly.terms()),
                      'branches': [{**b, 'polynomial': b['polynomial'] if len(b['polynomial']) < 1300
                                    else 'retained factor of length '+str(len(b['polynomial']))}
                                   for b in branches]}), flush=True)
result = {
    'status': 'EXACT_EXPLORATORY_RECIPROCAL_TRACE_CHARTS',
    'producer_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'input': {'path': str(source.relative_to(ROOT)), 'bytes': len(raw),
              'sha256': sha256(raw).hexdigest()},
    'coordinate_map': 'd=r/h, R=r^2; A=1-u^-1, B=1-v^-1, C=1-w^-1, D=1-z^-1, E=1-t^-1',
    'inverse_map': 'u=(1-A)^-1,v=(1-B)^-1,w=(1-C)^-1,z=(1-D)^-1,t=(1-E)^-1; h=r/d and r^2=R',
    'polynomial_definition': 'r*O_index = R^minR*d^mind*P / product((1-reciprocal_i)^max_i). All displayed denominators in this definition are nonzero on the original character torus.',
    'records': records,
    'scope': 'Exact algebraic transports of the already serialized rank-one traces. The E=-BD/A charts explicitly retain their A!=0 domain; no complete sign-stratum exclusion is asserted.'}
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'output': str(output.relative_to(ROOT)), 'bytes': output.stat().st_size,
                  'sha256': sha256(output.read_bytes()).hexdigest()}), flush=True)
