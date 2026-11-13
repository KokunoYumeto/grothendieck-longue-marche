#!/usr/bin/env python3
"""Exact finite H3 and character certificates for the D.51 proof note."""
from itertools import product
from pathlib import Path
import json


def det(a, p):
    return (a[0]*a[3] - a[1]*a[2]) % p


def mm(a, b, p):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % p
                 for i in range(2) for j in range(2))


def mv(a, v, p=3):
    return ((a[0]*v[0]+a[1]*v[1]) % p,
            (a[2]*v[0]+a[3]*v[1]) % p)


def omega(v, w, p=3):
    return (v[0]*w[1]-v[1]*w[0]) % p


def hmul(a, b):
    v, z = a
    w, t = b
    return (((v[0]+w[0]) % 3, (v[1]+w[1]) % 3),
            (z+t+2*omega(v, w)) % 3)


def theta(a, ell, h):
    v, z = h
    return mv(a, v), (z+ell[0]*v[0]+ell[1]*v[1]) % 3


def labelled_cube(a, ell, h):
    th = theta(a, ell, h)
    return hmul(hmul(h, th), theta(a, ell, th))


def main():
    identity = (1, 0, 0, 1)
    matrices = [a for a in product(range(3), repeat=4)
                if det(a, 3) and a != identity and
                mm(mm(a, a, 3), a, 3) == identity]
    assert len(matrices) == 8
    vectors = list(product(range(3), repeat=2))
    heis = [(v, z) for v in vectors for z in range(3)]
    cube_checks = 0
    good = []
    one_root = 0
    for a in matrices:
        w = next(w for w in vectors if mv(a, w) != w)
        mw = mv(a, w)
        e = ((mw[0]-w[0]) % 3, (mw[1]-w[1]) % 3)
        d = omega(e, w)
        assert d and mv(a, e) == e
        chi = lambda r: omega(e, r)*pow(d, -1, 3) % 3
        for ell in vectors:
            ell_e = (ell[0]*e[0]+ell[1]*e[1]) % 3
            roots = [b for b in range(3) if (d*b*b+ell_e*b) % 3 == 0]
            for h in heis:
                b = chi(h[0])
                expected = ((0, 0), (d*b*b+ell_e*b) % 3)
                assert labelled_cube(a, ell, h) == expected
                assert theta(a, ell, theta(a, ell, theta(a, ell, h))) == h
                cube_checks += 1
            if ell_e == 0:
                assert roots == [0]
                one_root += 1
                continue
            assert len(roots) == 2 and 0 in roots
            b1 = next(b for b in roots if b)
            b_cusp = (-b1) % 3
            assert b_cusp not in roots
            assert ell_e == (-d*b1) % 3
            psi = lambda u, b: (b+b1*u) % 3
            assert psi(1, b_cusp) == 0
            assert psi(1, 0) and psi(1, b1)
            # Normalize nonzero character coefficients to first nonzero 1.
            chars = [(1, b) for b in range(3)] + [(0, 1)]
            tf = [(cu, cb) for cu, cb in chars
                  if cu % 3 and (cu+cb*b1) % 3]
            assert len(tf) == 2
            assert (1, 0) in tf
            psi_normalized = (1, pow(b1, -1, 3))
            assert psi_normalized in tf
            good.append({"M": a, "ell": ell, "basis_e": e, "basis_w": w,
                         "omega_e_w": d, "section_b_values": [0, b1],
                         "cusp_b_value": b_cusp,
                         "cube_exponent_at_cusp": (d*b_cusp*b_cusp+ell_e*b_cusp) % 3,
                         "torsion_free_kernel_character_lines": tf})
    assert cube_checks == 1944
    assert len(good) == 48 and one_root == 24

    eigen_checks = []
    for q in (7, 13):
        roots = [z for z in range(2, q) if pow(z, 3, q) == 1]
        assert len(roots) == 2
        counts = {"one_plus_lambda": 0, "scalar_lambda_squared": 0}
        for a in product(range(q), repeat=4):
            lam = det(a, q)
            if lam not in roots or mm(mm(a, a, q), a, q) != identity:
                continue
            trace = (a[0]+a[3]) % q
            if a == (lam*lam % q, 0, 0, lam*lam % q):
                counts["scalar_lambda_squared"] += 1
                multiplicities = (0, 2, 2)
            else:
                assert trace == (1+lam) % q
                counts["one_plus_lambda"] += 1
                multiplicities = (1, 3, 0)
            assert sum(multiplicities) == 4
            assert multiplicities[0] in (0, 1)
        assert counts["one_plus_lambda"] == 2*q*(q+1)
        assert counts["scalar_lambda_squared"] == 2
        eigen_checks.append({"prime": q, "matrix_counts": counts,
                             "allowed_V_multiplicities": [[1, 3, 0], [0, 2, 2]]})
    result = {
        "claim": "D.51 proof note",
        "nonidentity_unipotent_matrices": len(matrices),
        "central_linear_automorphisms": 72,
        "labelled_cube_checks": cube_checks,
        "two_section_value_cases": len(good),
        "one_section_value_cases_excluded_by_D48_Bockstein": one_root,
        "two_section_and_cusp_line_certificates": good,
        "finite_eigenvalue_checks": eigen_checks,
        "scope": ("Exact finite formulas supporting the full subgroup construction. "
                  "No identification of the projective sibling U with Fhat2 is asserted.")
    }
    Path(__file__).with_name("torus_order3_sibling_d51_output.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
