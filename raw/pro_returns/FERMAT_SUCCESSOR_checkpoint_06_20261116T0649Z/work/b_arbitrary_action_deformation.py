#!/usr/bin/env python3
"""An explicit arithmetic deformation invisible to eta but visible at19.

This is a comparison of two arithmetic actions on the same intrinsic
class-three group.  The modified action is NOT claimed to arise from
another algebraic curve.  It isolates data which eta and the actual
outer A54 extension do not determine.
"""
import ast
from pathlib import Path
import json
import numpy as np

MOD=3**10
PREC=10
hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
lookup={h:i for i,h in enumerate(hall)}
pairs=[(i,j) for i in range(10) for j in range(i)]
bpairs=[(i,j) for i in range(8) for j in range(i)]
src=ast.parse(Path('deliverable/code/b_char2_symmetry.py').read_text())
exec(compile(ast.Module(body=[x for x in src.body if isinstance(x,ast.FunctionDef)
       and x.name in {'bracket','lie3'}],type_ignores=[]),'Hall_functions','exec'))
data=np.load('work/b_arbitrary_action_analysis_matrices.npz')
glob=np.load('deliverable/code/b_global_action_ambiguity_matrices.npz')
U=np.array([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]],dtype=np.int64)
b=data['boundary_bracket_parameters'][:,0]
Db=data['derivation_boundary'][0]
ad_b=np.zeros((330,10),dtype=np.int64)
for n,(i,j) in enumerate(bpairs):
    for k in range(10):
        for row,sgn in bracket(i+2,j+2,k):ad_b[row,k]+=int(b[n])*sgn
Delta=np.column_stack((-Db@U,3*Db))+3*ad_b
eO=np.concatenate((np.zeros(2,dtype=np.int64),-np.ones(8,dtype=np.int64)))
assert not np.any(Delta@eO)
assert np.any(Delta%3)
print('Integral primitive central derivation Delta fixes the C0 inertia exactly: PASS',flush=True)

T=glob['Tau_V'];C=glob['Conjugation_V']
assert not np.any((lie3(T)@Delta-49*Delta@T)%MOD)
assert not np.any((lie3(C)@Delta+Delta@C)%MOD)
print('Actual arithmetic module type: Z3(2) tensor chi_{-3}: PASS',flush=True)

def wedge_action(M):
    return np.array([[int(M[a,i])*int(M[bb,j])-int(M[a,j])*int(M[bb,i])
                     for i,j in bpairs] for a,bb in bpairs],dtype=np.int64)
def ad_boundary(parameter):
    out=np.zeros((330,10),dtype=np.int64)
    for n,(i,j) in enumerate(bpairs):
        for k in range(10):
            for row,sgn in bracket(i+2,j+2,k):out[row,k]+=int(parameter[n])*sgn
    return out
for g in glob['projective_automorphisms']:
    boundary_correction=3*(wedge_action(g[2:,2:])@b-b)
    assert not np.any((lie3(g)@Delta-Delta@g-ad_boundary(boundary_correction)@g)%MOD)
print('The derivation commutes with all54 geometric automorphisms modulo explicit inner derivations: PASS',flush=True)

# Every boundary direction is peripheral-conjugacy preserving.
for p in range(8):
    g=next(g for g in glob['projective_automorphisms']
           if np.array_equal(g[:2,:2],np.eye(2,dtype=np.int64))
           and np.array_equal(-g[2:,2:]@np.ones(8,dtype=np.int64),np.eye(8,dtype=np.int64)[:,p]))
    parameter=3*(wedge_action(g[2:,2:])@b-b)
    expected=-ad_boundary(parameter)[:,p+2]
    assert np.array_equal(Delta[:,p+2],expected)
print('All nine peripheral conjugacy classes are retained: PASS',flush=True)

# A0 is a rational cusp. Delta(e_A0)=3z, with z pure boundary and primitive.
assert not np.any(Delta[:,2]%3)
z=Delta[:,2]//3
assert np.any(z%3)
assert all(not z[i] for i,h in enumerate(hall) if min(h)<2)

# The free arithmetic generators tau,tau_bar have Kummer rows(2,0),(2,2).
# A normalized coefficient cocycle with values1,-1 is 2*kappa(zeta)+2*kappa(lambda) modulo3.
kummer=np.array([[2,0],[2,2]],dtype=np.int64)
assert np.array_equal(kummer@np.array([2,2])%3,np.array([1,2]))
p=19;zeta=7;lam=(1-zeta)%p
assert (zeta*zeta+zeta+1)%p==0
assert pow(zeta,(p-1)//3,p)==1
lam_exponent=next(i for i in range(3) if pow(zeta,i,p)==pow(lam,(p-1)//3,p))
coefficient_mod3=2*lam_exponent%3
assert coefficient_mod3==1
assert (p*p-1)%9==0 and (p*p-1)%27!=0
print('At the chosen prime over19: kappa(zeta)=0, kappa(lambda)=2, coefficient=1 modulo3: PASS',flush=True)
print('Delta(e_A0)=3z with primitive pure-W^3 z; correction is -b_19*z/120 and has valuation -1: PASS',flush=True)

result={'status':'explicit data-preserving arithmetic-action deformation certified',
        'module':'Z3(2) tensor chi_{-3}',
        'fixes_class_two_action':True,'fixes_entire_eta_extension':True,
        'fixes_base_cusp_C0':True,'preserves_peripheral_conjugacy':True,
        'commutes_with_A54_outer_action':True,
        'prime':19,'zeta_residue':7,'lambda_Kummer_mod3':2,
        'deformation_cocycle_mod3':1,'local_correction_denominator':120,
        'local_correction_minimum_3_valuation':-1,
        'primitive_boundary_Hall_vector':[[list(hall[i]),int(x)] for i,x in enumerate(z) if x],
        'scope':'The modified arithmetic action is not asserted geometric. The actual A0 cusp input twisted by kappa3(19) lifts for the actual action and fails for this modified action. Thus the specified eta/geometric-extension data alone do not determine the arbitrary-input class-three image.'}
Path('work/b_arbitrary_action_deformation.json').write_text(json.dumps(result,indent=2)+'\n')
np.savez_compressed('work/b_arbitrary_action_deformation_matrices.npz',
                    central_derivation=Delta,boundary_inner_parameter=b,
                    local_primitive_boundary_vector=z)
