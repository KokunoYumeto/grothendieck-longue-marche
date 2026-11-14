"""Exact algebra certificates for the independent cross-ratio-locus review.

These identities are integral polynomial identities, so their reductions are
valid in every characteristic. Irreducibility of the Kummer pullback and
ampleness are proved in audit/BC_review_crossratio.md, not inferred from tests.
"""
from itertools import combinations
from pathlib import Path
import json
import sympy as s

x1,x2,x3,x4,c=s.symbols('x1 x2 x3 x4 c')
xs=[x1,x2,x3,x4]
F=(x1-x3)*(x2-x4)-c*(x1-x4)*(x2-x3)
A=s.diff(F,x4)
B=s.expand(F-A*x4)
assert s.expand(A-(c*x2-x1+(1-c)*x3))==0
remainder=s.factor(B.subs(x1,c*x2+(1-c)*x3))
assert s.expand(remainder-c*(1-c)*(x2-x3)**2)==0

expected={
 (0,1):(1-c)*(x1-x3)*(x1-x4),
 (0,2):c*(x1-x2)*(x1-x4),
 (0,3):-(x1-x2)*(x1-x3),
 (1,2):(x1-x2)*(x2-x4),
 (1,3):-c*(x1-x2)*(x2-x3),
 (2,3):(1-c)*(x1-x3)*(x2-x3),
}
collisions={}
for i,j in combinations(range(4),2):
    value=s.factor(F.subs(xs[j],xs[i]))
    assert s.expand(value-expected[i,j])==0
    collisions[f'{i+1}={j+1}']=str(value)

X=s.symbols('X1:5');Z=s.symbols('Z1:5')
def bracket(i,j):
    return X[i]*Z[j]-X[j]*Z[i]
Fh=s.Poly(s.expand(bracket(0,2)*bracket(1,3)-c*bracket(0,3)*bracket(1,2)),*(X+Z))
for powers,coefficient in Fh.terms():
    assert all(powers[i]+powers[i+4]==1 for i in range(4))

# The special characteristic-three parameter c=-1 is permitted.
assert int((c*(1-c)).subs(c,2)) % 3 != 0
out={
 'passed':True,
 'linear_coefficient':str(s.factor(A)),
 'remainder_modulo_linear_coefficient':str(remainder),
 'all_characteristics_condition':'c*(1-c) != 0',
 'pair_collision_identities':collisions,
 'homogeneous_multidegree':[1,1,1,1],
 'characteristic_3_parameter_c_2_is_not_exceptional':True,
 'scope':'Exact polynomial identities only; geometric arguments appear in audit/BC_review_crossratio.md.'
}
Path(__file__).with_name('BC_crossratio_geometry_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
