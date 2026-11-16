#!/usr/bin/env python3
"""An intrinsic class-two finite quotient that detects the residual eta phase.

The input is the independently checked local coefficient row lambda_81.
Its restriction to J=[Zu+Zv,Lambda^2 V] has image 3 Z/81, so division
by three yields a primitive map J -> Z/27.  The induced alternating
pair Lambda^2 V -> (Z/27)^2 defines an actual class-two group, where
BCH is integral because 2 is a unit.  No Frobenius value on this
finite quotient is invented or calculated by this script.
"""
import json
from pathlib import Path
import numpy as np

MOD = 27
hall = [(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
hi = {h:i for i,h in enumerate(hall)}
pairs = [(i,j) for i in range(10) for j in range(i)]
U = np.array([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]], dtype=np.int64)
H = np.vstack((3*np.eye(2,dtype=np.int64),U))
ref = np.load('deliverable/code/b_action_ambiguity_refinement_matrices.npz')
aff = np.load('deliverable/code/b_char2_translation_affine_matrices.npz')
sym = np.load('deliverable/code/b_char2_symmetry_matrices.npz')
lam = ref['local_C81_detector'] % 81

def triple(i,j,k):
    """Hall expansion of [[e_i,e_j],e_k]."""
    if i == j:
        return []
    sign = 1
    if i < j:
        i,j,sign = j,i,-1
    if k >= j:
        return [(hi[i,j,k],sign)]
    return [(hi[i,k,j],sign),(hi[j,k,i],-sign)]

def lambda_h_b(h, i, j):
    # [h,[e_i,e_j]] = -[[e_i,e_j],h].
    return sum(-int(h[k])*sgn*int(lam[row])
               for k in range(10) for row,sgn in triple(i,j,k)) % 81

raw = np.array([[lambda_h_b(H[:,h],i,j) for i,j in pairs] for h in range(2)], dtype=np.int64)
assert not np.any(raw % 3)
phi = raw // 3
assert not np.any(lam @ aff['ad_w'] % 81)
assert np.any(phi % 3)
minors = [(a,b) for a in range(45) for b in range(a)
          if (int(phi[0,a])*int(phi[1,b])-int(phi[0,b])*int(phi[1,a])) % 3]
assert minors
print('lambda81 kills ad_w(V); lambda81(J)=3 Z/81: PASS')
print('Alternating map Lambda^2(V/27) -> (Z/27)^2 is onto: PASS')

def wedge_action(M):
    return np.array([[int(M[a,i])*int(M[b,j])-int(M[a,j])*int(M[b,i])
                      for i,j in pairs] for a,b in pairs], dtype=np.int64) % MOD

# The actual local Frobenius-two compact matrix and glued V matrix.
q = sym['Q8_matrices']
precision = 3**10
compact = (q[4,:2,:2]-q[6,:2,:2]) % precision
Pc = np.zeros((8,8),dtype=np.int64)
for j,i in enumerate([0,2,1,3,5,4,7,6]):
    Pc[i,j] = 1
cross = U @ compact - 2*Pc @ U
assert not np.any(cross % 3)
F = np.block([[compact,np.zeros((2,8),dtype=np.int64)], [cross//3,2*Pc]]) % MOD
M = compact % MOD
assert (int(M[0,0])*int(M[1,1])-int(M[0,1])*int(M[1,0])) % MOD == 2
assert np.array_equal(F@H % MOD,H@M % MOD)
Minv = pow(2,-1,MOD)*np.array([[M[1,1],-M[0,1]],[-M[1,0],M[0,0]]],dtype=np.int64) % MOD
C = 2*Minv.T % MOD
assert np.array_equal(phi @ wedge_action(F) % MOD,C @ phi % MOD)
print('Kernel of phi is stable under actual local Frobenius: PASS')
print('Central Frobenius matrix 2 M^{-t}:',C.tolist())

def bracket(x,y):
    wedge = np.array([int(x[i])*int(y[j])-int(x[j])*int(y[i]) for i,j in pairs],dtype=np.int64)
    return phi @ wedge % MOD

def multiply(left,right):
    x,z = left
    y,t = right
    return ((x+y)%MOD,(z+t+14*bracket(x,y))%MOD)

def action(g,B):
    x,z = g
    return (F@x%MOD,(C@z+B@x)%MOD)

# Integral BCH at class two: all linear B give automorphisms above F,C.
# Deterministic test vectors supplement the exact bilinear/equivariance proof.
rng = np.random.default_rng(810027)
for _ in range(100):
    g=(rng.integers(MOD,size=10),rng.integers(MOD,size=2))
    h=(rng.integers(MOD,size=10),rng.integers(MOD,size=2))
    k=(rng.integers(MOD,size=10),rng.integers(MOD,size=2))
    B=rng.integers(MOD,size=(2,10))
    assert all(np.array_equal(x,y) for x,y in zip(multiply(multiply(g,h),k),multiply(g,multiply(h,k))))
    assert all(np.array_equal(x,y) for x,y in zip(action(multiply(g,h),B),multiply(action(g,B),action(h,B))))

# Exact linear functional on the unknown quadratic Frobenius translation B.
# eta = (1/2)([B(u),F(v)]+[F(u),B(v)]).
# The two coordinates of B(x) evaluate brackets with u,v, respectively.
probe = np.zeros((2,10),dtype=np.int64)
probe[0,:] = (-int(M[0,1])*H[:,0]+int(M[0,0])*H[:,1])*pow(2,-1,MOD)%MOD
probe[1,:] = (-int(M[1,1])*H[:,0]+int(M[1,0])*H[:,1])*pow(2,-1,MOD)%MOD
assert np.any(probe%3)
print('Detector of eta(F2) is a primitive linear functional of the actual quadratic B matrix: PASS')

# A quadratic coordinate change z -> z+E*x adds E*F-C*E to B.
# Verify annihilation on a complete basis, not merely sampled changes.
for i in range(2):
    for j in range(10):
        E=np.zeros((2,10),dtype=np.int64)
        E[i,j]=1
        assert np.sum(probe*(E@F-C@E))%MOD == 0
# Changing the arithmetic lift by an inner automorphism adds [t,F*x].
# This is equivalent to lambda81(ad_w t)=0; check all ten basis vectors.
for i in range(10):
    t=np.eye(10,dtype=np.int64)[:,i]
    inner_B=np.column_stack([bracket(t,F[:,j]) for j in range(10)])
    assert np.sum(probe*inner_B)%MOD == 0
print('The probe annihilates all coordinate coboundaries and all inner lift changes: PASS')
wedge_w=np.array([int(H[i,0])*int(H[j,1])-int(H[i,1])*int(H[j,0]) for i,j in pairs],dtype=np.int64)
assert not np.any(phi@wedge_w%MOD)

# Modulo-three radical of the pair of alternating forms (size information only).
contractions = np.zeros((20,10),dtype=np.int64)
for h in range(2):
    for col,(i,j) in enumerate(pairs):
        contractions[10*h+j,i] += phi[h,col]
        contractions[10*h+i,j] -= phi[h,col]
A=contractions.copy()%3
rank=0
for col in range(10):
    nz=np.flatnonzero(A[rank:,col])
    if not len(nz):
        continue
    row=rank+int(nz[0]); A[[row,rank]]=A[[rank,row]]
    A[rank]=A[rank]*int(A[rank,col])%3
    for r in range(20):
        if r!=rank:
            A[r]=(A[r]-A[r,col]*A[rank])%3
    rank+=1
print('Common radical dimension modulo3:',10-rank)
print('Actual local class-two quotient: |G|=27^12=3^36; exponent27; derived group C27^2')
print('Full Frobenius quadratic matrix B is not computed here; its probe is evaluated separately by c_geometric_phase_verify.py')

result = {
    'status':'proved finite intrinsic detector; target value evaluated separately by the geometric phase certificate',
    'coefficient_modulus_on_J':27,
    'kills_inner_columns':True,
    'alternating_map_rank':2,
    'surjective_minor_columns':minors[0],
    'group_log3_order':36,
    'group_exponent':27,
    'group_nilpotency_class':2,
    'abelianization':'C27^10',
    'derived_subgroup':'C27^2',
    'central_Frobenius':C.tolist(),
    'compact_Frobenius':M.tolist(),
    'common_radical_dimension_mod3':10-rank,
    'quadratic_coordinate_invariant':True,
    'inner_Frobenius_lift_invariant':True,
    'determinant_commutator_in_central_kernel':True,
    'oriented_remaining_difference_mod27':18,
    'phi_Lambda2':phi.tolist(),
    'probe_unknown_quadratic_B':probe.tolist(),
    'scope':'An actual Frobenius-stable quotient of the intrinsic geometric group detects the remaining eta phase through its automorphism. The separate geometric phase certificate evaluates the requested scalar as19 modulo27; the full quadratic Frobenius matrix and function-field cover are not computed here.'
}
Path('deliverable/code/c_residual_class_two_detector.json').write_text(json.dumps(result,indent=2)+'\n')
np.savez_compressed('deliverable/code/c_residual_class_two_detector_matrices.npz',
                    phi=phi,compact_Frobenius=M,Frobenius_V=F,Frobenius_central=C,
                    probe_quadratic_Frobenius=probe,lambda81=lam,H=H)
