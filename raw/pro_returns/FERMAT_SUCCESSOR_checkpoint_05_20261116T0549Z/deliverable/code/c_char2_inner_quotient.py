#!/usr/bin/env python3
"""Primitive quotient Lie3(V)(-1) / ad_w(V), in the B.36 coordinates.

The degree-one basis begins with the two integral factors of w.  The
inner-path image then consists of exactly ten Hall basis vectors, so
the quotient is obtained by literal deletion, with no saturation or
finite-precision rank assumption.
"""
from collections import Counter
import json
import time
import numpy as np
import sympy as sp

started=time.monotonic()
PREC=10
MOD=3**PREC
hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
index={h:i for i,h in enumerate(hall)}
assert len(hall)==330

def hall_bracket(a,b,c):
    if a==b:return ()
    sign=1
    if a<b:a,b,sign=b,a,-sign
    if c>=b:return ((index[a,b,c],sign),)
    return ((index[a,c,b],sign),(index[b,c,a],-sign))

def lie3(B):
    B=np.array(B,dtype=np.int64)%MOD
    nonzero=[[(i,int(B[i,j])) for i in range(10) if B[i,j]] for j in range(10)]
    result=np.zeros((330,330),dtype=np.int64)
    for column,(i,j,k) in enumerate(hall):
        for a,x in nonzero[i]:
            for b,y in nonzero[j]:
                for c,z in nonzero[k]:
                    coefficient=x*y*z%MOD
                    for row,sign in hall_bracket(a,b,c):
                        result[row,column]=(int(result[row,column])+sign*coefficient)%MOD
    return result

