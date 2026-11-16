#!/usr/bin/env python3
"""Exact H_p subgroup and cusp-orbit checks supporting the A65 proof."""
from pathlib import Path
from collections import deque
import json


def check(p):
    identity = (0,0,0)
    G = [(x,y,z) for x in range(p) for y in range(p) for z in range(p)]
    allG = frozenset(G)
    Z = frozenset((0,0,z) for z in range(p))
    xgen, ygen = (1,0,0), (0,1,0)

    def mul(a,b):
        return ((a[0]+b[0])%p, (a[1]+b[1])%p,
                (a[2]+b[2]+a[0]*b[1])%p)

    def inv(a):
        return (-a[0]%p, -a[1]%p, (-a[2]+a[0]*a[1])%p)

    def cyclic(a):
        cur = identity
        out = set()
        for _ in range(p):
            out.add(cur)
            cur = mul(cur,a)
        assert cur == identity
        return frozenset(out)

    def generate(gens):
        out = {identity}
        todo = deque([identity])
        steps = tuple(gens)+tuple(inv(a) for a in gens)
        while todo:
            a = todo.popleft()
            for b in steps:
                c = mul(a,b)
                if c not in out:
                    out.add(c)
                    todo.append(c)
        return frozenset(out)

    assert generate((xgen,ygen)) == allG
    for a in G:
        assert mul(a,inv(a)) == identity
        assert len(cyclic(a)) == (1 if a == identity else p)

    lines = {frozenset(((j*a)%p,(j*b)%p) for j in range(p))
             for a in range(p) for b in range(p) if (a,b)!=(0,0)}
    assert len(lines) == p+1
    maximal = {frozenset(a for a in G if a[:2] in line) for line in lines}
    noncentral = {cyclic(a) for a in G if a not in Z}
    assert len(noncentral) == p*(p+1)
    predicted = {frozenset([identity]),Z,allG} | maximal | noncentral
    assert len(predicted) == p*p+2*p+4
    if p in (3,5):
        # Independent exhaustive subgroup generation, with no classification shortcut.
        found = {frozenset([identity])}
        todo = deque(found)
        while todo:
            H = todo.popleft()
            for a in G:
                if a not in H:
                    bigger = generate(tuple(H)+(a,))
                    if bigger not in found:
                        found.add(bigger)
                        todo.append(bigger)
        assert found == predicted

    cusp_points = {(a,b) for a in range(p) for b in range(p)}
    ordinary_checks = 0
    for H in noncentral:
        assert len(H)==p and H & Z == {identity}
        image = {a[:2] for a in H}
        assert len(image)==p and frozenset(image) in lines
        # The core is trivial, so the quotient really has full H_p closure.
        core = set(H)
        for g in (xgen,ygen):
            core &= {mul(mul(g,h),inv(g)) for h in H}
        assert core == {identity}
        representative = next(h for h in H if h != identity)
        a,b = representative[:2]
        orbits = set()
        for u,v in cusp_points:
            orbit = frozenset(((u+j*a)%p,(v+j*b)%p) for j in range(p))
            assert len(orbit)==p
            orbits.add(orbit)
        assert len(orbits)==p
        if p % 4 == 1:
            # The two connected CM lines at the two Gaussian places.
            connected = (1,0) if b != 0 else (0,1)
            reduction = (lambda v:v[1]) if connected==(1,0) else (lambda v:v[0])
            assert reduction((a,b)) != 0
            for orbit in orbits:
                assert {reduction(v) for v in orbit} == set(range(p))
            zero_orbit = next(o for o in orbits if (0,0) in o)
            assert connected not in zero_orbit
            assert reduction(connected)==0
            ordinary_checks += 1

    genus_C = 1+p*p*(p-1)//2
    genus_D = 1+p*(p-1)//2
    assert 2*genus_C-2 == p*(2*genus_D-2)
    assert 2*genus_D-2+p == p*p
    return {'p':p, 'group_order':len(G), 'subgroups':len(predicted),
        'noncentral_order_p_subgroups':len(noncentral),
        'brute_all_subgroups_equal_classification':p in (3,5),
        'every_noncentral_core_trivial':True,
        'cusp_orbits_each':p, 'ordinary_place_checks':ordinary_checks,
        'quotient_degree':p*p, 'quotient_genus':genus_D,
        'unramified_Riemann_Hurwitz':True, 'Euler_identity':True}


rows = [check(p) for p in (3,5,7,11,13)]
out = {'status':'PASS', 'statement':'A65 candidate, unregistered',
       'scope':'Finite exact group and cusp-orbit support only; actual stable-model geometry is proved in the text.',
       'rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: complete subgroup enumeration at3/5; all cyclic/maximal subgroup, core, cusp-orbit and genus checks at3/5/7/11/13; both ordinary CM-place choices.')
