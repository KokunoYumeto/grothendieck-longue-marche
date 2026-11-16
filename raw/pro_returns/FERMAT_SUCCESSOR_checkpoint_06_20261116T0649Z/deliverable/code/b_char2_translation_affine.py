#!/usr/bin/env python3
"""Exhaustive affine translation test for the cubic local eta at two.

The geometric path classes are the exact framed-Picard calculations in
c_char2_translation_paths.py.  All three equivariant integral Kummer
comparisons are retained.  Congruences are solved as affine lattices, so
no unrecorded choice of a 3-adic division or logarithm is made.
"""
import contextlib
import io
import json
import runpy
from collections import Counter
import numpy as np

with contextlib.redirect_stdout(io.StringIO()):
    c = runpy.run_path('deliverable/code/b_char2_symmetry.py')
    p = runpy.run_path('deliverable/code/c_char2_translation_paths.py')
MOD = c['MOD']
U = c['U']
smith = c['smith_transport']
lie3 = c['lie3']
bracket = c['bracket']
D = c['D']
E = c['E']
e2 = c['e2']
domain_moduli = np.array([3**e for e in e2], dtype=np.int64)
largest_modulus = int(max(domain_moduli))

coords = c['expected']
index = {x:i for i,x in enumerate(coords)}
Ts = []
LTs = []
for shift in [(1,0),(0,1)]:
    P = np.zeros((8,8), dtype=np.int64)
    for j,(a,b) in enumerate(coords):
        target = ((a+shift[0])%3,(b+shift[1])%3)
        if target == (0,0):
            P[:,j] = -1  # retain the integral -1 before division by three
        else:
            P[index[target],j] = 1
    raw = U-P@U
    assert not np.any(raw%3)
    T = np.zeros((10,10), dtype=np.int64)
    T[:2,:2] = np.eye(2,dtype=np.int64)
    T[2:,:2] = raw//3
    T[2:,2:] = P
    T %= MOD
    assert np.array_equal(T@T%MOD@T%MOD,np.eye(10,dtype=np.int64))
    L = lie3(T)
    assert not np.any((L@D-D@L)%MOD)
    Ts.append(T)
    LTs.append(L)

# The integral map x |-> [x,w], w=u wedge v.
adw = np.zeros((330,10),dtype=np.int64)
u = np.concatenate((np.array([3,0],dtype=np.int64),U[:,0]))
v = np.concatenate((np.array([0,3],dtype=np.int64),U[:,1]))
for k in range(10):
    for i in range(10):
        for j in range(10):
            coeff = -int(u[i])*int(v[j])
            if coeff:
                for row,sign in bracket(i,j,k):
                    adw[row,k] += coeff*sign
adw %= MOD
assert not np.any((adw@c['eO']-c['br'])%MOD)
for T,L in zip(Ts,LTs):
    assert not np.any((L@adw-adw@T)%MOD)
assert not np.any((c['LR']@adw-adw@c['RV'])%MOD)

fullvals,Qfull = smith(D)
print('Full F4 local Smith valuations:',dict(sorted(Counter(fullvals).items())),flush=True)
positive = [i for i,e in enumerate(fullvals) if e]
target_exponents = [fullvals[i] for i in positive]
target_moduli = np.array([3**e for e in target_exponents],dtype=np.int64)
assert max(fullvals)==4 and len(positive)==198

# Restriction from Q2 to its unramified quadratic extension is 1+Frob2.
embedding4 = E@(np.eye(41,dtype=np.int64)+c['R2_41'])%MOD
embedding4 = embedding4@c['Q2inv'][:,c['pos2']]%MOD
maps = []
for g in [c['LR']]+LTs:
    gmap = Qfull@(g-np.eye(330,dtype=np.int64))%MOD@embedding4%MOD
    gmap = gmap[positive,:]
    gmap %= target_moduli[:,None]
    assert not np.any((gmap*domain_moduli[None,:])%target_moduli[:,None])
    maps.append(gmap)
matrix = np.vstack(maps)
row_moduli = np.tile(target_moduli,3)

