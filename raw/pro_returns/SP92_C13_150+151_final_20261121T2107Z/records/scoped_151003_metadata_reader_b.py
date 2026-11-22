#!/usr/bin/env python3
"""Align current 151_scan003 metadata with its recorded blind adjudication.

No image is opened, no manuscript reading is made, and no TeX is compiled.
The page, raw witness fields, audit originals, historical review fields and
sealed TSVs are protected. Same-locus overlaps are reported, not deduplicated.
"""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path


W = Path("/workspace/scratch/d7279cb02214/SP92_C13_150+151_work")
RECORD = W / "records/151_scan003.json"
LOG = W / "records/scoped_151003_metadata_reader_b.json"
raw_before = RECORD.read_bytes()
before = json.loads(raw_before)
current = deepcopy(before)
page = (W / "pages/151_scan003.tex").read_text()
root_notes = json.loads((W / "second/151_scan003_root_crop_notes.json").read_text())
adjudications = json.loads((W / "second/151_scan003_adjudications.json").read_text())

protected_files = [
    "pages/151_scan003.tex",
    "records/151_scan003.tex",
    "second/151_scan003_boxes.tsv",
    "second/151_scan003_first.tsv",
    "second/151_scan003_second.tsv",
    "second/151_scan003_root_crop_notes.json",
    "second/151_scan003_adjudications.json",
]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


protected_hashes = {rel: digest(W / rel) for rel in protected_files}
edits = []


def at_path(obj, path):
    for part in path:
        obj = obj[part]
    return obj


def edit(path, value, reason, authority):
    old = at_path(current, path)
    if old == value:
        return
    parent = at_path(current, path[:-1])
    parent[path[-1]] = value
    edits.append({
        "path": path,
        "before": old,
        "after": value,
        "reason": reason,
        "authority": authority,
    })


def row_index(kind, row_id, id_key="id"):
    return next(i for i, row in enumerate(current[kind]) if row[id_key] == row_id)


def change(row_id, field, value, reason, authority):
    edit(["changes", row_index("changes", row_id), field],
         value, reason, authority)


def diff(row_id, reason, authority):
    edit(["diff_coverage", row_index("diff_coverage", row_id, "diff_id"), "reason"],
         reason, "Current diff summary follows the audited reading.", authority)


# Revision descriptions; current encoded readings were already updated by root.
edit(["deletion_insertion_review", 4, "place"],
     "Cancelled p-index equality",
     "Avoid certifying the first cancelled index in the descriptive title.",
     ["B08"])
edit(["deletion_insertion_review", 7, "state"],
     "Entire small p-index/delta-index draft is cancelled; the p index remains 1|12 and the delta index remains 1|0.",
     "Remove stale definite delta0 wording; both indices remain uncertain.",
     ["B13"])
edit(["deletion_insertion_review", 10, "attachment"],
     "Separate from the upper live chain and the nearby boxed sigma identity. The first short bracket lies under p0 only; the first three annotations are square-ended brackets, and only the last is a cusped brace.",
     "Record the audited first-bracket attachment and the retained final-brace exception.",
     ["B16"])
edit(["deletion_insertion_review", 11, "attachment"],
     "The authorial ?? sits above the not-equal sign; the p22-first index uncertainty remains unresolved. Both annotation lines are square-ended brackets, and the first lies inside the parentheses.",
     "Keep annotation geometry and parentheses attachment consistent with the audited formula.",
     ["B17"])
edit(["deletion_insertion_review", 15, "attachment"],
     "Between p12 and rho2 inside the inner square-ended lower bracket; the following rho2 and final sigma2 are live.",
     "Replace the obsolete inner-underbrace description.",
     ["B22"])

# Inventory: keep the inventory size and baseline count unchanged.
inventory_updates = [
    (12, "first_words_or_objects", "p index tentatively12 = p23",
     "The cancelled first index is no longer certified.", ["B08"]),
    (17, "first_words_or_objects", "raised a|leftward-arrow mark",
     "Include both recorded alternatives for the raised terminal.", ["B11"]),
    (21, "first_words_or_objects", "p_{1|12} delta_{1|0}",
     "Retain uncertainty in both cancelled indices.", ["B13"]),
    (23, "element", "Main-chain five square-ended underannotations",
     "All five main-chain grouping lines have audited bracket geometry.", ["B14"]),
    (27, "element", "Cancelled i.e. chain with three brackets and one brace",
     "The last grouping alone retains its central cusp.", ["B16"]),
    (28, "element", "Cancelled inequality and square-ended underannotations",
     "Both inequality grouping lines are brackets.", ["B17"]),
    (31, "element", "Value-system square-ended bracket annotations",
     "Neither value-box annotation is a cusped brace.", ["B18"]),
    (36, "element", "Lower live diagram in a frame with two gaps",
     "A complete rectangular frame is not the audited geometry.", ["B20"]),
    (38, "element", "Final rho/sigma identity in a gapped frame with an upward left arrowhead",
     "Identify the recorded frame gaps and upward left terminal.", ["B21"]),
    (39, "first_words_or_objects",
     "p0 p12 (relation =|ne) p0 p12 [cancelled sigma] rho2 sigma2",
     "The bottom relation remains equality/inequality uncertain.", ["B22"]),
    (41, "element", "Bottom formula square-ended bracket annotations",
     "All three bottom annotation lines are square-ended brackets.", ["B22"]),
]
for i, field, value, reason, authority in inventory_updates:
    edit(["inventory", i, field], value, reason, authority)

