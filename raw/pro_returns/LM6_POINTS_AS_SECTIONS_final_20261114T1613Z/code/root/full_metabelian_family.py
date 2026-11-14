#!/usr/bin/env python3
"""Finite cohomology certificate for the full-metabelian family of E.31."""
from pathlib import Path
from functools import reduce
from math import gcd,lcm
import json
import sympy as S

coords=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
U=S.Matrix([(v,-u) for u,v in coords])
R=S.Matrix([[0,-1],[1,-1]])
CE=S.Matrix([[1,-1],[0,-1]])
CT=S.zeros(8)
for j,i in enumerate([0,2,1,3,5,4,7,6]):CT[i,j]=-1
def block(a,b):
    low=U*a-b*U
    assert all(x%3==0 for x in low)
    return a.row_join(S.zeros(2,8)).col_join((low/3).row_join(b))
FV=block(S.eye(2)+3*R,7*S.eye(8));CV=block(CE,CT)
pairs=[(i,j) for i in range(10) for j in range(i+1,10)]
def wedge(m):
    return S.Matrix([[m[i,a]*m[j,b]-m[i,b]*m[j,a]
                       for a,b in pairs] for i,j in pairs])
T=wedge(FV);J=wedge(CV);I=S.eye(45)
u=S.Matrix([3,0]+list(U[:,0]));v=S.Matrix([0,3]+list(U[:,1]))
w=S.Matrix([u[i]*v[j]-u[j]*v[i] for i,j in pairs])
assert T*w==7*w and J*w==-w and J*J==I
assert reduce(gcd,[abs(int(x)) for x in w])==1
pivot=next(i for i,x in enumerate(w) if abs(x)==1)
row=(I-J)[pivot,:]*(T-I).inv()
den=lcm(*[int(x.q) for x in row]);row=[int(x*den) for x in row]
common=reduce(gcd,[abs(x) for x in row]);row=[x//common for x in row]
row=S.Matrix([row]);relations=(T-I)*(I+J)
assert row*relations==S.zeros(1,45)
value=int((row*w)[0]);assert value
valuation=0;z=abs(value)
while z%3==0:z//=3;valuation+=1
modulus=3**(valuation+1)
assert value%modulus
out={'coefficient':'Lambda^2 V_3','dimension':45,
     'ordered_wedge_basis':[list(x) for x in pairs],
     'compact_wedge':list(map(int,w)),
     'tau_matrix':[[int(x) for x in T.row(i)] for i in range(45)],
     'conjugation_matrix':[[int(x) for x in J.row(i)] for i in range(45)],
     'primitive_annihilator_row':list(map(int,row)),
     'relation_matrix':'(T-I)(I+J)',
     'annihilator_times_relation':'zero over the integers',
     'annihilator_times_w':value,'3_valuation':valuation,
     'finite_certificate_modulus':modulus,'residue':value%modulus,
     'checks_passed':True,
     'scope':'Certifies nonzero class of the explicit cocycle; Fox/Haar embedding and noncuspidality are proved in E.31.'}
Path(__file__).with_name('full_metabelian_family_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['dimension','primitive_annihilator_row',
      'annihilator_times_w','3_valuation','finite_certificate_modulus','residue','checks_passed']},indent=2))
