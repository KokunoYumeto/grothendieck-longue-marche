#!/usr/bin/env python3
"""E.74 exact wild local Smith cokernels from the E.41 Hall matrices.

For r=1,2 the integer Smith decomposition and both inverses are retained.
For r=3 all elementary 3-adic operations, both modular transformations
and both inverses are retained and checked. The split-lattice identity
proves torsion exponent <=3^5, so modulus3^6 determines the exact answer.
"""
from __future__ import annotations

import importlib.util
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
INPUT = ROOT / "LM7_FERMAT_TOWER/code/e_unramified_sections.py"
spec = importlib.util.spec_from_file_location("e41_hall", INPUT)
hall = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(hall)


def dense(columns):
    n = len(columns)
    ans = np.zeros((n, n), dtype=np.int64)
    for j, column in enumerate(columns):
        for i, value in column.items():
            ans[i, j] = value
    return ans


def v3(n):
    assert n
    n = abs(n)
    e = 0
    while n % 3 == 0:
        e += 1
        n //= 3
    return e


def integer_smith(matrix):
    A = sp.Matrix(matrix.tolist())
    dm = DomainMatrix.from_Matrix(A).convert_to(sp.ZZ)
    dd, ll, rr = smith_normal_decomp(dm)
    D, L, R = (x.to_Matrix() for x in (dd, ll, rr))
    assert D == L * A * R
    Li, Ri = L.inv(), R.inv()
    assert all(x.q == 1 for x in Li) and all(x.q == 1 for x in Ri)
    assert L * Li == sp.eye(L.rows) and Li * L == sp.eye(L.rows)
    assert R * Ri == sp.eye(R.rows) and Ri * R == sp.eye(R.rows)
    diagonals = [int(D[i, i]) for i in range(D.rows) if D[i, i]]
    vals = [v3(d) for d in diagonals]
    return {
        "integer_Smith_diagonal": diagonals,
        "Smith_valuation_counts": dict(sorted(Counter(vals).items())),
        "free_rank": D.rows - len(vals),
        "left_transform": [[int(x) for x in L.row(i)] for i in range(L.rows)],
        "right_transform": [[int(x) for x in R.row(i)] for i in range(R.rows)],
        "left_inverse": [[int(x) for x in Li.row(i)] for i in range(Li.rows)],
        "right_inverse": [[int(x) for x in Ri.row(i)] for i in range(Ri.rows)],
        "verified": ["exact_Smith_identity", "integer_inverse_left",
                     "integer_inverse_right", "all_inverse_products"]
    }


def modular_smith(matrix, modulus):
    A = matrix.copy() % modulus
    m, n = A.shape
    L, R = np.eye(m, dtype=np.int64), np.eye(n, dtype=np.int64)
    Li, Ri = L.copy(), R.copy()
    vals, operations = [], []
    precision = v3(modulus)
    for k in range(min(m, n)):
        sub = A[k:, k:]
        if not np.any(sub):
            break
        for valuation in range(precision):
            power = 3**valuation
            candidates = np.argwhere((sub % power == 0) & (sub % (3*power) != 0))
            if len(candidates):
                i, j = map(int, candidates[0] + k)
                break
        else:
            raise AssertionError("No nonzero pivot.")
        if i != k:
            A[[i, k]] = A[[k, i]]
            L[[i, k]] = L[[k, i]]
            Li[:, [i, k]] = Li[:, [k, i]]
        if j != k:
            A[:, [j, k]] = A[:, [k, j]]
            R[:, [j, k]] = R[:, [k, j]]
            Ri[[j, k]] = Ri[[k, j]]
        power = 3**valuation
        unit = int(A[k, k]) // power
        inverse = pow(unit, -1, modulus)
        A[k] = A[k] * inverse % modulus
        L[k] = L[k] * inverse % modulus
        Li[:, k] = Li[:, k] * unit % modulus
        assert A[k, k] == power
        assert np.all(A[:, k] % power == 0)
        factors = A[:, k] // power
        factors[k] = 0
        A = (A - factors[:, None] * A[k][None, :]) % modulus
        L = (L - factors[:, None] * L[k][None, :]) % modulus
        Li[:, k] = (Li[:, k] + Li @ factors) % modulus
        assert np.all(A[k, :] % power == 0)
        factors2 = A[k, :] // power
        factors2[k] = 0
        A = (A - A[:, k][:, None] * factors2[None, :]) % modulus
        R = (R - R[:, k][:, None] * factors2[None, :]) % modulus
        Ri[k] = (Ri[k] + factors2 @ Ri) % modulus
        vals.append(valuation)
        operations.append({
            "pivot": k, "row_swap": i, "column_swap": j,
            "row_unit": unit, "row_unit_inverse": inverse,
            "valuation": valuation,
            "row_elimination": factors.tolist(),
            "column_elimination": factors2.tolist()
        })
    diagonal = np.zeros_like(A)
    for k, valuation in enumerate(vals):
        diagonal[k, k] = 3**valuation
    assert np.array_equal(A, diagonal)
    assert np.array_equal((L @ (matrix % modulus) % modulus @ R) % modulus, A)
    for P, Q in [(L, Li), (Li, L), (R, Ri), (Ri, R)]:
        assert np.array_equal(P @ Q % modulus, np.eye(P.shape[0], dtype=np.int64))
    return vals, L, R, Li, Ri, operations


