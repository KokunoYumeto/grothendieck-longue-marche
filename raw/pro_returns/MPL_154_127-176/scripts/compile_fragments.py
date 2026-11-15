#!/usr/bin/env python3
"""Compile immutable copies of manuscript fragments without changing sources.

Examples:
    python scripts/compile_fragments.py --root /path/to/package --scans 127-135
    python scripts/compile_fragments.py --root /path/to/package --engine xelatex

The harness snapshots filenames before copying bytes. It neither interprets
manuscript content nor opens source images or context archives. Each copied
fragment is compiled independently, so TeX diagnostics retain its filename and
line numbers. All wrappers, formats, engine output, and compilation products
stay in a temporary directory. Only the concise report is written to the
package, at MPL_154_127-176_mechanical_compile_report.txt by default.

The optional TikZ bending library is not globally preloaded. Its curved-arrow
normalization overflowed on a nearly zero control vector in an unchanged
fragment; the same fragment passed both engines without that optional library.
See records/scan155_dimension_diagnosis.txt for the controlled comparison.

The twelve authorized editorial commands are defined solely for this test:
cotefile, scanpage, mspage, deleted, inserted, margin, uline, uuline, diagram,
figure, unsure, illegible. All take one argument. Editorial bodies remain in
the compilation stream; diagram/figure bodies gain no extra math environment.
The ordinary figure float command is intentionally replaced in this harness.
Underline commands are identities for syntax testing. Uncertainty commands
work in math and text and add visible bracketed markers.

Both engines run with shell escape disabled and halt at their first error.
pdfLaTeX uses draft mode and XeLaTeX produces XDV without PDF conversion; this
checks TeX processing without requiring a PDF backend or visual review.
Successful compilation does not validate transcription, source fidelity,
editorial meaning, diagram topology, pagination, or visual layout. Errors after
the first fatal error in each run may remain undetected.

If a local TeX installation lacks generated formats, the harness can build
them in temporary storage. --texmf-extra supplies an existing additional TeX
tree, for example one containing an installed ulem package. No package is
downloaded or replaced by this script, and no system configuration is written.
"""

from __future__ import annotations

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


