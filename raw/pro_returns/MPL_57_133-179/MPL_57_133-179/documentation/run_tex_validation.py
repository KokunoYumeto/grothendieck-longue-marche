#!/usr/bin/env python3
"""Compile immutable temporary copies of page fragments without changing them.

This is a syntax smoke check, not visual proofreading. Editorial macros are
rendered as their contents. The wrapper handles tikz-cd ampersands inside macro
arguments; the original fragment bytes are not normalized or edited.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", nargs="?", type=Path,
                        default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--label", default="latest")
    parser.add_argument("--format", type=Path,
                        help="Existing local xelatex.fmt to copy; otherwise build one locally")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", args.label):
        parser.error("--label must contain only letters, digits, underscores, or hyphens")
    root = args.package.resolve()
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    build = root.parent / f"tex_validation_{stamp}"
    (build / "pages").mkdir(parents=True)
    preamble = Path(__file__).with_name("syntax_wrapper_preamble.tex").read_text(encoding="utf-8")
    hashes = {}
    for page in sorted((root / "pages").glob("*.tex")):
        match = re.fullmatch(r"MPL_57_133-179_57_scan(\d+)\.tex", page.name)
        if not match:
            continue
        data = page.read_bytes()
        (build / "pages" / page.name).write_bytes(data)
        hashes[page.name] = hashlib.sha256(data).hexdigest()
        (build / f"check_{match.group(1)}.tex").write_text(
            preamble + "\\input{pages/" + page.name + "}\n\\end{document}\n",
            encoding="utf-8",
        )
    (build / "snapshot_hashes.json").write_text(json.dumps(hashes, indent=2) + "\n")
    if args.format:
        shutil.copyfile(args.format.resolve(), build / "xelatex.fmt")
    else:
        result = subprocess.run(
            ["xetex", "-ini", "-etex", "-jobname=xelatex", "-progname=xelatex", "xelatex.ini"],
            cwd=build, capture_output=True, text=True, timeout=60,
        )
        (build / "format_build.stdout.txt").write_text(result.stdout + result.stderr)
        if result.returncode:
            raise RuntimeError(f"Local format generation failed; see {build}")

    def compile_page(path: Path) -> dict:
        result = subprocess.run(
            ["xelatex", "-fmt=./xelatex.fmt", "-interaction=nonstopmode",
             "-halt-on-error", "-file-line-error", path.name],
            cwd=build, capture_output=True, text=True, timeout=60,
        )
        (build / (path.stem + ".stdout.txt")).write_text(result.stdout + result.stderr)
        lines = result.stdout.splitlines()
        errors = []
        for index, line in enumerate(lines):
            if line.startswith("!") or (line.startswith("./") and re.search(r":\d+: ", line)):
                errors.append("\n".join(lines[index:index + 5]))
        return {
            "scan": int(path.stem.split("_")[1]), "returncode": result.returncode,
            "errors": errors, "tail": lines[-8:] if result.returncode else [],
        }

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = sorted(executor.map(compile_page, sorted(build.glob("check_*.tex"))),
                         key=lambda row: row["scan"])
    changed = []
    for name, digest in hashes.items():
        if hashlib.sha256((root / "pages" / name).read_bytes()).hexdigest() != digest:
            changed.append(name)
    report = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "build_directory": str(build), "snapshot_sha256": hashes,
        "pass_count": sum(row["returncode"] == 0 for row in results),
        "fail_count": sum(row["returncode"] != 0 for row in results),
        "changed_during_check": changed, "results": results,
        "limitations": "Syntax smoke check with identity editorial macros. No image access, OCR, source-reading audit, content correction, or context access.",
    }
    report_path = root / "documentation" / f"tex_compile_report_{args.label}.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"report": str(report_path), "build_directory": str(build),
                      "pass_count": report["pass_count"], "fail_count": report["fail_count"],
                      "changed_during_check": changed,
                      "failures": [row for row in results if row["returncode"]]},
                     ensure_ascii=False, indent=2))
    return 1 if report["fail_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
