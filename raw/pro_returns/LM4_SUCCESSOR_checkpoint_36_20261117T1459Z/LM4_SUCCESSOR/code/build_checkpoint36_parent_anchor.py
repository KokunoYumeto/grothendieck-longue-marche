"""Pin the closed, actually verified checkpoint35 as the sole parent of36.

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
from preserve_checkpoint36_versions_inductive import tuple_sha

ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT.parent / "LM4_SUCCESSOR_checkpoint_35.zip"
EXPECTED_SHA = "33b0925ca3ba12d8944fc47243807a3c61ebb2a4f03ec47f7bb2ce1a5a83f121"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    assert PARENT.stat().st_size == 530938760
    h = hashlib.sha256()
    with PARENT.open("rb") as stream:
        for part in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            h.update(part)
    assert h.hexdigest() == EXPECTED_SHA
    verifications = {}
    for name, session, chunk in [("archive", 19472, "3e985f"), ("system_tars", 60334, "1a39d7"), ("inductive", 29713, "43e040")]:
        rel = f"records/checkpoint35_{name}_verification.json"
        raw = (ROOT / rel).read_bytes()
        report = json.loads(raw)
        assert report.get("sha256", report.get("archive_sha256")) == EXPECTED_SHA
        err = ROOT / f"records/checkpoint35_{name}_verification.err"
        assert err.read_bytes() == b""
        verifications[name] = {"path": rel, "bytes": len(raw), "sha256": digest(raw),
                               "producer_session": session, "producer_tool_chunk": chunk, "actual_exit_code_observed": 0}
    generic = json.loads((ROOT / verifications["archive"]["path"]).read_text())
    induction = json.loads((ROOT / verifications["inductive"]["path"]).read_text())
    native = json.loads((ROOT / verifications["system_tars"]["path"]).read_text())
    assert generic["entries"] == 10746 and generic["prior_entries_retained"] == 163040
    assert generic["crc"] == generic["every_manifest_entry"] == generic["every_retained_version"] == "PASS"
    assert induction["all_retained_rows"] == 163040 and induction["omissions"] == 0
    assert induction["complete_parent_map"] == induction["historical_tuple_composition"] == induction["all_closed_child_targets"] == "PASS"
    assert native["all_three_system_tar_restores"] == "PASS"
    observed_path = ROOT / "records/checkpoint35_verification_observed.json"
    observed_raw = observed_path.read_bytes()
    observed = json.loads(observed_raw)
    assert observed["all_actual_exit_codes_observed"] is True
    assert observed["archive_sha256"] == EXPECTED_SHA
    for role, evidence in verifications.items():
        for key, value in evidence.items():
            assert observed["verifications"][role][key] == value
    pinned = {}
    with CheckpointReader(PARENT) as parent:
        assert len(parent.names()) == 10746
        for rel in ["records/checkpoint_version_retention.csv",
                    "records/checkpoint_version_retention_summary.json",
                    "checkpoint_history/README.md",
                    "records/checkpoint_35_contents_sha256.tsv",
                    "code/checkpoint_archive_io.py"]:
            raw = parent.read(PREFIX + rel)
            pinned[rel] = {"bytes": len(raw), "sha256": digest(raw)}
            if rel.endswith("checkpoint_version_retention.csv"):
                rows = list(csv.DictReader(io.StringIO(raw.decode())))
        assert len(rows) == 163040
        assert all(row["omission_reason"] == "" for row in rows)
    anchor = {
        "schema": "checkpoint-inductive-anchor-v1",
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "parent_number": 35, "child_number": 36,
        "archive": PARENT.name, "archive_bytes": 530938760,
        "archive_sha256": EXPECTED_SHA, "logical_entries": 10746,
        "inherited_rows": 163040, "inherited_archives": 34,
        "inherited_tuple_sha256": tuple_sha(rows),
        "inherited_counts": dict(Counter(row["checkpoint"] for row in rows)),
        "trusted_coverage": {
            "status": "Closed checkpoint35 verified in this execution environment; all three producer exits observed as zero.",
            "assertion": "All163040 historical logical identities are retained in the closed35 archive. The closed35 verifier established the exact map composition over all10387 parent34 entries. Archives1-33 remain the previously pinned induction base; none is newly reopened here.",
            "verification_records": verifications,
            "verification_observation": {"path": str(observed_path.relative_to(ROOT)),
                "bytes": len(observed_raw), "sha256": digest(observed_raw)},
            "capture_record": "records/checkpoint35_capture_completion_observed.json",
        },
        "pinned_files": pinned,
    }
    target = ROOT / "records/checkpoint36_retention_parent_anchor.json"
    with target.open("x") as stream:
        json.dump(anchor, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps(anchor, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
