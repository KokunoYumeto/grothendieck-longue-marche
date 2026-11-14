#!/usr/bin/env python3
"""Exact finite checks for the modular-level unit-rank route audit.

The p-adic and arithmetic arguments are proved in the accompanying audit.
This file checks the finite matrix calculation, not a section conjecture.
Only the Python standard library is used.
"""
from collections import deque
from fractions import Fraction
from pathlib import Path
import json


def mul(a, b, n):
    return ((a[0]*b[0]+a[1]*b[2]) % n,
            (a[0]*b[1]+a[1]*b[3]) % n,
            (a[2]*b[0]+a[3]*b[2]) % n,
            (a[2]*b[1]+a[3]*b[3]) % n)


def inv(a, n):
    q = pow((a[0]*a[3]-a[1]*a[2]) % n, -1, n)
    return (q*a[3] % n, -q*a[1] % n,
            -q*a[2] % n, q*a[0] % n)


def subgroup(gens, n):
    identity = (1, 0, 0, 1)
    seen = {identity}
    todo = deque([identity])
    while todo:
        a = todo.popleft()
        for b in gens:
            c = mul(a, b, n)
            if c not in seen:
                seen.add(c)
                todo.append(c)
    return seen


def cosets_and_orbits(group, inertia, gens, n):
    # Left cosets; arithmetic action in the audit is right multiplication.
    remaining = set(group)
    cosets, index = [], {}
    while remaining:
        g = min(remaining)
        coset = {mul(h, g, n) for h in inertia}
        i = len(cosets)
        for h in coset:
            index[h] = i
        cosets.append(coset)
        remaining.difference_update(coset)
    remaining_i = set(range(len(cosets)))
    sizes = []
    while remaining_i:
        start = min(remaining_i)
        seen, todo = {start}, deque([start])
        while todo:
            i = todo.popleft()
            g = min(cosets[i])
            for a in gens:
                j = index[mul(g, a, n)]
                if j not in seen:
                    seen.add(j)
                    todo.append(j)
        remaining_i.difference_update(seen)
        sizes.append(len(seen))
    return len(cosets), sizes


def qmul(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def main():
    n = 5
    identity = (1, 0, 0, 1)
    negidentity = (4, 0, 0, 4)
    a = (1, 2, 0, 1)
    b = (1, 0, 3, 1)
    c = inv(mul(a, b, n), n)
    group = subgroup([a, b], n)
    all_sl = {(i, j, k, l) for i in range(n) for j in range(n)
              for k in range(n) for l in range(n)
              if (i*l-j*k) % n == 1}
    assert group == all_sl and len(group) == 120
    assert c == (1, 3, 2, 2)
    rows = {}
    for label, generator in [('0', a), ('1', b), ('infinity', c)]:
        inertia = subgroup([generator], n)
        count, orbit_sizes = cosets_and_orbits(group, inertia, [a, b], n)
        projective_inertia = subgroup([generator, negidentity], n)
        pc, po = cosets_and_orbits(group, projective_inertia, [a, b], n)
        rows[label] = dict(inertia_order=len(inertia),
                           full_cusps=count, arithmetic_orbit_sizes=orbit_sizes,
                           projective_cusps=pc, projective_orbit_sizes=po)
    assert [rows[x]['inertia_order'] for x in rows] == [5, 5, 10]
    assert [rows[x]['full_cusps'] for x in rows] == [24, 24, 12]
    assert all(len(v['arithmetic_orbit_sizes']) == 1 for v in rows.values())
    assert all(v['projective_cusps'] == 12 and v['projective_orbit_sizes'] == [12]
               for v in rows.values())

    affine_points = [(x, y) for x in range(7) for y in range(7)
                     if (y*y-x*(x-1)*(x-3)) % 7 == 0]
    assert affine_points == [(0, 0), (1, 0), (3, 0)]
    trace = 8-(len(affine_points)+1)
    assert trace == 4
    discriminant_mod5 = (trace*trace-4*7) % 5
    assert discriminant_mod5 == 3
    assert discriminant_mod5 not in {x*x % 5 for x in range(5)}
    frob = (0, 3, 1, 4)  # reduction of [[0,-7],[1,4]]
    gl = subgroup([(1, 1, 0, 1), frob], 5)
    assert len(gl) == 480
    assert {((g[0]*g[3]-g[1]*g[2]) % 5) for g in gl} == {1, 2, 3, 4}

    gq = tuple(map(Fraction, (0, -7, 1, 4)))
    iq = (Fraction(4, 7), Fraction(1), Fraction(-1, 7), Fraction(0))
    e12 = tuple(map(Fraction, (0, 1, 0, 0)))
    conjugate = qmul(qmul(gq, e12), iq)
    assert conjugate == (0, 0, Fraction(-1, 7), 0)
    assert qmul(gq, iq) == identity

    level_counts = []
    for exponent in (1, 2, 3, 4):
        level = 5**exponent
        sl_order = 24 * 5**(3*exponent-2)
        full = [sl_order//level, sl_order//level, sl_order//(2*level)]
        projective = [sl_order//(2*level)]*3
        level_counts.append(dict(level=level, degree=sl_order,
                                 geometric_cusps_by_label=full,
                                 geometric_projective_cusps_by_label=projective,
                                 full_genus=1+(sl_order-sum(full))//2,
                                 projective_genus=1+(sl_order//2-sum(projective))//2,
                                 rational_cusp_orbits=3, rational_unit_rank=2))
    assert level_counts[0]['full_genus'] == 31
    assert level_counts[0]['projective_genus'] == 13

    result = dict(status='PASS', scope='Finite matrix and point-count checks only; '
                  'the all-level Galois and unit proofs are in the audit.',
                  legendre_E3=dict(discriminant=576, c4=112,
                                  v3_discriminant=2, v3_c4=0,
                                  kodaira_at_3='I_2',
                                  affine_points_mod7=affine_points,
                                  points_mod7=4, frobenius_trace7=trace,
                                  discriminant_mod5=discriminant_mod5,
                                  generated_GL2_mod5_order=len(gl)),
                  SL2_mod5_order=len(group), cusp_fibres=rows,
                  frobenius_conjugation_E12=[str(x) for x in conjugate],
                  levels=level_counts)
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', output=str(path),
                          SL2_order=len(group), GL2_order=len(gl),
                          cusp_orbits=3, rational_unit_rank=2)))


if __name__ == '__main__':
    main()
