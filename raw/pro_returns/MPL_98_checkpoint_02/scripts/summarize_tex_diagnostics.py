#!/usr/bin/env python3
"""Summarize compiler diagnostics without reading scans or manuscript sources."""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import re


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compilation-report", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    previous = json.loads(args.compilation_report.read_text(encoding="utf-8"))
    pages = []
    for result in previous["results"]:
        record = {key: result[key] for key in
                  ("scan", "status", "exit_code", "error", "tex_reported_line")
                  if key in result}
        text = Path(result["log"]).read_text(encoding="utf-8") if result.get("log") else ""
        missing = Counter(re.findall(r"^Missing character: (.+)$", text, re.MULTILINE))
        overfull = re.findall(r"^Overfull \\[hv]box[^\n]*", text, re.MULTILINE)
        underfull = re.findall(r"^Underfull \\[hv]box[^\n]*", text, re.MULTILINE)
        warnings = Counter(re.findall(r"^(?:LaTeX(?: Font)?|Package [^\n]+?) Warning: [^\n]*", text, re.MULTILINE))
        if missing:
            record["missing_character_diagnostics"] = dict(missing)
        if overfull:
            record["overfull_box_diagnostics"] = overfull
        if underfull:
            record["underfull_box_count"] = len(underfull)
        if warnings:
            record["warning_headlines"] = dict(warnings)
        pages.append(record)
    scans = [record["scan"] for record in pages]
    issues = [record for record in pages if record["status"] != "passed" or
              any(key in record for key in ("missing_character_diagnostics", "overfull_box_diagnostics", "warning_headlines"))]
    report = {
        "recorded_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "scope": "TeX syntax and compiler-reported layout risks only; no manuscript image, reading, or mathematics audit",
        "compiled_scans": scans,
        "page_count": len(pages),
        "passed": sum(record["status"] == "passed" for record in pages),
        "failed": sum(record["status"] != "passed" for record in pages),
        "pages_with_missing_character_diagnostics": [record["scan"] for record in pages if "missing_character_diagnostics" in record],
        "pages_with_overfull_boxes": [record["scan"] for record in pages if "overfull_box_diagnostics" in record],
        "underfull_box_count": sum(record.get("underfull_box_count", 0) for record in pages),
        "issues": issues,
        "all_page_statuses": {str(record["scan"]): record["status"] for record in pages},
        "source_report": str(args.compilation_report.resolve()),
        "limitations": [
            "Only the first fatal error on each failed page is exposed; later issues may remain.",
            "The large-paper syntax harness and simplified state wrappers are not a diplomatic page-layout specification.",
            "Compiler-reported line numbers belong to the active TeX input; inspect the page log before applying edits.",
            "No transcription file is changed and no audited or research-check event is generated."]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
