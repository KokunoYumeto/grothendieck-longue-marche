"""Independent character-kernel verifier, without importing the producer.

This implementation uses subgroup generation by all pairs and the exact
character-sum identity for norms. It exhausts support patterns, weighting
each pattern by its number of vectors, rather than repeating field norms.
"""
from itertools import product
from pathlib import Path
import json

def subgroup_lattice(n,m):
    A=tuple(product(range(n),range(m)))
    groups=set()
    for x in A:
        for y in A:
            groups.add(frozenset(((i*x[0]+j*y[0])%n,
                                  (i*x[1]+j*y[1])%m)
                                 for i in range(n*m) for j in range(n*m)))
    return A,sorted(groups,key=lambda H:(len(H),sorted(H)))

def kernels(A,spec):
    return [frozenset((a,b) for a,b in A if (r*a+s*b)%d==0)
            for d,r,s,q in spec]

def norm_free(A,H,active):
    # The character norm is nonzero precisely for characters trivial on H.
    retained=[K for K in active if H<=K]
    stab=set(A)
    for K in retained:stab.intersection_update(K)
    return stab==set(H)

A,L=subgroup_lattice(9,3)
small=[(3,1,0,4),(3,0,1,4),(3,1,1,4),(3,1,2,4)]
large=small+[(9,1,3*j,64) for j in range(3)]
def weighted_count(spec,conditions):
    K=kernels(A,spec);answer=0;good=[]
    for support in product((0,1),repeat=len(spec)):
        active=[k for k,b in zip(K,support) if b]
        if all(norm_free(A,H,active) for H in conditions):
            weight=1
            for b,(_,_,_,q) in zip(support,spec):
                if b:weight*=q-1
            answer+=weight;good.append(support)
    return answer,good

prime=[H for H in L if len(A)//len(H)==3]
a,patterns_a=weighted_count(small,prime)
b,patterns_b=weighted_count(small,L)
c,patterns_c=weighted_count(large,L)
assert (len(L),a,b,c)==(10,81,0,20253807)
assert patterns_a==[(1,1,1,1)] and patterns_c==[(1,)*7]

B,LB=subgroup_lattice(3,3);KB=kernels(B,small)
# An invariant has u=v, arbitrary w, and z^2=z in F4, so z is0 or1.
invariants=[(u,u,w,z) for u in range(4) for w in range(4) for z in (0,1)]
good=[v for v in invariants
      if all(norm_free(B,H,[K for K,x in zip(KB,v) if x]) for H in LB)]
assert (len(LB),len(invariants),len(good))==(6,32,9)
result={'verified':True,'method':'Independent pair-generated subgroup lattices and weighted character-support enumeration',
        'constant_prime_quotient_free':a,'constant_all_quotient_free':b,
        'repaired_all_quotient_free':c,'semilinear_fixed':len(invariants),
        'semilinear_all_quotient_free':len(good)}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
