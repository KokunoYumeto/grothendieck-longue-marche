#!/usr/bin/env python3
"""Bind the actual peer page views and full final build-log review."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "work/part_c"
PDF = ROOT / "deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf"
EXPECTED_PDF = "3dbd3037a1cb9199a564ac7ce6d1bf2fcc584297d0821d284b434834b600fcf9"
PAGES = [
    360, 400, 440, 454, 471, 480, 486, 487, 488, 489, 520, 539,
    550, 551, 552, 560, 567, 571, 573, 574, 575, 576, 577, 578,
    580, 584, 587,
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
assert PDF.stat().st_size == 3950584
prep_path = ROOT / "work/root/render_preparation_587_final.json"
prep = json.loads(prep_path.read_text())
assert prep["sha256"] == EXPECTED_PDF
assert prep["pages"] == 587
assert prep["peer_pages"] == PAGES
assert len(prep["images"]) == 62
assert len(prep["root_pages"]) == 35
rows = [r for r in prep["images"] if r["reviewer"] == "peer"]
assert [r["page"] for r in rows] == PAGES
for row in rows:
    actual = binding(row["path"])
    assert actual["sha256"] == row["sha256"]
    assert actual["bytes"] == row["bytes"]
    assert not row["byte_identical_to_prior_578_image"]

observations = {
    360: "D.39i-j and the finite quotient/table D.39d-f are legible; long exponents, matrices, table columns and the footer are clear.",
    400: "D.57f-i exact sequences and the adjoining four-group/dihedral comparison fit cleanly; no clipped arrows or subscripts.",
    440: "D.70h-k quotient maps, conjugator calculation and idempotent formulas are complete and legible.",
    454: "Historical D.74.1 visibly retains alpha(x)=x^{-1}, alpha(y)=f^{-1}y^{-1}f and f in F'; the new claim heading, D.74.2-3 and preceding D.73w-x are clear.",
    471: "D.78 statement, semidirect-product inverse coordinates and cohomology maps D.78.1-4 are clear, including the retained unresolved K=1 scope.",
    480: "E.23 table, matrix displays and E.24 refuted recovery statement render cleanly.",
    486: "F.7 Open scope heading and the first overview page are complete and legible.",
    487: "F.7 overview explicitly incorporates F.24-F.26 and retains the remaining marginal/intersection-image questions; source-audit paragraph and F.7.2-3 are clear.",
    488: "F.7 solvable comparison proof and F.7.4-6 are legible, including the long exact sequence and closure notation.",
    489: "F.7 finite A5-image proof and F.7.7 compact-coset formula fit; no collisions in intersections, hats or subscripts.",
    520: "F.13.4 and the F.14 opening displays render correctly, including puncture labels, paired coordinates and the two-point forgetting factorization.",
    539: "Historical F.19.9 and its actual gamma map are fully visible; F.19.10 commutative diagram and inverse coordinates F.19.11 have clear alignment.",
    550: "F.21.5-10 actual source coordinates and covering maps are legible; the long F.21.10 inverse-coordinate display stays within the page.",
    551: "Historical exponent pairs are visibly (0,3),(2,4),(3,2),(4,0), with h=3(1+j) mod 5; F.21.11-16 and derivative display are clear.",
    552: "F.21.17-23 section, double cover, rational map, three identities and filling comparison are complete and legible.",
    560: "F.22.23 exact diagram and the F.23 opening statement/diagrams render cleanly; all finite-image and retained-scope text is visible.",
    567: "F.23.31 counts table and F.24 opening render clearly; the corrected closing display after F.24.1 is present, with F.24.2-3 properly separated.",
    571: "F.25 statement, scalar-field definitions and F.25.1-6 are legible; all retained hypotheses are visible.",
    573: "F.26 opening, exact affine reduction, trace criterion and order-nine conclusion F.26.1-5 are fully visible and properly tagged.",
    574: "F.26.6-12 complement, commutator, trace pairing, coefficient factorization and affine homomorphism display cleanly.",
    575: "F.26.13-17 cocycle criterion, tensor/Frobenius isomorphism and explicit inverse render cleanly, including all indexed denominators.",
    576: "F.26.18-22 field operations, exhaustive count 7560, 64-row rank table and real block matrix render correctly.",
    577: "F.26.23-24 and the entire proof ending are visible. The repaired wording says F3-linear span of imaginary-part evaluation rows of actual source conjugates. Rank histories and independent-method paragraph are clear.",
    578: "References begin immediately after the completed F.26 proof; entries 1-8 and their verification notes have readable wrapping.",
    580: "Reference 20 includes the verified Epstein 6.3 pp.99-101 and Appendix A4 p.107 note used by C.91; surrounding entries and long source metadata wrap cleanly.",
    584: "References 52-59, including the added Morales audit entry, render without clipped text or broken glyphs.",
    587: "The final reference entry 77 and the concluding page footer render cleanly; the page ends normally without truncated content.",
}
assert sorted(observations) == PAGES
view_groups = [PAGES[i:i+2] for i in range(0, len(PAGES), 2)]
assert all(1 <= len(g) <= 2 for g in view_groups)
for row in rows:
    row.update({
        "actual_viewed": True,
        "fresh_view_for_this_final_pdf": True,
        "review_result": "PASS",
        "observation": observations[row["page"]],
    })

copies = {
    "LM4_FINITE_GROUP_ACTIONS_paper.log": "final_587_build.log",
    "LM4_FINITE_GROUP_ACTIONS_paper.blg": "final_587_build.blg",
    "build_commands.json": "final_587_build_commands.json",
    "build_artifact.json": "final_587_build_artifact.json",
    **{f"build_stage_{i}_stdout.txt": f"final_587_stage_{i}_stdout.txt"
       for i in range(1, 5)},
}
logs = []
for src, dest in copies.items():
    source = ROOT / "deliverable" / src
    target = OUT / dest
    shutil.copyfile(source, target)
    assert source.read_bytes() == target.read_bytes()
    row = binding(target)
    row["source_path"] = str(source.relative_to(ROOT))
    row["lines"] = len(target.read_bytes().splitlines())
    row["read_in_full"] = True
    logs.append(row)

log = (OUT / "final_587_build.log").read_text()
blg = (OUT / "final_587_build.blg").read_text()
stages = [(OUT / f"final_587_stage_{i}_stdout.txt").read_text()
          for i in range(1, 5)]
assert stages[0] == stages[2] == stages[3]
commands = json.loads((OUT / "final_587_build_commands.json").read_text())
assert len(commands) == 4 and all(c["exit_code"] == 0 for c in commands)
artifact = json.loads((OUT / "final_587_build_artifact.json").read_text())
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
assert "has not \nchanged." in log
assert "You've used 77 entries" in blg
bib = (ROOT / "deliverable/LM4_FINITE_GROUP_ACTIONS_references.bib").read_text()
records = re.findall(r"(?m)^\s*@(\w+)\s*\{", bib)
record_count = sum(t.lower() not in {"comment", "string", "preamble"}
                   for t in records)
assert record_count == 85
assert len(re.findall(r"\\bibitem\{", (ROOT / "deliverable/LM4_FINITE_GROUP_ACTIONS_paper.bbl").read_text())) == 77

frozen = {
    "work/part_c/c91.tex": "0b5db75c25411d069d4316995b410faab63b5c624bed7f4044a963e27d1952ff",
    "work/part_c/c91_result.json": "e04468571d33ee0e597c3a14ecacd4f4552733d9440e49c977ac2cfcd12b582d",
    "work/part_c/c91_report.txt": "22bcb412d6e1e6cfadda05ee0fcc1c42e4ae8d818b8f4af3f838b33b5d39a485",
    "work/part_c/c91_provenance.json": "b5c94078c4b95d0c852736637f93085fa1b5b4eb1ded0de78da80693f2384197",
    "work/part_a/f_trace_obstruction_and_f9_images.tex": "1db6b7ce7170a2da642989abe86198811e9e4dbb42288d67263dd823932e1449",
    "work/part_c/review_f26.txt": "1e17eb9561b0b4a4316022279bbb3a419f6d179fcb4c62fab72c58243b09bd56",
    "work/part_c/review_f26.json": "a6f84ee112165ba77a5ee6faec7da00c89df6544e517a5963ccdf3a4a89fcffa",
}
for path, digest in frozen.items():
    assert binding(path)["sha256"] == digest
assert binding(PDF)["sha256"] == EXPECTED_PDF

result = {
    "reviewer": "/root/c89_review_and_general_c",
    "review_scope": "Independent actual visual review of the 27 assigned final-587 pages and complete final build-log/stage review.",
    "status": "PASS",
    "sealed_at_utc": datetime.now(timezone.utc).isoformat(),
    "pdf": {**binding(PDF), "pages": 587, "claims_in_parent_build": 264},
    "render_preparation": binding(prep_path),
    "total_parent_selection_pages": 62,
    "root_assigned_pages_count": 35,
    "peer_assigned_pages_count": 27,
    "peer_freshly_viewed_pages": PAGES,
    "peer_reused_without_fresh_view_pages": [],
    "actual_image_view_groups_in_order": view_groups,
    "maximum_images_per_view_call": 2,
    "no_unviewed_page_certified": True,
    "images": rows,
    "visual_findings": {
        "defects_found": [],
        "all_f26_pages_freshly_viewed": [573, 574, 575, 576, 577],
        "historical_passages_checked": {
            "D.74.1": 454, "F.19.9": 539, "F.21_exponent_pairs": 551,
        },
        "F.7_scope_pages_checked": [486, 487, 488, 489],
        "C.91_pages_reviewed_by": "Root; this peer record makes no fresh visual certification for unassigned pp.296-300.",
        "overall": "No clipping, overlap, missing glyph, malformed display, bad table/diagram alignment or footer collision observed on the assigned pages.",
    },
    "entire_final_build_logs_and_all_four_stage_outputs_read": True,
    "retained_log_copies": logs,
    "four_stage_commands": commands,
    "all_four_exit_codes_zero": True,
    "stage_1_3_4_stdout_byte_identical": True,
    "final_log_notice_counts": counts,
    "notice_interpretations": [
        "One inherited underfull hbox, badness 7133, source lines 62-63 in the opening table. Root owns final page 1 visual review.",
        "One inherited luaotfload-main lookup failure and OT1 fallback per LuaLaTeX run; fontenc/lmodern then load T1 Latin Modern and the output embeds the listed Type 1 fonts. This is a nonfatal loader notice, not an omitted error.",
        "Two informational microtype generic protrusion-setting notices, for T1/lmtt and OT1/lmss.",
        "One inherited BibTeX warning: C_Tukia1972 has a number but no volume.",
        "The final .out file is reported unchanged; no rerun warning or undefined citation/reference remains.",
    ],
    "bibliography_record_count": 85,
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
target = OUT / "render_review_587.json"
assert not target.exists(), "The final review is already sealed; do not overwrite it casually."
target.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({
    "result": "PASS",
    "record": binding(target),
    "fresh_actual_views": len(PAGES),
    "pdf_sha256": EXPECTED_PDF,
    "notice_counts": counts,
    "bib_records": record_count,
    "bib_used_entries": 77,
}, indent=2))
