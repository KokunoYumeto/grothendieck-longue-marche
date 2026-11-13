#!/usr/bin/env python3
"""Exact certificates for E.76.

With --gp /absolute/path/to/gp, rebuild the certified field, all local
norm kernels, ray quotients and actual field maps in an isolated temporary
directory. Every stage's actual combined stdout/stderr is retained next to
this program. Without --gp, verify the retained structured export. The
two deliberately failed exploratory scripts are retained but not rerun.
"""
from __future__ import annotations

import argparse
from functools import reduce
import json
from math import gcd, lcm, prod
from pathlib import Path
import shutil
import subprocess
import tempfile

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

HERE = Path(__file__).resolve().parent
STAGES = [
    ("e_basechange_field", "cyclotomic_base1"),
    ("e_basechange_local_norms", "cyclotomic_base1_local_norms"),
    ("e_basechange_unit_symbols", "cyclotomic_base1_unit_symbols"),
    ("e_basechange_genus", "cyclotomic_base1_genus"),
    ("e_basechange_ninth_norms", "cyclotomic_base1_ninth_norms"),
    ("e_basechange_ninth_genus", "cyclotomic_base1_ninth_genus"),
    ("e_basechange_ninth_transfer", "cyclotomic_base1_ninth_transfer"),
    ("e_basechange_export", "cyclotomic_base1_export"),
]


def rebuild(gp):
    gp = str(Path(gp).resolve())
    with tempfile.TemporaryDirectory(prefix="e76_exact_") as work:
        work = Path(work)
        dest = work / "research_norm_index/code"
        dest.mkdir(parents=True)
        for name, internal in STAGES:
            source = dest / (internal + ".gp")
            shutil.copyfile(HERE / (name + ".gp"), source)
            run = subprocess.run([gp, "-q", str(source)], cwd=work,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT, text=True)
            (HERE / (name + ".out")).write_text(run.stdout)
            assert run.returncode == 0, (name, run.returncode)
            assert "***   at top-level" not in run.stdout, run.stdout
            assert "***   user error" not in run.stdout, run.stdout
            assert ("DONE" in run.stdout or
                    '"status":"PASS"' in run.stdout or
                    (name == "e_basechange_unit_symbols" and
                     "CLASS_GENERATORS" in run.stdout)), name


def ints(M):
    return [[int(v) for v in row] for row in M.tolist()]


def integral(M):
    return all(v.q == 1 for v in M)


def smith(record):
    H, U, V = (sp.Matrix(record[k]) for k in ("hnf", "left", "right"))
    Ui, Vi = (sp.Matrix(record[k]) for k in ("left_inverse", "right_inverse"))
    ds = record["diagonal"]
    D = sp.diag(*ds)
    assert U * H * V == D
    assert abs(U.det()) == abs(V.det()) == 1
    assert U * Ui == Ui * U == sp.eye(H.rows)
    assert V * Vi == Vi * V == sp.eye(H.rows)
    assert integral(Ui) and integral(Vi)
    assert abs(int(H.det())) == prod(ds)
    assert all(ds[i] % ds[i + 1] == 0 for i in range(len(ds) - 1))
    return H, U, V, ds


