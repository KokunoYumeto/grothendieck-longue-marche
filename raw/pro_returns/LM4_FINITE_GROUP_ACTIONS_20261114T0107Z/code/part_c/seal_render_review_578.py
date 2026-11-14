"""Seal the independently completed final-578 visual review and log checks.

The visual observations below are the reviewer's manual observations, not
conclusions inferred from rendering or from the hash checks in this script.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PART = ROOT / "work/part_c"
PDF = ROOT / "deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf"
PDF_SHA = "7b32432e84921f17f1a8635e03621a30370b4f5254a1ea5656f0b8a0b1aa65ee"
PREP = ROOT / "work/root/render_preparation_578_final.json"
PRIOR = PART / "render_review_567.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def binding(path: Path) -> dict:
    return {"path": relative(path), "sha256": sha(path), "bytes": path.stat().st_size}


assert sha(PDF) == PDF_SHA
assert PDF.stat().st_size == 3895528
pdfinfo = subprocess.run(["pdfinfo", str(PDF)], check=True, capture_output=True, text=True).stdout
assert re.search(r"^Pages:\s+578\s*$", pdfinfo, re.M)
prep = json.loads(PREP.read_text())
prior = json.loads(PRIOR.read_text())
assert prep["sha256"] == PDF_SHA
assert sha(PRIOR) == "94d77a702a58d63b754e6a9fe1128262e3290deb5f7d6af040756a4fdf997f48"
prior_rows = {row["page"]: row for row in prior["pages"]}
prepared_rows = {row["page"]: row for row in prep["images"]}

fresh_batches = [
    [290, 291], [292, 293], [294, 295], [340, 350], [373, 403],
    [433, 449], [460, 466], [467, 468], [469, 470], [562, 563],
    [564, 565], [566, 567], [568], [351],
]
fresh = sorted(page for batch in fresh_batches for page in batch)
assert len(fresh) == len(set(fresh)) == 26
assert fresh == sorted(prep["peer_fresh_pages"] + [351])
reuse = list(range(277, 290))
requested = prep["peer_assigned_pages"]
covered = sorted(requested + [351])
assert len(covered) == len(set(covered)) == 39
assert set(covered) == set(fresh + reuse)

findings = {
    290: "C.88.14 and the transition to C.89 are legible. C.89.1-3, the full statement, and the opening proof fit the text block; no equation/tag collision or clipping.",
    291: "C.89.4-8, including the two map-and-inverse rows and the conjugated face extension, are readable and properly separated from their tags. The final paragraph continues normally onto page 292.",
    292: "C.89.9-10 and the full parameter-continuity argument are readable. The multi-line estimate is aligned and its tag does not collide with a formula.",
    293: "C.89.11-12 close the section proof cleanly. C.90 begins with readable heading, statement, equations C.90.1-2, provenance, and the opening proof; no overlap.",
    294: "C.90.3-7 display the normalized contraction, descent, lifted family, endpoint identities, and boundary extension clearly; the cases display and right-side tags fit.",
    295: "C.90.8-9 and the final scope paragraph fit. The transition to Part D and D.1 is clear; no clipped text or formula/tag collision.",
    340: "Historical D.33h-i, the cusp-normalizer sequence, and the surrounding pro-p argument are readable with no displayed-equation overflow.",
    350: "Historical D.37l-n, including the partition table and deck-map formulas, fit. This page contains the lead-in to D.37o, whose displayed formula is actually on page 351.",
    351: "Extra page actually viewed to cover D.37o: its two-line formula has clear separation from the tag and surrounding prose. The ensuing D.38a-c formulas and enumeration table are also legible and unclipped.",
    373: "Historical D.47b-f, including the paired conjugator equations and the symmetry constraint, are readable and lie within the text block.",
    403: "Historical D.60a-d and the case table fit. Quotient maps, the section formula, and the final embedding display do not collide with their tags.",
    433: "Historical D.69z and the transition to D.70, including D.70a at the foot of the text block, are readable; no clipping or overlap with the footer.",
    449: "Historical D.73w-x and D.74.1-3 fit. The two-row D.74.1 display is clear and its tag is separate from the formula.",
    460: "Historical D.76.3-9, including the incidence map, displayed inverse coordinates, and the augmentation-module map, are readable without tag collisions.",
    466: "D.78 begins cleanly. Equations D.78.1-4 and all statement formulas are readable, including the semidirect coordinates and coefficient-inclusion map.",
    467: "D.78.5-9 and their intervening pairing and filtration formulas fit. The two-case expression D.78.9 at the foot of the page stays above the footer.",
    468: "D.78.10-17, including the pairing, coefficient comparison, two-line isomorphism, and finite-orbit formula, remain readable with distinct tags.",
    469: "D.78.18-20 and the full pro-odd-kernel argument fit. The averaging formula and its sum have adequate clearance from the tag and following paragraph.",
    470: "D.78.21 and its exact scope paragraph close cleanly. The transition to Part E, E(a), and E.1 is legible and unclipped.",
    562: "F.23.31 and the F.24 opening are readable. The repaired F.24.1 display is properly closed, the following prose is in text mode, and F.24.2-3 fit without collisions.",
    563: "F.24.4-9 are readable. The repaired F.24.4 display is properly closed; the source-word, character, and coefficient-map prose following it renders normally.",
    564: "F.24.10-14, the rank-seven chart table, the retained pivot rows, and the explicit seventh-pivot identity fit and remain readable.",
    565: "The remainder of F.24's chart argument, restriction/sign comparison, and affine fixed-point proof are readable. F.24.15-16 have no tag collision.",
    566: "The F.24 scope paragraph closes cleanly. F.25.1-6 and the new theorem statement, provenance, normal-generation comparison, and translation-conjugation formula fit.",
    567: "F.25.7-11, including the affine normalization, inverse coordinates, annihilator formula, coefficient cocycle, and image inclusions, are readable and their tags remain separated.",
    568: "F.25's prime-field conclusion and final remaining-scope paragraph are readable and end with a correctly placed proof square. The intentional white space at the end of Part F is clear.",
}

page_records = []
for number in covered:
    if number == 351:
        path = PART / "rendered/review_578_extra/page351.png"
        expected_hash = "2a50ecc257b921eb294d073a2d1ec51438b8d97c2c814dc4ac45e2f46b410fbe"
        assert sha(path) == expected_hash
    else:
        prepared = prepared_rows[number]
        path = Path(prepared["path"])
        assert sha(path) == prepared["sha256"]
        assert path.stat().st_size == prepared["bytes"]
    row = {
        "page": number,
        "final_image": str(path),
        "final_sha256": sha(path),
        "final_bytes": path.stat().st_size,
        "fresh_final_image_actually_opened_and_emitted": number in fresh,
        "finding": findings.get(number),
    }
    if number in reuse:
        old = prior_rows[number]
        oldpath = Path(old["final_image"])
        assert number in prior["pages_covered_by_actual_image_viewing"]
        assert sha(oldpath) == old["final_sha256"]
        assert oldpath.read_bytes() == path.read_bytes()
        row.update({
            "prior_actually_reviewed_image": str(oldpath),
            "prior_image_sha256": sha(oldpath),
            "prior_review": relative(PRIOR),
            "byte_identical": True,
            "review_basis": "Independent full byte comparison with the final-567 image covered by the sealed prior actual-view review; no fresh viewing is claimed.",
            "finding": old["finding"],
        })
    else:
        row["review_basis"] = "This exact final-PDF PNG was opened with view_image and emitted, then visually inspected by the reviewer."
    page_records.append(row)

log_sources = [
    (ROOT / "deliverable/LM4_FINITE_GROUP_ACTIONS_paper.log", PART / "final_578_build.log"),
    (ROOT / "deliverable/LM4_FINITE_GROUP_ACTIONS_paper.blg", PART / "final_578_build.blg"),
    (ROOT / "work/root/build_262_final_stdout.txt", PART / "final_578_four_stage_transcript.txt"),
] + [
    (ROOT / f"deliverable/build_stage_{i}_stdout.txt", PART / f"final_578_stage_{i}_stdout.txt")
    for i in range(1, 5)
]
log_bindings = []
for source, target in log_sources:
    shutil.copyfile(source, target)
    assert source.read_bytes() == target.read_bytes()
    log_bindings.append({"original": binding(source), "sealed_copy": binding(target), "entire_contents_actually_read": True})

log = (PART / "final_578_build.log").read_text()
bib = (PART / "final_578_build.blg").read_text()
counts = {
    "overfull_hbox": log.count("Overfull \\hbox"),
    "overfull_vbox": log.count("Overfull \\vbox"),
    "underfull_hbox": log.count("Underfull \\hbox"),
    "underfull_vbox": log.count("Underfull \\vbox"),
    "missing_character": log.count("Missing character:"),
    "undefined_diagnostic": len(re.findall("undefined", log, re.I)),
    "latex_warning": log.count("LaTeX Warning:"),
    "latex_font_warning": log.count("LaTeX Font Warning:"),
    "package_warning": len(re.findall(r"Package .* Warning", log)),
    "fatal": len(re.findall(r"^!|Fatal error|Emergency stop", log, re.M)),
    "nonfatal_luaotfload_fallback": log.count("Error in luaotfload: reverting to OT1"),
    "generic_microtype_protrusion_information": log.count("Loading generic protrusion settings"),
    "bibtex_warning": len(re.findall(r"^Warning--", bib, re.M)),
}
assert counts == {
    "overfull_hbox": 0, "overfull_vbox": 0, "underfull_hbox": 1, "underfull_vbox": 0,
    "missing_character": 0, "undefined_diagnostic": 0, "latex_warning": 0,
    "latex_font_warning": 0, "package_warning": 0, "fatal": 0,
    "nonfatal_luaotfload_fallback": 1, "generic_microtype_protrusion_information": 2,
    "bibtex_warning": 1,
}
stages = [json.loads(line) for line in (PART / "final_578_four_stage_transcript.txt").read_text().splitlines()]
assert len(stages) == 4 and [row["exit_code"] for row in stages] == [0, 0, 0, 0]
assert "Label(s) may have changed" in (PART / "final_578_stage_1_stdout.txt").read_text()
for i in (3, 4):
    assert "Label(s) may have changed" not in (PART / f"final_578_stage_{i}_stdout.txt").read_text()

source_expectations = {
    "work/part_b/c89.tex": "fdb210d491cb66ebb4ab9f1fef1b41427d4b7d0e3b2a77bea197d261d6191299",
    "work/part_c/c90.tex": "f04a03b644916a1451602a186af35361b6a21fcd3b710c58c8dd12c3a1e1287f",
    "work/part_a/f_rank_one_marginal_obstruction.tex": "44e84bb754b46e288df19ec3d931ba16687ea2208422a096ea43d9a2db3a9d75",
    "work/part_a/f_affine_scalar_field_images.tex": "d94af591f2cf567ae5f31286a7b0c694ef94bfddd12927a0f24cdbdc90e5a0ee",
}
for name, expected in source_expectations.items():
    assert sha(ROOT / name) == expected

record = {
    "reviewer": "/root/c89_review_and_general_c",
    "phase": "Independent visual review of the frozen 262-claim, 578-page build",
    "reviewed_at_utc": datetime.now(timezone.utc).isoformat(),
    "pdf": relative(PDF), "pdf_sha256": PDF_SHA, "pdf_pages": 578, "pdf_bytes": 3895528,
    "pdf_hash_verified_during_and_after_review": True,
    "registered_claims": 262,
    "render_preparation": binding(PREP),
    "prior_actual_view_review": binding(PRIOR),
    "original_pages_requested": requested,
    "additional_requested_page": 351,
    "assignment_correction": "D.37o is displayed on page 351. Page 350 contains D.37l-n. The parent approved adding page 351, which was rendered directly from the same frozen PDF and actually viewed.",
    "pages_covered_by_actual_image_viewing": covered,
    "fresh_final_pages_actually_viewed": fresh,
    "fresh_final_view_batches": fresh_batches,
    "byte_identical_pages_carried_from_prior_actual_viewing": reuse,
    "total_reviewed_page_count": 39,
    "fresh_final_view_count": 26,
    "byte_identical_carry_forward_count": 13,
    "combined_root_and_peer_selection_counts": {
        "selected_pages": 104, "root_assigned": 65, "peer_assigned": 39,
        "fresh_images": 65, "exact_byte_reuse_images": 39,
        "scope": "Allocation totals only; this peer attests to its 39 pages. Root's 65-page visual review is recorded separately.",
    },
    "extra_page_rendering": {
        "page": 351, "dpi": 100,
        "command": ["pdftoppm", "-f", "351", "-l", "351", "-r", "100", "-singlefile", "-png", relative(PDF), "work/part_c/rendered/review_578_extra/page351"],
    },
    "verdict": "PASS",
    "remaining_visual_issues": [],
    "overall_visual_observations": [
        "All 26 fresh final PNGs were actually opened and emitted in batches of at most two images.",
        "Every reused page 277-289 was independently compared byte for byte with its image in the sealed 567-page actual-view record.",
        "No clipped text, equation/tag collision, table overflow, unreadable glyph, black box, or footer overlap was observed on the covered pages.",
        "The repaired F.24.1 and F.24.4 displays render normally and the following prose is outside display math.",
        "C.89, C.90, D.78, F.24, and F.25 were each viewed through their entire final-PDF typeset span.",
        "Page 568 has deliberate end-of-part white space after the final scope paragraph; the text and proof square are correctly placed.",
    ],
    "proof_typesetting_coverage": {
        "C89": [290, 291, 292, 293], "C90": [293, 294, 295],
        "D78": [466, 467, 468, 469, 470],
        "F24": [562, 563, 564, 565, 566], "F25": [566, 567, 568],
        "historical_D37o": [351], "historical_D74_1": [449],
    },
    "source_bindings": [binding(ROOT / name) for name in source_expectations],
    "compiled_tex": binding(ROOT / "deliverable/LM4_FINITE_GROUP_ACTIONS_paper.tex"),
    "independent_math_reviews": [binding(PART / name) for name in ["review_c89.json", "review_f24.json", "review_f25.json"]],
    "build_review": {
        "all_1901_final_lualatex_log_lines_actually_read": True,
        "all_48_bibtex_log_lines_actually_read": True,
        "complete_four_command_transcript_actually_read": True,
        "all_four_stage_stdout_files_actually_read": True,
        "stage_exit_codes": [0, 0, 0, 0],
        "files": log_bindings,
        "diagnostic_counts": counts,
        "nonfatal_notices": [
            {"kind": "luaotfload fallback", "count_in_final_log": 1, "inherited": True, "detail": "luaotfload-main is absent; the runtime reports reverting to OT1, then loads T1 Latin Modern and embeds the Type 1 fonts. This is a nonfatal runtime notice, not an absent diagnostic."},
            {"kind": "underfull hbox", "count_in_final_log": 1, "inherited": True, "detail": "Badness 7133 in source paragraph lines 62-63, the page-one notation-table text 'Two-group problem: 312,'. Page one is in the root visual assignment."},
            {"kind": "BibTeX number without volume", "count_in_bibtex_log": 1, "inherited": True, "detail": "C_Tukia1972 has a number but no volume. The final BibTeX log is byte-identical to the prior sealed final-567 BibTeX log; it reports 77 entries."},
            {"kind": "microtype information", "count_in_final_log": 2, "inherited": True, "detail": "Generic protrusion settings for lmtt (T1) and lmss (OT1); informational notices, not package warnings."},
        ],
        "resolved_intermediate_notice": "Stage 1 requests a rerun for changed labels. This notice is absent in stage 3, stage 4, and the final LuaLaTeX log; the final rerunfilecheck states that the .out file has not changed.",
        "bibliography_entries": 77,
        "final_bibtex_log_byte_identical_to_prior_sealed_log": sha(PART / "final_578_build.blg") == prior["build_review"]["final_bibtex_log_sha256"],
    },
    "source_changes_made_by_reviewer": False,
    "pdf_changes_made_by_reviewer": False,
    "pages": page_records,
}
assert len(log.splitlines()) == 1901
assert len(bib.splitlines()) == 48
assert sha(PDF) == PDF_SHA
target = PART / "render_review_578.json"
target.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"record": relative(target), "sha256": sha(target), "bytes": target.stat().st_size, "verdict": record["verdict"], "pages": 39, "fresh": 26, "reused": 13, "pdf_sha256": sha(PDF)}, indent=2))
