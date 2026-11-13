"""Library for the E.102 formula search (Claude Fable 5.2 at effort max, 13 Nov 2026).

Own code.  Only the degree-one data (the genus block of tau, the cusp block 7*I, the cusp labels and the
conjugation) are taken from the definitions in arithmetic_inputs() of the return's
code/e100_root_rebuild/inputs/e_unramified_sections.py (code of GPT-6 Astra (ChatGPT Pro mode); read, never run).

Conventions.  O = Z_3[zeta], zeta^2 + zeta + 1 = 0, basis (1, zeta).  W = O, C = cusp loops.
Matrices act on column vectors: M[i, j] is the coefficient of e_i in the image of e_j.
"""
import itertools
from collections import Counter

import numpy as np

P = 3


# ----------------------------------------------------------------------------------------------------------
# 3-adic linear algebra modulo 3^prec
# ----------------------------------------------------------------------------------------------------------

def valuation_array(A, prec):
    """Entrywise 3-adic valuation of A modulo 3^prec (prec = 'zero at this precision')."""
    A = np.asarray(A, dtype=np.int64) % (P ** prec)
    v = np.zeros(A.shape, dtype=np.int64)
    q = 1
    for _ in range(prec):
        q *= P
        v += (A % q == 0)
    return v


def smith_exponents(A, prec):
    """Exponents e_1 <= e_2 <= ... of the 3-adic Smith form of the integer matrix A, computed modulo 3^prec.
    An exponent equal to prec means: zero modulo 3^prec."""
    mod = P ** prec
    A = np.array(np.asarray(A, dtype=np.int64) % mod, dtype=np.int64)
    n, m = A.shape
    out = []
    for k in range(min(n, m)):
        V = valuation_array(A[k:, k:], prec)
        pos = int(V.argmin())
        i, j = divmod(pos, m - k)
        v = int(V[i, j])
        if v >= prec:
            out += [prec] * (min(n, m) - k)
            break
        i += k
        j += k
        if i != k:
            A[[k, i], :] = A[[i, k], :]
        if j != k:
            A[:, [k, j]] = A[:, [j, k]]
        piv = int(A[k, k])
        unit = piv // P ** v
        inv = pow(unit, -1, mod)
        A[k, :] = (A[k, :] * inv) % mod          # pivot is now exactly 3^v
        col = A[k + 1:, k] // P ** v             # exact: v is the minimal valuation
        A[k + 1:, k:] = (A[k + 1:, k:] - col[:, None] * A[k, k:][None, :]) % mod
        A[k, k + 1:] = 0                         # column operations clear the pivot row
        out.append(v)
    return sorted(out)


def torsion_type(exps, prec):
    """Counter {e: multiplicity} for 0 < e < prec; plus unit and zero counts."""
    c = Counter(exps)
    tors = {e: c[e] for e in sorted(c) if 0 < e < prec}
    return {"unit": c.get(0, 0), "tors": tors, "zero": c.get(prec, 0)}


def coker_type(T, J, sign=+1, prec=9):
    """Smith type of M / (T - 1) M^{J = sign}:  matrix (T - 1)(1 + sign*J).
    Returns (free_rank, {e: mult}) of the cokernel M/(T-1)M^{J=sign}."""
    n = T.shape[0]
    I = np.eye(n, dtype=np.int64)
    mod = P ** prec
    Cm = (((T - I) % mod) @ ((I + sign * J) % mod)) % mod
    t = torsion_type(smith_exponents(Cm, prec), prec)
    return t["zero"], t["tors"], t["unit"]


# ----------------------------------------------------------------------------------------------------------
# Functors on matrices
# ----------------------------------------------------------------------------------------------------------

def wedge2(A):
    A = np.asarray(A, dtype=np.int64)
    pairs = np.array(list(itertools.combinations(range(A.shape[0]), 2)), dtype=np.int64).reshape(-1, 2)
    i0, i1 = pairs[:, 0], pairs[:, 1]
    return A[np.ix_(i0, i0)] * A[np.ix_(i1, i1)] - A[np.ix_(i1, i0)] * A[np.ix_(i0, i1)]


