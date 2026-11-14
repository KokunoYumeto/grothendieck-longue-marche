#!/usr/bin/env python3
"""Seal the independent canonical-transporter proof and unchanged replay audit."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "work/part_c"
REPLAY = BASE / "canonical_transporter_peer_replay"
META = ROOT / "work/part_d_attack/actual_canonical_transporter_and_cusp_membership_result.json"
REPORT = BASE / "review_actual_canonical_transporter_and_cusp_membership.txt"
TARGET = REPORT.with_suffix(".json")


def bind(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)),
            "sha256": hashlib.sha256(data).hexdigest(),
            "bytes": len(data), "lines": len(data.splitlines())}


def bindings(value):
    if isinstance(value, dict):
        if "path" in value and "sha256" in value:
            yield value
        for item in value.values():
            yield from bindings(item)
    elif isinstance(value, list):
        for item in value:
            yield from bindings(item)


assert bind(META)["sha256"] == "62c400ad942308fb77906084f4cbfbe70a9f9f42fbd5b3fff042a65076bfa08a"
author = json.loads(META.read_text())
comparison_path = REPLAY / "comparison.json"
comparison = json.loads(comparison_path.read_text())
assert comparison["status"] == "PASS"
assert bind(comparison_path)["sha256"] == "dc9669333965828eab6ae4ac7b8f2aa6e3a3a23abfaac0cc09f191f2f1ff44ff"
assert bind(REPORT)["sha256"] == "5b3430238706432f2c655e01dad81b6996ec75c6e2e5744a7ab1cee4179eecad"
for item in bindings(comparison):
    actual = bind(ROOT / item["path"])
    for key in ("sha256", "bytes", "lines"):
        if key in item:
            assert actual[key] == item[key], (item["path"], key)

record = {
    "status": "PASS", "date": "2026-11-14",
    "reviewer": "/root/c89_review_and_general_c",
    "review_kind": "Independent complete proof/program/output/metadata review and unchanged isolated replay",
    "source": author["files"][0], "author_metadata": bind(META),
    "report": bind(REPORT), "sealer": bind(Path(__file__)),
    "read_scope": {
        "complete_proof_lines": 246,
        "complete_metadata_lines": 123,
        "complete_program_lines": 193,
        "complete_output_lines": 199,
        "reopened_prerequisites": [
            "Four-point comparison Sections1-3,5-7: actual quotient, centralizers, complete sign pairs and original T maps.",
            "GT0 class-two continuation equations9-15: exact Omega(s), qz0, r and original u1.",
            "Marked V4 continuation Sections1-3: exact p,r,v,g,w,t-prime and all original quotient coordinates.",
            "Actual J continuation full centralizer and unique original-section transporter conclusions."
        ],
        "new_primary_theorem_imported": False,
        "new_primary_pdf_view_claimed": False,
        "new_compilation_or_final_pdf_review_claimed": False
    },
    "mathematical_findings": [
        "Unique original a in F-prime, with the exact S3 conjugator adjustment and full conjugate-factor centralizer.",
        "Ordered d=tau a-inverse s is the unique negative normalizer involution in its specified quotient coset.",
        "Unique F transporter L, exact inverse recovery of d and a, and continuous compact-orbit inverse maps.",
        "Exact CT.5 full-word expansion; original coefficient nu0=1+6chi_x(L), with only 2- and 3-adic units inferred.",
        "Literal r=xi-inverse s xi is the old qz0 z reflection, by exact Omega-square calculation.",
        "Both A/B word forms, both sums and both coordinate differences verified on the original basis.",
        "Both cusp equivalences use full original reflection classes, trivial full centralizers and exact forced exponents.",
        "Exact B-to-A coset maps and continuous parity map R, whose inverse on the two cosets is Sigma(A)-1.",
        "Explicit four-row inverse table from the final gate to the previously accepted Z_K and original T.",
        "Full-unit and original-word gates remain unproved; no original T nonemptiness or H3 generation inferred."
    ],
    "requested_corrections": [],
    "replay": {
        "comparison": bind(comparison_path),
        "runner": comparison["runner"],
        "program": comparison["program"],
        "copied_program": comparison["copied_program"],
        "output": comparison["replay_output"],
        "stdout": comparison["replay_stdout"],
        "stderr": comparison["replay_stderr"],
        "exit_code": 0,
        "named_checks": 20,
        "universal_odd_exponent_cases": 17,
        "integral_branch_cases": 19,
        "external_computational_inputs": [],
        "complete_program_bytes_unchanged": True,
        "whole_output_raw_byte_identity": True,
        "output_path_or_schema_rewrite_used": False,
        "formal_letters_are_new_original_inputs": False,
        "finite_cases_used_as_proof_of_all_profinite_exponents": False
    },
    "author_files": author["files"],
    "mathematical_dependencies": author["mathematical_dependencies"],
    "direct_author_binding_routes": comparison["author_routes_verified_before_and_after"],
    "accepted_predecessor_metadata": comparison["predecessor_metadata"],
    "accepted_predecessor_binding_routes": comparison["predecessor_routes_verified_before_and_after"],
    "prior_review_and_acceptance": [
        bind(BASE / "review_actual_four_order_three_elements_and_cusp_comparison.txt"),
        bind(BASE / "review_actual_four_order_three_elements_and_cusp_comparison.json"),
        bind(ROOT / "work/root/four_order_three_continuation_acceptance.json")
    ],
    "all_frozen_author_files_unchanged": True,
    "original_inputs_retained": author["original_inputs_retained"],
    "retained_unproved_gates": author["retained_unproved_gates"]
}
routes = list(bindings(record))
for item in routes:
    actual = bind(ROOT / item["path"])
    for key in ("sha256", "bytes", "lines"):
        if key in item:
            assert actual[key] == item[key], (item["path"], key)
record["binding_verification"] = {
    "status": "PASS", "routes": len(routes),
    "unique_paths": len({item["path"] for item in routes}),
    "sha256_bytes_and_available_line_counts_checked": True
}
assert not TARGET.exists()
TARGET.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": "PASS", "report": bind(REPORT),
                  "metadata": bind(TARGET),
                  "binding_verification": record["binding_verification"]}, indent=2))
