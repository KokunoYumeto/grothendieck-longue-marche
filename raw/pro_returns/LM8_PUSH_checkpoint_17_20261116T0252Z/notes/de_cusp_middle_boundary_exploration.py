#!/usr/bin/env python3
"""Unregistered middle-range boundary calculation; no arithmetic theorem claimed."""
from pathlib import Path
import hashlib
import importlib.util
import json
import time

import sympy as sp

base = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("boundary_support", base / "pbc_D88_boundary_certificate.py")
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)


def run():
    rows = []
    for r, m, n in [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]:
        permutation = support.actual_relative_action(r, n, multiplier=2)
        translation = support.actual_relative_action(r, n, shift=1)
        deep_translation = support.actual_relative_action(r, n, shift=5**m)
        identity = sp.eye(permutation.rows)
        u_action = (identity + translation) * permutation
        half = pow(2, -1, 5**n)
        gauge = support.actual_relative_action(r, n, shift=-half)
        diagonal_action = gauge * u_action
        assert permutation * (translation - identity) == (translation - identity) * u_action
        assert gauge * diagonal_action == u_action * gauge
        reports = []
        for action in [permutation, u_action, diagonal_action]:
            relation = (action - identity).row_join(deep_translation - identity)
            reports.append(support.smith_report(relation))
        assert reports[0] == reports[1] == reports[2]
        rows.append({"r": r, "m": m, "N": n, "dimension": identity.rows,
                     "actual_relative_boundary_coinvariants": reports[0],
                     "all_three_actual_boundary_models_agree": True})
    return {"status": "COMPUTED", "scope": "Unregistered literal integral boundary quotient in r<m<N; no global or splitting claim.",
            "rows": rows}


if __name__ == "__main__":
    start = time.monotonic()
    result = run()
    result["elapsed_seconds"] = time.monotonic() - start
    result["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
