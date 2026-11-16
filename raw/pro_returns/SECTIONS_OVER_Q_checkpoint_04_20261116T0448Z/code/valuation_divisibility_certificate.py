"""Exact residue divisibility for prime-dependent valuation exponents.

This verifies the mathematical residue bound used in the attempted
three-coefficient ghost induction.  It does not assert that the
global induction has been completed.
"""
from pathlib import Path
import sympy as s

q, m, n, t, alpha, beta, gamma, u, v, L = s.symbols(
    "q m n t alpha beta gamma u v L")
b2 = lambda x: x * (x - 1) / 2
eps = (q - 1) / 2
eta = (q * q - 1) / 24
Bq = lambda x: (q - 1) * ((2*q - 1)*x*x - 3*x) / 12
ZD = (m*gamma-q*(alpha+eps)*t-n*b2(alpha)
      +beta*b2(q*m)/q+eps*m*t+n*Bq(m))
ZF = (n*(gamma-alpha*beta)+q*(beta+eps)*(m*n-t)
      +m*b2(beta)-eta*n-alpha*b2(q*n)/q
      -eps*(m*n*n-n*t)-m*Bq(n))

negative_subs = {n:m, alpha:beta+(q-1)*(u+s.Rational(1,2)),
                 t:b2(m)-m*u}
negative = [s.factor(z.subs(negative_subs, simultaneous=True)) for z in (ZD,ZF)]
relation = (q-1)*t+alpha*n-beta*m-(q-1)*m*n/2
assert s.expand(relation.subs(negative_subs, simultaneous=True)) == 0
messages = ["Negative ordinary pattern satisfies the exact class-two tame relation."]

for name, value in zip(("D", "F"), negative):
    polynomial = s.Poly(s.cancel(value.subs(m,-24*L*(q*q-1)) / ((q*q-1)*L)),
                        q, beta, gamma, u, L)
    assert all(coefficient.q == 1 for coefficient in polynomial.coeffs())
    messages.append(f"Negative residue Z_{name}/((q^2-1)*L) has integral polynomial coefficients; {len(polynomial.terms())} terms.")
    messages.append(f"Exact factored negative Z_{name}/m = {s.factor(value/m)}")

positive_zero = {n:0, beta:(q-1)*v, t:m*v}
positive_one = {m:0, alpha:(q-1)*u, t:-n*u}
for label, substitutions, variable in (("positive x",positive_zero,m),
                                        ("positive 1-x",positive_one,n)):
    for name, value in zip(("D", "F"), (ZD,ZF)):
        polynomial = s.Poly(s.cancel(value.subs(substitutions, simultaneous=True)
                                     .subs(variable,24*L*(q*q-1)) / ((q*q-1)*L)),
                            q, alpha, beta, gamma, u, v, L)
        assert all(coefficient.q == 1 for coefficient in polynomial.coeffs())
        messages.append(f"{label}: Z_{name}/((q^2-1)*L) has integral polynomial coefficients.")

output = "\n".join(messages) + "\n"
Path(__file__).with_name("valuation_divisibility_certificate_output.txt").write_text(output)
print(output, end="")
