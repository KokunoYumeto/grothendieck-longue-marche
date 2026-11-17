"""Record root-observed closed34 verification and successful one-shot delivery.

The process exits and chunks below were actually observed by root. This
postclosure record belongs to35 and creates or modifies no archive.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = "28dbe8b35a6f9e1c6b7e606aa59ceed041f2ab217959e0cc243ab7e83761d8fb"


def identity(path):
    raw = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


def main():
    checks = []
    for name, session, chunk in [
        ("archive", 83033, "a92f0e"),
        ("system_tars", 88075, "0c93d3"),
        ("inductive", 81129, "25e218"),
    ]:
        path = ROOT / f"records/checkpoint34_{name}_verification.json"
        report = json.loads(path.read_text())
        assert report.get("sha256", report.get("archive_sha256")) == EXPECTED
        assert path.with_suffix(".err").read_bytes() == b""
        checks.append({**identity(path), "actual_session": session,
                       "actual_exit": 0, "observed_exit_chunk": chunk,
                       "report": report})
    out = ROOT / "records/checkpoint34_library_save.out"
    err = ROOT / "records/checkpoint34_library_save.err"
    saved = json.loads(out.read_text())["results"]
    assert len(saved) == 1
    saved = saved[0]
    assert saved["status"] == "succeeded"
    assert saved["file_name"] == "LM4_SUCCESSOR_checkpoint_34.zip"
    prefix = "__OPENAI_LIBRARY_FILE_WRITE_RECEIPT_V1__="
    assert err.read_text().startswith(prefix)
    receipt = json.loads(err.read_text()[len(prefix):])
    assert receipt["file_id"] == saved["file_id"]
    assert receipt["library_file_id"] == saved["library_file_id"]
    assert receipt["sandbox_path"] == saved["local_path"]
    result = {"recorded_at": datetime.now(timezone.utc).isoformat(),
              "postclosure_record_belongs_to": 35,
              "verifications": checks,
              "save": {"actual_session": 3650, "actual_exit": 0,
                       "exit_observation_chunk": "4ff2c3",
                       "file_id": saved["file_id"],
                       "library_file_id": saved["library_file_id"],
                       "local_path": saved["local_path"],
                       "stdout": identity(out), "stderr": identity(err),
                       "stderr_scope": "Successful Library write receipt only; fully read, not empty.",
                       "user_delivery": "Exact native link delivered in commentary after actual exit0 and all three complete verifier reports were read."},
              "archive_mutated": False, "new_archive_created": False}
    target = ROOT / "records/checkpoint34_delivery_observed.json"
    with target.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(identity(target), indent=2))


if __name__ == "__main__":
    main()
