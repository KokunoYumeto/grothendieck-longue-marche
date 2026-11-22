#!/usr/bin/env python3
"""Repair only current metadata for already audited 151_scan005.

Authority is the existing page and recorded root audit. No images or source
readings, compilation, assembly, new change rows, or count decisions are made.
"""

from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path

W = Path("/workspace/scratch/d7279cb02214/SP92_C13_150+151_work")
record_path = W / "records/151_scan005.json"
log_path = W / "records/scoped_151005_metadata_reader_b.json"
record_bytes = record_path.read_bytes()
before = json.loads(record_bytes)
current = deepcopy(before)
page = (W / "pages/151_scan005.tex").read_text()
root_notes = json.loads((W / "second/151_scan005_root_crop_notes.json").read_text())
adjudications = json.loads((W / "second/151_scan005_adjudications.json").read_text())
audit_script = (W / "records/audit_151_scan005.py").read_text()
protected_files = [
    "pages/151_scan005.tex", "records/151_scan005.tex",
    "second/151_scan005_boxes.tsv", "second/151_scan005_first.tsv",
    "second/151_scan005_second.tsv",
    "second/151_scan005_root_crop_notes.json",
    "second/151_scan005_adjudications.json",
    "records/audit_151_scan005.py",
]


def file_hash(path):
    return sha256(path.read_bytes()).hexdigest()


protected_hashes = {p: file_hash(W / p) for p in protected_files}
edits = []


def get(obj, path):
    for item in path:
        obj = obj[item]
    return obj


def edit(path, value, reason, authority):
    old = get(current, path)
    if old == value:
        return
    get(current, path[:-1])[path[-1]] = value
    edits.append({
        "path": path, "before": old, "after": value,
        "reason": reason, "authority": authority,
    })


def index(key, row_id, id_key="id"):
    return next(i for i, row in enumerate(current[key]) if row[id_key] == row_id)


def change(row_id, field, value, reason, authority):
    edit(["changes", index("changes", row_id), field], value, reason, authority)


def diff(row_id, value, authority):
    edit(["diff_coverage", index("diff_coverage", row_id, "diff_id"), "reason"],
         value, "Align the current diff description with the recorded audit; classification and links are unchanged.",
         authority)


# Preserve the C_item witness excerpts. Repair current revision descriptions.
revision_updates = [
    (0, "state",
     "Mixed upper inventory: p0/p1 and delta0 in the left column are live; the middle p lists and right delta list are cancelled.",
     "The original whole-block deletion rationale is superseded by the recorded physical strike scope.", ["B01"]),
    (0, "attachment",
     "The upper inventory precedes the separate framed diagram and enclosed lists. Its live left-column entries are outside the middle/right cancellations; no replacement is inserted between the left-column letters.",
     "Describe the live/cancelled column scope without treating draft context as a deletion.", ["B01"]),
    (0, "evidence",
     "The recorded oblique strikes cross the middle p lists and the right delta1–3 list, but do not touch the separate left p0/p1 or delta0. The current page therefore retains the left column as live and applies deletion only to the crossed blocks; the small middle sigma-like draft also retains its separate cancellation.",
     "Remove the obsolete statement defending an outer deletion wrapper over live entries.", ["B01"]),
    (1, "attachment",
     "Small middle line between the two p-index rows of the upper inventory, within the cancelled middle block.",
     "Keep the separately cancelled draft attached to the cancelled middle column.", ["B01"]),
    (2, "attachment",
     "Below the mixed live/cancelled upper inventory, before the live id,sigma pair.",
     "Avoid implying that the entire upper inventory is deleted.", ["B01"]),
    (6, "state", "Live square-ended grouping brackets and underlabels.",
     "Distinguish the two flat lower brackets from a genuine cusped brace.", ["B06"]),
    (6, "evidence",
     "Both lower annotation lines have straight middles and short upturned ends, without central cusps. They are live square-ended brackets, not deletion bars. The separate parentheses in the third row enclose rho-squared delta1.",
     "Use the audited bracket geometry while retaining the existing parenthesis attachment.", ["B06"]),
    (7, "state", "Cancelled framed p-pair with a comma/slash separator doubt.",
     "The separator is no longer certified as a slash.", ["B07"]),
    (7, "evidence",
     "The upper p-pair is crossed within its frame. A short curved separator survives under the looping strike and favors a comma, while a slash remains possible; retain the local comma/slash uncertainty.",
     "Replace the earlier definite-slash description with the recorded unresolved separator.", ["B07"]),
    (9, "state", "Live curved leftward pointing leader.",
     "Identify the recorded curvature and direction without changing its attachment.", ["B08"]),
    (11, "state",
     "Live square-ended lower annotation with an unresolved overtraced label; no separately certified deleted letter.",
     "Keep the flat bracket geometry separate from the q1/p1 letter uncertainty.", ["B10"]),
]
for i, field, value, reason, authority in revision_updates:
    edit(["deletion_insertion_review", i, field], value, reason, authority)

