"""Step 1 (Claude Fable 5.2 at effort max): direct recomputation of E.102 with own code, and first structural
checks on the degree-one data."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from fable_e102_lib import *

T1, J1 = actual_data()
print("T1 =\n", T1)
print("J1 =\n", J1)

# compare with the return's definition written out literally (transcribed from arithmetic_inputs, not run)
cusps = [(1, 0), (2, 2), (0, 1), (2, 0), (1, 1), (0, 2), (2, 1), (1, 2)]
CT = np.zeros((8, 8), dtype=np.int64)
for j, i in enumerate([0, 2, 1, 3, 5, 4, 7, 6]):
    CT[i][j] = -1
assert np.array_equal(-conj_cusp_perm(), CT), "conjugation permutation differs from the return's CT"
print("conjugation on cusps = -[Q -> conj(Q)] in the labels u + v zeta: agrees with the return's CT")

# T' = J T J commutes with T ?
T1p = J1 @ T1 @ J1
print("T J T J == J T J T:", np.array_equal(T1 @ T1p, T1p @ T1))
print("T mod 3 - 1 has rank", np.linalg.matrix_rank((T1 - np.eye(10, dtype=np.int64)) % 3))

if len(sys.argv) > 1 and sys.argv[1] == "full":
    prec = 9
    mod = 3 ** prec
    T4 = K4(T1, mod)
    J4 = K4(J1, mod)
    free, tors, unit = coker_type(T4, J4, +1, prec)
    print("E.102 direct: rank", T4.shape[0], "| free", free, "| unit", unit, "| torsion", fmt(tors),
          "| log3 order", sum(e * k for e, k in tors.items()))
