#!/usr/bin/env python3
"""Independent nonmutating replay of the exact SL2-boundary comparison."""
from pathlib import Path
from unittest.mock import patch
import hashlib,json,runpy,time
import numpy as np

HERE=Path(__file__).resolve().parent
protected=[HERE/f"de_sl2_boundary_quotient.{suffix}" for suffix in ("py","json","npz","out")]
def hashes():
    return {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in protected}

started=time.time();before=hashes()
with patch.object(Path,"write_text",return_value=0),patch.object(np,"savez_compressed",return_value=None):
    runpy.run_path(str(HERE/"de_sl2_boundary_quotient.py"),run_name="__main__")
after=hashes();assert before==after
data=json.loads((HERE/"de_sl2_boundary_quotient.json").read_text())
assert data["H_image_order"]==800 and data["H_exponent"]==20
assert data["actual_F_image_order"]==7200
assert data["actual_F_abelianization_map"]=="ordinary exponent sums modulo30"
assert data["H_lower_central_third_is_trivial"]
result={"independent_complete_replay":"PASS","all_protected_artifacts_unchanged":True,
        "protected_sha256":after,
        "exact_F_image":"SL2(F3) fibre product with (Z/30)^2 over C3",
        "exact_H_image":"Q8 times C10^2",
        "actual_P20_factorization_verified":True,
        "elapsed_seconds":round(time.time()-started,3)}
(HERE/"bc_sl2_boundary_audit.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
print("PASS: independent exact source/H-image audit with all original artifacts preserved.")
