"""Complete public reader slots from existing audited sources, once only.

This repair reads no reader files and performs no new source-span audit.
"""

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
RECORD = HERE / "scan017_record_draft.json"
NOTE = HERE / "scan017_public_reader_repair.md"
EXPECTED_RECORD = "ad6d9c2e4814117cc541d7ce6101648eb2825b9dc290d06f255caef9a9bab0fa"
PRIOR_AUDIT = "4b12b4a0920de5850c4a9dc5206f85eb19a53f9417b03b005b067e3b7bde4b7d"
EXPECTED_MISSING = {
    "017-S01": list("ABC"),
    "017-S02": list("ABC"),
    "017-G13": list("AB"),
    "017-P01": list("ABC"),
    "017-S03": list("ABC"),
    "017-G12": list("AC"),
    "017-N04": ["C"],
    "017-N05": ["C"],
    "017-G05": ["B"],
    "017-G05-index": list("AB"),
    "017-G11": ["B"],
    "017-G11-upper": ["B"],
    "017-G11-lower": ["B"],
    "017-N06": ["C"],
    "017-G06": ["C"],
    "017-D12-final": list("BC"),
    "017-ARCHIVE": list("ABC"),
}

# These notes describe only the supplied reader source at the audited scope.
ABSENCE_NOTES = {
    ("017-G12", "A"): "No separate wedge is encoded in this complete slanted-note excerpt.",
    ("017-G12", "C"): "No separate wedge is encoded in this complete slanted-note excerpt.",
    ("017-G05", "B"): "The excerpt represents no separate upper mark.",
    ("017-G05-index", "B"): "The excerpt represents no separate upper mark.",
    ("017-G11", "B"): "No far-right pair is represented between this display endpoint and the following prose.",
    ("017-G11-upper", "B"): "No upper component of the far-right pair is represented in this source span.",
    ("017-G11-lower", "B"): "No lower component of the far-right pair is represented in this source span.",
    ("017-G06", "C"): "No separate point preceding the first union is represented in this source span.",
}


original_bytes = RECORD.read_bytes()
assert sha256(original_bytes).hexdigest() == EXPECTED_RECORD, "Record changed; stop."
record = json.loads(original_bytes)
original = deepcopy(record)
assert "public_reader_display_repair" not in record
assert len(record["decisions"]) == 56
actual_missing = {
    d["id"]: [role for role in "ABC" if not d["readers"].get(role)]
    for d in record["decisions"]
    if any(not d["readers"].get(role) for role in "ABC")
}
assert actual_missing == EXPECTED_MISSING
changed_slots = []

for index, decision in enumerate(record["decisions"]):
    assert "readers_report_only" not in decision
    decision["readers_report_only"] = deepcopy(decision["readers"])
    roles = actual_missing.get(decision["id"], [])
    if roles:
        decision["public_reader_source_provenance"] = {}
    for role in roles:
        assert role not in decision["readers"]
        proposals = decision["reader_tex_proposals"][role]
        assert len(proposals) == 1
        attachment = proposals[0]["attachment"]
        assert attachment["manifest"] == f"{role}.reading.tex"
        pointer = f"/decisions/{index}/reader_tex_proposals/{role}/0/attachment"
        absence_note = ABSENCE_NOTES.get((decision["id"], role))
        text = (
            f"Audited reader TeX: {attachment['manifest']}, "
            f"chars [{attachment['char_start']},{attachment['char_end']}), "
            f"lines {attachment['line_start']}–{attachment['line_end']}. "
            f"Scope: {attachment['scope']}.\n"
        )
        if absence_note:
            text += absence_note + "\n"
        text += "Exact source excerpt:\n" + attachment["excerpt"]
        decision["readers"][role] = [text]
        provenance = {
            "source_attachment_pointer": pointer,
            "source_kind": "existing audited reader_tex_proposals attachment",
            "report_difference_entry_at_this_row": False,
            "excerpt_copied_verbatim": True,
        }
        if absence_note:
            provenance["source_representation_note"] = absence_note
        decision["public_reader_source_provenance"][role] = provenance
        changed_slots.append({
            "decision_id": decision["id"],
            "reader": role,
            "source_attachment_pointer": pointer,
            "manifest": attachment["manifest"],
            "char_start": attachment["char_start"],
            "char_end": attachment["char_end"],
            "scope": attachment["scope"],
        })

