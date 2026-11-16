#!/usr/bin/env python3
"""Exact harmonic-cover test from two explicit points on E_34."""
from fractions import Fraction as F
from itertools import product
from harmonic_tripod_obstruction_search import fourth_roots_units, hilbert, primes, is_square

n = F(34)
P = (F(-16), F(120))
Q = (F(162), F(2016))
for x, y in (P, Q):
    assert y*y == x**3-n*n*x
Qprime = (-n*n/Q[0], n*n*Q[1]/Q[0]**2)
assert Qprime[1]**2 == Qprime[0]**3-n*n*Qprime[0]
R = (1+Qprime[0]/n)/2
c = (1-P[0]/n)/2
r = abs(P[1]/Qprime[1])
char = 2*r
D = [c/R, (c-1)/(R-1), (c-F(1,2))/(R-F(1,2))]
assert D[0]*D[1]*D[2] == -r*r
boundary = [(1/(1-R), 1/(1-2*R)), (1/R, 1/(2*R-1)), (1/(2*R), 1/(2*(1-R)))]
assert not any(is_square(-a) or is_square(-b) or is_square(-a*b) for a, b in boundary)
for name, value in [('P', P), ('Q', Q), ('Q_plus_2torsion', Qprime), ('R', R), ('c', c), ('r', r), ('character', char), ('D', D), ('boundary', boundary)]:
    print(f'{name}: {value}', flush=True)
S = {2, 3}
for value in [R, R-1, R-F(1,2), c, c-1, c-F(1,2), R-c, char]:
    S |= primes(value)
trials = points = nonzero = 0
for p in sorted(S):
    limit = 16384 if p == 2 else min(p**3, 10000)
    candidates = [F(x) for x in range(1, limit+1)]
    candidates += [F(x, p**h) for h in range(1, 3) for x in range(1, min(p**2, 3000)) if x % p]
    local_nonzero = 0
    for X in candidates:
        T = R*X**4
        if T in (0, F(1,2), 1, c):
            continue
        trials += 1
        Ys = fourth_roots_units((T-1)/(R-1), p)
        if not Ys:
            continue
        Zs = fourth_roots_units((T-F(1,2))/(R-F(1,2)), p)
        if not Zs:
            continue
        points += 1
        f = (T-c)/(R-c)
        if not hilbert(f, char, p):
            continue
        nonzero += 1
        local_nonzero += 1
        for Y, Z in product(Ys, Zs):
            symbols = [[hilbert(W, a, p), hilbert(W, b, p)] for W, (a,b) in zip((X,Y,Z), boundary)]
            if any(any(row) for row in symbols):
                continue
            print('EXACT LOCAL WITNESS', flush=True)
            for key, value in [('p',p),('X',X),('T',T),('Y_root_unit_representative',Y),('Z_root_unit_representative',Z),('normalized_function',f),('boundary_symbols',symbols)]:
                print(f'{key}: {value}', flush=True)
            print(f'trials={trials}, local_points={points}, nonzero_evaluations={nonzero}', flush=True)
            raise SystemExit(0)
    print(f'place={p}, nonzero_evaluations={local_nonzero}', flush=True)
print(f'No witness in this finite search: trials={trials}, local_points={points}, nonzero_evaluations={nonzero}', flush=True)
print('No assertion about rank or independence of P,Q is needed or inferred.', flush=True)
