#!/usr/bin/env python3
"""Exact certificates for the profinite metabelian involution in A.22.

The 75-element quotient is constructed independently of GAP.
Finite Haar idempotent checks illustrate, but do not replace, the
inverse-limit construction proved in the manuscript.
"""
from collections import deque
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def finite_quotient():
    # F_25 = F_5[z]/(z^2+z+1); pairs encode a+b*z.
    field = list(product(range(5), repeat=2))
    zero, one, zeta = (0, 0), (1, 0), (0, 1)
    def add(v, w):
        return ((v[0] + w[0]) % 5, (v[1] + w[1]) % 5)
    def neg(v):
        return ((-v[0]) % 5, (-v[1]) % 5)
    def mul(v, w):
        a, b = v
        c, d = w
        return ((a*c-b*d) % 5, (a*d+b*c-b*d) % 5)
    def inv(v):
        assert v != zero
        return next(w for w in field if mul(v, w) == one)
    assert all(mul(v, inv(v)) == one for v in field if v != zero)
    zeta2 = mul(zeta, zeta)
    assert mul(zeta2, zeta) == one and zeta != one
    zpowers = [one, zeta, zeta2]
    assert neg(one) not in zpowers

    elements = list(product(field, range(3)))
    identity = (zero, 0)
    def gmul(g, h):
        v, i = g
        w, j = h
        return (add(v, mul(zpowers[i], w)), (i+j) % 3)
    def ginv(g):
        v, i = g
        return (neg(mul(zpowers[(-i) % 3], v)), (-i) % 3)
    def conj(g, h):
        return gmul(gmul(ginv(h), g), h)
    def comm(g, h):
        return gmul(gmul(gmul(g, h), ginv(g)), ginv(h))
    def beta(g):
        v, i = g
        return (neg(v), i)
    def order(g):
        h = identity
        for n in range(1, 76):
            h = gmul(h, g)
            if h == identity:
                return n
        raise AssertionError("invalid element order")

    assert all(gmul(g, ginv(g)) == identity for g in elements)
    assert all(gmul(gmul(g, h), k) == gmul(g, gmul(h, k))
               for g in elements for h in elements for k in elements)
    x, y = (zero, 1), (one, 1)
    generated = {identity}
    queue = deque([identity])
    while queue:
        g = queue.popleft()
        for h in (x, y):
            k = gmul(g, h)
            if k not in generated:
                generated.add(k)
                queue.append(k)
    assert len(generated) == 75
    c = comm(x, y)
    assert c == (add(zeta, neg(one)), 0)
    d = mul(add(zeta, neg(one)), add(zeta, neg(one)))
    r = mul((3, 0), inv(d))  # -2 / ((X-1)(Y-1))
    s = mul(mul(zeta, mul(add(zeta, neg(one)), r)),
            inv(add(zeta2, neg(one))))
    f, h = (mul(c[0], r), 0), (mul(c[0], s), 0)
    a = add(one, mul(d, r))
    assert a == neg(one)
    assert r == (1, 1) and s == zeta
    assert f == ((3, 4), 0) and h == ((4, 3), 0)
    assert beta(x) == x and beta(y) == conj(y, f)
    xy = gmul(x, y)
    assert beta(xy) == conj(xy, h)
    assert gmul(f, beta(f)) == identity
    assert gmul(h, beta(h)) == identity
    assert all(beta(beta(g)) == g for g in elements)
    assert all(beta(gmul(g, h)) == gmul(beta(g), beta(h))
               for g in elements for h in elements)
    inner_conjugators = [
        g for g in elements if conj(x, g) == beta(x) and conj(y, g) == beta(y)
    ]
    assert inner_conjugators == []
    radical = {(v, 0) for v in field}
    normal_commutators = {comm(x, y)}
    queue = deque(normal_commutators)
    while queue:
        v = queue.popleft()
        for g in (x, y):
            w = conj(v, g)
            if w not in normal_commutators:
                normal_commutators.add(w)
                queue.append(w)
    derived = {identity}
    queue = deque([identity])
    while queue:
        v = queue.popleft()
        for w in normal_commutators:
            t = gmul(v, w)
            if t not in derived:
                derived.add(t)
                queue.append(t)
    assert derived == radical
    return {
        "field": "F5[zeta]/(zeta^2+zeta+1)",
        "group": "F25(additive) semidirect C3, scalar action zeta",
        "group_order": 75, "derived_order": 25,
        "x": x, "y": y, "xy": xy, "commutator": c,
        "orders_x_y_xy": [order(x), order(y), order(xy)],
        "r": r, "s": s, "f": f, "h": h, "derived_multiplier": a,
        "automorphism": "(v,i) -> (-v,i)",
        "generated_subgroup_order": len(generated),
        "associativity_triples_checked": 75**3,
        "automorphism_multiplication_pairs_checked": 75**2,
        "involution_elements_checked": 75,
        "possible_inner_conjugators_checked": 75,
        "inner_conjugators": inner_conjugators,
        "f_norm": True, "h_norm": True,
        "all_three_peripheral_classes_fixed": True,
        "nontrivial_outer_order": 2,
    }


