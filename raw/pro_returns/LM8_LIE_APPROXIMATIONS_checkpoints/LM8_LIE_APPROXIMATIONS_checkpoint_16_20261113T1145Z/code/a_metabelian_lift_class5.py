#!/usr/bin/env python3
"""Integral Hall-coordinate class-five lifting equations for A.22.

All noncommutative series are truncated by total degree. Lyndon brackets
give a complete free Lie basis. The complete twenty-parameter A.24 class-four family is retained.
Class-five elements use actual group Hall coordinates; the bare integral
Lie lattice is not assumed closed under BCH.
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
parser.add_argument("--class", dest="nilclass", type=int, choices=[5], default=5)
parser.add_argument("--mod5", action="store_true")
args = parser.parse_args()
C = args.nilclass
MOD5 = args.mod5
assert not MOD5, "class5 uses exact rational Magnus series with integral Hall coordinates"
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
assert [sum(len(w) == d for w in LYNDON) for d in range(1, C+1)] == [4, 6, 20, 60, 204][:C]


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


def integral5(t):
    return Fraction(t).denominator % 5 != 0


def mod5(t):
    t = Fraction(t)
    return t.numerator * pow(t.denominator, -1, 5) % 5


def rank_mod5(vectors):
    rows = [[mod5(t) for t in row] for row in vectors]
    if not rows:
        return 0
    at = 0
    for j in range(len(rows[0])):
        pivot = next((i for i in range(at, len(rows)) if rows[i][j]), None)
        if pivot is None:
            continue
        rows[at], rows[pivot] = rows[pivot], rows[at]
        unit = pow(rows[at][j], -1, 5)
        rows[at] = [x*unit % 5 for x in rows[at]]
        for i in range(at+1, len(rows)):
            if rows[i][j]:
                coefficient = rows[i][j]
                rows[i] = [(x-coefficient*y) % 5
                           for x, y in zip(rows[i], rows[at])]
        at += 1
    return at


# Hall group elements are recursively bracketed group commutators.
# Their leading terms are the corresponding Lyndon Lie brackets.
HG, HLOG = {}, {}


def hall_group(w):
    if w not in HG:
        if len(w) == 1:
            HG[w] = exp(GENS[w[0]])
        else:
            split = next(i for i in range(1, len(w)) if lyndon(w[i:]))
            g, h = hall_group(w[:split]), hall_group(w[split:])
            HG[w] = mul(mul(mul(g, h), inverse(g)), inverse(h))
        HLOG[w] = log(HG[w])
        lead = {v: t for v, t in HLOG[w].items() if len(v) == len(w)}
        assert lead == lyndon_bracket(w)
    return HG[w]


for w in LYNDON:
    hall_group(w)
    assert all(integral5(t) for t in HLOG[w].values())
report("PASS: all294 Hall group generators and their leading Lyndon brackets; Hall logarithms are5-integral.")


def hall_collect(g, maximum_degree=5):
    remainder = g
    out = []
    for w in LYNDON:
        if len(w) > maximum_degree:
            break
        coefficient = remainder.get(w, scalar(0))
        out.append(coefficient)
        if coefficient:
            remainder = mul(exp(scale(HLOG[w], -coefficient)), remainder)
    return out, remainder


def hall_build(coefficients):
    g = ONE
    for w, t in zip(LYNDON, coefficients):
        if t:
            g = mul(g, exp(scale(HLOG[w], t)))
    return g


c4 = json.loads((HERE/"a_metabelian_lift_class4_rational.json").read_text())
assert c4["linear_solution_nullity"] == 20
names5 = {"".join("ABCD"[i] for i in w): j for j, w in enumerate(LYNDON)}


def embed_c4(vector):
    result = {}
    for name, coefficient in zip(c4["basis"], vector):
        if coefficient != "0" and coefficient != 0:
            result = add(result, scale(LB[names5[name]], Fraction(coefficient)))
    return result


u4 = embed_c4(c4["f_log_Lyndon_coordinates"])
v4 = embed_c4(c4["h_log_Lyndon_coordinates"])
fu4, _ = hall_collect(exp(u4), 4)
hv4, _ = hall_collect(exp(v4), 4)
assert len(fu4) == len(hv4) == 90
assert all(integral5(t) for t in fu4+hv4)
fbase, hbase = hall_build(fu4), hall_build(hv4)
ubase, vbase = log(fbase), log(hbase)
assert {w: t for w, t in ubase.items() if len(w) <= 4} == u4
assert {w: t for w, t in vbase.items() if len(w) <= 4} == v4
assert hall_collect(fbase)[0] == fu4 + [scalar(0)]*204
assert hall_collect(hbase)[0] == hv4 + [scalar(0)]*204
report("PASS: actual integral Hall lifts of the complete class4 particular pair; no integral BCH-lattice assumption.")

# Compute the rational bracket ideal and prove that it is the actual
# integral logarithm of Q''. The latter group has class at most two,
# so its logarithm is additively closed (2 is a 5-adic unit).
H = [sub(B, CC), add(sub(CC, D), A)] + [p for w, p in zip(LYNDON, LB) if len(w) >= 2]
H_degrees = [1, 1] + [len(w) for w in LYNDON if len(w) >= 2]
H2_vectors = [coords(bracket(u, v))
              for i, u in enumerate(H) for j, v in enumerate(H[i+1:], i+1)
              if H_degrees[i]+H_degrees[j] <= 5]
H2_rows = span_echelon(H2_vectors)
H2_rank = len(H2_rows)
assert all(integral5(t) for _, row in H2_rows for t in row)
assert rank_mod5(H2_vectors) == H2_rank
report(f"Rational bracket ideal rank={H2_rank}; integral span saturated at5.")

g1 = mul(J(EB), inverse(EB))
g2 = mul(J(EC), inverse(EC))
group_generators = [(g1, 1), (g2, 1)] + [(HG[w], len(w)) for w in LYNDON if 2 <= len(w) <= 4]
actual_rows = []
for i, (g, degree_g) in enumerate(group_generators):
    for h, degree_h in group_generators[i+1:]:
        if degree_g+degree_h > 5:
            continue
        commutator = mul(mul(mul(g, h), inverse(g)), inverse(h))
        vector = coords(log(commutator))
        assert all(integral5(t) for t in vector)
        assert not any(reduce_mod(vector, H2_rows))
        actual_rows.append(vector)
assert rank_mod5(actual_rows) == H2_rank
report(f"PASS: {len(actual_rows)} actual group commutators span the complete rank{H2_rank} Q'' lattice modulo5.")
# Normality under N and C3 follows from the bracket ideal; adjoint series
# on degree>=2 through degree5 have only denominators dividing 3!.
# Thus this saturated span is exactly log(Q''), not just a rational span.

u1 = {w: t for w, t in ubase.items() if len(w) == 1}
v1 = {w: t for w, t in vbase.items() if len(w) == 1}
parameter_pairs = []
for kernel_vector in c4["affine_kernel_basis"]:
    du, dv = {}, {}
    for (side, name), coefficient in zip(c4["unknown_coordinates"], kernel_vector):
        coefficient = Fraction(coefficient)
        if coefficient:
            assert len(name) == 4
            if side == "f":
                du = add(du, scale(LB[names5[name]], coefficient))
            else:
                dv = add(dv, scale(LB[names5[name]], coefficient))
    # log(fbase exp(du)) through degree5; these are genuine integral
    # Hall-coordinate families for every Z5 parameter.
    parameter_pairs.append((add(du, scale(bracket(u1, du), Fraction(1, 2))),
                            add(dv, scale(bracket(v1, dv), Fraction(1, 2)))))
assert len(parameter_pairs) == 20


def induced_phi(u):
    py = conjugate(y, (exp(u), 0))
    images = [qpower(x, 3), qmul(py, qinv(x)),
              qmul(qmul(x, py), qpower(x, -2)), qmul(qpower(x, 2), py)]
    assert all(i == 0 for _, i in images)
    return substitute_factory([log(s) for s, _ in images])


def Xg(g):
    return mul(mul(x[0], J(g)), inverse(x[0]))


def Yg(g):
    return mul(mul(y[0], J(g)), inverse(y[0]))


def Zg(g):
    return mul(mul(xy[0], J2(g)), inverse(xy[0]))


def product_norm_J(g):
    return mul(mul(g, J(g)), J2(g))


nc = product_norm_J(comm[0])
ec = mul(comm[0], exp(scale(log(nc), Fraction(-1, 3))))


def residual(u, v):
    phi = induced_phi(u)
    f, h = exp(u), exp(v)
    normf = log(mul(f, exp(phi(u))))
    normh = log(mul(h, exp(phi(v))))
    lhs = qmul(x, conjugate(y, (f, 0)))
    rhs = conjugate(xy, (h, 0))
    delta = qmul(lhs, qinv(rhs))
    assert delta[1] == 0
    peripheral = log(delta[0])
    dxyf = mul(mul(mul(Xg(Yg(f)), inverse(Xg(f))), inverse(Yg(f))), f)
    hrelation = mul(mul(Zg(h), inverse(h)),
                    inverse(mul(Xg(Yg(f)), inverse(Xg(f)))))
    module_words = [product_norm_J(f), product_norm_J(h),
                    mul(dxyf, mul(ec, ec)), hrelation]
    parts = [coords(t) for t in [normf, normh, peripheral]]
    parts += [reduce_mod(coords(log(t)), H2_rows) for t in module_words]
    assert all(not any(p[:90]) for p in parts)
    answer = [t for part in parts for t in part[90:]]
    assert all(integral5(t) for t in answer)
    return answer


base = residual(ubase, vbase)
columns = []
for i, (du, dv) in enumerate(parameter_pairs):
    columns.append([a-b for a, b in zip(residual(add(ubase, du), add(vbase, dv)), base)])
    report(f"full prior-family columns {i+1}/20; elapsed {time.monotonic()-START:.1f}s")

# Degree-five changes are central in N. Their derivatives can be
# written exactly using only the degree-one actions J and P.
Jlin = substitute_factory([{w: t for w, t in a.items() if len(w) == 1} for a in J_images])
P1_images = [embed_c4(row) for row in c4["phi_images_Lyndon_coordinates"]]
Plin = substitute_factory([{w: t for w, t in a.items() if len(w) == 1} for a in P1_images])
TOP = [(i, w, p) for i, (w, p) in enumerate(zip(LYNDON, LB)) if len(w) == 5]
assert len(TOP) == 204


def encode_parts(parts):
    answer = []
    for i, polynomial in enumerate(parts):
        vector = coords(polynomial)
        if i >= 3:
            vector = reduce_mod(vector, H2_rows)
        assert not any(vector[:90])
        answer.extend(vector[90:])
    return answer


central_f, central_h = [], []
for count, (i, w, p) in enumerate(TOP, 1):
    jp, j2p, pp = Jlin(p), Jlin(Jlin(p)), Plin(p)
    lu = scale(sub(add(jp, j2p), scale(p, 2)), Fraction(2, 3))
    lv = scale(sub(sub(scale(j2p, 2), jp), p), Fraction(2, 3))
    jd = sub(j2p, jp)
    summation = add(add(p, jp), j2p)
    dxy = add(sub(j2p, scale(jp, 2)), p)
    central_f.append(encode_parts([add(add(p, pp), lu), lv, jd,
                                   summation, {}, dxy, scale(jd, -1)]))
    central_h.append(encode_parts([{}, add(p, pp), sub(p, j2p),
                                   {}, summation, {}, sub(j2p, p)]))
    if count % 40 == 0 or count == 204:
        report(f"central basis derivatives {count}/204; elapsed {time.monotonic()-START:.1f}s")

columns += central_f + central_h
unknown_names = ([["prior_class4_parameter", i] for i in range(20)] +
                 [[side, "".join("ABCD"[j] for j in w)] for side in ["f5", "h5"] for _, w, _ in TOP])
assert len(columns) == len(unknown_names) == 428
assert all(integral5(t) for column in columns for t in column)
rows = list(map(list, zip(*columns)))
rank5 = rank_mod5(rows)
augmented_rank5 = rank_mod5([row+[-b] for row, b in zip(rows, base)])
report(f"Integral class5 system shape={len(rows)}x428; ranks mod5={rank5},{augmented_rank5}.")

# Cross-check the derived central formulas against exact group evaluation.
for j in [0, 17, 103, 203]:
    p = TOP[j][2]
    assert [a-b for a, b in zip(residual(add(ubase, p), vbase), base)] == central_f[j]
    assert [a-b for a, b in zip(residual(ubase, add(vbase, p)), base)] == central_h[j]
report("PASS: derived central formulas agree with exact group evaluations in four declared basis checks.")

system = {
    "shape": [len(rows), 428],
    "unknown_coordinates": unknown_names,
    "matrix_sparse_entries": [(i, j, t) for i, row in enumerate(rows)
                              for j, t in enumerate(row) if t],
    "right_hand_side": [-b for b in base],
    "row_order": ["norm_f", "norm_h", "third_peripheral", "NormJ_f_mod_Qsecond",
                  "NormJ_h_mod_Qsecond", "DXY_f_Ec2_mod_Qsecond", "h_relation_mod_Qsecond"],
    "top_Lyndon_words": ["".join("ABCD"[j] for j in w) for _, w, _ in TOP],
}
system_text = json.dumps(system, indent=2, default=str)+"\n"
system_path = HERE/"a_metabelian_lift_class5_system.json"
system_path.write_text(system_text)
payload = {
    "class": 5,
    "group_model": "Actual integral Hall group coordinates inside rational Magnus series",
    "prior_parameters_retained": 20,
    "new_central_coordinates": 408,
    "open_kernel_coordinate_rank": 294,
    "second_derived_coordinate_rank": H2_rank,
    "actual_commutator_span_rank_mod5": rank_mod5(actual_rows),
    "system_rank_mod5": rank5,
    "augmented_system_rank_mod5": augmented_rank5,
    "system_file": "code/"+system_path.name,
    "system_sha256": hashlib.sha256(system_text.encode()).hexdigest(),
    "all_matrix_and_rhs_entries_five_integral": True,
    "f_base_Hall_coordinates_through_class4": fu4,
    "h_base_Hall_coordinates_through_class4": hv4,
    "prior_parameter_log_pairs": [[coords(du), coords(dv)] for du, dv in parameter_pairs],
    "f_base_log": coords(ubase),
    "h_base_log": coords(vbase),
    "Lyndon_basis": ["".join("ABCD"[i] for i in w) for w in LYNDON],
    "full_free_profinite_lift_asserted": False,
}
if augmented_rank5 > rank5:
    payload["integral_lift_exists"] = False
    payload["conclusion_scope"] = "Inconsistency of the entire integral Hall-coordinate class5 family, not a denominator-only test"
    report("OBSTRUCTION: no integral class5 lift in the complete prior family.")
else:
    report("No mod5 obstruction; solving the exact rational affine system.")
    solution, nullity, rank, kernel, free_columns, pivots = solve(rows, [-b for b in base])
    payload.update({"rational_solution_exists": solution is not None,
                    "rational_rank": rank, "rational_nullity": nullity,
                    "affine_particular_solution": solution, "affine_kernel_basis": kernel,
                    "affine_free_columns": free_columns, "rank_pivot_columns": pivots})
    if solution is not None:
        u, v = ubase, vbase
        for t, (du, dv) in zip(solution[:20], parameter_pairs):
            u, v = add(u, scale(du, t)), add(v, scale(dv, t))
        for t, (_, _, p) in zip(solution[20:224], TOP):
            u = add(u, scale(p, t))
        for t, (_, _, p) in zip(solution[224:], TOP):
            v = add(v, scale(p, t))
        assert not any(residual(u, v))
        f_hall, frem = hall_collect(exp(u))
        h_hall, hrem = hall_collect(exp(v))
        assert frem == hrem == ONE
        integral = all(integral5(t) for t in f_hall+h_hall)
        payload.update({"integral_particular_witness": integral,
                        "particular_parameter_values_five_integral": all(integral5(t) for t in solution),
                        "entire_affine_basis_five_integral": all(integral5(t) for row in kernel for t in row),
                        "f_log": coords(u), "h_log": coords(v),
                        "f_Hall_coordinates": f_hall, "h_Hall_coordinates": h_hall})
        if integral:
            phi = induced_phi(u)
            assert all(phi(phi(a)) == a for a in GENS)
            assert all(phi(J(a)) == J(phi(a)) for a in GENS)
            payload["order_two_and_deck_equivariance_verified"] = True
            payload["integral_lift_exists"] = True
        report(f"Rational class5 rank={rank}, nullity={nullity}; actual Hall-integral witness={integral}.")
    else:
        report("Rational inconsistency beyond the mod5 test; no integral lift.")

payload["elapsed_seconds"] = time.monotonic()-START
(HERE/"a_metabelian_lift_class5.json").write_text(json.dumps(payload, indent=2, default=str)+"\n")
report(f"Saved complete class5 system and result; elapsed {payload['elapsed_seconds']:.1f}s")
(HERE/"a_metabelian_lift_class5.out").write_text("\n".join(TRANSCRIPT)+"\n")

