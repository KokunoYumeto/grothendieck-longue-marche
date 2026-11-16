#!/usr/bin/env python3
"""Local exact arithmetic on six literal genus-two Fermat-eight quotients."""
from pathlib import Path
from math import gcd
import json
import sympy as sp

BASE = Path(__file__).resolve().parent
X, x, y, u, v, z = sp.symbols("X x y u v z")
primes = [5, 7, 11, 13, 17, 19, 23, 29, 31]
families = [(3, -2, 1), (6, 3, 3), (6, -2, 2),
            (24, 1, 5), (3, 1, 2), (-8, 9, 1)]

def legendre(a, p):
    a %= p
    if not a:
        return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1

def valuation(n, ell):
    v = 0
    while n % ell == 0:
        n //= ell
        v += 1
    return v

def counts(A, B, p):
    assert (2*A*B) % p
    d = next(d for d in range(2, p) if legendre(d, p) == -1)
    n1 = p+1+sum(legendre(A*a**5+B*a, p) for a in range(p))
    def mul(a, b):
        return ((a[0]*b[0]+d*a[1]*b[1]) % p,
                (a[0]*b[1]+a[1]*b[0]) % p)
    total = 0
    for a in range(p):
        for b in range(p):
            xx = (a, b)
            xx2 = mul(xx, xx)
            xx5 = mul(mul(xx2, xx2), xx)
            fa, fb = (A*xx5[0]+B*a) % p, (A*xx5[1]+B*b) % p
            total += legendre(fa*fa-d*fb*fb, p)
    n2 = p*p+1+total
    tr = p+1-n1
    a2 = (n2-p*p-1+tr*tr)//2
    frob = X**4-tr*X**3+a2*X**2-p*tr*X+p*p
    order = int(frob.subs(X, 1))
    assert order == (n1*n1+n2)//2-p
    return {
        "p": p, "quadratic_nonresidue": d, "curve_points": n1,
        "curve_points_over_quadratic": n2, "jacobian_order": order,
        "frobenius_polynomial": str(frob),
        "frobenius_irreducible": sp.Poly(frob, X).is_irreducible,
    }

out = []
for A, B, yp in families:
    f = A*x**5+B*x
    assert A+B == yp*yp
    disc = int(sp.discriminant(f, x))
    assert set(sp.factorint(abs(disc))).issubset({2, 3})
    rows = [counts(A, B, p) for p in primes]
    possible_ells = set()
    for row in rows:
        possible_ells.update(sp.factorint(row["jacobian_order"]))
    torsion_bound = 1
    for ell in possible_ells:
        e = min(valuation(row["jacobian_order"], ell)
                for row in rows if row["p"] != ell)
        torsion_bound *= ell**e
    assert torsion_bound == 2
    # Literal Mumford doubling of [(1,yp)-infinity].
    uu = (x-1)**2
    vv = yp+sp.Rational(5*A+B, 2*yp)*(x-1)
    assert sp.rem(f-vv**2, uu, x) == 0
    assert sp.degree(uu, x) == 2
    # A further exact doubling: the formal square root mod (x-1)^4.
    coefficients = [sp.Rational(yp)]
    t = sp.symbols("t")
    ft = sp.Poly(f.subs(x, 1+t), t)
    for k in range(1, 4):
        previous = sum(coefficients[i]*coefficients[k-i]
                       for i in range(1, k))
        coefficients.append((ft.nth(k)-previous)/(2*yp))
    vv4 = sp.expand(sum(coefficients[i]*(x-1)**i for i in range(4)))
    uu4 = (x-1)**4
    assert sp.rem(f-vv4**2, uu4, x) == 0
    unred = sp.div(f-vv4**2, uu4, x)[0]
    ured = sp.Poly(unred, x).monic().as_expr()
    vred = sp.rem(-vv4, ured, x)
    assert sp.rem(f-vred**2, ured, x) == 0
    assert sp.degree(ured, x) == 2
    data = {
        "A": A, "B": B, "point": [1, yp],
        "curve": str(f), "discriminant": disc,
        "finite_field_counts": rows,
        "rational_torsion_order_bound": torsion_bound,
        "twice_point_mumford": [str(uu), str(vv)],
        "four_times_point_mumford": [str(ured), str(vred)],
        "irreducible_good_frobenius_primes":
            [row["p"] for row in rows if row["frobenius_irreducible"]],
    }
    out.append(data)
    chosen = 13 if (A, B) in [(3, -2), (24, 1)] else 5
    chosen_row = next(row for row in rows if row["p"] == chosen)
    assert chosen_row["frobenius_irreducible"]
    assert sp.sympify(chosen_row["frobenius_polynomial"]) == X**4+chosen**2
    print("CURVE y^2 =", f, "POINT (1,", yp, ")")
    print("GOOD ORDERS", [(r["p"], r["jacobian_order"]) for r in rows])
    print("RATIONAL TORSION ORDER BOUND", torsion_bound)
    print("2P =", uu, ",", vv)
    print("4P =", ured, ",", vred)
    print("IRREDUCIBLE FROBENIUS PRIMES",
          data["irreducible_good_frobenius_primes"])

# Literal maps from 3u^8-2v^8=1 to the three hyperelliptic curves:
# (u/v,1/v^4), (v,3u^4), (u,2v^4).
relation = 3*u**8-2*v**8-1
maps = [
    (3, -2, u/v, 1/v**4, -1/v**8),
    (6, 3, v, 3*u**4, 3),
    (6, -2, u, 2*v**4, -2),
    (24, 1, u*v, 3*u**8+2*v**8, 3*u**8-2*v**8+1),
    (3, 1, u/v**2, (3*u**8+1)/(2*v**8),
     (3*u**8-1+2*v**8)/(4*v**16)),
    (-8, 9, v/u**2, (2*v**8-1)/u**8,
     -(3*u**8+2*v**8+1)/u**16),
]
for A, B, xx, yy, quotient in maps:
    residual = sp.factor(yy**2-A*xx**8-B)
    assert not sp.cancel(residual-quotient*relation)
    # C8 -> genus two: (X,Y)=(x^2,xy).
    assert sp.expand((x*y)**2-(A*(x*x)**5+B*x*x)
                     - x*x*(y*y-A*x**8-B)) == 0
print("PASS: all six literal Fermat-to-hyperelliptic and genus-two maps")
(BASE/"point3_fermat8_genus2_certificate_data.json").write_text(
    json.dumps({"families": out, "scope": "Exact local computation only."},
               indent=2)+"\n")
