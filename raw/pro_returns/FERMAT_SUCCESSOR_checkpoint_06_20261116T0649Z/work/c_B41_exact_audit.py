#!/usr/bin/env python3
"""Independent unreduced-integer reconstruction of B41's six-term derivation."""
import ast
from pathlib import Path
import numpy as np
import json

MOD=3**20
hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
lookup={h:i for i,h in enumerate(hall)}
pairs=[(i,j) for i in range(10) for j in range(i)]
bpairs=[(i,j) for i in range(8) for j in range(i)]
source=ast.parse(Path('deliverable/code/b_char2_symmetry.py').read_text())
exec(compile(ast.Module(body=[x for x in source.body if isinstance(x,ast.FunctionDef)
    and x.name in {'bracket','lie3'}],type_ignores=[]),'Hall-functions','exec'))
glob=np.load('deliverable/code/b_global_action_ambiguity_matrices.npz')
U=np.array([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]],dtype=np.int64)
auto=glob['projective_automorphisms']

def lie_exact(g):
    h=lie3(g)
    return (h+MOD//2)%MOD-MOD//2

def wedge(M):
    return np.array([[int(M[a,i])*int(M[b,j])-int(M[a,j])*int(M[b,i])
                     for i,j in bpairs] for a,b in bpairs],dtype=np.int64)

def ad(parameter):
    out=np.zeros((330,10),dtype=np.int64)
    for n,(i,j) in enumerate(bpairs):
        for k in range(10):
            for row,sgn in bracket(i+2,j+2,k):out[row,k]+=int(parameter[n])*sgn
    return out

# Reconstruct b from the written six terms, not the saved parameter vector.
b=np.zeros(28,dtype=np.int64)
for pair,coefficient in [((3,2),1),((3,1),-1),((4,0),1),
                          ((4,2),-1),((5,1),1),((5,0),-1)]:
    b[bpairs.index(pair)]=coefficient
Db=np.zeros((330,8),dtype=np.int64)
translation=[]
for p in range(8):
    candidates=[g for g in auto if np.array_equal(g[:2,:2],np.eye(2,dtype=np.int64))
          and np.array_equal(-g[2:,2:]@np.ones(8,dtype=np.int64),np.eye(8,dtype=np.int64)[:,p])]
    assert len(candidates)==1
    g=candidates[0];translation.append(g)
    Db[:,p]=-ad(wedge(g[2:,2:])@b)[:,p+2]
Delta=np.column_stack((-Db@U,3*Db))+3*ad(b)
stored=np.load('work/b_arbitrary_action_deformation_matrices.npz')
assert np.array_equal(Delta,stored['central_derivation'])
assert np.array_equal(b,stored['boundary_inner_parameter'])
assert not np.any(Delta@np.r_[np.zeros(2,dtype=np.int64),-np.ones(8,dtype=np.int64)])
assert np.any(Delta%3)

T=glob['Tau_V'];C=glob['Conjugation_V']
assert not np.any(lie_exact(T)@Delta-49*Delta@T)
assert not np.any(lie_exact(C)@Delta+Delta@C)
assert np.array_equal(wedge(C[2:,2:])@b,-b)
max_residual_term=0
for g in auto:
    gb=wedge(g[2:,2:])@b
    correction=3*(gb-b)
    lhs=lie_exact(g)@Delta-Delta@g
    rhs=ad(correction)@g
    max_residual_term=max(max_residual_term,int(np.max(np.abs(lhs))),int(np.max(np.abs(rhs))))
    assert np.array_equal(lhs,rhs)
    if np.array_equal(-g[2:,2:]@np.ones(8,dtype=np.int64),-np.ones(8,dtype=np.int64)):
        assert np.array_equal(gb,b)

z=Delta[:,2]//3
assert np.array_equal(3*z,Delta[:,2])
assert z[lookup[(3,2,5)]]==1
assert all(not z[i] for i,h in enumerate(hall) if min(h)<2)
BP=wedge(translation[0][2:,2:])@b-b
assert np.array_equal(wedge(C[2:,2:])@BP,-BP)
assert not np.any(Delta[:,2]+3*ad(BP)[:,2])

result={"status":"all exact integer B41 derivation checks passed",
        "reconstructed_from":"six written boundary brackets and unique nine-point translations",
        "geometric_actions_checked":54,
        "max_absolute_Delta_entry":int(np.max(np.abs(Delta))),
        "max_absolute_geometric_inner_term":max_residual_term,
        "primitive_Hall_coefficient":{"label":[3,2,5],"value":1},
        "pure_boundary_vector_terms":int(np.count_nonzero(z)),
        "A0_origin_shift_sign":"+3 b_g (T_A0 b-b), whose conjugation cancels Delta(e_A0)",
        "scope":"actual deformation of class-three arithmetic action; no algebraic-curve realization claimed"}
Path('work/c_B41_exact_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
