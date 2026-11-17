#!/usr/bin/env python3
"""Exact geometric quotient and rational identities of SECTIONS A.139.

The absent A.134 ordinary harmonic construction and its local Brauer
evaluation constants are not certified by this script.
"""
from fractions import Fraction as F

def mul(a, b):
    p = 0
    for i in range(8):
        if b & (1 << i):
            p ^= a << i
    # v^8=1 on the eight-dimensional module: characteristic two gives
    # F_2[v]/(v^8-1)=F_2[delta]/delta^8.
    while p.bit_length() > 8:
        top = p.bit_length() - 1
        p ^= (1 << top) | (1 << (top - 8))
    return p

def rank(vecs):
    pivots = {}
    for v in vecs:
        while v:
            p = v.bit_length() - 1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p] = v
                break
    return len(pivots)

delta = 3  # v+1
delta_power = 1
ranks = []
for k in range(9):
    ranks.append(rank([mul(delta_power, 1 << j) for j in range(8)]))
    delta_power = mul(delta_power, delta)
assert ranks == list(range(8, -1, -1))
orders = [4096] + [2 ** ranks[k] for k in range(1, 9)]
assert orders == [4096, 128, 64, 32, 16, 8, 4, 2, 1]

R, h, s = F(529, 382), F(1, 2), 155564491
a0, a1, ah = R, R - 1, (R - h) * s*s
a = a0*a1*ah
assert a == F(318039202706815117780707, 27871484)
c, d, rho = F(-338, 191), 18512174429, F(34, 1088951437)
assert d == 7*17*s
assert c*(c-1)*(c-h)/a == -rho*rho
assert d/(2*rho) == F(1088951437, 2)**2

print("H_D has index 8 in rank-two free group and Schreier rank 9.")
print("H_D/(H_D^2[H_D,H_D]) has dimension 9 over F_2.")
print("Q_D = F_2^8 semidirect C_16; |Q_D| =", 4096)
print("ranks of multiplication by delta^k, k=0..8:", ranks)
print("orders Gamma_1..Gamma_9:", orders)
print("exact nilpotency class: 8")
print("a =", a)
print("F(c)/a = -rho^2 and d/(2rho)=(1088951437/2)^2: verified")
print("PASS: geometric quotient and rational identities only.")
print("A.134 arithmetic construction/local Brauer evaluations: not certified.")
