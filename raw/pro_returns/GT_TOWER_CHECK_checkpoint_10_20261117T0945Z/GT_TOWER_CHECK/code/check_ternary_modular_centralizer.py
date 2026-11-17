#!/usr/bin/env python3
"""Exact centralizer residues in the retained modular vertex-module source.

This checks the modular E0 source itself.  It does not assert that a
five-point target retains its complete module; that comparison is a
separate actual map calculation.
"""
from pathlib import Path
import sys
import json
import numpy as np

HERE = Path(__file__).resolve().parent
TOWER = HERE.parent / "tower_code"
sys.path.insert(0, str(TOWER))
source = (TOWER / "test_fivepoint_cm_level.py").read_text()
prefix = source.split("records=[];base_records=[]", 1)[0]
namespace = {"__name__": "centralizer_modular_prefix",
             "__file__": str(HERE / "ternary_modular_prefix.py")}
exec(compile(prefix, str(TOWER / "test_fivepoint_cm_level.py"), "exec"), namespace)

b_eval = namespace["b_eval"]
subst = namespace["subst"]
bx, by = namespace["bx"], namespace["by"]
btable = namespace["btable"]
br = namespace["br"]
bfpaths = namespace["bfpaths"]
push = namespace["push"]
K = namespace["bkernel"][3]
rank_projection = namespace["row_space_projection"]
dim = len(namespace["bcases"][3][1])
er = np.zeros(dim, dtype=np.int16)
er[0] = 1
correction = (K - push(K, br, 3)) % 3
rows, projection = rank_projection(correction, 3)
assert len(K) == 96
records = []
passing = []
for residue, word in sorted(bfpaths.items()):
    if btable[residue, br] != btable[br, residue]:
        continue
    q, ta = b_eval(subst(word, (bx, by)), 3)
    assert q == residue
    defect = (ta + push(er, residue, 3) - er - push(ta, br, 3)) % 3
    residual = defect @ projection % 3
    good = not np.any(residual)
    if good:
        passing.append(residue)
        certificate = None
    else:
        col = int(np.flatnonzero(residual)[0])
        functional = projection[:, col]
        assert not np.any(correction @ functional % 3)
        assert int(defect @ functional % 3) != 0
        certificate = {"functional": functional.tolist(),
                       "defect_value": int(defect @ functional % 3)}
    records.append({"base_residue": residue,
                    "projective_matrix_mod12": list(namespace["BQ"][residue]),
                    "pure_lift_word": list(word),
                    "centralizer_lift_exists": good,
                    "nonzero_obstruction_coordinates": int(np.count_nonzero(residual)),
                    "certificate": certificate})
assert len(records) == 6
assert passing == [0]
scalar = namespace["bi"][namespace["canon"]((5, 0, 0, 5))]
assert scalar == 573
assert next(r for r in records if r["base_residue"] == scalar)["centralizer_lift_exists"] is False
result = {"status": "PASS",
          "scope": "Actual modular E0 pure r-centralizer residues; no five-point factorization is inferred.",
          "projective_modular_base_order": 576,
          "pure_base_order": len(bfpaths),
          "permutation_module_dimension": dim,
          "actual_pure_kernel_dimension": len(K),
          "r_correction_rank": len(rows),
          "pure_base_centralizer_count": len(records),
          "lifted_pure_base_residues": passing,
          "records": records}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print("PASS exact modular source: pure kernel dimension96 inside the ternary vertex permutation module of dimension192")
print("PASS r-centralizer correction rank", len(rows))
print("PASS all six pure base r-centralizer residues tested; only identity lifts")
print("PASS scalar5I residue573 excluded, with an explicit dual linear functional")
print("No assertion that the five-point homology target retains this entire modular source is made.")
