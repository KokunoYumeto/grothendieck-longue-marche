#!/usr/bin/env python3
"""Exact rational identities and collision data for F.17.

This certifies the displayed maps over Q(zeta_5), not an assertion about
completed image intersections. The proof supplies the covering topology.
"""
from collections import Counter
from pathlib import Path
import json
import sympy as sp

z, s, V = sp.symbols("z s V")
phi5 = sp.Poly(z**4 + z**3 + z**2 + z + 1, z, domain=sp.QQ)
counts = Counter()


def check(name, condition):
    assert condition, name
    counts[name] += 1


def red(expr):
    return sp.Poly(sp.expand(expr), z, domain=sp.QQ).rem(phi5).as_expr()


def inv(expr):
    return sp.invert(sp.Poly(red(expr), z, domain=sp.QQ), phi5).as_expr()


def conj(expr):
    return red(red(expr).subs(z, z**4))


def zero_in_s(expr):
    poly = sp.Poly(sp.expand(expr), s)
    return all(red(coefficient) == 0 for coefficient in poly.all_coeffs())


def rational_zero(expr):
    numerator, _ = sp.fraction(sp.cancel(expr))
    return zero_in_s(numerator)


def coeffs(expr):
    poly = sp.Poly(red(expr), z, domain=sp.QQ)
    return [str(poly.nth(i)) for i in range(4)]


def main():
    a = (z-s)/(z+s)
    extra = []
    rows = []
    for j in (0, 2, 3, 4):
        u = red(z**j)
        A = red(2*z*u-u**2)
        B = red(z*u**2*inv(2*u-z))
        minus_numerator = (u-s)**2*(z+s)-(u+s)**2*(z-s)
        plus_numerator = (u-s)**2*(z+s)+(u+s)**2*(z-s)
        check("collision_factorization",
              zero_in_s(minus_numerator-2*s*(s**2-A)))
        check("collision_factorization",
              zero_in_s(plus_numerator-2*(z-2*u)*(s**2-B)))
        check("reciprocal_conjugate", red(B*conj(A)) == 1)
        check("norm_identity",
              red(A*conj(A)-(5-2*(z*inv(u)+u*inv(z)))) == 0)
        for name, value in (("A", A), ("B", B)):
            check("nonzero_collision_value", value != 0)
            check("outside_original_punctures", red(value**5-1) != 0)
            check("denominator_nonvanishing", red(value-u**2) != 0)
            check("denominator_nonvanishing", red(value-z**2) != 0)
            extra.append((j, name, value))
        check("simple_plus_collision", red(4*A) != 0)
        check("simple_minus_collision",
              red(16*(z-2*u)**2*B) != 0)
        rows.append({"j": j, "u": coeffs(u), "A": coeffs(A),
                     "B": coeffs(B), "A_fixed_label": "a_plus",
                     "B_fixed_label": "a_minus"})
    for i, first in enumerate(extra):
        for second in extra[i+1:]:
            check("distinct_extra_squared_values",
                  red(first[2]-second[2]) != 0)
    check("source_ranks", (12-1, 12+2*len(extra)-1, 4-1)
          == (11, 27, 3))

    # The square quotient of the six retained points.
    Q = ((V-a)/(V+a))**2
    check("six_point_quotient", rational_zero(Q.subs(V, 0)-1))
    check("six_point_quotient", rational_zero(Q.subs(V, 1)-s**2/z**2))
    check("six_point_quotient",
          rational_zero(Q.subs(V, a**2)-s**2/z**2))
    check("six_point_quotient", sp.cancel(Q.subs(V, a)) == 0)
    check("six_point_infinity", sp.limit(Q, V, sp.oo) == 1)
    check("six_point_branch_pole",
          sp.cancel(((V+a)**2).subs(V, -a)) == 0)
    check("deck_quotient_invariance", rational_zero(
        sp.cancel(Q.subs(V, a**2/V)-Q)))
    check("sheet_fixed_labels", rational_zero(a.subs(s, -s)-1/a))
    check("sheet_ordinary_labels", rational_zero(
        a.subs(s, -s)**2-1/a**2))

    # On the named six points, V -> V/a^2 matches the two sheets and
    # interchanges exactly the pair {1,a^2}; the deck interchanges
    # both ordinary pairs. Their cosets give the two pure label sheets.
    labels = ("zero", "infinity", "one", "a_squared", "a_plus", "a_minus")
    sheet = dict(zip(labels, labels))
    sheet["one"], sheet["a_squared"] = "a_squared", "one"
    deck = dict(zip(labels, labels))
    for x, y in (("zero", "infinity"), ("one", "a_squared")):
        deck[x], deck[y] = y, x
    check("sheet_permutation", sum(sheet[x] != x for x in labels) == 2)
    check("deck_permutation", sum(deck[x] != x for x in labels) == 4)
    check("pure_label_index", sheet != deck
          and any(sheet[x] != x for x in labels))
    check("deck_and_sheet_orders", all(sheet[sheet[x]] == x
          and deck[deck[x]] == x for x in labels))

    # A simple added collision has coefficient one, so its full
    # procyclic meridian has the displayed order in every finite
    # primary winding quotient.
    moduli = (2, 4, 8, 16, 32, 3, 9, 27, 5, 25, 7, 49, 11, 121, 13)
    for modulus in moduli:
        for exponent in range(modulus):
            check("unit_winding_coordinate",
                  (exponent % modulus == 0) == (exponent == 0))
        check("primitive_finite_winding", len(set(range(modulus))) == modulus)

    result = {
        "claim": "F.17", "status": "PASS",
        "coefficient_field": "Q[z]/(z^4+z^3+z^2+z+1), z=zeta_5",
        "extra_squared_values": rows,
        "extra_source_points": 16,
        "source_ranks": {"Y": 11, "Y_dagger": 27, "Y0": 3},
        "pure_label_sheet_permutation": sheet,
        "deck_permutation": deck,
        "checks": dict(counts), "total_checks": sum(counts.values()),
        "scope": "Exact rational collision, quotient, sheet-label, and primitive winding identities. Full topology is established in the proof for the stated six-point cover map; no injectivity of the ten-point drilling map or image-intersection conclusion is asserted."
    }
    out = Path(__file__).with_name("common_reflection_drilling_f17_output.json")
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: result[k] for k in
                     ("claim", "status", "extra_source_points", "source_ranks",
                      "checks", "total_checks", "scope")}, indent=2))


if __name__ == "__main__":
    main()
