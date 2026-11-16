"""NOTES §33 (a), main session (Claude Opus 5.5 at effort max), 16 Nov 2026. Exact proof of the Siegel values of §30 (j).
Claim: for a = (2/3, 1/3) and every tau, g_a(tau)^12 = Delta(tau) / P'(z_a)^4, where z_a = a1 tau + a2, P = Weierstrass
function of the lattice Z tau + Z, Delta = (2 pi)^12 q prod (1 - q^n)^24 = g2^3 - 27 g3^2. (Reason: g_a = k_a Delta^{1/12},
k_{2a}/k_a^4 = sigma(2z)/sigma(z)^4 = -P'(z), and k_{2a} = k_{-a+(2,1)} = eps(-a,(2,1)) k_{-a} = (-1)(-k_a) = k_a.)
At tau = rho, g2 = 0 and the order-3 fixed point has P(z_a) = 0, so P'(z_a)^2 = -g3 and g_a(rho)^12 = -27 g3^2 / g3^2 = -27.
Test the identity at generic tau (this checks the root of unity eps = 1), then at rho."""
from mpmath import mp, mpf, mpc, exp, pi, diff

mp.dps = 40
I = mpc(0, 1)


def siegel(a1, a2, tau, terms=400):
    q = exp(2 * pi * I * tau); z = a1 * tau + a2; qz = exp(2 * pi * I * z)
    B2 = a1 * a1 - a1 + mpf(1) / 6
    v = -exp(2 * pi * I * tau * B2 / 2) * exp(2 * pi * I * a2 * (a1 - 1) / 2) * (1 - qz)
    for n in range(1, terms):
        v *= (1 - q ** n * qz) * (1 - q ** n / qz)
    return v


def wp(z, tau, terms=400):
    q = exp(2 * pi * I * tau); u = exp(2 * pi * I * z)
    s = mpf(1) / 12 + u / (1 - u) ** 2
    for n in range(1, terms):
        s += q ** n * u / (1 - q ** n * u) ** 2 + q ** n / u / (1 - q ** n / u) ** 2 - 2 * q ** n / (1 - q ** n) ** 2
    return (2 * pi * I) ** 2 * s


def Delta(tau, terms=400):
    q = exp(2 * pi * I * tau); p = q
    for n in range(1, terms):
        p *= (1 - q ** n) ** 24
    return (2 * pi) ** 12 * p


a1, a2 = mpf(2) / 3, mpf(1) / 3
for tau in [mpc(mpf("0.1"), mpf("1.3")), mpc(mpf("-0.37"), mpf("0.91")), exp(2 * pi * I / 3)]:
    z = a1 * tau + a2
    dP = diff(lambda t: wp(t, tau), z)
    r = siegel(a1, a2, tau) ** 12 * dP ** 4 / Delta(tau)
    print("tau =", mp.nstr(tau, 6), " g^12 P'^4 / Delta =", mp.nstr(r, 25))
rho = exp(2 * pi * I / 3)
print("P(z_a) at rho:", mp.nstr(wp(a1 * rho + a2, rho), 10), "  g_a(rho)^12 =", mp.nstr(siegel(a1, a2, rho) ** 12, 30))
