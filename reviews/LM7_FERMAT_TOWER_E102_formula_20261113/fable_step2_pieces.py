"""Step 2 (Claude Fable 5.2 at effort max): the splitting V = V_1 (+) chi*D_0 over Gamma = <tau, c>, and the
six pieces of K_4 = Lambda^2 Lambda^2 V with their multiplicities.

V_1 = {(w, w') in O x O : w = w' mod 3}, tau = (pi, chi), c = (conj, conj): rank 4.
D_0: tau = 1, c = diag(+1^dplus, -1^dminus); the summand of V is chi (x) D_0.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import sympy as sp
from math import comb
from fable_e102_lib import *

I2 = np.eye(2, dtype=np.int64)


def V1_data(pi=(1, 3), chi=7, glue=None):
    """tau and c on V_1 (glue = identity W/3 -> C_1/3), basis: (1; 0), (zeta; 0), (0; c_1), (0; c_zeta)
    in the glued coordinates of glue_matrix."""
    G = I2 if glue is None else np.asarray(glue, dtype=np.int64)
    T = glue_matrix(mult_matrix(*pi), chi * I2, G)
    J = glue_matrix(CONJ_W, CONJ_W, G)
    return T, J


def explicit_splitting(T1, J1):
    """Change of basis S (columns) with S^-1 T1 S = T_{V_1} (+) chi*1_6 and S^-1 J1 S = J_{V_1} (+) signs."""
    U = weil_U()
    JC = J1[2:, 2:]
    one = np.array([1, 0]); s = np.array([1, 2])           # 1 and s = 1 + 2 zeta = sqrt(-3)
    # J-equivariant integral lift phi of the glue map: phi(1) in C^+, phi(s) in C^-, phi = U mod 3.
    # (work with 2*phi(1) and 2*phi(s) to stay integral; then phi = these times the 3-adic unit 1/2)
    p1 = U @ one + JC @ (U @ one)      # = 2 phi(1)
    ps = U @ s - JC @ (U @ s)          # = 2 phi(s)
    # phi(1) = p1/2, phi(zeta) = (phi(s) - phi(1))/2 = (ps - p1)/4.  Use exact rationals.
    phi = sp.Matrix(8, 2, lambda i, j: [sp.Rational(int(p1[i]), 2), sp.Rational(int(ps[i] - p1[i]), 4)][j])
    Um = sp.Matrix(U.tolist())
    # v(w) = (w ; (U w - phi(w))/3) in code coordinates, c'(w) = (0 ; phi(w))
    top = sp.eye(2).col_join((Um - phi) / 3)
    bot = sp.zeros(2, 2).col_join(phi)
    cols = [top[:, 0], top[:, 1], bot[:, 0], bot[:, 1]]
    # complement C_2: J-eigenvectors in C, chosen so that the whole matrix is invertible mod 3
    JCs = sp.Matrix(JC.tolist())
    plus = [(sp.eye(8) + JCs)[:, j] for j in range(8)]
    minus = [(sp.eye(8) - JCs)[:, j] for j in range(8)]
    chosen, signs = [], []

    def rank3(vs):
        M = sp.Matrix.hstack(*vs).applyfunc(lambda x: sp.Integer(int((x.p * pow(int(x.q), -1, 3)) % 3)))
        return np.linalg.matrix_rank(np.array(M.tolist(), dtype=float))  # small; checked again exactly below

    def rank_mod3(vs):
        M = np.array([[int((x.p * pow(int(x.q), -1, 3)) % 3) for x in v] for v in vs], dtype=np.int64).T
        M = M.copy(); r = 0
        rows, cols_ = M.shape
        for c in range(cols_):
            piv = [i for i in range(r, rows) if M[i, c] % 3]
            if not piv:
                continue
            M[[r, piv[0]]] = M[[piv[0], r]]
            M[r] = (M[r] * pow(int(M[r, c]), -1, 3)) % 3
            for i in range(rows):
                if i != r and M[i, c] % 3:
                    M[i] = (M[i] - M[i, c] * M[r]) % 3
            r += 1
        return r

    base = [bot[2:, 0], bot[2:, 1]]            # phi(1), phi(zeta) inside C
    cur = list(base)
    for vec, sg in [(v, +1) for v in plus] + [(v, -1) for v in minus]:
        if rank_mod3(cur + [vec]) > len(cur):
            cur.append(vec); chosen.append(sp.zeros(2, 1).col_join(vec)); signs.append(sg)
    assert len(cur) == 8
    S = sp.Matrix.hstack(*(cols + chosen))
    assert S.det() != 0 and sp.Integer(S.det().q) % 3 != 0 and sp.Integer(S.det().p) % 3 != 0
    Si = S.inv()
    Tn = Si * sp.Matrix(T1.tolist()) * S
    Jn = Si * sp.Matrix(J1.tolist()) * S
    return S, Tn, Jn, signs


def pieces(pi=(1, 3), chi=7, glue=None, prec=9):
    """The six pieces: name -> (rank, Q+, Q-) where Q+- = torsion type of M/(T-1)M^{J=+-1}."""
    T, J = V1_data(pi, chi, glue)
    mod = 3 ** prec
    L2T, L2J = wedge2(T), wedge2(J)
    S2T, S2J = sym2(T), sym2(J)
    one = np.array([[1]], dtype=np.int64)
    mods = {
        "a: L2L2 V1": (wedge2(L2T), wedge2(L2J)),
        "b: chi^2 L2 V1": (chi ** 2 * L2T, L2J),
        "c: chi^2 S2 V1": (chi ** 2 * S2T, S2J),
        "d: chi^4": (chi ** 4 * one, one),
        "e: chi L2V1 (x) V1": (chi * kron(L2T, T), kron(L2J, J)),
        "f: chi^3 V1": (chi ** 3 * T, J),
    }
    out = {}
    for name, (TM, JM) in mods.items():
        TM = TM % mod
        fp, qp, _ = coker_type(TM, JM, +1, prec)
        fm, qm, _ = coker_type(TM, JM, -1, prec)
        out[name] = (TM.shape[0], qp, qm, fp, fm)
    return out


def multiplicities(dp, dm):
    """(m_plus, m_minus) of each piece for D_0 with c-signs (dp, dm)."""
    a, b = comb(dp, 2) + comb(dm, 2), dp * dm          # Lambda^2 D_0
    return {
        "a: L2L2 V1": (1, 0),
        "b: chi^2 L2 V1": (dp * dp + dm * dm, 2 * dp * dm),
        "c: chi^2 S2 V1": (a, b),
        "d: chi^4": (comb(a, 2) + comb(b, 2), a * b),
        "e: chi L2V1 (x) V1": (dp, dm),
        "f: chi^3 V1": (dp * a + dm * b, dp * b + dm * a),
    }


def predict(pc, dp, dm):
    mult = multiplicities(dp, dm)
    tot = Counter(); free = 0
    for name, (rk, qp, qm, fp, fm) in pc.items():
        mp, mm = mult[name]
        for e, k in qp.items():
            tot[e] += k * mp
        for e, k in qm.items():
            tot[e] += k * mm
        free += fp * mp + fm * mm
    return free, dict(sorted(tot.items()))


if __name__ == "__main__":
    T1, J1 = actual_data()
    S, Tn, Jn, signs = explicit_splitting(T1, J1)
    print("S^-1 T S =")
    sp.pprint(Tn)
    print("S^-1 J S =")
    sp.pprint(Jn)
    print("signs of c on the complement D_0:", signs)
    TV1, JV1 = V1_data()
    assert Tn[:4, :4] == sp.Matrix(TV1.tolist()) and Jn[:4, :4] == sp.Matrix(JV1.tolist())
    assert Tn[4:, 4:] == 7 * sp.eye(6) and Tn[:4, 4:] == sp.zeros(4, 6) and Tn[4:, :4] == sp.zeros(6, 4)
    assert Jn[4:, 4:] == sp.diag(*signs) and Jn[:4, 4:] == sp.zeros(4, 6) and Jn[4:, :4] == sp.zeros(6, 4)
    print("VERIFIED exactly: V = V_1 (+) 7*D_0 as a module over <tau, c>; det S =", S.det())
    dp, dm = signs.count(1), signs.count(-1)
    pc = pieces()
    mult = multiplicities(dp, dm)
    print("\npiece | rank | mult (+,-) | Q+ | Q- | free+ free-")
    for name, (rk, qp, qm, fp, fm) in pc.items():
        print(name, "|", rk, "|", mult[name], "|", fmt(qp), "|", fmt(qm), "|", fp, fm)
    free, tot = predict(pc, dp, dm)
    print("\nFORMULA TOTAL: free", free, "| torsion", fmt(tot), "| unit pivots", 990 - free - sum(tot.values()))