def target_of_path(alpha):
    x = Qfull@adw%MOD@alpha%MOD
    return x[positive]%target_moduli

sigma_target = target_of_path(c['eO'])
assert np.any(sigma_target)
assert not np.any(3*sigma_target%target_moduli)

def solve_affine(matrix,target,moduli,killed_by=None):
    """Solve rowwise a*y=b mod 3^r, returning a complete affine lattice.

    An update substitutes a unimodular coordinate elimination followed by
    one 3-power scaling.  Reduction modulo 81 is harmless because every
    domain and target group is annihilated by 81.
    """
    n=matrix.shape[1]
    base=np.zeros(n,dtype=np.int64)
    lattice=np.eye(n,dtype=np.int64)
    equations=list(zip(matrix,target,moduli))
    if killed_by is not None:
        equations += [(np.eye(n,dtype=np.int64)[i],0,3**max(e-killed_by,0))
                      for i,e in enumerate(e2)]
    for equation_index,(a,b,modulus) in enumerate(equations):
        modulus=int(modulus)
        if modulus==1:
            continue
        coefficients=a@lattice%modulus
        residual=(int(b)-int(a@base))%modulus
        power=1
        while power<modulus and not np.any((coefficients//power)%3):
            power*=3
        if power==modulus:
            if residual:
                return None,{'inconsistent_row':equation_index,'modulus':modulus,'residual':residual}
            continue
        if residual%power:
            return None,{'inconsistent_row':equation_index,'modulus':modulus,
                         'common_divisor':power,'residual':residual}
        pivot=int(np.nonzero((coefficients//power)%3)[0][0])
        reduced_modulus=modulus//power
        inverse=pow(int(coefficients[pivot])//power,-1,reduced_modulus)
        shift=(inverse*(residual//power))%reduced_modulus
        old=lattice[:,pivot].copy()
        base=(base+old*shift)%largest_modulus
        quotients=(inverse*(coefficients//power))%reduced_modulus
        quotients[pivot]=0
        lattice=(lattice-old[:,None]*quotients[None,:])%largest_modulus
        lattice[:,pivot]=old*reduced_modulus%largest_modulus
    base%=domain_moduli
    lattice%=domain_moduli[:,None]
    assert not np.any((matrix@base-target)%moduli)
    assert not np.any((matrix@lattice)%moduli[:,None])
    if killed_by is not None:
        assert not np.any((3**killed_by*base)%domain_moduli)
        assert not np.any((3**killed_by*lattice)%domain_moduli[:,None])
    return (base,lattice),None

homogeneous,_=solve_affine(matrix,np.zeros(len(matrix),dtype=np.int64),row_moduli)
assert homogeneous is not None
zero,kernel_lattice=homogeneous
kernel_order=max(c['orderval'](col,e2) for col in kernel_lattice.T)
kernel_quotient,_=smith(np.hstack((kernel_lattice,np.diag(domain_moduli))))
kernel_log_size=sum(e2)-sum(kernel_quotient)
assert kernel_order==1 and kernel_log_size==2
print('Exact homogeneous kernel: C3^2 (exponent3, order9)',flush=True)

records=[]
affine_targets=[]
for comparison in range(3):
    shear=(p['particular']+comparison*p['kernel'][0])%3
    alphas=[]
    for d in [p['P1'],p['P2']]:
        path=(d,p['tor_at'](d,p['logz'](p['ks'][d])))
        image=p['image'](path,shear)
        alpha=np.array(image[0]+image[1],dtype=np.int64)
        alphas.append(alpha)
    target=np.concatenate([sigma_target]+[target_of_path(a) for a in alphas])
    affine_targets.append(target)
    answer,error=solve_affine(matrix,target,row_moduli)
    record={'comparison':comparison,'shear':shear.tolist(),
            'translation_paths':[a.tolist() for a in alphas],
            'consistent':answer is not None}
    if answer is None:
        record['failure']=error
        print('Comparison',comparison,'INCONSISTENT:',error,flush=True)
        records.append(record)
        continue
    base,lattice=answer
    feasibility=[]
    least=None
    for k in range(1,5):
        small,failure=solve_affine(matrix,target,row_moduli,killed_by=k)
        feasibility.append(small is not None)
        if small is not None and least is None:
            least=k
            base=small[0]
    assert least is not None
    assert c['orderval'](base,e2)==least
    # The full set is an affine coset of C3^2; enumerate all nine members.
    members={tuple(int(x) for x in base)}
    for column in lattice.T:
        members={tuple(int(x) for x in (np.array(a)+t*column)%domain_moduli)
                 for a in members for t in range(3)}
    assert len(members)==9
    orders=sorted({c['orderval'](np.array(a),e2) for a in members})
    for a in members:
        assert not np.any((matrix@np.array(a)-target)%row_moduli)
    record.update({'least_order_exponent':least,'feasible_killed_by_powers_1_to_4':feasibility,
                   'particular_smith_coordinates':base.tolist(),
                   'number_of_solutions':len(members),'all_order_exponents':orders,
                   'all_solution_smith_coordinates':[list(a) for a in sorted(members)]})
    records.append(record)
    print('Comparison',comparison,'feasible orders killed by3^1..3^4:',feasibility,flush=True)
    print('  least exponent',least,'all nine solution exponents',orders,flush=True)
    print('  particular:',base.tolist(),flush=True)

# A short certificate for all 27 entries in the JSON list.  Increasing t
# by three stays in the same comparison and gives the second kernel
# direction.  Its twelfth coordinate is always 3 modulo 9.
base_all=np.array([0,0,1,2,0,2,5,9,6,9,24,3,36],dtype=np.int64)
direction3=np.array([0,0,2,1,1,3,0,0,18,9,0,0,0],dtype=np.int64)
direction9=np.array([0,0,0,0,0,6,6,0,18,0,18,9,27],dtype=np.int64)
assert c['orderval'](direction3,e2)==1
assert c['orderval'](direction9,e2)==2
for comparison,record in enumerate(records):
    claimed={tuple(int(x) for x in (base_all+s*direction3+t*direction9)%domain_moduli)
             for s in range(3) for t in range(9) if t%3==comparison}
    actual={tuple(x) for x in record['all_solution_smith_coordinates']}
    assert claimed==actual
    assert all(x[11]%9==3 for x in claimed)
    assert all(not np.any(27*np.array(x)%domain_moduli) for x in claimed)
print('All27 solutions: b+s*h3+t*h9, s mod3, t mod9; comparison=t mod3',flush=True)
print('Every twelfth Smith coordinate is3 mod9, and27 kills every solution: PASS',flush=True)

result={'status':'exact affine congruences solved for all three comparisons',
        'modulus':MOD,'domain_smith_exponents':e2,
        'target_smith_histogram':dict(sorted(Counter(fullvals).items())),
        'homogeneous_kernel_type':['C3','C3'],'comparisons':records,
        'all27_parametrization':{'base':base_all.tolist(),
                                'order3_direction':direction3.tolist(),
                                'order9_direction':direction9.tolist(),
                                'ranges':'s=0,1,2; t=0,...,8; comparison=t mod3'},
        'scope':'Geometric conclusion requires the framed Picard translation identity; '
                'all comparison choices and all resulting finite affine solutions are retained.'}
with open('deliverable/code/b_char2_translation_affine.json','w') as out:
    json.dump(result,out,indent=2)
    out.write('\n')
np.savez_compressed('deliverable/code/b_char2_translation_affine_matrices.npz',
                    modulus=np.array([MOD]),translations=np.stack(Ts),
                    Lie_translations=np.stack(LTs),ad_w=adw,
                    Smith_row_full_F4=Qfull,positive_F4=np.array(positive),
                    embedding_F2_to_full_F4=embedding4,
                    affine_matrix=matrix,affine_row_moduli=row_moduli,
                    affine_targets=np.stack(affine_targets),
                    domain_moduli=domain_moduli,kernel_lattice=kernel_lattice)
