"""NOTES §30 (b), main session (Claude Opus 5.5 at effort max), 16 Nov 2026. Checks, to 40 digits:
(1) on E3: y^2 = x^3 + 1 the point P = (sqrt3 - 1, (sqrt3 - 1) sqrt3 r0), r0 = (3/4)^(1/4), has 2P = (-1, 0), so it is
    a 4-torsion point and Q^ab(E3[4]) = Q^ab(r0) (x^3 = 6 sqrt3 - 10 is a root of the 4-division factor x^6 + 20x^3 - 8);
(2) r0 = N(z1)/N(z2) with S6's Neron values N(z1) = 27^(1/12) = 3^(1/4) and N(z2) = 8^(1/6) = sqrt2
    (|q1| = |w|^2 N(z1)^12/1728^2 = |w|^2/48^3, |q2| = |w| N(z2)^6/1728 = |w|/216);
(3) r0^12 = 216^2/48^3 = 27/64, S6's nome ratio q1/q2^2."""
from mpmath import mp, mpf, sqrt

mp.dps = 40
r0 = (mpf(3) / 4) ** (mpf(1) / 4)
x = sqrt(3) - 1
y = sqrt(x ** 3 + 1)
print("x^6 + 20x^3 - 8 =", x ** 6 + 20 * x ** 3 - 8)
print("y - (sqrt3 - 1) sqrt3 r0 =", y - (sqrt(3) - 1) * sqrt(3) * r0)
lam = 3 * x ** 2 / (2 * y)
print("x(2P) =", lam ** 2 - 2 * x, "(expected -1)")
N1 = (mpf(1728) ** 2 / mpf(48) ** 3) ** (mpf(1) / 12)
N2 = (mpf(1728) / 216) ** (mpf(1) / 6)
print("N1 - 3^(1/4) =", N1 - mpf(3) ** (mpf(1) / 4), "  N2 - sqrt2 =", N2 - sqrt(2))
print("N1/N2 - r0 =", N1 / N2 - r0)
print("216^2/48^3 - r0^12 =", mpf(216) ** 2 / mpf(48) ** 3 - r0 ** 12, "  r0^12 =", r0 ** 12)
