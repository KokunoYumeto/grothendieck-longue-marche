#!/usr/bin/env python3
"""Exact finite checks for the actual framed images at levels 24 and 60.

Infinite lifting and arithmetic image claims are proved in the accompanying
notes.  This certificate checks the finite rings, genuine signed matrices,
derived image constraints, shear, finite groups and parity kernels exactly.
It never identifies finite compatibility alone with full gentle liftability.
"""
from collections import deque
from itertools import product
from pathlib import Path
import hashlib
import json
import math


def matmul(a, b, n):
    x, y, z, w = a
    e, f, g, h = b
    return ((x*e+y*g) % n, (x*f+y*h) % n,
            (z*e+w*g) % n, (z*f+w*h) % n)


def matinv(a, n):
    x, y, z, w = a
    assert (x*w-y*z) % n == 1
    return (w % n, -y % n, -z % n, x % n)


def closure(gens, mul, identity):
    seen = {identity}
    queue = deque([identity])
    gens = tuple(dict.fromkeys(gens))
    while queue:
        a = queue.popleft()
        for b in gens:
            c = mul(a, b)
            if c not in seen:
                seen.add(c)
                queue.append(c)
    return seen


def matrix_group_and_derived(n):
    one = (1, 0, 0, 1)
    x = (1, 2, 0, 1)
    y = (1, 0, -2 % n, 1)
    mul = lambda a, b: matmul(a, b, n)
    gens = [x, y, matinv(x, n), matinv(y, n)]
    group = closure(gens, mul, one)
    c = mul(mul(mul(x, y), matinv(x, n)), matinv(y, n))
    orbit = {c}
    queue = deque([c])
    while queue:
        a = queue.popleft()
        for g in gens:
            b = mul(mul(g, a), matinv(g, n))
            if b not in orbit:
                orbit.add(b)
                queue.append(b)
    derived = closure(orbit, mul, one)
    assert derived <= group
    assert (-1 % n, 0, 0, -1 % n) not in group
    assert all((a % 4, b % 4, c % 4, d % 4) in
               {(1, 0, 0, 1), (1, 2, 0, 1),
                (1, 0, 2, 1), (1, 2, 2, 1)}
               for a, b, c, d in group)
    return group, derived, len(orbit)


def ringmul(a, b, n, cubic):
    x, y = a
    z, w = b
    return ((x*z-y*w) % n,
            (x*w+y*z-(y*w if cubic else 0)) % n)


def ringpow(a, k, n, cubic):
    r = (1, 0)
    while k:
        if k & 1:
            r = ringmul(r, a, n, cubic)
        a = ringmul(a, a, n, cubic)
        k >>= 1
    return r


def norm(a, cubic):
    x, y = a
    return x*x+y*y-(x*y if cubic else 0)


def ring_matrix(a, n, cubic):
    x, y = a
    if cubic:  # omega=-R, R=[[0,1],[-1,1]].
        return (x % n, -y % n, y % n, (x-y) % n)
    return (x % n, y % n, -y % n, x % n)


def actual_local_reduction(n, cubic):
    result = set()
    for a, b in product(range(n), repeat=2):
        if a % 4 != 1 or b % 4 != 0 or norm((a, b), cubic) % n != 1:
            continue
        if n % 8 == 0:
            if cubic and b % 8 != 0:
                continue
            if not cubic and a % 8 != 1:
                continue
        result.add((a, b))
    assert (1, 0) in result
    assert all(ringmul(a, b, n, cubic) in result for a in result for b in result)
    return result


def finite_order(a, mul, identity, bound):
    r = identity
    for k in range(1, bound+1):
        r = mul(r, a)
        if r == identity:
            return k
    raise AssertionError("order exceeds finite bound")


def crt_pair(n, residues):
    a = next(i for i in range(n) if all(i % m == v[0] for m, v in residues))
    b = next(i for i in range(n) if all(i % m == v[1] for m, v in residues))
    return (a, b)


