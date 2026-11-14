#!/usr/bin/env python3
"""Bind the independent full proof/program review and literal replay."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
STEM = "work/part_c/review_actual_order_three_defect_and_canonical_candidate"
AUTHOR = "work/part_d_attack/actual_order_three_defect_and_canonical_candidate_result.json"
EXPECTED_AUTHOR = "b5c422c5570c93f8ce4c795412a8426d9c7d3edd88e5465984ccd3b8fd087923"
COMPARISON = "work/part_c/order_three_defects_peer_replay/comparison.json"
EXPECTED_COMPARISON = "d33d78c7ea75217be996e70739290358aad0231e219d4fe93b4340b51924292c"

def bind(path):
    item = ROOT / path
    value = item.read_bytes()
    return {"path": path, "sha256": hashlib.sha256(value).hexdigest(), "bytes": len(value),
            "lines": len(value.splitlines()) if item.suffix != ".pdf" else None}

assert bind(AUTHOR)["sha256"] == EXPECTED_AUTHOR
assert bind(COMPARISON)["sha256"] == EXPECTED_COMPARISON
metadata = json.loads((ROOT / AUTHOR).read_text())
routes = []
for group in ("files", "dependencies", "source_comparison_only"):
    for expected in metadata[group]:
        actual = bind(expected["path"])
        assert actual["sha256"] == expected["sha256"]
        assert actual["bytes"] == expected["bytes"]
        routes.append({"group": group, **actual})
assert len(routes) == 20
comparison = json.loads((ROOT / COMPARISON).read_text())
assert comparison["status"] == "PASS"
assert comparison["all_four_output_and_stdout_files_whole_bytes_equal"]
replay_files = [
    bind(str(path.relative_to(ROOT)))
    for path in sorted((ROOT / "work/part_c/order_three_defects_peer_replay").iterdir())
    if path.is_file()
]
report = bind(STEM + ".txt")
record = {
    "title": "Independent peer review of the actual order-three defects and canonical original pants candidate",
    "date": "2026-11-14",
    "reviewer": "/root/c89_review_and_general_c",
    "verdict": "PASS",
    "correction_requested": False,
    "numbered_claim_assigned_by_reviewer": False,
    "report": report,
    "author_metadata": bind(AUTHOR),
    "all_20_author_routes_verified": routes,
    "full_read_scope": {
        "new_proof_lines": 424,
        "new_program_lines": 255,
        "new_output_lines": 209,
        "author_metadata": "Complete",
        "order_three_primary_comparison_lines": 40,
        "marked_v4_dependency_lines": 256,
        "norm_odd_local_dependency_lines": 287,
        "class_two_gt0_dependency_lines": 229,
        "single_parameter_dependency": "Lines 1-105, including both solution-space maps and inverses.",
        "d74_dependency": "Lines 562-646, including the centralizer, unique-h and original D74.40 scope.",
        "marked_primary_comparison_lines": 40,
        "remaining_dependency_scope": "Hash verified; previous accepted audits retained, with no claim of another complete rereading."
    },
    "mathematical_checks": {
        "actual_overgroup_topology_and_embedding": "PASS",
        "C2_C3_full_kernel_and_quotient_inverse_maps": "PASS",
        "actual_Gplus_and_cyclic_extension_maps": "PASS",
        "full_unit_family_inverse_and_two_intertwinings": "PASS",
        "three_literal_ambient_defect_identifications": "PASS",
        "complete_extension_space_homeomorphism": "PASS",
        "full_abelian_epsilon_obstruction_and_mod_four_scope": "PASS",
        "alpha_inverted_cusp_alignment_using_original_section_classes": "PASS",
        "forward_transport_to_original_T_without_surjectivity": "PASS",
        "reverse_original_reflection_normalization": "PASS",
        "both_mod_four_original_gnu_wnu_formulas": "PASS",
        "actual_rho_M_and_OT23_inverse": "PASS",
        "extension_uniqueness_via_actual_image_centralizer": "PASS",
        "projection_homeomorphism_to_original_T": "PASS",
        "full_original_W_and_exact_two_gate_set_identity": "PASS",
        "both_conjugator_fibers_and_character_inverse": "PASS",
        "original_standard_input_scope": "PASS"
    },
    "replay": {
        "comparison": bind(COMPARISON),
        "runner": bind("work/part_c/code/replay_actual_order_three_defects.py"),
        "files": replay_files,
        "unchanged_program": True,
        "external_input_files": [],
        "exit_code": 0,
        "stderr_bytes": 0,
        "named_checks": 24,
        "free_words": 161,
        "defect_cases": 644,
        "exact_zero_triples": [
            {"nu": -1, "epsilon": 1, "c": "y"},
            {"nu": 1, "epsilon": -1, "c": "x^-1"}],
        "finite_nonzero_separations": 642,
        "finite_nonzero_separations_by_prime": {"3": 598, "5": 44},
        "full_output_forward_map": "Identity on every byte.",
        "full_output_inverse_map": "Identity on every byte.",
        "all_four_output_stdout_files_exact_equal": True,
        "scope": "The actual original standard h=1,g=x^-1,w=x,m=-1 and full units nu=-1,+1 only."
    },
    "primary_read_scope": bind("work/part_c/order_three_defects_peer_replay/primary_read_scope.json"),
    "retained_unresolved": [
        "m=a-b is not established to be a unit in the full profinite integers for a remaining input.",
        "The full original W is not established to be 1 for a remaining input.",
        "The actual eta image <z,g> is not established to be all F.",
        "Original T nonemptiness and full D74.40 realization remain unproved."
    ],
    "frozen_author_and_dependency_files_changed": False,
    "sealer": bind(str(Path(__file__).relative_to(ROOT)))
}
(ROOT / (STEM + ".json")).write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"verdict": "PASS", "report": report, "metadata": bind(STEM + ".json"),
                  "author_routes": 20}, indent=2))
