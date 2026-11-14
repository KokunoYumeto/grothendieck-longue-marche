#!/usr/bin/env python3
"""Exploratory generic-parameter remainders; exceptional divisors are retained."""
from pathlib import Path
from hashlib import sha256
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
source = Path(__file__).with_name('nonproduct_sign_reciprocal_elimination.json')
raw = source.read_bytes()
data = json.loads(raw)
R, d, A, B, C, D, E = sp.symbols('R d A B C D E')
names = {str(x):x for x in [R,d,A,B,C,D,E]}
polys = {r['source_index']: sp.sympify(r['polynomial'], locals=names) for r in data['records']}
domain = sp.QQ.frac_field(R,d)
records = []
for title, substitution in [('C=0',{C:0}),('C=1-d',{C:1-d})]:
    initial = [sp.factor(polys[i].subs(substitution)) for i in [2,4,6]]
    print(json.dumps({'stage':'groebner_started','stratum':title}), flush=True)
    basis = sp.groebner(initial, E,D,B,A, domain=domain, order='grevlex')
    denominators = set()
    for p in basis.polys:
        for coefficient in p.coeffs():
            denominators.add(str(sp.factor(sp.denom(coefficient))))
    item = {'stratum':title, 'initial_generators':[str(p) for p in initial],
            'basis':[str(sp.factor(p.as_expr())) for p in basis.polys],
            'coefficient_denominators':sorted(denominators), 'remainders':[]}
    print(json.dumps({'stage':'groebner_done','stratum':title,'basis_size':len(basis.polys),
                       'coefficient_denominators':sorted(denominators)}), flush=True)
    for i in [1,10,8]:
        original = polys[i].subs(substitution)
        quotients, remainder = basis.reduce(original)
        assert sp.Poly(original-sum(q*g.as_expr() for q,g in zip(quotients,basis.polys))
                       -remainder, E,D,B,A, domain=domain).is_zero
        factor = sp.factor(remainder)
        item['remainders'].append({'source_index':i,'remainder':str(factor),
                                   'quotients':[str(q) for q in quotients]})
        print(json.dumps({'stage':'remainder','stratum':title,'index':i,
                          'terms':len(sp.Poly(remainder,E,D,B,A,domain=domain).terms()),
                          'remainder':str(factor) if len(str(factor))<2000 else 'retained length '+str(len(str(factor)))}), flush=True)
    records.append(item)
result = {'status':'EXPLORATORY_GENERIC_PARAMETER_REMAINDERS',
          'input':{'path':str(source.relative_to(ROOT)),'bytes':len(raw),'sha256':sha256(raw).hexdigest()},
          'producer_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
          'coefficient_field':'QQ(R,d)', 'monomial_order':'grevlex E,D,B,A',
          'records':records,
          'scope':'This is a generic-parameter computation only. All coefficient divisors are retained. No finite-characteristic or exceptional-parameter exclusion is inferred.'}
output=Path(__file__).with_suffix('.json')
output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'output':str(output.relative_to(ROOT))}),flush=True)
