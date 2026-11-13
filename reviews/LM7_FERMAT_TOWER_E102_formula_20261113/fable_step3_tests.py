"""Step 3 (Claude Fable 5.2 at effort max): tests of the piece formula against direct Smith forms on the full
rank-990 module, for changed data: the extension class (glue), the cyclotomic value chi, the CM value pi, and
the conjugation.

FORMULA (structure part).  V = V_core (+) chi*D_0 over <tau, c>, where V_core is W glued to a lattice C_1 of
rank g = rank of the glue map mod 3 (g = 0, 1, 2), and D_0 has c-signs (dp, dm).  Then
  torsion(C_4) = sum over the six pieces P of  Q+(P)^{m+(P)} (+) Q-(P)^{m-(P)},   free rank = rank K^{J=-1},
with Q+-(P) = torsion of P/(T-1)P^{J=+-1} (matrices of rank <= 24) and the multiplicities of
fable_step2_pieces.multiplicities(dp, dm).
"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from fable_e102_lib import *
from fable_step2_pieces import multiplicities

PREC_DIRECT, PREC_PIECE = 10, 12
I8 = np.eye(8, dtype=np.int64)


def core_data(pi, chi, gtype):
    """V_core for glue type: 'split' (W), '1+' / '1-' (rank-1 glue; C_1 has c-sign +/-), '2' (rank-2 glue)."""
    E = mult_matrix(*pi)
    if gtype == "split":
        return E, CONJ_W.copy()
    if gtype == "2":
        G = np.eye(2, dtype=np.int64)
        return glue_matrix(E, chi * G, G), glue_matrix(CONJ_W, CONJ_W, G)
    # rank one: functional l on W = O with basis (1, zeta); s = 1 + 2 zeta.
    # '1+': l(1) = 1, l(s) = 0  -> l = (1, 1) on (1, zeta);  c-sign of C_1 is +
    # '1-': l(1) = 0, l(s) = 1  -> l = (0, 2) on (1, zeta) (l(s) = 4 = 1 mod 3); c-sign of C_1 is -
    l = np.array([[1, 1]]) if gtype == "1+" else np.array([[0, 2]])
    sg = 1 if gtype == "1+" else -1
    return (glue_matrix(E, np.array([[chi]]), l), glue_matrix(CONJ_W, np.array([[sg]]), l))


def piece_table(Tc, Jc, chi, prec=PREC_PIECE):
    mod = 3 ** prec
    L2T, L2J = wedge2(Tc), wedge2(Jc)
    S2T, S2J = sym2(Tc), sym2(Jc)
    one = np.array([[1]], dtype=np.int64)
    mods = {
        "a: L2L2 V1": (wedge2(L2T), wedge2(L2J)),
        "b: chi^2 L2 V1": (chi ** 2 * L2T, L2J),
        "c: chi^2 S2 V1": (chi ** 2 * S2T, S2J),
        "d: chi^4": (chi ** 4 * one, one),
        "e: chi L2V1 (x) V1": (chi * kron(L2T, Tc), kron(L2J, Jc)),
        "f: chi^3 V1": (chi ** 3 * Tc, Jc),
    }
    out = {}
    for name, (TM, JM) in mods.items():
        if TM.shape[0] == 0:
            out[name] = (0, {}, {}, 0, 0)
            continue
        TM = TM % mod
        fp, qp, _ = coker_type(TM, JM, +1, prec)
        fm, qm, _ = coker_type(TM, JM, -1, prec)
        out[name] = (TM.shape[0], qp, qm, fp, fm)
    return out


def formula(pi, chi, gtype, dp, dm):
    Tc, Jc = core_data(pi, chi, gtype)
    pc = piece_table(Tc, Jc, chi)
    mult = multiplicities(dp, dm)
    tot = Counter(); free = 0
    for name, (rk, qp, qm, fp, fm) in pc.items():
        mp, mm = mult[name]
        for e, k in qp.items():
            tot[e] += k * mp
        for e, k in qm.items():
            tot[e] += k * mm
        free += fp * mp + fm * mm
    return free, {e: k for e, k in sorted(tot.items()) if k}, pc


def direct(T1, J1):
    n = T1.shape[0]
    assert np.array_equal(J1 @ J1, np.eye(n, dtype=np.int64))
    mod = 3 ** PREC_DIRECT
    T4, J4 = K4(T1, mod), K4(J1, mod)
    free, tors, unit = coker_type(T4, J4, +1, PREC_DIRECT)
    return free, tors, unit


def cusp_model(pi, chi, G=None, shift=(0, 0), neg=False, PC=None):
    """Degree-one data in the cusp basis: glue map U*G (optionally PC*U*G), conjugation on the cusp loops
    = -perm(Q -> conj(Q) + shift)   or   +perm(Q -> -conj(Q) + shift) if neg."""
    U = weil_U()
    if G is not None:
        U = U @ np.asarray(G, dtype=np.int64)
    if PC is not None:
        U = np.asarray(PC, dtype=np.int64) @ U
    perm = conj_cusp_perm(shift, neg)
    JC = perm if neg else -perm
    T1 = glue_matrix(mult_matrix(*pi), chi * I8, U)
    J1 = glue_matrix(CONJ_W, JC, U)
    rk = rank_mod3(U)
    tr = int(np.trace(JC))
    return T1, J1, rk, ((8 + tr) // 2, (8 - tr) // 2)


def rank_mod3(M):
    M = np.array(M, dtype=np.int64) % 3
    r = 0
    rows, cols = M.shape
    for c in range(cols):
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


def direct_sum_model(pi, chi, gtype, dp, dm, seed):
    """V_core (+) chi*D_0 with prescribed signs, conjugated by a random integer matrix of determinant +-1."""
    Tc, Jc = core_data(pi, chi, gtype)
    n0 = Tc.shape[0]
    n = n0 + dp + dm
    T1 = dsum(Tc, chi * np.eye(dp + dm, dtype=np.int64))
    J1 = dsum(Jc, np.diag([1] * dp + [-1] * dm).astype(np.int64)) if dp + dm else Jc
    rng = np.random.default_rng(seed)
    S = np.eye(n, dtype=np.int64); Si = np.eye(n, dtype=np.int64)
    for _ in range(40):
        i, j = rng.choice(n, 2, replace=False)
        a = int(rng.integers(-2, 3))
        El = np.eye(n, dtype=np.int64); El[i, j] = a
        Eli = np.eye(n, dtype=np.int64); Eli[i, j] = -a
        S = S @ El; Si = Eli @ Si
    assert np.array_equal(S @ Si, np.eye(n, dtype=np.int64))
    return S @ T1 @ Si, S @ J1 @ Si


CASES = []
# (label, builder for direct data, formula inputs (pi, chi, gtype, dp, dm))
s_proj_plus = np.array([[1, 1], [0, 0]])    # w -> l_+(w) * 1 : kills s = 1 + 2 zeta, keeps 1   (commutes with conj mod 3)
s_proj_minus = np.array([[0, 1], [0, 2]])   # w -> l_-(w) * s : kills 1, s -> 2*(2... ) see check in main
CASES.append(("T0 actual: pi=1+3z, chi=7, Weil glue", lambda: cusp_model((1, 3), 7), ((1, 3), 7, "2", 2, 4)))
# --- extension class
CASES.append(("T1a split (glue 0)", lambda: cusp_model((1, 3), 7, G=np.zeros((2, 2), dtype=np.int64)), ((1, 3), 7, "split", 3, 5)))
CASES.append(("T1b rank-1 glue, kernel = s-line", lambda: cusp_model((1, 3), 7, G=s_proj_plus), ((1, 3), 7, "1+", 2, 5)))
CASES.append(("T1c rank-1 glue, kernel = 1-line", lambda: cusp_model((1, 3), 7, G=s_proj_minus), ((1, 3), 7, "1-", 3, 4)))
CASES.append(("T1d rank-2 glue U*conj (not the Weil pairing)", lambda: cusp_model((1, 3), 7, G=CONJ_W), ((1, 3), 7, "2", 2, 4)))
CASES.append(("T1e rank-2 glue 2*U", lambda: cusp_model((1, 3), 7, G=2 * np.eye(2, dtype=np.int64)), ((1, 3), 7, "2", 2, 4)))
# --- cyclotomic value
for chi in (4, 10, 16, 19, 28):
    CASES.append(("T2 chi=%d, pi=1+3z" % chi, (lambda chi=chi: cusp_model((1, 3), chi)), ((1, 3), chi, "2", 2, 4)))
# --- CM value (chi = N(pi)) and mixed
for pi, chi in (((1, -3), 13), ((4, 3), 13), ((-2, 3), 19), ((1, 6), 31), ((4, -3), 37), ((1, 9), 73), ((4, 0), 16), ((1, -3), 7), ((4, 9), 7)):
    CASES.append(("T3 pi=%d%+dz, chi=%d" % (pi[0], pi[1], chi), (lambda pi=pi, chi=chi: cusp_model(pi, chi)), (pi, chi, "2", 2, 4)))
# --- conjugation
CASES.append(("T4a conj shifted by s on the cusps", lambda: cusp_model((1, 3), 7, shift=(1, 2)), ((1, 3), 7, "2", 2, 4)))
CASES.append(("T4b cusp loops with +perm(Q -> -conj Q): signs (5,3)", lambda: cusp_model((1, 3), 7, neg=True), ((1, 3), 7, "2", 4, 2)))
CASES.append(("T4c +perm(Q -> -conj Q + 1)", lambda: cusp_model((1, 3), 7, neg=True, shift=(1, 0)), ((1, 3), 7, "2", 4, 2)))
for (dp, dm, seed) in ((0, 6, 1), (6, 0, 2), (3, 3, 3), (1, 5, 4)):
    CASES.append(("T4d direct-sum model, D_0 signs (%d,%d), random basis" % (dp, dm),
                  (lambda dp=dp, dm=dm, seed=seed: direct_sum_model((1, 3), 7, "2", dp, dm, seed) + (None, None)),
                  ((1, 3), 7, "2", dp, dm)))
CASES.append(("T4e direct-sum model, rank-1 core '1-', signs (5,2), chi=10", lambda: direct_sum_model((1, 3), 10, "1-", 5, 2, 5) + (None, None), ((1, 3), 10, "1-", 5, 2)))


if __name__ == "__main__":
    sel = sys.argv[1:] or None
    ok_all = True
    for label, build, finp in CASES:
        if sel and not any(label.startswith(s) for s in sel):
            continue
        t0 = time.time()
        T1, J1, rk, signsC = build()
        pi, chi, gtype, dp, dm = finp
        if rk is not None:   # consistency of the declared structure with the data
            g = {"split": 0, "1+": 1, "1-": 1, "2": 2}[gtype]
            assert rk == g, (label, rk, g)
            c1 = {"split": (0, 0), "1+": (1, 0), "1-": (0, 1), "2": (1, 1)}[gtype]
            assert (dp + c1[0], dm + c1[1]) == signsC, (label, signsC, dp, dm)
        free_d, tors_d, unit_d = direct(T1, J1)
        free_f, tors_f, pc = formula(pi, chi, gtype, dp, dm)
        ok = (free_d == free_f and tors_d == tors_f)
        ok_all &= ok
        print("%-58s | direct: Z^%d + %s (unit %d) | formula: Z^%d + %s | %s | %.0fs" % (
            label, free_d, fmt(tors_d), unit_d, free_f, fmt(tors_f), "AGREE" if ok else "DIFFER", time.time() - t0))
        sys.stdout.flush()
    print("ALL AGREE" if ok_all else "SOME DIFFER")
