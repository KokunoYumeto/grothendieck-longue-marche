"""NOTES §33 (b), main session (Claude Opus 5.5 at effort max), 16 Nov 2026. Exact arithmetic on S6's nomes in S6_02's
corner parameter r (w = r^6, u = w^2 = r^12): q1 = -w^2/48^3 (order-3 point), q2 = i w/216 (order-4 point), S6_05 C.2.1.
Checks with sympy: (1) q1 = (w/1728)^2 g_a(rho)^12 and q2 = (w/1728) g_b(i)^6 with g_a^12 = -27, g_b = -1 + i;
(2) q1/q2^2 = 27/64; (3) the twelfth root of q1/r^12 and the sixth root of q2/r^6: minimal polynomials over Q and
whether they lie in an abelian field (degree and Galois group of the splitting field of x^12 - c)."""
import sympy as sp

w, r = sp.symbols("w r")
I = sp.I
ga12 = sp.Integer(-27)
gb = -1 + I
q1 = -w**2 / 48**3
q2 = I * w / 216
print("(1)", sp.simplify(q1 - (w / 1728)**2 * ga12) == 0, sp.simplify(q2 - (w / 1728) * sp.expand(gb**6)) == 0, sp.expand(gb**6))
print("(2) q1/q2^2 =", sp.simplify(q1 / q2**2))
c1 = sp.simplify(q1.subs(w, r**6) / r**12)
c2 = sp.simplify(q2.subs(w, r**6) / r**6)
print("(3) q1 = c1 r^12 with c1 =", c1, "=", sp.factorrat(sp.Abs(c1)), "; q2 = c2 r^6 with c2 =", c2)
x = sp.symbols("x")
# c1^(1/12) = zeta_24 * 3^(1/4) / (2 sqrt 3) = zeta_24 * 3^(-1/4) / 2: its 4th power times 16 is -(-1)^(1/3)/3 ... check (2 c1^(1/12))^4 * 3 is a root of unity
z = sp.exp(I * sp.pi / 12) * sp.Rational(1, 2) * 3**sp.Rational(-1, 4)
print("    candidate c1^(1/12) = e^{pi i/12} 3^{-1/4}/2: z^12 - c1 =", sp.nsimplify(sp.expand(z**12 - c1)))
z2 = sp.exp(I * sp.pi / 12) / sp.sqrt(6)
print("    candidate c2^(1/6) = e^{pi i/12}/sqrt 6: z2^6 - c2 =", sp.simplify(sp.expand(z2**6) - c2))
print("    r0 = (3/4)^(1/4) and (q1/q2^2)^(1/12):", sp.simplify((sp.Rational(27, 64))**sp.Rational(1, 12) - (sp.Rational(3, 4))**sp.Rational(1, 4)) == 0)