# Current prose explanations. Recorded coordinate results are not recomputed.
notes = current["notes"]
replacements = [
    ("The main equality's baseline delta3 and delta2, and their lower rho annotations,",
     "The main equality's baseline delta3, delta1 and delta2, and their lower rho annotations,"),
    ("The final formula was read with both nested brackets and all their labels:",
     "The final formula was read with three square-ended annotation brackets and all their labels:"),
    ("The final live sigma2 is present. The boxed identity immediately above",
     "The final live sigma2 is present, and the relation remains equality/inequality uncertain. The boxed identity immediately above"),
    ("At the last formula, the inner underbrace p12 rho^2=p31 is valid.",
     "At the last formula, the inner lower-bracket label p12 rho^2=p31 is valid."),
    ("The outer overbrace visibly labels p12 rho^2 sigma2 as p12,",
     "The outer upper bracket visibly labels p12 rho^2 sigma2 as p12,"),
    ("Thus that brace label fails in this model;",
     "Thus that bracket label fails in this model;"),
    ("Composing with p0 makes the full displayed equality true,",
     "Composing with p0 makes the equality interpretation of the displayed relation true,"),
]
for old, new in replacements:
    assert notes.count(old) == 1, (old, notes.count(old))
    notes = notes.replace(old, new)
edit(["notes"], notes,
     "Align current descriptions of the main terms, bottom relation and bracket geometry; leave the recorded coordinate computations and their results unchanged.",
     ["B14", "B22"])

line_convention = current["line_count_convention"]
assert line_convention.count("brace-label bands") == 2
line_convention = line_convention.replace(
    "diagram label/object/relation bands, brace-label bands,",
    "diagram label/object/relation bands, annotation-label bands,")
line_convention = line_convention.replace(
    "three-value box plus two brace-label bands",
    "three-value box plus two bracket-label bands")
edit(["line_count_convention"], line_convention,
     "Use the audited annotation terminology without altering any baseline count or its breakdown.",
     ["B18"])
edit(["notation", 5, "reading"],
     "Main formula terms and annotation labels remain in their written positions; square-ended brackets are distinguished from the one retained cusped brace.",
     "Make the current notation description explicit about the audited graphic distinction.",
     ["B14", "B16", "B17", "B18", "B22"])
edit(["notation", 5, "evidence"],
     "All five main-chain annotations, the first three in the cancelled i.e. chain, both cancelled-inequality annotations, both value-box annotations and all three bottom annotations have square ends and no central cusp. Only the last annotation in the cancelled i.e. chain retains a central downward cusp.",
     "Record the precise audited occurrence list and its exception.",
     ["B14", "B16", "B17", "B18", "B22"])

# Change-row current descriptions; raw C/H fields and count flags are protected.
change("C26", "evidence",
       "The small mark stands above and to the right of the final delta2. Its loop/return and angled left stroke admit a or a leftward arrow; the identity remains uncertain at that raised position. No letters are supplied from the formula meaning.",
       "Remove the earlier a-only description from the current evidence.",
       ["B11"])
change("C42", "evidence",
       "The complete i.e. chain is cancelled: delta0 p0, p12 delta1 with sigma underneath, p12 rho delta1 with id underneath, and p12 rho2 delta1. The first short bracket starts to the right of the delta body and lies under p0 only. The first three grouping lines are flat with rising ends; only the final grouping has a central downward cusp and remains a brace. H mentions this chain editorially but does not transcribe it.",
       "State the first-three-brackets/final-brace exception and first attachment explicitly.",
       ["B16"])
change("C47", "evidence",
       "The first annotation lies above rho delta1, with delta3 above its flat square-ended bracket. It is distinct from the square-ended lower annotation on the second row. Neither grouping line has a central cusp.",
       "Remove the obsolete lower-underbrace description.",
       ["B18"])
