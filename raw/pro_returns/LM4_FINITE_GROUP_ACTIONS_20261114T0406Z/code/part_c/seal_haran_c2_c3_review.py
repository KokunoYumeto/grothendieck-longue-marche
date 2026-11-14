#!/usr/bin/env python3
"""Seal the independent Haran source, marked-map and finite-witness audit."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "work/part_c"
REPLAY = BASE / "haran_c2_c3_peer_replay"
META = ROOT / "work/part_d_attack/haran_c2_c3_actual_map_comparison_result.json"
REPORT = BASE / "review_haran_c2_c3_actual_map_comparison.txt"


def bind(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)),
            "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


assert bind(META)["sha256"] == "fcac5535d5ba53ae9c67a4d09823c7c2970124466da6160abe6dbdb336d1d39d"
author = json.loads(META.read_text())
comparison_path = REPLAY / "comparison.json"
comparison = json.loads(comparison_path.read_text())
assert comparison["status"] == "PASS"
for entry in comparison["author_routes_verified"]:
    actual = bind(ROOT / entry["path"])
    assert actual["sha256"] == entry["sha256"]
    assert actual["bytes"] == entry["bytes"]
render_path = REPLAY / "primary/render_record.json"
render = json.loads(render_path.read_text())
for entry in render["images"]:
    actual = bind(ROOT / entry["path"])
    assert actual["sha256"] == entry["sha256"]
    assert actual["bytes"] == entry["bytes"]
primary = {
    "status": "PASS",
    "reviewer": "/root/c89_review_and_general_c",
    "date": "2026-11-14",
    "author_pdf_url": "https://www.math.tau.ac.il/~haran/Papers/closed_subgroups.pdf",
    "author_publications_url": "https://www.math.tau.ac.il/~haran/Papers/",
    "primary_pdf_ref": "turn1314view0",
    "read_refs": ["turn1317view0", "turn1317view1", "turn1317view2"],
    "author_publications_ref": "turn1320view0",
    "publisher_metadata_refs": ["turn1317search0", "turn1317search1"],
    "publisher_issue_open": "turn1319view0 timed out; no page reading claimed for this failed open.",
    "read_scope": [
        "Introduction and full-profinite notation, printed 266-267.",
        "Definition3.1, printed274; Definitions4.1-4.2 and Proposition4.3, printed277-278.",
        "Theorem5.1 and its complete displayed proof reduction/finite wreath-product construction, printed279-283.",
        "Corollary5.4 and complete Example5.5, printed283.",
        "Corollary9.6, printed297; Theorem9.7 and proof, printed298."
    ],
    "full_33_page_audit_claimed": False,
    "source_copies": author["primary_source_copies"],
    "render_record": bind(render_path),
    "actual_view_groups": [[283, 297], [298]],
    "actually_viewed_images": render["images"],
    "bibliography_record": bind(ROOT / "work/part_d_attack/haran_closed_subgroups_1987_reference.bib"),
    "bibliography_verdict": "PASS; exact author/title/journal/series/volume/issue/pages/year/DOI/author URL; no existing bibliography changed."
}
primary_path = REPLAY / "primary_read_scope.json"
assert not primary_path.exists()
primary_path.write_text(json.dumps(primary, indent=2) + "\n")
record = {
    "status": "PASS",
    "date": "2026-11-14",
    "reviewer": "/root/c89_review_and_general_c",
    "review_kind": "Independent complete proof/source/program/bibliography audit with isolated unchanged replay",
    "report": bind(REPORT),
    "report_lines": len(REPORT.read_text().splitlines()),
    "sealer": bind(Path(__file__)),
    "author_metadata": bind(META),
    "source": author["files"][0],
    "read_scope": {
        "proof_lines": 194,
        "program_lines": 123,
        "output_lines": 87,
        "bib_lines": 13,
        "metadata_entirely_read": True,
        "D32_entire_source_reopened": True,
        "primary_read_scope": bind(primary_path),
        "actual_primary_view_groups": [[283, 297], [298]],
        "prior_full_comparison_reviews": [
            bind(BASE / "review_actual_four_order_three_elements_and_cusp_comparison.txt"),
            bind(BASE / "review_actual_four_order_three_elements_and_cusp_comparison.json"),
            bind(BASE / "review_actual_order_three_defect_and_canonical_candidate.txt"),
            bind(BASE / "review_actual_order_three_defect_and_canonical_candidate.json")
        ]
    },
    "mathematical_review": {
        "actual_full_coproduct_and_factor_embeddings": "PASS",
        "complete_relative_intersection_family": "PASS",
        "Definitions4_1_4_2_local_lifts_and_target_constraints": "PASS",
        "separated_family_inheritance_hypotheses": "PASS",
        "exact_pro_p_input_obstruction_from_two_finite_injections": "PASS",
        "compact_chain_lower_bounds_and_minimal_closed_subgroup": "PASS",
        "particular_factor_generator_epimorphism": "PASS",
        "marked_map_noninjectivity_via_Q_e_inverse": "PASS",
        "actual_S4_surjection_and_proper_order_six_image": "PASS",
        "proper_H1_and_proper_Hstar_scope": "PASS",
        "S3_quotient_automorphism_q_e_equals_a_q": "PASS",
        "exact_original_free_image_e_F": "PASS",
        "coset_map_inverse_and_topology": "PASS",
        "full_induced_profinite_topology_for_Schreier_comparison": "PASS",
        "rank_and_character_no_proper_open_image_argument": "PASS",
        "literal_standard_J_word_defect_without_quotient_J_assumption": "PASS",
        "original_H3_j_and_cusp_scope_retained": "PASS"
    },
    "bibliography_review": {
        "verdict": "PASS",
        "record": bind(ROOT / "work/part_d_attack/haran_closed_subgroups_1987_reference.bib"),
        "existing_bibliography_modified": False
    },
    "replay": {
        "comparison": bind(comparison_path),
        "runner": bind(BASE / "code/replay_haran_c2_c3_witness.py"),
        "exit_code": 0,
        "stderr_bytes": 0,
        "external_computational_inputs": [],
        "named_checks": 11,
        "S3_conjugator_pairs": 36,
        "S4_image_order": 24,
        "proper_image_order": 6,
        "proper_image_fixed_point": 3,
        "standard_J_defect": [3, 4, 1, 2],
        "program_copy_whole_bytes_identical": True,
        "four_output_files_whole_bytes_identical": True,
        "output_transport_both_directions": "Identity on all bytes.",
        "files": [bind(path) for path in sorted(REPLAY.rglob("*")) if path.is_file()]
    },
    "author_routes_verified": comparison["author_routes_verified"],
    "all_author_routes_and_metadata_reverified_at_seal": True,
    "correction_requested": None,
    "author_files_modified": False,
    "new_numbered_claim_assigned": False,
    "retained_unresolved": [
        "No identification of Hstar or H1 with the original H3.",
        "No injectivity or full-image conclusion for the original Phi_kappa.",
        "No original all-prime unit, cusp-word zero, or T nonemptiness conclusion."
    ]
}
out = REPORT.with_suffix(".json")
assert not out.exists()
out.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": "PASS", "report": bind(REPORT),
                  "metadata": bind(out), "primary_scope": bind(primary_path),
                  "comparison": bind(comparison_path)}, indent=2))
