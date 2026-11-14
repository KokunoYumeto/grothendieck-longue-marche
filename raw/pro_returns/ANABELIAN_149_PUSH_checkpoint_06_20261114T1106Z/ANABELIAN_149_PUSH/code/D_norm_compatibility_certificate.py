#!/usr/bin/env python3
"""Finite checks for D.24; the valuation argument is proved in the text."""
import json
from pathlib import Path

rows = [{"a": a, "b": b, "norm_mod_3": (a*a+b*b) % 3}
        for a in range(3) for b in range(3)]
zeros = [[r["a"], r["b"]] for r in rows if r["norm_mod_3"] == 0]
trace = [{"vector": [a, b], "trace_mod_2": (a+b) % 2}
         for a in range(2) for b in range(2)]
assert zeros == [[0, 0]]
assert {r["trace_mod_2"] for r in trace} == {0, 1}
assert all((r["vector"][1]+r["vector"][0]) % 2 == r["trace_mod_2"]
           for r in trace)
result = {
    "claim": "D.24",
    "field_extension": "Q(i)/Q",
    "kummer_modulus": 2,
    "norm_polynomial": "a^2+b^2",
    "residue_prime": 3,
    "complete_norm_residue_table": rows,
    "norm_zero_pairs": zeros,
    "trace_on_two_cosets_mod_2": trace,
    "trace_is_surjective_and_swap_invariant": True,
    "mathematical_consequence":
        "v_3(N(a+bi)) is even for all nonzero a+bi in Q(i); "
        "the Kummer squareclass of 3 is not a norm, although the "
        "permutation-module trace is surjective.",
    "scope": "This certifies the elementary residue calculation, "
             "not a nonexistence theorem for compatible sections."
}
out = Path(__file__).resolve().parent.parent / "audit" / "D_norm_compatibility_certificate.json"
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"output": str(out), "zero_pairs": zeros,
                  "trace_surjective": True}, indent=2))
