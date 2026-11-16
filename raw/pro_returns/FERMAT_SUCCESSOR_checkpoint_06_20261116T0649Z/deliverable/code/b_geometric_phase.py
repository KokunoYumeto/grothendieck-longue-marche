#!/usr/bin/env python3
"""Actual outer geometric extension from the elliptic Schreier cover.

The candidate comparison is made on Q=Lie3(V)(-1)/ad_w(V), where
all choices of paths between tangential basepoints disappear.  The
CM-to-quaternion basis change is chosen strictly symplectic.
"""
import ast
from pathlib import Path
import json
from itertools import product
import numpy as np
import sympy as sp

PREC=10
MOD=3**PREC
hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
lookup={h:i for i,h in enumerate(hall)}
pairs=[(i,j) for i in range(10) for j in range(i)]
source=ast.parse(Path('deliverable/code/b_char2_symmetry.py').read_text())
exec(compile(ast.Module(body=[x for x in source.body if isinstance(x,ast.FunctionDef)
       and x.name in {'bracket','lie3','inverse_unit'}],type_ignores=[]),'Hall_functions','exec'))
sch=np.load('deliverable/code/b_elliptic_schreier_matrices.npz')
sch_words=json.loads(Path('deliverable/code/b_elliptic_schreier.json').read_text())
quo=np.load('deliverable/code/c_char2_inner_quotient_matrices.npz')
ref=np.load('deliverable/code/b_geometric_invariants_matrices.npz')
sym=np.load('deliverable/code/b_char2_symmetry_matrices.npz')
projection=quo['quotient_projection']
inclusion=quo['Lie_basis_change'][:,quo['kept_indices']]
P=sch['original_basis_in_Schreier']
Pinv=sch['Schreier_basis_in_original']
U=np.array([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]],dtype=np.int64)
u=np.concatenate(([3,0],U[:,0]))
v=np.concatenate(([0,3],U[:,1]))

def wedge_action(B):
    return np.array([[int(B[a,i])*int(B[b,j])-int(B[a,j])*int(B[b,i])
                     for i,j in pairs] for a,b in pairs],dtype=np.int64)%MOD
def central_bracket(b,x):
    out=np.zeros(330,dtype=np.int64)
    for n,(i,j) in enumerate(pairs):
        for k in range(10):
            coefficient=int(b[n])*int(x[k])%MOD
            if coefficient:
                for row,sgn in bracket(i,j,k):out[row]=(out[row]+sgn*coefficient)%MOD
    return out

L2inv=wedge_action(Pinv)
generators=[]
def reversed_fibre_quadratic(word):
    # Schreier words concatenate chronological paths from left to right.
    # Aut(fibre) uses composition: monodromy of x1...xr is M_xr...M_x1.
    # The linear coordinate is unchanged; the quadratic coordinate reverses.
    x=np.zeros(10,dtype=np.int64)
    twice=np.zeros(45,dtype=np.int64)
    for letter in reversed(word):
        y=np.zeros(10,dtype=np.int64);y[abs(letter)-1]=1 if letter>0 else -1
        twice+=np.array([int(x[i])*int(y[j])-int(x[j])*int(y[i]) for i,j in pairs],dtype=np.int64)
        x+=y
    return twice
for C,twice_B,images in zip(sch['translation_V'],sch['quadratic_Schreier_twice'],
                           sch_words['images_of_Schreier_generators']):
    fibre_twice=np.column_stack([reversed_fibre_quadratic(word) for word in images])
    assert np.array_equal(fibre_twice,-twice_B)
    B=L2inv@fibre_twice%MOD@P%MOD*pow(2,-1,MOD)%MOD
    t=(central_bracket(B@u%MOD,C@v%MOD)-central_bracket(B@v%MOD,C@u%MOD))%MOD
    tq=projection@t%MOD
    Aq=projection@lie3(C)%MOD@inclusion%MOD
    generators.append((C,Aq,tq))

# Exact finite geometric action after the primitive inner quotient.
I10=np.eye(10,dtype=np.int64)
group={tuple(I10.flatten()):(I10,np.zeros(320,dtype=np.int64))}
pending=[tuple(I10.flatten())]
while pending:
    oldkey=pending.pop()
    old,oldt=group[oldkey]
    for C,A,t in generators:
        new=C@old
        newt=(t+A@oldt)%MOD
        key=tuple(new.flatten())
        if key in group:
            assert np.array_equal(group[key][1],newt), 'Based path term survived outer quotient'
        else:
            group[key]=(new,newt);pending.append(key)
            assert len(group)<=54
