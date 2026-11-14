#!/usr/bin/env python3
"""Exact certificates for Gal(X^5-X-1/Q)=S5 used in the residual-field audit."""
from itertools import permutations, product


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def remainder(a, b, p):
    a, b = trim([x % p for x in a]), trim([x % p for x in b])
    while len(a) >= len(b):
        c = a[-1] * pow(b[-1], -1, p) % p
        shift = len(a) - len(b)
        for i, coefficient in enumerate(b):
            a[shift+i] = (a[shift+i] - c*coefficient) % p
        a = trim(a)
    return a


def multiply(a, b, p):
    out = [0] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j] + x*y) % p
    return trim(out)


f = [-1, -1, 0, 0, 0, 1]
q2 = [1, 1, 1]
q3 = [1, 0, 1, 1]
assert multiply(q2, q3, 2) == [x % 2 for x in f]
assert all(remainder(q, [-a % 2, 1], 2) for q in (q2, q3) for a in range(2))
print('Modulo 2: X^5-X-1 = (X^2+X+1)(X^3+X^2+1).')
print('Both factors are irreducible (degrees 2 and 3, with no roots), and distinct.')
checks = 0
for degree in (1, 2):
    for coeff in product(range(3), repeat=degree):
        assert remainder(f, list(coeff)+[1], 3)
        checks += 1
print(f'Modulo 3: no monic divisor of degree 1 or 2 ({checks} divisions checked).')
print('A reducible degree-5 polynomial has a factor of degree at most 2, so it is irreducible.')


identity = tuple(range(5))


def compose(a, b):
    return tuple(a[b[i]] for i in range(5))


def inverse(a):
    out = [0] * 5
    for i, x in enumerate(a):
        out[x] = i
    return tuple(out)


def derived(group):
    inverses = {a: inverse(a) for a in group}
    generators = {
        compose(compose(compose(a, b), inverses[a]), inverses[b])
        for a in group for b in group
    }
    subgroup = {identity}
    pending = [identity]
    while pending:
        a = pending.pop()
        for b in generators:
            c = compose(a, b)
            if c not in subgroup:
                subgroup.add(c)
                pending.append(c)
    return subgroup


s5 = set(permutations(range(5)))
a5 = derived(s5)
a5_again = derived(a5)
assert len(s5) == 120 and len(a5) == 60 and a5_again == a5
print('Exact derived-subgroup orders:', len(s5), len(a5), len(a5_again))
print('Thus S5 is not solvable; its splitting field is not contained in Q^solv.')
