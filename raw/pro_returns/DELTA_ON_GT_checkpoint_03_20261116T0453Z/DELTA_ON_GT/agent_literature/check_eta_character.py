#!/usr/bin/env python3
"""Exact finite certificate for the eta-squared character modulo twelve.

Enumerates SL2(Z/12), propagates T -> 1 and S -> -3 in Z/12,
and checks every Cayley edge. No external packages or inputs.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 2026-11-16.
"""
from collections import deque
from itertools import product

N = 12
I = (1, 0, 0, 1)
T = (1, 1, 0, 1)
S = (0, 11, 1, 0)

def mul(a, b):
    return ((a[0]*b[0]+a[1]*b[2]) % N,
            (a[0]*b[1]+a[1]*b[3]) % N,
            (a[2]*b[0]+a[3]*b[2]) % N,
            (a[2]*b[1]+a[3]*b[3]) % N)

def inv(a):
    return (a[3], -a[1] % N, -a[2] % N, a[0])

gens = ((T, 1), (inv(T), -1), (S, -3), (inv(S), 3))
character = {I: 0}
queue = deque([I])
edges = 0
while queue:
    a = queue.popleft()
    for b, k in gens:
        ab = mul(a, b)
        expected = (character[a]+k) % N
        if ab not in character:
            character[ab] = expected
            queue.append(ab)
        else:
            assert character[ab] == expected, (a, b)
        edges += 1

all_sl = {a for a in product(range(N), repeat=4)
          if (a[0]*a[3]-a[1]*a[2]) % N == 1}
assert set(character) == all_sl
assert len(all_sl) == 1152
print('SL2(Z/12) ORDER', len(all_sl))
print('CAYLEY EDGES VERIFIED', edges)
print('eta^2: T -> zeta12, S -> zeta12^(-3)')
for u in (1, 5, 7, 11):
    k = character[(u, 0, 0, u)]
    assert k in (0, 6)
    sign = 1 if k == 0 else -1
    expected = 1 if u % 4 == 1 else -1
    assert sign == expected
    print('central u, exponent mod12, eta^2 sign', u, k, sign)

R = ((0, -1), (1, -1))
K = ((1-R[0][0], -R[0][1]), (-R[1][0], 1-R[1][1]))
assert K == ((1, 1), (-1, 2))
assert K[0][0]*K[1][1]-K[0][1]*K[1][0] == 3
print('I-R =', K, 'determinant 3')
print('DONE')
