#!/usr/bin/env python3
"""Bind the independent four-order-three proof/source/code review."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "work/part_c"
REPLAY = BASE / "four_order_three_standard_peer_replay"
META = ROOT / "work/part_d_attack/actual_four_order_three_elements_and_cusp_comparison_result.json"
REPORT = BASE / "review_actual_four_order_three_elements_and_cusp_comparison.txt"
OUTPUT = REPORT.with_suffix(".json")


def bind(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)),
            "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


metadata = json.loads(META.read_text())
comparison = json.loads((REPLAY / "comparison.json").read_text())
assert bind(META)["sha256"] == "c1c043d263c17c78528df0db18fef9c6e57f0c47c438053345d427a2d667b00b"
assert comparison["status"] == "PASS"
assert comparison["named_checks"] == 22
assert comparison["actual_standard_image_order"] == 1080
assert comparison["all_four_output_and_stdout_files_whole_bytes_equal"]
for group in ("direct_author_binding_routes", "prior_author_binding_routes"):
    for route in comparison[group]:
        current = bind(ROOT / route["path"])
        assert current["sha256"] == route["sha256"]
        assert current["bytes"] == route["bytes"]
primary = {
    "status": "PASS",
    "date": "2026-11-14",
    "reviewer": "/root/c89_review_and_general_c",
    "sources": [{
        "url": "https://webusers.imj-prg.fr/~pierre.lochak/textes/inventiones.pdf",
        "retrieval_refs": ["turn1301view0", "turn1303view0", "turn1303view1"],
        "read_scope": "Printed 597 definitions (H), (A1)-(A3), Proposition(a); printed 598 unnumbered Corollary and complete proof, independently reopened. The retained full-text appendix proof through printed 600 was also read.",
        "verified_clause": "The full free profinite product of profinite factors has every nontrivial finite subgroup conjugate into a factor.",
        "application": "The already proved actual M=C2(tau)*C3(xi); order three excludes the C2 factor, and M_ab fixes the generator orientation.",
        "new_amalgam_recognition_theorem_imported": False,
        "retained_copies": metadata["primary_copies"]
    }, {
        "url": "https://mat.unb.br/~pz/arquivos/vfreepaper3.pdf",
        "read_scope": "Complete Theorem5, manuscript page4, independently read in the preceding accepted peer review; exact prior scope record bound here.",
        "verified_clause": "Full free profinite factor intersection, hence the positive normalizer and centralizer of the actual C3 factor.",
        "prior_primary_scope": bind(BASE / "order_three_defects_peer_replay/primary_read_scope.json")
    }],
    "new_primary_pdf_visual_review_claimed": False,
    "author_primary_comparison": bind(ROOT / "work/part_d_attack/four_order_three_primary_source_comparison.txt")
}
primary_path = REPLAY / "primary_read_scope.json"
assert not primary_path.exists()
primary_path.write_text(json.dumps(primary, indent=2) + "\n")
replay_files = [bind(path) for path in sorted(REPLAY.iterdir()) if path.is_file()]
record = {
    "status": "PASS",
    "date": "2026-11-14",
    "reviewer": "/root/c89_review_and_general_c",
    "review_kind": "Independent complete mathematical, primary-source, program and isolated-replay audit",
    "report": bind(REPORT),
    "report_line_count": len(REPORT.read_text().splitlines()),
    "sealer": bind(Path(__file__)),
    "reviewed_source": metadata["files"][0],
    "author_metadata": bind(META),
    "read_scope": {
        "proof_lines": 331,
        "program_lines": 137,
        "output_lines": 234,
        "author_primary_comparison_lines": 33,
        "author_metadata_fully_read": True,
        "all_proof_and_program_lines_read": True,
        "primary_read_scope": bind(primary_path),
        "previous_independent_full_order_three_review": [
            bind(BASE / "review_actual_order_three_defect_and_canonical_candidate.txt"),
            bind(BASE / "review_actual_order_three_defect_and_canonical_candidate.json")
        ]
    },
    "mathematical_review": {
        "original_objects_retained": ["F", "M", "M_all", "s", "h", "t", "j", "r", "g", "w", "p", "T"],
        "actual_C2_times_S3_quotient_and_inverse": "PASS",
        "full_positive_centralizers_of_s_and_j": "PASS",
        "finite_factor_conjugacy_hypotheses_and_signed_generator": "PASS",
        "normalizer_d_square_and_six_normal_forms": "PASS",
        "actual_transporter_to_j": "PASS",
        "four_point_completeness_and_choice_independent_inverse": "PASS",
        "finite_space_topologies": "PASS",
        "four_Phi_maps_and_canonical_closed_image": "PASS",
        "both_actual_involution_intertwinings": "PASS",
        "exact_original_free_image_and_quotient_automorphism": "PASS",
        "P0_amalgam_both_generator_maps_and_finite_embeddings": "PASS",
        "exact_index_twelve_kernel_quotient_comparison": "PASS",
        "full_image_equivalences_without_full_image_assertion": "PASS",
        "undivided_omega_matrix_calculation": "PASS",
        "actual_section_parity_transport": "PASS",
        "M_abelian_orientation_and_mod_three_congruence": "PASS",
        "epsilon_sigma_coefficient_transformations": "PASS",
        "closed_solution_space_T_homeomorphism_and_original_h_inverse": "PASS",
        "full_centralizer_argument_for_j_inversion": "PASS",
        "continuous_parameter_elimination_in_full_Zhat": "PASS",
        "original_F_cusp_word_and_exact_two_vectors": "PASS",
        "standard_full_word_successes_and_failures": "PASS",
        "solution_space_image_equality_scope": "PASS"
    },
    "replay": {
        "comparison": bind(REPLAY / "comparison.json"),
        "runner": bind(BASE / "code/replay_actual_four_order_three_standard.py"),
        "external_computational_inputs": [],
        "source_copy_bytes_unchanged": True,
        "exit_code": 0,
        "stderr_bytes": 0,
        "named_checks": 22,
        "actual_standard_image_order": 1080,
        "four_output_files_whole_bytes_identical": True,
        "output_transport": "Identity on all bytes in both directions.",
        "epsilon_rows": [1, -1, -1, 1],
        "sigma_rows": [1, -1, 1, -1],
        "nu_rows": [1, -1, 1, -1],
        "standard_cusp_zero_rows": [2, 3],
        "finite_failed_cusp_matrix_witnesses": [[0, 2, 2, 4], [1, 3, 3, 0]],
        "files": replay_files
    },
    "binding_review": {
        "direct_author_binding_routes_count": 22,
        "prior_author_binding_routes_count": 20,
        "unique_frozen_files_including_current_metadata_count": 29,
        "direct_author_binding_routes": comparison["direct_author_binding_routes"],
        "prior_author_binding_routes": comparison["prior_author_binding_routes"],
        "all_hashes_and_sizes_verified_before_and_after_replay": True,
        "all_hashes_and_sizes_verified_at_seal": True
    },
    "correction_requested": None,
    "author_files_modified": False,
    "new_numbered_claim_assigned": False,
    "retained_unresolved": [
        "Full generation H3=M, equivalently the full image of the actual P0 map.",
        "Unit coordinates of the canonical nu0 at primes other than two and three.",
        "The original full cusp-word zero for a remaining input.",
        "Original all-prime unit m, W=1, eta surjectivity and T nonemptiness."
    ]
}
assert not OUTPUT.exists()
OUTPUT.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": "PASS", "report": bind(REPORT),
                  "metadata": bind(OUTPUT), "primary_scope": bind(primary_path),
                  "replay_comparison": bind(REPLAY / "comparison.json")}, indent=2))