PAGE_RE = re.compile(r"MPL_154_127-176_154_scan([0-9]{3})\.tex\Z")
PACKAGES = ("article.cls", "tikz.sty", "tikz-cd.sty", "amsmath.sty", "amssymb.sty", "graphicx.sty", "xcolor.sty", "ulem.sty")
EDITORIAL_MACROS = ("cotefile", "scanpage", "mspage", "deleted", "inserted", "margin", "uline", "uuline", "diagram", "figure", "unsure", "illegible")
PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage{amsmath,amssymb}
\usepackage{graphicx,xcolor}
\usepackage[normalem]{ulem}
\usepackage{tikz}
\usepackage{tikz-cd}
\usetikzlibrary{arrows,arrows.meta,backgrounds,calc,decorations,decorations.markings,decorations.pathmorphing,decorations.pathreplacing,decorations.shapes,fit,intersections,matrix,patterns,patterns.meta,positioning,quotes,shapes.arrows,shapes.geometric,shapes.misc,shapes.symbols}
\setlength{\textwidth}{17cm}
\setlength{\textheight}{25cm}
\setlength{\oddsidemargin}{-0.3cm}
\setlength{\topmargin}{-1.5cm}
\errorcontextlines=3
\long\def\cotefile#1{\par\noindent\textbf{Cote #1}\par}
\long\def\scanpage#1{\par\noindent\textbf{Scan #1}\par}
\long\def\mspage#1{\par\noindent\textbf{Manuscript page #1}\par}
\long\def\deleted#1{#1}
\long\def\inserted#1{#1}
\long\def\margin#1{#1}
\long\def\uline#1{#1}
\long\def\uuline#1{#1}
\long\def\diagram#1{#1}
\long\def\figure#1{#1}
\long\def\unsure#1{\ifmmode\text{[?]}\else[?]\fi#1}
\long\def\illegible#1{\ifmmode\text{[illegible]}\else[illegible]\fi#1}
\begin{document}
"""


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def scan_selection(value: str | None) -> set[int] | None:
    if value is None:
        return None
    selected: set[int] = set()
    for item in value.split(","):
        match = re.fullmatch(r"([0-9]{3})(?:-([0-9]{3}))?", item.strip())
        if match is None:
            raise ValueError("--scans must use three-digit scans or ranges, for example 127-135,140")
        first = int(match.group(1))
        last = int(match.group(2) or first)
        if first > last or first < 127 or last > 176:
            raise ValueError("scan ranges must lie within 127–176 and increase")
        selected.update(range(first, last + 1))
    return selected


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def snapshot_sources(root: Path, work: Path, selected: set[int] | None) -> tuple[Path, dict]:
    # Materialize the complete filename list before reading any fragment bytes.
    names = tuple(sorted(path.name for path in (root / "pages").iterdir() if PAGE_RE.fullmatch(path.name)))
    chosen = tuple(name for name in names if selected is None or int(PAGE_RE.fullmatch(name).group(1)) in selected)
    if selected is not None:
        present = {int(PAGE_RE.fullmatch(name).group(1)) for name in chosen}
        missing = sorted(selected - present)
        if missing:
            raise ValueError("requested source scans are missing: " + ", ".join(map(str, missing)))
    if not chosen:
        raise ValueError("no page fragments were selected")
    snapshot = work / "snapshot"
    (snapshot / "pages").mkdir(parents=True)
    manifest = {
        "captured_at_utc": utc_now(), "source_root": str(root),
        "filenames_first": list(names), "files": [],
    }
    for name in chosen:
        source = (root / "pages" / name).resolve()
        if root not in source.parents:
            raise ValueError(f"source resolves outside the package: {name}")
        data = source.read_bytes()
        (snapshot / "pages" / name).write_bytes(data)
        manifest["files"].append({"relative_path": "pages/" + name, "sha256": digest(data), "bytes": len(data)})
    (snapshot / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return snapshot, manifest


def load_snapshot(snapshot: Path, selected: set[int] | None) -> dict:
    manifest = json.loads((snapshot / "manifest.json").read_text(encoding="utf-8"))
    records = []
    seen: set[str] = set()
    for record in manifest["files"]:
        relative = Path(record["relative_path"])
        match = PAGE_RE.fullmatch(relative.name)
        if relative.parts != ("pages", relative.name) or match is None:
            raise ValueError("snapshot contains an unexpected page path")
        scan = int(match.group(1))
        if selected is not None and scan not in selected:
            continue
        if relative.as_posix() in seen:
            raise ValueError("snapshot contains a duplicate page path")
        seen.add(relative.as_posix())
        path = (snapshot / relative).resolve()
        if snapshot not in path.parents:
            raise ValueError("snapshot page resolves outside its snapshot directory")
        if digest(path.read_bytes()) != record["sha256"]:
            raise ValueError(f"snapshot hash mismatch: {relative}")
        records.append(record)
    if not records:
        raise ValueError("snapshot has no selected pages")
    if selected is not None:
        present = {int(PAGE_RE.fullmatch(Path(record["relative_path"]).name).group(1)) for record in records}
        if selected - present:
            raise ValueError("snapshot does not contain all requested scans")
    manifest["files"] = sorted(records, key=lambda record: record["relative_path"])
    return manifest


def kpsewhich(filename: str, env: dict[str, str]) -> str:
    executable = shutil.which("kpsewhich")
    if executable is None:
        return ""
    result = subprocess.run([executable, filename], env=env, capture_output=True, text=True, timeout=20)
    return result.stdout.strip() if result.returncode == 0 else ""


def tex_environment(work: Path, extras: list[Path], notes: list[str]) -> dict[str, str]:
    env = os.environ.copy()
    env["max_print_line"] = "1000"
    env["TEXMFVAR"] = str(work / "texmf-var")
    env["TEXMFCONFIG"] = str(work / "texmf-config")
    env["VARTEXFONTS"] = str(work / "texmf-var" / "fonts")
    # Some minimal installations retain !! database-only lookup without ls-R.
    # Use a per-process filesystem search; do not regenerate system databases.
    if not kpsewhich("article.cls", env):
        trees = [*extras, Path("/etc/texmf"), Path("/usr/share/texmf"), Path("/usr/share/texlive/texmf-dist")]
        trees = [path.resolve() for path in trees if path.is_dir()]
        if trees:
            env["TEXMF"] = "{" + ",".join(map(str, trees)) + "}"
            notes.append("Used an isolated filesystem TeX search because default package lookup was unavailable.")
    if extras:
        inputs = ":".join(str(path.resolve() / "tex") + "//" for path in extras)
        env["TEXINPUTS"] = inputs + ":" + env.get("TEXINPUTS", "")
    return env


def ensure_formats(engines: list[str], work: Path, env: dict[str, str], supplied: Path | None, notes: list[str]) -> None:
    formats = work / "formats"
    formats.mkdir(parents=True, exist_ok=True)
    existing = str(supplied.resolve()) + "//:" if supplied is not None else ""
    env["TEXFORMATS"] = existing + str(formats) + "//:" + env.get("TEXFORMATS", "")
    for engine in engines:
        if kpsewhich(engine + ".fmt", env):
            continue
        native = "pdftex" if engine == "pdflatex" else "xetex"
        executable = shutil.which(native)
        if executable is None:
            raise ValueError(f"cannot initialize {engine}: {native} is unavailable")
        command = [executable, "-ini", "-etex", "-interaction=nonstopmode", "-halt-on-error", "-no-shell-escape", "-jobname=" + engine, "-progname=" + engine, engine + ".ini"]
        result = subprocess.run(command, cwd=formats, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors="replace", timeout=60)
        (formats / (engine + "-format-output.txt")).write_text(result.stdout, encoding="utf-8")
        if result.returncode or not (formats / (engine + ".fmt")).is_file():
            raise ValueError(f"temporary {engine} format initialization failed; see {formats / (engine + '-format-output.txt')}")
        notes.append(f"Initialized a temporary {engine} format.")


def parse_diagnostics(output: str, relative: str, build: Path) -> list[dict]:
    diagnostics = []
    seen: set[tuple[str, int | None, str]] = set()
    for line in output.splitlines():
        match = re.match(r"^(.+?\.(?:tex|sty|cls|def|cfg)):([0-9]+):\s*(.+)$", line)
        if match is None:
            continue
        filename, number, message = match.groups()
        if message.startswith("==> Fatal error occurred"):
            continue
        source = relative if Path(filename).name == Path(relative).name else str(Path(filename))
        if Path(filename).name == "harness.tex":
            source = str(build / "harness.tex")
        key = (source, int(number), message)
        if key not in seen:
            diagnostics.append({"file": source, "line": int(number), "message": message})
            seen.add(key)
    if not diagnostics:
        for line in output.splitlines():
            if line.startswith("!") or "I can't find the format file" in line:
                diagnostics.append({"file": relative, "line": None, "message": line.lstrip("! ")})
    return diagnostics


def compile_one(engine: str, relative: str, snapshot: Path, work: Path, env: dict[str, str], timeout: int) -> dict:
    stem = Path(relative).stem
    build = work / "builds" / engine / stem
    build.mkdir(parents=True)
    wrapper = PREAMBLE + "\\input{" + str(snapshot / relative) + "}\n\\end{document}\n"
    (build / "harness.tex").write_text(wrapper, encoding="utf-8")
    mode = "-draftmode" if engine == "pdflatex" else "-no-pdf"
    command = [shutil.which(engine), "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "-no-shell-escape", mode, "harness.tex"]
    try:
        result = subprocess.run(command, cwd=build, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors="replace", timeout=timeout)
        output = result.stdout
        returncode = result.returncode
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        raw = exc.stdout or ""
        output = raw.decode("utf-8", errors="replace") if isinstance(raw, bytes) else raw
        returncode = 124
        timed_out = True
    (build / "engine-output.txt").write_text(output, encoding="utf-8")
    diagnostics = parse_diagnostics(output, relative, build) if returncode else []
    if timed_out:
        diagnostics.append({"file": relative, "line": None, "message": f"engine timed out after {timeout} seconds"})
    if returncode and not diagnostics:
        diagnostics.append({"file": relative, "line": None, "message": "engine failed without a file/line diagnostic; inspect the temporary engine output"})
    glyph_warnings = sorted(set(line.strip() for line in output.splitlines() if line.startswith("Missing character:")))
    return {"engine": engine, "source": relative, "returncode": returncode, "diagnostics": diagnostics, "missing_glyph_warnings": glyph_warnings, "build_directory": str(build)}


def write_report(path: Path, manifest: dict, results: list[dict], notes: list[str], changed: list[str], work: Path, infrastructure_error: str | None) -> None:
    lines = [
        "MPL 154: mechanical LaTeX compilation report",
        "Generated: " + utc_now(),
        "Snapshot: " + str(manifest.get("captured_at_utc", "unavailable")),
        f"Selected fragments: {len(manifest.get('files', []))}",
        "Scope: immutable fragment copies; syntax processing only; no image or context review.",
        "Source changes made by harness: none.",
        "Authorized one-argument test macros: " + ", ".join(EDITORIAL_MACROS) + ".",
        "Editorial bodies remain active. Underline commands are identities; uncertainty markers are visible.",
        "Packages: tikz, tikz-cd, amsmath, amssymb, graphicx, xcolor, ulem; standard TikZ libraries.",
        "Modes: pdfLaTeX draft; XeLaTeX XDV; shell escape disabled; stop at first fatal error per run.",
        "",
    ]
    if infrastructure_error:
        lines.extend(["INFRASTRUCTURE ERROR: " + infrastructure_error, ""])
    for note in notes:
        lines.append("NOTE: " + note)
    if notes:
        lines.append("")
    lines.append("COMPILATION RESULTS")
    for result in results:
        status = "PASS" if result["returncode"] == 0 else "FAIL"
        lines.append(f"{result['source']} | {result['engine']} | {status}")
        for diagnostic in result["diagnostics"]:
            location = diagnostic["file"] + (":" + str(diagnostic["line"]) if diagnostic["line"] is not None else ":line unavailable")
            lines.append("  " + location + ": " + diagnostic["message"])
        for warning in result["missing_glyph_warnings"]:
            lines.append("  GLYPH WARNING (no source line supplied by engine): " + warning)
    if not results:
        lines.append("No fragment compilation completed.")
    passed = sum(result["returncode"] == 0 for result in results)
    lines.extend(["", f"Completed engine runs: {len(results)}; passed: {passed}; failed: {len(results) - passed}."])
    if changed:
        lines.append("CHANGED SINCE SNAPSHOT: " + ", ".join(changed))
        lines.append("Compilation results describe the frozen copies, not the subsequently changed source files.")
    else:
        lines.append("Original source hashes still matched the snapshot when this report was generated.")
    lines.extend(["", "SNAPSHOT SHA256"])
    for record in manifest.get("files", []):
        lines.append(record["sha256"] + "  " + record["relative_path"])
    lines.extend([
        "", "Temporary build records: " + str(work), "",
        "LIMITATION: Compilation cannot validate transcription accuracy, completeness, manuscript meaning,",
        "diagram topology, or visual layout. Later errors may be hidden by a first fatal error.",
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--scans", help="optional selection, for example 127-135,140; default is all currently available fragments")
    parser.add_argument("--engine", choices=("both", "pdflatex", "xelatex"), default="both")
    parser.add_argument("--snapshot-dir", type=Path, help="reuse an existing snapshot with manifest.json")
    parser.add_argument("--texmf-extra", action="append", default=[], type=Path, help="additional installed TeX tree; may be repeated")
    parser.add_argument("--format-dir", type=Path, help="directory containing previously built formats")
    parser.add_argument("--report", type=Path, help="report destination; defaults to the package report filename")
    parser.add_argument("--timeout", type=int, default=45, help="maximum seconds per fragment/engine run")
    args = parser.parse_args()
    root = args.root.expanduser().resolve()
    report = args.report.resolve() if args.report else root / "MPL_154_127-176_mechanical_compile_report.txt"
    if not root.is_dir() or args.timeout <= 0:
        parser.error("--root must be an existing directory and --timeout must be positive")
    work = Path(tempfile.mkdtemp(prefix="mpl154-latex-build-"))
    notes: list[str] = []
    results: list[dict] = []
    changed: list[str] = []
    manifest: dict = {"files": []}
    infrastructure_error = None
    try:
        selected = scan_selection(args.scans)
        if args.snapshot_dir:
            snapshot = args.snapshot_dir.resolve()
            manifest = load_snapshot(snapshot, selected)
            if Path(manifest["source_root"]).resolve() != root:
                raise ValueError("snapshot source root does not match --root")
        else:
            snapshot, manifest = snapshot_sources(root, work, selected)
        engines = ["pdflatex", "xelatex"] if args.engine == "both" else [args.engine]
        for engine in engines:
            if shutil.which(engine) is None:
                raise ValueError(f"required engine is unavailable: {engine}")
            version = subprocess.run([engine, "--version"], capture_output=True, text=True, timeout=10)
            if version.returncode == 0 and version.stdout.splitlines():
                notes.append(version.stdout.splitlines()[0])
        env = tex_environment(work, args.texmf_extra, notes)
        missing = [package for package in PACKAGES if not kpsewhich(package, env)]
        if missing:
            raise ValueError("required TeX packages unavailable: " + ", ".join(missing))
        ensure_formats(engines, work, env, args.format_dir, notes)
        for record in manifest["files"]:
            for engine in engines:
                result = compile_one(engine, record["relative_path"], snapshot, work, env, args.timeout)
                results.append(result)
                print(result["source"] + " | " + engine + " | " + ("PASS" if result["returncode"] == 0 else "FAIL"), flush=True)
                for diagnostic in result["diagnostics"]:
                    suffix = ":" + str(diagnostic["line"]) if diagnostic["line"] is not None else ":line unavailable"
                    print("  " + diagnostic["file"] + suffix + ": " + diagnostic["message"], flush=True)
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
        infrastructure_error = str(exc)
    for record in manifest["files"]:
        try:
            if digest((root / record["relative_path"]).read_bytes()) != record["sha256"]:
                changed.append(record["relative_path"])
        except OSError:
            changed.append(record["relative_path"])
    write_report(report, manifest, results, notes, changed, work, infrastructure_error)
    (work / "run.json").write_text(json.dumps({"manifest": manifest, "results": results, "notes": notes, "changed_sources": changed, "infrastructure_error": infrastructure_error}, indent=2) + "\n", encoding="utf-8")
    print("Report: " + str(report), flush=True)
    print("Temporary build records: " + str(work), flush=True)
    if infrastructure_error:
        print("INFRASTRUCTURE ERROR: " + infrastructure_error, flush=True)
        return 2
    return 1 if changed or any(result["returncode"] for result in results) else 0


if __name__ == "__main__":
    sys.exit(main())
