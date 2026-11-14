#!/usr/bin/env python3
"""Exact raw odd-trace transports on the four hr=-1 deleted-coordinate branches."""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import json
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'work/part_a/code/affine_nonproduct_general_rank_one_pairings_stage_output.json'
raw=source.read_bytes()
data=json.loads(raw)
d,t,v,z=sp.symbols('d t v z')
variables=[d,t,v,z]
records=[]
for uf,wf in [(0,0),(0,1),(1,0),(1,1)]:
    branch={'u':'1/d' if uf else '1','w':'1/d' if wf else '1'}
    rows=[]
    for row in data['records']:
        coefficients=Counter()
        for coefficient,(er,eh,et,eu,ev,ew,ez) in row['exact_laurent_coefficients']:
            if (er+eh)%2:
                p=(er+eh+1)//2
                coefficients[(p-eh-uf*eu-wf*ew,et,ev,ez)]+=coefficient*(-1 if p%2 else 1)
        coefficients={e:c for e,c in coefficients.items() if c}
        expression=sp.Add(*(c*sp.prod(a**b for a,b in zip(variables,e)) for e,c in coefficients.items()))
        factor=sp.factor(expression)
        assert sp.cancel(factor-expression)==0
        item={'index':row['index'],'source_label':row['label'],
              'normalized_odd_trace':str(factor),'terms':len(coefficients),
              'coefficients':[[c,list(e)] for e,c in sorted(coefficients.items())]}
        rows.append(item)
        print(json.dumps({'branch':branch,'index':row['index'],'terms':len(coefficients),
                          'factor':str(factor) if len(str(factor))<1200 else 'retained length '+str(len(str(factor)))}),flush=True)
    records.append({'branch':branch,'records':rows})
result={'status':'EXACT_EXPLORATORY_HR_MINUS_ONE_TRACE_BRANCHES',
        'producer_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'input':{'path':str(source.relative_to(ROOT)),'bytes':len(raw),'sha256':sha256(raw).hexdigest()},
        'coordinate_map':'r*O_i; R=r^2=-d, d=r/h, u=d^-uf, w=d^-wf; variables d,t,v,z.',
        'exact_exponent_map':'(er,eh,et,eu,ev,ew,ez) -> (p-eh-uf*eu-wf*ew,et,ev,ez), p=(er+eh+1)/2; coefficient multiplied by (-1)^p.',
        'records':records,
        'scope':'Four exact specializations of the bound original trace polynomials. No all-field exclusion of the remaining branches is inferred.'}
output=Path(__file__).with_suffix('.json')
output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'output':str(output.relative_to(ROOT)),'bytes':output.stat().st_size,'sha256':sha256(output.read_bytes()).hexdigest()}),flush=True)