def finite_haar_components():
    # Quotients (Z/m)^2 of A^(5'), with diagonal quotient C3.
    # The normalized Haar idempotent for its kernel has coefficients
    # 3/m^2 on a+b=0 mod3. Subtract full averaging, 1/m^2.
    moduli = [3, 6, 9, 12, 18]
    coefficient_powers = [1, 2, 3]
    values = {}
    rows = []
    for m, k in product(moduli, coefficient_powers):
        modulus = 5**k
        inv_m2 = pow(m*m, -1, modulus)
        elements = list(product(range(m), repeat=2))
        e = {v: (2 if sum(v) % 3 == 0 else -1) * inv_m2 % modulus
             for v in elements}
        haar = {v: (3*inv_m2 % modulus if sum(v) % 3 == 0 else 0)
                for v in elements}
        assert sum(e.values()) % modulus == 0
        for target in elements:
            convolution = sum(
                e[u] * e[((target[0]-u[0]) % m, (target[1]-u[1]) % m)]
                for u in elements
            ) % modulus
            assert convolution == e[target]
            assert haar[((target[0]-3) % m, target[1])] == haar[target]
        values[m, k] = e
        rows.append({"abelian_modulus": m, "coefficient_modulus": modulus,
                     "quotient_order": m*m, "idempotent": True,
                     "augmentation": 0, "haar_invariant_under_t_cubed": True})
    compatibilities = 0
    for m, n in product(moduli, repeat=2):
        if n > m and n % m == 0:
            for k in coefficient_powers:
                modulus = 5**k
                projected = {(a, b): 0 for a, b in product(range(m), repeat=2)}
                for (a, b), coefficient in values[n, k].items():
                    projected[a % m, b % m] += coefficient
                assert {v: coefficient % modulus for v, coefficient in projected.items()} == values[m, k]
                compatibilities += 1
    for m in moduli:
        for k in (1, 2):
            assert {v: a % 5**k for v, a in values[m, k+1].items()} == values[m, k]
            compatibilities += 1
    return {"scope": "15 stated finite quotient/coefficient pairs",
            "rows": rows, "projection_compatibilities_checked": compatibilities,
            "scope_limit": "The general continuous idempotent is proved by inverse limits in A.22."}


def main():
    result = {"status": "PASS", "finite_group_certificate": finite_quotient(),
              "finite_haar_components": finite_haar_components(),
              "scope_limit": (
                  "The infinite construction is an automorphism of the full free profinite "
                  "metabelian quotient. The code certifies its stated finite quotient. "
                  "No order-preserving peripheral lift to the full free profinite group is asserted."
              )}
    (HERE / "a_metabelian_involution.json").write_text(json.dumps(result, indent=2) + "\n")
    print("PASS: order75 finite metabelian group and generating pair.")
    print("PASS: 421875 associativity triples; 5625 automorphism multiplication pairs.")
    print("PASS: peripheral x,y,xy; f/h norm equations; exact automorphism order2.")
    print("PASS: all75 possible inner conjugators excluded; outer order2.")
    print("PASS: 15 finite Haar-idempotent cases and all stated projection compatibilities.")
    print("Full free profinite lifting is not asserted.")


if __name__ == "__main__":
    main()
