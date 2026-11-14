"""Import actual root observations, preserving the prepared heading evidence.

The existing check_heading_closure.record validates hashes but hardcodes its
reviewer as editorial. This adapter keeps those checks and the actual supplied
reviewer. It generates no visual observations and changes no build inputs.
"""
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
REPORT = ROOT / "work/data/heading_closure_final.json"
NOTES = ROOT / "work/data/revision872_final_review/root_special_headings872_actual.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ref(path):
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": sha(path)}


def write_new(path, value):
    assert not path.exists(), path.name
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def main():
    assert sha(NOTES) == "18b9d874d546850a4fb6ca155ea76c0385b5cb7f7de6475c36861794936a9165"
    before_bytes = REPORT.read_bytes()
    report = json.loads(before_bytes)
    notes = json.loads(NOTES.read_text())
    assert report["status"] == "PENDING_VISUAL"
    assert report["expected_witnesses"] == len(report["witnesses"]) == 10
    assert set(notes) == {row["key"] for row in report["witnesses"]}
    for reader in report["readers"]:
        assert sha(ROOT / "work/build" / reader["file"]) == reader["sha256"]
    before_rows = copy.deepcopy(report["witnesses"])
    for row in report["witnesses"]:
        note = notes[row["key"]]
        assert row["status"] == "PENDING_VISUAL"
        for key in ("pdf_sha256", "heading_page", "evidence"):
            assert note[key] == row[key]
        for evidence in row["evidence"]:
            assert sha(ROOT / evidence["image"]) == evidence["sha256"]
        assert note["reviewer"] == "assistant/root"
        assert note["status"] == "PASS" and len(note["observation"]) > 20
        row.update(status=note["status"], reviewer=note["reviewer"],
                   observation=note["observation"],
                   review_basis="Actual final-PDF full-page and native heading/body images",
                   observation_record=ref(NOTES))
    for before, after in zip(before_rows, report["witnesses"]):
        assert all(after[key] == value for key, value in before.items() if key != "status")
    report.update(status="PASS", pass_count=10)
    backup = HERE / "heading_closure_before.json"
    assert not backup.exists()
    backup.write_bytes(before_bytes)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    write_new(HERE / "IMPORT_VALIDATION.json", {
        "status": "PASS", "observations": 10,
        "observations_generated_by_script": False,
        "actual_reviewer": "assistant/root",
        "before": ref(backup), "observations_record": ref(NOTES),
        "after": ref(REPORT), "adapter": ref(Path(__file__)),
        "base_checker_unchanged": ref(ROOT / "work/scripts/check_heading_closure.py"),
        "preservation": "All prepared reader, witness, source and image fields preserved; only closure status and actual observation metadata added.",
        "reason_for_adapter": "The base recorder hardcodes reviewer=editorial. This import records the actual root reviewer without changing the frozen helper."
    })
    print(json.dumps({"status": "PASS", "witnesses": 10, "report": ref(REPORT)}))


if __name__ == "__main__":
    main()
