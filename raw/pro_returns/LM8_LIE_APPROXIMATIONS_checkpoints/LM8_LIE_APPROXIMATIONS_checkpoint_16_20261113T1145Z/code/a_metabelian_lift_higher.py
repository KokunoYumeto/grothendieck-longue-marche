#!/usr/bin/env python3
"""Exact class-three/four relative-kernel lifting equations for A.22.

All noncommutative series are truncated by total degree. Lyndon brackets
give a complete free Lie basis. Corrections of degree >=3 enter the
equations affinely through class4, so the full finite-dimensional lifting
problem above the specified A.23 class2 solution is a linear system.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
from math import factorial
import argparse
import hashlib
import json
import time

parser = argparse.ArgumentParser()
parser.add_argument("--class", dest="nilclass", type=int, choices=[3, 4], default=3)
parser.add_argument("--mod5", action="store_true")
args = parser.parse_args()
C = args.nilclass
MOD5 = args.mod5
HERE = Path(__file__).resolve().parent
START = time.monotonic()
TRANSCRIPT = []


def report(message):
    TRANSCRIPT.append(message)
    print(message, flush=True)


def scalar(x):
    if MOD5:
        x = Fraction(x)
        return x.numerator * pow(x.denominator, -1, 5) % 5
    return Fraction(x)


def inv(x):
    return pow(x, -1, 5) if MOD5 else 1 / Fraction(x)


def clean(a):
    return {w: v for w, v in a.items() if v}


def add(a, b):
    c = a.copy()
    for w, v in b.items():
        c[w] = scalar(c.get(w, 0) + v)
    return clean(c)


def scale(a, s):
    s = scalar(s)
    return clean({w: scalar(v * s) for w, v in a.items()})


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    by_degree = [[] for _ in range(C + 1)]
    for w, v in b.items():
        by_degree[len(w)].append((w, v))
    out = {}
    for u, s in a.items():
        for d in range(C - len(u) + 1):
            for v, t in by_degree[d]:
                w = u + v
                out[w] = scalar(out.get(w, 0) + s * t)
    return clean(out)


ONE = {(): scalar(1)}
GENS = [{(i,): scalar(1)} for i in range(4)]


def exp(a):
    out, term = ONE, ONE
    for n in range(1, C + 1):
        term = mul(term, a)
        out = add(out, scale(term, Fraction(1, factorial(n))))
    return out


def log(a):
    u = sub(a, ONE)
    out, term = {}, ONE
    for n in range(1, C + 1):
        term = mul(term, u)
        out = add(out, scale(term, Fraction((-1)**(n+1), n)))
    return out


def inverse(a):
    u = sub(a, ONE)
    out, term = ONE, ONE
    for n in range(1, C + 1):
        term = mul(term, u)
        out = add(out, scale(term, (-1)**n))
    return out


def bracket(a, b):
    return sub(mul(a, b), mul(b, a))


def substitute_factory(images):
    cache = {(): ONE, **{(i,): images[i] for i in range(4)}}
    def word_image(w):
        if w not in cache:
            cache[w] = mul(word_image(w[:-1]), images[w[-1]])
        return cache[w]
    def apply(a):
        out = {}
        for w, v in a.items():
            out = add(out, scale(word_image(w), v))
        return out
    return apply


def lyndon(w):
    return all(w < w[i:] for i in range(1, len(w)))


LYNDON = [w for d in range(1, C+1)
          for w in product(range(4), repeat=d) if lyndon(w)]
LBRACKETS = {}


def lyndon_bracket(w):
    if w not in LBRACKETS:
        if len(w) == 1:
            LBRACKETS[w] = GENS[w[0]]
        else:
            split = next(i for i in range(1, len(w)) if lyndon(w[i:]))
            LBRACKETS[w] = bracket(lyndon_bracket(w[:split]), lyndon_bracket(w[split:]))
    return LBRACKETS[w]


LB = [lyndon_bracket(w) for w in LYNDON]
DIM = len(LB)
assert [sum(len(w) == d for w in LYNDON) for d in range(1, C+1)] == [4, 6, 20, 60][:C]


def coords(a):
    rest = a.copy()
    out = []
    for w, p in zip(LYNDON, LB):
        c = rest.get(w, 0)
        out.append(c)
        if c:
            rest = sub(rest, scale(p, c))
    assert not rest, ("not a Lie element", rest)
    return out


def from_coords(a):
    out = {}
    for c, p in zip(a, LB):
        if c:
            out = add(out, scale(p, c))
    return out


def vector_add(a, b):
    return [scalar(x+y) for x, y in zip(a, b)]


def vector_scale(a, s):
    return [scalar(x*s) for x in a]


def span_echelon(vectors):
    rows = []
    for vector in vectors:
        v = list(vector)
        for pivot, row in rows:
            if v[pivot]:
                v = vector_add(v, vector_scale(row, -v[pivot]))
        pivot = next((i for i, x in enumerate(v) if x), None)
        if pivot is not None:
            v = vector_scale(v, inv(v[pivot]))
            rows.append((pivot, v))
            rows.sort()
    return rows


def reduce_mod(v, rows):
    v = list(v)
    for pivot, row in rows:
        if v[pivot]:
            v = vector_add(v, vector_scale(row, -v[pivot]))
    return v


def solve(rows, rhs):
    n = len(rows[0])
    table = [[scalar(x) for x in row]+[scalar(y)] for row, y in zip(rows, rhs)]
    pivots, at = [], 0
    for j in range(n):
        pivot = next((i for i in range(at, len(table)) if table[i][j]), None)
        if pivot is None:
            continue
        table[at], table[pivot] = table[pivot], table[at]
        table[at] = vector_scale(table[at], inv(table[at][j]))
        for i in range(len(table)):
            if i != at and table[i][j]:
                table[i] = vector_add(table[i], vector_scale(table[at], -table[i][j]))
        pivots.append(j)
        at += 1
    inconsistent = [r for r in table if not any(r[:-1]) and r[-1]]
    if inconsistent:
        return None, n-len(pivots), len(pivots), [], [], pivots
    answer = [scalar(0)] * n
    for i, j in enumerate(pivots):
        answer[j] = table[i][-1]
    free_columns = [j for j in range(n) if j not in pivots]
    kernel = []
    for free in free_columns:
        vector = [scalar(0)] * n
        vector[free] = scalar(1)
        for i, pivot in enumerate(pivots):
            vector[pivot] = -table[i][free]
        kernel.append(vector)
    return answer, n-len(pivots), len(pivots), kernel, free_columns, pivots


A, B, CC, D = GENS
EA, EB, EC, ED = [exp(t) for t in GENS]
T_images = [A, CC, log(mul(ED, inverse(EA))), log(mul(EA, EB))]
T = substitute_factory(T_images)
assert all(T(T(T(u))) == mul(mul(EA, u), inverse(EA)) for u in GENS)
aminus = exp(scale(A, Fraction(-1, 3)))
aplus = inverse(aminus)
J_images = [mul(mul(aminus, T(u)), aplus) for u in GENS]
J = substitute_factory(J_images)
J2 = substitute_factory([J(J(u)) for u in GENS])
assert all(J(J2(u)) == u for u in GENS)
assert J(A) == A
JPOW = [lambda s: s, J, J2]


def qmul(g, h):
    a, i = g
    b, j = h
    return mul(a, JPOW[i](b)), (i+j) % 3


def qinv(g):
    a, i = g
    return JPOW[-i % 3](inverse(a)), -i % 3


def qpower(g, n):
    if n < 0:
        return qpower(qinv(g), -n)
    h = (ONE, 0)
    while n:
        if n & 1:
            h = qmul(h, g)
        g = qmul(g, g)
        n //= 2
    return h


def conjugate(g, h):
    return qmul(qmul(qinv(h), g), h)


def adjoint(g, v):
    n, i = g
    return mul(mul(n, JPOW[i](v)), inverse(n))


x = (exp(scale(A, Fraction(1, 3))), 1)
y = qmul((EB, 0), x)
xy = qmul(x, y)
schreier = [qpower(x, 3), qmul(y, qinv(x)),
            qmul(qmul(x, y), qpower(x, -2)), qmul(qpower(x, 2), y)]
assert schreier == [(u, 0) for u in [EA, EB, EC, ED]]
comm = qmul(qmul(qmul(x, y), qinv(x)), qinv(y))
assert comm[1] == 0
logcomm = log(comm[0])
EX = lambda s: adjoint(x, s)
EY = lambda s: adjoint(y, s)
EZ = lambda s: adjoint(xy, s)


def E(s):
    return sub(s, scale(add(add(s, J(s)), J2(s)), Fraction(1, 3)))


# The Lie algebra of Q' has two noninvariant degree-one directions and
# every bracket direction. Its second derived algebra is [H,H].
H = [sub(B, CC), add(sub(CC, D), A)] + [p for w, p in zip(LYNDON, LB) if len(w) >= 2]
H2_rows = span_echelon([coords(bracket(u, v)) for i, u in enumerate(H)
                       for v in H[i+1:]])
H2_rank = len(H2_rows)
if not MOD5:
    assert all(Fraction(t).denominator % 5 for _, row in H2_rows for t in row)
report(f"class={C}; Lie dimension={DIM}; Q'' Lie rank={H2_rank}; constructing exact equations")

# Fixed A.23 data, as Lie polynomials rather than a collected group word.
u0 = add(scale(add(add(A, B), scale(D, -1)), Fraction(2, 3)),
         add(add(scale(bracket(A, B), Fraction(-4, 27)),
                 scale(bracket(A, CC), Fraction(-1, 27))),
             add(add(scale(bracket(A, D), Fraction(5, 27)),
                     scale(bracket(B, CC), Fraction(1, 9))),
                 scale(bracket(CC, D), Fraction(-1, 9)))))
v0 = add(scale(add(add(A, CC), scale(D, -1)), Fraction(2, 3)),
         add(add(scale(bracket(A, B), Fraction(1, 27)),
                 scale(bracket(A, CC), Fraction(-8, 27))),
             add(add(scale(bracket(A, D), Fraction(1, 27)),
                     scale(bracket(B, CC), Fraction(-1, 9))),
                 scale(bracket(B, D), Fraction(-1, 9)))))


def induced_phi(u):
    py = conjugate(y, (exp(u), 0))
    images = [qpower(x, 3), qmul(py, qinv(x)),
              qmul(qmul(x, py), qpower(x, -2)), qmul(qpower(x, 2), py)]
    assert all(i == 0 for _, i in images)
    return substitute_factory([log(s) for s, _ in images])


def full_residual(u, v):
    phi = induced_phi(u)
    f, h = exp(u), exp(v)
    normf = log(mul(f, exp(phi(u))))
    normh = log(mul(h, exp(phi(v))))
    lhs = qmul(x, conjugate(y, (f, 0)))
    rhs = conjugate(xy, (h, 0))
    delta = qmul(lhs, qinv(rhs))
    assert delta[1] == 0
    peripheral = log(delta[0])
    yu = sub(EY(u), u)
    module = [
        sub(E(u), u),
        sub(E(v), v),
        add(sub(EX(yu), yu), scale(E(logcomm), 2)),
        sub(sub(EZ(v), v), EX(yu)),
    ]
    parts = [coords(t) for t in [normf, normh, peripheral]]
    parts += [reduce_mod(coords(t), H2_rows) for t in module]
    assert all(not any(p[:10]) for p in parts)
    return [z for part in parts for z in part[10:]]


unknowns = [(side, i) for side in [0, 1]
            for i, w in enumerate(LYNDON) if len(w) >= 3]
base = full_residual(u0, v0)
columns = []
for j, (side, i) in enumerate(unknowns):
    u = add(u0, LB[i]) if side == 0 else u0
    v = add(v0, LB[i]) if side == 1 else v0
    columns.append([scalar(a-b) for a, b in zip(full_residual(u, v), base)])
    if (j+1) % 20 == 0 or j+1 == len(unknowns):
        report(f"columns {j+1}/{len(unknowns)}; elapsed {time.monotonic()-START:.1f}s")

rows = list(map(list, zip(*columns)))
solution, nullity, rank, kernel, free_columns, pivot_columns = solve(rows, [-x for x in base])
suffix = "mod5" if MOD5 else "rational"
stem = f"a_metabelian_lift_class{C}_{suffix}"
system = {
    "row_order": ["norm_f", "norm_h", "third_peripheral", "E_f-f",
                  "E_h-h", "(X-1)(Y-1)f+2Elogc", "(Z-1)h-X(Y-1)f"],
    "weight_at_least_three_Lyndon_words": ["".join("ABCD"[j] for j in w)
                                           for w in LYNDON if len(w) >= 3],
    "unknown_coordinates": [("f" if side == 0 else "h", "".join("ABCD"[j] for j in LYNDON[i]))
                            for side, i in unknowns],
    "shape": [len(rows), len(unknowns)],
    "matrix_sparse_entries": [(i, j, t) for i, row in enumerate(rows)
                              for j, t in enumerate(row) if t],
    "right_hand_side": [-x for x in base],
}
system_text = json.dumps(system, indent=2, default=str)+"\n"
(HERE/f"{stem}_system.json").write_text(system_text)
payload = {
    "nilpotency_class_of_open_pro5_kernel": C,
    "arithmetic": "F5" if MOD5 else "exact rational",
    "free_Lie_dimensions_by_weight": [4, 6, 20, 60][:C],
    "free_Lie_dimension": DIM,
    "second_derived_Lie_rank": H2_rank,
    "unknowns": len(unknowns),
    "linear_system_rank": rank,
    "linear_solution_nullity": nullity,
    "affine_particular_solution": solution,
    "affine_kernel_basis": kernel,
    "affine_free_columns": free_columns,
    "rank_pivot_columns": pivot_columns,
    "unknown_coordinates": system["unknown_coordinates"],
    "system_file": f"code/{stem}_system.json",
    "system_sha256": hashlib.sha256(system_text.encode()).hexdigest(),
    "lift_exists_in_calculation": solution is not None,
    "full_free_profinite_lift_asserted": False,
    "basis": ["".join("ABCD"[i] for i in w) for w in LYNDON],
    "calculation_scope": "Every higher-weight coefficient above the specified class2 solution; exact affine equations, not sampling. Rational solutions must be checked for 5-integrality separately.",
}
if solution is not None:
    u, v = u0, v0
    for t, (side, i) in zip(solution, unknowns):
        if side == 0:
            u = add(u, scale(LB[i], t))
        else:
            v = add(v, scale(LB[i], t))
    assert not any(full_residual(u, v))
    phi = induced_phi(u)
    assert all(phi(phi(a)) == a for a in GENS)
    assert all(phi(J(a)) == J(phi(a)) for a in GENS)
    assert phi(A) == A
    payload["f_log_Lyndon_coordinates"] = coords(u)
    payload["h_log_Lyndon_coordinates"] = coords(v)
    payload["phi_images_Lyndon_coordinates"] = [coords(phi(a)) for a in GENS]
    payload["five_integral"] = (True if MOD5 else
                               all(Fraction(t).denominator % 5
                                   for t in coords(u)+coords(v)+sum([coords(phi(a)) for a in GENS], [])))
    payload["entire_affine_kernel_basis_five_integral"] = (True if MOD5 else
        all(Fraction(t).denominator % 5 for vector in kernel for t in vector))
    assert all(not scalar(sum(a*b for a, b in zip(row, vector)))
               for vector in kernel for row in rows)
    assert all(scalar(sum(a*b for a, b in zip(row, solution))) == scalar(-value)
               for row, value in zip(rows, base))
    assert all(vector[j] == int(j == free)
               for vector, free in zip(kernel, free_columns) for j in free_columns)
    payload["order_two_and_equivariance_verified"] = True
    # A complete affine-system proof is by weight: two corrections of
    # degree at least3 first interact in degree at least5 here. This
    # explicit mixed vector is only a cross-check of implementation.
    test = [scalar((i+1) % 5) for i in range(len(unknowns))]
    ut, vt = u0, v0
    for t, (side, i) in zip(test, unknowns):
        if side == 0:
            ut = add(ut, scale(LB[i], t))
        else:
            vt = add(vt, scale(LB[i], t))
    predicted = list(base)
    for t, column in zip(test, columns):
        predicted = vector_add(predicted, vector_scale(column, t))
    assert full_residual(ut, vt) == predicted
    payload["mixed_affinity_crosscheck"] = True
    report(f"PASS: class{C} lift; nullity={nullity}; 5-integral={payload['five_integral']}; whole affine basis integral={payload['entire_affine_kernel_basis_five_integral']}")
else:
    report(f"INCONSISTENT: class{C} lifting system; rank={rank}")

payload["elapsed_seconds"] = time.monotonic()-START
out = HERE/f"{stem}.json"
out.write_text(json.dumps(payload, indent=2, default=str)+"\n")
report(f"Saved {out.name}; elapsed {payload['elapsed_seconds']:.1f}s")
(HERE/f"{stem}.out").write_text("\n".join(TRANSCRIPT)+"\n")
