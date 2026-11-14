#!/usr/bin/env python3
"""Seal the actual 33 peer image views and complete final-600 log review."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "work/part_c"
PDF = ROOT / "deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf"
EXPECTED_PDF = "42ef0d3fff1be048a0c3d09f065c19114341f15174930173ce847bbcd0b0ae8f"
PAGES = [
    360, 400, 440, 459, 475, 480, 491, 492, 493, 494, 495, 520,
    544, 555, 556, 557, 565, 575, 578, 580, 581, 582, 583, 584,
    585, 586, 587, 588, 589, 590, 591, 596, 600,
]


def binding(path):
    path = Path(path)
    if not path.is_absolute():
        path = ROOT / path
    data = path.read_bytes()
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


assert binding(PDF)["sha256"] == EXPECTED_PDF
assert PDF.stat().st_size == 4061958
prep_path = ROOT / "work/root/render_preparation_600_final.json"
prep = json.loads(prep_path.read_text())
assert prep["sha256"] == EXPECTED_PDF and prep["pages"] == 600
assert prep["peer_pages"] == PAGES
assert len(prep["images"]) == 74 and len(prep["root_pages"]) == 41
rows = [r for r in prep["images"] if r["reviewer"] == "peer"]
assert [r["page"] for r in rows] == PAGES
for row in prep["images"]:
    actual = binding(row["path"])
    assert actual["sha256"] == row["sha256"]
    assert actual["bytes"] == row["bytes"]
for row in rows:
    assert not row["byte_identical_to_prior_587_image"]

observations = {
    360: "D.37l partition table, D.37m marking and inverse substitutions, and D.37n actual deck map render clearly; long conjugation words, columns, tags and footer are unobstructed.",
    400: "D.54k-l norm and cube formulas, the proof ending, and D.55a-c finite-torsion statement render cleanly, including all prime subscripts and the nine-type list.",
    440: "D.69g-l chain boundary, both inverse module maps, cohomology decomposition and rank-one calculation are complete and legible.",
    459: "Historical D.74.1 visibly retains alpha(x)=x^{-1}, alpha(y)=f^{-1}y^{-1}f and f in F'; the D.74 heading, D.74.2-3 and preceding D.73w-x are clear.",
    475: "D.77.8-12 permutation quotient, actual generated-image comparison, incidence differential and coset map fit cleanly; all cycle symbols, hats and group labels remain legible.",
    480: "D.78.21 and the retained kernel/scope conclusion are clear; the transition to Part E and E.1 multiplication and exact sequences renders cleanly.",
    491: "F.7 Open heading and its first overview page are fully visible, including F.7.1 and the retained residual source-membership scope.",
    492: "The F.7 overview visibly incorporates F.27 and F.28, gives the exact two- and three-parameter character loci and rank 6m+1, and retains the unresolved general character locus, full marginal and intersection-image questions. The source audit and F.7.2 remain legible.",
    493: "F.7.3-6 and the solvable induction are clear; long closure/intersection expressions, exact-sequence arrows and the final displayed normalizer equality do not collide with the footer.",
    494: "The F.7 finite A5-image argument and its exceptional/free-orbit paragraphs render cleanly, with clear subgroup and wreath-product notation.",
    495: "F.7.7-9 compact-coset formula, pointed exact sequence and the 36-set intersection display are complete and legible.",
    520: "F.11.16-17 literal braid words and Artin identities, the proof ending, and F.12.1-3 actual based injection and configuration map render clearly.",
    544: "Historical F.19.9 and its actual gamma map are fully visible; F.19.10 commutative exact diagram and F.19.11 inverse coordinates have clear alignment. F.19.5-13 are legible.",
    555: "F.21.5-10 actual source coordinates and covering maps are legible; the long inverse-coordinate display F.21.10 stays within the page.",
    556: "Historical exponent pairs are visibly (0,3),(2,4),(3,2),(4,0), with h=3(1+j) mod 5; F.21.11-16, the derivative formula and quotient maps are clear.",
    557: "F.21.17-23 section, double cover, rational map, three identities and filling comparison render cleanly, including the final subgroup-factorization display.",
    565: "F.22.23 exact diagram and the F.23 opening statement/diagrams render clearly; the source-sign map, all finite-image scope and retained hypotheses remain visible.",
    575: "F.24 restriction/cohomology/sign comparison and affine fixed-point proof ending are legible; F.24.15-16 and the averaging formula are properly separated and tagged.",
    578: "F.25 proof ending and F.26 opening are clear; F.26.1-5 affine reduction, trace criterion and order-nine conclusion are fully visible and properly tagged.",
    580: "F.26.13-17 cocycle criterion, tensor/Frobenius map and explicit inverse render cleanly, including all indexed denominators and the final trace-sum display.",
    581: "F.26.18-22 field operations, exhaustive count 7560, 64-row rank table and real block matrix render correctly.",
    582: "F.26.23-24 and its proof ending are visible. The corrected F3-linear-span wording for actual source-conjugate rows is retained. F.27 begins cleanly with its complete title and displays F.27.1-2.",
    583: "F.27.3-8 summed restriction, exact cocycle kernel, field comparisons, nonzero factors and coefficient/principal-quotient maps are fully legible.",
    584: "F.27.9-16 actual source action, source labels, explicit basis and inverse, principal corrections, and the entire five-by-five matrix H render clearly; the matrix and tag fit above the footer.",
    585: "F.27.17-23 both determinant formulas, essential-line proof, actual seed index 25, seed-conjugate evaluations and Frobenius/Vandermonde determinant are fully visible and legible.",
    586: "F.27.24 explicit Vandermonde inverse and the complete summed-kernel/trace/sign proof ending render clearly. The 699-check evidence paragraph and F.28 opening heading and first statement lines are unobstructed.",
    587: "F.28.1-5 character locus, affine equality, exceptional cases, coefficient map and principal quotient render cleanly; all field and nonvanishing hypotheses are readable.",
    588: "F.28.6-12 actual inclusion/projection/section maps, explicit basis, block action, original-index table and actual seed evaluations render clearly. The comparison table has legible columns and the separate boundary scalar is properly aligned.",
    589: "F.28.13-15 Frobenius-pair separation, every cross-type comparison paragraph, summed restriction and the explicit intertwiner map render cleanly, with no obscured exponents or subscripts.",
    590: "F.28.16 exact cocycle kernel and the full trace/affine/sign proof ending are legible. The 781-check certificate paragraph and final proof square are present, followed by normal clear page space.",
    591: "References begin on the page after the completed F.28 proof; entries 1-8 and their verification notes have readable wrapping and clear glyphs.",
    596: "References 43-51 and their detailed verification notes render cleanly, including the original-topology C81 scope in entry 46; no clipped names, URLs or mathematical notation.",
    600: "The continuation of reference 76 and final entry 77 are clear; the final page ends normally with an unobstructed page-number footer and no truncated content.",
}
assert sorted(observations) == PAGES
view_groups = [PAGES[i:i+2] for i in range(0, len(PAGES), 2)]
assert len(view_groups) == 17 and all(1 <= len(g) <= 2 for g in view_groups)
for row in rows:
    row.update({
        "actual_viewed": True,
        "fresh_view_for_this_final_pdf": True,
        "review_result": "PASS",
        "observation": observations[row["page"]],
    })

copies = {
    "LM4_FINITE_GROUP_ACTIONS_paper.log": "final_600_build.log",
    "LM4_FINITE_GROUP_ACTIONS_paper.blg": "final_600_build.blg",
    "build_commands.json": "final_600_build_commands.json",
    "build_artifact.json": "final_600_build_artifact.json",
    **{f"build_stage_{i}_stdout.txt": f"final_600_stage_{i}_stdout.txt"
       for i in range(1, 5)},
}
logs = []
for src, dest in copies.items():
    source = ROOT / "deliverable" / src
    target = OUT / dest
    assert target.exists() and source.read_bytes() == target.read_bytes()
    row = binding(target)
    row["source_path"] = str(source.relative_to(ROOT))
    row["lines"] = len(target.read_bytes().splitlines())
    row["read_in_full"] = True
    logs.append(row)

log = (OUT / "final_600_build.log").read_text()
blg = (OUT / "final_600_build.blg").read_text()
stages = [(OUT / f"final_600_stage_{i}_stdout.txt").read_text()
          for i in range(1, 5)]
assert stages[2] == stages[3] and stages[0] != stages[2]
commands = json.loads((OUT / "final_600_build_commands.json").read_text())
assert len(commands) == 4 and all(c["exit_code"] == 0 for c in commands)
artifact = json.loads((OUT / "final_600_build_artifact.json").read_text())
assert artifact["pdf_sha256"] == EXPECTED_PDF
for name, expected in artifact["source_sha256"].items():
    assert binding(ROOT / "deliverable" / name)["sha256"] == expected

counts = {
    "overfull_boxes": len(re.findall(r"Overfull \\[hv]box", log)),
    "underfull_hboxes": len(re.findall(r"Underfull \\hbox", log)),
    "underfull_vboxes": len(re.findall(r"Underfull \\vbox", log)),
    "missing_characters": log.count("Missing character:"),
    "undefined_control_sequences": log.count("Undefined control sequence"),
    "undefined_reference_or_citation_lines": sum(
        "undefined" in line.lower() and
        ("reference" in line.lower() or "citation" in line.lower())
        for line in log.splitlines()),
    "latex_warnings": log.count("LaTeX Warning:"),
    "package_warning_lines": len(re.findall(r"^Package .+ Warning:", log, re.M)),
    "latex_font_warnings": log.count("LaTeX Font Warning:"),
    "fatal_error_lines": sum(
        line.startswith("!") or "Fatal error" in line or "Emergency stop" in line
        for line in log.splitlines()),
    "luaotfload_fallback_events": log.count("Error in luaotfload: reverting to OT1"),
    "generic_microtype_protrusion_notices": log.count("Loading generic protrusion settings"),
    "bibtex_warnings": len(re.findall(r"^Warning--", blg, re.M)),
}
expected_counts = {
    "overfull_boxes": 0, "underfull_hboxes": 1, "underfull_vboxes": 0,
    "missing_characters": 0, "undefined_control_sequences": 0,
    "undefined_reference_or_citation_lines": 0, "latex_warnings": 0,
    "package_warning_lines": 0, "latex_font_warnings": 0,
    "fatal_error_lines": 0, "luaotfload_fallback_events": 1,
    "generic_microtype_protrusion_notices": 2, "bibtex_warnings": 1,
}
assert counts == expected_counts
assert "badness 7133" in log and "lines 62--63" in log
assert "has not \nchanged." in log and "You've used 77 entries" in blg
assert stages[0].count("LaTeX Warning: Label(s) may have changed.") == 1
assert "LaTeX Warning:" not in stages[2] and "LaTeX Warning:" not in stages[3]
stage_counts = []
for number, text in enumerate(stages, 1):
    row = {
        "stage": number,
        "latex_warnings": text.count("LaTeX Warning:"),
        "label_rerun_warnings": text.count("Label(s) may have changed."),
        "underfull_hboxes": text.count("Underfull \\hbox"),
        "luaotfload_fallback_events": text.count("Error in luaotfload: reverting to OT1"),
        "bibtex_warnings": len(re.findall(r"^Warning--", text, re.M)),
        "overfull_boxes": len(re.findall(r"Overfull \\[hv]box", text)),
        "missing_characters": text.count("Missing character:"),
        "undefined_control_sequences": text.count("Undefined control sequence"),
        "fatal_error_lines": sum(line.startswith("!") or "Fatal error" in line
                                 or "Emergency stop" in line for line in text.splitlines()),
    }
    assert row["overfull_boxes"] == row["missing_characters"] == 0
    assert row["undefined_control_sequences"] == row["fatal_error_lines"] == 0
    assert row["latex_warnings"] == (1 if number == 1 else 0)
    assert row["underfull_hboxes"] == (0 if number == 2 else 1)
    assert row["luaotfload_fallback_events"] == (0 if number == 2 else 1)
    assert row["bibtex_warnings"] == (1 if number == 2 else 0)
    stage_counts.append(row)
bib = (ROOT / "deliverable/LM4_FINITE_GROUP_ACTIONS_references.bib").read_text()
records = re.findall(r"(?m)^\s*@(\w+)\s*\{", bib)
record_count = sum(t.lower() not in {"comment", "string", "preamble"}
                   for t in records)
assert record_count == 87
assert len(re.findall(r"\\bibitem\{", (ROOT / "deliverable/LM4_FINITE_GROUP_ACTIONS_paper.bbl").read_text())) == 77

frozen = {
    "work/part_c/c91.tex": "0b5db75c25411d069d4316995b410faab63b5c624bed7f4044a963e27d1952ff",
    "work/part_c/c91_result.json": "e04468571d33ee0e597c3a14ecacd4f4552733d9440e49c977ac2cfcd12b582d",
    "work/part_c/c91_report.txt": "22bcb412d6e1e6cfadda05ee0fcc1c42e4ae8d818b8f4af3f838b33b5d39a485",
    "work/part_c/c91_provenance.json": "b5c94078c4b95d0c852736637f93085fa1b5b4eb1ded0de78da80693f2384197",
    "work/part_c/general_pointed_descent_comparison.tex": "71d95a8bcb21e20e7118f8a0f07ba9caadbefbb5d89796d6475aab0e63b8a620",
    "work/part_c/c92.tex": "e978d4c54fa14090d67e1fd0620561bd251a8e3673132284aa144030b129ad7c",
    "work/part_c/c92_result.json": "f361c746cc709a5b164975166af8ae35accbe8e47c700041233a53f850c0ab05",
    "work/part_c/c92_report.txt": "f28cdf1f7480f7636108930ee8f1de196b10b41beb9fe19b1d369f6b6eabc09b",
    "work/part_c/c92_provenance.json": "9a9085c616e66a9ac4dc5dc4d7cbe801b6425c430ed6772db15516a562ee354c",
    "work/part_a/f_trace_obstruction_and_f9_images.tex": "1db6b7ce7170a2da642989abe86198811e9e4dbb42288d67263dd823932e1449",
    "work/part_c/review_f26.txt": "1e17eb9561b0b4a4316022279bbb3a419f6d179fcb4c62fab72c58243b09bd56",
    "work/part_c/review_f26.json": "a6f84ee112165ba77a5ee6faec7da00c89df6544e517a5963ccdf3a4a89fcffa",
    "work/part_a/f_product_one_character_locus_images.tex": "91dbd2e919ebda809dcfaa61f05d2ee465ef67739252b34991fb29fc44c9d21f",
    "work/part_a/f_product_one_character_locus_images_results.json": "f0c8784aefaff5d7d82e3233640e876a3fd88fe972bd69ee60c1c0f1c8b4c4a4",
    "work/part_a/f_product_one_character_locus_images_report.txt": "28d8a5575fde7192d706cf04242d7a50adfd08c7e700d9091c9da330b4318efb",
    "work/part_a/f_product_one_character_locus_images_evidence_manifest.json": "7d742227687538a8bd4b378b6658569e34b02c7a9d108fe600777cb84d1f9e71",
    "work/part_c/review_f27.txt": "4a0a2ecdb7b18180167a0b4ca5da62562fa9297132f42e40108e746977d308ea",
    "work/part_c/review_f27.json": "02914ec97996180695a2682b9c45a0aa8b9dee97d9b957c5685fb8bbc32564c5",
    "work/part_a/f_three_parameter_product_one_images.tex": "b9e5941bddeb92cc831825c067bc1ff8c6e8b952f35eb608cf02c142dae26262",
    "work/part_a/f_three_parameter_product_one_images_results.json": "63c995d853a0f1a604760e1688e65d20ec9f9b52baf691ebc7cb5dd44c5d03a3",
    "work/part_a/f_three_parameter_product_one_images_report.txt": "3251321d35f2be8684185e2672ed886fbc025b4debf34ef01672e076a62bbeca",
    "work/part_a/f_three_parameter_product_one_images_evidence_manifest.json": "4f9bfde218594399390965cf2878a01afcf2cff235c45bfd1c6d6a341ecb777f",
    "work/part_c/review_f28.txt": "f8dd555419ff9279786a77bbd3dd241965647bd5410afc0b388167150e0c4311",
    "work/part_c/review_f28.json": "3b0ce1d77b45fe76bc5aeefd5dc962b0e77a2ec6566466c5dec5c31e635bc726",
}
for path, digest in frozen.items():
    assert binding(path)["sha256"] == digest, path
assert binding(PDF)["sha256"] == EXPECTED_PDF

result = {
    "reviewer": "/root/c89_review_and_general_c",
    "review_scope": "Independent actual visual review of the 33 assigned final-600 pages and complete final build-log/stage review.",
    "status": "PASS",
    "sealed_at_utc": datetime.now(timezone.utc).isoformat(),
    "pdf": {**binding(PDF), "pages": 600, "claims_in_parent_build": 267},
    "render_preparation": binding(prep_path),
    "total_parent_selection_pages": 74,
    "root_assigned_pages_count": 41,
    "peer_assigned_pages_count": 33,
    "peer_freshly_viewed_pages": PAGES,
    "peer_reused_without_fresh_view_pages": [],
    "actual_image_view_groups_in_order": view_groups,
    "maximum_images_per_view_call": 2,
    "no_unviewed_page_certified": True,
    "images": rows,
    "visual_findings": {
        "defects_found": [],
        "all_f27_pages_freshly_viewed": [582, 583, 584, 585, 586],
        "all_f28_pages_freshly_viewed": [586, 587, 588, 589, 590],
        "f26_sample_pages_freshly_viewed": [578, 580, 581, 582],
        "historical_passages_checked": {
            "D.74.1": 459, "F.19.9": 544, "F.21_exponent_pairs": 556,
        },
        "F.7_scope_pages_checked": [491, 492, 493, 494, 495],
        "C.92_pages_reviewed_by": "Root; this peer record makes no fresh visual certification for unassigned pp.300-305.",
        "overall": "No clipping, overlap, missing glyph, malformed display, bad table/diagram alignment or footer collision observed on the assigned pages.",
    },
    "entire_final_build_logs_and_all_four_stage_outputs_read": True,
    "retained_log_copies": logs,
    "four_stage_commands": commands,
    "all_four_exit_codes_zero": True,
    "stage_1_3_4_stdout_byte_identical": False,
    "stage_3_4_stdout_byte_identical": True,
    "stage_output_notice_counts": stage_counts,
    "final_log_notice_counts": counts,
    "notice_interpretations": [
        "One inherited underfull hbox, badness 7133, source lines 62-63 in the opening table. Root owns final page 1 visual review.",
        "One inherited luaotfload-main lookup failure and OT1 fallback per LuaLaTeX run; fontenc/lmodern then load T1 Latin Modern and the output embeds the listed Type 1 fonts. This nonfatal loader notice is retained explicitly.",
        "Two informational microtype generic protrusion-setting notices in the final log, for T1/lmtt and OT1/lmss.",
        "One inherited BibTeX warning: C_Tukia1972 has a number but no volume.",
        "Stage 1 has one Label(s) may have changed rerun warning. It is absent from stages 3 and 4, whose stdout files are byte-identical. The final log reports the .out file unchanged, with no rerun or undefined-reference/citation warning.",
    ],
    "bibliography_record_count": record_count,
    "bibtex_used_entries": 77,
    "printed_bibliography_entries": 77,
    "build_source_bindings": [
        binding("deliverable/LM4_FINITE_GROUP_ACTIONS_paper.tex"),
        binding("deliverable/LM4_FINITE_GROUP_ACTIONS_references.bib"),
        binding("deliverable/LM4_FINITE_GROUP_ACTIONS_paper.bbl"),
    ],
    "frozen_source_and_review_bindings_unchanged": [binding(p) for p in frozen],
    "review_writer": binding(__file__),
    "no_frozen_source_or_final_pdf_edits": True,
}
target = OUT / "render_review_600.json"
assert not target.exists(), "The final review is already sealed; do not overwrite it casually."
target.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({
    "result": "PASS",
    "record": binding(target),
    "fresh_actual_views": len(PAGES),
    "view_calls": len(view_groups),
    "pdf_sha256": EXPECTED_PDF,
    "notice_counts": counts,
    "bib_records": record_count,
    "bib_used_entries": 77,
}, indent=2))