assert len(changed_slots) == 31
record["public_reader_display_repair"] = {
    "status": "Source-only public reader completion; root approval pending.",
    "record_before_repair_sha256": EXPECTED_RECORD,
    "prior_source_audit": "checks/scan017_source_audit.md",
    "prior_source_audit_sha256": PRIOR_AUDIT,
    "repair_note": "checks/scan017_public_reader_repair.md",
    "original_mapping_field": "decisions[].readers_report_only",
    "source_provenance_field": "decisions[].public_reader_source_provenance",
    "changed_public_rows": len(actual_missing),
    "added_public_reader_slots": len(changed_slots),
    "public_rows_with_A_B_C": 56,
    "new_source_spans": 0,
    "new_source_or_image_audit": False,
    "scope": (
        "Only missing public reader slots are filled from existing audited "
        "reader_tex_proposals attachment.excerpt and scope. Original report "
        "mappings and all pre-existing entries remain verbatim. Representation "
        "absence is stated only within the recorded source scope. All prior "
        "ink choices, counts, raw sources, source attachments and approval "
        "states remain unchanged."
    ),
    "changed_slots": changed_slots,
}

# One narrow in-memory structural check: remove only this authorized repair,
# then recover the entire pre-repair object exactly.
recovered = deepcopy(record)
del recovered["public_reader_display_repair"]
for before, after, restored in zip(original["decisions"], record["decisions"], recovered["decisions"]):
    assert after["readers_report_only"] == before["readers"]
    for role, value in before["readers"].items():
        assert after["readers"][role] == value
    assert all(after["readers"].get(role) for role in "ABC")
    restored["readers"] = restored.pop("readers_report_only")
    restored.pop("public_reader_source_provenance", None)
assert recovered == original
assert record["main_adjudicated"] is False
assert all(d["main_approved"] is False for d in record["decisions"])

final_bytes = (json.dumps(record, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
record_after = sha256(final_bytes).hexdigest()
note = [
    "# Scan017 — public reader display repair",
    "",
    "Root's approval gate found 31 missing public reader slots on 17 decision rows. "
    "All 31 slots had an already-audited `reader_tex_proposals` attachment. "
    "This repair copies each exact excerpt and its recorded scope into the "
    "public `readers` field, with a source reference. The eight source-absence "
    "notes stay within those existing spans.",
    "",
    "Every original mapping is preserved verbatim as "
    "`decisions[].readers_report_only`; every pre-existing public reading is "
    "unchanged. The added source pointers are retained in "
    "`decisions[].public_reader_source_provenance`. All 56 decisions now "
    "account for A, B and C. No unanimity has been inferred.",
    "",
    f"- Record before repair: `{EXPECTED_RECORD}`.",
    f"- Record after display repair: `{record_after}`.",
    f"- Original source audit, before its authorized addendum: `{PRIOR_AUDIT}`.",
    f"- Selected TeX remains: `{record['root_selected_source_sha256']}`.",
    f"- Selected source map remains: `{record['source_attachment_map_sha256']}`.",
    "- Counts remain C 22 / H 33; 56 decisions, 18 doubts, 39 inventory entries.",
    "- Original approval states remain false; root approval is pending.",
    "",
    "## Exact existing source references",
    "",
    "Pointers below are within `scan017_record_draft.json`; character intervals "
    "and scopes are copied from the existing attachments. No source file was "
    "opened or recalculated for this repair.",
    "",
    "| Decision | Added reader | Existing attachment pointer | Source interval | Recorded scope |",
    "| --- | --- | --- | --- | --- |",
]
for slot in changed_slots:
    note.append(
        f"| {slot['decision_id']} | {slot['reader']} | "
        f"`{slot['source_attachment_pointer']}` | "
        f"`{slot['manifest']} [{slot['char_start']},{slot['char_end']})` | "
        f"{slot['scope']} |"
    )
note.extend([
    "",
    "## Narrow verification",
    "",
    "A single in-memory structural comparison restored the complete original "
    "record object after removing only the added metadata/provenance and "
    "restoring `readers_report_only`. It matched exactly. All original "
    "reader entries are unchanged, and every A/B/C public slot is populated. "
    "No reader file, selected TeX, selected map, count, ink decision, source "
    "attachment or approval state was changed. There was no repeated span "
    "audit, image inspection or mathematical computation.",
    "",
])

RECORD.write_bytes(final_bytes)
NOTE.write_text("\n".join(note), encoding="utf-8")
print(json.dumps({
    "record_sha256": record_after,
    "changed_rows": actual_missing,
    "added_slots": len(changed_slots),
    "repair_note": str(NOTE),
    "repair_note_sha256": sha256(NOTE.read_bytes()).hexdigest(),
}, ensure_ascii=False, indent=2))
