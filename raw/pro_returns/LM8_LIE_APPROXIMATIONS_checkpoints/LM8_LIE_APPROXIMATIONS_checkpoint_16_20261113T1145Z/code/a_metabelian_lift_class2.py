#!/usr/bin/env python3
"""Exact first nonmetabelian test of the specified A.22 involution.

Let K = ker(Fhat(x,y) -> C3), with x,y both mapping to 1. This
constructs Q = Fhat / closure(K^5 gamma_3(K)) using its class-two
exponent-five BCH kernel. The calculation is on complete Lie bases
and all linear equations, not a sampled search of the 29296875 elements.
"""
from itertools import combinations
from pathlib import Path
from fractions import Fraction
import json
import sys

RATIONAL = "--rational" in sys.argv
P = None if RATIONAL else 5
D = 10
PAIRS = list(combinations(range(4), 2))
ZERO = (0,) * D
BASIS = [tuple(int(i == j) for i in range(D)) for j in range(D)]
IDENTITY = BASIS
HERE = Path(__file__).resolve().parent


def field(x):
    return Fraction(x) if RATIONAL else x % P


def reciprocal(x):
    return 1 / Fraction(x) if RATIONAL else pow(x, -1, P)


HALF = reciprocal(2)
THIRD = reciprocal(3)


def add(a, b):
    return tuple(field(x + y) for x, y in zip(a, b))


def scale(a, s):
    return tuple(field(x * s) for x in a)


def sub(a, b):
    return add(a, scale(b, -1))


def linear(columns, v):
    answer = ZERO
    for c, s in zip(columns, v):
        answer = add(answer, scale(c, s))
    return answer


def compose(a, b):
    return [linear(a, c) for c in b]


def matrix_power(a, n):
    answer = IDENTITY
    while n:
        if n & 1:
            answer = compose(answer, a)
        a = compose(a, a)
        n //= 2
    return answer


def bracket(a, b):
    return (0,) * 4 + tuple(field(a[i] * b[j] - a[j] * b[i])
                            for i, j in PAIRS)


def bch(a, b):
    return add(add(a, b), scale(bracket(a, b), HALF))


def from_free_images(images):
    return list(images) + [bracket(images[i], images[j]) for i, j in PAIRS]


def inner(a):
    return [add(v, bracket(a, v)) for v in BASIS]


def solve(rows, rhs, variables):
    """Return a particular solution and nullity, or None if inconsistent."""
    table = [[field(x) for x in row] + [field(y)]
             for row, y in zip(rows, rhs)]
    pivots = []
    at = 0
    for j in range(variables):
        pivot = next((i for i in range(at, len(table)) if table[i][j]), None)
        if pivot is None:
            continue
        table[at], table[pivot] = table[pivot], table[at]
        inv = reciprocal(table[at][j])
        table[at] = [field(x * inv) for x in table[at]]
        for i in range(len(table)):
            if i != at and table[i][j]:
                factor = table[i][j]
                table[i] = [field(x - factor * y)
                            for x, y in zip(table[i], table[at])]
        pivots.append(j)
        at += 1
    if any(all(x == 0 for x in row[:-1]) and row[-1] for row in table):
        return None
    answer = [0] * variables
    for i, j in enumerate(pivots):
        answer[j] = table[i][-1]
    return answer, variables - len(pivots)


def span_basis(vectors):
    out = []
    for v in vectors:
        rows = [[c[i] for c in out] for i in range(D)]
        if solve(rows, v, len(out)) is None:
            out.append(v)
    return out


def in_span(v, columns):
    return solve([[c[i] for c in columns] for i in range(D)],
                 v, len(columns)) is not None