# Existing inventory rows only; no element is added or removed.
inventory_updates = [
    (1, "element", "Upper three-column inventory with live left entries and cancelled middle/right blocks",
     "Remove the obsolete whole-block abandonment description.", ["B01"]),
    (1, "kind", "display",
     "This single inventory row contains both live and cancelled material.", ["B01"]),
    (4, "element", "Shouldered open frame with E0,E1,E2, a detached uncertain mark above E2 and four arrows",
     "Include the recorded detached E2 mark.", ["B03"]),
    (4, "first_words_or_objects",
     r"E_0,E_1,\overset{\unsure{\prime|\cdot}}{E}_2;\ \mathcal G_2,\mathcal G_3;\ p_0,\delta_0,p_{12},\delta_1",
     "Retain the prime/dot uncertainty in the object inventory.", ["B03"]),
    (6, "element", "Three central relations with two square-ended lower brackets in a frame with a doubled upper-left return",
     "Record both the lower bracket forms and the audited frame return.", ["B06"]),
    (7, "element", "Two E0 relations in one frame with separate corner gaps",
     "The four frame strokes stop separately before adjacent corners.", ["B05"]),
    (9, "element", "Three single-prime definitions inside an oval clipped at right and interrupted at its upper-left join",
     "Avoid implying a closed continuous prime-definition oval.", ["B08"]),
    (10, "element", "Cancelled framed p-pair with an uncertain comma/slash separator",
     "The cancelled separator remains unresolved.", ["B07"]),
    (10, "first_words_or_objects", r"\deleted{p_0\unsure{,|/}p_1}",
     "Replace the stale definite slash in this current inventory description.", ["B07"]),
    (11, "element", "Live p0,p1 oval with a hooked overlapping upper-right closure",
     "Include the recorded closing return.", ["B07"]),
    (12, "element", "Two sigma relations in a common interrupted frame with a genuine cusped underbrace and live p21 label",
     "Keep the actual underbrace distinct from the other square-ended annotation brackets.", ["B08"]),
    (13, "element", "Delta-generator oval and curved leftward leader",
     "The leader is curved, not a straight relation stroke.", ["B08"]),
    (13, "first_words_or_objects", r"\delta_1,\delta_2,\delta_3; curved leftward leader",
     "Avoid a straight long-arrow glyph in the current shape description.", ["B08"]),
    (14, "first_words_or_objects",
     r"p_{12},p_{23},p_{31};\ p_{21},p_{32},p_{13};\ \unsure{3} at the oval outline",
     "The doubtful 3-like contour is not a fourth entry or an exponent on p31.", ["B08"]),
    (15, "element", "Two invariance rows in one wide interrupted frame",
     "Include the audited breaks in the common frame.", ["B09"]),
    (16, "element", "Final product relation in a frame with corner gaps and a square-ended lower annotation",
     "Remove the generic continuous-box/brace description.", ["B10"]),
    (16, "first_words_or_objects",
     r"p_0p_{12}\sigma_1=p_0p_{12}; square-ended lower bracket labelled \unsure{q_1|p_1}",
     "Keep the current square-ended bracket and unresolved q1/p1 label explicit.", ["B10"]),
    (17, "element", "q-generator oval with a flattened right side, upper overlap and inward tick",
     "Describe the recorded outline without interpreting its ticks as letters.", ["B11"]),
]
for i, field, value, reason, authority in inventory_updates:
    edit(["inventory", i, field], value, reason, authority)

