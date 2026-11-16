#!/usr/bin/env python3
"""Exact finite support for A64; the written proof supplies the actual models."""
from pathlib import Path
import json
import sympy as s


def valuation(n, p):
    a = 0
    while n % p == 0:
        a += 1
        n //= p
    return a, n


def prime_divisors(n):
    result = []
    r = 2
    while r * r <= n:
        if n % r == 0:
            result.append(r)
            while n % r == 0:
                n //= r
        r += 1
    if n > 1:
        result.append(n)
    return result


def elliptic_count(r):
    if r == 2:
        # The potential-good j=0 special model; geometric isomorphism is enough.
        return 1 + sum((y*y+y-x*x*x) % r == 0
                       for x in range(r) for y in range(r))
    return 1 + sum((y*y-x*x*x+x) % r == 0
                   for x in range(r) for y in range(r))


d, c, m, r0, g = s.symbols('d c m r0 g', positive=True, integer=True)
cluster_sum = r0+d*(c-1)+d*(m**2/c-1)*c
assert s.expand(cluster_sum-(r0+d*(m**2-1))) == 0
assert s.expand(cluster_sum.subs(r0, d-2*g+2)-(m**2*d-2*g+2)) == 0

elliptic_rows = []
for r in (2, 3, 5, 7, 11, 13, 17):
    count = elliptic_count(r)
    trace = r+1-count
    rank = int(trace % r != 0)
    assert rank == (0 if r == 2 or r % 4 == 3 else 1)
    elliptic_rows.append({'r': r, 'point_count': count,
                          'trace': trace, 'r_rank': rank})

# Abstract branch-index consistency checks; these are not realization claims.
branch_rows = []
for indices in ((1,), (1,1), (3,), (3,1,1), (5,3,1), (2,2), (2,2,2,2), (3,3,3)):
    degree = sum(indices)
    genus = 1+(degree-len(indices))//2
    assert 2*genus-2 == degree-len(indices)
    for residue in (2,3,5,7):
        if any(e % residue == 0 for e in indices):
            continue
        for exponent in (1,2):
            for rank in (0,1):
                for prime_to_part in (1,5 if residue != 5 else 7):
                    enlarge = residue**exponent*prime_to_part
                    size = residue**(exponent*(2-rank))
                    number = prime_to_part**2*residue**(exponent*rank)
                    assert size*number == enlarge**2 and size >= 2
                    ramified_sizes = [1+e*(size-1) for e in indices]
                    assert min(ramified_sizes) >= 2
                    total = sum(ramified_sizes)+degree*(number-1)*size
                    assert total == enlarge**2*degree-2*genus+2
                    branch_rows.append({'indices': indices, 'residue': residue,
                        'exponent': exponent, 'rank': rank, 'm': enlarge,
                        'target_cluster_size': size, 'target_clusters': number,
                        'source_origin_clusters': ramified_sizes, 'total': total})

# Actual Heisenberg degree and ramification data from A61/A62.
heisenberg_rows = []
for p in (3,5,7,11,13):
    degree = p**3
    genus = 1+p*p*(p-1)//2
    original_marks = p*p
    assert degree-original_marks == 2*genus-2
    for enlarge in sorted({2,3,4,5,6,7,9,11,13,2*p,3*p,4*p,p*p}):
        allowed = [r for r in prime_divisors(enlarge) if r != p]
        if not allowed:
            continue
        residue = allowed[0]
        exponent, prime_to_part = valuation(enlarge, residue)
        rank = 0 if residue == 2 or residue % 4 == 3 else 1
        size = residue**(exponent*(2-rank))
        number = prime_to_part**2*residue**(exponent*rank)
        one_origin_cluster = 1+p*(size-1)
        total = original_marks*one_origin_cluster+degree*(number-1)*size
        assert total == p**3*enlarge**2-p**3+p*p
        assert 2*genus-2+total == p**3*enlarge**2
        assert one_origin_cluster >= 2 and size >= 2
        assert degree % residue != 0
        heisenberg_rows.append({'p':p, 'm':enlarge, 'allowed_residue':residue,
            'rank':rank, 'cluster_size':size, 'target_clusters':number,
            'each_original_cusp_cluster':one_origin_cluster,
            'cusp_total':total, 'Euler_exact':True})

inert_rows = []
for p in (3,7,11,19):
    for exponent in range(4):
        enlarge = p**exponent
        target_torsion_order = p*enlarge
        count = p*p+p*(target_torsion_order**2-p*p)
        assert count == p**(2*exponent+3)-p**3+p*p
        assert count >= p*p >= 9
        inert_rows.append({'p':p, 'm':enlarge, 'special_target_points':1,
                           'marks':count, 'original_marks':p*p})

routes = {'outside_closure':0, 'ordinary_A63':0, 'inert_p_power':0}
for p in (3,5,7,11,13,19):
    for enlarge in range(1,101):
        if any(r != p for r in prime_divisors(enlarge)):
            routes['outside_closure'] += 1
        elif p % 4 == 1:
            routes['ordinary_A63'] += 1
        else:
            exponent, remaining = valuation(enlarge, p)
            assert remaining == 1
            routes['inert_p_power'] += 1
assert sum(routes.values()) == 600

result = {
    'status':'PASS', 'statement':'A64 candidate, not registered',
    'scope':'Exact count identities only. The actual tame model and marked paths are established in the written proof, not inferred from tests.',
    'symbolic_cluster_identity':str(s.expand(cluster_sum)),
    'symbolic_Riemann_Hurwitz_identity':True,
    'elliptic_counts':elliptic_rows,
    'abstract_branch_patterns':branch_rows,
    'actual_Heisenberg_count_rows':heisenberg_rows,
    'inert_p_power_rows':inert_rows,
    'case_partition_600_checks':routes,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(f'PASS: symbolic cluster/Euler identities; {len(branch_rows)} tame-index count checks; '
      f'{len(heisenberg_rows)} actual Heisenberg count rows; {len(inert_rows)} inert-power rows; all 600 case partitions.')
