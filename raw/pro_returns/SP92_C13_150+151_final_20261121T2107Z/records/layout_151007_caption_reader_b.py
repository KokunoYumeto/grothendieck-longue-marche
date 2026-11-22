#!/usr/bin/env python3
"""Apply root's exact representation-only caption-node layout substitution."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path

W = Path("/workspace/scratch/d7279cb02214/SP92_C13_150+151_work")
OLD = r"\node[anchor=west] at (14.0,-5.10)"
NEW = r"\node[anchor=north west,font=\tiny] at (14.0,-4.90)"
text_files = ["pages/151_scan007.tex", "records/151_scan007.tex"]
json_files = [
    "records/151_scan007.json",
    "second/151_scan007_root_crop_notes.json",
    "second/151_scan007_adjudications.json",
]
protected_files = [
    "second/151_scan007_first.tsv", "second/151_scan007_second.tsv",
    "second/151_scan007_boxes.tsv", "records/audit_151_scan007.py",
    "records/151_scan007_root_audit_observations.md",
]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


protected_hashes = {p: digest(W / p) for p in protected_files}
staged = []
edits = []
for rel in text_files:
    path = W / rel
    raw = path.read_bytes()
    old = raw.decode()
    assert old.count(OLD) == 1, rel
    new = old.replace(OLD, NEW)
    assert new.replace(NEW, OLD) == old
    staged.append((rel, raw, new.encode()))
    edits.append(dict(file=rel, path=None, replacements=1, before=OLD, after=NEW))

expected_paths = {
    "records/151_scan007.json": [
        ["changes", 33, "final"], ["audit_changes", 5, "final"],
        ["audit_changes", 6, "final"]],
    "second/151_scan007_root_crop_notes.json": [
        ["B24", "final"], ["B25", "final"]],
    "second/151_scan007_adjudications.json": [
        ["adjudications", 23, "final"], ["adjudications", 24, "final"]],
}


def value_at(obj, path):
    for key in path:
        obj = obj[key]
    return obj


for rel in json_files:
    path = W / rel
    raw = path.read_bytes()
    original = json.loads(raw)
    current = deepcopy(original)
    for field_path in expected_paths[rel]:
        old = value_at(current, field_path)
        assert isinstance(old, str) and old.count(OLD) == 1, (rel, field_path)
        new = old.replace(OLD, NEW)
        assert new.replace(NEW, OLD) == old
        value_at(current, field_path[:-1])[field_path[-1]] = new
        edits.append(dict(file=rel, path=field_path, replacements=1,
                          before=OLD, after=NEW))
    restored = deepcopy(current)
    for field_path in expected_paths[rel]:
        value_at(restored, field_path[:-1])[field_path[-1]] = value_at(original, field_path)
    assert restored == original, "A non-authorized final field changed."
    encoded = (json.dumps(current, ensure_ascii=False, indent=2) + "\n").encode()
    assert json.loads(encoded) == current
    staged.append((rel, raw, encoded))

assert len(edits) == 9
for rel, raw, _ in staged:
    assert (W / rel).read_bytes() == raw, ("Concurrent edit", rel)
file_changes = []
for rel, raw, encoded in staged:
    (W / rel).write_bytes(encoded)
    assert (W / rel).read_bytes() == encoded
    file_changes.append(dict(file=rel,
                             sha256_before=sha256(raw).hexdigest(),
                             sha256_after=sha256(encoded).hexdigest()))
assert (W / text_files[0]).read_bytes() == (W / text_files[1]).read_bytes()
for rel, expected in protected_hashes.items():
    assert digest(W / rel) == expected, rel
record = json.loads((W / "records/151_scan007.json").read_text())
page = (W / text_files[0]).read_text()
assert len(record["changes"]) == 45
assert record["audit_differing_boxes"] == 29 and record["audit_changed_boxes"] == 8
assert next(c["final"] for c in record["changes"] if c["id"] == "C34") in page

log = {
    "task": "Representation-only caption layout encoding for current 151_scan007",
    "reader": "/root/reader_b", "model": "GPT-6 Astra Pro",
    "effort": "not exposed", "run": "SP92",
    "utc": datetime.now(timezone.utc).isoformat(),
    "authority": "Root's explicit exact-substitution instruction after the metadata pass.",
    "reason": "Use a tiny font and top-left anchor for the three-line caption, with root's specified y position, to avoid the adjacent cancelled id-like entry.",
    "before": OLD, "after": NEW, "edits": edits, "files": file_changes,
    "classification": "layout encoding only; not a manuscript reading correction",
    "protected_files_sha256": protected_hashes,
    "checks": {
        "exactly_9_substitutions": True,
        "two_current_tex_files_identical": True,
        "only_7_authorized_current_final_fields_modified_in_JSON": True,
        "replacement_reversible_to_original_text_exactly": True,
        "reading_text_unchanged": True,
        "original_audit_first_second_and_sealed_tsvs_unchanged": True,
        "historical_scripts_observations_second_boxes_unchanged": True,
        "all_45_rows_and_count_flags_unchanged": True,
        "audit_29_differing_and_8_changed_boxes_unchanged": True,
        "C34_final_matches_current_page": True,
        "no_images_or_new_readings": True,
        "no_compilation_or_assembly": True,
    },
}
log_path = W / "records/layout_151007_caption_reader_b.json"
log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"log": str(log_path), "substitutions": 9, "checks": "passed"}))
