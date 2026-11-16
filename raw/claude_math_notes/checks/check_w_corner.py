"""Checks for the note on S6's w -> 0 and the j = 0 point (16 Nov 2026).
1. K = t^4/(t-1)^3 with t = j/1728 equals E4^12/(1728 E6^6 Delta); y = K^(1/12) = 1728^(-1/12) E4/(eta^2 sqrt(E6)).
2. Near the LG point, |y| / |t_H| -> 2, with t_H the Hesse coordinate (j = 27 t^3 (8-t^3)^3/(1+t^3)^3).
3. Im beta_part(z) = (6/pi) log|theta1(z,tau)/eta(tau)| - (1/pi) log 1728 at the two CM points reproduces S6_05 C.1.3.
4. 48^3 = 1728^2/3^3 and 216 = 1728/2^3."""
from mpmath import mp, mpf, mpc, exp, pi, log, sqrt, jtheta, findroot
mp.dps = 40
I = mpc(0, 1)

def q_of(tau): return exp(2*pi*I*tau)
def eta(tau):
    q = q_of(tau); s = mpf(1)
    for n in range(1, 400): s *= (1 - q**n)
    return exp(pi*I*tau/12)*s
def E4(tau):
    q = q_of(tau); return 1 + 240*sum(n**3*q**n/(1-q**n) for n in range(1, 400))
def E6(tau):
    q = q_of(tau); return 1 - 504*sum(n**5*q**n/(1-q**n) for n in range(1, 400))

tau = mpc(mpf('0.13'), mpf('1.21'))
e4, e6, et = E4(tau), E6(tau), eta(tau)
Delta = et**24
j = e4**3/Delta
t = j/1728
K1 = t**4/(t-1)**3
K2 = e4**12/(1728*e6**6*Delta)
print("1. K via t vs via E4,E6,Delta: rel.err", abs(K1-K2)/abs(K1))
print("   check Delta = (E4^3-E6^2)/1728:", abs(Delta - (e4**3-e6**2)/1728)/abs(Delta))

# 2. near the LG point: t_H small, y^12 = K(t(t_H))
for th in [mpf('1e-2'), mpf('1e-3')]:
    jj = 27*th**3*(8-th**3)**3/(1+th**3)**3
    tt = jj/1728
    KK = tt**4/(tt-1)**3
    print("2. t_H =", th, " |y|/|t_H| =", abs(KK)**(mpf(1)/12)/th)

# 3. Neron-type values at the CM points (theta1 with period 1: theta1(pi z | tau) in mpmath's nome convention)
def theta1_over_eta(z, tau):
    nome = exp(pi*I*tau)
    return jtheta(1, pi*z, nome)/eta(tau)
rho = exp(pi*I/3)
for name, tau0, z, T6 in [("z1", rho, (2-rho)/3, None), ("z2", I, (1-I)/2, None)]:
    v = theta1_over_eta(z, tau0)
    Im_beta = (6/pi)*log(abs(v)) - log(1728)/pi
    N = abs(v)*exp(-pi*z.imag**2/tau0.imag)
    print("3.", name, "|theta1/eta| =", mp.nstr(abs(v), 20), " N =", mp.nstr(N, 20), " (6/pi)log|th/eta| - log(1728)/pi =", mp.nstr(Im_beta, 25))
print("   S6_05 C.1.3: Im beta_part(z1) = -1.27101206057537346286579673538, Im beta_part(z2) = -0.21100425815613411418178314271")
print("4.", 48**3, 1728**2//27, 1728**2 % 27, "|", 216, 1728//8)
