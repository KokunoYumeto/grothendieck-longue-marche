# Mechanical documentation audit: scans 170–178

## Scan 170: classify the first-limit row as an uncertainty-only difference

- **Exact place:** `result/records/scan170/decision.json`, `differences[12].kind` (zero-based array index), place `line 18, first limit sign`. The same classification is exported in `result/SP51_CW_134-2_collation.tsv` at that place. `result/scripts/decide_170.py` also explicitly assigns `misread symbol or index` in its `first limit sign` branch.
- **Recorded evidence:** The decision quotes H as `\varprojlim` and retains `\unsure{\varprojlim|\underline{\lim}}`. Thus H and the consolidated record have the same preferred reading; the recorded difference is the retained alternative. Reader A `differences[12]` calls this `retained C doubt` and says, “A plain rule remains possible. C doubt retained.” Reader B `differences[11]` (`B170-D12`) calls it `mathematical sign and retained uncertainty`; reader C `differences[12]` (`D13`) calls it `mathematical sign/retained doubt`. All three return the same two alternatives in the same order.
- **Why this requires a record correction:** The recorded collation convention in `result/briefs/brief_v09_scan178.md` says to use `other` for uncertainty-only changes. The current `misread symbol or index` label implies a changed preferred symbol even though the stored H and final fields do not show one.
- **Suggested correction:** Change this row's `kind` to `other`, make the matching change in the decision-building script, and regenerate the derived collation. Preserve the final reading, doubt, H-difference flag, evidence, and counts. This correction requires no new image inspection or reading adjudication.

No additional actionable report-coverage, three-reader disagreement, or source-assertion/check-event reference issue was found in this bounded record audit. Only completed reader text/report records, decisions, aggregate documentation, existing audit results, and relevant scripts were inspected; no images, original witnesses, web pages, or TeX engine were opened.

## Root disposition

The sole classification issue was corrected in scan170 decision.differences[12] and in decide_170.py, then the collation was regenerated. No transcription text changed. The audit inspected only completed written records, not manuscript images, and was not an additional scan reading.