# Current notes: historical computations and first-pass observations stay intact.
notes = current["notes"]
note_replacements = [
    ("The upper inventory is abandoned as a block, although its left-column p0/p1 and delta0 are not physically struck.",
     "The upper inventory has a live left column containing p0/p1 and delta0, while its middle and right blocks are cancelled."),
    ("The sigma p12 annotation in the side relation box has a genuine central cusp and remains a brace.",
     "The sigma p12 annotation in the side relation box has a genuine central cusp and remains a brace. The delta-generator oval has a separate curved leftward leader to the first sigma relation."),
    ("The primed-definition oval is kept open at its clipped right edge,",
     "The primed-definition oval is kept open at its clipped right edge and interrupted upper-left join,"),
]
for old, new in note_replacements:
    assert notes.count(old) == 1, (old, notes.count(old))
    notes = notes.replace(old, new)
edit(["notes"], notes,
     "Remove the stale whole-block deletion rationale and complete the recorded leader/oval geometry descriptions.",
     ["B01", "B08"])
edit(["notation", 4, "sign"], r"p_0/p_1; p_0\unsure{,|/}p_1",
     "Separate the live upper slash from the cancelled margin separator doubt.", ["B01", "B07"])
edit(["notation", 4, "reading"],
     "The live upper-left inventory has a literal slash; the cancelled framed p-pair has a comma-first comma/slash uncertainty.",
     "Do not generalize the clear upper slash to the separately cancelled pair.", ["B01", "B07"])
edit(["notation", 4, "evidence"],
     "The top p0/p1 and delta0 are outside the cancellation strokes. In the cancelled margin pair, a short curved separator survives within the looping strike and favors comma, with slash still possible.",
     "Align the notation statement with the recorded strike boundaries and separator uncertainty.", ["B01", "B07"])
mark_i = index("decisions", "M0748")
edit(["decisions", mark_i, "reading"], r"\unsure{3}",
     "The current mark is placed at the outline and is no longer encoded as an exponent.", ["B08"])
edit(["decisions", mark_i, "ink"],
     "The 3-like contour remains uncertain at the upper-right oval outline. It may be a numeral or a curled closing stroke; it is retained at that outline position, without asserting an exponent attached to p31.",
     "Keep the current decision description consistent with C25 and the recorded audit.", ["B08"])

# Current change-row evidence and final snippets, without changing row counts.
change("C10", "final", r"E_1\xleftarrow{p_{12}}\overset{\unsure{\prime|\cdot}}{E}_2",
       "Keep the illustrative arrow fragment's E2 endpoint consistent with the audited detached mark; C37 remains the separate mark-omission row.",
       ["B03", "current C37 final"])
change("C13", "evidence",
       "Both E0 identities share one frame. Its top, bottom, left and right strokes each stop before adjacent corners, leaving separate pen gaps. There are no independent enclosures for the two rows.",
       "Replace the generic frame description with the recorded interrupted outline.", ["B05"])
change("C16", "evidence",
       "All three central rows share one four-sided frame. Its upper-left edge has a doubled return and a gap to the top rule. The long left stroke belongs to this frame rather than to a cases brace. The separate cancelled id-like draft remains tentative, and the two lower annotation lines are square-ended brackets, as recorded in their own rows.",
       "Describe the specific frame return/gap while preserving the separate draft and annotation scopes.", ["B06"])
change("C20", "evidence",
       "The upper p-pair is cancelled within its frame. Both p entries and their indices remain readable. A short curved separator under the looping strike favors a comma, but a slash remains possible; retain comma/slash uncertainty. The recorded frame segments are preserved in the current final.",
       "Remove the contradictory definite-slash statement.", ["B07"])

