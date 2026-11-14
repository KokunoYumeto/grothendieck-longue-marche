"""Replay the complete frozen E120 Tor-symbol certificate in a fresh tree."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / "research_e120"
FRESH = HERE / "tor_symbol_fresh"
MANIFEST = AUTHOR / "ledger/a_elliptic_tor_symbol_manifest.json"
MANIFEST_SHA = "14116ce60b91b8968fa659dc022e3f4cbe02d13c9b50ef583d427207452c9001"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    assert sha(MANIFEST) == MANIFEST_SHA
    manifest = json.loads(MANIFEST.read_text())
    rows = manifest["owned"] + manifest["immutable_inputs"]
    for row in rows:
        assert sha(AUTHOR / row["path"]) == row["sha256"], row
    assert not FRESH.exists()
    (FRESH / "code").mkdir(parents=True)
    for row in manifest["immutable_inputs"]:
        shutil.copy2(AUTHOR / row["path"], FRESH / row["path"])
    source = "code/a_elliptic_tor_symbol.py"
    shutil.copy2(AUTHOR / source, FRESH / source)
    shutil.copy2(MANIFEST, HERE / "tor_author_manifest.json")
    shutil.copy2(AUTHOR / "notes/elliptic_tor_symbol.md", HERE / "tor_author_note.md")
    helper = FRESH / "code/a_e120_exact.py"
    empty_run = subprocess.run([sys.executable, str(helper)], capture_output=True)
    helper.with_suffix(".out").write_bytes(empty_run.stdout)
    helper.with_suffix(".err").write_bytes(empty_run.stderr)
    assert empty_run.returncode == 0 and not empty_run.stdout and not empty_run.stderr
    helper.with_name(helper.stem + "_status.json").write_text(json.dumps({
        "status": "silent module executed successfully", "exit_code": 0,
        "source_sha256": sha(helper),
        "reason": "This helper defines exact coefficient operations and has no main procedure or print statement. Its actual standalone stdout and stderr are empty; the importing Tor certificate exercises the operations.",
        "importing_certificate": "a_elliptic_tor_symbol.py"
    }, indent=2) + "\n")
    run = subprocess.run([sys.executable, str(FRESH / source)], capture_output=True, cwd=FRESH)
    for suffix, data in ((".out", run.stdout), (".err", run.stderr)):
        (FRESH / source).with_suffix(suffix).write_bytes(data)
    assert run.returncode == 0, run.stderr.decode()
    comparisons = []
    for suffix in (".out", ".err", ".json"):
        expected = (AUTHOR / source).with_suffix(suffix)
        actual = (FRESH / source).with_suffix(suffix)
        assert actual.read_bytes() == expected.read_bytes(), suffix
        comparisons.append({"file": str(actual.relative_to(HERE)),
                            "bytes": actual.stat().st_size, "sha256": sha(actual),
                            "complete_byte_equality": True})
    for row in rows:
        assert sha(AUTHOR / row["path"]) == row["sha256"], row
    for row in manifest["immutable_inputs"]:
        assert sha(FRESH / row["path"]) == row["sha256"], row
    result = {"status": "PASS", "manifest_sha256": MANIFEST_SHA,
              "owned_files_checked_before_and_after": len(manifest["owned"]),
              "immutable_inputs_checked_before_and_after": len(manifest["immutable_inputs"]),
              "full_replay_exit_code": run.returncode, "comparisons": comparisons,
              "fields_or_bytes_excluded": [],
              "helper_actual_silent_execution_exit_code": empty_run.returncode,
              "author_sources_modified": False,
              "checked_utc": datetime.now(timezone.utc).isoformat()}
    (HERE / "tor_replay_audit.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
