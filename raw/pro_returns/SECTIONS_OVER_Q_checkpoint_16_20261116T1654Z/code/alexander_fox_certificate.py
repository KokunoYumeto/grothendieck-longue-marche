"""Exact symbolic checks for A.75.  The proof does not rely on sampling."""
import sympy as s

X, Y = s.symbols("X Y")
S, T = X - 1, Y - 1
partial = s.Matrix([[S, T]])
e = s.Matrix([-T, S])

def clean(z):
    return s.cancel(s.expand(z))

def eqzero(z):
    if isinstance(z, s.MatrixBase):
        assert all(clean(t) == 0 for t in z), z
    else:
        assert clean(z) == 0, z

def theta(z, alpha):
    return s.sympify(z).subs({X: X**alpha, Y: Y**alpha}, simultaneous=True)

def LX(a):
    return clean((X**a - 1) / S)

def LY(b):
    return clean((Y**b - 1) / T)

def jac(alpha, k):
    return s.Matrix([
        [LX(alpha), -T * (Y**alpha - 1) * k],
        [0, LY(alpha) + S * (Y**alpha - 1) * k],
    ])

def multiplier(alpha, k):
    return clean(LX(alpha) * LY(alpha)
                 + (X**alpha - 1) * (Y**alpha - 1) * k)

def vec(a, b):
    return s.Matrix([LX(a), X**a * LY(b)])

matrix_checks = 0
chain_checks = 0
gauge_checks = 0
defect_checks = 0

for alpha in (1, 2, 3, 5):
    for k in (0, 1, S, T, 1 + S - T):
        J = jac(alpha, k)
        F = multiplier(alpha, k)
        eqzero(partial * J - theta(partial, alpha))
        eqzero(J * theta(e, alpha) - F * e)
        eqzero(F.subs({X: 1, Y: 1}) - alpha**2)
        matrix_checks += 1

for alpha, beta in ((1, 2), (2, 1), (2, 3), (3, 2), (3, 3)):
    for kg, kh in ((0, 1), (1, 0), (S, T), (1 + T, S - T)):
        Fg = multiplier(alpha, kg)
        kgh = clean(kg + Fg * theta(kh, alpha))
        Jgh = jac(alpha * beta, kgh)
        eqzero(Jgh - jac(alpha, kg) * theta(jac(beta, kh), alpha))
        eqzero(multiplier(alpha * beta, kgh)
               - Fg * theta(multiplier(beta, kh), alpha))
        chain_checks += 1

for a in (-2, -1, 0, 1, 2):
    for b in (-2, -1, 0, 1, 2):
        u, w = X**a * Y**b, vec(a, b)
        eqzero(partial * w - s.Matrix([u - 1]))
        for d in (0, 1, S - T):
            wd = w + d * e
            K = u * s.eye(2) - wd * partial
            eqzero(partial * K - partial)
            eqzero(K * e - u * e)
            gauge_checks += 1

for alpha in (1, 2, 3):
    for ag, bg, ah, bh in ((0, 1, 1, 0), (1, 0, 0, 1),
                          (1, 1, 1, 1), (-1, 1, 1, -1)):
        for k in (0, 1, S - T):
            ug = X**ag * Y**bg
            v = (vec(ag, bg) + ug * jac(alpha, k)
                 * theta(vec(ah, bh), alpha)
                 - vec(ag + alpha * ah, bg + alpha * bh))
            eqzero(partial * v)
            omega = clean(v[1] / S)
            eqzero(v - omega * e)
            # Laurent-polynomial denominators may contain only X,Y,
            # never S or T: extraction introduces no nonintegral division.
            den = s.denom(omega)
            eqzero(den.subs({X: 1, Y: 1}) - 1)
            defect_checks += 1

print("A.75 exact completed Fox identities")
print("Matrix/boundary/Ihara multiplier checks:", matrix_checks)
print("Semilinear chain-rule composition checks:", chain_checks)
print("Inner-action gauge checks:", gauge_checks)
print("Full scalar-defect extraction checks:", defect_checks)
print("All exact symbolic identities passed.")
