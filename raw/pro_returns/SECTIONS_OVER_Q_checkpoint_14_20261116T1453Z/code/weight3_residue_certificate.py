"""Strict weight-three residue identities for the actual class-two lift.

This computes psi(W_D), psi(W_F) symbolically, verifies the exact
weight-two tame relation, and checks the two ordinary nonnegative
valuation reductions.  No division by q^2-1 is imposed by the program.
"""
import sympy as s

q = s.symbols("q", integer=True, positive=True)
j = s.symbols("j", integer=True)
alpha, beta, gamma, m, n, t, eta = s.symbols("alpha beta gamma m n t eta")
u, v, z = s.symbols("u v z")


def b2(x):
    return x*(x-1)/2


def W(g, h):
    chi, a, b, hh, ff = g
    _, aa, bb, hhh, _ = h
    eps = (chi-1)/2
    return (-(a+eps)*chi**2*hhh-b2(a)*chi*bb,
            (b+eps)*chi**2*(aa*bb-hhh)+b2(b)*chi*aa-ff*chi*bb)


Phi = (q, alpha, beta, gamma, eta)
Tau = (s.Integer(1), m, n, t, s.Integer(0))
PhiTau = (q, alpha+q*m, beta+q*n, gamma+q**2*t+alpha*q*n, eta)
PhiInv = (1/q, -alpha/q, -beta/q, (alpha*beta-gamma)/q**2,
          -eta/q**2)
Tau_j = (s.Integer(1), j*m, j*n, j*t+b2(j)*m*n, s.Integer(0))
terms = [W(Phi,Tau), W(PhiTau,PhiInv), W(Phi,PhiInv), W(Tau_j,Tau)]
raw = [s.simplify((terms[0][i]+terms[1][i]-terms[2][i]
                  -s.summation(terms[3][i], (j,1,q-1)))/q)
       for i in range(2)]


def Bq(x):
    return (q-1)*((2*q-1)*x**2-3*x)/12


eps = (q-1)/2
Z_D = (m*gamma-q*(alpha+eps)*t-n*b2(alpha)
       +beta*b2(q*m)/q+eps*m*t+n*Bq(m))
Z_F = (n*(gamma-alpha*beta)+q*(beta+eps)*(m*n-t)+m*b2(beta)-eta*n
       -alpha*b2(q*n)/q-eps*(m*n**2-n*t)-m*Bq(n))
assert all(s.expand(r-z0) == 0 for r,z0 in zip(raw,(Z_D,Z_F)))
print("Both full strict residue formulas agree identically with psi(W_D), psi(W_F).")

# The class-two tame group relation has defect q times this expression.
class2_relation = (q-1)*t+alpha*n-beta*m-(q-1)*m*n/2
h_PhiTauPhiInv = q**2*t+q*(alpha*n-beta*m)
h_Tau_q = q*t+b2(q)*m*n
assert s.expand(h_PhiTauPhiInv-h_Tau_q-q*class2_relation) == 0
print("Class-two tame relation: (q-1)t + alpha*n - beta*m - (q-1)m*n/2 = 0.")

case_zero = {n:0, beta:(q-1)*v, t:m*v}
reduced_zero = (m*(gamma-q*alpha*v)+(q**2-1)*b2(m)*v,
                -(q**2-1)*m*b2(v+1))
for full, reduced in zip((Z_D,Z_F), reduced_zero):
    assert s.expand(full.subs(case_zero, simultaneous=True)-reduced) == 0
print("At a positive x-valuation: Z_D=m(gamma-q*alpha*v)+(q^2-1)binom(m,2)v;")
print("                         Z_F=-(q^2-1)m*binom(v+1,2).")

case_one = {m:0, alpha:(q-1)*u, t:-n*u}
reduced_one = ((q**2-1)*n*b2(u+1),
               n*(gamma+beta*u-eta)-(q**2-1)*b2(n)*u)
for full, reduced in zip((Z_D,Z_F), reduced_one):
    assert s.expand(full.subs(case_one, simultaneous=True)-reduced) == 0
print("At a positive (1-x)-valuation: Z_D=(q^2-1)n*binom(u+1,2);")
print("                             Z_F=n(gamma+beta*u-eta)-(q^2-1)binom(n,2)u.")

for full, expected in zip((Z_D,Z_F), (m*z,n*z)):
    assert s.expand(full.subs(gamma,gamma+z)-full-expected) == 0
    assert s.expand(full.subs({m:0,n:0,t:0}, simultaneous=True)) == 0
print("An unramified central shift gamma -> gamma+z changes the family by (m*z,n*z).")
print("Both coordinates vanish exactly as cochains when m=n=t=0.")

# Finite integer-value samples audit denominator integrality at ell=2,3
# for B_q, with q always a different prime from the coefficient prime.
checks = 0
for qq in (2,3,5,7,11,13,17,19):
    for zz in range(-20,21):
        direct = sum(s.Integer(jj*zz)*(jj*zz-1)/2 for jj in range(1,qq))/qq
        closed = Bq(s.Integer(zz)).subs(q,qq)
        assert direct == closed
        for ell in (2,3,5,7):
            if ell != qq:
                assert s.denom(direct) % ell != 0
                checks += 1
print(f"B_q integer-value and allowed-denominator checks: {checks} passed.")