assert len(group)==54
print('All54 outer geometric extension actions close, including every path relation: PASS',flush=True)
sum_t=sum((t for _,t in group.values()),start=np.zeros(320,dtype=np.int64))%MOD
h27=-sum_t*pow(2,-1,MOD)%MOD
for _,A,t in generators:
    assert not np.any(((A-np.eye(320,dtype=np.int64))@h27-27*t)%MOD)
print('Actual geometric extension represented by h27/27 in the invariant rational-coset group: PASS',flush=True)

# Choose a strict symplectic CM intertwiner B: S B=B R.
QI=sym['Q8_matrices'][2,:2,:2]
QJ=sym['Q8_matrices'][4,:2,:2]
QK=sym['Q8_matrices'][6,:2,:2]
S=-(np.eye(2,dtype=np.int64)+QI+QJ+QK)*pow(2,-1,MOD)%MOD
R=np.array([[0,-1],[1,-1]],dtype=np.int64)
B0=np.column_stack((np.array([1,0],dtype=np.int64),S[:,0]))
det=int(B0[0,0])*int(B0[1,1])-int(B0[0,1])*int(B0[1,0])
target=pow(det,-1,MOD)
root=1;power=3
for digit in range(1,PREC):
    choices=[root+k*power for k in range(3) if ((root+k*power)**2-target)%(3*power)==0]
    assert len(choices)==1
    root=choices[0];power*=3
