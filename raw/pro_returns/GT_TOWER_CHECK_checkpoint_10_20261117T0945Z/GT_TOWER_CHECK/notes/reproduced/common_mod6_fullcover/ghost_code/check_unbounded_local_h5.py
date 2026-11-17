#!/usr/bin/env python3
"""Same-marking H5 local certificate; not the giant A.66 prime search."""
from itertools import product

q = 1545001  # Previously certified small Heisenberg prime.
zeta = 33119
x3 = 235919
theta3 = 1
assert pow(zeta, 5, q) == 1 and zeta != 1
assert pow(x3, 5, q) == 3
assert pow(q - 2, (q - 1) // 5, q) == 1
for i in range(5):
    theta3 = theta3 * pow((1 - pow(zeta, i, q) * x3) % q, i, q) % q
symbol3 = pow(theta3, (q - 1) // 5, q)
assert symbol3 != 1
print('Point-three marked H5 specialization:')
print(f'q={q}, zeta={zeta}, X={x3}, Theta={theta3}, fifth-power symbol={symbol3}')


def lift_fifth_root(value, initial, precision):
    root, k = initial, 1
    assert (pow(root, 5, q) - value) % q == 0
    while k < precision:
        k = min(2 * k, precision)
        modulus = q ** k
        root = (root - (pow(root, 5, modulus) - value)
                * pow(5 * pow(root, 4, modulus), -1, modulus)) % modulus
        assert (pow(root, 5, modulus) - value) % modulus == 0
    return root


precision = 6
modulus = q ** precision
zeta_lift = lift_fifth_root(1, zeta, precision)
X = q
t = q ** 5
Y = lift_fifth_root(1 - t, 1, precision)
Theta = 1
for i in range(5):
    Theta = Theta * pow((1 - pow(zeta_lift, i, modulus) * X) % modulus,
                        i, modulus) % modulus
Z = lift_fifth_root(Theta, 1, precision)
assert pow(X, 5, modulus) == t % modulus
assert pow(Y, 5, modulus) == (1 - t) % modulus
assert pow(Z, 5, modulus) == Theta
assert Y % q == Z % q == 1
print(f'Ordinary local point t=q^5 in the identical generic cover, modulo q^{precision}:')
print(f'zeta={zeta_lift}, X={X}, Y={Y}, Z={Z}')
print('All three fifth-root equations hold; unit derivatives give unique compatible Hensel lifts.')

H = list(product(range(5), repeat=3))


def mul(u, v):
    a, b, h = u
    c, d, k = v
    return ((a + c) % 5, (b + d) % 5, (h + k + a * d) % 5)


for c in range(1, 5):
    central = (0, 0, c)
    assert all(mul(central, u) == mul(u, central) for u in H)
    fixed = [u for u in H if mul(central, u) == u]
    assert not fixed
    print(f'Central translation {central}: {len(H)} sheets, {len(fixed)} fixed sheets')
print('PASS. This small local certificate is not claimed to satisfy the enormous A.66 CRT modulus.')
