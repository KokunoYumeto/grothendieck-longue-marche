#!/usr/bin/env python3
"""One exact F_2[C_3] check; no claim about the actual canonical word."""

def mul(a, b):
    ans = 0
    for i in range(3):
        for j in range(3):
            if (a >> i) & (b >> j) & 1:
                ans ^= 1 << ((i + j) % 3)
    return ans


def inv(a):
    return sum(((a >> i) & 1) << ((-i) % 3) for i in range(3))


def aug(a):
    return a.bit_count() % 2


one, x, x2 = 1, 2, 4
b = one ^ x ^ x2
v = one ^ x
assert mul(x, x2) == one
assert inv(b) == b
assert aug(b) == 1
assert v != 0 and mul(b, v) == 0
assert mul(b, b) == b
print("Ring: F_2[x]/(x^3-1), basis (1,x,x^2).")
print("x*x^2 = 1; inversion sends x to x^2.")
print("b = 1+x+x^2; inversion(b)=b; augmentation(b)=1.")
print("v = 1+x is nonzero; b*v=0; b^2=b.")
print("PASS: b is a fixed augmentation-one nonunit.")
print("Scope: generic ring warning only; no actual canonical-word counterexample.")
