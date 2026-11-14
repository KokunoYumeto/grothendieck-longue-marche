#!/usr/bin/env python3
"""Exact rational substitutions for the crossed deleted-coordinate sign branches."""
from pathlib import Path
from hashlib import sha256
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
source = ROOT / 'work/root/nonproduct_hr_minus_one_trace_branches.json'
raw = source.read_bytes()
data = json.loads(raw)
d,t,v,z = sp.symbols('d t v z')
variables = (d,t,v,z)
records = []
cases = [
    ({'u':'1/d','w':'1'}, 't=1, v=(d+1)/d', {t:1,v:(d+1)/d}),
    ({'u':'1/d','w':'1'}, 't=-1/d, v=(d+1)/(2d+1)', {t:-1/d,v:(d+1)/(2*d+1)}),
    ({'u':'1','w':'1/d'}, 'v=1', {v:1}),
    ({'u':'1','w':'1/d'}, 'z=1', {z:1}),
    ({'u':'1','w':'1/d'}, 'z=-1/d', {z:-1/d}),
]
for branch, label, substitution in cases:
    rows = next(x['records'] for x in data['records'] if x['branch']==branch)
    result_rows=[]
    print(json.dumps({'branch':branch,'case':label}),flush=True)
    for row in rows:
        original=sp.Add(*(coefficient*sp.prod(a**b for a,b in zip(variables,exponent))
                          for coefficient,exponent in row['coefficients']))
        expression=original.subs(substitution, simultaneous=True)
        factor=sp.factor(expression)
        assert sp.cancel(factor-expression)==0
        numerator,denominator=sp.fraction(factor)
        result_rows.append({'index':row['index'],'factor':str(factor),
                            'numerator':str(numerator),'denominator':str(denominator)})
        print(json.dumps({'index':row['index'],'factor':str(factor) if len(str(factor))<1800 else 'retained length '+str(len(str(factor)))}),flush=True)
    records.append({'branch':branch,'case':label,
                    'substitution':{str(a):str(b) for a,b in substitution.items()},
                    'records':result_rows})
result={'status':'EXACT_RATIONAL_SUBSTITUTION_RESEARCH',
        'producer_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'input':{'path':str(source.relative_to(ROOT)),'bytes':len(raw),'sha256':sha256(raw).hexdigest()},
        'records':records,
        'scope':'Every substitution and displayed factor is an exact rational identity. Nonzero denominators and exhaustive case coverage require the accompanying field argument; this file does not assert them.'}
output=Path(__file__).with_suffix('.json')
output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'output':str(output.relative_to(ROOT)),'bytes':output.stat().st_size,'sha256':sha256(output.read_bytes()).hexdigest()}),flush=True)
