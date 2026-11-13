"""Step 4 (Claude Fable 5.2 at effort max): the same splitting in Lie degree three (the class-three layer
L_3(N) = Lie_3(V), rank 330), computed directly and by pieces.

Lie_3(V) is realised as the saturated sublattice of V^{(x)3} spanned by the Hall elements
[[e_i, e_j], e_k], i > j <= k  (free Lie ring inside the free associative ring).
Lie_3(A (+) B) = Lie_3(A) (+) A(x)A(x)B (+) A(x)B(x)B (+) Lie_3(B)   (multidegrees), so with V = V_1 (+) chi*D_0:
  Lie_3(V) = Lie_3(V_1) (+) chi*(V_1(x)V_1)(x)D_0 (+) chi^2*V_1(x)(D_0(x)D_0) (+) chi^3*Lie_3(D_0).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from fable_e102_lib import *
from fable_step3_tests import core_data, rank_mod3


def hall3(n):
    return [(i, j, k) for i in range(n) for j in range(i) for k in range(j, n)]


def lie3_embedding(n):
    basis = hall3(n)
    B = np.zeros((n ** 3, len(basis)), dtype=np.int64)
    idx = lambda a, b, c: (a * n + b) * n + c
    for col, (i, j, k) in enumerate(basis):
        B[idx(i, j, k), col] += 1
        B[idx(j, i, k), col] -= 1
        B[idx(k, i, j), col] -= 1
        B[idx(k, j, i), col] += 1
    return basis, B


def independent_rows_mod3(B):
    """Indices of rows of B forming a square submatrix invertible mod 3 (greedy)."""
    d = B.shape[1]
    ech = np.zeros((0, d), dtype=np.int64)
    piv_cols, rows = [], []
    for r in range(B.shape[0]):
        v = B[r] % 3
        for e, pc in zip(ech, piv_cols):
            if v[pc]:
                v = (v - v[pc] * e) % 3
        nz = np.nonzero(v)[0]
        if len(nz) == 0:
            continue
        pc = int(nz[0])
        v = (v * pow(int(v[pc]), -1, 3)) % 3
        ech = np.vstack([ech, v]); piv_cols.append(pc); rows.append(r)
        if len(rows) == d:
            break
    assert len(rows) == d
    return rows


def inv_mod(M, mod):
    n = M.shape[0]
    A = np.concatenate([np.array(M % mod, dtype=np.int64), np.eye(n, dtype=np.int64)], axis=1)
    for c in range(n):
        piv = next(i for i in range(c, n) if A[i, c] % 3)
        if piv != c:
            A[[c, piv]] = A[[piv, c]]
        A[c] = (A[c] * pow(int(A[c, c]), -1, mod)) % mod
        col = A[:, c].copy(); col[c] = 0
        A = (A - col[:, None] * A[c][None, :]) % mod
    return A[:, n:]


def lie3(A, prec):
    mod = 3 ** prec
    n = A.shape[0]
    basis, B = lie3_embedding(n)
    A = np.asarray(A, dtype=np.int64) % mod
    A2 = np.kron(A, A) % mod
    AB = B.copy()
    # apply A (x) A (x) A to the columns of B without forming the n^3 x n^3 matrix when n is large
    A3B = (np.kron(A2, A) % mod) @ B % mod if n <= 6 else None
    if A3B is None:
        Bt = B.T.reshape(len(basis), n, n, n).astype(np.int64)        # [col, a, b, c]
        X = np.einsum('ia,zabc->zibc', A, Bt) % mod
        X = np.einsum('jb,zibc->zijc', A, X) % mod
        X = np.einsum('kc,zijc->zijk', A, X) % mod
        A3B = X.reshape(len(basis), n ** 3).T
    rows = independent_rows_mod3(B)
    Binv = inv_mod(B[rows], mod)
    M = (Binv @ A3B[rows]) % mod
    assert np.array_equal((B @ M) % mod, A3B % mod), "Lie_3 is not stable / basis is not saturated"
    return M


def lie3_signs(signs):
    n = len(signs)
    p = sum(1 for (i, j, k) in hall3(n) if signs[i] * signs[j] * signs[k] == 1)
    return p, len(hall3(n)) - p


def run(pi=(1, 3), chi=7, gtype="2", dp=2, dm=4, prec=10):
    mod = 3 ** prec
    Tc, Jc = core_data(pi, chi, gtype)
    one = np.array([[1]], dtype=np.int64)
    lp, lm = lie3_signs([1] * dp + [-1] * dm)
    mods = {
        "Lie_3 V1": (lie3(Tc, prec), lie3(Jc, prec), (1, 0)),
        "chi V1(x)V1": (chi * kron(Tc, Tc), kron(Jc, Jc), (dp, dm)),
        "chi^2 V1": (chi ** 2 * Tc, Jc, (dp * dp + dm * dm, 2 * dp * dm)),
        "chi^3": (chi ** 3 * one, one, (lp, lm)),
    }
    tot = Counter(); free = 0
    print("degree three, pieces (pi=%s, chi=%d, glue %s, D_0 signs (%d,%d)):" % (pi, chi, gtype, dp, dm))
    for name, (TM, JM, (mp, mm)) in mods.items():
        TM = TM % mod
        fp, qp, _ = coker_type(TM, JM, +1, prec)
        fm, qm, _ = coker_type(TM, JM, -1, prec)
        print("  %-12s rank %2d mult (%d,%d) | Q+ = %-22s | Q- = %-22s" % (name, TM.shape[0], mp, mm, fmt(qp), fmt(qm)))
        for e, k in qp.items():
            tot[e] += k * mp
        for e, k in qm.items():
            tot[e] += k * mm
        free += fp * mp + fm * mm
    return free, {e: k for e, k in sorted(tot.items()) if k}


if __name__ == "__main__":
    prec = 10
    free_f, tors_f = run(prec=prec)
    print("FORMULA degree 3: Z^%d + %s" % (free_f, fmt(tors_f)))
    T1, J1 = actual_data()
    T3, J3 = lie3(T1, prec), lie3(J1, prec)
    assert np.array_equal((J3 @ J3) % 3 ** prec, np.eye(330, dtype=np.int64))
    tr = int(np.trace(J3 % 3 ** prec)); tr = tr % 3 ** prec; tr = tr - 3 ** prec if tr > 3 ** prec // 2 else tr
    free_d, tors_d, unit_d = coker_type(T3, J3, +1, prec)
    print("DIRECT  degree 3: rank 330, trace J %d | Z^%d + %s (unit %d)" % (tr, free_d, fmt(tors_d), unit_d))
    print("AGREE" if (free_d, tors_d) == (free_f, tors_f) else "DIFFER")
    # degree two for completeness: L_2 = Lambda^2 V = Lambda^2 V1 (+) chi V1 (x) D_0 (+) chi^2 Lambda^2 D_0
    Tc, Jc = core_data((1, 3), 7, "2")
    mod = 3 ** prec
    print("degree two pieces: L2 V1:", [fmt(coker_type(wedge2(Tc) % mod, wedge2(Jc), s, prec)[1]) for s in (1, -1)],
          "| chi V1:", [fmt(coker_type(7 * Tc % mod, Jc, s, prec)[1]) for s in (1, -1)],
          "| chi^2:", fmt(coker_type(np.array([[49]]), np.array([[1]]), 1, prec)[1]))
    f2, t2, u2 = coker_type(wedge2(T1) % mod, wedge2(J1), +1, prec)
    print("DIRECT degree 2: Z^%d + %s" % (f2, fmt(t2)))
    f1, t1, u1 = coker_type(T1 % mod, J1, +1, prec)
    print("DIRECT degree 1: Z^%d + %s" % (f1, fmt(t1)))
