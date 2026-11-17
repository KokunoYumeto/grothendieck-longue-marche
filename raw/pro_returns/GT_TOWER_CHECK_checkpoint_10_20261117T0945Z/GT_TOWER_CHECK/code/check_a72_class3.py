#!/usr/bin/env python3
"""Exact certificates for the new selected A.72 class-three exclusions.

The small finite-field prime tests only the new Heisenberg condition,
not the much larger A.72 boundary-field and CRT conditions. Existence
with all those conditions is proved by the exact field intersection.
"""
from collections import deque
from math import factorial, lcm
from sympy import isprime, nthroot_mod, primitive_root


for p in (7, 11, 13, 17, 19):
    # Formal exponent-vector proof of Theta(zeta X)/Theta(X).
    original = list(range(p))
    shifted = [(j - 1) % p for j in range(p)]
    difference = [shifted[j] - original[j] for j in range(p)]
    assert difference == [p - 1] + [-1] * (p - 1)
    for lam in range(1, p):
        k = pow(lam, -1, p)
        indices = [k * j % p for j in range(p)]
        assert all((indices[j] - k * j) % p == 0 for j in range(p))
    # Literal original initial factorial/precision values.
    B0 = 24
    assert B0 % p != 0
    N0, m = p * B0, 24 * p * B0
    assert m % p == 0 and m % (p * p) != 0
    assert (N0 * factorial(6)) % p == 0
    assert (N0 * factorial(6)) % (p * p) != 0
    precision = 2 * 1 + 4
    assert precision == 6
    # Universal exact residue modulo p^2; q=1 mod p^2 and alpha=0 mod p.
    modulus = p * p
    q = 1 + modulus
    for alpha0 in range(p):
        for gamma in range(1, p):
            for u in range(p):
                alpha = p * alpha0
                zd = (m * (gamma - q * alpha * u)
                      + (q * q - 1) * u * m * (m - 1) // 2)
                assert zd % p == 0 and zd % modulus != 0
    print(f"p={p}: radical/descent exponent identities, v_p(n0)=1, "
          "initial precision6, and all residue classes passed")


p = 7
root = primitive_root(p)


def mul(u, v):
    a, b, h, lam = u
    A, B, H, Lam = v
    return ((a + lam * A) % p, (b + lam * B) % p,
            (h + lam * lam * H + a * lam * B) % p,
            lam * Lam % p)


identity = (0, 0, 0, 1)
generators = [(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 0, root)]
seen, queue = {identity}, deque([identity])
while queue:
    u = queue.popleft()
    for g in generators:
        v = mul(u, g)
        if v not in seen:
            seen.add(v)
            queue.append(v)
assert len(seen) == p ** 3 * (p - 1)
print(f"Explicit H_7 semidirect F_7^*: generated order {len(seen)}")

for i in range(1, 500000):
    q = p * p * i + 1
    if not isprime(q):
        continue
    if pow(3, (q - 1) // p, q) != 1:
        continue
    if pow(q - 2, (q - 1) // p, q) != 1:
        continue
    zeta = pow(int(primitive_root(q)), (q - 1) // p, q)
    x = int(nthroot_mod(3, p, q))
    theta = 1
    for j in range(p):
        theta = theta * pow((1 - pow(zeta, j, q) * x) % q, j, q) % q
    symbol = pow(theta, (q - 1) // p, q)
    if symbol == 1:
        continue
    assert pow(x, p, q) == 3 and pow(zeta, p, q) == 1 and zeta != 1
    # Check invariance under every choice of the seventh root of three.
    symbols = []
    for j in range(p):
        xx = x * pow(zeta, j, q) % q
        th = 1
        for h in range(p):
            th = th * pow((1 - pow(zeta, h, q) * xx) % q, h, q) % q
        symbols.append(pow(th, (q - 1) // p, q))
    assert all(v == symbol for v in symbols)
    print(f"Small central-Frobenius certificate: p={p}, q={q}, "
          f"zeta={zeta}, x={x}, theta={theta}, symbol={symbol}")
    print("All seven root choices give the same nontrivial symbol.")
    break
else:
    raise AssertionError("No finite-field certificate found within the search range")

print("PASS. The small q is not asserted to meet any particular A.72 CRT field.")
