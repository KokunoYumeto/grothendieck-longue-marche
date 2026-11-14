#!/usr/bin/env python3
"""Finite checks illustrating F.49; the infinite assertions are proved in text."""
from itertools import product


def mul(x, y):
    # F_9 = F_3[a]/(a^2 + 1).
    u, v = x
    s, t = y
    return ((u*s + 2*v*t) % 3, (u*t + v*s) % 3)


def power(x, n):
    z = (1, 0)
    while n:
        if n & 1:
            z = mul(z, x)
        x = mul(x, x)
        n //= 2
    return z


elements = list(product(range(3), repeat=2))
frob = {x: power(x, 3) for x in elements}
assert len(set(frob.values())) == 9
assert all(frob[frob[x]] == x for x in elements)
assert all(frob[(a, 0)] == (a, 0) for a in range(3))
assert frob[(0, 1)] == (0, 2)
closed_orbits = {frozenset((x, frob[x])) for x in elements}
assert len(closed_orbits) == 6
assert all(frozenset(frob[x] for x in orbit) == orbit for orbit in closed_orbits)
print('F_9: Frobenius fixes all three F_3-points and all six closed-point orbits.')
print('F_9: the two framed points a and -a above t^2+1 are interchanged.')


def delta_mod(n):
    """Coordinate of delta: 2-adic coordinate 0, odd coordinates 1."""
    two = 1
    odd = n
    while odd % 2 == 0:
        two *= 2
        odd //= 2
    if odd == 1:
        return 0
    return (two * pow(two, -1, odd)) % n


checks = 0
for n in range(1, 129):
    for m in range(n, 513, n):
        assert delta_mod(m) % n == delta_mod(n)
        checks += 1
assert all(delta_mod(2**r) == 0 for r in range(12))
assert delta_mod(3) == 1
print(f'Pro-Frobenius coordinates: {checks} finite divisibility compatibilities passed.')
print('Coordinates modulo 1..12:', [delta_mod(n) for n in range(1, 13)])
print('The coherent delta fixes every degree-2-power finite subfield and moves F_(p^3).')
