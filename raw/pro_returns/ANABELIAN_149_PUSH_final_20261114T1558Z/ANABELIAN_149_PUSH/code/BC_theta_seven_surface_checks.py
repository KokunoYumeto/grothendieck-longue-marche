#!/usr/bin/env python3
"""Exact finite-field checks for the theta-seven surface candidate.

The general identities and dimension assertion are proved in the audit.
This standard-library script checks every good ordered-fibre pair up to
exchange over F16, an explicit point outside the cubic locus, and the
separate one-parameter family over F16.
"""
from collections import defaultdict
from pathlib import Path
import json


def mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 16:
            a ^= 19  # omega^4+omega+1
    return out


def power(a, n):
    out = 1
    for _ in range(n):
        out = mul(out, a)
    return out


def div(a, b):
    assert b != 0
    return mul(a, power(b, 14))


def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else 0) ^
                 (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def product(p, q):
    out = [0] * (len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] ^= mul(a, b)
    return trim(out)


def ppow(p, n):
    out = [1]
    for _ in range(n):
        out = product(out, p)
    return out


def evaluate(p, x):
    out = 0
    for a in reversed(p):
        out = mul(out, x) ^ a
    return out


def H(x, t):
    return div(power(mul(x, x ^ 1), 3),
               mul(power(x ^ t, 5), power(mul(x, x) ^ t, 2)))


def obstruction(a, b, c):
    return power(a ^ b ^ c, 3) ^ mul(mul(a, b), c)


def check_norm(t, a, b, c, A, B):
    assert all((a, b, c, evaluate(B, 0), evaluate(B, 1), evaluate(B, t)))
    assert B[-1] == 1 and evaluate(A, t) == 0
    u = [0, 1, 1]
    phi_t = mul(a, t) ^ div(b, t) ^ div(c, t ^ 1)
    phi_numerator = [b, b ^ c, a, a]
    left = add(product(u, add(ppow(A, 2), product(A, B))),
               product(ppow(B, 2), add(phi_numerator, product([phi_t], u))))
    right = product([a], ppow([t, 1], 7))
    assert left == right
    return phi_t, left


def main():
    pair_count = 0
    off_cubic_count = 0
    example = None
    for t in range(2, 16):
        fibres = defaultdict(list)
        for r in range(2, 16):
            if r == t or mul(r, r) == t:
                continue
            fibres[H(r, t)].append(r)
        for value, roots in fibres.items():
            for i, r in enumerate(roots):
                for s in roots[i+1:]:
                    kappa = mul(power(r ^ s, 2), value)
                    a = kappa
                    b = div(mul(kappa, power(t, 7)), power(mul(r, s), 2))
                    c = div(mul(kappa, power(t ^ 1, 7)),
                            power(mul(r ^ 1, s ^ 1), 2))
                    rho_r = div(mul(r ^ t, mul(r, r ^ 1)), mul(r, r) ^ t)
                    rho_s = div(mul(s ^ t, mul(s, s ^ 1)), mul(s, s) ^ t)
                    v_t = div(rho_r, t ^ r) ^ div(rho_s, t ^ s)
                    B = [mul(r, s), r ^ s, 1]
                    A = [mul(rho_r, s) ^ mul(rho_s, r) ^ mul(v_t, B[0]),
                         rho_r ^ rho_s ^ mul(v_t, B[1]), v_t]
                    phi_t, norm = check_norm(t, a, b, c, A, B)
                    obs = obstruction(a, b, c)
                    pair_count += 1
                    off_cubic_count += bool(obs)
                    if (t, r, s) == (2, 10, 13):
                        example = {"t": t, "r": r, "s": s,
                                   "H_value": value, "kappa": kappa,
                                   "a": a, "b": b, "c": c,
                                   "A_low_first": A, "B_low_first": B,
                                   "phi_t": phi_t,
                                   "norm_numerator_low_first": norm,
                                   "cubic_obstruction": obs}
    assert example is not None
    assert (example["a"], example["b"], example["c"],
            example["cubic_obstruction"]) == (6, 13, 11, 7)
    assert example["A_low_first"] == [9, 1, 6]
    assert example["B_low_first"] == [11, 7, 1]
    one_parameter_checks = 0
    for t in range(2, 16):
        U = mul(t, t ^ 1)
        a = div(1, power(U, 2))
        b = div(power(t, 3), power(t ^ 1, 2))
        c = div(power(t ^ 1, 3), power(t, 2))
        phi_t, _ = check_norm(t, a, b, c, [t, 1], [t, 0, 1])
        assert phi_t == mul(a, t ^ 1)
        assert obstruction(a, b, c) == div(power(U, 3) ^ U ^ 1, power(U, 3))
        one_parameter_checks += 1
    result = {"status": "PASS", "field": "F2[omega]/(omega^4+omega+1)",
              "surface_pairs_checked_up_to_exchange": pair_count,
              "pairs_outside_cubic_locus": off_cubic_count,
              "one_parameter_checks": one_parameter_checks,
              "explicit_surface_example": example,
              "scope": "Finite certificates for the displayed formulas; the general proof and dimension argument are in the candidate audit."}
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
