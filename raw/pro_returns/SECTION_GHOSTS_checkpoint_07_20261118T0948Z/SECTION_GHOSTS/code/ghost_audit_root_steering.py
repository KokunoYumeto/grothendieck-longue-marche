#!/usr/bin/env python3
"""Finite unit-group certificate for E.121's root-steering calculation.

This checks the local arithmetic on a small auxiliary prime. It does not
compute the point-three global central Frobenius, nor an A.44 prime with
its enormous full CRT modulus. Every possible central residue is checked.
"""
import sympy as S

q, n, generator = 9721, 24, 7
assert S.isprime(q) and S.primitive_root(q) == generator
assert S.factorint(q-1) == {2:3, 3:5, 5:1}
log_minus_two = int(S.discrete_log(q, (-2)%q, generator))
log_three = int(S.discrete_log(q, 3, generator))
assert log_minus_two % n == 0 and log_three % 3 != 0
z_exponent = (-log_minus_two//n) % ((q-1)//n)
zeta_exponent = (q-1)//3
roots = []
primitives = []
for k in range(3):
    exponent = (z_exponent+k*zeta_exponent) % (q-1)
    residue = pow(generator, exponent, q)
    assert (-2*pow(residue,n,q)) % q == 1
    numerator = log_minus_two+n*exponent
    assert numerator % (q-1) == 0
    primitive = numerator//(q-1)
    roots.append(residue)
    primitives.append(primitive)
assert {u % 3 for u in primitives} == {0,1,2}
print(f"Auxiliary q={q}, n={n}, v3(q-1)=5, v3(n)=1, primitive generator={generator}.")
print(f"Discrete logs of -2 and3: {log_minus_two}, {log_three}.")
print(f"Three n-th roots of (-2)^(-1): {roots}.")
print(f"Normalized unit-cocycle primitives: {primitives}; modulo3: {[u%3 for u in primitives]}.")
for gamma in range(3):
    mismatches = [(gamma-q*log_three*u)%3 for u in primitives]
    assert mismatches.count(0) == 1
    print(f"For central residue gamma={gamma}, mismatch residues={mismatches}: exactly two nonzero.")
for f in range(1,9):
    for e in range(f+1,f+7):
        for unit in (1,2,4,5):
            n0=3**f*unit
            torsion_log=3**(e-f)
            assert (n0*torsion_log)//3**e == unit
            assert unit % 3 != 0
print("PASS: all 192 abstract valuation cases preserve a unit primitive increment.")
print("This certificate checks local root steering; it does not certify a numerical recursive A.44 output.")
