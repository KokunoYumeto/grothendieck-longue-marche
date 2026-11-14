#!/usr/bin/env python3
"""Exact finite source and positive CM signs for the E.58 construction.

Independent standard-library enumeration.  The infinite centralizer lift and
relative peripheral lift are proved in E.58; this certifies their actual finite
input, including the joint source and the order obstruction to retaining G6.
"""
from collections import Counter
from itertools import product
from math import gcd
from pathlib import Path
import hashlib
import json
import time


I = (1, 0, 0, 1)


def mm(a, b, m):
    return ((a[0] * b[0] + a[1] * b[2]) % m,
            (a[0] * b[1] + a[1] * b[3]) % m,
            (a[2] * b[0] + a[3] * b[2]) % m,
            (a[2] * b[1] + a[3] * b[3]) % m)


def mi(a, m):
    return (a[3] % m, -a[1] % m, -a[2] % m, a[0] % m)


def neg(a):
    return tuple(-x % 12 for x in a)


def canon(a):
    return min(tuple(a), neg(a))


def qm(a, b):
    return canon(mm(a, b, 12))


def qi(a):
    return canon(mi(a, 12))


def power(a, n, mul, identity):
    out = identity
    for _ in range(n):
        out = mul(out, a)
    return out


def comm(a, b, mul, inv):
    return mul(mul(mul(a, b), inv(a)), inv(b))


def closure(gens, mul, identity):
    seen, queue = {identity}, [identity]
    for a in queue:
        for b in gens:
            c = mul(a, b)
            if c not in seen:
                seen.add(c)
                queue.append(c)
    return seen


def order(a, mul, identity, bound):
    return next(n for n in range(1, bound + 1)
                if power(a, n, mul, identity) == identity)


def am(g, h):
    A, v = g[:4], g[4:]
    B, w = h[:4], h[4:]
    return mm(A, B, 3) + ((v[0] + A[0] * w[0] + A[1] * w[1]) % 3,
                          (v[1] + A[2] * w[0] + A[3] * w[1]) % 3)


def ai(g):
    A, v = mi(g[:4], 3), g[4:]
    # Linear parts can have determinant -1; use the literal determinant.
    det = (g[0] * g[3] - g[1] * g[2]) % 3
    A = tuple(x * pow(det, -1, 3) % 3 for x in A)
    return A + ((-A[0] * v[0] - A[1] * v[1]) % 3,
                (-A[2] * v[0] - A[3] * v[1]) % 3)


