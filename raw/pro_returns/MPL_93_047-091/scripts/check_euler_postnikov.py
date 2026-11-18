#!/usr/bin/env python3
"""Small exact calculations for research_euler.md (no manuscript reading).

These finite checks certify the displayed algebra, not the imported topological
realization theorem. The free quadratic-module model is M=Z, L=Z x Z/4,
partial(m,b)=2m, w(x,y)=(0,xy mod4), with action (m,b)^x=(m,b+2mx).
Its finite quotient below has M=Z/4, L=Z/8, partial(a)=2a mod4.
"""

from itertools import product


def boundary(a):
    return 2*a % 4


def pairing(x, y):
    return 2*x*y % 8


def action(a, x):
    return (a + pairing(boundary(a), x)) % 8


def carry(a, b):
    return 1 if a == b == 1 else 0


def k_lift(a, b, c):
    return (action(carry(b, c), a) - carry((a+b) % 2, c)
            + carry(a, (b+c) % 2) - carry(a, b)) % 8


def kappa(a, b, c):
    return k_lift(a, b, c) // 2


def d2(f, a, b, c, modulus):
    return (f(b, c) - f((a+b) % 2, c) + f(a, (b+c) % 2) - f(a, b)) % modulus


def d3(f, a, b, c, d, modulus):
    return (f(b, c, d) - f((a+b) % 2, c, d) + f(a, (b+c) % 2, d)
            - f(a, b, (c+d) % 2) + f(a, b, c)) % modulus


def main():
    assert all(boundary(pairing(x, y)) == 0 for x, y in product(range(4), repeat=2))
    assert all((pairing(boundary(a), x) + pairing(x, boundary(a))) % 8 == 0
               for a, x in product(range(8), range(4)))
    assert all(pairing(boundary(a), boundary(b)) == 0 for a, b in product(range(8), repeat=2))
    assert all(action(action(a, x), y) == action(a, (x+y) % 4)
               for a, x, y in product(range(8), range(4), range(4)))
    assert all(action((a+b) % 8, x) == (action(a, x)+action(b, x)) % 8
               for a, b, x in product(range(8), range(8), range(4)))
    assert all(boundary(action(a, x)) == boundary(a) for a, x in product(range(8), range(4)))
    assert all(action(a, boundary(b)) == a for a, b in product(range(8), repeat=2))
    kernel = [a for a in range(8) if boundary(a) == 0]
    assert kernel == [0, 2, 4, 6]
    assert all(action(a, x) == a for a, x in product(kernel, range(4)))
    assert all(k_lift(a,b,c) in kernel for a,b,c in product(range(2),repeat=3))
    assert kappa(1,1,1) == 2
    assert all(d3(kappa,*q,4) == 0 for q in product(range(2),repeat=4))
    for z in range(4):
        f = lambda a,b: z if a == b == 1 else 0
        assert d2(f,1,1,1,4) == 0
    print('PASS: finite reduced quadratic module and crossed-module action identities.')
    print('PASS: kernel C4 and cokernel C2, with trivial induced action on kernel.')
    print('PASS: kappa(1,1,1)=2 mod4; all 16 normalized cocycle equations hold.')
    print('PASS: none of the 4 normalized C2-to-C4 two-cochains has this coboundary.')
    # A normalized 3-cochain of C2 is determined by its value at (1,1,1).
    for modulus, expected in [(4,[0,2]),(2,[0,1])]:
        cocycles=[]
        for z in range(modulus):
            f=lambda a,b,c: z if a == b == c == 1 else 0
            if all(d3(f,*q,modulus) == 0 for q in product(range(2),repeat=4)):
                cocycles.append(z)
        assert cocycles == expected
        print(f'PASS: H^3(C2;Z/{modulus}) has normalized representatives {cocycles}; all normalized 2-coboundaries vanish.')
    # Free-model identities: integer-coordinate equations are literal equality;
    # second-coordinate identities are polynomial and periodic modulo four.
    for m,n,b,c,x,y in product(range(4),repeat=6):
        assert ((2*m)*x + x*(2*m)) % 4 == 0
        assert ((2*m)*(2*n)) % 4 == 0
        assert (b+2*m*x+2*m*y) % 4 == (b+2*m*(x+y)) % 4
        assert (b+c+2*(m+n)*x) % 4 == ((b+2*m*x)+(c+2*n*x)) % 4
    print('PASS: free model M=Z,L=Z x C4 has the required modulo-four identities; its first coordinates satisfy them identically.')
    totals=[(1971,190,87,277),(1972,206,92,298),(1973,223,93,316),
            (1974,249,93,342),(1975,257,104,361),(1976,275,79,354)]
    assert all(a+b == total for _,a,b,total in totals)
    print('PASS: all six scan061 budget column totals, including 275+79=354.')
    print('SCOPE: exact elementary algebra/arithmetic only; no formal proof assistant, image inspection, or independent proof of topological realization.')


if __name__ == '__main__':
    main()
