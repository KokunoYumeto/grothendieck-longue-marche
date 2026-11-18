"""Executed finite checks for the E.135 denominator and E.136 countermodel.

This checks prime fields only. The general finite-field assertions have
the separate algebraic proofs in the paper.
"""
from math import isqrt


def isprime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def v3(n):
    result = 0
    while n % 3 == 0:
        n //= 3
        result += 1
    return result


fermat_checks = 0
lift_checks = 0
denominator_checks = 0
for q in range(2, 201):
    if q % 3 != 2 or not isprime(q):
        continue
    previous = {t: (t, (1-t) % q) for t in range(2, q)}
    for n in range(1, 7):
        m = 3**n
        powers = [pow(x, m, q) for x in range(q)]
        assert len(set(powers)) == q
        roots = {value: x for x, value in enumerate(powers)}
        affine = sum((powers[x]+powers[y]) % q == 1
                     for x in range(q) for y in range(q))
        infinity = sum(value == q-1 for value in powers)
        assert affine+infinity == q+1
        current = {t: (roots[t], roots[(1-t) % q]) for t in range(2, q)}
        for t, (x, y) in current.items():
            assert (pow(x, 3, q), pow(y, 3, q)) == previous[t]
            lift_checks += 1
        previous = current
        fermat_checks += 1
    e = v3(q*q-1)
    for k in range(1, 101):
        assert v3(q**(2*k)-1) == e+v3(k)
        denominator_checks += 1

print('E136 prime-field Fermat counts through q200 and n6:', fermat_checks)
print('E136 compatible interior lift checks:', lift_checks)
print('E136 largest checked degree/genus:', 3**12, (3**6-1)*(3**6-2)//2)
print('E135 even-weight correction denominator checks:', denominator_checks)
print('PASS: finite checks; general finite-field and all-n claims proved separately')
