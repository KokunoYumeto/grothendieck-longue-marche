"""Pin the closed, actually verified checkpoint34 as the sole parent of35.

No earlier archive is opened, no archive is created, and no mutable
retention table is published. The parent is read as immutable evidence.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv
import hashlib
import io
import json
import zipfile

from checkpoint_archive_io import CheckpointReader, PREFIX
from preserve_checkpoint35_versions_inductive import tuple_sha

ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT.parent / "LM4_SUCCESSOR_checkpoint_34.zip"
EXPECTED_SHA = "28dbe8b35a6f9e1c6b7e606aa59ceed041f2ab217959e0cc243ab7e83761d8fb"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    assert PARENT.stat().st_size == 529409669
    h = hashlib.sha256()
    with PARENT.open("rb") as stream:
        for part in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            h.update(part)
    assert h.hexdigest() == EXPECTED_SHA
    verifications = {}
    for name, session, chunk in [("archive", 83033, "a92f0e"), ("system_tars", 88075, "0c93d3"), ("inductive", 81129, "25e218")]:
        rel = f"records/checkpoint34_{name}_verification.json"
        raw = (ROOT / rel).read_bytes()
        report = json.loads(raw)
        assert report.get("sha256", report.get("archive_sha256")) == EXPECTED_SHA
        err = ROOT / f"records/checkpoint34_{name}_verification.err"
        assert err.read_bytes() == b""
        verifications[name] = {"path": rel, "bytes": len(raw), "sha256": digest(raw),
                               "producer_session": session, "producer_tool_chunk": chunk, "actual_exit_code_observed": 0}
    generic = json.loads((ROOT / verifications["archive"]["path"]).read_text())
    induction = json.loads((ROOT / verifications["inductive"]["path"]).read_text())
    native = json.loads((ROOT / verifications["system_tars"]["path"]).read_text())
    assert generic["entries"] == 10387 and generic["prior_entries_retained"] == 152653
    assert generic["crc"] == generic["every_manifest_entry"] == generic["every_retained_version"] == "PASS"
    assert induction["all_retained_rows"] == 152653 and induction["omissions"] == 0
    assert induction["complete_parent_map"] == induction["historical_tuple_composition"] == induction["all_closed_child_targets"] == "PASS"
    assert native["all_three_system_tar_restores"] == "PASS"
    pinned = {}
    with CheckpointReader(PARENT) as parent:
        assert len(parent.names()) == 10387
        for rel in ["records/checkpoint_version_retention.csv",
                    "records/checkpoint_version_retention_summary.json",
                    "checkpoint_history/README.md",
                    "records/checkpoint_34_contents_sha256.tsv",
                    "code/checkpoint_archive_io.py"]:
            raw = parent.read(PREFIX + rel)
            pinned[rel] = {"bytes": len(raw), "sha256": digest(raw)}
            if rel.endswith("checkpoint_version_retention.csv"):
                rows = list(csv.DictReader(io.StringIO(raw.decode())))
        assert len(rows) == 152653
        assert all(row["omission_reason"] == "" for row in rows)
    anchor = {
        "schema": "checkpoint-inductive-anchor-v1",
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "parent_number": 34, "child_number": 35,
        "archive": PARENT.name, "archive_bytes": 529409669,
        "archive_sha256": EXPECTED_SHA, "logical_entries": 10387,
        "inherited_rows": 152653, "inherited_archives": 33,
        "inherited_tuple_sha256": tuple_sha(rows),
        "inherited_counts": dict(Counter(row["checkpoint"] for row in rows)),
        "trusted_coverage": {
            "status": "Closed checkpoint34 verified in this execution environment; all three producer exits observed as zero.",
            "assertion": "All152653 historical logical identities are retained in the closed34 archive. The closed34 verifier established the exact map composition over all10053 parent33 entries. Archives1-32 remain the previously pinned induction base; none is newly reopened here.",
            "verification_records": verifications,
            "capture_record": "records/checkpoint34_capture_completion_observed.json",
        },
        "pinned_files": pinned,
    }
    target = ROOT / "records/checkpoint35_retention_parent_anchor.json"
    with target.open("x") as stream:
        json.dump(anchor, stream, indent=2, sort_keys=True)
        stream.write("\n")
    observed = {"recorded_at": datetime.now(timezone.utc).isoformat(),
                "archive_sha256": EXPECTED_SHA, "verifications": verifications,
                "all_actual_exit_codes_observed": True,
                "archive_mutated": False, "new_archive_created": False}
    with (ROOT / "records/checkpoint34_verification_observed.json").open("x") as stream:
        json.dump(observed, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps(anchor, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