B=B0*root%MOD
assert np.array_equal(B%3,np.eye(2,dtype=np.int64))
assert (int(B[0,0])*int(B[1,1])-int(B[0,1])*int(B[1,0]))%MOD==1
assert not np.any((S@B-B@R)%MOD)
cross=U@B-U
assert not np.any(cross%3)
K=np.block([[B,np.zeros((2,8),dtype=np.int64)],[cross//3,np.eye(8,dtype=np.int64)]])%MOD
Kq=projection@lie3(K)%MOD@inclusion%MOD
h27local=Kq@h27%MOD
invariants=Kq@ref['invariant_basis_modulus']%MOD

# The intertwiner is only known mod3^10, and the gluing divided by3;
# every calculation that follows is therefore checked at mod3^8.
verify_mod=3**8
assert not np.any((projection@lie3(K)%MOD@quo['Lie_basis_change'][:,quo['deleted_indices']])%verify_mod)
for (C,A,t) in generators:
    C_local=K@C%MOD@inverse_unit(K)%MOD
    A_local=projection@lie3(C_local)%MOD@inclusion%MOD
    assert not np.any((A_local@invariants-invariants)%verify_mod)

# Invariants have a unit 4x4 minor.  Record its row positions.
row_echelon=invariants.T.copy()%3
piv=[];r=0
for col in range(320):
    nz=np.flatnonzero(row_echelon[r:,col])
    if not len(nz):continue
    j=r+int(nz[0]);row_echelon[[r,j]]=row_echelon[[j,r]]
    row_echelon[r]=row_echelon[r]*int(row_echelon[r,col])%3
    for j in range(4):
        if j!=r:row_echelon[j]=(row_echelon[j]-row_echelon[j,col]*row_echelon[r])%3
    piv.append(col);r+=1
    if r==4:break
assert r==4
minor_inverse=inverse_unit(invariants[piv,:])

# D=Frob4−1 has four rational eigenvalues -3,3,-9,15.
# Its inverse times81 is -(D^3-6D^2-144D+54I)/15.
D=(quo['quotient_Frob4']-np.eye(320,dtype=np.int64))%MOD
polynomial=(D@D%MOD@D-6*(D@D%MOD)-144*D+54*np.eye(320,dtype=np.int64))%MOD
assert not np.any((D@polynomial+1215*np.eye(320,dtype=np.int64))%MOD)
local_candidates=quo['local_candidates']
numerator=polynomial@local_candidates%MOD
assert not np.any(numerator%3)
q81=-(numerator//3)*pow(5,-1,MOD//3)%(MOD//3)
assert not np.any((D@q81-81*local_candidates)%(MOD//3))
diff=(q81-3*h27local[:,None])%81
coefficients=minor_inverse@diff[piv,:]%MOD%81
errors=(diff-invariants@coefficients)%81
survives=~np.any(errors,axis=0)
survivor_indices=np.flatnonzero(survives)
print('Local B36 candidates matching the actual geometric extension:',len(survivor_indices),'of27',flush=True)
print('Indices:',survivor_indices.tolist(),flush=True)
xs=quo['candidate_Q2_coordinates']
for i in survivor_indices:print('Candidate:',xs[i].tolist(),flush=True)

# A short independent selection certificate in B36's affine parameters.
param=json.loads(Path('deliverable/code/b_char2_translation_affine.json').read_text())['all27_parametrization']
parameter_columns=np.array([param['base'],param['order3_direction'],param['order9_direction']],dtype=np.int64).T
parameter_values=quo['local_candidate_embedding']@parameter_columns%MOD
parameter_numerator=polynomial@parameter_values%MOD
assert not np.any(parameter_numerator%3)
parameter_cosets=-(parameter_numerator//3)*pow(5,-1,MOD//3)%(MOD//3)
parameter_cosets[:,0]=(parameter_cosets[:,0]-3*h27local)%(MOD//3)
parameter_errors=(parameter_cosets-invariants@(minor_inverse@parameter_cosets[piv,:]%MOD))%81
short_rows=[]
for row,expected in [(54,[0,27,0]),(81,[27,0,9])]:
    ell=np.zeros(320,dtype=np.int64);ell[row]=1
    ell[piv]-=invariants[row]@minor_inverse%MOD
    ell%=81
    assert not np.any(ell@invariants%81)
    assert np.array_equal(ell@parameter_cosets%81,np.array(expected,dtype=np.int64))
    short_rows.append(ell)
assert np.array_equal(parameter_errors@np.array([1,0,6],dtype=np.int64)%81,np.zeros(320,dtype=np.int64))
assert len(survivor_indices)==1
assert np.array_equal(xs[survivor_indices[0]],
                      (parameter_columns[:,0]+6*parameter_columns[:,2])%
                      np.load('deliverable/code/b_char2_translation_affine_matrices.npz')['domain_moduli'])
print('Sparse selection congruences: 27*s=0 and 27+9*t=0 modulo81; hence s=0,t=6: PASS',flush=True)

result={'status':'actual geometric extension computed; local compatibility tested',
        'geometric_group_order':54,'surviving_candidate_indices':survivor_indices.tolist(),
        'surviving_Q2_coordinates':xs[survivor_indices].tolist(),
        'intertwiner_compact_modulus':B.tolist(),'modulus':MOD,
        'sparse_congruences':[
            {'quotient_row':row,'functional_entries':[[int(i),int(x if x<=40 else x-81)]
                    for i,x in enumerate(ell) if x],
             'values_on_base_h3_h9':parameter_errors[row].tolist()}
            for row,ell in zip([54,81],short_rows)],
        'selected_affine_parameters':{'s_mod3':0,'t_mod9':6},
        'local_C81_detector_value':57,'intrinsic_C27_detector_value':19,
        'chronological_to_fibre_convention':'Reverse every chronological path word; this preserves V and negates its quadratic BCH coordinate.',
        'scope':'Uses a strict symplectic CM intertwiner; independence of its unknown centralizer is justified by the actual arithmetic tau/tau_bar action, separately in the proof. The chronological-to-fibre geometric bridge is proved in B.40.'}
Path('deliverable/code/b_geometric_phase.json').write_text(json.dumps(result,indent=2)+'\n')
np.savez_compressed('deliverable/code/b_geometric_phase_matrices.npz',
                    geometric_Q_actions=np.stack([A for _,A,_ in generators]),
                    geometric_displacements=np.stack([t for _,_,t in generators]),
                    geometric_rational_coset_times27=h27,
                    CM_to_Q8_compact=B,CM_to_Q8_V=K,CM_to_Q8_Q=Kq,
                    local_geometric_coset_times27=h27local,
                    local_invariant_basis=invariants,candidate_rational_cosets_times81=q81,
                    candidate_compatibility_errors=errors,
                    parameter_compatibility_errors=parameter_errors,
                    sparse_selection_rows=np.stack(short_rows),
                    survivor_indices=survivor_indices)