# C21 concerns the left relation frame only. Extract those exact current-page
# drawing commands from the already audited B08 cluster, omitting the leader,
# ovals and primed definitions that have their own change rows.
c40 = current["changes"][index("changes", "C40")]
cluster = c40["final"]
assert cluster in page
leader_line = r"\draw[->] (2,1.14)..controls(1.7,1.5)and(.25,1.68)..(-.6,1.47);"
assert cluster.count(leader_line) == 1
left_frame_prefix = cluster[:cluster.index(leader_line)]
assert left_frame_prefix in page
left_frame_final = left_frame_prefix + r"\end{tikzpicture}}"
change("C21", "final", left_frame_final,
       "The old bare gathered equations omitted the frame this row claims to record. Use the exact current-page left relation/frame drawing, retaining its genuine cusped underbrace.",
       ["B08", "current page", "audit_151_scan005.py: new8"])
change("C21", "evidence",
       "One interrupted frame surrounds the two stacked sigma relations. The sigma p12 underannotation has a genuine central downward cusp and is labelled p21; the crossing of its stem by the lower frame boundary is not cancellation. The current final now includes these actual frame strokes. The curved delta-oval leader is a separate feature recorded by C24.",
       "Keep the common frame, genuine brace and separate leader scopes explicit.", ["B08"])
change("C26", "evidence",
       "Both invariant statements, including the i.e. row and pour g in G3, share one wide interrupted frame. The separate corner strokes and upper-right return are drawn in the current page. The isolated lower-left dot is not sentence punctuation.",
       "Describe the audited frame instead of appending a generic gap statement.", ["B09"])
change("C40", "evidence",
       c40["evidence"].replace("the latter has a separate3-like closing curl left doubtful",
                               "the latter has a 3-like outline curl left doubtful"),
       "Do not imply that the uncertain closing contour is a separately certified numeral.", ["B08"])

# This is a correction of a NEW current witness summary, not a change to the
# original witness or to the historical audit first reading. The root audit
# script populated C41.C from old10 (the resolved first-pass candidate).
assert "'C41','Final relation bracket and interrupted frame',old10" in audit_script
c31 = current["changes"][index("changes", "C31")]
c29 = current["changes"][index("changes", "C29")]
assert c29["C"] == r"\sigma_{\unsure{1|3}}"
assert c29["C"] in c31["C"]
change("C41", "C", c31["C"],
       "Restore the actual recorded C witness excerpt from the same-locus C31 field. The audit script copied the resolved first-pass candidate old10 into this new C summary and thereby lost C's sigma 1|3 uncertainty.",
       ["existing C29.C", "existing C31.C", "audit_151_scan005.py: C41/old10 provenance"])

# Diff classifications/links remain unchanged; these are current descriptions.
diff("D0932",
     "The delta0 of the first inventory column is present in both witnesses but moved in H's prose description. The separate audited deletion-state correction keeps this left-column entry live and is recorded by C36.",
     ["B01"])
diff("D0953",
     "The three relations share a four-sided frame with a doubled upper-left return and a gap to the top rule; the left side is not a cases brace.",
     ["B06"])
diff("D0959",
     "The cancelled framed p-pair is omitted in H; its intervening separator remains comma/slash uncertain.",
     ["B07"])
diff("D0960",
     "The alignment contains both rendering syntax and source drawing features. The two sigma relations share one interrupted frame, unlike H's separate boxes; audited oval-contour differences are recorded separately by C40.",
     ["B08"])
diff("D0964",
     "The broad shift includes the omitted curved leftward leader, the unresolved 3-like mark on the oval outline, and the scope of the wide frame. All three prime equations and the six ordinary p-indices agree in the recorded audit.",
     ["B08", "B09"])
diff("D0969",
     "H's backslash-comma between the factors is mathematical spacing. The current lower annotation is a square-ended bracket; that separate geometry correction is recorded by C41.",
     ["B10"])

# Protect historical observations, original blind readings and all count fields.
for key in ["half_review", "root_review", "root_reviewed", "second_boxes",
            "audit_changes", "audit_reader", "audit_boxes",
            "audit_differing_boxes", "audit_token_difference_runs",
            "audit_changed_boxes", "audit_utc", "line_count", "check_events"]:
    assert current[key] == before[key], key
