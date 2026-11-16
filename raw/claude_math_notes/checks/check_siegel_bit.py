"""NOTES §30 (j), main session (Claude Opus 5.5 at effort max), 16 Nov 2026. F16, S6 side.
Siegel function (Kubert-Lang): g_a(tau) = -q^{B2(a1)/2} e^{2 pi i a2 (a1 - 1)/2} (1 - q_z) prod_{n>=1} (1 - q^n q_z)(1 - q^n/q_z),
q = e^{2 pi i tau}, z = a1 tau + a2, q_z = e^{2 pi i z}, B2(x) = x^2 - x + 1/6. The archimedean Neron function is
lambda = -log|g_a(tau)|, so S6's N = e^lambda = 1/|g_a|.
Test: at tau = rho = e^{2 pi i/3}, a = the fixed point of z -> rho z of order 3, and at tau = i, a = (1/2, 1/2):
(1) |g| = 3^{-1/4} and 2^{-1/2} (S6's N(z1) = 3^{1/4}, N(z2) = sqrt 2);
(2) is g_a(rho)^2 * sqrt(-3) a root of unity (then g_a(rho) = zeta * (sqrt -3)^{-1/2}, which generates Q^ab(3^{1/4}) over
    Q^ab); is g_a(i) * (1 + i) a root of unity (then g_a(i) is abelian)."""
from mpmath import mp, mpf, mpc, exp, pi, sqrt, log, fabs, arg, nint

mp.dps = 50
I = mpc(0, 1)


def siegel(a1, a2, tau, terms=200):
    q = exp(2 * pi * I * tau)
    z = a1 * tau + a2
    qz = exp(2 * pi * I * z)
    B2 = a1 * a1 - a1 + mpf(1) / 6
    val = -exp(2 * pi * I * tau * B2 / 2) * exp(2 * pi * I * a2 * (a1 - 1) / 2) * (1 - qz)
    for n in range(1, terms):
        val *= (1 - q ** n * qz) * (1 - q ** n / qz)
    return val


def root_of_unity_order(w, maxn=144):
    for n in range(1, maxn + 1):
        if fabs(w ** n - 1) < mpf(10) ** (-30):
            return n
    return None


rho = exp(2 * pi * I / 3)
# fixed points of z -> rho z on C/(Z + Z rho): (1 - rho) z in the lattice; z = (1 - rho)/3 = a1 rho + a2 with a1 = -1/3, a2 = 1/3
for (a1, a2) in [(mpf(2) / 3, mpf(1) / 3), (mpf(1) / 3, mpf(2) / 3)]:
    z = a1 * rho + a2
    print("rho-point a =", (float(a1), float(a2)), " (1 - rho) z =", (1 - rho) * z)
    g = siegel(a1, a2, rho)
    print("  |g| =", fabs(g), " 3^{-1/4} =", mpf(3) ** (-0.25))
    w = g ** 2 * sqrt(mpc(-3, 0))
    print("  g^2 sqrt(-3) =", w, " |.| =", fabs(w), " root of unity of order", root_of_unity_order(w))
    w12 = g ** 12
    print("  g^12 =", w12, " |g^12| * 27 =", fabs(w12) * 27)

for (a1, a2) in [(mpf(1) / 2, mpf(1) / 2)]:
    tau = I
    z = a1 * tau + a2
    print("i-point a =", (float(a1), float(a2)), " (1 - i) z =", (1 - I) * z)
    g = siegel(a1, a2, tau)
    print("  |g| =", fabs(g), " 2^{-1/2} =", 1 / sqrt(2))
    w = g * (1 + I)
    print("  g (1 + i) =", w, " root of unity of order", root_of_unity_order(w))