change("C50", "evidence",
       "The lower margin relation p12 sigma3=sigma p12 ends at its last numeral inside the surrounding box. The recorded punctuation check found no detached comma after the formula or beside the right box edge. The separate sigma3 delta1=delta1 relation is covered by C49.",
       "Remove copied evidence about delta indices that belong to the neighboring upper box.",
       ["B19", "existing C50 punctuation check"])
change("C52", "evidence",
       "Inside the lower diagram frame, which has an upper-left and a lower-right gap, E0,E1,E2 lie in one row. Straight left-facing arrows are labelled p0 and p12; lower curved right-facing arrows are labelled delta0 and delta1. All four tips and labels agree in the recorded audit. H omits this second diagram. This row concerns the objects/maps; C63 separately records the frame geometry.",
       "Describe the audited frame and distinguish this row's map/object scope from C63.",
       ["B20"])
c60_final = current["changes"][row_index("changes", "C60")]["final"]
assert c60_final in page
change("C61", "final", c60_final,
       "Replace the obsolete brace-ending fragment with the current complete last-term encoding; the row remains a terminal-punctuation correction.",
       ["B22", "unchanged current page"])
change("C61", "evidence",
       "No independent full stop follows the final sigma2 or the upper p12 label. The lower annotations meet the trimmed sheet edge. This row records only terminal punctuation; the outer bracket and its label are covered by C60.",
       "Keep the punctuation-only scope explicit after replacing the obsolete encoded fragment.",
       ["B22", "existing C61 punctuation check"])

diff("D0895",
     "H reorders sigma rows and omits the raised a|leftward-arrow terminal in the third delta-rho row; punctuation is separately collated.",
     ["B11"])
diff("D0901",
     "H aligns its relocated sigma identity against the omitted cancelled draft, whose p index remains 1|12 and delta index remains 1|0.",
     ["B13"])
diff("D0913",
     "Long alignment crosses cancelled trials and the value box: full chains, question placement, index doubts, annotation position/geometry and the crossed rho subscript are collated by actual place. The first three cancelled i.e. groupings are brackets and its last is a cusped brace; both inequality and both value-box annotations are square-ended brackets.",
     ["B16", "B17", "B18"])
diff("D0916",
     "Aligned/cases display wrapper only. The two value-box annotation lines are represented as square-ended brackets in the current page; their upper/lower placement and geometry are recorded separately in C47 and C65.",
     ["B18"])
edit(["status"], "root-finalized; blind crop audit complete",
     "The first-pass waiting status is obsolete after the recorded root finalization and completed blind adjudication.",
     ["root_reviewed", "audited", "audit_differing_boxes=20", "audit_changed_boxes=10"])

# Immutable provenance and originals.
protected_record_fields = [
    "second_boxes", "audit_changes", "half_review", "crop_manifest",
    "root_review", "root_reviewed", "validation", "line_count",
    "decisions", "check_events",
]
for key in protected_record_fields:
    assert current[key] == before[key], key
assert [row["id"] for row in current["changes"]] == [
    row["id"] for row in before["changes"]]
assert len(current["changes"]) == len(before["changes"]) == 66
assert len(current["diff_coverage"]) == len(before["diff_coverage"]) == 76
assert len(current["inventory"]) == len(before["inventory"]) == 43
assert len(current["deletion_insertion_review"]) == 16


def collect_protected_leaves(obj, path=()):
    found = {}
    if isinstance(obj, dict):
        for key, value in obj.items():
            child_path = path + (key,)
            if key in {"C", "H", "first", "second", "witness_errors"}:
                found[child_path] = deepcopy(value)
            else:
                found.update(collect_protected_leaves(value, child_path))
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            found.update(collect_protected_leaves(value, path + (i,)))
    return found


assert collect_protected_leaves(current) == collect_protected_leaves(before)
for old, new in zip(before["changes"], current["changes"]):
    for key in set(old) | set(new):
        if key not in {"final", "evidence"}:
            assert old.get(key) == new.get(key), (old["id"], key)
change_ids = {row["id"] for row in current["changes"]}
assert all(cid in change_ids for row in current["diff_coverage"]
           for cid in row["change_ids"])
assert sum(bool(note.get("viewed")) for note in root_notes.values()) == 20
assert sum(bool(note.get("changed")) for note in root_notes.values()) == 10
assert len(adjudications["adjudications"]) == 20
assert current["audit_differing_boxes"] == 20
assert current["audit_changed_boxes"] == 10
assert current["audit_boxes"] == 23
assert "underbrace" not in current["deletion_insertion_review"][15]["attachment"]
assert "lower underbrace" not in current["changes"][row_index("changes", "C47")]["evidence"]
assert "both delta subscripts" not in current["changes"][row_index("changes", "C50")]["evidence"]
assert current["changes"][row_index("changes", "C61")]["final"] in page

