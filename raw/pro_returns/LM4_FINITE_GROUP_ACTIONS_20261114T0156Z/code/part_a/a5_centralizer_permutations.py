#!/usr/bin/env python3
"""Exact puncture-permutation restrictions for the A5 centralizer audit."""
from itertools import permutations
from collections import deque
from pathlib import Path
import json


one=tuple(range(5))
def mul(a,b):return tuple(a[b[i]] for i in range(5))
def inv(a):return tuple(a.index(i) for i in range(5))
def parity(a):return sum(a[i]>a[j] for i in range(5) for j in range(i+1,5)) % 2
def generated(gens):
    out={one};queue=deque([one])
    while queue:
        a=queue.popleft()
        for b in gens:
            c=mul(a,b)
            if c not in out:out.add(c);queue.append(c)
    return out
def cycle(*entries):
    p=list(range(5))
    for i,j in zip(entries,entries[1:]+entries[:1]):p[i-1]=j-1
    return tuple(p)


G=set(p for p in permutations(range(5)) if parity(p)==0)
a=mul(cycle(1,2),cycle(3,4))
b=cycle(1,3,5)
assert generated([a,b])==G
A4={g for g in G if g[4]==4}
assert len(A4)==12 and a in A4
rows=[]
for d,c in [(2,a),(3,cycle(1,2,3)),(5,cycle(1,2,3,4,5))]:
    K=generated([c]);assert len(K)==d
    cosets=sorted(set(frozenset(mul(g,k) for k in K) for g in G),key=lambda C:min(C))
    index={v:i for i,C in enumerate(cosets) for v in C}
    N={g for g in G if {mul(mul(g,k),inv(g)) for k in K}==K}
    commuting=[]
    for n in N:
        perm=tuple(index[mul(min(C),n)] for C in cosets)
        if perm not in commuting:commuting.append(perm)
    assert len(commuting)==2 and len(N)==2*d
    for perm in commuting:
        for g in G:
            action=tuple(index[mul(g,min(C))] for C in cosets)
            assert all(perm[action[i]]==action[perm[i]] for i in range(len(cosets)))
    if d==2:
        # Every A4-ramification point is fixed by the oriented A4 centralizer.
        forced=[i for i,C in enumerate(cosets)
                if any(g!=one and index[mul(g,min(C))]==i for g in A4)]
        reason='ramification points for the solvable tetrahedral subgroup A4'
    else:
        forced=[i for i,C in enumerate(cosets) if index[mul(c,min(C))]==i]
        reason='the two poles of the odd-order rotation'
    allowed=[perm for perm in commuting if all(perm[i]==i for i in forced)]
    assert len(allowed)==1 and allowed[0]==tuple(range(len(cosets)))
    rows.append({'stabilizer_order':d,'orbit_size':len(cosets),
        'normalizer_order_in_A5':len(N),'raw_commutant_order':len(commuting),
        'forced_fixed_punctures':len(forced),'reason':reason,
        'remaining_commutant_order':len(allowed)})

K5=generated([cycle(1,2,3,4,5)])
vertices=sorted(set(frozenset(mul(g,k) for k in K5) for g in G),key=lambda C:min(C))
vertex_index={v:i for i,C in enumerate(vertices) for v in C}
def vertex_action(g):return tuple(vertex_index[mul(g,min(C))] for C in vertices)
assert len({vertex_action(g)[0] for g in A4})==12
five_subgroups={frozenset(generated([g])) for g in G
                if g!=one and len(generated([g]))==5}
assert len(five_subgroups)==6
six_point_sets=set()
seven_point_sets=set()
six_records=[]
for K in sorted(five_subgroups,key=lambda K:sorted(K)):
    generator=min(K-{one});perm=vertex_action(generator)
    remaining=set(range(12));cycles=[]
    while remaining:
        start=min(remaining);orbit=[];i=start
        while i not in orbit:orbit.append(i);i=perm[i]
        cycles.append(orbit);remaining.difference_update(orbit)
    poles=[C[0] for C in cycles if len(C)==1]
    long=[C for C in cycles if len(C)==5]
    assert len(poles)==2 and len(long)==2
    for orbit in long:seven_point_sets.add(frozenset(poles+orbit))
    for pole in poles:
        for orbit in long:
            I=frozenset([pole]+orbit)
            six_point_sets.add(I)
            labels=sorted(I);local=tuple(labels.index(perm[i]) for i in labels)
            commutant=[q for q in permutations(range(6))
                       if all(q[local[i]]==local[q[i]] for i in range(6))]
            assert len(commutant)==5
            six_records.append({'C5_generator':list(generator),'retained_vertices':labels,
                                'restriction_cycle_lengths':[1,5],
                                'finite_permutation_commutant_order':len(commutant)})
assert len(six_point_sets)==24
unseen=set(six_point_sets);orbit_sizes=[]
while unseen:
    I=min(unseen,key=lambda S:sorted(S))
    orbit={frozenset(vertex_action(g)[i] for i in I) for g in G}
    assert orbit<=six_point_sets
    orbit_sizes.append(len(orbit));unseen.difference_update(orbit)
assert sorted(orbit_sizes)==[12,12]

# Label the orbit by A4: a vertex is g(v0).  Collisions at a fixed point
# of H<=A4 are RIGHT cosets gH, not the left A4 permutation orbits.
assert len(seven_point_sets)==12
group_labels={vertex_action(g)[0]:g for g in A4}
label_vertices={g:i for i,g in group_labels.items()}
cyclic_subgroups=sorted({frozenset(generated([g])) for g in A4 if g!=one},
                       key=lambda H:(len(H),sorted(H)))
