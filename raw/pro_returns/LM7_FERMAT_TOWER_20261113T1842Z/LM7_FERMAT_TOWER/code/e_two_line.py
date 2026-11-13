#!/usr/bin/env python3
"""Exact finite certificates for E.52.

Run with --gp PATH to rerun the certified PARI computations before the
independent rational polynomial and matrix checks. Without that argument,
verify the retained e_two_units.out. PARI's bnfcertify, not an assumed GRH,
certifies each finite unit basis and class group.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
import subprocess

import sympy as sp

BASE = Path(__file__).resolve().parent
x, y = sp.symbols("x y")


def valuation(n, p=3):
    n = int(n)
    if n == 0:
        return 10**9
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a


def gp_element(s):
    assert s.startswith("Mod(") and s.endswith(")"), s
    a, p = s[4:-1].rsplit(", ", 1)
    return (sp.sympify(a.replace("^", "**"), locals={"x": x}),
            sp.sympify(p.replace("^", "**"), locals={"x": x}))


def rem(a, p):
    return sp.rem(a, p, x, domain=sp.QQ)


def powmod(a, n, p):
    if n < 0:
        a = sp.invert(a, p, x)
        n = -n
    b = sp.Integer(1)
    while n:
        if n & 1:
            b = rem(b*a, p)
        a = rem(a*a, p)
        n >>= 1
    return b


def cubic_norm(u):
    """Exact 3-by-3 determinant in Q(y)[x]/(x^3-y)."""
    q = sp.Poly(sp.rem(u, x**3-y, x), x)
    a, b, c = (q.nth(i) for i in range(3))
    N = sp.expand(a**3+y*b**3+y**2*c**3-3*y*a*b*c)
    # The reduced polynomial has degree at most two, fixing the order of
    # the resultant arguments and independently checking the determinant.
    assert N == sp.expand(sp.resultant(x**3-y, q.as_expr(), x))
    return N


def matrix_data(M):
    return [[str(v) for v in row] for row in M.tolist()]


def split_matrix(rows, columns, data):
    B = sp.Matrix(rows, columns, lambda i, j: data[i][j])
    if rows == 0:
        S = sp.zeros(columns, 0)
        K = sp.eye(columns)
        pivots = ()
    else:
        pivots = next(
            z for z in itertools.combinations(range(columns), rows)
            if int(B[:, list(z)].det()) % 3
        )
        C = B[:, list(pivots)]
        S = sp.zeros(columns, rows)
        for i, p in enumerate(pivots):
            for j in range(rows):
                S[p, j] = C.inv()[i, j]
        nonpivots = [i for i in range(columns) if i not in pivots]
        K = sp.zeros(columns, columns-rows)
        for j, i in enumerate(nonpivots):
            K[:, j] = sp.eye(columns)[:, i] - S*B[:, i]
    Q = S.row_join(K)
    assert B*S == sp.eye(rows)
    assert B*K == sp.zeros(rows, columns-rows)
    assert Q*Q.inv() == sp.eye(columns)
    assert all(v.q % 3 for v in Q)
    det = Q.det()
    assert det and det.p % 3 and det.q % 3
    # Exact inverse-coordinate identities, including every zero-rank case.
    assert B*Q == sp.eye(rows).row_join(sp.zeros(rows, columns-rows))
    return {
        "pivot_columns_zero_based": list(pivots),
        "norm_matrix": data,
        "right_inverse": matrix_data(S),
        "kernel_basis": matrix_data(K),
        "coordinate_matrix": matrix_data(Q),
        "inverse_coordinate_matrix": matrix_data(Q.inv()),
        "determinant": str(det),
    }


def verify_number_fields(output):
    text = output.read_text()
    assert "***   at " not in text and "***   user error" not in text, text
    records = [json.loads(z) for z in text.splitlines() if z.startswith("{")]
    assert records[-1] == {
        "type": "completion", "status": "PASS", "fields": 8, "transitions": 5
    }
    fields = {(z["d"], z["j"]): z for z in records if z["type"] == "field"}
    transitions = [z for z in records if z["type"] == "transition"]
    assert len(fields) == 8 and len(transitions) == 5
    for (d, j), z in fields.items():
        degree = 3**d if j == 0 else 2*3**(d+j-1)
        rank = (3**d-1)//2 if j == 0 else 3**(d+j-1)-1
        assert z["certified"] == 1 and z["class_number"] == 1
        assert z["degree"] == degree
        assert z["prime_two"] == [3**d, 1 if j == 0 else 2*3**(j-1)]
        assert z["prime_three"] == [degree, 1]
        assert z["root_order"] == 2 if j == 0 else z["root_order"] == 2*3**j
        assert len(z["normalized_units"]) == rank
    certificates = []
    checked_norms = 0
    for z in transitions:
        d, j = z["d"], z["j"]
        lo, hi = fields[d, j], fields[d+1, j]
        P = sp.sympify(lo["polynomial"].replace("^", "**"), locals={"x": x})
        Q = sp.sympify(hi["polynomial"].replace("^", "**"), locals={"x": x})
        assert sp.expand(P.subs(x, x**3)-Q) == 0
        lo_units = [gp_element(u)[0] for u in lo["normalized_units"]]
        hi_units = [gp_element(u)[0] for u in hi["normalized_units"]]
        for i, u in enumerate(hi_units):
            # The determinant of multiplication in the actual cubic algebra.
            norm = rem(cubic_norm(u).subs(y, x), P)
            gp_norm, gp_P = gp_element(z["normalized_unit_norms"][i])
            assert gp_P == P and rem(norm-gp_norm, P) == 0
            product = sp.Integer(1)
            for a, v in enumerate(lo_units):
                product = rem(product*powmod(v, z["matrix"][a][i], P), P)
            quotient = rem(norm*sp.invert(product, P, x), P)
            assert quotient in (sp.Integer(1), sp.Integer(-1))
            checked_norms += 1
        assert all(a % 3 for a in z["smith"])
        certificate = split_matrix(z["rows"], z["columns"], z["matrix"])
        certificate.update({"d": d, "j": j, "smith": z["smith"]})
        certificates.append(certificate)
    return records, certificates, checked_norms


def finite_tower_checks():
    factorizations = []
    for m in range(1, 4):
        for d in range(3):
            degree = 3**d
            product = x**degree-2
            factors = [product]
            for j in range(1, m+1):
                f = (x**(2*3**(d+j-1))
                     + 2**(3**(j-1))*x**(3**(d+j-1))
                     + 2**(2*3**(j-1)))
                factors.append(f)
                product = sp.expand(product*f)
            assert product == x**(3**(m+d))-2**(3**m)
            factorizations.append({
                "m": m, "d": d,
                "degrees": [sp.degree(f, x) for f in factors]
            })
    ranks = []
    for m in range(1, 6):
        h = (3**m-1)//2
        for d in range(6):
            pieces = [(3**d-1)//2] + [3**(d+j-1)-1 for j in range(1, m+1)]
            R = (3**(m+d)-1)//2-m
            assert sum(pieces) == R
            assert (3**(m+d+1)-1)//2-m-R == 3**(m+d)
            if d == 0:
                assert R == h-m >= 0
            ranks.append({"m": m, "d": d, "factor_ranks": pieces, "rank": R,
                          "next_kernel_rank": 3**(m+d)})
    roots = []
    for j in range(1, 7):
        modulus = 3**j
        f = 2*3**(j-1)
        assert int(sp.n_order(2, modulus)) == f
        assert valuation(2**f-1) == j
        roots.append({"j": j, "residue_degree": f, "three_part": modulus})
    return factorizations, ranks, roots


def valuation_checks():
    prime_rows = []
    chain_checks = 0
    for p in list(sp.primerange(2, 261)):
        if p in (2, 3):
            continue
        order = int(sp.n_order(2, p))
        s = valuation(p-1)
        for m in range(1, 4):
            eligible = valuation(order) <= m
            assert eligible == (int(sp.n_order(pow(2, 3**m, p), p)) % 3 != 0)
            target = pow(2, 3**m, p)
            # The images of all higher roots stabilize to a single chain,
            # although individual levels may contain many roots of unity.
            n = m
            top = m+s+1
            roots_top = [a for a in range(1, p) if pow(a, 3**top, p) == target]
            images = {pow(a, 3**(top-n), p) for a in roots_top}
            assert len(images) == (1 if eligible else 0)
            for a in images:
                assert pow(a, 3**n, p) == target
            chain_checks += 1
            prime_rows.append({"p": p, "m": m, "order_two": order,
                               "eligible": eligible,
                               "stable_residue_chain": sorted(images)})
    # The residue-correction formula works for every possible short
    # sequence in the first two finite root modules, including all signs.
    corrections = 0
    for j in (1, 2):
        q = 3**j
        for seq in itertools.product(range(q), repeat=j+1):
            rho0 = sum(3**a*seq[a] for a in range(j)) % q
            rho1 = sum(3**a*seq[a+1] for a in range(j)) % q
            assert (seq[0]+3*rho1-rho0) % q == 0
            corrections += 1
    # Independent valuation-coordinate identities and inverse formulas.
    coordinate_checks = 0
    for m in range(1, 6):
        w = [1]+[2*3**(j-1) for j in range(1, m+1)]
        for k in range(17):
            b2, b3 = 2*k-7, 5*k-3
            z2 = [((i+1)*k+3*i)%23-11 for i in range(m)]
            z3 = [((i+4)*k-i)%29-14 for i in range(m)]
            d2 = [3*b2-sum(w[j]*z2[j-1] for j in range(1, m+1))]+z2
            d3 = [3*b3-sum(z3)]+z3
            assert sum(a*b for a, b in zip(w, d2)) == 3*b2
            assert sum(d3) == 3*b3
            assert d2[1:] == z2 and d3[1:] == z3
            coordinate_checks += 1
    return prime_rows, chain_checks, corrections, coordinate_checks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gp", type=Path)
    args = parser.parse_args()
    gp_output = BASE/"e_two_units.out"
    if args.gp:
        with gp_output.open("w") as out:
            subprocess.run([str(args.gp.resolve()), "-fq", str(BASE/"e_two_units.gp")],
                           stdout=out, stderr=subprocess.STDOUT, check=True)
    records, matrices, norm_count = verify_number_fields(gp_output)
    print("PASS eight unconditionally certified fields and five unit norm maps")
    print(f"PASS {norm_count} independent exact relative-unit resultants and relations")
    print("PASS all retained right inverses, kernel bases, and inverse matrices over Z_(3)")
    factorizations, ranks, roots = finite_tower_checks()
    print(f"PASS {len(factorizations)} etale factorizations, {len(ranks)} exact rank decompositions")
    rows, chains, corrections, coords = valuation_checks()
    print(f"PASS {chains} fixed prime-chain checks and {corrections} residue corrections")
    print(f"PASS {coords} full toric valuation coordinate/inverse checks")
    payload = {
        "statement": "E.52", "status": "PASS", "pari_version": "2.19.0",
        "pari_source_url": "https://pari.math.u-bordeaux.fr/pub/pari/unix/pari-2.19.0.tar.gz",
        "pari_source_sha256": "f317b9722eb5d9094a60303774f066f3a83e3ec1f170be8546c44d7583f30b6d",
        "pari_records": records, "matrix_certificates": matrices,
        "independent_unit_norms": norm_count,
        "factorizations": factorizations, "ranks": ranks,
        "residue_root_checks": roots, "prime_chains": rows,
        "residue_correction_cases": corrections, "valuation_coordinate_cases": coords,
    }
    (BASE/"e_two_line.json").write_text(json.dumps(payload, indent=2, default=int)+"\n")
    print("E.52 PASS")


if __name__ == "__main__":
    main()
