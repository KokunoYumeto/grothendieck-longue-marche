#!/usr/bin/env python3
"""Finite arithmetic certificate for the uncountable-kernel proof.

No finite run proves the infinite derived-limit statement.  The proof
using product/c0 is in ghost_h2_counterexample.tex.
"""
from sympy import isprime

def v3(n):
    k = 0
    while n % 3 == 0:
        k += 1
        n //= 3
    return k

qs = []
for j in range(1, 13):
    modulus = 3 ** (j + 1)
    q = 1 + 3**j
    while not isprime(q):
        q += modulus
    assert v3(q-1) == j
    qs.append(q)
print("Selected primes q_j with q_j=1+3^j mod 3^(j+1):")
print(qs)
print("Their exact v_3(q_j-1):", [v3(q-1) for q in qs])

# At target level n=1, the image from level m in coordinate j is
# F_3 precisely for m<=j; otherwise it is zero.
for m in range(1, 7):
    active = []
    for j, q in enumerate(qs[:8], 1):
        d, mod = q-1, 3**m
        kernel = [a for a in range(mod) if d*a % mod == 0]
        residues = {a % 3 for a in kernel}
        assert residues == ({0, 1, 2} if m <= j else {0})
        if len(residues) == 3:
            active.append(j)
    print("Image from level", m, "to level 1, active selected coordinates:", active)
print("PASS: exact residue reduction maps on the finite sample.")
print("Infinite nonvanishing and uncountability are proved separately.")
