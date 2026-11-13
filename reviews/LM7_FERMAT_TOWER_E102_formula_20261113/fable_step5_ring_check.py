"""Step 5 (Claude Fable 5.2 at effort max): check of the ring description of the pieces.

V_1 = B := {(w, w') in O x O : w = w' mod 3} is free of rank one over the Gorenstein ring B, and tau, tau' = c tau c
act by multiplication by (pi, chi), (conj(pi), chi).  For a piece P cut out of chi^k V_1^{(x)m} by a 2-group of
permutations, Gorenstein duality gives
    Q^{+-}(P) = H^0(<tau,c>, P (x) sgn^{+-} (x) Q/Z)  ~  ( P / (tau-1)P )^{c = +-(-1)^m}      (coinvariants),
i.e. the pieces are isotypic parts of the finite ring A_m = B^{(x)m} / (chi^k tau^{(x)m} - 1, chi^k tau'^{(x)m} - 1).
Checked here: the cokernel of [T-1 | eps*J-1] : P (+) P -> P  (coinvariants of <T, eps*J>)  equals  Q^{eps*(-1)^m}(P).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from fable_e102_lib import *
from fable_step3_tests import core_data

prec = 12
mod = 3 ** prec
chi = 7
Tc, Jc = core_data((1, 3), chi, "2")
L2T, L2J, S2T, S2J = wedge2(Tc), wedge2(Jc), sym2(Tc), sym2(Jc)
one = np.array([[1]], dtype=np.int64)
mods = {
    "a: L2L2 V1": (wedge2(L2T), wedge2(L2J), 4),
    "b: chi^2 L2 V1": (chi ** 2 * L2T, L2J, 2),
    "c: chi^2 S2 V1": (chi ** 2 * S2T, S2J, 2),
    "d: chi^4": (chi ** 4 * one, one, 0),
    "e: chi L2V1 (x) V1": (chi * kron(L2T, Tc), kron(L2J, Jc), 3),
    "f: chi^3 V1": (chi ** 3 * Tc, Jc, 1),
}
ok = True
for name, (TM, JM, m) in mods.items():
    n = TM.shape[0]
    I = np.eye(n, dtype=np.int64)
    res = {}
    for eps in (1, -1):
        st = np.hstack([(TM - I) % mod, (eps * JM - I) % mod])        # M (+) M -> M, (x, y) -> (T-1)x + (eps*J-1)y
        co = torsion_type(smith_exponents(st, prec), prec)["tors"]       # coinvariants of <T, eps*J>
        sign = eps * (-1) ** m
        q = coker_type(TM % mod, JM, sign, prec)[1]
        res[eps] = (fmt(co), fmt(q), co == q)
        ok &= (co == q)
    print("%-20s m=%d | coinv(c=+) = %-22s = Q^%s: %s | coinv(c=-) = %-22s = Q^%s: %s" % (
        name, m, res[1][0], "+" if (-1) ** m == 1 else "-", res[1][2], res[-1][0], "-" if (-1) ** m == 1 else "+", res[-1][2]))
print("RING DESCRIPTION CONSISTENT" if ok else "MISMATCH")
