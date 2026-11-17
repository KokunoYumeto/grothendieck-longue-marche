"""Pin the closed, actually verified checkpoint33 as the sole parent of34.

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
from preserve_checkpoint34_versions_inductive import tuple_sha

ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT.parent / "LM4_SUCCESSOR_checkpoint_33.zip"
EXPECTED_SHA = "5c68edb5a023c97cb400b506f7e1b7303f19e3cac9212947491e47793d77ef96"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    assert PARENT.stat().st_size == 508499680
    h = hashlib.sha256()
    with PARENT.open("rb") as stream:
        for part in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            h.update(part)
    assert h.hexdigest() == EXPECTED_SHA
    verifications = {}
    for name, session in [("archive", 5195), ("system_tars", 28023), ("inductive", 66162)]:
        rel = f"records/checkpoint33_{name}_verification.json"
        raw = (ROOT / rel).read_bytes()
        report = json.loads(raw)
        assert report.get("sha256", report.get("archive_sha256")) == EXPECTED_SHA
        err = ROOT / f"records/checkpoint33_{name}_verification.err"
        assert err.read_bytes() == b""
        verifications[name] = {"path": rel, "bytes": len(raw), "sha256": digest(raw),
                               "producer_session": session, "actual_exit_code_observed": 0}
    generic = json.loads((ROOT / verifications["archive"]["path"]).read_text())
    induction = json.loads((ROOT / verifications["inductive"]["path"]).read_text())
    native = json.loads((ROOT / verifications["system_tars"]["path"]).read_text())
    assert generic["entries"] == 10053 and generic["prior_entries_retained"] == 142600
    assert generic["crc"] == generic["every_manifest_entry"] == generic["every_retained_version"] == "PASS"
    assert induction["all_retained_rows"] == 142600 and induction["omissions"] == 0
    assert induction["complete_parent_map"] == induction["historical_tuple_composition"] == induction["all_closed_child_targets"] == "PASS"
    assert native["all_three_system_tar_restores"] == "PASS"
    pinned = {}
    with CheckpointReader(PARENT) as parent:
        assert len(parent.names()) == 10053
        for rel in ["records/checkpoint_version_retention.csv",
                    "records/checkpoint_version_retention_summary.json",
                    "checkpoint_history/README.md",
                    "records/checkpoint_33_contents_sha256.tsv",
                    "code/checkpoint_archive_io.py"]:
            raw = parent.read(PREFIX + rel)
            pinned[rel] = {"bytes": len(raw), "sha256": digest(raw)}
            if rel.endswith("checkpoint_version_retention.csv"):
                rows = list(csv.DictReader(io.StringIO(raw.decode())))
        assert len(rows) == 142600
        assert all(row["omission_reason"] == "" for row in rows)
    anchor = {
        "schema": "checkpoint-inductive-anchor-v1",
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "parent_number": 33, "child_number": 34,
        "archive": PARENT.name, "archive_bytes": 508499680,
        "archive_sha256": EXPECTED_SHA, "logical_entries": 10053,
        "inherited_rows": 142600, "inherited_archives": 32,
        "inherited_tuple_sha256": tuple_sha(rows),
        "inherited_counts": dict(Counter(row["checkpoint"] for row in rows)),
        "trusted_coverage": {
            "status": "Closed checkpoint33 verified in this execution environment; all three producer exits observed as zero.",
            "assertion": "All142600 historical logical identities are retained in the closed33 archive. The closed33 verifier established the exact map composition over all9680 parent32 entries. Archives1-31 remain the previously pinned induction base; none is newly reopened here.",
            "verification_records": verifications,
            "capture_record": "records/checkpoint33_capture_completion_observed.json",
        },
        "pinned_files": pinned,
    }
    target = ROOT / "records/checkpoint34_retention_parent_anchor.json"
    with target.open("x") as stream:
        json.dump(anchor, stream, indent=2, sort_keys=True)
        stream.write("\n")
    observed = {"recorded_at": datetime.now(timezone.utc).isoformat(),
                "archive_sha256": EXPECTED_SHA, "verifications": verifications,
                "all_actual_exit_codes_observed": True,
                "archive_mutated": False, "new_archive_created": False}
    with (ROOT / "records/checkpoint33_verification_observed.json").open("x") as stream:
        json.dump(observed, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps(anchor, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
