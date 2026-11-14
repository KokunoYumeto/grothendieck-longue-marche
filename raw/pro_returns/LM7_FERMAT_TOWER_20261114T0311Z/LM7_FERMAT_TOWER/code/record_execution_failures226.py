"""Bind retained empty stdout to the actual recorded failures in E122.

No execution output is generated or substituted here. The original source,
stdout and stderr bytes remain unchanged; these are supplementary labels.
"""
from pathlib import Path
import hashlib
import json
import shutil

BASE = Path(__file__).resolve().parents[1]
CODE = BASE / "code"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    history = CODE / "packaging226_history/first_missing_failure_status"
    history.mkdir(parents=True, exist_ok=False)
    shutil.copy2(CODE / "package.py", history / "package.py")
    shutil.copy2(BASE.parent / "root_package226.out", history / "package.out")
    shutil.copy2(BASE.parent / "root_package226.err", history / "package.err")
    status = {"status": "failed before result", "exit_code": 1,
              "reason": "The package validator found genuine empty stdout from the retained initial E122 layout failure; its separate execution-status label had not yet been added.",
              "stderr_path": "package.err", "stderr_sha256": sha(history / "package.err"),
              "source_sha256": sha(history / "package.py")}
    (history / "package_status.json").write_text(json.dumps(status, indent=2) + "\n")
    evidence = BASE / "ledger/e_fiftythree_higher_computation_status.json"
    data = json.loads(evidence.read_text())
    rows = [
        ("audit/initial_layout/code/e53_higher_layout.py", 1,
         "Initial LuaLaTeX execution stopped at the matrix exceeding the default ten-column limit; the actual traceback and compiler log are retained."),
        ("code/history/initial_freeze_count/e53_higher_freeze.py", 1,
         "The initial delimiter-count guard also counted a line-break optional argument; its actual assertion failure is retained."),
        ("code/history/initial_residue_denominator/e53_upper_residue_search.py", 1,
         "An actual residue search reached a prime dividing a power-basis denominator; its assertion failure is retained."),
        ("code/history/initial_root_character_stream/e53_upper_root_characters.gp", 0,
         "PARI reported a nonexistent component and skipped the file while returning process exit zero. This is a failed interpretation, and supplies no successful result."),
    ]
    records = []
    for rel, exit_code, reason in rows:
        path = CODE / "e122_bundle" / rel
        assert path.is_file() and path.with_suffix(".out").read_bytes() == b""
        err = path.with_suffix(".err")
        assert err.stat().st_size
        source_name = rel.removeprefix("code/")
        matched = [r for r in data["executions"] if r["program"] == source_name]
        assert len(matched) == 1 and matched[0]["exit"] == exit_code, rel
        record = {"status": "failed before result" if exit_code else "failed with interpreter-reported error",
                  "exit_code": exit_code, "reason": reason,
                  "stderr_path": err.name, "stderr_sha256": sha(err),
                  "source_sha256": sha(path),
                  "execution_evidence": str(evidence.relative_to(BASE)),
                  "execution_evidence_sha256": sha(evidence),
                  "execution_record": matched[0]}
        if exit_code == 0:
            record["exact_error_marker"] = "nonexistent component: index > 2"
            assert record["exact_error_marker"] in err.read_text()
            assert "... skipping file 'e53_upper_root_characters.gp'" in err.read_text()
        target = path.with_name(path.stem + "_status.json")
        assert not target.exists()
        target.write_text(json.dumps(record, indent=2) + "\n")
        records.append({"status_file": str(target.relative_to(BASE)), "sha256": sha(target)})
    print(json.dumps({"status": "PASS", "original_output_bytes_modified": 0,
                      "supplementary_status_records": records,
                      "first_package_attempt_retained": str(history.relative_to(BASE))}, indent=2))


if __name__ == "__main__":
    main()