def smith_rows(B):
    """Full-row-rank square matrix: exact DVR pivots and row transport."""
    A=B.copy()%MOD
    n,m=A.shape
    assert n==m
    rows=np.eye(n,dtype=np.int64)
    valuations=[]
    for k in range(n):
        active=A[k:,k:]
        power=1
        for v in range(PREC):
            nz=np.argwhere((active//power)%3)
            if len(nz):break
            power*=3
        else:raise AssertionError('Expected pivot not visible at precision')
        i,j=map(int,nz[0]);i+=k;j+=k
        A[[k,i]]=A[[i,k]];rows[[k,i]]=rows[[i,k]]
        A[:,[k,j]]=A[:,[j,k]]
        unit=int(A[k,k])//power
        inverse=pow(unit,-1,MOD)
        A[k]=A[k]*inverse%MOD;rows[k]=rows[k]*inverse%MOD
        assert A[k,k]==power
        quot=A[:,k]//power
        assert not np.any(A[:,k]%power)
        quot[k]=0
        A=(A-quot[:,None]*A[k][None,:])%MOD
        rows=(rows-quot[:,None]*rows[k][None,:])%MOD
        for j in range(k+1,m):
            assert A[k,j]%power==0
            fac=int(A[k,j])//power
            A[:,j]=(A[:,j]-fac*A[:,k])%MOD
        valuations.append(v)
    assert np.array_equal(A,np.diag([3**v for v in valuations]))
    return valuations,rows

U=np.array([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]],dtype=np.int64)
u=np.concatenate(([3,0],U[:,0]))
v=np.concatenate(([0,3],U[:,1]))
remaining=[0,1,3,5,6,7,8,9]
VB=np.column_stack([u,v]+[np.eye(10,dtype=np.int64)[:,j] for j in remaining])
det=int(sp.Matrix(VB).det())
assert abs(det)==1
VBinv=np.array(sp.Matrix(VB).inv(),dtype=np.int64)
assert np.array_equal(VBinv@VB,np.eye(10,dtype=np.int64))
LB=lie3(VB)
LBinv=lie3(VBinv)
assert np.array_equal(LBinv@LB%MOD,np.eye(330,dtype=np.int64))
inner=[index[1,0,k] for k in range(10)]
keep=[j for j in range(330) if j not in inner]
assert len(keep)==320
affine=np.load('deliverable/code/b_char2_translation_affine_matrices.npz')
adw=affine['ad_w']
expected=np.zeros((330,10),dtype=np.int64)
for k,row in enumerate(inner):expected[row,k]=1
assert np.array_equal(LBinv@adw%MOD@VB%MOD,expected)
print('Integral adapted V basis has determinant',det,flush=True)
print('ad_w(V) is exactly the10 Hall basis columns(1,0,k); quotient rank320: PASS',flush=True)

# Compatible CM matrix in the quaternion basis; no c-conjugator is used.
symmetry=np.load('deliverable/code/b_char2_symmetry_matrices.npz')
quaternions=symmetry['Q8_matrices']
QI=quaternions[2,:2,:2]
QJ=quaternions[4,:2,:2]
QK=quaternions[6,:2,:2]
I2=np.eye(2,dtype=np.int64)
S=(-(I2+QI+QJ+QK)*pow(2,-1,MOD))%MOD
S2=S@S%MOD
assert np.array_equal((S2+S+I2)%MOD,np.zeros((2,2),dtype=np.int64))

def seven_matrix(compact_sigma):
    B=np.zeros((10,10),dtype=np.int64)
    B[:2,:2]=I2+3*compact_sigma
    B[2:,:2]=U@(compact_sigma-2*I2)
    B[2:,2:]=7*np.eye(8,dtype=np.int64)
    return B%MOD

T1=seven_matrix(S)
T2=seven_matrix(S2)
F4=np.zeros((10,10),dtype=np.int64)
F4[:2,:2]=-2*I2
F4[2:,:2]=-2*U
F4[2:,2:]=4*np.eye(8,dtype=np.int64)
F4%=MOD
actions=[];adapted_actions=[]
for name,M,chi in [('tau',T1,7),('tau_bar',T2,7),('Frob4',F4,4)]:
    adapted=VBinv@M%MOD@VB%MOD
    A=lie3(adapted)*pow(chi,-1,MOD)%MOD
    assert not np.any(A[np.ix_(keep,inner)])
    assert np.array_equal(A[np.ix_(inner,inner)],adapted)
    quotient=A[np.ix_(keep,keep)]
    actions.append(quotient)
    adapted_actions.append(A)
    print(name,'preserves primitive inner image and has the correct induced V action: PASS',flush=True)
for A in actions:
    for B in actions:assert not np.any((A@B-B@A)%MOD)
print('Both actual7-Frobenii and Frobenius4 commute on the quotient: PASS',flush=True)

projection=LBinv[keep,:]
local_embedding=projection@affine['embedding_F2_to_full_F4']%MOD
candidate_data=json.load(open('deliverable/code/b_char2_translation_affine.json'))
xs=[];comparison=[]
for record in candidate_data['comparisons']:
    for candidate in record['all_solution_smith_coordinates']:
        xs.append(candidate);comparison.append(record['comparison'])
xs=np.array(xs,dtype=np.int64)
local_candidates=local_embedding@xs.T%MOD
assert local_candidates.shape==(320,27)
domain=affine['domain_moduli']
global_vals,global_rows=smith_rows((actions[0]-np.eye(320,dtype=np.int64))%MOD)
local_vals,local_rows=smith_rows((actions[2]-np.eye(320,dtype=np.int64))%MOD)
print('Quotient tau−1 Smith valuations:',dict(sorted(Counter(global_vals).items())),flush=True)
print('Quotient Frob4−1 Smith valuations:',dict(sorted(Counter(local_vals).items())),flush=True)
positive=[i for i,e in enumerate(local_vals) if e]
local_moduli=np.array([3**local_vals[i] for i in positive],dtype=np.int64)
local_smith=(local_rows@local_candidates%MOD)[positive,:]%local_moduli[:,None]
orders=[]
for column in local_smith.T:
    k=next(k for k in range(max(local_vals)+1) if not np.any(3**k*column%local_moduli))
    orders.append(3**k)
print('Projected27 candidate orders:',dict(sorted(Counter(orders).items())),flush=True)
torsion_tests=[]
differences=[]
for name,action in [('tau',actions[0]),('tau_bar',actions[1])]:
    difference=local_rows@(action-np.eye(320,dtype=np.int64))%MOD@local_candidates%MOD
    residues=difference[positive,:]%local_moduli[:,None]
    fixed=~np.any(residues,axis=0)
    difference_orders=[]
    for column in residues.T:
        k=next(k for k in range(max(local_vals)+1)
               if not np.any(3**k*column%local_moduli))
        difference_orders.append(3**k)
    assert not np.any(fixed)
    assert set(difference_orders)=={9}
    small_index=positive.index(193)
    assert local_moduli[small_index]==9
    expected_small=6 if name=='tau' else 3
    assert np.all(residues[small_index]==expected_small)
    strong_index=positive.index(300)
    assert local_moduli[strong_index]==81
    expected_strong=18 if name=='tau' else 9
    assert np.all(residues[strong_index]%27==expected_strong)
    torsion_tests.append({
        'arithmetic_element':name,'fixed_candidates':int(np.sum(fixed)),
        'difference_orders':difference_orders,
        'constant_witness':{'zero_based_Smith_row':193,'modulus':9,
                            'value_on_all27':expected_small},
        'order9_witness':{'zero_based_Smith_row':300,'modulus':81,
                          'values':sorted(set(int(x) for x in residues[strong_index])),
                          'fixed_residue_mod27':expected_strong}})
    differences.append(residues)
    print(name,': no fixed candidate; all27 differences have exact order9',flush=True)
    print('  Universal witness: Smith row193 modulo9 =',expected_small,flush=True)
    print('  Strong witness: Smith row300 modulo81 =',
          sorted(set(int(x) for x in residues[strong_index])),flush=True)
# A sparse certificate in the original B.36 Hall basis, independent of
# displaying a 320-dimensional Smith transport.
sparse_terms=[((2,0,4),-1),((4,0,2),-2),((4,0,4),3),
              ((4,0,8),1),((8,0,4),-4)]
ell=np.zeros(330,dtype=np.int64)
for word,coefficient in sparse_terms:ell[index[word]]=coefficient
assert np.array_equal(ell%9,local_rows[193]@projection%9)
original_D4=(pow(4,-1,MOD)*lie3(F4)-np.eye(330,dtype=np.int64))%MOD
original_Tau=pow(7,-1,MOD)*lie3(T1)%MOD
assert not np.any(ell@original_D4%9)
assert not np.any(ell@adw%9)
detector=ell@(original_Tau-np.eye(330,dtype=np.int64))%MOD
detector=detector@affine['embedding_F2_to_full_F4']%MOD%9
expected_detector=np.array([0,0,0,0,0,0,3,6,6,6,6,0,0],dtype=np.int64)
assert np.array_equal(detector,expected_detector)
param=candidate_data['all27_parametrization']
assert int(detector@np.array(param['base']))%9==6
assert int(detector@np.array(param['order3_direction']))%9==0
assert int(detector@np.array(param['order9_direction']))%9==0
assert np.all(detector@xs.T%9==6)
print('Sparse mod9 functional: five Hall coefficients kill D4A and ad_wV: PASS',flush=True)
print('On(tau−1)e: 3*x7+6*(x8+x9+x10+x11)=6 mod9 for all27 candidates',flush=True)
result={
    'status':'primitive quotient and actual K/F4 action matrices certified',
    'modulus':MOD,'adapted_V_determinant':det,
    'deleted_Hall_vectors':[[1,0,k] for k in range(10)],
    'quotient_rank':320,
    'global_tau_Smith_histogram':dict(sorted(Counter(global_vals).items())),
    'local_Frob4_Smith_histogram':dict(sorted(Counter(local_vals).items())),
    'local_candidate_orders':orders,
    'global_torsion_exclusion_tests':torsion_tests,
    'sparse_mod9_certificate':{
        'Hall_terms':[{'word':list(word),'coefficient':coefficient}
                      for word,coefficient in sparse_terms],
        'kills':['D4A','ad_wV'],
        'coefficient_row_on_B36_Q2_coordinates':detector.tolist(),
        'values_on_base_order3_order9_directions':[6,0,0],
        'value_on_every_candidate':6},
    'conclusion':'No possible projected actual local eta class is the localization of a torsion global K-cohomology class.',
    'scope':'Global torsion comparison can use actual tau and conjugate tau over K; no unknown global c change of basis is used.',
    'elapsed_seconds':time.monotonic()-started}
with open('deliverable/code/c_char2_inner_quotient.json','w') as output:
    json.dump(result,output,indent=2);output.write('\n')
np.savez_compressed('deliverable/code/c_char2_inner_quotient_matrices.npz',
    modulus=np.array([MOD]),VB=VB,VBinv=VBinv,
    Lie_basis_change=LB,Lie_basis_inverse=LBinv,
    quotient_projection=projection,deleted_indices=np.array(inner),kept_indices=np.array(keep),
    compact_CM=S,Tau_V=T1,Tau_bar_V=T2,Frob4_V=F4,
    quotient_Tau=actions[0],quotient_Tau_bar=actions[1],quotient_Frob4=actions[2],
    global_tau_Smith_exponents=np.array(global_vals),global_tau_Smith_rows=global_rows,
    local_Smith_exponents=np.array(local_vals),local_Smith_rows=local_rows,
    local_positive_indices=np.array(positive),local_candidate_embedding=local_embedding,
    local_candidates=local_candidates,local_candidate_Smith=local_smith,
    global_difference_Smith=np.stack(differences),
    sparse_mod9_functional=ell,sparse_mod9_candidate_detector=detector,
    candidate_comparisons=np.array(comparison),candidate_Q2_coordinates=xs)
print('Saved all rank320 matrices and27 projected candidates.',flush=True)
print('Elapsed seconds:',round(result['elapsed_seconds'],3),flush=True)
