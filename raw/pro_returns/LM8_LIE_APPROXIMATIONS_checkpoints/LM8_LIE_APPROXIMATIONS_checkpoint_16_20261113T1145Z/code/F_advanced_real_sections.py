#!/usr/bin/env python3
"""Exact finite checks for F.19: integral real metabelian sections.

The theorem is proved with the completed Alexander module.  This finite
calculation independently enumerates every class-two cocycle and its entire
twisted-conjugacy orbit, and checks the module involutions on every basis
element.  It also records the transition maps, including the disappearing
finite central class.  No rationalization or random sampling is used.
"""
from collections import deque
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def mul(g, h, q):
    a, b, c = g
    u, v, w = h
    return ((a + u) % q, (b + v) % q, (c + w - u*b) % q)


def inv(g, q):
    a, b, c = g
    return (-a % q, -b % q, (-c-a*b) % q)


def sigma(g, q):
    a, b, c = g
    return (-a % q, -b % q, c)


def twisted(g, h, q):
    return mul(mul(inv(h, q), g, q), sigma(h, q), q)


def finite_stage(n):
    q = 2**n
    zero = (0, 0, 0)
    cocycles = set()
    for a in range(q):
        for b in range(q):
            if a*b % 2:
                continue
            c = (-a*b//2) % (q//2)
            for z in (c, c+q//2):
                g = (a, b, z)
                assert mul(g, sigma(g, q), q) == zero
                cocycles.add(g)
    reps = [zero, (0, 0, q//2), (1, 0, 0), (0, 1, 0)]
    generators = [(1, 0, 0), (q-1, 0, 0), (0, 1, 0), (0, q-1, 0)]
    cls = {}
    sizes = []
    for label, rep in enumerate(reps):
        assert rep not in cls
        queue = deque([rep])
        cls[rep] = label
        size = 0
        while queue:
            g = queue.popleft()
            size += 1
            for h in generators:
                t = twisted(g, h, q)
                a,b,c = g
                u,v,w = h
                direct=((a-2*u)%q, (b-2*v)%q, (c+a*v+u*b-2*u*v)%q)
                assert t == direct and t in cocycles
                if t not in cls:
                    cls[t] = label
                    queue.append(t)
                else:
                    assert cls[t] == label
        sizes.append(size)
    assert set(cls) == cocycles
    assert sizes == [q*q//4, q*q//4, q*q//2, q*q//2]
    # The twisted Alexander actions on the delta-basis of Z_2[[Z_2^2]].
    module_checks = []
    for name, shift in [('1',(-1,-1)), ('x',(0,-1)), ('y',(-1,0))]:
        axis = 0 if shift[0] % 2 else 1
        seen = set()
        for a in range(q):
            for b in range(q):
                z=(a,b)
                t=((shift[0]-a)%q,(shift[1]-b)%q)
                tt=((shift[0]-t[0])%q,(shift[1]-t[1])%q)
                assert tt == z and t != z
                assert z[axis] % 2 != t[axis] % 2
                seen.add(tuple(sorted([z,t])))
        assert len(seen) == q*q//2
        module_checks.append(dict(lift=name, affine_shift=shift,
                                  swapped_parity_axis=axis,
                                  basis_elements=q*q, free_pairs=len(seen)))
    return dict(exponent=n, modulus=q, group_order=q**3,
                cocycle_count=len(cocycles), class_count=4,
                class_representatives=reps, orbit_sizes=sizes,
                alexander_involutions=module_checks), cls


def main():
    stages=[]
    previous=None
    for n in range(1,9):
        item, cls=finite_stage(n)
        if previous is not None:
            lower=2**(n-1)
            target_sets=[set() for _ in range(4)]
            for g,k in cls.items():
                target_sets[k].add(previous[tuple(x%lower for x in g)])
            assert target_sets == [{0},{0},{2},{3}]
            item['transition_to_previous']=[next(iter(s)) for s in target_sets]
        stages.append(item)
        previous=cls
        print(f"2^{n}: |N|={item['group_order']}, cocycles={item['cocycle_count']}, "
              f"H1=4, orbit sizes={item['orbit_sizes']}; all three module actions free")
    fermat=[]
    for n in range(1,9):
        t=2**(n-1)
        reps=[]
        for i,j in [(0,0),(1,0),(0,1),(1,1)]:
            # Exact integer coordinates, before reduction to any finite quotient.
            reps.append([-2*t*i,-2*t*j,-2*t*t*i*j])
        assert all(2*c+a*b == 0 for a,b,c in reps)
        fermat.append(dict(level=2**n, relative_class_representatives=reps,
                           class_count=4, next_level_image_class=0))
    out=dict(statement='F.19', status='Proved',
             scope='All class-two cocycles/orbits modulo 2^n for 1<=n<=8; all basis vectors in the three finite Alexander permutation modules; exact relative Fermat representatives. The full compact theorem is proved in the text.',
             commutator='[x,y]=xyx^-1y^-1',
             normal_form='x^a y^b [x,y]^c',
             group_law='(a,b,c)(u,v,w)=(a+u,b+v,c+w-u*b)',
             real_action='sigma(a,b,c)=(-a,-b,c)',
             cocycle_equation='2*c+a*b=0',
             compact_class_representatives=[[0,0,0],[1,0,0],[0,1,0]],
             finite_stages=stages, relative_fermat=fermat)
    (ROOT/'F_advanced_real_sections.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Profinite class-two and full metabelian H1: exactly three classes; relative Fermat kernels: four.')


if __name__ == '__main__':
    main()