def order_in_diagonal(v, ds):
    return lcm(*(d // gcd(d, int(a)) for d, a in zip(ds, v)))


def reduced(v, ds):
    return [int(a) % d for a, d in zip(v, ds) if d > 1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gp", help="rebuild all exact number-field stages")
    args = parser.parse_args()
    if args.gp:
        rebuild(args.gp)
    raw = (HERE / "e_basechange_export.out").read_text()
    assert "***   at top-level" not in raw
    records = [json.loads(s) for s in raw.splitlines() if s.startswith("{")]
    assert records[-1] == {"type": "completion", "status": "PASS"}
    indexed = {(r["type"], r.get("n"), r.get("prime")): r for r in records}
    field = next(r for r in records if r["type"] == "field")
    assert field["certified"] == 1
    assert field["class_group"] == [3, 3] and field["class_number"] == 9
    assert field["root_order"] == 18
    assert field["discriminant"] == -(3**27) * 17**12
    assert field["unit_norms"] == [1] * 9
    ramified = [r for r in records if r["type"] == "ramified_prime"]
    assert len(ramified) == 6
    for j, record in enumerate(ramified):
        assert record["index"] == j+1
        assert record["class"] == ([1,0] if j < 3 else [2,0])
        assert (record["rational_prime"], record["e"], record["f"]) == (
            (3,6,1) if j < 3 else (17,3,2))
        assert abs(sp.Matrix(record["ideal"]).det()) == (3 if j < 3 else 289)
    cg = [r for r in records if r["type"] == "class_generator"]
    assert len(cg) == 2
    assert [abs(int(sp.Matrix(r["ideal"]).det())) for r in cg] == [3,109]
    t, z, y = sp.symbols("t z y")
    P = sp.Poly(sum(c * t**i for i, c in enumerate(field["polynomial_ascending"])),
                t, domain=sp.QQ)

    def element(v):
        return sp.Poly(sum(sp.Rational(a, b) * t**i
                           for i, (a, b) in enumerate(v)), t, domain=sp.QQ)

    def power(a, k):
        b = sp.Poly(1, t, domain=sp.QQ)
        while k:
            if k & 1:
                b = (b*a).rem(P)
            a = (a*a).rem(P)
            k //= 2
        return b

    xi, a = element(field["xi"]), element(field["a"])
    assert power(xi, 9).as_expr() == 1
    assert (power(xi, 6) + power(xi, 3)).as_expr() + 1 == 0
    assert power(a, 3).as_expr() == 17
    assert (a - xi).as_expr() == t
    beta = (a * xi).rem(P)
    assert power(beta, 3) == 17 * power(xi, 3)
    basis = [element(v) for v in field["integral_basis"]]
    assert len(basis) == 18
    Z = sp.Matrix(18, 18, lambda i, j: basis[j].nth(i))
    assert Z.det() != 0

    # Independently verify every retained local norm determinant. All norms
    # lie in Q(beta), beta^6+17 beta^3+289=0; reduce there before embedding.
    beta6 = z**6 + 17*z**3 + 289
    beta_powers = [power(beta, i) for i in range(6)]
    determinant_checks = 0
    for n in (3, 9):
        record = indexed[("local_kernel", n, 1)]
        for k, coords in enumerate(record["norms_basis"], 1):
            u = sp.rem(1 + (y + 1)**k, y**n - z, y)
            N = sp.Poly(sp.rem(sp.resultant(y**n-z, u, y), beta6, z), z)
            expected = sum((N.nth(i)*beta_powers[i] for i in range(6)),
                           sp.Poly(0, t, domain=sp.QQ))
            actual = sum((sp.Integer(c)*b for c, b in zip(coords, basis)),
                         sp.Poly(0, t, domain=sp.QQ))
            assert actual == expected
            determinant_checks += 1

    local_checks = 0
    smith_checks = 0
    for n in (3, 9):
        for j in (1, 2, 3):
            record = indexed[("local_kernel", n, j)]
            assert record["power_quotient"] == [n]*7
            M = sp.Matrix(record["norm_matrix"])
            H, U, V, ds = smith(indexed[("local_smith", n*10+j, None)])
            assert H == hermite_normal_form((n*sp.eye(7)).row_join(M))
            assert ds == [n, 1, 1, 1, 1, 1, 1]
            ch = sp.Matrix([record["character"]])
            assert all(int(v) % n == 0 for v in ch*M)
            assert gcd(n, reduce(gcd, map(abs, record["character"]))) == 1
            assert record["norms_basis"] == indexed[("local_kernel", n, 1)]["norms_basis"]
            local_checks += 1
            smith_checks += 1

    units = {}
    genus = {}
    primes = {}
    for n in (3, 9):
        M = sp.Matrix(indexed[("global_unit_characters", n, None)]["matrix"])
        H, U, V, ds = smith(indexed[("unit_symbol_smith", n, None)])
        assert H == hermite_normal_form((n*sp.eye(6)).row_join(M))
        index = n**6 // prod(ds)
        assert index == {3: 27, 9: 2187}[n]
        units[n] = {"matrix": ints(M), "cokernel": [d for d in ds if d > 1],
                    "norm_index": index, "ambiguous_order": 9*n**5 // index}
        assert units[n]["ambiguous_order"] == {3: 81, 9: 243}[n]
        presentation = sp.Matrix(indexed[("genus_presentation", n, None)]["presentation"])
        H, U, V, ds = smith(indexed[("genus_smith", n, None)])
        assert H == hermite_normal_form(presentation)
        assert [d for d in ds if d > 1] == {3: [9, 3, 3, 3], 9: [9, 9, 9, 3]}[n]
        ray = indexed[("genus_presentation", n, None)]["ray_cyclic"]
        assert presentation[:, :len(ray)] == sp.diag(*ray)
        assert prod(ds) == 9*n**6 // index
        genus[n] = (H, U, V, ds)
        primes[n] = []
        for j in (1, 2, 3):
            record = indexed[("prime_frobenius", n, j)]
            cl = sp.Matrix(record["ray_class"])
            coord = sp.Matrix(record["smith_coordinates"])
            assert coord == U*cl
            assert order_in_diagonal(coord, ds) == 3
            primes[n].append((cl, reduced(coord, ds)))
        smith_checks += 2
    assert [v for _, v in primes[3]] == [[3, 1, 0, 1]]*3
    assert [v for _, v in primes[9]] == [[3, 6, 0, 2], [6, 6, 6, 2], [0, 6, 3, 2]]

    maps = indexed[("actual_maps", None, None)]
    H, U, V, ds = genus[9]
    D = sp.Matrix(maps["delta"])
    r = H.rows
    assert integral(H.inv()*D*H)
    assert integral(H.inv()*(D**3-sp.eye(r)))
    outer = indexed[("outer_delta_smith", 9, None)]
    OH, OU, OV, ods = smith(outer)
    assert OH == hermite_normal_form(H.row_join(D-sp.eye(r)))
    assert [x for x in ods if x > 1] == [3, 3, 3]
    K = sp.Matrix(maps["kummer_kernel_basis"])
    chi = sp.Matrix([maps["kummer_character"]])
    assert abs(K.det()) == 9 and integral(K.inv()*H)
    assert all(int(v) % 9 == 0 for v in chi*K)
    AH = sp.Matrix(maps["relative_class_presentation"])
    assert AH == K.inv()*H
    A_smith = smith_normal_form(AH, domain=sp.ZZ)
    assert sorted(abs(int(A_smith[i,i])) for i in range(r) if abs(A_smith[i,i]) > 1) == [3,9,9]
    AP = sp.Matrix(maps["relative_delta_presentation"])
    assert AP == AH.row_join(K.inv()*(D-sp.eye(r))*K)
    RH, RU, RV, rds = smith(indexed[("relative_delta_smith", 9, None)])
    assert RH == hermite_normal_form(AP)
    assert [x for x in rds if x > 1] == [3, 3]
    for j in (1, 2, 3):
        record = indexed[("relative_prime", None, j)]
        cl = primes[9][j-1][0]
        v = sp.Matrix(record["kernel_coordinates"])
        assert K*v == cl
        assert sp.Matrix(record["smith_coordinates"]) == RU*v
        assert record["order"] == order_in_diagonal(RU*v, rds) == 3
        assert reduced(RU*v, rds) == [2,0]
    smith_checks += 2

    Q = sp.Matrix(maps["genus_restriction"])
    H3 = genus[3][0]
    assert integral(H3.inv()*Q*H)
    assert hermite_normal_form(H3.row_join(Q)) == sp.eye(H3.rows)
    for j in range(3):
        assert integral(H3.inv()*(Q*primes[9][j][0]-primes[3][j][0]))
    G = sp.Matrix(maps["ray_basis_change"])
    W = sp.Matrix(maps["ray_basis_inverse"])
    ray = indexed[("genus_presentation", 9, None)]["ray_cyclic"]
    assert integral(sp.diag(*ray).inv()*(G*W-sp.eye(r)))
    raw_chi = []
    residue_count = 0
    for j, factors in maps["kummer_prime_records"]:
        assert j == len(raw_chi)+1
        for p, f, e, value in factors:
            assert p not in (3,17) and (p**f-1) % 9 == 0
            assert sp.isprime(p)
            residue_count += 1
        raw_chi.append(sum(e*value for p,f,e,value in factors) % 9)
    assert all(int(v) % 9 == 0 for v in sp.Matrix([raw_chi])*W-chi)
    assert all(int(v) % 9 == 0 for v in chi*H)

    result = {
        "status": "PASS", "statement": "E.76",
        "certified_class_group": [3,3], "certified_class_number":9,
        "complete_fundamental_unit_rank":8,
        "ramified_prime_class_coordinates": [[1,0]]*3+[[2,0]]*3,
        "local_norm_kernel_certificates":local_checks,
        "independent_exact_norm_determinants":determinant_checks,
        "full_integer_smith_inverse_certificates":smith_checks,
        "actual_kummer_prime_factors":residue_count,
        "unit_norm_characters":units,
        "genus_cyclic": {3:[9,3,3,3],9:[9,9,9,3]},
        "prime_genus_coordinates":{n:[v for _,v in primes[n]] for n in (3,9)},
        "relative_unramified_cyclic":[9,9,3],
        "outer_delta_coinvariants":[3,3,3],
        "relative_delta_coinvariants":[3,3],
        "original_prime_detected_coordinates":[[2,0]]*3,
        "original_prime_detected_order":3,
        "h":"unevaluated", "original_q3_level3_order":"3 or 9",
        "retained_failed_attempts":[
            "e_basechange_genus_polmod_attempt.gp/.out: documented polynomial input required for bnrgaloismatrix",
            "e_basechange_transfer_basis_attempt.gp/.out: implicit and explicit ray generators differ; resolved by actual inverse modulo cyclic relations",
            "e_basechange_polynomial_domain_attempt.py/.out: equal polynomial values had distinct SymPy coefficient domains; exact expression comparison fixes the check",
            "e_basechange_driver_marker_attempt.py/.out: one successful GP stage has CLASS_GENERATORS rather than DONE as its final record"
        ]
    }
    (HERE / "e_cyclotomic_basechange.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
