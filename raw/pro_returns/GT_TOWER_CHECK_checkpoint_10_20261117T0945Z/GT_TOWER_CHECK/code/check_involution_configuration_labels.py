#!/usr/bin/env python3
"""Exact component and relative-homology certificate for A.4.54.

Enumerates every compact mod-two matrix and every label permutation
centralizing the actual involution for n=9,10,11,12. For compatible
cases it constructs the missing relative-homology block. For every
incompatible case it identifies a fixed-label column obstruction.
"""
from pathlib import Path
from itertools import permutations, product
import json
import numpy as np

HERE=Path(__file__).resolve().parent
periods=[np.array(a,dtype=np.int64).reshape(2,2)
         for a in product(range(2),repeat=4)
         if (a[0]*a[3]-a[1]*a[2])%2==1]
assert len(periods)==6
two=[(3,0),(0,3),(3,3)]
three=[(0,0)]+[p for p in product((0,2,4),repeat=2) if p!=(0,0)]
pair_permutations=list(permutations(range(4)))
signs=list(product(range(2),repeat=4))
assert len(pair_permutations)*len(signs)==384
expected={9:(1,2304,2304),10:(3,4608,1536),
          11:(6,13824,2304),12:(6,55296,9216)}
records=[]
arrays={}
for n in range(9,13):
    k=n-8
    points=three+two[:k-1]
    index={p:i for i,p in enumerate(points)}
    sigma=[index[tuple((-v)%6 for v in p)] for p in points]
    fixed=[i for i,j in enumerate(sigma) if i==j]
    pairs=[(i,j) for i,j in enumerate(sigma) if i<j]
    assert len(fixed)==k and len(pairs)==4 and fixed[0]==0
    component_assignments=list(permutations(two,k-1))
    assert len(component_assignments)==expected[n][0]
    t=np.zeros((2,n),dtype=np.int64)
    for j in range(1,n):
        numer=-np.array(points[j])-np.array(points[sigma[j]])
        assert not np.any(numer%6)
        t[:,j]=numer//6%2
    P=np.zeros((n-1,n-1),dtype=np.int64)
    for j in range(1,n):P[sigma[j]-1,j-1]=1
    invol=np.block([[np.eye(2,dtype=np.int64),t[:,1:]],
                   [np.zeros((n-1,2),dtype=np.int64),P]])%2
    assert np.array_equal(invol@invol%2,np.eye(n+1,dtype=np.int64))
    for j in fixed:
        assert np.array_equal(t[:,j],(-np.array(points[j])//3)%2)
    arrays['involution_'+str(n)]=invol
    arrays['points_sixths_'+str(n)]=np.array(points)
    tested=passing=0
    branch_records=[]
    for ai,A in enumerate(periods):
        for fperm in permutations(fixed):
            fixed_map=dict(zip(fixed,fperm))
            branch_ok=all(np.array_equal(
                (A@np.array(points[j])+np.array(points[fixed_map[0]]))%6,
                np.array(points[fixed_map[j]])) for j in fixed)
            group_pass=0
            example=None
            for pp in pair_permutations:
                for bits in signs:
                    tau=[None]*n
                    for j,target in fixed_map.items():tau[j]=target
                    for j,(left,right) in enumerate(pairs):
                        targets=pairs[pp[j]]
                        tau[left]=targets[bits[j]]
                        tau[right]=targets[1-bits[j]]
                    assert sorted(tau)==list(range(n))
                    assert all(tau[sigma[j]]==sigma[tau[j]] for j in range(n))
                    S=np.zeros((n-1,n-1),dtype=np.int64)
                    for j in range(1,n):
                        if tau[j]:S[tau[j]-1,j-1]+=1
                        if tau[0]:S[tau[0]-1,j-1]-=1
                    S%=2
                    rhs=(t[:,1:]@S-A@t[:,1:])%2
                    obstruction=[j for j in fixed if j and np.any(rhs[:,j-1])]
                    possible=not obstruction
                    assert possible==branch_ok
                    assert all(np.array_equal(rhs[:,a-1],rhs[:,b-1])
                               for a,b in pairs)
                    tested+=1
                    if possible:
                        B=np.zeros((2,n-1),dtype=np.int64)
                        for a,b in pairs:B[:,a-1]=rhs[:,a-1]
                        assert np.array_equal((B@P-B)%2,rhs)
                        M=np.block([[A,B],[np.zeros((n-1,2),dtype=np.int64),S]])%2
                        assert np.array_equal(M@invol%2,invol@M%2)
                        passing+=1;group_pass+=1
                        if example is None:
                            example={'labels':tau,'relative_arc_block':B.tolist()}
                    elif example is None:
                        j=obstruction[0]
                        assert np.array_equal(P[:,j-1],np.eye(n-1,dtype=np.int64)[:,j-1])
                        example={'labels':tau,'fixed_obstruction_column':j,
                                 'nonzero_rhs':rhs[:,j-1].tolist()}
            assert group_pass in (0,384)
            branch_records.append({'compact_matrix':A.tolist(),
                                   'fixed_label_targets':list(fperm),
                                   'compatible':branch_ok,
                                   'tested_pair_markings':384,
                                   'passing_pair_markings':group_pass,
                                   'example':example})
    assert (tested,passing)==expected[n][1:]
    records.append({'n':n,'fixed_labels':fixed,'paired_orbits':pairs,
                    'fixed_components':len(component_assignments),
                    'component_assignments_sixths':component_assignments,
                    'relative_homology_dimension':n+1,
                    'tested_period_label_cases':tested,
                    'compatible_cases':passing,
                    'incompatible_cases':tested-passing,
                    'branch_records':branch_records})
    print('PASS n=',n,'components=',len(component_assignments),
          'all period/label cases=',tested,'compatible=',passing,
          'incompatible=',tested-passing,flush=True)

# The same relative action retains all finite period residues required for
# the Γ(6) split subgroup. The following is an actual generated subgroup.
I=(1,0,0,1);U=(1,1,0,1);L=(1,0,5,1)
def mul(a,b):return tuple(sum(a[2*i+l]*b[2*l+j] for l in range(2))%6
                          for i in range(2) for j in range(2))
states=[I];seen={I}
for a in states:
    for b in (U,L):
        c=mul(a,b)
        if c not in seen:seen.add(c);states.append(c)
assert len(states)==144
assert len({tuple(v%2 for v in a) for a in states})==6
assert len({tuple(v%3 for v in a) for a in states})==24
print('PASS actual SL2(Z/6) image has order144 and the two CRT projections6,24.',flush=True)
data={'scope':'Exact finite component and relative-homology marking certificate; no gentle-shadow census',
      'all_assertions_passed':True,'source':'literal E[3] and selected E[2] points in T[6]',
      'total_period_label_cases':sum(r['tested_period_label_cases'] for r in records),
      'records':records,'SL2_mod6_order':144,'SL2_mod6_matrices':states,
      'independent_pair_signs':signs}
HERE.joinpath('check_involution_configuration_labels.json').write_text(json.dumps(data,indent=2)+'\n')
np.savez_compressed(HERE/'check_involution_configuration_labels.npz',**arrays)
print('PASS all76032 cases; actual branch-affine condition is exactly the finite relative-homology constraint.',flush=True)