def run_level(n):
    pure, derived, orbit_size = matrix_group_and_derived(n)
    tset = actual_local_reduction(n, True)
    wset = actual_local_reduction(n, False)
    cubic_mod3 = [ringpow((0, 2), k, 3, True) for k in range(6)]
    quartic_mod3 = [ringpow((0, 1), k, 3, False) for k in range(4)]
    one = (1, 0)
    identity = (0, one, one)

    def mul(a, b):
        return ((a[0]+b[0]) % n, ringmul(a[1], b[1], n, True),
                ringmul(a[2], b[2], n, False))

    def parity(a):
        k = cubic_mod3.index(tuple(v % 3 for v in a[1]))
        ell = quartic_mod3.index(tuple(v % 3 for v in a[2]))
        return (k+ell) % 2

    frames = set()
    valid_shears = []
    raw_pairs = {}
    for t in sorted(tset):
        k = cubic_mod3.index(tuple(v % 3 for v in t))
        allowed = []
        tm = ring_matrix(t, n, True)
        for shear in range(n):
            v = (1, shear, 0, 1)
            a = matmul(v, matinv(tm, n), n)
            if a not in derived:
                continue
            allowed.append(shear)
            assert shear % (8 if n == 24 else 4) == 0
            assert (shear+k) % 3 == 0
            for w in wset:
                beta = matmul(v, matinv(ring_matrix(w, n, False), n), n)
                assert beta in pure
                frame = (shear, t, w)
                raw = (a, beta)
                assert raw not in raw_pairs or raw_pairs[raw] == frame
                raw_pairs[raw] = frame
                frames.add(frame)
        expected = [s for s in range(n) if
                    s % (8 if n == 24 else 4) == 0 and (s+k) % 3 == 0]
        assert allowed == expected
        valid_shears.append({'T': t, 'cubic_mod3_exponent': k, 'shears': allowed})

    if n == 24:
        gens = [
            (0, (13, 0), one),       # extra Eisenstein two-adic bit
            (8, (9, 8), one),        # cubic rotation at3, t=8
            (0, one, (1, 12)),       # extra Gaussian two-adic bit
            (0, one, (9, 16)),       # quartic rotation at3
        ]
        invariant_factors = [2, 6, 2, 4]
        arithmetic_gens = [gens[0], gens[2], mul(gens[1], gens[3])]
        arithmetic_factors = [2, 2, 12]
    else:
        gens = [
            (20, (21, 20), one),     # cubic rotation at3, shear0 at5
            (0, (25, 24), one),      # cubic rotation at5
            (0, one, (21, 40)),      # quartic rotation at3
            (0, one, (25, 36)),      # quartic rotation at5
            (12, one, one),          # independent shear C5
        ]
        invariant_factors = [6, 6, 4, 4, 5]
        arithmetic_gens = [mul(gens[0], gens[2]), gens[1], gens[3], gens[4]]
        arithmetic_factors = [12, 6, 4, 5]

    generated = closure(gens, mul, identity)
    assert generated == frames
    assert len(frames) == math.prod(invariant_factors)
    orders = [finite_order(g, mul, identity, len(frames)) for g in gens]
    assert orders == invariant_factors
    assert all(mul(a, b) == mul(b, a) for a in gens for b in gens)
    kernel = {g for g in frames if parity(g) == 0}
    assert closure(arithmetic_gens, mul, identity) == kernel
    assert len(kernel) == math.prod(arithmetic_factors)
    assert [finite_order(g, mul, identity, len(frames)) for g in arithmetic_gens] == arithmetic_factors
    for a in frames:
        for b in gens:
            assert parity(mul(a, b)) == (parity(a)+parity(b)) % 2

    return {'level': n, 'signed_pure_order': len(pure),
            'signed_pure_derived_order': len(derived),
            'commutator_conjugacy_orbit_size': orbit_size,
            'cubic_coordinate_order': len(tset),
            'quartic_coordinate_order': len(wset),
            'paired_CM_order': len(tset)*len(wset),
            'framed_image_order': len(frames),
            'framed_cyclic_factors': invariant_factors,
            'framed_generators': gens,
            'generator_parities': [parity(g) for g in gens],
            'arithmetic_kernel_order': len(kernel),
            'arithmetic_kernel_cyclic_factors': arithmetic_factors,
            'arithmetic_kernel_generators': arithmetic_gens,
            'raw_frame_pair_injective': len(raw_pairs) == len(frames),
            'all_T_shears': valid_shears,
            'actuality_scope': 'Finite identities checked here; actual surjectivity follows from C20 and the written Tate/Kummer5 argument, not from enumeration.'}


def norm_lift_checks():
    # Exact finite corroboration of the separate all-depth Hensel proof.
    modulus = 2**18
    cubic = []
    for a in (1, 3, 5, 7):
        b = 0
        for j in range(18):
            candidates = (b, b+2**j)
            b = next(v for v in candidates
                     if ((a*a-1)//8-a*v+8*v*v) % 2**(j+1) == 0)
        u = (a, 8*b)
        assert norm(u, True) % modulus == 1
        cubic.append({'residue_mod8': [a, 0], 'lift_mod2pow18': [v % modulus for v in u]})
    gaussian = []
    for sign, k in product((1, -1), (0, 1)):
        t = 2*k
        deninv = pow(1+t*t, -1, modulus)
        u = (sign*(1-t*t)*deninv % modulus, sign*2*t*deninv % modulus)
        assert norm(u, False) % modulus == 1
        gaussian.append({'residue_mod8': [v % 8 for v in u], 'lift_mod2pow18': u})
    assert {tuple(v['residue_mod8']) for v in gaussian} == {(1, 0), (7, 0), (1, 4), (7, 4)}
    residues = {}
    for p in (3, 5):
        for cubic_flag in (False, True):
            finite = [(a, b) for a, b in product(range(p), repeat=2)
                      if norm((a, b), cubic_flag) % p == 1]
            for u in finite:
                c = 1
                for j in range(1, 7):
                    c = next(c+e*p**j for e in range(p)
                             if (c+e*p**j)**2*norm(u, cubic_flag) % p**(j+1) == 1)
                assert c % p == 1
                assert norm((c*u[0], c*u[1]), cubic_flag) % p**7 == 1
            residues[f'{"cubic" if cubic_flag else "quartic"}_mod{p}'] = len(finite)
    return {'cubic_two_adic_lifts': cubic, 'quartic_two_adic_lifts': gaussian,
            'odd_norm_one_counts_and_lifts_to_p7': residues,
            'warning': 'Gaussian norm-one residues modulo8 without the actual lift condition would be too large.'}


def main():
    result = {'status': 'PASS', 'levels': [run_level(24), run_level(60)],
              'local_norm_lift_checks': norm_lift_checks(),
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope': 'Exact finite certificate for a structural actual-image proof. Galois/full-group liftability is not inferred merely from finite solutions.'}
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'levels': [
        {k: x[k] for k in ('level','signed_pure_order','signed_pure_derived_order',
                           'paired_CM_order','framed_image_order','arithmetic_kernel_order')}
        for x in result['levels']], 'result_sha256': hashlib.sha256(path.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
