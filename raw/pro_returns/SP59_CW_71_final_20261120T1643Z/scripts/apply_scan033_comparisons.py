#!/usr/bin/env python3
"""Apply the primary reader's approved scan033 comparison bookkeeping only.

The approved proposal remains immutable. This module also supplies the guarded
in-memory step used by read033.py. No image or ink decision is made here.
"""

from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(OUT / "scripts"))
import records
import package as package_tools
from apply_exact_fragment_replacements import (
    atomic_write, count_state, read_rows, row_hash, sha, table_bytes,
)

PROPOSAL = OUT / "metadata" / "scan033_comparison_replacements_proposed.tsv"
PROPOSAL_SHA256 = "7c475fddf7a8ea3675c161c9b037790a447bfa332a8d8b1e77a2b3e7bbc86444"
GLYPH_HASHES = {
    "71-033-001": "2e3df204d28c669d180124a0bbe31a57fac32ded175713537d97bb64c6d6905f",
    "71-033-002": "fc4f11e443820674245437ffea588f84a94224ec46f3fc106a0755cd41a90689",
    "71-033-003": "37801a8ca4cbc940ae844639580bfe62a0d20be6a63cfdfaec6062a8d5413275",
}
OLD_SCOPE = "certainty or symbol differences against C are recorded in their own C-only rows."
NEW_SCOPE = "certainty or symbol differences against C are recorded separately; the three excluded glyph rows also record H omissions."


def proposals():
    if sha(PROPOSAL.read_bytes()) != PROPOSAL_SHA256:
        raise RuntimeError("The reviewed scan033 proposal has changed")
    _, rows = read_rows(PROPOSAL)
    if [r["id"] for r in rows] != [f"71-033-{i:03d}" for i in range(12, 20)]:
        raise RuntimeError("Unexpected scan033 proposal IDs")
    return rows


def canonical(source, ordinal):
    row = dict(source)
    defaults = dict(id=f"71-033-{ordinal:03d}", confidence="medium",
                    diff_C=False, diff_H=False, kind="other", error_kind="Other",
                    marked_H="no", consequential="", S_id="")
    for key, value in defaults.items():
        row.setdefault(key, value)
    if set(row) - set(records.CHANGE_FIELDS):
        raise RuntimeError("Unexpected change-row field")
    return {key: ("yes" if row.get(key) is True else "no" if row.get(key) is False
                  else str(row.get(key, "") or "")) for key in records.CHANGE_FIELDS}


def clean_evidence(value):
    return value.replace("[Proposed scope clarification] ", "").replace(OLD_SCOPE, NEW_SCOPE)


