#!/usr/bin/env python3
"""Independent literal-bracket and divisor reconstruction for B.43.

All Hall coordinates here use the intrinsic fibre-functor bracket.
The deck element h of the radical cover is the inverse of c=[y,x].
"""
import ast,json
from pathlib import Path
import numpy as np

MOD=3**20
hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
lookup={h:i for i,h in enumerate(hall)}
bpairs=[(i,j) for i in range(8) for j in range(i)]
source=ast.parse(Path('deliverable/code/b_char2_symmetry.py').read_text())
exec(compile(ast.Module(body=[x for x in source.body if isinstance(x,ast.FunctionDef)
    and x.name=='bracket'],type_ignores=[]),'Hall-bracket','exec'))
auto=np.load('deliverable/code/b_global_action_ambiguity_matrices.npz')['projective_automorphisms']
U=np.array([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]],dtype=np.int64)

def wedge(M):
    return np.array([[int(M[a,i])*int(M[b,j])-int(M[a,j])*int(M[b,i])
                     for i,j in bpairs] for a,b in bpairs],dtype=np.int64)

def ad(b):
    D=np.zeros((330,10),dtype=np.int64)
    for n,(i,j) in enumerate(bpairs):
        for k in range(10):
            for row,sgn in bracket(i+2,j+2,k): D[row,k]+=int(b[n])*sgn
    return D

b1=np.zeros(28,dtype=np.int64)
for pair,c in [((3,2),1),((3,1),-1),((4,0),1),((4,2),-1),((5,1),1),((5,0),-1)]:
    b1[bpairs.index(pair)]=c
b2=np.zeros(28,dtype=np.int64)
for pair,c in [((1,0),-1),((2,0),1),((2,1),-1),((4,3),-1),((5,3),1),((5,4),-1)]:
    b2[bpairs.index(pair)]=c
for j in range(6):
    c=1 if j<3 else -1
    b2[bpairs.index((6,j))]+=c
    b2[bpairs.index((7,j))]-=c

translations=[]
for p in range(8):
    gs=[g for g in auto if np.array_equal(g[:2,:2],np.eye(2,dtype=np.int64))
        and np.array_equal(-g[2:,2:]@np.ones(8,dtype=np.int64),np.eye(8,dtype=np.int64)[:,p])]
    assert len(gs)==1
    translations.append(gs[0][2:,2:])

deriv=[]
for b in [b1,b2]:
    Db=np.column_stack([-ad(wedge(T)@b)[:,p+2] for p,T in enumerate(translations)])
    deriv.append(np.column_stack((-Db@U,3*Db))+3*ad(b))

boundary=[np.array([[-2,1,1,0,0,0,0,0],[-2,0,0,0,1,0,0,1]],dtype=np.int64),
          np.array([[1,1,1,0,0,0,-3,0],[0,0,0,1,1,1,-3,0]],dtype=np.int64)]
rows=[]
for i,PW in enumerate(boundary):
    assert not np.any(PW@U%3)
    P=np.column_stack((-PW@U//3,PW))
    L=np.array([[(P[1,j]*P[0,k]-P[0,j]*P[1,k])*P[r,l]
                for j,k,l in hall] for r in range(2)],dtype=np.int64)
    scalars=[];origin=[]
    cusp=0 if i==0 else 6
    exterior=np.array([PW[1,j]*PW[0,k]-PW[0,j]*PW[1,k] for j,k in bpairs],dtype=np.int64)
    for b,D in zip([b1,b2],deriv):
        pushed=L@D
        rr,cc=next((r,c) for r in range(2) for c in range(10) if P[r,c])
        scalar=int(pushed[rr,cc])//int(P[rr,cc])
        assert np.array_equal(pushed,scalar*P)
        scalars.append(scalar)
        origin.append(int(3*exterior@(wedge(translations[cusp])@b-b)))
    rows.append({'map':i+1,'V_matrix':P.tolist(),'intrinsic_derivation_scalars':scalars,
                 'intrinsic_cusp_origin_shifts':origin,
                 'deck_h_cusp_origin_shifts':[-x for x in origin]})
assert rows[0]['intrinsic_derivation_scalars']==[-9,0]
assert rows[1]['intrinsic_derivation_scalars']==[0,-54]
assert rows[0]['intrinsic_cusp_origin_shifts']==[9,0]
assert rows[1]['intrinsic_cusp_origin_shifts']==[0,54]
result={'status':'all independently reconstructed integral B43 rows passed',
        'construction':'literal six/eighteen boundary brackets, actual translation permutations and written divisors',
        'marking':'intrinsic c=[R_b,R_a]=deck h^{-1}; actual relative cusp deck h^{-k} has intrinsic coefficient+k',
        'rows':rows}
Path('work/c_B43_origin_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
