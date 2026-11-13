"""Step 6 (Claude Fable 5.2 at effort max): the six-piece table over a grid of CM values pi = 1 + 3(x + y zeta)
with chi = N(pi); the tables are grouped and compared with the congruence class of a = (pi - 1)/3 = a0 + a1*s
(a0 = x + y mod 3, a1 = -y mod 3).  Shows for which pi the table of the actual data is valid."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from collections import defaultdict
from fable_e102_lib import *
from fable_step3_tests import core_data, piece_table

classes = defaultdict(list)
for x in range(-4, 5):
    for y in range(-4, 5):
        if (x, y) == (0, 0):
            continue
        pi = (1 + 3 * x, 3 * y)
        chi = pi[0] ** 2 - pi[0] * pi[1] + pi[1] ** 2
        Tc, Jc = core_data(pi, chi, "2")
        pc = piece_table(Tc, Jc, chi, prec=13)
        key = " ; ".join("%s: %s | %s" % (name[0], fmt(qp), fmt(qm)) for name, (rk, qp, qm, fp, fm) in pc.items())
        classes[key].append(((x + y) % 3, (-y) % 3, x, y))
for key, lst in sorted(classes.items(), key=lambda kv: -len(kv[1])):
    cong = sorted(set((a0, a1) for a0, a1, x, y in lst))
    print(len(lst), "values of pi; (a0, a1) mod 3 in", cong)
    if len(lst) >= 8:
        print("   ", key)