assert len(current["changes"]) == len(before["changes"]) == 42
assert len(current["diff_coverage"]) == len(before["diff_coverage"]) == 47
assert len(current["inventory"]) == len(before["inventory"]) == 19
assert len(current["deletion_insertion_review"]) == 12
assert len(current["decisions"]) == 6
assert [x["id"] for x in current["changes"]] == [x["id"] for x in before["changes"]]
for old, new in zip(before["changes"], current["changes"]):
    allowed = {"evidence", "final"} | ({"C"} if old["id"] == "C41" else set())
    for key in set(old) | set(new):
        if key not in allowed:
            assert old.get(key) == new.get(key), (old["id"], key)
for old, new in zip(before["diff_coverage"], current["diff_coverage"]):
    for key in set(old) | set(new):
        if key != "reason":
            assert old.get(key) == new.get(key), (old["diff_id"], key)
for old, new in zip(before["deletion_insertion_review"], current["deletion_insertion_review"]):
    assert old["C_item"] == new["C_item"]
for old, new in zip(before["decisions"], current["decisions"]):
    if old["id"] != "M0748":
        assert old == new
    else:
        for key in old:
            if key not in {"reading", "ink"}:
                assert old[key] == new[key]


def protected_leaves(obj, path=()):
    out = {}
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in {"first", "second", "witness_errors"}:
                out[path + (key,)] = value
            else:
                out.update(protected_leaves(value, path + (key,)))
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            out.update(protected_leaves(value, path + (i,)))
    return out


assert protected_leaves(current) == protected_leaves(before)
change_ids = {x["id"] for x in current["changes"]}
assert all(cid in change_ids for row in current["diff_coverage"] for cid in row["change_ids"])
assert len(root_notes) == sum(bool(n.get("viewed")) for n in root_notes.values()) == 11
assert sum(bool(n.get("changed")) for n in root_notes.values()) == 9
assert len(adjudications["adjudications"]) == 11
assert current["audit_boxes"] == 12
assert current["audit_differing_boxes"] == 11
assert current["audit_changed_boxes"] == 9
assert current["decisions"][mark_i]["reading"] == r"\unsure{3}"
assert r"\overset{\unsure{\prime|\cdot}}{E}_2" in page
assert r"\deleted{\unsure{\mathrm{id}}}" in page
assert protected_hashes["pages/151_scan005.tex"] == protected_hashes["records/151_scan005.tex"]

overlap_flags = [
    {
        "rows": ["C21", "C40"],
        "locus": "Side sigma-relation frame",
        "assessment": "C21 records the common frame and its interrupted outline. C40 is titled for generator ovals but also explicitly mentions the same left-frame gap. Its full-cluster final contains the frame. This shared correction needs root's scope/count treatment; no row is removed here.",
    },
    {
        "rows": ["C24", "C40"],
        "locus": "Curved leader from the delta-generator oval",
        "assessment": "C24 separately records the curved leader. C40's evidence/final also includes that leader while its C/H descriptions concern oval outlines. Flagged as a repeated feature claim, without deleting C40's independently changed oval geometry.",
    },
    {
        "rows": ["C25", "C40"],
        "locus": "Six-p oval's uncertain 3-like closing contour",
        "assessment": "C25 records the unresolved outline mark; C40 includes it as context for the oval shape. This is a scope overlap, not evidence that C40 lacks a separate oval correction.",
    },
    {
        "rows": ["C31", "C41"],
        "locus": "Final product relation",
        "assessment": "The final strings coincide, but C31 explicitly limits its correction to terminal punctuation; C41 records the bracket and frame geometry. No confirmed duplicate correction.",
    },
    {
        "rows": ["C16", "C18", "C19", "C38"],
        "locus": "Central three-relation frame",
        "assessment": "C16's full final contains the cancelled id-like draft, third-row parentheses/bracket and middle-row bracket addressed by C18/C19/C38. C16 itself is a frame-scope row; the aspects are separately stated rather than confirmed duplicates.",
    },
    {
        "rows": ["C26", "C27", "C28"],
        "locus": "Wide invariant-statements frame",
        "assessment": "C26's full-frame final includes the G glyph and ending addressed by C27/C28, whose scopes are letter reading and punctuation. No confirmed duplicate correction.",
    },
    {
        "rows": ["C29", "C30", "C41"],
        "locus": "Final product relation",
        "assessment": "C41's whole-formula final includes the resolved sigma index and uncertain label separately addressed by C29/C30. C41's place names bracket/frame geometry. No count action is taken.",
    },
    {
        "rows": ["C32", "C33", "C34", "C42"],
        "locus": "Lower-right q oval",
        "assessment": "C42 contains the q entries as context but records the outline; C32–C34 record the three letter readings. No confirmed duplicate correction.",
    },
]
metadata_flags = [
    {
        "path": ["changes", index("changes", "C36"), "kind"],
        "value": current["changes"][index("changes", "C36")]["kind"],
        "issue": "Uses shorthand 'deletion state' rather than the previously specified full collation-kind value. Left unchanged because this assignment is a description/provenance repair, with change classifications and counts protected.",
    },
    {
        "path": ["changes", index("changes", "C19")],
        "issue": "This parentheses-focused omission row now also carries a C-side bracket-geometry correction. Its C field already has the parentheses. The C and H departures therefore have different feature/category scopes; root should review that mixed counting scope. No classification, count flag or row is changed here.",
    },
    {
        "path": ["changes", index("changes", "C20")],
        "issue": "This omission row now also carries C-side separator/frame corrections although C already contains the cancelled pair. H's omission and C's changed reading/geometry have different feature/category scopes; root should review without treating them as identical omissions. No classification, count flag or row is changed here.",
    }
]