def main():
    started = time.monotonic()
    Q = {canon(a) for a in product(range(12), repeat=4)
         if (a[0] * a[3] - a[1] * a[2]) % 12 == 1}
    s = canon((0, 1, 11, 0))
    r = canon((0, 11, 1, 11))
    tau = qm(s, r)
    x = power(qi(tau), 2, qm, I)
    y = qm(qm(s, x), s)
    assert len(Q) == 576 and closure((s, r), qm, I) == Q
    assert power(s, 2, qm, I) == power(r, 3, qm, I) == I
    assert x == (1, 2, 0, 1) and y == (1, 0, 10, 1)
    F = closure((x, y), qm, I)
    assert len(F) == 96
    assert F == {q for q in Q if tuple(a % 2 for a in q) == I}
    derived_gens = {comm(a, b, qm, qi) for a, b in product(F, repeat=2)}
    Fderived = closure(derived_gens, qm, I)
    H = closure(derived_gens | {power(a, 3, qm, I) for a in F}, qm, I)
    assert len(Fderived) == 8 and len(H) == 32

    V4 = {(1, 0, 0, 1), (1, 2, 0, 1), (1, 0, 2, 1), (1, 2, 2, 1)}
    def lift(q):
        choices = [a for a in (q, neg(q)) if tuple(v % 4 for v in a) in V4]
        assert len(choices) == 1
        return choices[0]
    def split(q):
        a = lift(q)
        return tuple(v % 4 for v in a), tuple(v % 3 for v in a)
    SL3 = {a for a in product(range(3), repeat=4)
           if (a[0] * a[3] - a[1] * a[2]) % 3 == 1}
    Q8 = {a for a in SL3 if a == I or a == (2, 0, 0, 2)
          or (a[0] + a[3]) % 3 == 0}
    assert len(Q8) == 8
    assert {split(a) for a in F} == set(product(V4, SL3))
    assert {split(a) for a in H} == set(product(V4, Q8))
    assert all(split(qm(a, b)) == (mm(split(a)[0], split(b)[0], 4),
                                  mm(split(a)[1], split(b)[1], 3))
               for a, b in product(F, repeat=2))
    ii, jj = (0, 1, 2, 0), (1, 1, 1, 2)
    assert mm(ii, ii, 3) == mm(jj, jj, 3) == (2, 0, 0, 2)
    assert mm(ii, jj, 3) == tuple(-v % 3 for v in mm(jj, ii, 3))
    assert closure((ii, jj), lambda a, b: mm(a, b, 3), I) == Q8

    # The actual B/H quotient: affine transformations on F3^2.
    # Its x,y values are the two translations, so its kernel is exactly H.
    oneD = I + (0, 0)
    sD = (0, 1, 1, 0, 0, 0)
    rD = (0, 2, 1, 2, 0, 1)
    tauD = am(sD, rD)
    xD = power(ai(tauD), 2, am, oneD)
    yD = am(am(sD, xD), sD)
    D = closure((sD, rD), am, oneD)
    assert len(D) == 54
    assert power(sD, 2, am, oneD) == power(rD, 3, am, oneD) == oneD
    assert xD == I + (1, 0) and yD == I + (0, 1)
    assert comm(xD, yD, am, ai) == oneD
    assert power(xD, 3, am, oneD) == power(yD, 3, am, oneD) == oneD

    def jm(a, b):
        return qm(a[0], b[0]), am(a[1], b[1])
    oneJ = (I, oneD)
    J = closure(((s, sD), (r, rD)), jm, oneJ)
    assert len(J) == 1728
    assert {a for a, b in J} == Q and {b for a, b in J} == D
    assert {(a, b) for a, b in J if b == oneD} == {(a, oneD) for a in H}
    assert len({b for a, b in J if a == I}) == 3
    qcosets = {frozenset(qm(a, h) for h in H) for a in Q}
    assert len(qcosets) == 18
    qcoset = {a: min(C) for C in qcosets for a in C}
    D_to_common = {}
    for a, b in J:
        if b in D_to_common:
            assert D_to_common[b] == qcoset[a]
        D_to_common[b] = qcoset[a]
    assert J == {(a, b) for a in Q for b in D if qcoset[a] == D_to_common[b]}

    xy_comm = comm(x, y, qm, qi)
    z = power(xy_comm, 2, qm, I)
    assert xy_comm == (1, 8, 8, 5)
    assert z == (5, 0, 0, 5) and order(z, qm, I, 12) == 2
    assert z in H and all(qm(z, a) == qm(a, z) for a in Q)
    assert split(z) == (I, (2, 0, 0, 2))
    assert (z, oneD) in J
    rJ = (r, rD)
    centralizerJ = {a for a in J if jm(a, rJ) == jm(rJ, a)}
    assert (z, oneD) in centralizerJ

    # The exact E.1 positive convention: A=z, beta=V=1.
    Ainv = mi(lift(z), 12)
    betainv = I
    v = (1, 2)
    R3 = tuple(a % 3 for a in r)
    assert ((R3[0] * v[0] + R3[1] * v[1]) % 3,
            (R3[2] * v[0] + R3[3] * v[1]) % 3) == v
    Av = ((Ainv[0] * v[0] + Ainv[1] * v[1]) % 3,
          (Ainv[2] * v[0] + Ainv[3] * v[1]) % 3)
    bits = (int(Av == (2, 1)), int(tuple(a % 3 for a in betainv)
                                     not in (I, (2, 0, 0, 2))))
    assert Av == (2, 1) and bits == (1, 0)

    # Integral Bass--Serre cycle for tau^12; a unit edge coefficient makes
    # its N-abelianization primitive, without choosing a homology basis.
    assert order(tau, qm, I, 24) == 12
    chain = Counter()
    t = I
    for _ in range(12):
        chain[qm(t, s)] += 1
        chain[qm(t, tau)] -= 1
        t = qm(t, tau)
    chain = Counter({a: n for a, n in chain.items() if n})
    boundary = Counter()
    r2 = qm(r, r)
    for a, n in chain.items():
        sv = ('s', min(a, qm(a, s)))
        rv = ('r', min(a, qm(a, r), qm(a, r2)))
        boundary[rv] += n
        boundary[sv] -= n
    assert all(n == 0 for n in boundary.values())
    assert len(chain) == 24 and set(chain.values()) == {-1, 1}
    primitive_gcd = 0
    for n in chain.values():
        primitive_gcd = gcd(primitive_gcd, n)
    assert primitive_gcd == 1
    assert power(x, 6, qm, I) == I and power(xD, 6, am, oneD) == oneD

    result = {
        "status": "PASS_EXACT_RELATIVE_CM_SOURCE",
        "scope": "Finite source maps and CM signs; infinite lifts are proved in E58.",
        "Q_order": len(Q), "F_Q_order": len(F), "F_Q_derived_order": len(Fderived),
        "H_Q_order": len(H), "H_Q_actual_split": "C2^2 x Q8",
        "D_B_over_H_order": len(D), "actual_joint_order": len(J),
        "actual_common_order": len(qcosets), "r_joint_centralizer_order": len(centralizerJ),
        "s_Q": s, "r_Q": r, "tau_Q": tau, "x_Q": x, "y_Q": y,
        "s_D_affine": sD, "r_D_affine": rD, "x_D_translation": xD, "y_D_translation": yD,
        "commutator_xy_Q": xy_comm, "literal_H_word": "[x,y]^2",
        "z_Q": z, "z_order": 2, "z_mod4": split(z)[0], "z_mod3": split(z)[1],
        "z_lies_in_actual_joint_kernel": True,
        "A_beta_V": [z, I, I], "fixed_3_torsion_line_vector": v,
        "A_inverse_on_line": Av, "E1_positive_CM_bits": bits, "extra_CM_coset": True,
        "tau12_integral_cycle_nonzero_edges": len(chain),
        "tau12_integral_cycle_gcd": primitive_gcd,
        "tau12_integral_cycle": [{"edge": a, "coefficient": n} for a, n in sorted(chain.items())],
        "G6_image_order_of_x6": 6,
        "G6_cannot_factor_through_relative_pro2_H": True,
    }
    path = Path(__file__)
    result["source_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    path.with_suffix('.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result, indent=2, sort_keys=True))
    print(f"Elapsed seconds: {time.monotonic() - started:.3f}")


if __name__ == '__main__':
    main()
