#!/usr/bin/env python3
"""Exhaustive signed F_3 certificate for the actual coherent-frame formula.

No profinite existence assertion is inferred from this finite calculation.
The companion proof constructs the actual class and its comparison map first.
"""
from itertools import product
from pathlib import Path
from hashlib import sha256
import json

P = 3
I = (1, 0, 0, 1)
X = (1, 2, 0, 1)
Y = (1, 0, 1, 1)
C = (0, 2, 1, 2)
S = (0, 2, 1, 0)
D = (1, 0, 0, 2)


def mul(a, b):
    return tuple(v % P for v in (
        a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
        a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3]))


def inv(a):
    det = (a[0]*a[3]-a[1]*a[2]) % P
    assert det
    t = pow(det, -1, P)
    return tuple((t*v) % P for v in (a[3], -a[1], -a[2], a[0]))


def power(a, n):
    if n < 0:
        return power(inv(a), -n)
    out = I
    for _ in range(n):
        out = mul(out, a)
    return out


def chain(*args):
    out = I
    for a in args:
        out = mul(out, a)
    return out


def scalar(t, a=I):
    return tuple(t*x % P for x in a)


def conj(a, b):
    return chain(a, b, inv(a))


SL2 = [a for a in product(range(P), repeat=4)
       if (a[0]*a[3]-a[1]*a[2]) % P == 1]
Q8 = [a for a in SL2 if power(a, 4) == I]
assert len(SL2) == 24 and len(Q8) == 8
assert {conj(C, a) for a in Q8} == set(Q8)
assert [a for a in Q8 if conj(C, a) == a] == [I, scalar(-1)]

rows = []
table = []
for nu in range(3):
    for d in (1, -1):
        eps = (1-d)//2
        U = scalar(d, chain(power(Y, -nu), power(X, nu)))
        b = U[1]
        H = (1, -b % P, 0, d % P)
        K = conj(H, D)
        assert K == (1, nu, 0, 2)
        Phi = chain(power(Y, nu), power(X, -nu))
        De = (1, 0, 0, d % P)
        Je = conj(De, C)
        assert Je == scalar((-1)**eps, chain(power(Y, eps), C))
        target = conj(H, C)
        candidates = [Q for Q in Q8 if conj(Q, Je) == target]
        assert len(candidates) == 2
        assert candidates[1] == scalar(-1, candidates[0])
        table.append({'nu':nu, 'd':d, 'Q_up_to_sign':candidates[0]})
        for Q in candidates:
            for epsA in (1, -1):
                A = scalar(epsA, chain(power(X, nu), power(C, -nu)))
                assert A in Q8
                j = chain(Phi, A) if eps == 0 else conj(S, A)
                W = chain(inv(j), S, K, inv(Q), inv(K), inv(S), U, Q)
                expected = scalar(epsA*d)
                assert W == expected, (nu, d, epsA, Q, W, expected)
                rows.append({'nu':nu, 'd':d, 'epsilon':eps,
                             'epsilon_A':epsA, 'Q':Q, 'U':U,
                             'H':H, 'J_e':Je, 'q_j':j,
                             'actual_W':W, 'expected_W':expected})
assert len(rows) == 24
print(json.dumps({
    'status':'PASS', 'field':'F_3',
    'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'matrix_group_order':len(SL2), 'derived_quaternion_order':len(Q8),
    'checked_cases':len(rows), 'table_up_to_sign':table, 'cases':rows,
    'conclusion':'For every actual finite input satisfying the stated transporter equation, q_3(w)=epsilon_A*(d mod 3)*I.',
    'scope':'Finite comparison certificate only; actual profinite existence and frame independence require the companion proof.'
}, indent=2))