def sym2(A):
    """Action on S^2 in the monomial basis e_i e_j (i <= j)."""
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    idx = [(i, j) for i in range(n) for j in range(i, n)]
    out = np.zeros((len(idx), len(idx)), dtype=np.int64)
    for b, (k, l) in enumerate(idx):
        # (A e_k)(A e_l) = sum_{i,j} A[i,k] A[j,l] e_i e_j
        prod = np.outer(A[:, k], A[:, l])
        for a, (i, j) in enumerate(idx):
            out[a, b] = prod[i, j] if i == j else prod[i, j] + prod[j, i]
    return out


def kron(*Ms):
    out = np.array([[1]], dtype=np.int64)
    for M in Ms:
        out = np.kron(out, np.asarray(M, dtype=np.int64))
    return out


def dsum(*Ms):
    n = sum(M.shape[0] for M in Ms)
    out = np.zeros((n, n), dtype=np.int64)
    k = 0
    for M in Ms:
        d = M.shape[0]
        out[k:k + d, k:k + d] = M
        k += d
    return out


def K4(A, mod=None):
    out = wedge2(wedge2(A) if mod is None else wedge2(A) % mod)
    return out if mod is None else out % mod


# ----------------------------------------------------------------------------------------------------------
# Degree-one data
# ----------------------------------------------------------------------------------------------------------

CUSPS = [(1, 0), (2, 2), (0, 1), (2, 0), (1, 1), (0, 2), (2, 1), (1, 2)]   # labels u + v*zeta in O/3, nonzero


def mult_matrix(x, y):
    """Multiplication by x + y*zeta on O in the basis (1, zeta)."""
    return np.array([[x, -y], [y, x - y]], dtype=np.int64)


CONJ_W = np.array([[1, -1], [0, -1]], dtype=np.int64)      # complex conjugation on O in the basis (1, zeta)


def weil_U():
    """Row of the cusp (u, v): the functional (a, b) -> v*a - u*b (the Weil pairing with the cusp label)."""
    return np.array([(v, -u) for (u, v) in CUSPS], dtype=np.int64)


def conj_cusp_perm(shift=(0, 0), neg=False):
    """Permutation matrix of Q -> conj(Q) + shift (or -conj(Q) + shift) on the 9 cusps, restricted to the
    basis d_Q, Q != 0, of C = Z[cusps]/(sum) (d_0 = -sum of the others)."""
    def conj(q):
        u, v = q
        return ((u - v) % 3, (-v) % 3)
    Pm = np.zeros((8, 8), dtype=np.int64)
    for j, q in enumerate(CUSPS):
        u, v = conj(q)
        if neg:
            u, v = (-u) % 3, (-v) % 3
        t = ((u + shift[0]) % 3, (v + shift[1]) % 3)
        if t == (0, 0):
            Pm[:, j] -= 1                       # d_0 = - sum_{Q != 0} d_Q
        else:
            Pm[CUSPS.index(t), j] += 1
    # the cusp 0 itself goes to `shift`; it is not a basis vector, nothing to record
    return Pm


def glue_matrix(E, TC, U):
    """The operator diag(E, TC) on the glued lattice V = {(w, c)}: block lower triangular, extension block
    (U E - TC U)/3 (must be integral)."""
    E = np.asarray(E, dtype=np.int64)
    TC = np.asarray(TC, dtype=np.int64)
    U = np.asarray(U, dtype=np.int64)
    nW, nC = E.shape[0], TC.shape[0]
    A = np.zeros((nW + nC, nW + nC), dtype=np.int64)
    A[:nW, :nW] = E
    A[nW:, nW:] = TC
    num = U @ E - TC @ U
    assert np.all(num % 3 == 0), "operator does not preserve the glued lattice"
    A[nW:, :nW] = num // 3
    return A


def actual_data():
    """The degree-one data of the return: tau = (1 + 3 zeta on W, 7 on C), c = (conjugation, -permutation)."""
    U = weil_U()
    T1 = glue_matrix(mult_matrix(1, 3), 7 * np.eye(8, dtype=np.int64), U)
    J1 = glue_matrix(CONJ_W, -conj_cusp_perm(), U)
    assert np.array_equal(J1 @ J1, np.eye(10, dtype=np.int64))
    return T1, J1


def fmt(tors):
    return " + ".join("C%d^%d" % (3 ** e, k) for e, k in sorted(tors.items())) if tors else "0"
