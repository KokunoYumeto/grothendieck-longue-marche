"""NOTES §34, main session (Claude Opus 5.5 at effort max), 16 Nov 2026. The two finite ends of S6_02's twelve-cycle.
E_j = C/(Z + kappa_j Z) (S6_02 A.1.2), kappa_1 = c + 1/2 - (3i/2pi) log 48, kappa_2 = c + 3/2 - (3i/pi) log 6 (S6_05 C.2.1),
w = e^{-pi i c} = r^6. Checks: (1) both E_j have Tate parameter e^{-2 pi i kappa_j} = const * r^12 (I_12 in r);
Alb(S_1) = E_1, Alb(S_2) = C/(Z + (kappa_2/2) Z) has parameter const * r^6 (I_6); (2) the ratio of the two I_12 parameters is
27/64, and d_* = kappa_1^part - kappa_2^part = -1 + (3i/2pi) log(3/4), Im d_* in (-0.2, -0.1) as certified in S6_02;
(3) the twelfth roots of the constants: (c2^2)^{1/12} * sqrt 6 and c1^{1/12} * 2 * 3^{1/4} are roots of unity;
(4) the Albanese maps on component labels: i -> 3i mod 12 and i -> 2i mod 6, with images of size 4 and 3 (R11)."""
from mpmath import mp, mpf, mpc, exp, log, pi, sqrt, fabs, im
mp.dps = 40
I = mpc(0, 1)
k1p = mpf(1) / 2 - 3 * I / (2 * pi) * log(48)
k2p = mpf(3) / 2 - 3 * I / pi * log(6)
for c in (mpc(0.3, -2.0), mpc(-1.7, -3.1)):
    w = exp(-pi * I * c); r = w ** (mpf(1) / 6)
    Q1 = exp(-2 * pi * I * (k1p + c)); Q2 = exp(-2 * pi * I * (k2p + c)); A2 = exp(-pi * I * (k2p + c))
    print("c =", c, " Q1/r^12 =", Q1 / r ** 12, " Q2/r^12 =", Q2 / r ** 12, " Alb2/r^6 =", A2 / r ** 6)
    print("   Q1/Q2 =", Q1 / Q2, " 27/64 =", mpf(27) / 64)
ds = k1p - k2p
print("d_* =", ds, " closed form -1 + (3i/2pi) log(3/4) =", -1 + 3 * I / (2 * pi) * log(mpf(3) / 4), " Im =", im(ds))
c1 = -mpf(1) / 48 ** 3; c2sq = (I / 216) ** 2
print("c1 =", c1, " c2^2 =", c2sq, " c1/c2^2 =", c1 / c2sq)
def rou(z, n=288):
    for k in range(1, n + 1):
        if fabs(z ** k - 1) < mpf(10) ** -30: return k
x2 = (c2sq ** (mpf(1) / 12)) * sqrt(6); x1 = (c1 ** (mpf(1) / 12)) * 2 * mpf(3) ** (mpf(1) / 4)
print("(c2^2)^(1/12) sqrt6 : |.| =", fabs(x2), " root of unity of order", rou(x2))
print("c1^(1/12) 2 3^(1/4) : |.| =", fabs(x1), " root of unity of order", rou(x1))
print("labels j=1: deck +4 orbits", sorted({frozenset((i + 4 * k) % 12 for k in range(3)) for i in range(12)}, key=min).__len__(),
      "; Albanese image of i -> 3i mod 12:", sorted({3 * i % 12 for i in range(12)}))
print("labels j=2: deck -3 orbits", sorted({frozenset((i - 3 * k) % 12 for k in range(4)) for i in range(12)}, key=min).__len__(),
      "; Albanese image of i -> 2i mod 6:", sorted({2 * i % 6 for i in range(12)}))
