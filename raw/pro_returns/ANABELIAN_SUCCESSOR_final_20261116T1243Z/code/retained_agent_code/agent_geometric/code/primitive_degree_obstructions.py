#!/usr/bin/env python3
"""Exact necessary orbit/intersection test for primitive two-rank zero in genus two.
No sufficiency is asserted. Python standard library only.
"""
import json
from math import gcd, isqrt
from pathlib import Path


def orbit(n):
    assert n > 1 and n % 2
    h, a = set(), 1
    while a not in h:
        h.add(a)
        a = 2 * a % n
    assert a == 1
    u = h | {(-x) % n for x in h}
    phi = sum(gcd(i, n) == 1 for i in range(1, n))
    assert phi % len(u) == 0
    r = 2 * phi // len(u)
    return dict(n=n, phi=phi, order_of_two=len(h),
                minus_one_in_doubling_orbit=(n-1 in h),
                order_of_plus_minus_doubling_group=len(u),
                required_primitive_theta_points=r,
                pair_bound=2*(n-1), primitive_pair_lower_bound=r*(r-1),
                nonordinary_pair_lower_bound=r*(r+1),
                universally_excluded=r*(r-1)>2*(n-1),
                excluded_for_nonordinary_base=r*(r+1)>2*(n-1))


def main():
    data=[orbit(n) for n in range(3, 2002, 2)]
    examples=[orbit(n) for n in (3, 5, 7, 9, 11, 13, 35, 127, 257)]
    # For d >= 48, (2^d-1)^(1/6) >= 3d.  The seed is checked
    # by integer arithmetic; the ratio 2^((d-1)/6)/d then increases.
    assert 2**47 >= (3*48)**6
    assert 2*48**6 > 49**6
    out=dict(status='necessary conditions only', examples=examples,
             excluded_odd_degrees_through_2001=[x['n'] for x in data if x['universally_excluded']],
             extra_nonordinary_exclusions_through_2001=[x['n'] for x in data if x['excluded_for_nonordinary_base'] and not x['universally_excluded']],
             infinite_family={'n':'2^d-1','d_at_least':48,
                 'totient_lower_bound':'phi(n) >= (2/3) n^(2/3) for odd n',
                 'required_points_lower_bound':'r >= phi(n)/d >= 2 sqrt(n)',
                 'seed_inequality_verified':True,
                 'monotonicity_seed_inequality_verified':True},
             all_exact_tests=data)
    p=Path(__file__).with_name('primitive_degree_obstructions_output.json')
    p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='all_exact_tests'},indent=2))

if __name__=='__main__':
    main()
