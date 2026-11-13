#!/usr/bin/env python3
"""Exact local obstruction exponent at the two primes over19, for E.38."""
from pathlib import Path
import json
import sympy as s
from e_intrinsic_class2 import Vmat,ext,smith_dvr,R,ix,pivot

rows=[i for i in range(45) if ix[i]!=(0,1)]
cols=[i for i in range(45) if i!=pivot]
result=[]
for a,b in [(-2,3),(-5,-3)]:
 A=Vmat(a*s.eye(2)+b*R,19*s.eye(8))
 D=(ext(A)-19*s.eye(45)).extract(rows,cols)
 vals,left,right=smith_dvr(D,44)
 result.append({'primary':[a,b],'norm':19,'Smith_valuations':vals,'largest_valuation':max(vals),'sum_valuations':sum(vals)})
 print('Prime generator',a,b,'Smith valuations',vals,'maximum',max(vals),flush=True)
assert result[0]['Smith_valuations']==result[1]['Smith_valuations']
assert sum(result[0]['Smith_valuations'])==78
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: both integral local cokernels have the stated exact exponent.',flush=True)