def approved_rows(changes, tex):
    """Return approved rows, refusing altered scopes or changed page text."""
    proposed = proposals()
    digest = sha((tex.rstrip() + "\n").encode("utf-8"))
    if any(p["source_final_sha256"] != digest for p in proposed):
        raise RuntimeError("Scan033 page changed since comparison approval; review its fragments")
    result = [canonical(row, i) for i, row in enumerate(changes, 1)]
    by_id = {row["id"]: row for row in result}
    if len(by_id) != len(result):
        raise RuntimeError("Duplicate scan033 row IDs")
    for p in proposed:
        row = by_id[p["id"]]
        original = dict(row, C=p["old_C"], final=p["old_final"], scan_shows=p["old_scan_shows"])
        if row_hash(original) != p["original_row_sha256"]:
            raise RuntimeError("Protected original-row fields changed: " + p["id"])
        # The already-authorized in/A syntax safeguard runs before extraction.
        allowed_C = {p["old_C"], p["old_C"].replace(r"\inA.", r"\in A."), p["new_C"]}
        allowed_final = {p["old_final"], p["old_final"].replace(r"\inA.", r"\in A."), p["new_final"]}
        evidence = clean_evidence(p["new_scan_shows"])
        if (row["C"] not in allowed_C or row["final"] not in allowed_final
                or row["scan_shows"] not in {p["old_scan_shows"], clean_evidence(p["old_scan_shows"]), evidence}):
            raise RuntimeError("Unreviewed comparison-cell change: " + p["id"])
        row.update(C=p["new_C"], final=p["new_final"], scan_shows=evidence)
    for identifier, expected_hash in GLYPH_HASHES.items():
        row = by_id[identifier]
        original = dict(row, diff_H="no", kind="misread symbol or index")
        if row_hash(original) != expected_hash:
            raise RuntimeError("Protected glyph row changed: " + identifier)
        if (row["diff_H"], row["kind"]) not in {("no", "misread symbol or index"), ("yes", "omission")}:
            raise RuntimeError("Unreviewed glyph classification: " + identifier)
        row.update(diff_H="yes", kind="omission")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    validation = package_tools.validate()
    if validation["errors"]:
        raise RuntimeError("Preflight errors: " + "; ".join(validation["errors"]))
    table_path = OUT / "records" / "scan033" / "changes.tsv"
    original_bytes = table_path.read_bytes()
    _, old_rows = read_rows(table_path, records.CHANGE_FIELDS)
    page = OUT / "pages" / records.page_name(33)
    page_bytes = page.read_bytes()
    new_rows = approved_rows(old_rows, page_bytes.decode("utf-8"))
    changed = [(old, new) for old, new in zip(old_rows, new_rows) if old != new]
    print(f"Scan033: {len(changed)} rows require the approved updates.")
    if not args.apply:
        print("Read-only preview; use --apply only after primary-reader authorization.")
        return
    if not changed:
        print("Already applied exactly; no files changed.")
        return
    expected_ids = set(GLYPH_HASHES) | {f"71-033-{i:03d}" for i in range(12, 20)}
    if {old["id"] for old, _ in changed} != expected_ids:
        raise RuntimeError("Partially applied state requires review before writing")
    combined = OUT / f"{records.PREFIX}_transcription.tex"
    combined_bytes = combined.read_bytes()
    before_counts = count_state()
    script = OUT / "scripts" / "read033.py"
    script_before = script.read_bytes()
    body = script_before.decode("utf-8")
    old_glyph = "diff_C=True,kind='misread symbol or index',error_kind='Symbols and indices')"
    if body.count(old_glyph) != 1 or body.count("items=[]") != 1:
        raise RuntimeError("Unexpected read033 safeguard anchors")
    body = body.replace(old_glyph, "diff_C=True,diff_H=True,kind='omission',error_kind='Symbols and indices')")
    body = body.replace(OLD_SCOPE, NEW_SCOPE)
    body = body.replace("items=[]", "# Preserve the approved exact comparisons and separate glyph omissions.\nfrom apply_scan033_comparisons import approved_rows\ncs = approved_rows(cs, t)\nitems=[]")
    ast.parse(body)
    now = records.utc_now()
    application = OUT / "metadata" / "scan033_comparison_applications.tsv"
    if application.exists():
        raise RuntimeError("Scan033 application history already exists for an unapplied state")
    fields = ["date_utc", "id", "proposal_sha256", "source_final_sha256", "old_row_sha256", "new_row_sha256", "changed_fields"]
    history = [{"date_utc": now, "id": old["id"], "proposal_sha256": PROPOSAL_SHA256,
                "source_final_sha256": sha(page_bytes), "old_row_sha256": row_hash(old),
                "new_row_sha256": row_hash(new),
                "changed_fields": ";".join(k for k in records.CHANGE_FIELDS if old[k] != new[k])}
               for old, new in changed]
    log_path = OUT / "MECHANICAL_REPAIRS.tsv"
    log_fields, logs = read_rows(log_path, ["path", "before_sha256", "after_sha256", "date_utc"])
    writes = {table_path: table_bytes(records.CHANGE_FIELDS, new_rows), script: body.encode("utf-8")}
    for path, data in writes.items():
        logs.append({"path": str(path.relative_to(OUT)), "before_sha256": sha(path.read_bytes()),
                     "after_sha256": sha(data), "date_utc": now})
    if table_path.read_bytes() != original_bytes or page.read_bytes() != page_bytes or script.read_bytes() != script_before:
        raise RuntimeError("Concurrent scan033 edit detected")
    for path, data in writes.items():
        atomic_write(path, data)
    atomic_write(application, table_bytes(fields, history))
    atomic_write(log_path, table_bytes(log_fields, logs))
    records.build()
    expected_counts = dict(before_counts, against_H=before_counts["against_H"] + 3)
    if count_state() != expected_counts:
        raise RuntimeError("Unexpected count delta after scan033 changes")
    if page.read_bytes() != page_bytes or combined.read_bytes() != combined_bytes:
        raise RuntimeError("Unexpected transcription mutation")
    validation = package_tools.validate()
    if validation["errors"]:
        raise RuntimeError("Post-application errors: " + "; ".join(validation["errors"]))
    records.log_event(f"mechanical scan033 comparison repair {now}; eight approved main-block comparisons and three individual H glyph omissions; H +3, C and distinct places unchanged; no page-text changes")
    print("Applied approved comparisons; H +3, C and distinct places unchanged.")
    print("Page and consolidated transcription bytes unchanged.")
    print(f"Validation: {len(validation['errors'])} errors; {len(validation['warnings'])} warnings.")
    print("Counts:", count_state())


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, ValueError, KeyError) as exc:
        print("ERROR:", exc, file=sys.stderr)
        sys.exit(1)
