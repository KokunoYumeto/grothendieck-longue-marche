#!/usr/bin/env python3
"""Exploratory actual-source r=1 matrix comparison; no registered theorem."""
from pathlib import Path
import hashlib,json
import sympy as sp
ROOT=Path(__file__).resolve().parents[3]
folder=Path(__file__).resolve().parent
source=ROOT/'work/part_a/code/affine_product_one_four_parameter_stage_output.json'
data=json.loads(source.read_text())
r,s,t,u,c,z=sp.symbols('r s t u c z')
local={str(x):x for x in [r,s,t,u,c,z]}
def M(a):return sp.Matrix([[sp.sympify(x,locals=local) for x in row] for row in a])
def clean(a):return a.applyfunc(lambda x:sp.factor(sp.cancel(x)))
def strings(a):return [[str(x) for x in row] for row in a.tolist()]
e=sp.eye(6);C=s*t*u
J=sp.Matrix.hstack(e[:,2]-s*e[:,1],e[:,3]-s*t*e[:,1],e[:,1],e[:,0]-e[:,1],e[:,4]-C*e[:,1],e[:,5]-C*e[:,1])
Ji=sp.Matrix.vstack(e[2,:],e[3,:],sp.Matrix([[1,1,s,s*t,C,C]]),e[0,:],e[4,:],e[5,:])
assert clean(J*Ji)==sp.eye(6) and clean(Ji*J)==sp.eye(6)
rows=[];blocks=[]
for row in data['source_records']:
 A=M(row['action_H1_6']).subs(r,1)
 B=clean(Ji*A*J);blocks.append(B)
 assert all(B[i,j]==0 for i in range(2,6) for j in range(6) if i!=j)
 G=clean(B[:2,:2].subs(s,c/(t*u)))
 rows.append({'index':row['index'],'label':row['label'],'core':strings(G),
  'core_characteristic_polynomial':str(sp.factor(G.charpoly(z).as_expr())),
  'quotient_characters':[str(sp.factor(B[i,i].subs(s,c/(t*u)))) for i in range(2,6)]})
exception=[]
for quotient_column,name in [(2,'boundary'),(3,'X1')]:
 eq=[];locations=[]
 for index,B in enumerate(blocks):
  A=clean(B.subs({s:1/t,u:-1}));lam=A[quotient_column,quotient_column]
  D=A-lam*sp.eye(6)
  for i in range(6):eq.append(list(D[i,:]));locations.append([index,i])
 E=sp.Matrix(eq);pivots=tuple(E.T.rref()[1]);rank=len(pivots)
 determinant=sp.factor(E.extract(pivots,list(range(6))).det()) if rank==6 else None
 exception.append({'quotient':name,'rank_over_Qt':rank,'selected_source_rows':[locations[i] for i in pivots],
  'selected_square_determinant':str(determinant) if determinant is not None else None,
  'nullspace':[strings(v) for v in E.nullspace()]})
out={'status':'EXPLORATORY_IDENTITIES_ONLY','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'coefficient_specialization':'r=1; c=stu; s=c/(tu)',
 'basis':strings(J),'inverse_basis':strings(Ji),'source_comparisons':rows,
 'exception_c_equals_u_equals_minus_one':exception,
 'scope':'No all-field consequence is registered. The literal four-parameter producer has not yet had a separate integral audit.'}
(folder/'output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'source_comparisons':[{k:x[k] for k in ['index','label','core_characteristic_polynomial','quotient_characters']} for x in rows],'exception':exception},indent=2))
