#!/usr/bin/env python3
"""Compile each page separately to locate syntax blockers after the first one.

This mechanically inputs page files; it does not interpret or modify them.
All logs and generated PDFs go to the required --output directory.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import re
import subprocess

from validate_transcription import make_harness, tex_availability


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--tex-environment", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=3)
    args = parser.parse_args()
    overrides = json.loads(args.tex_environment.read_text(encoding="utf-8"))
    allowed = {"TEXMF", "TEXMFVAR", "TEXMFCONFIG", "TEXFORMATS", "TEXFONTMAPS"}
    if not isinstance(overrides, dict) or set(overrides) - allowed or not all(isinstance(value, str) for value in overrides.values()):
        parser.error("invalid TeX environment override file")
    environment = dict(os.environ, **overrides)
    available = tex_availability(environment)
    engine = available["executables"]["pdflatex"]
    missing = [name for name, path in available["packages"].items() if not path]
    if not engine or missing:
        parser.error("TeX unavailable: " + ", ".join(missing))
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    files = sorted((args.base.resolve() / "pages").glob("MPL_98_98_scan*.tex"))

    def compile_page(path: Path) -> dict:
        scan = int(re.search(r"scan(\d+)\.tex$", path.name).group(1))
        destination = output / f"scan{scan:03d}"
        destination.mkdir(exist_ok=True)
        harness = make_harness([path], destination)
        try:
            run = subprocess.run([engine, "-no-shell-escape", "-interaction=nonstopmode",
                                  "-halt-on-error", harness.name], cwd=destination,
                                 env=environment, capture_output=True, text=True, timeout=120)
            transcript = run.stdout + run.stderr
            (destination / "compile_stdout.txt").write_text(transcript, encoding="utf-8")
            result = {"scan": scan, "exit_code": run.returncode,
                      "status": "passed" if run.returncode == 0 else "failed",
                      "log": str(destination / "compile_stdout.txt")}
            if run.returncode:
                error = re.search(r"^! (.+)$", transcript, re.MULTILINE)
                result["error"] = error.group(1) if error else "No standard TeX error line; inspect log."
                if error:
                    line = re.search(r"^l\.(\d+)\b", transcript[error.end():], re.MULTILINE)
                    result["tex_reported_line"] = int(line.group(1)) if line else None
            return result
        except subprocess.TimeoutExpired:
            return {"scan": scan, "status": "timeout", "exit_code": None}

    with ThreadPoolExecutor(max_workers=max(1, min(args.workers, 4))) as pool:
        results = list(pool.map(compile_page, files))
    failures = [result for result in results if result["status"] != "passed"]
    report = {"scope": "syntax compilation only; no image, reading, or mathematics audit",
              "pages": len(results), "passed": len(results) - len(failures),
              "failed": len(failures), "tex_environment": str(args.tex_environment),
              "results": results,
              "limitations": ["Harness state wrappers are simplified; see VALIDATION.md.",
                              "A successful page compile does not certify correspondence with the scan."]}
    (output / "page_compilation_report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"pages": report["pages"], "passed": report["passed"],
                      "failed": report["failed"], "failures": failures,
                      "report": str(output / "page_compilation_report.json")}, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
