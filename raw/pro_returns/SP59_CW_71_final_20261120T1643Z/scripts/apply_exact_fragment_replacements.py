#!/usr/bin/env python3
"""Review/apply the separately reviewed 23-cell exact-fragment proposal.

Default invocation is read-only. --apply is required for mutation. The script
reads consolidated text and record tables only: no images, witnesses, OCR,
mathematical checking, or TeX compilation. It changes only approved final cells.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(OUT / "scripts"))
import records
import package as package_tools

PROPOSAL = OUT / "metadata" / "exact_fragment_replacements_proposed.tsv"
EXPECTED_IDS = {
    "71-025-027",
    *{f"71-027-{n:03d}" for n in range(18, 26)},
    *{f"71-029-{n:03d}" for n in range(18, 23)},
    *{f"71-031-{n:03d}" for n in range(11, 20)},
}
REQUIRED_PROPOSAL_FIELDS = {
    "scan", "id", "place", "old_final", "new_final", "exclusions",
    "source_file", "source_start_anchor", "source_end_anchor",
    "original_row_sha256", "source_sha256", "diff_C", "diff_H",
    "kind", "error_kind", "confidence",
}
APPLICATION_FIELDS = [
    "date_utc", "proposal_sha256", "id", "source_file", "source_sha256",
    "old_final_sha256", "new_final_sha256", "old_row_sha256", "new_row_sha256",
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def row_hash(row):
    return sha("\0".join(row[field] for field in records.CHANGE_FIELDS).encode("utf-8"))


def read_rows(path, fields=None):
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        if fields is not None and reader.fieldnames != fields:
            raise RuntimeError(f"Unexpected table schema: {path.relative_to(OUT)}")
        header = reader.fieldnames or []
        rows = list(reader)
    if any(None in row or any(value is None for value in row.values()) for row in rows):
        raise RuntimeError(f"Malformed table: {path.relative_to(OUT)}")
    return header, rows


def table_bytes(fields, rows):
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def atomic_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".exact-fragments.tmp")
    with temporary.open("wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(temporary, path)


def count_state():
    pages = records.load_records()
    changes = [row for page in pages for row in page["changes"]]
    return {
        "pages": len(pages),
        "against_C": sum(records.as_bool(row["diff_C"]) for row in changes),
        "against_H": sum(records.as_bool(row["diff_H"]) for row in changes),
        "changed_places": sum(records.as_bool(row["diff_C"]) or records.as_bool(row["diff_H"]) for row in changes),
        "inventory_rows": sum(len(page["inventory"]) for page in pages),
        "check_events": sum(len(page["checks"]) for page in pages),
    }


def prepare():
    proposal_bytes = PROPOSAL.read_bytes()
    header, proposals = read_rows(PROPOSAL)
    if set(header) != REQUIRED_PROPOSAL_FIELDS:
        raise RuntimeError("Proposal columns differ from the reviewed schema")
    identifiers = [r["id"] for r in proposals]
    if len(identifiers) != 23 or len(set(identifiers)) != 23 or set(identifiers) != EXPECTED_IDS:
        raise RuntimeError("This script is limited to the reviewed 23 IDs; it will not apply a wider proposal")
    validation = package_tools.validate()
    if validation["errors"]:
        raise RuntimeError("Preflight structural errors: " + "; ".join(validation["errors"]))

    inputs = {PROPOSAL: proposal_bytes}
    tables = {}
    pending = []
    already = []
    source_hashes = {}
    for p in proposals:
        scan = int(p["scan"])
        expected_source = OUT / "pages" / records.page_name(scan)
        supplied_source = OUT / p["source_file"]
        if supplied_source.resolve() != expected_source.resolve():
            raise RuntimeError(f"Incorrect source mapping for {p['id']}")
        source_bytes = expected_source.read_bytes()
        if sha(source_bytes) != p["source_sha256"]:
            raise RuntimeError(f"Source page changed after proposal: scan {scan:03d}; review/regenerate its proposed fragments")
        inputs[expected_source] = source_bytes
        source_hashes[expected_source] = p["source_sha256"]

        table_path = records.record_dir(scan) / "changes.tsv"
        if table_path not in tables:
            inputs[table_path] = table_path.read_bytes()
            _, tables[table_path] = read_rows(table_path, records.CHANGE_FIELDS)
        matches = [row for row in tables[table_path] if row["id"] == p["id"]]
        if len(matches) != 1:
            raise RuntimeError(f"Expected one target row for {p['id']}")
        row = matches[0]
        if not p["new_final"].strip():
            raise RuntimeError(f"Empty proposed replacement for {p['id']}")
        for field in ("place", "diff_C", "diff_H", "kind", "error_kind", "confidence"):
            if row[field] != p[field]:
                raise RuntimeError(f"Protected {field} changed for {p['id']}; the proposal cannot alter its scope/classification")

        # Restore the proposal's original final cell before hashing. This admits
        # exactly two states: untouched original or this exact proposal applied.
        restored = dict(row)
        restored["final"] = p["old_final"]
        if row_hash(restored) != p["original_row_sha256"]:
            raise RuntimeError(f"Target row changed after proposal: {p['id']}")
        if row["final"] == p["new_final"]:
            already.append(p["id"])
            continue
        if row["final"] != p["old_final"] or row_hash(row) != p["original_row_sha256"]:
            raise RuntimeError(f"Final cell independently changed for {p['id']}")
        before = dict(row)
        row["final"] = p["new_final"]
        # Every field except final must be byte-for-byte unchanged.
        if any(row[k] != before[k] for k in records.CHANGE_FIELDS if k != "final"):
            raise RuntimeError(f"Unexpected non-final mutation planned for {p['id']}")
        pending.append((p, before, dict(row)))

    writes = {}
    for path, rows in tables.items():
        data = table_bytes(records.CHANGE_FIELDS, rows)
        if data != inputs[path]:
            writes[path] = data

    history_path = OUT / "metadata" / "exact_fragment_applications.tsv"
    if history_path.exists():
        inputs[history_path] = history_path.read_bytes()
        _, history = read_rows(history_path, APPLICATION_FIELDS)
    else:
        history = []
    combined = OUT / f"{records.PREFIX}_transcription.tex"
    inputs[combined] = combined.read_bytes()
    return {
        "inputs": inputs, "writes": writes, "pending": pending, "already": already,
        "history": history, "history_path": history_path,
        "source_hashes": source_hashes, "proposal_sha256": sha(proposal_bytes),
        "before_counts": count_state(), "combined": combined,
    }


def apply(plan):
    if not plan["pending"]:
        if plan["writes"]:
            raise RuntimeError("Unexpected serialization-only writes in an already applied plan")
        print("All 23 replacements are already applied exactly; no files or log entries changed.")
        return
    for path, data in plan["inputs"].items():
        if path.read_bytes() != data:
            raise RuntimeError(f"Concurrent edit detected: {path.relative_to(OUT)}")
    timestamp = records.utc_now()
    history = list(plan["history"])
    for proposed, before, after in plan["pending"]:
        history.append({
            "date_utc": timestamp,
            "proposal_sha256": plan["proposal_sha256"],
            "id": proposed["id"],
            "source_file": proposed["source_file"],
            "source_sha256": proposed["source_sha256"],
            "old_final_sha256": sha(before["final"].encode("utf-8")),
            "new_final_sha256": sha(after["final"].encode("utf-8")),
            "old_row_sha256": row_hash(before),
            "new_row_sha256": row_hash(after),
        })
    for path, data in plan["writes"].items():
        atomic_write(path, data)
    atomic_write(plan["history_path"], table_bytes(APPLICATION_FIELDS, history))
    records.build()
    if count_state() != plan["before_counts"]:
        raise RuntimeError("Counts unexpectedly changed after final-cell-only replacements")
    for path, expected in plan["source_hashes"].items():
        if sha(path.read_bytes()) != expected:
            raise RuntimeError(f"Unexpected page mutation: {path.relative_to(OUT)}")
    if plan["combined"].read_bytes() != plan["inputs"][plan["combined"]]:
        raise RuntimeError("Combined transcription unexpectedly changed")
    validation = package_tools.validate()
    if validation["errors"]:
        raise RuntimeError("Post-application errors: " + "; ".join(validation["errors"]))
    records.log_event(f"mechanical exact-fragment comparison updates {timestamp}; {len(plan['pending'])} final cells; counts and transcription unchanged; no new ink decisions")
    print(f"Applied {len(plan['pending'])} final cells; {len(plan['already'])} were already applied.")
    print("All counts, page bytes, and combined-transcription bytes remain unchanged.")
    print(f"Validation errors: {len(validation['errors'])}; warnings: {len(validation['warnings'])}")
    for warning in validation["warnings"]:
        print("  " + warning)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Apply only after the primary reader authorizes the reviewed proposal")
    args = parser.parse_args()
    plan = prepare()
    print(f"Guarded proposal: {len(plan['pending'])} pending; {len(plan['already'])} already applied.")
    for proposed, _, _ in plan["pending"]:
        print("  " + proposed["id"] + " — " + proposed["place"])
    if args.apply:
        apply(plan)
    else:
        print("READ-ONLY PREVIEW. No files changed. --apply requires prior primary-reader authorization.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, ValueError) as exc:
        print("ERROR:", exc, file=sys.stderr)
        sys.exit(1)
