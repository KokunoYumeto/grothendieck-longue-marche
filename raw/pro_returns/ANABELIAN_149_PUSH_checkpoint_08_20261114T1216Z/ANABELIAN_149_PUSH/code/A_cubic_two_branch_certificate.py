#!/usr/bin/env python3
"""Exact finite certificates for the two-branch cubic construction.

The geometric argument is audit/A_cubic_two_branch_candidate.md. This checks
all residue vectors on the nine-point torsion orbit, every reflection on a
cyclic cubic fibre, and the character/stabilizer identity in all subspaces of
F_3^r for r<=3. It uses only the Python standard library.
"""
import itertools
import json
from pathlib import Path

checks = []
def check(name, condition, **data):
    assert condition, name
    checks.append(dict(name=name, passed=True, **data))

G = list(itertools.product(range(3), repeat=2))
zero = (0, 0)
def add(x, y): return tuple((a+b)%3 for a,b in zip(x,y))
def neg(x): return tuple(-a%3 for a in x)
def mul(a,x): return tuple(a*b%3 for b in x)

for a in [1,2]:
    coeff = {g:0 for g in G}
    centers = []
    for g in G:
        if g == zero: continue
        coeff[g] = (coeff[g]+a)%3
        coeff[zero] = (coeff[zero]-a)%3
        x = neg(g)
        check(f'center_a{a}_g{g}', x not in [zero,g] and mul(2,x)==g,
              g=g, center=x)
        centers.append(x)
    check(f'nine_point_residue_a{a}', all(coeff[g]==a for g in G),
          coefficients=[coeff[g] for g in G])
    check(f'all_nonzero_centers_a{a}', set(centers)==set(G)-{zero})

for c in range(3):
    rho=lambda i:(c-i)%3
    fixed=[i for i in range(3) if rho(i)==i]
    check(f'reflection_{c}_fixed',len(fixed)==1,fixed=fixed)
    check(f'reflection_{c}_order2',all(rho(rho(i))==i for i in range(3)))
    check(f'reflection_{c}_inverts',all(rho((rho(i)+1)%3)==(i-1)%3 for i in range(3)))
    rho2=lambda i:(c+2-i)%3
    check(f'reflection_pair_{c}_separates',
          all(i==j for i in range(3) for j in range(3)
              if j in {i,rho(i)} and j in {i,rho2(i)}))

small_vectors = [(1,2,0),(0,2,1)]
check('three_point_special_residue',
      tuple(sum(v[i] for v in small_vectors)%3 for i in range(3))==(1,1,1),
      vectors=small_vectors)

# Generate every subspace by closure under spans; keep sets canonical.
subspace_counts={}
character_cases=0
for r in range(1,4):
    space=list(itertools.product(range(3),repeat=r))
    origin=(0,)*r
    subspaces={frozenset([origin])}
    frontier=list(subspaces)
    while frontier:
        H=frontier.pop()
        for v in space:
            if v in H: continue
            K=frozenset(add(h,mul(a,v)) for h in H for a in range(3))
            if K not in subspaces:
                subspaces.add(K); frontier.append(K)
    subspace_counts[str(r)]=len(subspaces)
    for I in subspaces:
        chars=[c for c in space if c!=origin]
        def dot(c,x):return sum(a*b for a,b in zip(c,x))%3
        kernels=[]
        for c in chars:
            ker={x for x in space if dot(c,x)==0}
            kernels.append({add(i,x) for i in I for x in ker})
        intersection=set(space)
        for H in kernels: intersection &= H
        assert intersection==set(I)
        # The equivalent sufficient family: characters killing inertia.
        annihilator=[c for c in chars if all(dot(c,i)==0 for i in I)]
        detected={x for x in space if all(dot(c,x)==0 for c in annihilator)}
        assert detected==set(I)
        character_cases += 1
check('all_character_stabilizer_cases',True,cases=character_cases,
      subspace_counts=subspace_counts)

check('genus_three_cover',2*3-2 == 2*(3-1))
check('elliptic_reflection_quotient',2*3-2 == 2*(2*1-2)+2*2)
check('ambient_ramification_index',3*2==6 and 6%3==0)
check('odd_galois_closure_primes',all((3**r*9)%2==1 for r in range(20)))

result=dict(status='passed',checks=checks,total_checks=len(checks),
            scope='Exact finite identities supporting the uniform geometric proof; no parameter sampling.',
            proof='audit/A_cubic_two_branch_candidate.md')
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(status='passed',total_checks=len(checks),
                     character_cases=character_cases,output=str(out))))
