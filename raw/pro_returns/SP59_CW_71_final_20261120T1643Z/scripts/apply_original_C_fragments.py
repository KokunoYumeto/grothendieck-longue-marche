#!/usr/bin/env python3
"""Apply the root-approved 48 C cells, preserving frozen transcription bytes.

Default invocation is a guarded read-only preview. --apply changes only C
comparison cells and application documentation, then rebuilds exactly once.
No first-reading script is executed and no page-done/audit event is added.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parents[1]
ROOT = OUT.parent
sys.path.insert(0, str(OUT / "scripts"))
import records
import package as package_tools
from apply_exact_fragment_replacements import (
    atomic_write, count_state, read_rows, row_hash, sha, table_bytes,
)

PROPOSAL = OUT / "metadata" / "original_C_fragment_replacements_proposed.tsv"
APPROVED_SHA256 = "4b928bf81cbd0cea2562b37dc07f86d6764ce3b964dfd1519e670dbb32c40caf"
EXPECTED_IDS = {
    "71-023-011",
    *{f"71-023-{i:03d}" for i in range(18, 28)},
    *{f"71-025-{i:03d}" for i in range(20, 29)},
    *{f"71-027-{i:03d}" for i in range(17, 27)},
    *{f"71-029-{i:03d}" for i in range(17, 26)},
    *{f"71-031-{i:03d}" for i in range(11, 20)},
}
LEDGER_FIELDS = [
    "approval_recorded_utc", "applied_utc", "approved_by", "approval_source",
    "proposal_sha256", "scan", "id", "source_C_file", "source_C_sha256",
    "final_sha256", "old_C_sha256", "new_C_sha256", "old_row_sha256", "new_row_sha256",
]


def prepare():
    data = PROPOSAL.read_bytes()
    if sha(data) != APPROVED_SHA256:
        raise RuntimeError("Proposal differs from the 48-cell TSV approved by root")
    _, proposals = read_rows(PROPOSAL)
    if len(proposals) != 48 or {p["id"] for p in proposals} != EXPECTED_IDS:
        raise RuntimeError("Unexpected proposal coverage")
    validation = package_tools.validate(complete=True, require_audits=True)
    if validation["errors"]:
        raise RuntimeError("Preflight errors: " + "; ".join(validation["errors"]))
    if package_tools.verify_frozen(log=False) != 26:
        raise RuntimeError("Expected 26 frozen transcription files")
    inputs = {PROPOSAL: data}
    tables = {}
    pending = []
    already = []
    for p in proposals:
        scan = int(p["scan"])
        expected_source = ROOT / "source/SP59_CW_71_witnesses/codex" / records.FOLDERS[scan] / "pages" / records.page_name(scan)
        source_path = ROOT / p["source_C_file"]
        if source_path.resolve() != expected_source.resolve():
            raise RuntimeError("Unexpected source path for " + p["id"])
        source_bytes = source_path.read_bytes()
        if sha(source_bytes) != p["source_C_sha256"]:
            raise RuntimeError("Original source C changed: " + p["id"])
        inputs[source_path] = source_bytes
        table_path = records.record_dir(scan) / "changes.tsv"
        if table_path not in tables:
            inputs[table_path] = table_path.read_bytes()
            _, tables[table_path] = read_rows(table_path, records.CHANGE_FIELDS)
        matches = [row for row in tables[table_path] if row["id"] == p["id"]]
        if len(matches) != 1:
            raise RuntimeError("Expected one target row: " + p["id"])
        row = matches[0]
        if sha(row["final"].encode("utf-8")) != p["final_sha256"]:
            raise RuntimeError("Final comparison changed: " + p["id"])
        for field in ("place", "diff_C", "diff_H", "kind", "error_kind", "confidence"):
            if row[field] != p[field]:
                raise RuntimeError("Protected field changed: " + p["id"] + "/" + field)
        restored = dict(row, C=p["old_C"])
        if row_hash(restored) != p["original_row_sha256"]:
            raise RuntimeError("Protected original-row content changed: " + p["id"])
        if row["C"] == p["new_C"]:
            already.append(p["id"])
        elif row["C"] == p["old_C"] and row_hash(row) == p["original_row_sha256"]:
            before = dict(row)
            row["C"] = p["new_C"]
            if not row["C"].strip() or any(row[k] != before[k] for k in records.CHANGE_FIELDS if k != "C"):
                raise RuntimeError("Unexpected row mutation planned: " + p["id"])
            pending.append((p, before, dict(row)))
        else:
            raise RuntimeError("C comparison independently changed: " + p["id"])
    for path in package_tools.transcription_paths():
        inputs[path] = path.read_bytes()
    inputs[OUT / package_tools.FROZEN_NAME] = (OUT / package_tools.FROZEN_NAME).read_bytes()
    return inputs, tables, pending, already, count_state()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    inputs, tables, pending, already, before_counts = prepare()
    print(f"Guarded original-C proposal: {len(pending)} pending; {len(already)} already applied.")
    if not args.apply:
        print("Read-only preview; no files changed.")
        return
    if not pending:
        print("All approved cells already match exactly; no rebuild or log entry added.")
        return
    if len(pending) != 48 or already:
        raise RuntimeError("Partial application state requires review")
    ledger_path = OUT / "metadata" / "original_C_fragment_applications.tsv"
    if ledger_path.exists():
        raise RuntimeError("Application ledger already exists for an unapplied state")
    for path, data in inputs.items():
        if path.read_bytes() != data:
            raise RuntimeError("Concurrent edit detected: " + str(path))
    now = records.utc_now()
    ledger = []
    for p, before, after in pending:
        ledger.append({
            "approval_recorded_utc": now, "applied_utc": now,
            "approved_by": "root / sole primary reader",
            "approval_source": "Conversation authorization approving all 48 new_C cells unchanged and identifying the proposal SHA256",
            "proposal_sha256": APPROVED_SHA256, "scan": p["scan"], "id": p["id"],
            "source_C_file": p["source_C_file"], "source_C_sha256": p["source_C_sha256"],
            "final_sha256": p["final_sha256"],
            "old_C_sha256": sha(before["C"].encode("utf-8")),
            "new_C_sha256": sha(after["C"].encode("utf-8")),
            "old_row_sha256": row_hash(before), "new_row_sha256": row_hash(after),
        })
    repair_path = OUT / "MECHANICAL_REPAIRS.tsv"
    repair_fields, repairs = read_rows(repair_path, ["path", "before_sha256", "after_sha256", "date_utc"])
    for path, rows in tables.items():
        data = table_bytes(records.CHANGE_FIELDS, rows)
        repairs.append({"path": str(path.relative_to(OUT)), "before_sha256": sha(inputs[path]), "after_sha256": sha(data), "date_utc": now})
        atomic_write(path, data)
    atomic_write(ledger_path, table_bytes(LEDGER_FIELDS, ledger))
    atomic_write(repair_path, table_bytes(repair_fields, repairs))
    # This is the sole aggregate rebuild in an application run.
    records.build()
    if count_state() != before_counts:
        raise RuntimeError("Counts changed after C-cell-only replacements")
    for path in package_tools.transcription_paths():
        if path.read_bytes() != inputs[path]:
            raise RuntimeError("Frozen transcription bytes changed: " + path.name)
    if package_tools.verify_frozen(log=False) != 26:
        raise RuntimeError("Frozen verification count changed")
    validation = package_tools.validate(complete=True, require_audits=True)
    if validation["errors"]:
        raise RuntimeError("Post-application errors: " + "; ".join(validation["errors"]))
    records.log_event(f"mechanical original-C comparison updates {now}; 48 C cells approved unchanged; flags, scopes, counts and 26 frozen transcription files unchanged; rebuilt once")
    print("Applied exactly 48 C cells; aggregate rebuilds: 1.")
    print("Counts unchanged:", count_state())
    print("All 26 frozen transcription hashes unchanged.")
    print(f"Validation: {len(validation['errors'])} errors; {len(validation['warnings'])} warnings.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, ValueError, KeyError) as exc:
        print("ERROR:", exc, file=sys.stderr)
        sys.exit(1)
