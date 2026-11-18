"""Exact, characteristic-zero Legendre Picard-Fuchs/Schwarzian check.

Run MPL_93_092-134/integral_schwarzian_check.
GPT-6 Astra Pro (inherited); effort setting not exposed.
This script checks rational identities, not a formalized de Rham theorem.
"""

import sympy as sp

x, z = sp.symbols("x z")
f = x * (x - 1) * (x - z)
g = x * (x - 1)
h = x - z

# For omega=dx/y and y^2=f, the parameter derivatives divided by omega.
omega_z = -sp.diff(f, z) / (2 * f)
omega_zz = sp.diff(omega_z, z) + omega_z**2
assert sp.cancel(omega_z - 1 / (2 * h)) == 0
assert sp.cancel(omega_zz - sp.Rational(3, 4) / h**2) == 0

# Primitive R/y = y/(2h^2). Its x differential divided by omega.
R = g / (2 * h)
primitive_dx = sp.diff(R, x) - R * sp.diff(f, x) / (2 * f)
L_omega = z * (1 - z) * omega_zz + (1 - 2 * z) * omega_z - sp.Rational(1, 4)
exact_remainder = sp.cancel(L_omega - primitive_dx)
assert exact_remainder == 0
print("omega_z / omega =", sp.factor(omega_z))
print("omega_zz / omega =", sp.factor(omega_zz))
print("L omega / omega =", sp.factor(L_omega))
print("L omega - d_x[y/(2(x-z)^2)], divided by omega:", exact_remainder)

P = (1 - 2 * z) / (z * (1 - z))
Q = -sp.Rational(1, 4) / (z * (1 - z))
mu = sp.factor(2 * sp.diff(P, z) + P**2 - 4 * Q)
three_cusp = -(z**2 - z + 1) / (z**2 * (z - 1)**2)
mu_remainder = sp.cancel(mu - three_cusp)
assert mu_remainder == 0
print("P =", sp.factor(P))
print("Q =", sp.factor(Q))
print("mu = 2P' + P^2 - 4Q =", mu)
print("Difference from root's three-cusp coefficient:", mu_remainder)
print("All identities exact over Q(x,z); period/Gauss-Manin interpretation is explained in legendre_comparison.md.")
