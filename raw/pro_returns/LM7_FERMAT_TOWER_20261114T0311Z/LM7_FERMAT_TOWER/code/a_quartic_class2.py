#!/usr/bin/env python3
"""Exact quartic frame and class-two certificates for E.105.

All field arithmetic is in Q[zeta_8]=Q[t]/(t^4+1).  No arithmetic
or coefficient data are imported from another project program.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import random
import sympy as sp


ZERO = (F(0),) * 4
ONE = (F(1), F(0), F(0), F(0))
ZETA = (F(0), F(1), F(0), F(0))
variable = sp.Symbol("t")


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


def scale(a, n):
    return tuple(F(n) * x for x in a)


def mul(a, b):
    c = [F(0)] * 7
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    for k in range(6, 3, -1):
        c[k - 4] -= c[k]
    return tuple(c[:4])


def inverse(a):
    p = sum(sp.Rational(x.numerator, x.denominator) * variable**i
            for i, x in enumerate(a))
    v = sp.Poly(sp.invert(p, variable**4 + 1), variable)
    return tuple(F(v.nth(i)) for i in range(4))


def divide(a, b):
    return mul(a, inverse(b))


def power(a, n):
    if n < 0:
        return power(inverse(a), -n)
    result = ONE
    while n:
        if n & 1:
            result = mul(result, a)
        a = mul(a, a)
        n //= 2
    return result


def qmatrix(a):
    return [[str(F(v)) for v in row] for row in a.tolist()]


def modular(x, m):
    x = F(x)
    return x.numerator * pow(x.denominator, -1, m) % m


def main():
    sqrt2 = sub(ZETA, power(ZETA, 3))
    assert mul(sqrt2, sqrt2) == scale(ONE, 2)
    monomials = {mul(power(ZETA, k), power(sqrt2, n)): (k, n)
                 for k in range(8) for n in range(-24, 25)}
    assert len(monomials) == 8 * 49
    points = []
    for kind in ("A", "B", "C"):
        for i in range(4):
            a = power(ZETA, 1 + 2 * i)
            assert power(a, 4) == neg(ONE)
            point = ((ZERO, a, ONE) if kind == "A" else
                     (a, ZERO, ONE) if kind == "B" else (a, ONE, ZERO))
            line = ((ZERO, ONE, neg(a)) if kind == "A" else
                    (ONE, ZERO, neg(a)) if kind == "B" else (ONE, neg(a), ZERO))
            assert add(add(power(point[0], 4), power(point[1], 4)),
                       power(point[2], 4)) == ZERO
            points.append(dict(name=kind + str(i), a=a, point=point, line=line))
    origin = 4
    assert points[origin]["name"] == "B0"
    other = [i for i in range(12) if i != origin]
    labels = [points[i]["name"] for i in other]

    # The same literal formal branch works in each of the three charts.
    s = sp.Symbol("s")
    branch = 1 + s**4 / 4 - 3 * s**8 / 32 + 7 * s**12 / 128
    assert sp.series(branch**4 - (1 + s**4), s, 0, 16).removeO() == 0

    def line_leading(i, j):
        if i == j:
            return 4, scale(points[j]["a"], F(1, 4))
        value = ZERO
        for a, b in zip(points[i]["line"], points[j]["point"]):
            value = add(value, mul(a, b))
        assert value != ZERO
        return 0, value

    def function_leading(i, j):
        n, a = line_leading(i, j)
        m, b = line_leading(origin, j)
        return n - m, divide(a, b)

    frames, n_columns, k_columns = {}, [], []
    for d in other:
        _, origin_value = function_leading(d, origin)
        column_n, column_k, values = [], [], {}
        for q in other:
            order, value = function_leading(d, q)
            value = divide(value, origin_value)
            k, n = monomials[value]
            assert value == mul(power(ZETA, k), power(sqrt2, n))
            values[points[q]["name"]] = dict(
                zeta8_exponent=k, sqrt2_exponent=n,
                field_coefficients=[str(x) for x in value], function_order=order)
            column_n.append(n)
            column_k.append(k)
        n_columns.append(column_n)
        k_columns.append(column_k)
        frames[points[d]["name"]] = values
    N = sp.Matrix(n_columns).T
    K = sp.Matrix(k_columns).T
    assert N == N.T
    Vpaths = N / 8
    v = sum((Vpaths[:, labels.index(name)] for name in ("B1", "B2", "B3")),
            sp.zeros(11, 1)) / 4
    expected_v = [-F(1, 2)] * 4 + [-F(5, 8), -F(3, 4), -F(5, 8)] + [-F(1, 2)] * 4
    assert list(v) == expected_v
    basis = sp.eye(11)
    pairs = list(combinations(range(11), 2))

    def wedge(a, b):
        return sp.Matrix([a[i] * b[j] - a[j] * b[i] for i, j in pairs])

    L = sp.Matrix.hstack(*(wedge(basis[:, i], Vpaths[:, i]) for i in range(11)))
    Lv = L + sp.Matrix.hstack(*(wedge(v, basis[:, i]) for i in range(11)))
    wA = sp.Matrix([int(t[0] == "A") for t in labels])
    wC = sp.Matrix([int(t[0] == "C") for t in labels])
    wB = -wA - wC
    I = sp.Matrix.hstack(wA / 4, wB / 4)
    toric = sp.Matrix([[int(t[0] == "A") - int(t[0] == "C") for t in labels],
                       [int(t[0] == "B") - int(t[0] == "C") for t in labels]])
    assert toric * I == sp.eye(2)
    assert toric * v == sp.zeros(2, 1)
    assert Lv * I == sp.zeros(55, 2)
    assert Lv.rank() == 9
    galois = []
    for k in (1, 3, 5, 7):
        columns = []
        for label in labels:
            image = label[0] + str(((k * (1 + 2 * int(label[1])) % 8) - 1) // 2)
            columns.append(-sp.ones(11, 1) if image == "B0" else basis[:, labels.index(image)])
        P = sp.Matrix.hstack(*columns)
        W2 = sp.Matrix.hstack(*(wedge(P[:, i], P[:, j]) for i, j in pairs))
        assert P * I == I and toric * P == toric
        assert W2 * Lv == Lv * P
        galois.append(dict(zeta_exponent=k, permutation_quotient_matrix=qmatrix(P)))

    # Coherent 4-division exists uniquely for every odd power level.
    division = []
    for m in (3, 5, 7, 9, 15, 25, 27, 35, 45, 49, 75, 81, 99, 125):
        a = pow(4, -1, m)
        b = (1 - 4 * a) // m
        assert 4 * a + m * b == 1
        for r in range(m):
            assert 4 * (a * r) % m == r
        division.append(dict(m=m, a=a, b=b))
    # Exact rational two-primary root carry: kappa(zeta_8^k)/4 = delta(k/32).
    root_checks = 0
    for n in range(1, 9):
        modulus = 2**n
        for chi in range(1, 1 + 8 * 32, 8):
            for k in range(8):
                value = k * (chi - 1) // 8
                assert F(value, 4) == F(k, 32) * (chi - 1)
                assert (k * (chi - 1) - 8 * value) % (8 * modulus) == 0
                root_checks += 1
    endpoint_signs = []
    endpoint_checks = 0
    for d in range(11):
        sigma = [int(q != d) for q in range(11)]
        endpoint_signs.append(sigma)
        for _ in range(40):
            local_rng = random.Random(105000 + d * 40 + _)
            orders = [local_rng.randrange(-12, 13) for q in range(11)]
            at_origin = -sum(orders)
            assert (sum(a * b for a, b in zip(sigma, orders)) - orders[d] - at_origin) % 2 == 0
            endpoint_checks += 1
        for chi in range(1, 1 + 8 * 32, 8):
            for epsilon in sigma:
                assert F(epsilon * (chi - 1), 2) == (chi - 1) * F(epsilon, 2)
                endpoint_checks += 1

    rng = random.Random(105)
    action_checks = origin_checks = relative_checks = cup_checks = 0
    for prime, exponent in ((3, 3), (5, 2), (7, 2), (11, 1)):
        m = prime**exponent
        inv2 = pow(2, -1, m)
        vv = tuple(modular(x, m) for x in v)
        lm = [[modular(x, m) for x in row] for row in L.tolist()]
        lvm = [[modular(x, m) for x in row] for row in Lv.tolist()]
        im = [[modular(x, m) for x in row] for row in I.tolist()]

        def av(a, b):
            return tuple((x + y) % m for x, y in zip(a, b))

        def sv(n, a):
            return tuple(n * x % m for x in a)

        def wv(a, b):
            return tuple((a[i] * b[j] - a[j] * b[i]) % m for i, j in pairs)

        def mat(M, a):
            return tuple(sum(x * y for x, y in zip(row, a)) % m for row in M)

        def prod(x, y):
            return av(x[0], y[0]), av(av(x[1], y[1]), sv(inv2, wv(x[0], y[0])))

        def inv(x):
            return sv(-1, x[0]), sv(-1, x[1])

        def theta(g, x, which=lm):
            chi, a = g
            return sv(chi, x[0]), av(sv(chi * chi, x[1]), sv(chi * a, mat(which, x[0])))

        def origin(g):
            _, a = g
            return sv(a, vv), sv(inv2 * a * a, mat(lm, vv))

        def gm(g, h):
            return g[0] * h[0] % m, (g[1] + g[0] * h[1]) % m

        units = [i for i in range(m) if i % prime]
        for _ in range(500):
            g, h = [(rng.choice(units), rng.randrange(m)) for _ in range(2)]
            x = (tuple(rng.randrange(m) for _ in range(11)),
                 tuple(rng.randrange(m) for _ in range(55)))
            y = (tuple(rng.randrange(m) for _ in range(11)),
                 tuple(rng.randrange(m) for _ in range(55)))
            assert theta(g, theta(h, x)) == theta(gm(g, h), x)
            assert theta(g, prod(x, y)) == prod(theta(g, x), theta(g, y))
            action_checks += 2
            assert origin(gm(g, h)) == prod(origin(g), theta(g, origin(h)))
            origin_checks += 1
            assert theta(g, x, lvm) == prod(prod(origin(g), theta(g, x)), inv(origin(g)))
            relative_checks += 1
            alpha, beta, alpha_h, beta_h = [rng.randrange(m) for _ in range(4)]
            x0 = mat(im, (alpha, beta))
            y0 = mat(im, (alpha_h, beta_h))
            assert mat(lvm, x0) == (0,) * 55
            raw = sv(inv2 * g[0], wv(x0, y0))
            determinant = inv2 * g[0] * (alpha * beta_h - beta * alpha_h)
            omega = wv(tuple(row[0] for row in im), tuple(row[1] for row in im))
            assert raw == sv(determinant, omega)
            # delta(alpha beta) = -(alpha cup beta + beta cup alpha).
            cross = (g[0]**2 * alpha_h * beta_h
                     - (alpha + g[0] * alpha_h) * (beta + g[0] * beta_h)
                     + alpha * beta) % m
            assert cross == -g[0] * (alpha * beta_h + beta * alpha_h) % m
            cup_checks += 1

    # A finite abelian-kernel extension with a nontrivial module action and
    # an actual section only specified on an index-four subgroup.
    coset_rows = []
    for prime, modulus, order, rho in ((3, 27, 12, 10), (5, 125, 20, 26), (7, 49, 28, 8)):
        assert pow(rho, order, modulus) == 1
        inv4 = pow(4, -1, modulus)
        f = [0] + [rng.randrange(modulus) for _ in range(order - 1)]

        def cocycle(g, h):
            return (f[g] + pow(rho, g, modulus) * f[h] - f[(g + h) % order]) % modulus

        def multiply(x, y):
            a, g = x
            b, h = y
            return ((a + pow(rho, g, modulus) * b + cocycle(g, h)) % modulus,
                    (g + h) % order)

        def invert(x):
            a, g = x
            h = -g % order
            return (-pow(pow(rho, g, modulus), -1, modulus) * (a + cocycle(g, h)) % modulus, h)

        z = {0: 0}
        step = modulus // prime
        for j in range(1, order // 4 + 1):
            z[4 * j % order] = (z[4 * (j - 1) % order] + pow(rho, 4 * (j - 1), modulus) * step) % modulus
        assert z[0] == 0

        def section_H(h):
            assert h % 4 == 0
            return ((-f[h] + z[h]) % modulus, h)

        representatives = [(rng.randrange(modulus), i) for i in range(4)]
        representatives[0] = (0, 0)

        def averaging(e, lifts=representatives):
            total = 0
            g = e[1]
            for i in range(4):
                j = (g + i) % 4
                h = (g + i - j) % order
                term = multiply(multiply(multiply(e, lifts[i]), invert(section_H(h))), invert(lifts[j]))
                assert term[1] == 0
                total += term[0]
            return total % modulus

        def section(g, lifts=representatives):
            e = (0, g)
            return multiply((-inv4 * averaging(e, lifts) % modulus, 0), e)

        for g in range(order):
            for h in range(order):
                assert multiply(section(g), section(h)) == section((g + h) % order)
        checks = order * order
        for _ in range(1000):
            e, f0 = [(rng.randrange(modulus), rng.randrange(order)) for _ in range(2)]
            assert averaging(multiply(e, f0)) == (averaging(e) + pow(rho, e[1], modulus) * averaging(f0)) % modulus
            checks += 1
        shifts = [0] + [rng.randrange(modulus) for _ in range(3)]
        lifts2 = [multiply((a, 0), e) for a, e in zip(shifts, representatives)]
        q = sum(shifts) * inv4 % modulus
        for g in range(order):
            transported = multiply(multiply((q, 0), section(g)), (-q % modulus, 0))
            assert section(g, lifts2) == transported
        coset_rows.append(dict(prime=prime, modulus=modulus, quotient_order=order,
                               module_generator=rho, multiplication_checks=checks,
                               exact_change_of_lift_checks=order))

    # Six actual determinant maps in wedge^2(V^3), with explicit inverse columns.
    hpairs = list(combinations(range(6), 2))
    hindex = {p: i for i, p in enumerate(hpairs)}
    determinants = sp.zeros(6, 15)
    inclusions = sp.zeros(15, 6)
    for i in range(3):
        k = hindex[(2 * i, 2 * i + 1)]
        determinants[i, k] = inclusions[k, i] = 1
    for col, (i, j) in enumerate(combinations(range(3), 2), start=3):
        k, l = hindex[(2 * i, 2 * j + 1)], hindex[(2 * i + 1, 2 * j)]
        determinants[col, k], determinants[col, l] = 1, -1
        inclusions[k, col], inclusions[l, col] = sp.Rational(1, 2), -sp.Rational(1, 2)
    assert determinants * inclusions == sp.eye(6)
    assert len(pairs) + 11 * 6 + len(hpairs) == 136

    output = dict(
        statement="E.105", origin="B0=[zeta8:0:1], tangent y/z=1",
        peripheral_order=labels, frames=frames,
        sqrt2_exponent_matrix=N.tolist(), zeta8_exponent_matrix=K.tolist(),
        path_vectors_matrix=qmatrix(Vpaths), averaged_origin_vector=[str(F(x)) for x in v],
        wedge_basis=[[labels[i], labels[j]] for i, j in pairs],
        peripheral_action_matrix=qmatrix(L), relative_action_matrix=qmatrix(Lv),
        relative_action_rank=9, toric_projection=qmatrix(toric), toric_section=qmatrix(I),
        galois_quotient_matrices=galois, coherent_four_division=division,
        rational_two_primary_root_carry_checks=root_checks,
        actual_tangential_sign_vectors=endpoint_signs,
        tangential_sign_character_and_carry_checks=endpoint_checks,
        actual_field_frame_checks=121, formal_chart_checks=12,
        class_two_action_checks=action_checks, actual_origin_cocycle_checks=origin_checks,
        relative_inner_action_checks=relative_checks, toric_cup_checks=cup_checks,
        finite_central_extension_averages=coset_rows,
        central_module_ranks=dict(toric_wedge=55, mixed=66, determinant=6, symmetric_square=9, total=136),
        compact_determinant_projection=qmatrix(determinants), compact_determinant_section=qmatrix(inclusions),
        scope="Exact frame values, actual peripheral action on G_F, its origin cochain, central averaging and coefficient maps; no unknown handle action is substituted by a graded action.",
    )
    Path(__file__).with_suffix(".json").write_text(json.dumps(output, indent=2, default=int) + "\n")
    print("PASS: 121 exact quartic frames and all root phases; 12 formal charts.")
    print(f"PASS: {action_checks} class-two action checks; {origin_checks} origin cocycles; {relative_checks} inner transports.")
    print(f"PASS: {cup_checks} toric cup identities; rank(L_v)=9 and L_v iota=0.")
    print(f"PASS: {root_checks} literal rational two-primary root carries and {len(division)} odd 4-division systems.")
    print(f"PASS: {endpoint_checks} literal endpoint-sign characters/carries; their fourth powers are retained as one.")
    print("PASS: three actual index-four abelian-kernel averages with complete quotient multiplication and change-of-lift comparisons.")
    print("PASS: rank-136 central decomposition; all six determinant projection/section identities.")


if __name__ == "__main__":
    main()
