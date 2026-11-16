#!/usr/bin/env python3
"""Exact finite arithmetic for A.82 and its two Hensel tests."""

from itertools import product


def vp(n,p):
    assert n != 0
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a


def quotient(a,p):
    return ((pow(a,p-1,p*p)-1)//p) % p


def squares(p):
    return {x*x % p for x in range(1,p)}


odd_forms = 0
odd_unit_zeros = 0
for p in (3,5,7):
    for rank in (1,2,3):
        for coeffs in product(range(p), repeat=rank):
            if not any(coeffs):
                continue
            j = next(i for i,c in enumerate(coeffs) if c)
            odd_forms += 1
            for z in product(range(1,p), repeat=rank):
                value = sum(c*x*x for c,x in zip(coeffs,z))
                if value % p:
                    continue
                derivative = 2*coeffs[j]*z[j] % p
                t = -(value//p)*pow(derivative,-1,p) % p
                lifted = list(z)
                lifted[j] += p*t
                assert all(x % p for x in lifted)
                assert sum(c*x*x for c,x in zip(coeffs,lifted)) % (p*p) == 0
                odd_unit_zeros += 1

root_lookup = {x*x % 1024:x for x in range(1,1024,2)}
assert set(root_lookup) == set(range(1,1024,8))
dyadic_forms = 0
dyadic_unit_zeros = 0
for rank in (1,2,3):
    for coeffs in product(range(8), repeat=rank):
        odd = [i for i,c in enumerate(coeffs) if c % 2]
        if not odd:
            continue
        dyadic_forms += 1
        necessary = sum(coeffs) % 8 == 0
        # Every odd square is1 mod8, so this also checks all residue tuples.
        for z in product((1,3,5,7), repeat=rank):
            assert (sum(c*x*x for c,x in zip(coeffs,z)) % 8 == 0) == necessary
        if necessary:
            j = odd[0]
            target = -(sum(coeffs)-coeffs[j])*pow(coeffs[j],-1,1024) % 1024
            assert target in root_lookup
            lifted = [1]*rank
            lifted[j] = root_lookup[target]
            assert sum(c*x*x for c,x in zip(coeffs,lifted)) % 1024 == 0
            dyadic_unit_zeros += 1

assert (quotient(3,17),quotient(11,17)) == (10,9)
assert -(10)*pow(9,-1,17) % 17 == 14
assert 14 not in squares(17)
T17 = {(10*x*x+9*y*y) % 17 for x in range(1,17) for y in range(1,17)}
assert 0 not in T17
assert (quotient(2,11),quotient(17,11)) == (5,3)
assert -5*pow(3,-1,11) % 11 == 2 and 2 not in squares(11)
assert vp(2**2-1,3) == 1 and vp(17**2-1,3) == 2
assert (-33) % 8 == 7
assert all((1-8*u) % 8 == 1 for u in (1,3,5,7))
assert {u*u % 8 for u in (1,3,5,7)} == {1}

# In dimension2 the finite form criterion equals the square-ratio criterion.
binary_checks = 0
for p in (3,5,7,11,13,17,19):
    sq = squares(p)
    for a,b in product(range(1,p),repeat=2):
        ratio = -a*pow(b,-1,p) % p
        exists = any((a+b*z) % p == 0 for z in sq)
        assert exists == (ratio in sq)
        binary_checks += 1

print('A.82 exact finite arithmetic certificate: all checks passed.')
print(f'Odd normalized forms examined: {odd_forms}; unit residue zeros lifted explicitly modulo p^2: {odd_unit_zeros}.')
print(f'Dyadic normalized forms examined: {dyadic_forms}; admissible all-unit zeros lifted modulo2^10: {dyadic_unit_zeros}.')
print(f'Binary square-ratio equivalences: {binary_checks}.')
print('lambda34: normalized17-Fermat quotients(3,11)=(10,9), required ratio14 is not a square.')
print('Nonzero squares modulo17:', sorted(squares(17)))
print('Values of the normalized binary form on nonzero coordinates modulo17:', sorted(T17))
print('lambda34 coefficient2: the spurious valuation3 branch gives squareclass1, whereas B has squareclass7.')
print('lambda34 coefficient3: exact logarithm depths for2 and17 are1 and2.')
print('lambda34 coefficient11: Fermat quotients(2,17)=(5,3), ratio2 is not a square.')
print('The common global multiplier and all-prime lifting equivalences are proved in A82; these are finite exact checks.')