assert [len(H) for H in cyclic_subgroups]==[2,2,2,3,3,3,3]
partitions=[]
for H in cyclic_subgroups:
    partitions.append(set(frozenset(label_vertices[mul(g,h)] for h in H) for g in A4))
collision_six=[]
for I in sorted(six_point_sets,key=lambda I:sorted(I)):
    missing=[j for j,partition in enumerate(partitions)
             if all(len(I&C)<=1 for C in partition)]
    assert len(missing)==1 and len(cyclic_subgroups[missing[0]])==2
    collision_six.append(missing[0])
assert len(set(collision_six))==1
common_missing=collision_six[0]
antipodal_h=next(g for g in cyclic_subgroups[common_missing] if g!=one)
antipodal=tuple(label_vertices[mul(group_labels[i],antipodal_h)] for i in range(12))
assert all(antipodal[antipodal[i]]==i and antipodal[i]!=i for i in range(12))
assert all(all(antipodal[vertex_action(g)[i]]==vertex_action(g)[antipodal[i]]
               for i in range(12)) for g in G)
assert all(all(any(len(I&C)>=2 for C in partition) for partition in partitions)
           for I in seven_point_sets)

def rref(rows,p=101):
    rows=[list(x) for x in rows];piv=[];r=0
    if not rows:return [],[]
    for c in range(len(rows[0])):
        j=next((j for j in range(r,len(rows)) if rows[j][c]%p),None)
        if j is None:continue
        rows[r],rows[j]=rows[j],rows[r]
        u=pow(rows[r][c]%p,-1,p);rows[r]=[x*u%p for x in rows[r]]
        for j in range(len(rows)):
            if j!=r and rows[j][c]%p:
                u=rows[j][c]%p
                rows[j]=[(a-u*b)%p for a,b in zip(rows[j],rows[r])]
        piv.append(c);r+=1
        if r==len(rows):break
    return rows[:r],piv

def peripheral_homology_matrix(subsets,p=101):
    matrix=[];individual=[]
    for I in sorted(subsets,key=lambda I:sorted(I)):
        I=sorted(I);edges=[(i,j) for i in I for j in I if i<j]
        relations=[[int(i in edge) for edge in edges] for i in I]
        relations.append([1]*len(edges))
        rel,piv=rref(relations,p);free=[i for i in range(len(edges)) if i not in piv]
        columns=[]
        for partition in partitions:
            v=[int(any(i in C and j in C for C in partition)) for i,j in edges]
            for row,c in zip(rel,piv):
                u=v[c];v=[(a-u*b)%p for a,b in zip(v,row)]
            # The two fixed points of H give the same homology column.
            columns.extend([[v[c] for c in free]]*2)
        # Omit the fourteenth peripheral generator; the sole source relation
        # is the product of all fourteen peripherals.
        columns=columns[:13]
        local=[list(row) for row in zip(*columns)]
        individual.append(len(rref(local,p)[1]));matrix.extend(local)
    return {'coefficient_prime':p,'source_H1_dimension':13,
            'individual_map_ranks':individual,'joint_rank':len(rref(matrix,p)[1]),
            'joint_kernel_dimension':13-len(rref(matrix,p)[1])}

six_homology=peripheral_homology_matrix(six_point_sets)
seven_homology=peripheral_homology_matrix(seven_point_sets)
assert six_homology['joint_rank']==5
assert seven_homology['joint_rank']==6

out={'A5_order':len(G),'displayed_order2_order3_pair_generates_A5':True,
     'exceptional_orbit_checks':rows,
     'free_orbit_formula':'For m free A5-orbits, the realized puncture commutant is A5^m semidirect S_m.',
     'minimal_twelve_puncture_reduction':{
         'A4_action_on_twelve_vertices_is_regular':True,
         'A4_quotient_free_punctures':1,'A4_quotient_branch_points':3,
         'discrete_A4_centralizer_rank':2,'pure_A4_centralizer_index':12,
         'pure_A4_centralizer_rank_by_Schreier':13,
         'number_of_C5_subgroups':len(five_subgroups),
         'six_point_forgetting_subsets':len(six_point_sets),
         'A5_orbit_sizes_of_subsets':sorted(orbit_sizes),
         'six_point_records':six_records,
         'proved_constraint':'The completed A5 centralizer lies in the embedded Fhat13 pure A4 centralizer and in all24 six-point and all12 seven-point forgetting kernels.',
         'six_point_maps_proved_noninjective':True,
         'common_invisible_order2_ramification_stabilizer':list(antipodal_h),
         'right_multiplication_is_A5_equivariant_antipodal_involution':list(antipodal),
         'common_invisible_ramification_points':2,
         'nontrivial_joint_kernel':'Each peripheral meridian of these two ramification points maps trivially under all24 six-point configuration maps, which extend across these points.',
         'seven_point_forgetting_subsets':[sorted(I) for I in sorted(seven_point_sets,key=lambda I:sorted(I))],
         'seven_point_maps_retain_collisions_at_all_fourteen_ramification_points':True,
         'six_point_abelian_quotient_check':six_homology,
         'seven_point_abelian_quotient_check':seven_homology,
         'unsettled_map':'Injectivity of the seven-point joint map on the embedded Fhat13 is not proved. Its induced H1 map over F101 has a seven-dimensional kernel.'},
     'scope':'This determines the finite puncture-permutation image. It does not prove the equality of full profinite and completed discrete centralizers.'}
Path(__file__).with_name('a5_centralizer_permutations_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
