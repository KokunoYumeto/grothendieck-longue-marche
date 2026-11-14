#!/usr/bin/env python3
"""Exact signed dual orbits of the actual 97-dimensional Q-module.

This verifies the actual Q=SL2(Z/12)/{+-I} action on N_ab/3.
It does not replace the enormous arithmetic G3 by a surrogate.
The symbolic lift uses these actual character projectors; membership
in the active set remains specified by the actual subgroup A.
"""
from pathlib import Path
from collections import deque
import hashlib,json,time
import numpy as np

OUT=Path(__file__).resolve().parent
started=time.time()
input_path=OUT/'d_arithmetic_correction_graph.json'
data=json.loads(input_path.read_text())
states=[tuple(x) for x in data['Q_states']]
index={a:i for i,a in enumerate(states)}
assert len(states)==len(index)==576
def norm(a):return min(tuple(a),tuple(-x%12 for x in a))
def mul(a,b):
    x,y,z,w=a;p,q,r,s=b
    return norm(((x*p+y*r)%12,(x*q+y*s)%12,
                 (z*p+w*r)%12,(z*q+w*s)%12))
identity=index[norm((1,0,0,1))]
assert identity==0
S=index[norm((0,1,11,0))]
R=index[norm((0,11,1,11))]
table=np.array([[index[mul(a,b)] for b in states] for a in states],dtype=np.int16)
rs=table[:,S].tolist();rr=table[:,R].tolist()
assert rs==data['right_s'] and rr==data['right_r']
v2=[(0,min(g,rs[g])) for g in range(576)]
v3=[(1,min(g,rr[g],rr[rr[g]])) for g in range(576)]
adj={v:[] for v in set(v2+v3)}
for e in range(576):
    adj[v2[e]].append((v3[e],e))
    adj[v3[e]].append((v2[e],e))
paths={v2[0]:{}};queue=deque([v2[0]]);tree=set()
while queue:
    v=queue.popleft()
    for u,e in adj[v]:
        if u not in paths:
            c=paths[v].copy();c[e]=c.get(e,0)+(1 if v[0]==0 else -1)
            if not c[e]:del c[e]
            paths[u]=c;tree.add(e);queue.append(u)
chords=[e for e in range(576) if e not in tree]
assert chords==data['cycle_chords'] and len(chords)==97
ci={e:i for i,e in enumerate(chords)}
cycles=[]
for e in chords:
    c=paths[v2[e]].copy()
    for j,a in paths[v3[e]].items():c[j]=c.get(j,0)-a
    c[e]=c.get(e,0)+1
    cycles.append({j:a for j,a in c.items() if a})
matrices=np.zeros((576,97,97),dtype=np.int16)
for g in range(576):
    for j,c in enumerate(cycles):
        for edge,coefficient in c.items():
            image=int(table[g,edge])
            if image in ci:
                matrices[g,ci[image],j]+=coefficient
matrices%=3
I=np.eye(97,dtype=np.int16)
assert np.array_equal(matrices[0],I)
assert matrices[S].T.tolist()==data['mod3_s_columns']
assert matrices[R].T.tolist()==data['mod3_r_columns']
for token in (S,R):
    for g in range(576):
        assert np.array_equal((matrices[g]@matrices[token])%3,
                              matrices[int(table[g,token])])

def rank3(a):
    a=np.array(a,dtype=np.int16,copy=True)%3
    row=0
    for col in range(a.shape[1]):
        candidates=np.flatnonzero(a[row:,col])
        if not len(candidates):continue
        p=row+int(candidates[0])
        if p!=row:a[[p,row]]=a[[row,p]]
        if a[row,col]==2:a[row]=(2*a[row])%3
        factors=a[row+1:,col].copy()
        a[row+1:]=(a[row+1:]-factors[:,None]*a[row])%3
        row+=1
        if row==a.shape[0]:break
    return row

fixed=[]
bad_upper=0
for g in range(576):
    plus=97-rank3(matrices[g]-I)
    minus=97-rank3(matrices[g]+I)
    fixed.append({'q_state':g,'fix_plus_dimension':plus,
                  'fix_minus_dimension':minus})
    if g:bad_upper+=3**plus-1
    bad_upper+=3**minus-1
assert fixed[0]['fix_plus_dimension']==97
assert fixed[0]['fix_minus_dimension']==0
active_lower=80*3**93
good_active_lower=active_lower-bad_upper
assert good_active_lower>0
orbit_lower=(good_active_lower+1151)//1152

