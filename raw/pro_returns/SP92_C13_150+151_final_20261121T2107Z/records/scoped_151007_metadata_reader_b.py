#!/usr/bin/env python3
"""Current-metadata alignment for audited 151_scan007; recorded evidence only."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path

W = Path("/workspace/scratch/d7279cb02214/SP92_C13_150+151_work")
record_path = W / "records/151_scan007.json"
log_path = W / "records/scoped_151007_metadata_reader_b.json"
raw = record_path.read_bytes()
before = json.loads(raw)
current = deepcopy(before)
root_notes = json.loads((W / "second/151_scan007_root_crop_notes.json").read_text())
adjudications = json.loads((W / "second/151_scan007_adjudications.json").read_text())
page = (W / "pages/151_scan007.tex").read_text()
protected_files = [
    "pages/151_scan007.tex", "records/151_scan007.tex",
    "second/151_scan007_boxes.tsv", "second/151_scan007_first.tsv",
    "second/151_scan007_second.tsv", "second/151_scan007_root_crop_notes.json",
    "second/151_scan007_adjudications.json", "records/audit_151_scan007.py",
    "records/151_scan007_root_audit_observations.md",
]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


protected_hashes = {p: digest(W / p) for p in protected_files}
edits = []


def get(obj, path):
    for key in path:
        obj = obj[key]
    return obj


def edit(path, value, reason, authority):
    old = get(current, path)
    if old == value:
        return
    get(current, path[:-1])[path[-1]] = value
    edits.append(dict(path=path, before=old, after=value,
                      reason=reason, authority=authority))


def row_index(key, ident, id_key="id"):
    return next(i for i, row in enumerate(current[key]) if row[id_key] == ident)


def change(ident, field, value, reason, authority):
    edit(["changes", row_index("changes", ident), field], value, reason, authority)


def diff(ident, value, authority):
    edit(["diff_coverage", row_index("diff_coverage", ident, "diff_id"), "reason"],
         value, "Align the current summary with the recorded audit; links and classifications are unchanged.",
         authority)


# Current prose descriptions; the historical mathematical checks are preserved.
notes = current["notes"]
replacements = [
    ("including the separate upper (x,x,y), the bare z,x,y",
     "including the separate upper tuple with doubtful first x and middle x|z, the bare z,x,y"),
    ("A smaller compartment works with delta2; adjacent live and canceled equations and a repeated E1/E2 diagram remain separately transcribed.",
     "A smaller compartment works with delta2; adjacent live and canceled equations and a repeated E1/E2 diagram remain individually transcribed within the integrated drawing."),
    ("The top coordinate/projection diagram has a clear chevron on its first tail-bar arrow.",
     "The top coordinate/projection diagram has a barred tail and two distinct right-facing chevrons on its first mapping; its two lower arrows have ordinary single heads."),
    ("The small box is a compartment within the lower right of the large outer rectangle, sharing its right and bottom border.",
     "The inner compartment occupies the lower right of the outer frame and shares its right and bottom borders. The outer frame has separate upper-left and lower-left joins and an overrun right upright; the compartment has a separately started left upright and a top rule ending in a small right arrowhead."),
    ("Only the repeated equation and separate id-like mark below it have dense hatching.",
     "The repeated equation and separate id-like mark below it have dense hatching."),
    ("The former can be narrowed to exposed p12sigma3 and final p12 with only the intervening equals/sigma doubtful; the latter remains doubtful as id.",
     "In the repeated equation, the initial p is exposed but its 12 subscript remains uncertain; sigma3 and final p12 are exposed, while the intervening equals/sigma also remains doubtful. The separate short entry remains doubtful as id."),
]
for old, new in replacements:
    assert notes.count(old) == 1, (old, notes.count(old))
    notes = notes.replace(old, new)
edit(["notes"], notes,
     "Remove superseded tuple certainty, single-head wording and overconfident cancellation recovery; align the shared-frame description without changing the recorded mathematical checks.",
     ["B04", "B06", "B24", "B25", "B27"])
edit(["line_count_note"], current["line_count_note"].replace(
    "detached brace/arrow labels", "detached annotation/arrow labels"),
    "Use current annotation terminology without changing the 53-baseline count or its convention.",
    ["B02", "B08", "B24", "B25"])

# The three side equations remain live; only the caption has the recorded
# alternative involving a cancelled short form.
edit(["deletion_insertion_review", 5, "place"],
     "Inner-compartment relations and uncertain parenthetic",
     "Identify the common compartment and distinguish its caption from the live equations.",
     ["B24", "B25"])
edit(["deletion_insertion_review", 5, "state"],
     "Three live relations and live lower annotations; the parenthetic retains a lexical/deletion-scope alternative.",
     "Do not describe the entire caption as certified live application.",
     ["B25"])
edit(["deletion_insertion_review", 5, "bounds"],
     "All three side equations and their two square-ended lower brackets remain live. The caption reads application or cancelled appl followed by constante, then de E1 sur, with final e subscript1|q. The adjacent underlined relation and sigma2delta2=delta2 remain live.",
     "Propagate the recorded word/deletion and final-index doubts only to their actual caption scope.",
     ["B25", "B26"])
edit(["deletion_insertion_review", 5, "attachment"],
     "The compartment shares the outer frame's right and bottom borders; its top rule has a small right arrowhead and its left upright starts separately below. Nearby hatching does not cancel the three side equations.",
     "Match the recorded integrated frame while preserving the equation cancellation bounds.",
     ["B24", "B25"])
edit(["deletion_insertion_review", 6, "attachment"],
     "Dense oblique hatching crosses the whole repeated relation. The initial p is exposed, but its12 subscript remains uncertain; sigma3 and final p12 are exposed, and central equals/sigma remains doubtful.",
     "Restore uncertainty on the initial12 while retaining the established partial recovery.",
     ["B27"])

inventory_updates = [
    (1, "element", "Cancelled p0 identity with a square-ended lower annotation",
     "The p31 grouping line has flat middle and upturned ends.", ["B02"]),
    (3, "element", "Cancelled two-row diagram with a barred double-headed first mapping",
     "The first mapping has two chevrons; both lower arrows remain ordinary single heads.", ["B04"]),
    (5, "first_words_or_objects", r"(\unsure{x},\unsure{x|z},y)",
     "Both recorded local coordinate uncertainties remain explicit.", ["B06"]),
    (6, "element", "Cancelled rho calculation with loop-ended continuation and square-ended y,x bracket",
     "Keep the continuation terminal and the y,x grouping geometry distinct.", ["B08"]),
    (7, "first_words_or_objects", r"\delta_1\sigma=(x\unsure{,}y,y)",
     "The first comma is not separable confidently from x's terminal curl.", ["B07"]),
    (9, "first_words_or_objects", r"(x,\unsure{x|z},y)",
     "Retain both admitted middle-coordinate readings.", ["B07"]),
    (11, "element", "Cancelled last mapping with barred tail and square downturned terminal",
     "No chevron is supplied to this mapping.", ["B10"]),
    (21, "element", "Five main relations within the integrated outer frame",
     "The common spatial drawing includes the inner compartment and right-side material.", ["B24"]),
    (21, "position", "lower outer frame, with separate left joins and an overrun right upright",
     "Replace the generic continuous-rectangle position description.", ["B24"]),
    (22, "element", "Two main square-ended lower brackets and their labels",
     "Keep the grouping strokes separate from the descending delta labels.", ["B24"]),
    (24, "element", "Three live relations in the inner compartment sharing the outer right and bottom",
     "Avoid implying a detached second box.", ["B24", "B25"]),
    (24, "position", "lower-right compartment within the integrated outer frame",
     "Record the shared spatial enclosure.", ["B24"]),
    (25, "element", "Two inner-compartment square-ended lower brackets and their labels",
     "Both lower annotation strokes are flat with upturned ends.", ["B25"]),
    (26, "element", "Inner-compartment parenthetic with word/deletion and final-index uncertainty",
     "Do not certify a single live lexical reading for the crowded caption.", ["B25"]),
    (26, "position", "three short lines beside the inner compartment's last equation",
     "Distinguish the caption from the equation's literal result e1.", ["B25"]),
    (26, "first_words_or_objects",
     r"(\unsure{application|\deleted{appl} constante} de E_1 sur e_{\unsure{1|q}})",
     "Preserve both the lexical/deletion alternative and final subscript doubt.", ["B25"]),
    (29, "first_words_or_objects",
     r"p_{\unsure{12}}\sigma_3\unsure{=\sigma}p_{12}",
     "The first12 and central equals/sigma remain uncertain under hatching.", ["B27"]),
    (31, "element", "Lower-right repeated diagram crossing the outer frame's right border",
     "The diagram belongs to the integrated cluster and crosses its boundary.", ["B24", "B29"]),
]
for i, field, value, reason, authority in inventory_updates:
    edit(["inventory", i, field], value, reason, authority)

edit(["notation", 3, "evidence"],
     "The continuation's small open loop is distinct from the two right-facing chevrons in the first coordinate diagram.",
     "Remove the superseded singular-head comparison.",
     ["B04", "B08"])
edit(["hand_log", 3, "habit"],
     "Mapping terminals include doubled chevrons, ordinary single heads, an open loop and a square turned end.",
     "Reflect the recorded occurrence-specific arrow forms without regularization.",
     ["B04", "B08", "B10"])
edit(["hand_log", 4, "scope"],
     "The live underlined RHS retains literal11. Other clear12 occurrences remain as read; the cancelled repeated relation's initial12 stays uncertain under hatching.",
     "Avoid implying that the newly doubtful cancelled index is certified.",
     ["B26", "B27"])
edit(["doubts", 4, "place"],
     "Initial subscript and center of the cancelled right repeated relation",
     "The current doubt covers the initial12 as well as the central signs.",
     ["B27"])
edit(["doubts", 4, "alternatives"],
     ["initial subscript tentatively12 under hatching",
      "equals followed by sigma", "central hatching not fully separable"],
     "Describe the already recorded index uncertainty without inventing an alternative numeral.",
     ["B27"])

# Current change descriptions. The already updated finals and raw C/H excerpts
# remain unchanged throughout this metadata-only pass.
change("C04", "evidence",
       "The first row has (x,y,z), a mapping with a barred tail and two independent right-facing chevrons, and (z,y,x). Below are a source-free ordinary right arrow, (x,z), and a second ordinary right arrow to x. All tuples agree, and the complete diagram remains cancelled en bloc. H condenses the calculations and omits this distinct two-row diagram.",
       "Replace conflicting singular-head and double-head descriptions with the recorded complete geometry.",
       ["B04"])
change("C06", "place", "Separate upper cancelled tuple",
       "The current place label must not certify the two uncertain coordinates as x,x.",
       ["B06"])
change("C06", "evidence",
       "The separate tuple remains cancelled within the upper draft. Its first x meets a diagonal strike and is not fully separable; the middle crossed/angled glyph admits x or z. Final y and the delimiters are clear. This separate occurrence is omitted from H; the added local uncertainty does not create a new correction row.",
       "Remove the superseded claim that both first coordinates are clearly x.",
       ["B06"])
change("C07", "evidence",
       "The written operator rho²sigma₂: precedes a mapping with its own tail bar and head. Two closing parentheses follow (z,y,x). The next-line continuation starts with a separate bar and ends in a small open loop, distinct from the first coordinate diagram's two chevrons. Its target is literally (y,x,z), with a square-ended bracket beneath y,x. The complete calculation remains cancelled en bloc.",
       "Remove obsolete underline and singular-head wording while retaining the literal coordinate order and extra delimiter.",
       ["B04", "B08"])
change("C08", "evidence",
       "The tuple letters are x,y,y, and delta's index1 and the equality are clear. The first comma after x cannot be separated confidently from x's terminal curl and remains doubtful. The formula is part of the upper draft cancelled en bloc.",
       "Include the recorded comma uncertainty without changing the cancelled-state correction.",
       ["B07"])
change("C10", "evidence",
       "The tuples occupy separate left-hand baselines within the cancelled upper draft. The second is plainly (y,y,x); the first has an overtraced middle glyph admitting x or z. The added uncertainty is retained locally and is not counted as a separate correction.",
       "Replace the earlier x-only description with the audited x|z doubt.",
       ["B07"])
change("C34", "place",
       "Integrated outer frame, shared inner compartment and right-side spatial layout",
       "The row now records the entire cluster's frame/placement geometry, not only a generic five-row rectangle.",
       ["B24"])
change("C34", "evidence",
       current["changes"][row_index("changes", "C34")]["evidence"] +
       " This row records the frame and spatial placement; C44 and C45 separately record the two main lower annotation shapes.",
       "Keep the cluster-geometry scope distinct from the two main bracket rows.",
       ["B24", "existing C44/C45 scopes"])
change("C36", "place", "Delta1 label and lower bracket under rho delta2 in the inner compartment",
       "Use the integrated-compartment description for the already recorded label/geometry correction.",
       ["B25"])
change("C37", "place", "Delta3 label and lower bracket under rho squared delta2 in the inner compartment",
       "Use the integrated-compartment description without extending caption uncertainty to the literal equation result e1.",
       ["B25"])
change("C38", "place",
       "Inner-compartment parenthetic with uncertain word/deletion scope and final e subscript",
       "Remove the old title that certified application and final e1.",
       ["B25"])
change("C42", "evidence",
       current["changes"][row_index("changes", "C42")]["evidence"] +
       " The diagram crosses the outer frame's right border in the integrated cluster; that spatial relationship is recorded by C34.",
       "Retain the border-crossing relationship while keeping this row's omitted-diagram scope distinct.",
       ["B24", "B29"])

diff("D0983",
     "H condenses away the separate cancelled two-row coordinate/projection diagram. The current first mapping has a barred tail and two distinct right heads; the two lower arrows have ordinary single heads.",
     ["B04"])
diff("D0988",
     "The separate upper tuple is omitted from H; its first x is doubtful and its middle coordinate remains x|z. Le calcul de is editorial connective prose.",
     ["B06"])
for ident in ["D0991", "D0992"]:
    diff(ident,
         "The delta tuple, bare right-hand triple and repeated left tuples retain their cancelled state and source arrangement. The first comma of delta1sigma is doubtful, and the repeated tuple's middle coordinate remains x|z.",
         ["B07", "B09"])
for ident in ["D1016", "D1021"]:
    diff(ident,
         "The five main relations belong to an outer frame with pen gaps and a shared lower-right compartment, rather than a cases brace. C34 records the integrated frame and placement geometry; C44/C45 record the main lower bracket shapes separately.",
         ["B24"])
diff("D1022",
     "H's introductory explanation is editorial. The three side relations occupy an inner compartment sharing the outer frame's right and bottom borders; they are not a detached second box in the current page.",
     ["B24", "B25"])
for ident in ["D1027", "D1028", "D1029"]:
    diff(ident,
         "The parenthetic remains uncertain between application and cancelled appl followed by constante; de E1 sur is retained, and its final e subscript is1|q. H paraphrases the material as a constant map.",
         ["B25"])
diff("D1030",
     "The live underlined relation retains literal p11. The two heavily cancelled entries remain separate: the repeated relation has a doubtful initial12 and central equals/sigma, while the id-like scrap stays tentative. These are not H's editorial recap.",
     ["B26", "B27", "B28"])
for ident in ["D1031", "D1032"]:
    diff(ident,
         "The lower-right diagram crosses the integrated frame's right border, and thin foliation6 is present. H's remaining prose is editorial; C34 records the common cluster geometry separately from C42's diagram omission.",
         ["B24", "B29"])

# Original readings, historical audit records, decisions and counts are locked.
for key in ["half_review", "root_review", "root_reviewed", "second_boxes", "crops",
            "audit_changes", "audit_reader", "audit_boxes", "audit_differing_boxes",
            "audit_token_difference_runs", "audit_changed_boxes", "audit_utc",
            "line_count", "check_events", "decisions", "abbreviations"]:
    assert current[key] == before[key], key
assert len(current["changes"]) == len(before["changes"]) == 45
assert len(current["diff_coverage"]) == len(before["diff_coverage"]) == 55
assert len(current["inventory"]) == 33
assert len(current["deletion_insertion_review"]) == 8
assert len(current["doubts"]) == 10
for old, new in zip(before["changes"], current["changes"]):
    for key in set(old) | set(new):
        if key not in {"place", "evidence"}:
            assert old.get(key) == new.get(key), (old["id"], key)
for old, new in zip(before["diff_coverage"], current["diff_coverage"]):
    for key in set(old) | set(new):
        if key != "reason":
            assert old.get(key) == new.get(key), (old["diff_id"], key)


def protected_leaves(obj, path=()):
    found = {}
    if isinstance(obj, dict):
        for key, val in obj.items():
            if key in {"C", "H", "C_items", "first", "second", "witness_errors"}:
                found[path + (key,)] = val
            else:
                found.update(protected_leaves(val, path + (key,)))
    elif isinstance(obj, list):
        for i, val in enumerate(obj):
            found.update(protected_leaves(val, path + (i,)))
    return found


assert protected_leaves(current) == protected_leaves(before)
ids = {row["id"] for row in current["changes"]}
assert all(cid in ids for row in current["diff_coverage"] for cid in row["change_ids"])
assert len(root_notes) == sum(bool(v.get("viewed")) for v in root_notes.values()) == 29
assert sum(bool(v.get("changed")) for v in root_notes.values()) == 8
assert len(adjudications["adjudications"]) == 29
assert current["audit_boxes"] == 30
assert current["audit_changed_boxes"] == 8
assert current["audit_differing_boxes"] == 29
assert current["changes"][row_index("changes", "C34")]["final"] in page
assert current["changes"][row_index("changes", "C38")]["final"] in page
assert protected_hashes["pages/151_scan007.tex"] == protected_hashes["records/151_scan007.tex"]

flags = [
    {
        "rows": ["C34", "C44", "C45"],
        "assessment": "C34 contains the whole cluster as final context but now explicitly records frame/spatial geometry; C44/C45 independently record the two main square-ended annotation shapes. No confirmed duplicate correction and no row/count change.",
    },
    {
        "rows": ["C34", "C42"],
        "assessment": "C34 records the lower diagram's border-crossing placement within the cluster; C42 records H's omission of its objects/arrows. Same region, separately stated features; no deduplication.",
    },
    {
        "rows": ["C34", "C35", "C36", "C37", "C38", "C39", "C40", "C41"],
        "assessment": "The complete cluster final necessarily contains the text, labels and cancelled entries corrected by these other rows. The cluster row is restricted descriptively to frame and spatial layout, not a second count of those readings.",
    },
    {
        "rows": ["C02", "C04"],
        "assessment": "Audit updates add C-side bracket/double-head geometry to rows whose earlier categories concern H's deletion-state error or omission. Their witness/category scopes are mixed; classification and all count flags are left unchanged for root.",
    },
    {
        "rows": ["C36", "C37"],
        "assessment": "C-side departures now concern bracket geometry; H-side departures concern omitted mathematical labels. Both rows retain the existing omission category and consequential flag. Root may wish to distinguish these witness-specific scopes in any count interpretation; no flags changed here.",
    },
]
assert record_path.read_bytes() == raw, "Concurrent record edit detected."
new_bytes = (json.dumps(current, ensure_ascii=False, indent=2) + "\n").encode()
assert json.loads(new_bytes) == current
record_path.write_bytes(new_bytes)
assert json.loads(record_path.read_bytes()) == current
for rel, expected in protected_hashes.items():
    assert digest(W / rel) == expected, rel

log = {
    "task": "Current-metadata consistency cleanup for audited 151_scan007",
    "reader": "/root/reader_b", "model": "GPT-6 Astra Pro", "effort": "not exposed",
    "run": "SP92", "utc": datetime.now(timezone.utc).isoformat(),
    "authority": ["pages/151_scan007.tex", "second/151_scan007_root_crop_notes.json",
                  "second/151_scan007_adjudications.json", "records/audit_151_scan007.py",
                  "records/151_scan007_root_audit_observations.md"],
    "scope": "Current descriptions only. No new readings/images, row additions/removals, count-flag changes, compilation or assembly. The separately authorized caption layout encoding is not part of this pass.",
    "record_sha256_before": sha256(raw).hexdigest(),
    "record_sha256_after": digest(record_path),
    "field_edits": len(edits), "edits": edits,
    "scope_flags": flags,
    "protected_files_sha256": protected_hashes,
    "checks": {
        "json_round_trip": True,
        "all_45_changes_ids_order_C_H_finals_and_count_flags_unchanged": True,
        "all_55_diff_classifications_links_unchanged_and_valid": True,
        "all_29_differing_boxes_recorded_viewed": True,
        "exactly_8_changed_audit_boxes": True,
        "all_8_decisions_unchanged": True,
        "line_count_53_unchanged": True,
        "page_and_records_tex_unchanged_and_identical": True,
        "sealed_first_second_and_box_tsvs_unchanged": True,
        "audit_originals_history_second_boxes_and_observation_files_unchanged": True,
        "no_images_or_new_readings": True,
        "no_compilation_or_assembly": True,
    },
}
log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"log": str(log_path), "field_edits": len(edits),
                  "change_rows_unchanged": 45, "checks": "passed"}))
