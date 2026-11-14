#!/usr/bin/env python3
"""Seal the full peer F33 review against the final acyclic author evidence."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PART = ROOT / "work/part_c"
AUTHOR = ROOT / "work/part_a"
STEM = "f_quadratic_sign_pair_restriction"
EXPECTED = {
    ".tex": "8a2cd87d9139c6e2bccd99cc9bb8db53883d064da5653fd804e2e2457ab96037",
    "_results.json": "46d8c1f968e0133ad46d23fb3c20960b444081b29364c267715a20b0db49d2f2",
    "_report.txt": "5b1493d029d5700957aa13cb2776d46cb11168bc2ff11f7d58ae4f1228a04e7e",
    "_preservation.json": "82da89dcaeea70dc9232f218124bd6020e38e240860565d761e1fdbfc18392aa",
    "_evidence_manifest.json": "6e08ac16e40d12ac995500f3c0527f56c03d9277a954e1d666f719bd67208104"
}


def bind(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)),
            "sha256": hashlib.sha256(data).hexdigest(),
            "bytes": len(data), "lines": len(data.splitlines())}


def verify(entry):
    path = Path(entry["path"])
    if not path.is_absolute():
        path = ROOT / path
    actual = bind(path)
    for key in ("sha256", "bytes", "lines"):
        if key in entry:
            assert actual[key] == entry[key], (path, key)
    return actual


author_bindings = {}
for suffix, expected in EXPECTED.items():
    actual = bind(AUTHOR / (STEM + suffix))
    assert actual["sha256"] == expected
    author_bindings[suffix] = actual
manifest = json.loads((AUTHOR / (STEM + "_evidence_manifest.json")).read_text())
preservation = json.loads((AUTHOR / (STEM + "_preservation.json")).read_text())
entries = [verify(entry) for entry in manifest["entries"]]
assert len(entries) == manifest["entry_count"] == 69
assert len({entry["path"] for entry in entries}) == 69
prior = []
prior_paths = set()
prior_recorded_paths = set()
path_spellings = {}
total = 0
for item in preservation["manifests"]:
    path = ROOT / item["manifest"]
    assert bind(path)["sha256"] == item["manifest_sha256"]
    old = json.loads(path.read_text())
    checked = [verify(entry) for entry in old["entries"]]
    assert len(checked) == item["entries"]
    total += len(checked)
    prior_paths.update(entry["path"] for entry in checked)
    for recorded, actual in zip(old["entries"], checked):
        prior_recorded_paths.add(recorded["path"])
        path_spellings.setdefault(actual["path"], set()).add(recorded["path"])
    prior.append({"manifest": bind(path), "entries_verified": len(checked),
                  "entries": checked})
assert total == preservation["entry_count"] == 400
assert len(prior_recorded_paths) == preservation["unique_bound_files"] == 294
assert len(prior_paths) == 291
aliases = [{"workspace_file": bind(ROOT / path),
            "recorded_paths": sorted(spellings),
            "path_map": "An absolute path is restricted to this exact ROOT prefix; a relative path is joined to ROOT. Both resolve to the displayed identical file."}
           for path, spellings in sorted(path_spellings.items()) if len(spellings) > 1]
assert len(aliases) == 3 and all(len(item["recorded_paths"]) == 2 for item in aliases)

replay_path = PART / "f33_peer_replay/comparison.json"
printed_path = PART / "f33_peer_replay/printed_formula_crosscheck.json"
replay = json.loads(replay_path.read_text())
printed = json.loads(printed_path.read_text())
assert bind(replay_path)["sha256"] == "e2e65a7a34a26f7ffd9c164f71990a8f5d8ada806d2233794c5a2083b23d9890"
assert bind(printed_path)["sha256"] == "48c5138b9ff66b4ca062f0cb21ad412ee1107505abbfb58bf364c7406964a12b"
assert replay["checks"] == 252309 and replay["raw_output_whole_bytes_identical"]
assert replay["raw_stdout_whole_bytes_identical"] and replay["exit_code"] == 0
assert printed["status"] == "PASS" and printed["checks"] == 27737
body_path = PART / "review_f33_body.txt"
assert bind(body_path)["sha256"] == "b290041255cfdb7321c4a07407b5dbac05b6acce8adc7877b0cc86eb7bf6c84e"

audit = {"status": "PASS_FINAL_F33_AND_PRIOR_F23_F32_BINDINGS", "date": "2026-11-14",
         "sealer": bind(Path(__file__)), "final_author_files": author_bindings,
         "manifest_entries_checked": entries, "manifest_entry_count": 69,
         "prior_manifests_checked": prior, "prior_entry_routes": 400,
         "prior_distinct_recorded_path_strings": 294,
         "prior_distinct_workspace_files": 291,
         "exact_absolute_relative_path_transports": aliases,
         "preservation_count_precision": "The frozen author's unique_bound_files=294 counts distinct recorded path strings; the three explicit paired spellings give291 workspace files. All400 routes and all hashes pass.",
         "all_bound_frozen_bytes_unchanged": True,
         "review_remains_outside_author_manifest": True}
audit_path = PART / "review_f33_binding_audit.json"
assert not audit_path.exists()
audit_path.write_text(json.dumps(audit, indent=2) + "\n")
header = """FINAL INDEPENDENT F.33 REVIEW: PASS
===================================
No mathematical, source or program correction requested.

