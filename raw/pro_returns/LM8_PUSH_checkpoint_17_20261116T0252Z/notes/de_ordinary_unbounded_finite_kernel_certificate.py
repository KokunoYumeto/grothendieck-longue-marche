"""Exact D93 candidate certificate.

This executes literal integral matrices for r=1,2 and checks the displayed
actual-action specialization and natural zero map.  The all-r determinant
and arithmetic arguments are proved in the TeX draft, not inferred here.
run() is read-only and returns the full certificate for independent replay.
"""
from pathlib import Path
import hashlib
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


def v5(n):
    n = abs(int(n))
    assert n
    value = 0
    while n % 5 == 0:
        value += 1
        n //= 5
    return value


def run():
    rows = []
    for r in (1, 2):
        n = 5**r
        eye = sp.eye(n)
        T = sp.Matrix(n, n, lambda i, j: int(i == (j + 1) % n))
        perm = sp.Matrix(n, n, lambda i, j: int(i == (2 * j) % n))
        assert T**n == eye
        q = T**n - eye
        assert q == sp.zeros(n)
        # On R/(q), both t1^(5^r) and t2 are exactly one.
        # Cartier untwist 1/2, retained q factor 2, second axis factor 2,
        # first axis factor (I+T), and retained u^2 factor (I+T)^2.
        raw_action = sp.Rational(1, 2) * (2 * eye) * (eye + T) * (
            2 * eye
        ) * (eye + T)**2 * perm
        M = 2 * (eye + T)**3 * perm
        assert raw_action == M
        assert q * M == sp.zeros(n)
        D = smith_normal_form(M - eye, domain=sp.ZZ)
        diagonal = [abs(int(D[i, i])) for i in range(n)]
        assert all(diagonal)
        valuations = [v5(z) for z in diagonal if z % 5 == 0]
        expected = [2] if r == 1 else [1, 3]
        assert valuations == expected
        exact_det = int((eye - M).det())
        fourier_det = 1 - 16
        for j in range(1, r + 1):
            fourier_det *= 1 - 2 ** (4 * 5 ** (j - 1))
        assert exact_det == fourier_det
        assert v5(exact_det) == 1 + r * (r + 1) // 2
        t = 2**n
        B = t - 1
        h = 2 ** (5 ** (r - 1))
        assert (h - 1)**5 < B < h**5
        assert sp.gcd(B, 10) == 1
        rows.append({
            "r": r,
            "matrix_dimension": n,
            "actual_point": str(t),
            "second_kummer_integer": str(B),
            "second_coordinate_factorization": {
                str(p): int(e) for p, e in sp.factorint(B).items()
            },
            "integer_smith_diagonal": diagonal,
            "five_primary_elementary_divisor_valuations": valuations,
            "free_rank": 0,
            "exact_det_I_minus_M": str(exact_det),
            "fourier_det_I_minus_M": str(fourier_det),
            "compact_kernel_order": str(5 ** (1 + r * (r + 1) // 2)),
            "actual_action_specialization": True,
            "actual_q_multiplication_map_zero": True,
            "non_fifth_power_inequality": True,
        })
    # Low jets have weights chi^2 and chi^3.  At chi=2 their differences
    # are 3 and 7, which are units; the proof uses tame averaging exactly.
    assert sp.gcd((2**2 - 1) * (2**3 - 1), 5) == 1
    residue_rows = []
    for r in range(1, 31):
        t_mod_25 = pow(2, pow(5, r, 20), 25)
        b_mod_25 = (1 - t_mod_25) % 25
        assert t_mod_25 == 7 and b_mod_25 == 19
        # For a unit x, lambda_x mod5=((x^4-1)/5)/4 mod5.
        # The expression only needs x modulo25.
        lambda_b = (((b_mod_25**4 - 1) // 5) * pow(4, -1, 5)) % 5
        assert lambda_b == 1
        residue_rows.append({
            "r": r, "point_mod25": t_mod_25,
            "one_minus_point_mod25": b_mod_25,
            "second_unit_log_coefficient_mod5": lambda_b,
        })
    lambda_two = (((2**4 - 1) // 5) * pow(4, -1, 5)) % 5
    assert lambda_two == 2
    return {
        "candidate": "D.93, notes-only and unregistered",
        "status": "PASS",
        "scope": "Exact r=1,2 integral Smith matrices and displayed identities; "
                 "the all-depth proof is in the draft, with no extrapolated Smith pattern.",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "matrix_rows": rows,
        "low_jet_difference_determinant": 21,
        "first_unit_log_coefficient_mod5": lambda_two,
        "unit_log_residue_rows": residue_rows,
        "all_depth_order_formula": "5^(1+r*(r+1)/2), proved by the Fourier-cycle determinant",
    }


if __name__ == "__main__":
    result = run()
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