def main():
    a, b, c0, d = BASIS[:4]
    # Schreier basis:
    # a=x^3, b=y*x^-1, c0=x*y*x^-2, d=x^2*y.
    # T=conjugation by x. It satisfies T^3=conjugation by a.
    T = from_free_images([a, c0, bch(d, scale(a, -1)), bch(a, b)])
    assert matrix_power(T, 3) == inner(a)
    # z=a^(-1/3)*x has order 3; division by 3 is integral over Z5.
    J = compose(inner(scale(a, -THIRD)), T)
    assert matrix_power(J, 3) == IDENTITY
    assert linear(J, a) == a
    for u in BASIS:
        for v in BASIS:
            assert linear(J, bracket(u, v)) == bracket(linear(J, u), linear(J, v))
    JPOW = [IDENTITY, J, compose(J, J)]

    def mul(g, h):
        v, i = g
        w, j = h
        return bch(v, linear(JPOW[i], w)), (i + j) % 3

    def inverse(g):
        v, i = g
        return scale(linear(JPOW[-i % 3], v), -1), -i % 3

    def power(g, n):
        if n < 0:
            return power(inverse(g), -n)
        h = (ZERO, 0)
        while n:
            if n & 1:
                h = mul(h, g)
            g = mul(g, g)
            n //= 2
        return h

    def conjugate(g, h):
        return mul(mul(inverse(h), g), h)

    def commutator(g, h):
        return mul(mul(mul(g, h), inverse(g)), inverse(h))

    def conj_matrix(g):
        return [mul(mul(g, (v, 0)), inverse(g))[0] for v in BASIS]

    x = (scale(a, THIRD), 1)
    y = mul((b, 0), x)
    xy = mul(x, y)
    schreier = [power(x, 3), mul(y, inverse(x)),
                mul(mul(x, y), power(x, -2)), mul(power(x, 2), y)]
    assert schreier == [(v, 0) for v in BASIS[:4]]
    assert conj_matrix(x) == T
    X, Y, Z = conj_matrix(x), conj_matrix(y), conj_matrix(xy)
    comm = commutator(x, y)
    assert comm[1] == 0
    # Derived Lie subspace is Im(J-I) plus the full bracket space.
    derived = span_basis([sub(linear(J, v), v) for v in BASIS] + BASIS[4:])
    second = span_basis([bracket(u, v) for u in derived for v in derived])
    assert len(derived) == 8
    assert len(second) == 1
    w = second[0]
    assert linear(J, w) == w
    assert all(bracket(w, v) == ZERO for v in BASIS)
    assert in_span(comm[0], derived)
    assert all(in_span(sub(linear(X, linear(Y, v)), linear(Y, linear(X, v))),
                       second) for v in derived)
    # z and (y^3)^(-1/3)y are the prime-to-five parts of x and y.
    # On Q'/Q'' they induce the same order-three action.
    y3 = power(y, 3)
    assert y3[1] == 0
    yt = mul((scale(y3[0], -THIRD), 0), y)
    assert power(yt, 3) == (ZERO, 0)
    JY = conj_matrix(yt)
    assert all(in_span(sub(linear(J, v), linear(JY, v)), second)
               for v in derived)
    if not RATIONAL:
        assert matrix_power(X, 10) == J
        assert matrix_power(Y, 10) == JY
    E = [sub(v, scale(add(add(v, linear(J, v)), linear(JPOW[2], v)), THIRD))
         for v in BASIS]
    assert all(in_span(sub(linear(E, linear(E, v)), linear(E, v)), second)
               for v in derived)
    XmI, YmI, ZmI = [[sub(c, v) for c, v in zip(M, BASIS)] for M in [X, Y, Z]]
    DXY = compose(XmI, YmI)
    EmI = [sub(c, v) for c, v in zip(E, BASIS)]

    def module_solve(operator, target):
        """Solve operator(v)=target and E(v)=v in Q'/Q''."""
        columns = [linear(operator, v) for v in derived]
        ecolumns = [linear(EmI, v) for v in derived]
        rows = [[columns[j][i] for j in range(8)] + [w[i], 0]
                for i in range(D)]
        rows += [[ecolumns[j][i] for j in range(8)] + [0, w[i]]
                 for i in range(D)]
        result = solve(rows, list(target) + list(ZERO), 10)
        assert result is not None
        solution, nullity = result
        assert nullity == 1
        return linear(derived, solution[:8])

    f = module_solve(DXY, scale(linear(E, comm[0]), -2))
    h = module_solve(ZmI, linear(X, linear(YmI, f)))

    def induced_phi(flog):
        py = conjugate(y, (flog, 0))
        generators = [power(x, 3), mul(py, inverse(x)),
                      mul(mul(x, py), power(x, -2)), mul(power(x, 2), py)]
        assert all(i == 0 for _, i in generators)
        matrix = from_free_images([v for v, _ in generators])
        assert linear(matrix, a) == a
        assert compose(matrix, J) == compose(J, matrix)
        return matrix

    phi = induced_phi(f)
    assert compose(phi, phi) == IDENTITY
    assert linear(phi, w) == w
    assert phi != IDENTITY
    assert all(linear(phi, bracket(u, v)) == bracket(linear(phi, u), linear(phi, v))
               for u in BASIS for v in BASIS)

    def normalise(logg):
        norm = bch(logg, linear(phi, logg))
        result = solve([[t] for t in w], norm, 1)
        assert result is not None
        coefficient = result[0][0]
        corrected = sub(logg, scale(w, coefficient * HALF))
        assert bch(corrected, linear(phi, corrected)) == ZERO
        return corrected, coefficient

    f, f_norm_correction = normalise(f)
    h, h_norm_correction = normalise(h)
    assert induced_phi(f) == phi
    left = mul(x, conjugate(y, (f, 0)))
    right = conjugate(xy, (h, 0))
    defect = mul(left, inverse(right))
    success = defect == (ZERO, 0)
    # This does not presuppose success; any failed equality is reported.
    if RATIONAL:
        assert all(Fraction(t).denominator % 5 for vector in [f, h, w, *phi, *J]
                   for t in vector)
    payload = {
        "quotient": ("Fhat2 / ker(K -> free class-two pro-5 quotient), K=ker(x,y->1 in C3)"
                     if RATIONAL else "Fhat2 / closure(K^5 gamma_3(K)), K=ker(x,y->1 in C3)"),
        "prime": 5,
        "order": "infinite; open kernel Z5^10 in BCH coordinates" if RATIONAL else 3 * 5**10,
        "kernel_rank": 4,
        "basis": ["A", "B", "C", "D", "[A,B]", "[A,C]", "[A,D]",
                  "[B,C]", "[B,D]", "[C,D]"],
        "schreier_basis": ["x^3", "y*x^-1", "x*y*x^-2", "x^2*y"],
        "derived_order": "Z5-rank8" if RATIONAL else 5**8,
        "second_derived_order": "Z5-rank1" if RATIONAL else 5,
        "central_second_derived_generator": w,
        "f_log": f,
        "h_log": h,
        "f_norm_adjustment": f_norm_correction,
        "h_norm_adjustment": h_norm_correction,
        "phi_columns": phi,
        "peripheral_defect": defect,
        "peripheral_lift_pass": success,
        "norm_equations_pass": True,
        "automorphism_exact_order": 2,
        "calculation_scope": "Complete finite-dimensional linear systems and all basis bracket identities; no sampled group search and no enumeration of all group elements.",
        "full_free_profinite_lift_asserted": False,
    }
    basename = "a_metabelian_lift_class2_5adic" if RATIONAL else "a_metabelian_lift_class2"
    (HERE/f"{basename}.json").write_text(json.dumps(payload, indent=2, default=str)+"\n")
    lines = [
        ("Exact rational identities, integral at5; class-two pro-5 kernel of rank10."
         if RATIONAL else f"Exact quotient order {3*5**10}; derived order {5**8}; second derived order 5."),
        "PASS: complete Schreier relations, class-two BCH model and order-three action.",
        "PASS: prescribed A.22 metabelian f/h residues and both exact norm identities.",
        "PASS: exact-order-two automorphism on the complete Lie basis.",
        f"Peripheral lift: {'PASS' if success else 'FAIL'}; defect={defect}.",
        f"f={f}; h={h}.",
        "No assertion of a lift to the full free profinite group.",
    ]
    text = "\n".join(lines) + "\n"
    (HERE/f"{basename}.out").write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
