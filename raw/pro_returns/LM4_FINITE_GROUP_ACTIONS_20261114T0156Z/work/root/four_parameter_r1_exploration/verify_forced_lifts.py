#!/usr/bin/env python3
"""Check the short exceptional matrix identities; literal-word audit is separate."""
from pathlib import Path
import hashlib,json
import sympy as sp
ROOT=Path(__file__).resolve().parents[3]
folder=Path(__file__).resolve().parent
source=ROOT/'work/part_a/code/affine_product_one_four_parameter_stage_output.json'
data=json.loads(source.read_text());r,s,t,u=sp.symbols('r s t u')
local={str(x):x for x in [r,s,t,u]}
def clean(a):return a.applyfunc(lambda x:sp.factor(sp.cancel(x)))
def M(a):return sp.Matrix([[sp.sympify(x,locals=local) for x in row] for row in a])
def strings(a):return [[str(x) for x in row] for row in a.tolist()]
e=sp.eye(6)
J=sp.Matrix.hstack(e[:,2]-e[:,1]/t,e[:,3]-e[:,1],e[:,1],e[:,0]-e[:,1],e[:,4]+e[:,1],e[:,5]+e[:,1])
Ji=sp.Matrix.vstack(e[2,:],e[3,:],sp.Matrix([[1,1,1/t,1,-1,-1]]),e[0,:],e[4,:],e[5,:])
assert clean(J*Ji)==sp.eye(6) and clean(Ji*J)==sp.eye(6)
T={i:clean(Ji*M(data['source_records'][i]['action_H1_6']).subs({r:1,s:1/t,u:-1})*J) for i in [1,2,7]}
for i in [2,7]:
 assert T[i][:2,:2]==t*sp.eye(2)
 assert all(T[i][j,k]==0 for j in range(2,6) for k in range(6) if j!=k)
assert [T[2][i,i] for i in range(2,6)]==[t,1/t,-t,-t]
assert [T[7][i,i] for i in range(2,6)]==[1/t,t,-t,-t]
vb=sp.Matrix([1-2*t,2,1,0,0,0]);vx=sp.Matrix([-t,0,0,1,0,0])
assert clean(T[7]*vb-vb/t)==sp.zeros(6,1)
assert clean(T[2]*vx-vx/t)==sp.zeros(6,1)
residual=sp.Matrix([3*t-1,-2,0,0,0,0])
assert T[1][2,2]==T[1][3,3]==1
assert clean(T[1]*vb-vb)==residual
assert clean(T[1]*vx-vx)==residual
out={'status':'PASS_EXACT_FORCED_LIFT_IDENTITIES','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'character':['1','t^-1','t','-1','1','1','-1'],
 'coordinate_order':['core_x','core_y','boundary','X1','X5','X6'],
 'basis':strings(J),'inverse_basis':strings(Ji),'source_matrices':{str(i):strings(T[i]) for i in [1,2,7]},
 'forced_boundary_lift':strings(vb),'forced_X1_lift':strings(vx),'source_1_residual_for_both':strings(residual),
 'proof_scope':'In the exceptional locus c=u=-1 with unequal scalar fields, k1=Fp, characteristic is odd and t lies outside Fp. Thus t-t^-1 and2t are nonzero. Sources2/7 kill all other quotient coordinates and force the displayed normalized lifts; source1 residual has nonzero second coordinate -2. Both common eigenline types are absent. These matrix identities await the separate literal-word audit of their input.'}
(folder/'forced_lifts_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'residual':['3*t-1','-2'],'source_indices':[1,2,7],'source_sha256':out['source_sha256']}))
