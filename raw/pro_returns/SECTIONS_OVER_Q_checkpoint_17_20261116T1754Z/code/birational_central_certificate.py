"""Finite certificate used in the birational/central lifting audit.

The proof is infinite/profinite and is in notes/birational.md.  This script
checks its sole finite arithmetic witness, and the nine-pair norm witness
referred to in AP D.24.  It does not claim to compute any Galois section.
"""
from itertools import product

p = 3
squares = {a * a % p for a in range(p)}
assert squares == {0, 1}
assert (-1) % p not in squares
assert 2 % p not in squares
print("F_3 squares:", sorted(squares))
print("The classes of 1 and -1 differ in F_3^*/F_3^{*2}.")
print("At t=2, the deleted-point coordinate t-3 equals -1.")
print("The chosen central lift has coordinate 1.")
print("Their local modulus-two Kummer coordinates at 3 differ.")
zeros = [(a, b) for a, b in product(range(p), repeat=2)
         if (a * a + b * b) % p == 0]
assert zeros == [(0, 0)]
print("F_3 zeros of a^2+b^2:", zeros)
print("This is the residue witness for the Q(i)/Q norm parity obstruction at 3.")