overlap_flags = [
    {
        "rows": ["C39", "C40"],
        "locus": "Main-chain final delta2 annotation",
        "assessment": "Identical final fragments; C39 addresses placement/geometry, while C40 addresses terminal punctuation.",
    },
    {
        "rows": ["C56", "C64"],
        "locus": "Final identity and frame",
        "assessment": "Identical final fragments; C56 addresses following punctuation, while C64 addresses the left arrowhead and frame gaps.",
    },
    {
        "rows": ["C52", "C63"],
        "locus": "Lower diagram",
        "assessment": "Both describe the omitted H diagram: C52 records objects/maps, C63 records frame gaps. This is the clearest potential H-omission overlap if counting the entire omitted diagram as one locus.",
    },
    {
        "rows": ["C48", "C65"],
        "locus": "Second-row value-box product",
        "assessment": "C65 includes C48's cancelled-subscript fragment, but explicitly limits its own correction to bracket geometry.",
    },
    {
        "rows": ["C57", "C66"],
        "locus": "Bottom-left annotation",
        "assessment": "C57 concerns the uncertain 2/1 index; C66 concerns the square-ended grouping line.",
    },
    {
        "rows": ["C60", "C61"],
        "locus": "Bottom outer annotation and formula ending",
        "assessment": "After the encoding-only final-fragment repair, the final strings coincide. C60 addresses outer annotation/label placement; C61 explicitly addresses terminal punctuation only.",
    },
    {
        "rows": ["C34", "C35"],
        "locus": "First main-chain delta3 underannotation",
        "assessment": "C34's complete fragment includes C35's cancelled raised glyph. C34 addresses main-term/annotation placement and geometry; C35 addresses the separately cancelled glyph omitted from H.",
    },
    {
        "rows": ["C58", "C59", "C60"],
        "locus": "Bottom right-hand product",
        "assessment": "C60's complete outer-annotation fragment includes the cancelled factor C58 and live factor C59. Its evidence assigns those factors to their separate rows and limits C60 to the outer grouping/label.",
    },
]

# Avoid losing concurrent root edits.
assert RECORD.read_bytes() == raw_before, "Record changed while this scoped repair was being prepared."
encoded = (json.dumps(current, ensure_ascii=False, indent=2) + "\n").encode()
assert json.loads(encoded) == current
RECORD.write_bytes(encoded)
assert json.loads(RECORD.read_bytes()) == current
for rel, expected in protected_hashes.items():
    assert digest(W / rel) == expected, rel

log = {
    "task": "Current-metadata consistency cleanup for audited 151_scan003",
    "reader": "/root/reader_b",
    "model": "GPT-6 Astra Pro",
    "effort": "not exposed",
    "run": "SP92",
    "utc": datetime.now(timezone.utc).isoformat(),
    "scope": "Recorded evidence only; no images, new readings, compilation, assembly, row deletion or aggregate-count change.",
    "authority": [
        "pages/151_scan003.tex",
        "second/151_scan003_root_crop_notes.json",
        "second/151_scan003_adjudications.json",
        "existing current metadata for unchanged punctuation observations",
    ],
    "record_sha256_before": sha256(raw_before).hexdigest(),
    "record_sha256_after": digest(RECORD),
    "edits": edits,
    "field_edits": len(edits),
    "overlap_flags": overlap_flags,
    "overlap_action": "Flagged for root; no row was removed, merged, reclassified, or excluded from counts.",
    "historical_counter_note": "The original validation.changes=62 and other first-pass validation fields remain byte-equivalent as historical validation metadata. Current changes contains66 rows; the audit adds four rows. This cleanup makes no aggregate-count decision.",
    "protected_files_sha256": protected_hashes,
    "protected_record_fields": protected_record_fields,
    "checks": {
        "json_round_trip": True,
        "page_and_record_candidate_unchanged": True,
        "root_notes_and_adjudications_unchanged": True,
        "sealed_first_second_and_box_tsvs_unchanged": True,
        "raw_C_H_witness_fields_unchanged": True,
        "original_audit_first_second_and_audit_changes_unchanged": True,
        "second_boxes_and_historical_review_fields_unchanged": True,
        "decisions_unchanged": True,
        "change_ids_order_count_and_flags_unchanged": True,
        "all_76_diff_links_resolve": True,
        "all_20_differing_boxes_recorded_viewed": True,
        "exactly_10_audit_changed_boxes": True,
        "C61_current_fragment_occurs_in_page": True,
        "baseline_count_and_breakdown_unchanged": True,
        "no_image_view": True,
        "no_compilation": True,
        "no_assembly": True,
    },
}
LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({
    "record": str(RECORD),
    "log": str(LOG),
    "field_edits": len(edits),
    "current_rows_unchanged": len(current["changes"]),
    "overlap_flags": len(overlap_flags),
    "checks": "passed",
}, ensure_ascii=False))
