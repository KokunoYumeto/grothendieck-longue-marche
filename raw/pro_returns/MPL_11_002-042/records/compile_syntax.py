#!/usr/bin/env python3
"""Compile unchanged page snapshots with a syntax-only TeX harness.

Usage from the deliverable root:
    python records/compile_syntax.py .
    python records/compile_syntax.py . --scans 003,005 --scratch /path/outside/deliverable

All drivers, copied inputs, TeX formats, logs and results stay in scratch.
No page, inventory, progress log or frozen manifest is modified. The PDF engine's
draft mode performs typesetting without generating final PDFs. This check cannot
establish source fidelity, mathematical correctness, or final presentation.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


PREFIX = "MPL_11_002-042"
SCANS = tuple(range(3, 33)) + tuple(range(34, 43))
REQUIRED = (
    "article.cls", "fontenc.sty", "inputenc.sty", "amsmath.sty", "amssymb.sty",
    "tikz.sty", "tikz-cd.sty", "pdflatex.ini",
)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def local_environment(scratch):
    environment = os.environ.copy()
    texmf_roots = [
        path for path in ("/etc/texmf", "/var/lib/texmf", "/usr/share/texmf", "/usr/share/texlive/texmf-dist")
        if Path(path).is_dir()
    ]
    if Path("/usr/share/texlive/texmf-dist").is_dir():
        # Avoid stale database-only (!!) lookup entries; changes affect this process only.
        environment["TEXMF"] = "{" + ",".join(texmf_roots) + "}"
    environment["TEXFORMATS"] = str(scratch) + os.pathsep
    environment["TEXMFVAR"] = str(scratch / "texmf-var")
    environment["TEXMFCONFIG"] = str(scratch / "texmf-config")
    environment["TEXMFOUTPUT"] = str(scratch)
    environment["VARTEXFONTS"] = str(scratch / "fonts")
    for name in ("MKTEXFMT", "MKTEXPK", "MKTEXTFM"):
        environment[name] = "0"
    return environment


def error_locations(output):
    result = []
    lines = output.splitlines()
    for index, line in enumerate(lines):
        match = re.match(r"^(.+?\.tex):([0-9]+):\s*(.*)$", line)
        if match:
            if match.group(3).startswith("==> Fatal error"):
                continue
            error = {"file": Path(match.group(1)).name, "line": int(match.group(2)), "message": match.group(3)}
            if "Undefined control sequence" in match.group(3):
                error["following_control_words"] = re.findall(r"\\[A-Za-z@]+", "\n".join(lines[index + 1:index + 4]))
            result.append(error)
        elif line.startswith("!"):
            result.append({"file": None, "line": None, "message": line[1:].strip()})
    return result


def save_results(scratch, results):
    (scratch / "syntax_results.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--scans", help="Comma-separated scan numbers; default is all 39 expected scans")
    parser.add_argument("--scratch", help="Output directory outside the deliverable; default is a new temporary sibling")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        parser.error("Deliverable root must exist.")
    selected = SCANS
    if args.scans:
        try:
            wanted = {int(part) for part in args.scans.split(",")}
        except ValueError:
            parser.error("--scans must contain comma-separated integers.")
        if not wanted or not wanted.issubset(SCANS):
            parser.error("--scans contains a number outside 003–032, 034–042.")
        selected = tuple(scan for scan in SCANS if scan in wanted)
    if args.scratch:
        scratch = Path(args.scratch).resolve()
        try:
            scratch.relative_to(root)
        except ValueError:
            pass
        else:
            parser.error("Scratch output must be outside the deliverable directory.")
        scratch.mkdir(parents=True, exist_ok=True)
    else:
        scratch = Path(tempfile.mkdtemp(prefix="mpl-tex-syntax-", dir=root.parent)).resolve()
    print(f"Scratch output: {scratch}", flush=True)
    environment = local_environment(scratch)
    results = {
        "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "root": str(root), "scratch": str(scratch), "mode": "syntax-only draft compilation",
        "harness_sha256": None, "dependencies": {}, "pages": [],
    }
    engine = shutil.which("pdflatex")
    kpsewhich = shutil.which("kpsewhich")
    if not engine or not kpsewhich:
        results["blocked"] = "pdflatex or kpsewhich is unavailable"
        save_results(scratch, results)
        print("BLOCKED: " + results["blocked"], flush=True)
        return 2
    for package in REQUIRED:
        probe = subprocess.run([kpsewhich, package], env=environment, capture_output=True, text=True, timeout=15)
        results["dependencies"][package] = probe.stdout.strip() or None
    missing = [name for name, path in results["dependencies"].items() if path is None]
    if missing:
        results["blocked"] = "Missing TeX dependencies: " + ", ".join(missing)
        save_results(scratch, results)
        print("BLOCKED: " + results["blocked"], flush=True)
        return 2
    harness = (root / "records" / "syntax_harness.tex").read_bytes()
    results["harness_sha256"] = sha256(harness)
    (scratch / "syntax_harness.tex").write_bytes(harness)
    snapshots = {}
    for scan in selected:
        source = root / "pages" / f"{PREFIX}_11_scan{scan:03d}.tex"
        data = source.read_bytes()
        snapshots[scan] = (source, sha256(data))
        (scratch / f"page_scan{scan:03d}.tex").write_bytes(data)
    # Generate the format in scratch; no fmtutil or system-wide update is invoked.
    format_run = subprocess.run(
        [engine, "-ini", "-etex", "-jobname=pdflatex", "-progname=pdflatex",
         "-interaction=nonstopmode", "-halt-on-error", "pdflatex.ini"],
        cwd=scratch, env=environment, capture_output=True, text=True, errors="replace", timeout=60,
    )
    format_output = format_run.stdout + format_run.stderr
    (scratch / "format.stdout.log").write_text(format_output, encoding="utf-8")
    if format_run.returncode != 0 or not (scratch / "pdflatex.fmt").is_file():
        results["blocked"] = "Temporary pdflatex format generation failed"
        results["format_errors"] = error_locations(format_output)
        save_results(scratch, results)
        print("BLOCKED: " + results["blocked"] + "; see format.stdout.log", flush=True)
        for error in results["format_errors"]:
            print(error, flush=True)
        return 2
    for scan in selected:
        driver = f"driver_scan{scan:03d}.tex"
        (scratch / driver).write_text(
            "\\input{syntax_harness.tex}\n\\begin{document}\n"
            + f"\\input{{page_scan{scan:03d}.tex}}\n"
            + "\\end{document}\n", encoding="utf-8",
        )
        try:
            run = subprocess.run(
                [engine, "-draftmode", "-no-shell-escape", "-file-line-error",
                 "-interaction=nonstopmode", "-halt-on-error", driver],
                cwd=scratch, env=environment, capture_output=True, text=True, errors="replace", timeout=45,
            )
            output = run.stdout + run.stderr
            code = run.returncode
        except subprocess.TimeoutExpired:
            output = "Compilation exceeded the 45-second per-page limit.\n"
            code = 124
        (scratch / f"driver_scan{scan:03d}.stdout.log").write_text(output, encoding="utf-8")
        source, digest = snapshots[scan]
        current_digest = sha256(source.read_bytes())
        page = {
            "scan": scan, "source": str(source.relative_to(root)), "sha256": digest,
            "source_unchanged_since_snapshot": current_digest == digest,
            "returncode": code, "errors": error_locations(output),
        }
        results["pages"].append(page)
        status = "PASS" if code == 0 else "FAIL"
        print(f"scan {scan:03d}: {status}", flush=True)
        for error in page["errors"]:
            print(f"  {error['file']}:{error['line']}: {error['message']}", flush=True)
            if error.get("following_control_words"):
                print("  Nearby control words: " + ", ".join(error["following_control_words"]), flush=True)
        if current_digest != digest:
            print("  Source changed after snapshot; rerun this scan.", flush=True)
        save_results(scratch, results)
    for page in results["pages"]:
        source, digest = snapshots[page["scan"]]
        unchanged = sha256(source.read_bytes()) == digest
        if page["source_unchanged_since_snapshot"] and not unchanged:
            print(f"scan {page['scan']:03d}: source changed after its compile; rerun this scan.", flush=True)
        page["source_unchanged_since_snapshot"] = unchanged
    results["completed_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    save_results(scratch, results)
    failed = sum(page["returncode"] != 0 for page in results["pages"])
    changed = sum(not page["source_unchanged_since_snapshot"] for page in results["pages"])
    print(f"Result: {len(selected) - failed}/{len(selected)} pages compiled; {changed} changed after snapshot.", flush=True)
    print(f"Machine-readable results: {scratch / 'syntax_results.json'}", flush=True)
    return 1 if failed or changed else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, subprocess.TimeoutExpired) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(2)