# Ninety-seven independent literal covectors each have a free signed orbit.
# This also detects every nonzero possible actual parameter without choosing it.
rng=np.random.default_rng(0xD59)
pivots={};basis=[];trials=0
while len(basis)<97:
    trials+=1
    v=rng.integers(0,3,size=97,dtype=np.int16)
    images=np.einsum('i,qij->qj',v,matrices,dtype=np.int32)%3
    same=np.flatnonzero(np.all(images==v,axis=1)).tolist()
    opposite=np.flatnonzero(np.all(images==(-v)%3,axis=1)).tolist()
    if same!=[0] or opposite:continue
    reduced=v.copy()
    for p in sorted(pivots):
        if reduced[p]:reduced=(reduced-reduced[p]*pivots[p])%3
    candidates=np.flatnonzero(reduced)
    if not len(candidates):continue
    p=int(candidates[0])
    if reduced[p]==2:reduced=(2*reduced)%3
    pivots[p]=reduced;basis.append(v.tolist())
assert rank3(basis)==97
assert all(len({tuple(x) for x in (np.einsum('i,qij->qj',np.array(v,dtype=np.int16),matrices,dtype=np.int32)%3).tolist()})==576 for v in basis)

# Uniform nontrivial cusp characters.  The 48 actual N-cusps have one
# primitive sum relation.  Setting every value equal to1 is consistent
# over F3 because48=0; the resulting affine space has dimension50.
t=int(table[S,R]);powers=[0];at=t
while at:
    powers.append(at);at=int(table[at,t])
assert len(powers)==12
cosets={min(int(table[g,h]) for h in powers) for g in range(576)}
assert len(cosets)==48
cusp_representatives=sorted(cosets)
cusp0=np.array(data['actual_cusp_t12_mod3_cycle'],dtype=np.int16)
cusp_columns=np.column_stack([(matrices[g]@cusp0)%3 for g in cusp_representatives])
assert rank3(cusp_columns)==47
assert not np.any(cusp_columns.sum(axis=1)%3)
for token in (S,R):
    assert {tuple(v) for v in ((matrices[token]@cusp_columns)%3).T.tolist()}=={tuple(v) for v in cusp_columns.T.tolist()}
small_path=OUT/'d_arithmetic_affine_base.json'
small=json.loads(small_path.read_text())
phi=np.array(small['actual_quotient_covector_rows'],dtype=np.int16)
assert rank3(phi)==4 and not np.any((phi@cusp_columns)%3)
assert small['actual_parameter_s_r_candidates']==[[2,1,2,1]]

def affine_solve3(a,b):
    a=np.array(a,dtype=np.int16,copy=True)%3
    b=np.array(b,dtype=np.int16,copy=True)%3
    augmented=np.column_stack([a,b]);row=0;piv=[]
    for col in range(a.shape[1]):
        choices=np.flatnonzero(augmented[row:,col])
        if not len(choices):continue
        p=row+int(choices[0])
        if p!=row:augmented[[p,row]]=augmented[[row,p]]
        if augmented[row,col]==2:augmented[row]=(2*augmented[row])%3
        factors=augmented[:,col].copy();factors[row]=0
        augmented=(augmented-factors[:,None]*augmented[row])%3
        piv.append(col);row+=1
        if row==a.shape[0]:break
    if any(not np.any(q[:-1]) and q[-1] for q in augmented):return None,row,None
    particular=np.zeros(a.shape[1],dtype=np.int16)
    for j,p in enumerate(piv):particular[p]=augmented[j,-1]
    free=[j for j in range(a.shape[1]) if j not in piv]
    null=[]
    for f in free:
        v=np.zeros(a.shape[1],dtype=np.int16);v[f]=1
        for j,p in enumerate(piv):v[p]=-augmented[j,f]%3
        null.append(v)
    null=np.column_stack(null) if null else np.zeros((a.shape[1],0),dtype=np.int16)
    assert np.array_equal((a@particular)%3,b)
    assert not np.any((a@null)%3)
    return particular,row,null

uniform0,uniform_rank,uniform_kernel=affine_solve3(cusp_columns.T,np.ones(48,dtype=np.int16))
assert uniform_rank==47 and uniform_kernel.shape==(97,50)
uniform_fixed=[];uniform_bad_upper=0
for g in range(1,576):
    defect=matrices[g].T-I
    particular,rank,_=affine_solve3(defect@uniform_kernel,-defect@uniform0)
    consistent=particular is not None
    count=3**(50-rank) if consistent else 0
    uniform_bad_upper+=count
    uniform_fixed.append({'q_state':g,'consistent':consistent,
                          'affine_fixed_dimension':50-rank if consistent else None,
                          'fixed_point_count':str(count)})
uniform_active_lower=2*3**49
uniform_good_lower=uniform_active_lower-uniform_bad_upper
assert uniform_good_lower>0
uniform_orbit_lower=(uniform_good_lower+575)//576

