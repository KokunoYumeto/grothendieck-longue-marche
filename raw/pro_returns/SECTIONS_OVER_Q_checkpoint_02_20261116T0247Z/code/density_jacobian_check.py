"""Exact certificates for the D1 density audit (Python 3 + SymPy).

The proofs for all primes are in notes/density_jacobian_counterexamples.md.
This script verifies the algebraic morphisms and representative finite-field
counts; it makes no numerical inference about Dirichlet densities.
"""

import sympy as sp

x, a, u, T = sp.symbols("x a u T")
f = u**3 + a*u**2 + a*u + 1
F = x**6 + 2*a*x**4 + 4*a*x**2 + 8
assert sp.expand(F/8 - f.subs(u, x**2/2)) == 0
assert sp.expand(F/x**6 - f.subs(u, 2/x**2)) == 0
assert sp.factor(sp.discriminant(f, u)) == (a-3)**3*(a+1)
assert sp.factor(sp.discriminant(F, x)) != 0
print("Morphism identities: 2(y/4)^2=f(x^2/2), (y/x^3)^2=f(2/x^2).")
print("Pullback differential coefficients in basis (dx/y,x dx/y): (0,4),(-4,0).")
print("Discriminant of sextic:", sp.factor(sp.discriminant(F, x)))

def invariants(a2, a4, a6):
    b2, b4, b6, b8 = 4*a2, 2*a4, 4*a6, 4*a2*a6-a4*a4
    c4 = b2*b2-24*b4
    delta = -b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
    return c4, delta

for av in (0, 4):
    c4, delta = invariants(av, av, 1)
    assert delta == 16*(av-3)**3*(av+1)
    assert c4 == 16*av*(av-3)
    print(f"E_{av}: c4={c4}, Delta={delta}; v5(Delta)={'1' if av==4 else '0'}.")

def chi(n, p):
    r = pow(int(n) % p, (p-1)//2, p)
    return -1 if r == p-1 else r

def elliptic_trace(p, av):
    return -sum(chi(z**3+av*z*z+av*z+1, p) for z in range(p))

def genus2_trace(p, av):
    # The monic, squarefree sextic has two rational points at infinity.
    return -1-sum(chi(z**6+2*av*z**4+4*av*z*z+8, p) for z in range(p))

primes = list(sp.primerange(7, 401))
for p in primes:
    for av in (0, 4):
        assert genus2_trace(p, av) == (1+chi(2, p))*elliptic_trace(p, av)
inert = [p for p in primes if chi(2, p) == -1]
print("All", 2*len(primes), "genus-two/elliptic trace identities checked at 7 <= p < 401.")
print("p, a_p(E_4), a_p(E_0), a_p(J_4), a_p(J_0), T^2 coefficient of P(J_4), T^2 coefficient of P(J_0)")
for p in inert[:15]:
    b, g = elliptic_trace(p, 4), elliptic_trace(p, 0)
    assert genus2_trace(p, 4) == genus2_trace(p, 0) == 0
    print(p, b, g, 0, 0, 2*p-b*b, 2*p-g*g, sep=",")

def cm_i_trace(p):
    return -sum(chi(z**3-z, p) for z in range(p))

def cm_3_trace(p):
    return -sum(chi(z**3+1, p) for z in range(p))

assert cm_i_trace(5) == -2
assert cm_3_trace(5) == 0
for p in sp.primerange(5, 401):
    if p % 12 == 11:
        assert cm_i_trace(p) == cm_3_trace(p) == 0
print("CM elliptic trace zero verified for all p<401, p=11 mod12.")
print("At5: P_i(T)=T^2+2T+5, P_3(T)=T^2+5.")
print("Ratio of roots of P_i = (-3-4i)/5 is not a root of unity in Q(i).")
print("Ratio of roots of P_3 = -1; no positive Frobenius powers can be conjugate.")
print("PASS")
