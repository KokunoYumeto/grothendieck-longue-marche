#!/usr/bin/env python3
"""Bind the independent actual-transporter review to its frozen evidence."""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
PEER = ROOT / "work/part_c"
AUTHOR = ROOT / "work/part_d_attack"

def binding(path):
    raw = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(raw),
            "lines": len(raw.splitlines()), "sha256": hashlib.sha256(raw).hexdigest()}

meta_path = AUTHOR / "actual_transporter_single_parameter_reduction_result.json"
assert binding(meta_path)["sha256"] == "cc281bb8abf4e351971891dc881106143449491d81abef5ce33d10cde632d4bf"
metadata = json.loads(meta_path.read_text())
bound = []
for entry in metadata["files"] + metadata["dependency_bindings"]:
    observed = binding(ROOT / entry["path"])
    assert observed["sha256"] == entry["sha256"]
    assert observed["bytes"] == entry["bytes"]
    assert observed["lines"] == entry["lines"]
    bound.append(observed)

comparison_path = PEER / "actual_transporter_independent_replay/comparison.json"
assert binding(comparison_path)["sha256"] == "4d552dc69bf21ef94b4b743570f43f2780b99156d19483e8c635f976c50980a4"
comparison = json.loads(comparison_path.read_text())
assert comparison["status"] == "PASS"
assert comparison["named_assertions"] == 24
assert comparison["retained_refined_conjugator_witnesses"] == 40
for row in comparison["replay_files"]:
    observed = binding(ROOT / row["path"])
    assert observed["sha256"] == row["sha256"] and observed["bytes"] == row["bytes"]

report = PEER / "review_actual_transporter_single_parameter_reduction.txt"
assert "Verdict: PASS." in report.read_text()
output = json.loads((AUTHOR / "code/actual_transporter_reduction_output.json").read_text())

result = {
    "title": "Independent review of the actual transporter single-parameter reduction",
    "reviewer": "/root/c89_review_and_general_c",
    "sealed_utc": datetime.now(timezone.utc).isoformat(),
    "verdict": "PASS",
    "mathematical_corrections_requested": [],
    "program_corrections_requested": [],
    "full_proof_read": {"lines": 391, "complete": True},
    "full_canonical_program_read": {"lines": 361, "complete": True},
    "review_report": binding(report),
    "author_metadata": binding(meta_path),
    "author_metadata_entries_verified": len(bound),
    "frozen_author_files_and_dependencies": bound,
    "additional_dependency_passage": {
        "file": binding(ROOT / "work/part_a/a.tex"),
        "passage": "Claim A.7 and its proof; full peripheral centralizer used on original <xy>.",
        "entire_file_reread": False,
    },
    "dependency_passages_checked": [
        "D.74: actual dihedral maps and labelled endpoints, whole section centralizers, unique h, original equation D.74.40.",
        "D.35: original solution space and complete conjugator fiber; actual standard-extension coproduct maps retained as a frozen dependency.",
        "pants_section_lifts_and_peripheral_comparison: section C, explicit q4/i/rho/tau maps, labelled section images, identity on full abelianization.",
        "tau_original_cusp_followup: sections A and B, primitive-character full centralizer proof, entire image normalizers, actual original z endpoint maps.",
    ],
    "mathematical_checks": {
        "original_endpoint_transporters_and_full_uniqueness": "PASS",
        "full_half_unit_map_and_inverse_topology": "PASS",
        "necessity_with_even_reflection_correction": "PASS",
        "sufficiency_with_exact_product_order": "PASS",
        "Phi_and_explicit_character_inverse_both_composites": "PASS",
        "reflection_coordinate_change": "PASS",
        "alpha_D_sign_identity": "PASS",
        "full_abelianization_and_D_in_F_prime": "PASS",
        "fixed_generated_subgroup_for_all_full_units": "PASS",
        "entire_tau_image_normalizer_and_factor_labels": "PASS",
        "Phi_tau_and_explicit_character_inverse_both_composites": "PASS",
        "actual_solution_map_is_identity_on_mu_lambda_coordinates": "PASS",
        "exact_remaining_kernel_intersection": "PASS",
        "finite_modulus_2e_and_same_level_T_to_B_map": "PASS",
        "both_compactness_refinements_and_B_fine_to_T_coarse_map": "PASS",
        "actual_A5_times_C2_cubed_quotient": "PASS",
        "exact_mod2_homology_kernel_and_affine_image": "PASS",
        "actual_delta_edge_action": "PASS",
        "exact_surjective_refinement_map_to_coarse_quotient": "PASS",
        "exhaustive_affine_exponent_calculation": "PASS",
        "complete_61_dimensional_conjugator_linear_systems": "PASS",
        "all_unit_tables_counts_and_residual_scope": "PASS",
    },
    "isolated_replay": {
        "comparison": binding(comparison_path),
        "runner": binding(PEER / "code/replay_actual_transporter_reduction.py"),
        "files": [binding(ROOT / row["path"]) for row in comparison["replay_files"]],
        "exit_code": 0,
        "stderr_bytes": 0,
        "named_checks": 24,
        "base_unit_rows": 16,
        "refined_unit_rows": 32,
        "retained_refined_conjugator_witnesses": 40,
        "full_group_assertions_per_retained_witness": 2,
        "literal_reflection_comparisons": 480,
        "output_and_stdout_byte_identical_to_frozen_evidence": True,
        "path_transport_used": False,
        "method": "Unchanged canonical producer copied and executed in a separate directory; mathematical completeness audited separately from the code.",
        "independent_new_finite_algorithm_claimed": False,
    },
    "finite_results": {
        "base_total_order": output["base_total_order"],
        "base_parity_order": output["base_parity_order"],
        "base_parity_exponent": output["base_parity_exponent"],
        "refined_parity_group_order": output["refined_parity_group_order"],
        "refined_parity_exponent": output["refined_parity_exponent"],
        "base_B_unit_residues": output["base_B_unit_residues"],
        "base_T_unit_residues": output["base_T_unit_residues"],
        "refined_B_unit_residues": output["refined_B_unit_residues"],
        "refined_T_unit_residues": output["refined_T_unit_residues"],
        "base_nonempty_fiber_conjugators": 20,
        "refined_nonempty_fiber_conjugators": 40960,
        "refined_consistent_base_cosets_per_nonempty_fiber": 5,
        "solutions_per_consistent_base_coset": 8192,
    },
    "unresolved_scope_retained": metadata["unresolved"],
    "frozen_sources_modified": False,
    "author_metadata_pending_fields_modified": False,
    "numbered_claim_registered_by_peer": False,
    "fresh_PDF_or_compiler_review_claimed": False,
    "record_builder": binding(Path(__file__).resolve()),
}
target = PEER / "review_actual_transporter_single_parameter_reduction.json"
target.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"status": "PASS", "report": binding(report), "metadata": binding(target)}, indent=2))
