"""Independent recomputation of LM7_FERMAT_TOWER E.102 and a search for the formula behind it (main session,
Claude Opus 5.5 at effort max, 13 Nov 2026). Own code; only the degree-one data are taken from the return's
definitions (arithmetic_inputs in code/e100_root_rebuild/inputs/e_unramified_sections.py, read, not run).
K_4 = ker(L_4(N) -> L_4(N/N'')) = [L_2, L_2] = Lambda^2(Lambda^2 V), V = N^ab = Z_3^10, functorial in the action
on V. C_4 = K_4 / (T-1) K_4^{J=+1}."""
import itertools, sys
import numpy as np

P, PREC = 3, 9
MOD = P ** PREC


def vmat(E, T, U):
    A = np.zeros((10, 10), dtype=np.int64)
    A[:2, :2] = E
    A[2:, 2:] = T
    for i in range(8):
        for j in range(2):
            num = sum(U[i][k] * E[k][j] for k in range(2)) - sum(T[i][k] * U[k][j] for k in range(8))
            assert num % 3 == 0
            A[2 + i, j] = num // 3
    return A


cusps = [(1, 0), (2, 2), (0, 1), (2, 0), (1, 1), (0, 2), (2, 1), (1, 2)]
U = [(v, -u) for u, v in cusps]
CT = np.zeros((8, 8), dtype=np.int64)
for j, i in enumerate([0, 2, 1, 3, 5, 4, 7, 6]):
    CT[i][j] = -1
E_tau = np.array([[1, -3], [3, -2]])
T1 = vmat(E_tau, 7 * np.eye(8, dtype=np.int64), U)
J1 = vmat(np.array([[1, -1], [0, -1]]), CT, U)
assert np.array_equal(J1 @ J1, np.eye(10, dtype=np.int64))


def wedge2(A):
    A = np.asarray(A, dtype=np.int64)
    pairs = np.array(list(itertools.combinations(range(A.shape[0]), 2)))
    i0, i1 = pairs[:, 0], pairs[:, 1]
    return (A[np.ix_(i0, i0)] * A[np.ix_(i1, i1)] - A[np.ix_(i1, i0)] * A[np.ix_(i0, i1)])


def smith_vals(A):
    """3-adic Smith exponents of an integer matrix (mod 3^PREC); PREC means 0 at this precision."""
    A = np.array(A % MOD, dtype=np.int64)
    n, m = A.shape
    vals = []
    val = np.zeros(MOD, dtype=np.int8)
    for a in range(MOD):
        b, v = a, 0
        if a == 0:
            v = PREC
        else:
            while b % 3 == 0:
                b //= 3; v += 1
        val[a] = v
    for k in range(min(n, m)):
        V = val[A[k:, k:]]
        pos = int(V.argmin()); i, j = divmod(pos, m - k); v = int(V[i, j])
        if v >= PREC:
            vals += [PREC] * (min(n, m) - k); break
        i += k; j += k
        A[[k, i], :] = A[[i, k], :]; A[:, [k, j]] = A[:, [j, k]]
        piv = int(A[k, k]); unit = piv // 3 ** v; inv = pow(unit, -1, MOD)
        A[k, :] = (A[k, :] * inv) % MOD
        col = A[k + 1:, k] // 3 ** v
        A[k + 1:, k:] = (A[k + 1:, k:] - col[:, None] * A[k, k:]) % MOD
        row = A[k, k + 1:] // 3 ** v
        A[k:, k + 1:] = (A[k:, k + 1:] - A[k:, k][:, None] * row[None, :]) % MOD
        vals.append(v)
    return vals


def run(T1, J1, label):
    T4, J4 = wedge2(wedge2(T1)), wedge2(wedge2(J1))
    n = T4.shape[0]
    I = np.eye(n, dtype=np.int64)
    assert np.array_equal(J4 @ J4, I)
    Cm = (((T4 - I) % MOD) @ ((I + J4) % MOD)) % MOD
    vals = smith_vals(Cm)
    from collections import Counter
    c = Counter(vals)
    tors = {3 ** e: k for e, k in sorted(c.items()) if 0 < e < PREC}
    print(label, "| rank K4", n, "| trace J4", int(np.trace(J4)), "| unit pivots", c.get(0, 0),
          "| torsion", tors, "| free", c.get(PREC, 0), "| torsion exponent", sum(e * k for e, k in c.items() if 0 < e < PREC))
    sys.stdout.flush()


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "both"
    if which in ("actual", "both"):
        run(T1, J1, "ACTUAL (non-split extension, the return's data)")
    if which in ("split", "both"):
        T1s, J1s = T1.copy(), J1.copy()
        T1s[2:, :2] = 0; J1s[2:, :2] = 0
        run(T1s, J1s, "SPLIT (off-diagonal extension block set to 0)")