def main():
    inputs = hall.arithmetic_inputs()
    H, C = hall.Hall(3), hall.Chen(3)
    output = {
        "source_matrices": "E41 arithmetic_inputs and integral Hall substitution",
        "cokernel_presentation": "[T_r-7I | J_r+I]",
        "layers": {}, "status": "PASS"
    }
    for degree in [1, 2, 3]:
        matrices = {key: dense(H.action(value, degree)[0])
                    for key, value in inputs.items()}
        T, J = matrices["tau"], matrices["c"]
        n = len(T)
        I = np.eye(n, dtype=np.int64)
        assert np.array_equal(J @ J, I)
        for key in ["tau", "c"]:
            assert np.array_equal(dense(H.action(inputs[key], degree, marked=True)[0]),
                                  matrices[key])
            assert np.array_equal(dense(C.action(inputs[key], degree)[0]), matrices[key])
        A = np.hstack([T - 7*I, J + I])
        row = {
            "degree": degree, "rank": n,
            "input_tau": T.tolist(), "input_c": J.tolist(),
            "matrix": A.tolist(),
            "all_three_targets_agree": True
        }
        if degree <= 2:
            row.update(integer_smith(A))
            assert row["free_rank"] == {1: 5, 2: 1}[degree]
        else:
            b = max(1 + v3(j) for j in range(degree-2, 2*degree-1))
            bound, modulus = degree+b, 3**(degree+b+1)
            assert bound == 5 and modulus == 729
            vals, L, R, Li, Ri, ops = modular_smith(A, modulus)
            assert len(vals) == n and max(vals) <= bound
            B, C0 = matrices["B"], matrices["C"]
            F, Fs = matrices["Frob_K2"], matrices["split_Frob_K2"]
            assert np.array_equal(B @ C0, 3**degree * I)
            assert np.array_equal(F @ B, B @ Fs)
            eigenvalues = sorted(set(map(int, np.diag(Fs))))
            assert np.array_equal(Fs, np.diag(np.diag(Fs)))
            fractions = [Fraction(3**b, e-4) for e in eigenvalues]
            assert all(f.denominator % 3 for f in fractions)
            np.savez_compressed(
                HERE / "e_wild_layers_r3_transforms.npz",
                matrix=A, left=L, right=R, left_inverse=Li, right_inverse=Ri,
                split_embedding=B, split_back=C0, split_Frobenius=Fs)
            row.update({
                "modulus": modulus, "torsion_bound_exponent": bound,
                "Smith_valuation_counts": dict(sorted(Counter(vals).items())),
                "free_rank": n-len(vals), "elementary_operations": ops,
                "transform_archive": "e_wild_layers_r3_transforms.npz",
                "split_Frobenius_eigenvalues": eigenvalues,
                "denominator_certificate": [str(f) for f in fractions],
                "verified": ["modular_Smith_identity", "both_inverse_pairs",
                             "split_embedding_identity", "Frobenius_intertwiner",
                             "torsion_precision_bound"]
            })
        row["H1_free_rank"] = n + row["free_rank"]
        output["layers"][degree] = row
        print("DEGREE", degree, "RANK", n,
              "SMITH", row["Smith_valuation_counts"],
              "FREE", row["free_rank"], "H1_FREE", row["H1_free_rank"], flush=True)
    (HERE / "e_wild_layers.json").write_text(json.dumps(output, separators=(",", ":")) + "\n")
    print("PASS: exact integer maps in degrees1,2; verified modular maps/inverses and precision in degree3.",
          flush=True)


if __name__ == "__main__":
    main()
