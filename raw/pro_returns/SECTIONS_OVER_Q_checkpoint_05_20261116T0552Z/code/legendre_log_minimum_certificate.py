#!/usr/bin/env python3
"""Exact finite certificate and range comparison for A.79.

The enumeration verifies an explicit criterion; it does not classify all
realizations. The infinite families are established by the proof.
"""
from functools import lru_cache


@lru_cache(None)
def factor(n):
    assert n >= 1
    result = []
    d = 2
    while d*d <= n:
        e = 0
        while n % d == 0:
            e += 1
            n //= d
        if e:
            result.append((d,e))
        d = 3 if d == 2 else d+2
    if n > 1:
        result.append((n,1))
    return tuple(result)


def vp(n,p):
    assert n != 0
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


@lru_cache(None)
def log_depth(p,q):
    assert p != q
    if p == 2:
        return vp(q*q-1,2)-1
    depth = 1
    assert pow(q,p-1,p) == 1
    while pow(q,p-1,p**(depth+1)) == 1:
        depth += 1
    assert pow(q,p-1,p**depth) == 1
    assert pow(q,p-1,p**(depth+1)) != 1
    return depth


def weight(p,q,e):
    return vp(e,p) + log_depth(p,q)


def p_candidates(lam):
    return tuple(p for p,e in factor(lam) if p != 2 or e >= 5)


def is_power_of_two(n):
    return n > 0 and n & (n-1) == 0


def criterion(lam):
    assert lam > 1 and lam % 2 == 0
    rows = []
    for p in p_candidates(lam):
        values = tuple((q,weight(p,q,e)) for q,e in factor(lam-1))
        minimum = min(v for q,v in values)
        attained = tuple(q for q,v in values if v == minimum)
        if len(attained) != 1:
            return False, tuple(rows)
        rows.append((p,values,attained[0]))
    return True, tuple(rows)


def earlier_criteria(lam):
    k = vp(lam,2)
    return (lam <= 32
            or (len(factor(lam-1)) == 1 and k % 2 == 1)
            or is_power_of_two(lam) or is_power_of_two(lam-1))


recognized = []
new_gl = []
new_h = []
new_composite = []
for lam in range(2,5001,2):
    passed, rows = criterion(lam)
    if not passed:
        continue
    k = vp(lam,2)
    scope = 'H' if k in (2,4) else 'GL'
    recognized.append((lam,scope))
    if not earlier_criteria(lam):
        (new_h if scope == 'H' else new_gl).append(lam)
        if len(factor(lam-1)) > 1:
            new_composite.append((lam,scope))

new_h_after_a64 = [lam for lam in new_h
                  if not (vp(lam,2) == 4 and len(factor(lam//16)) == 1)]

assert factor(191) == ((191,1),)
assert factor(88) == ((2,3),(11,1)) and factor(87) == ((3,1),(29,1))
assert criterion(88) == (True, ((11,((3,2),(29,1)),29),))
assert criterion(120) == (True, ((3,((7,1),(17,2)),7),(5,((7,2),(17,1)),17)))
assert all(lam in new_gl for lam in (88,120,192,470,1088))
assert all(lam in new_h for lam in (44,60,68,244))

family_checks = 0
for q, starting_j, target_k in ((191,0,6),(3,2,2)):
    for j in range(starting_j,starting_j+25):
        exponent = 2*j+1
        lam = q**exponent+1
        assert vp(lam,2) == target_k
        assert lam > (1 << target_k)
        assert not is_power_of_two(lam) and not is_power_of_two(lam-1)
        # Its neighbour is exactly the one-prime powerq^exponent;
        # factorization of the much larger lambda is unnecessary.
        assert (lam-1) == q**exponent
        family_checks += 1

print('A.79 exact finite criterion and range certificate: all checks passed.')
print('Range: even integers2 through5000. The earlier comparison includes A41, A45(extended through32), and A63.')
print(f'Parameters passing the exact criterion: {len(recognized)}.')
print(f'Additional relative to those specified criteria: {len(new_gl)} with arbitrary labeled GL; {len(new_h)} requiringH.')
print('Additional GL parameters:', ', '.join(map(str,new_gl)))
print('First40 additional H parameters:', ', '.join(map(str,new_h[:40])))
print(f'After also excluding the explicit normalized prime-power criterion A64: {len(new_h_after_a64)} additionalH parameters.')
print('First40 after that further comparison:', ', '.join(map(str,new_h_after_a64[:40])))
print('Additional composite-neighbour parameters and scopes:', new_composite)
for lam in (44,88,120,192,244):
    print(f'lambda={lam}, v2={vp(lam,2)}, neighbour factorization={factor(lam-1)}, exact rows={criterion(lam)[1]}')
print(f'Exact dyadic valuations and exclusion from A63 checked for {family_checks} initial family members.')
print('The families themselves and arbitrary-parameter recognition are proved in A79, with the GL/H distinction retained.')
print('No claim that these are all recognized parameters, or that A1/A7 is settled, is made.')