# A literal affine spanning family of51 free characters certifies that
# no nonzero compact parameter can annihilate the entire free family.
uniform_family=[];uniform_pivots={};uniform_trials=0
while len(uniform_family)<51:
    uniform_trials+=1
    v=(uniform0+uniform_kernel@rng.integers(0,3,size=50,dtype=np.int16))%3
    images=np.einsum('i,qij->qj',v,matrices,dtype=np.int32)%3
    assert np.all((images@cusp_columns)%3==1)
    same=np.flatnonzero(np.all(images==v,axis=1)).tolist()
    assert not np.any(np.all(images==(-v)%3,axis=1))
    if same!=[0]:continue
    if not uniform_family:
        uniform_family.append(v.tolist());continue
    reduced=(v-np.array(uniform_family[0],dtype=np.int16))%3
    for p in sorted(uniform_pivots):
        if reduced[p]:reduced=(reduced-reduced[p]*uniform_pivots[p])%3
    candidates=np.flatnonzero(reduced)
    if not len(candidates):continue
    p=int(candidates[0])
    if reduced[p]==2:reduced=(2*reduced)%3
    uniform_pivots[p]=reduced;uniform_family.append(v.tolist())
assert rank3(np.array(uniform_family[1:],dtype=np.int16)-np.array(uniform_family[0],dtype=np.int16))==50
summary={
 'scope':'Actual 576-state Q module N_ab/3, reconstructed from its marked graph.',
 'Q_order':576,'module_dimension':97,
 'complete_generator_matrix_product_checks':1152,
 'signed_fixed_space_dimensions_evaluated':1152,
 'largest_nonidentity_positive_fixed_dimension':max(x['fix_plus_dimension'] for x in fixed[1:]),
 'largest_negative_fixed_dimension':max(x['fix_minus_dimension'] for x in fixed),
 'signed_bad_nonzero_covector_union_upper_bound':str(bad_upper),
 'actual_active_covector_lower_bound_from_Astar':str(active_lower),
 'free_signed_active_covector_lower_bound':str(good_active_lower),
 'free_signed_active_orbit_lower_bound':str(orbit_lower),
 'signed_free_basis_rank':97,'basis_sampling_trials':trials,
 'each_signed_free_orbit_vector_count':1152,
 'each_signed_free_orbit_pair_count':576,
 'nontrivial_character_homology_dimension_over_F4':96,
 'each_signed_free_central_block_dimension_over_F2':576*96**2,
 'each_signed_free_central_block_coinvariant_dimension':96**2,
 'small_quotient_nonzero_character_count':80,
 'free_signed_characters_cannot_factor_through_small_quotient':1152>80,
 'actual_N_cusp_count':48,'actual_cusp_span_rank_mod3':47,
 'actual_oriented_cusp_generator_permutation_checks':96,
 'uniform_cusp_character_affine_dimension':50,
 'small_quotient_kills_every_actual_N_cusp':True,
 'actual_arithmetic_parameter_has_nonzero_compact_image':True,
 'uniform_affine_fixed_systems_checked':575,
 'largest_consistent_uniform_fixed_dimension':max(x['affine_fixed_dimension'] for x in uniform_fixed if x['consistent']),
 'uniform_bad_character_union_upper_bound':str(uniform_bad_upper),
 'uniform_active_character_lower_bound':str(uniform_active_lower),
 'uniform_free_active_character_lower_bound':str(uniform_good_lower),
 'uniform_free_active_pair_orbit_lower_bound':str(uniform_orbit_lower),
 'uniform_signed_free_affine_spanning_family_size':51,
 'uniform_signed_free_affine_span_dimension':50,
 'uniform_family_sampling_trials':uniform_trials,
 'elapsed_seconds':round(time.time()-started,3)}
certificate={'summary':summary,
 'input_sha256':hashlib.sha256(input_path.read_bytes()).hexdigest(),
 'small_quotient_input_sha256':hashlib.sha256(small_path.read_bytes()).hexdigest(),
 'complete_signed_fixed_space_dimensions':fixed,
 'literal_signed_free_covector_basis':basis,
 'actual_cusp_representatives':cusp_representatives,
 'actual_cusp_columns':cusp_columns.T.tolist(),
 'uniform_cusp_affine_particular':uniform0.tolist(),
 'uniform_cusp_affine_kernel_columns':uniform_kernel.T.tolist(),
 'complete_uniform_affine_fixed_systems':uniform_fixed,
 'literal_uniform_free_affine_family':uniform_family}
(OUT/'d_arithmetic_free_characters.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
