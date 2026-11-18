#!/usr/bin/env python3
"""Run isolated per-page syntax compilations without displaying manuscript text."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
QA = ROOT.parent / "MPL_67_002-052_latex_qa"
SCANS = tuple(n for n in range(2, 53) if n not in {15, 22, 23, 47, 52})


def run(scan: int) -> dict:
    output = QA / "per_scan" / f"{scan:03d}"
    formats = output / "formats"
    formats.mkdir(parents=True, exist_ok=True)
    shared_format = QA / "formats" / "xelatex.fmt"
    linked_format = formats / "xelatex.fmt"
    if shared_format.is_file() and not linked_format.exists():
        linked_format.symlink_to(shared_format)
    process = subprocess.run(
        [sys.executable, str(ROOT / "records/compile_qa.py"), "--scan", str(scan),
         "--output-dir", str(output), "--no-pdf"],
        capture_output=True, text=True, timeout=240, check=False)
    report_path = output / "qa_report.json"
    if report_path.is_file():
        result = json.loads(report_path.read_text(encoding="utf-8"))
    else:
        result = {"compiler_returncode": process.returncode,
                  "harness_failure": True,
                  "diagnostic_log": str(output / "harness_stderr.log")}
        (output / "harness_stderr.log").write_text(process.stderr, encoding="utf-8")
    result["scan"] = scan
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--changed-only", action="store_true", help="Recheck failed, changed or previously unchecked sources")
    args = parser.parse_args()
    report_file = ROOT / "records/latex_qa_report.json"
    previous = json.loads(report_file.read_text(encoding="utf-8")) if args.changed_only and report_file.is_file() else {}
    by_scan = {entry["scan"]: entry for entry in previous.get("reports", [])}
    selected = []
    for scan in SCANS:
        source = ROOT / "pages" / f"MPL_67_002-052_67_scan{scan:03d}.tex"
        old = by_scan.get(scan, {})
        current_hash = hashlib.sha256(source.read_bytes()).hexdigest()
        if not args.changed_only or old.get("compiler_returncode") != 0 or old.get("missing_character_diagnostics") or old.get("source_hashes", {}).get(str(source)) != current_hash:
            selected.append(scan)
    with ThreadPoolExecutor(max_workers=3) as executor:
        for result in executor.map(run, selected):
            by_scan[result["scan"]] = result
    results = [by_scan[scan] for scan in SCANS]
    summary = {
        "utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "purpose": "Mechanical LaTeX syntax QA; no image or reading audit",
        "page_count": len(results),
        "compiled_this_run": selected,
        "pdf_driver": "omitted for syntax and glyph checks",
        "passed": [r["scan"] for r in results if r.get("compiler_returncode") == 0],
        "failed": [r["scan"] for r in results if r.get("compiler_returncode") != 0],
        "reports": results,
    }
    report_file.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    public = {k: v for k, v in summary.items() if k != "reports"}
    public["diagnostics"] = [
        {"scan": r["scan"], "compiler_returncode": r.get("compiler_returncode"),
         "diagnostics": r.get("diagnostics", []),
         "missing_characters": r.get("missing_character_diagnostics", []),
         "font_warnings": r.get("font_warning_count", 0),
         "source_files_unchanged": r.get("source_files_unchanged")}
        for r in results
        if r.get("compiler_returncode") != 0 or r.get("missing_character_diagnostics")
           or r.get("font_warning_count") or not r.get("source_files_unchanged")
    ]
    print(json.dumps(public, indent=2, ensure_ascii=False))
    return 0 if not summary["failed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
