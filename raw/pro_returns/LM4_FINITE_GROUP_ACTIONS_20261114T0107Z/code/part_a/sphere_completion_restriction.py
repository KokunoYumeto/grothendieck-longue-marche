#!/usr/bin/env python3
"""Finite certificates for D.31; no finite search replaces its profinite proof."""
from itertools import permutations, product
from pathlib import Path
from collections import deque
import json


def matrix_group(p, special=False):
    def normalize(a):
        k=next(x for x in a if x)
        return tuple(x*pow(k,-1,p)%p for x in a)
    def mul(a,b):
        A,B,C,D=a; E,F,G,H=b
        return normalize(((A*E+B*G)%p,(A*F+B*H)%p,
                          (C*E+D*G)%p,(C*F+D*H)%p))
    def inv(a):
        A,B,C,D=a
        return normalize((D,(-B)%p,(-C)%p,A))
    squares={a*a%p for a in range(1,p)}
    group=set()
    for a in product(range(p),repeat=4):
        det=(a[0]*a[3]-a[1]*a[2])%p
        if det and (not special or det in squares):group.add(normalize(a))
    return group,mul,inv,normalize


rows=[]
psl5=None
for p in (3,5,7,11,13):
    for special in (True,False):
        G,mul,inv,norm=matrix_group(p,special)
        one=(1,0,0,1)
        U={norm((1,t,0,1)) for t in range(p)}
        u=norm((1,1,0,1))
        N={g for g in G if mul(mul(g,u),inv(g)) in U}
        powers={norm((1,t,0,1)):t for t in range(p)}
        automizers={powers[mul(mul(g,u),inv(g))] for g in N}
        expected={a*a%p for a in range(1,p)} if special else set(range(1,p))
        assert automizers==expected
        assert len(G)==p*(p*p-1)//(2 if special else 1)
        assert len(N)==p*len(expected)
        rows.append({'group':('PSL2' if special else 'PGL2')+f'(F{p})',
                     'order':len(G),'unipotent_subgroup_order':p,
                     'normalizer_order':len(N),'automizer_exponents':sorted(automizers),
                     'automizer_order':len(automizers),
                     'passes_order_at_most_two':len(automizers)<=2})
        if p==5 and special:
            invol=[g for g in G if g!=one and mul(g,g)==one]
            fourgroups=set()
            for a,b in product(invol,repeat=2):
                if a!=b and mul(a,b)==mul(b,a):
                    fourgroups.add(frozenset((one,a,b,mul(a,b))))
            fourgroups=sorted(fourgroups,key=lambda V:sorted(V))
            assert len(invol)==15 and len(fourgroups)==5
            index={V:i for i,V in enumerate(fourgroups)}
            def action(g):
                return tuple(index[frozenset(mul(mul(g,h),inv(g)) for h in V)]
                             for V in fourgroups)
            image={action(g) for g in G}
            assert len(image)==60
            assert all(sum(a[i]>a[j] for i in range(5) for j in range(i+1,5))%2==0
                       for a in image)
            psl5={'map':'conjugation on the five Sylow 2-subgroups, indexed by lexicographic order',
                  'sylow2_subgroups':[[list(a) for a in sorted(V)] for V in fourgroups],
                  'image_order':len(image),'kernel_order':len(G)//len(image),
                  'all_image_permutations_even':True,
                  'upper_unipotent_generator_image_0_based':list(action(u)),
                  'weyl_generator_image_0_based':list(action(norm((0,4,1,0))))}


def perm_mul(a,b):return tuple(a[b[i]] for i in range(len(a)))
def perm_inv(a):return tuple(a.index(i) for i in range(len(a)))
def cycle(n,*entries):
    a=list(range(n))
    for i,j in zip(entries,entries[1:]+entries[:1]):a[i-1]=j-1
    return tuple(a)
def parity(a):return sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))%2
def generate(gens,n):
    one=tuple(range(n));out={one};q=deque([one])
    while q:
        a=q.popleft()
        for b in gens:
            c=perm_mul(a,b)
            if c not in out:out.add(c);q.append(c)
    return out

S5=set(permutations(range(5)));A5={a for a in S5 if not parity(a)}
c=cycle(5,1,2,3,4,5);C5=generate([c],5)
cyc=[tuple(range(5))]
for _ in range(4):cyc.append(perm_mul(cyc[-1],c))
five_rows=[]
for name,G in [('A5',A5),('S5',S5)]:
    N={g for g in G if perm_mul(perm_mul(g,c),perm_inv(g)) in C5}
    exponents={cyc.index(perm_mul(perm_mul(g,c),perm_inv(g))) for g in N}
    five_rows.append({'group':name,'order':len(G),'normalizer_C5_order':len(N),
                      'automizer_exponents':sorted(exponents)})
assert five_rows[0]['automizer_exponents']==[1,4]
assert five_rows[1]['automizer_exponents']==[1,2,3,4]

orbit_rows=[]
for d,c in [(2,perm_mul(cycle(5,1,2),cycle(5,3,4))),
            (3,cycle(5,1,2,3)),(5,cycle(5,1,2,3,4,5))]:
    D=generate([c],5)
    cosets=set(frozenset(perm_mul(g,h) for h in D) for g in A5)
    fixed=sum(frozenset(perm_mul(c,h) for h in coset)==coset for coset in cosets)
    assert fixed==2
    orbit_rows.append({'point_stabilizer_order':d,'orbit_size':len(cosets),
                       'fixed_points_of_generator':fixed,'maximum_multiplicity':1})

A7_elementary=generate([cycle(7,1,2,3),cycle(7,4,5,6)],7)
assert len(A7_elementary)==9 and all(not parity(a) for a in A7_elementary)
assert all(perm_mul(perm_mul(a,a),a)==tuple(range(7)) for a in A7_elementary)

out={'projective_matrix_automizers':rows,'PSL2_F5_to_A5':psl5,
     'A5_S5_order5_automizers':five_rows,
     'icosahedral_permutation_orbits':orbit_rows,
     'free_orbit_size':60,
     'A7_contains_elementary_abelian_C3_squared':{'order':len(A7_elementary),
         'generators_0_based':[list(cycle(7,1,2,3)),list(cycle(7,4,5,6))]},
     'scope':'Finite certificates for the eliminations and exact PSL2(F5)-to-A5 map. The completed braid transfer and all-prime group restriction are proved in D.31.'}
Path(__file__).with_name('sphere_completion_restriction_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