assert record_path.read_bytes() == record_bytes, "Concurrent root record edit detected."
new_bytes = (json.dumps(current, ensure_ascii=False, indent=2) + "\n").encode()
assert json.loads(new_bytes) == current
record_path.write_bytes(new_bytes)
assert json.loads(record_path.read_bytes()) == current
for rel, expected in protected_hashes.items():
    assert file_hash(W / rel) == expected, rel

log = {
    "task": "Current-metadata consistency cleanup for audited 151_scan005",
    "reader": "/root/reader_b", "model": "GPT-6 Astra Pro",
    "effort": "not exposed", "run": "SP92",
    "utc": datetime.now(timezone.utc).isoformat(),
    "scope": "Existing root audit and page only; no images, new readings, added/removed change rows, aggregate decisions, compilation or assembly.",
    "authority": [
        "pages/151_scan005.tex", "second/151_scan005_root_crop_notes.json",
        "second/151_scan005_adjudications.json", "records/audit_151_scan005.py",
        "existing C29.C and C31.C for correction of new current C41.C provenance",
    ],
    "record_sha256_before": sha256(record_bytes).hexdigest(),
    "record_sha256_after": file_hash(record_path),
    "field_edits": len(edits), "edits": edits,
    "overlap_flags": overlap_flags,
    "overlap_action": "Flagged only. No row merge, deletion, reclassification, exclusion or change to count flags.",
    "metadata_flags": metadata_flags,
    "protected_files_sha256": protected_hashes,
    "checks": {
        "json_round_trip": True,
        "page_and_records_tex_unchanged_and_identical": True,
        "sealed_first_second_and_box_tsvs_unchanged": True,
        "original_audit_first_second_and_audit_changes_unchanged": True,
        "root_notes_adjudications_and_audit_script_unchanged": True,
        "historical_half_review_root_review_and_second_boxes_unchanged": True,
        "original_C_item_witness_excerpts_unchanged": True,
        "all_C_H_fields_unchanged_except_authorized_new_C41_C_summary": True,
        "decision_changes_limited_to_current_M0748_description": True,
        "all_42_change_ids_order_and_count_flags_unchanged": True,
        "all_47_diff_classifications_and_links_unchanged_and_valid": True,
        "all_11_differing_boxes_recorded_viewed": True,
        "exactly_9_changed_audit_boxes": True,
        "C21_drawing_commands_copied_from_unchanged_page": True,
        "line_count_35_unchanged": True,
        "no_images": True, "no_new_readings": True,
        "no_compilation": True, "no_assembly": True,
    },
}
log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({
    "record": str(record_path), "log": str(log_path),
    "field_edits": len(edits), "change_rows_unchanged": len(current["changes"]),
    "overlap_flags": len(overlap_flags), "checks": "passed",
}, ensure_ascii=False))
