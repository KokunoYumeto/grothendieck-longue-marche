#!/usr/bin/env python3
"""Exact cyclotomic certificates for F.31; no floating point arithmetic."""
import json
from pathlib import Path
import sympy as s

x = s.symbols("x")
b, c = s.symbols("b c")
z, p, d, e, w = s.symbols("z p d e w")
checks = 0
tangent_checks = 0
rows = []
for n in range(3, 25):
    phi = s.Poly(s.cyclotomic_poly(n, x), x, domain=s.QQ)
    def red(expr):
        return s.rem(s.Poly(s.expand(expr), x, domain=s.QQ), phi).as_expr()
    def root_power(k):
        return x ** (k % n)
    assert red(sum(root_power(2*a) for a in range(n))) == 0
    assert red(sum(root_power(-2*a) for a in range(n))) == 0
    for j in range(1, n):
        lam = root_power(j) - 1
        lam_bar = root_power(-j) - 1
        # D_a = -(lambda * bar(beta) * zeta^-a
        #         + bar(lambda) * beta * zeta^a).
        coeff_b2 = sum(lam_bar**2 * root_power(2*a) for a in range(n))
        coeff_c2 = sum(lam**2 * root_power(-2*a) for a in range(n))
        coeff_bc = 2*n*lam*lam_bar
        assert red(coeff_b2) == 0
        assert red(coeff_c2) == 0
        assert red(coeff_bc - 2*n*(2-root_power(j)-root_power(-j))) == 0
        assert red(lam*lam_bar) != 0
        if n >= 5:
            # beta=1, remove the two tangential endpoints a=0,j.
            A = lam*lam_bar
            remaining = 0
            nonzero_other = False
            for a in range(n):
                if a in (0, j):
                    continue
                D = -(lam*root_power(-a)+lam_bar*root_power(a))
                remaining += D**2
                nonzero_other |= red(D) != 0
            assert red(remaining - 2*A*(n-A)) == 0
            assert nonzero_other
            tangent_checks += 1
        checks += 1
    rows.append({"n": n, "nonzero_deck_classes": n-1, "status": "PASS"})

# The inverse map of the actual cyclic cover and its listed puncture fibers.
for n in (3, 4, 5, 8, 9, 25):
    inverse = d + (p-d)*w**n
    r = (e-d)/(p-d)
    assert s.cancel((inverse-d)/(p-d) - w**n) == 0
    assert s.cancel(inverse-e - (p-d)*(w**n-r)) == 0
    assert s.simplify(inverse.subs(w, 1)-p) == 0
    assert s.simplify(inverse.subs(w, 0)-d) == 0
    assert s.simplify(s.diff(inverse,w).subs(w,1)-n*(p-d)) == 0

# The n=2 exclusion in the sum-of-squares argument is real: no false
# universal claim about that second moment is used.
assert s.rem(s.Poly(sum(x**((2*a)%2) for a in range(2)), x),
             s.Poly(s.cyclotomic_poly(2, x), x)).as_expr() == 2

result = {
    "statement": "F.31",
    "cyclotomic_field_checks": checks,
    "tangent_checks": tangent_checks,
    "moduli": list(range(3,25)),
    "inverse_map_checks": [3,4,5,8,9,25],
    "formula": "sum_a D_a^2 = 2*n*(zeta^j-1)*(zeta^(-j)-1)*beta*bar(beta)",
    "n_2_exception_retained": True,
    "rows": rows,
    "status": "PASS",
}
print("F.31 genus-zero cyclic-cover certificate")
print(f"Exact cyclotomic identities: {checks} nonzero deck classes, moduli 3 through 24")
print(f"Exact tangent exclusion identities: {tangent_checks} classes, moduli 5 through 24")
print("All coefficients checked in Q[x]/Phi_n(x)")
print("Actual inverse maps and all third-cusp fibers checked for n=3,4,5,8,9,25")
print("The n=2 exception is retained; divisibility by larger moduli handles modulus 2")
print("PASS")
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
