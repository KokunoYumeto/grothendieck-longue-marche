#!/usr/bin/env python3
"""Exact abelian extension constraints for the E76 ninth-genus quotient."""
from itertools import product
import json
from pathlib import Path
import sympy as s

H=s.Matrix([[4,3,0],[8,7,6],[1,0,1]])
orders=(9,9,3)
R=s.diag(*orders)
J=(H**3-s.eye(3))
assert all(v.q==1 for v in R.inv()*J)
rel=R.inv()*J
records=[]
for a,b,c in product(range(3),repeat=3):
    ext=s.Matrix([[a,b,c]])
    compatible=(b==0)
    cube=[int(v)%3 for v in ext*rel]
    records.append(dict(extension=[a,b,c],relations_preserved=compatible,
                        h_cube=cube,order_three_lift=compatible and cube==[0,0,0]))
ans=dict(status='PASS',h=[list(H.row(i)) for i in range(3)],
         h_cube_relation_matrix=[[int(x) for x in rel.row(i)] for i in range(3)],
         allowed_extensions=[r['extension'] for r in records if r['order_three_lift']],
         records=records)
q=s.Matrix([6,0,2])
qnorm=R.inv()*(s.eye(3)+H+H**2)*q
assert all(x.q==1 for x in qnorm)
ans['three_prime_product_relation_coefficients']=[int(x) for x in qnorm]
ans['path_correction_on_q_norm_mod3']=[int(x)%3 for x in (2*s.eye(3)+H)*q]
ans['q_triple_relation_coefficients']=[int(x) for x in R.inv()*(3*q)]
t=s.Matrix([6,5,1])
tnorm=R.inv()*(s.eye(3)+H+H**2)*t
assert all(x.q==1 for x in tnorm)
ans['seventeen_product_relation_coefficients']=[int(x) for x in tnorm]
ans['seventeen_correction_mod3']=[int(x)%3 for x in (2*s.eye(3)+H)*t]
ans['h']=[[int(x) for x in row] for row in ans['h']]
text=json.dumps(ans,indent=2)
Path(__file__).with_suffix('.json').write_text(text+'\n')
print(text)