Final author source SHA256:
  8a2cd87d9139c6e2bccd99cc9bb8db53883d064da5653fd804e2e2457ab96037
Final author results SHA256:
  46d8c1f968e0133ad46d23fb3c20960b444081b29364c267715a20b0db49d2f2
Final author report SHA256:
  5b1493d029d5700957aa13cb2776d46cb11168bc2ff11f7d58ae4f1228a04e7e
Final preservation SHA256:
  82da89dcaeea70dc9232f218124bd6020e38e240860565d761e1fdbfc18392aa
Final author manifest SHA256:
  6e08ac16e40d12ac995500f3c0527f56c03d9277a954e1d666f719bd67208104

I read the complete final author results, report, preservation record
and all manifest entries after receiving the author freeze. All 69
final manifest entries were independently checked against current
complete file bytes. The ten prior F.23--F.32 manifests and all 400
of their entry routes were also independently rechecked. The frozen
preservation count 294 counts distinct recorded path strings. Those
map to 291 workspace files through exactly three absolute/relative
path pairs: the F.23 marginal_braids.json, its mathematical source
f_source_sign_and_marginal_images.tex, and that source's results JSON.
For every pair, joining the relative path to the recorded workspace
root gives exactly the absolute path, with identical bytes and SHA.
All three forward path maps and their common file bindings are in
the binding audit; no frozen author count or manifest was changed.
The final theorem scope, operation counts, coordinate dictionary
and retained older producer descriptions agree with the proof and
the separately verified actual-divisor domain. The root
review and root isolated replay record were read after my independent
proof, program and formula review had passed.

The complete verification routes are retained separately in
work/part_c/review_f33_binding_audit.json. This final review binds the
frozen author manifest and remains outside it, preserving the acyclic
evidence chain. The following body supplies the mathematical review.

"""
report_path = PART / "review_f33.txt"
assert not report_path.exists()
report_path.write_text(header + body_path.read_text())
record = {
    "status": "PASS", "claim": "F.33", "reserved_global_claim_number": 272,
    "date": "2026-11-14", "reviewer": "/root/c89_review_and_general_c",
    "report": bind(report_path), "mathematical_body": bind(body_path),
    "sealer": bind(Path(__file__)), "author": author_bindings,
    "binding_audit": bind(audit_path),
    "read_scope": {
        "proof_lines": 404, "new_producer_lines": 196, "literal_checker_lines": 330,
        "all_three_helper_source_programs_read": True,
        "complete_final_author_results_report_manifest_preservation_read": True,
        "F23_original_source_membership_and_based_sign_maps_reopened": True,
        "F24_actual_universal_word_evaluation_reopened": True,
        "root_actual_divisor_audit_fully_read": True,
        "root_review_and_replay_read_after_independent_PASS": True
    },
    "replay": {"comparison": bind(replay_path), "checks": 252309,
               "literal_negative_sources": 19, "original_source_rows": 64,
               "input_files": 8, "complete_program_bytes_unchanged": True,
               "raw_output_whole_bytes_identical": True,
               "raw_stdout_whole_bytes_identical": True, "output_rewriting_used": False},
    "printed_and_coordinate_audit": {
        "output": bind(printed_path), "checks": 27737,
        "all_50_printed_pivots_and_terminal_block_checked": True,
        "all_1763_operations_and_51_unit_witness_divisors_checked": True,
        "both_full_gauge_inverse_maps_checked": True,
        "all_64_E_to_N_maps_checked": True,
        "both_paired_inverses_cleared_by_2r_checked": True,
        "anti_principal_parameter_map_checked": True
    },
    "proved_scope": {
        "matrix": "All fields, every characteristic, nonzero R,s,t,u,v,w,z and nontrivial deleted tuple.",
        "paired_cocycles": "Finite fields of odd characteristic, chi=(r,s,t,u,v,w,z), chi-prime=(-r,s,t,u,v,w,z), nonzero values and nontrivial deleted tuple; r^2=1 included.",
        "exact_kernel": "{(b(chi-1),-b(chi-prime-1)):b in k}",
        "rank_on_original_generator_coordinates": 13,
        "summed_H1_restriction_injective": True,
        "positive_sign_transport": "The original B_+ and B_+ inverse of F23.13, with Y_i^+=B_+(X_i)."
    },
    "many_Frobenius_factor_consequence_claimed": False,
    "requested_corrections": [], "new_PDF_or_compiler_review_claimed": False,
    "all_frozen_author_and_prior_files_unchanged": True,
    "author_manifest_entries_verified": 69,
    "prior_entry_routes_verified": 400,
    "prior_distinct_recorded_paths_verified": 294,
    "prior_distinct_workspace_files_verified": 291,
    "exact_absolute_relative_path_transports": aliases,
    "preservation_count_precision_recorded": True,
    "cyclic_binding_introduced": False
}
target = PART / "review_f33.json"
assert not target.exists()
target.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": "PASS", "report": bind(report_path),
                  "metadata": bind(target), "binding_audit": bind(audit_path),
                  "manifest_entries": 69, "prior_routes": 400,
                  "prior_distinct_recorded_paths": 294,
                  "prior_distinct_workspace_files": 291}, indent=2))
