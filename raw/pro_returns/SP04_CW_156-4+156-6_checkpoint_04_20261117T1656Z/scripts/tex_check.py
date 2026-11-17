#!/usr/bin/env python3
"""Optional mechanical TeX check in an isolated directory; never rewrites inputs.

No manuscript/witness text is interpreted by this script. It stages byte-for-
byte copies, uses the supplied preamble unchanged, and reports engine status.
No packages/formats are installed. This is independent of the required visual
reading and structural checks, and is run only on the root's explicit command.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

OUT = Path(__file__).resolve().parents[1]
PREFIX = "SP04_CW_156-4+156-6"
PACKAGES = ["article.cls", "iftex.sty", "amsmath.sty", "amssymb.sty", "mathrsfs.sty",
            "tikz.sty", "tikz-cd.sty", "enumitem.sty", "ulem.sty", "xcolor.sty"]
ENGINE_IDS = {"lualatex": "luahbtex", "pdflatex": "pdftex"}

# These are invented diagnostic strings, not manuscript readings. Failure of
# a probe is reported as a macro/engine issue; it never triggers a text edit.
PROBES = {
    "diplomatic_math": r"""Text \unsure{word}, \deleted{word}, \inserted{word}.
    $\unsure{x_i}$, $\deleted{x_i}$, $\inserted{x_i}$, \deleted{$x_i$}.
    \[\deleted{x_i+y_j}=\unsure{z^!}.\]""",
    "nested_deletions": r"""\deleted{outer \deleted{inner} outer}.
    $\deleted{x+\deleted{y}}$.
    \deleted{outer $\deleted{x_i}$ outer}.""",
    "tikz": r"""\diagram{\begin{tikzcd}[ampersand replacement=\&]
    X_i \arrow[r,"{\deleted{f}}"] \arrow[d,"g"'] \& Y^! \arrow[d,"h"] \\
    Z \arrow[r,"{\unsure{k}}"'] \& T
    \end{tikzcd}}
    \figure{\begin{tikzpicture}\draw[->] (0,0)--(1,1);
    \node at (0,0) {$\deleted{x_i}$};\node at (1,1) {$\unsure{y^!}$};
    \end{tikzpicture}}""",
}


def preflight(engine, env=None, format_file=None):
    executable = shutil.which(engine)
    kpse = shutil.which("kpsewhich")
    result = {"engine": engine, "executable": executable, "kpsewhich": kpse,
              "missing": [], "ready": False}
    if not executable or not kpse:
        result["missing"] = [name for name, value in ((engine, executable), ("kpsewhich", kpse)) if not value]
        return result
    version = subprocess.run([executable, "--version"], env=env, capture_output=True, text=True, timeout=10)
    result["version"] = version.stdout.splitlines()[0] if version.stdout.splitlines() else "unavailable"
    needed = PACKAGES + (["fontspec.sty"] if engine == "lualatex" else ["fontenc.sty", "inputenc.sty"])
    for name in needed:
        found = subprocess.run([kpse, f"--progname={engine}", name], env=env, capture_output=True, text=True, timeout=10)
        if found.returncode != 0 or not found.stdout.strip():
            result["missing"].append(name)
    fmt = f"{engine}.fmt"
    if format_file is not None:
        result["explicit_format"] = str(format_file)
        if not Path(format_file).is_file():
            result["missing"].append(str(format_file))
    else:
        found = subprocess.run([kpse, f"--progname={engine}", f"--engine={ENGINE_IDS[engine]}", "--format=fmt", fmt],
                               env=env, capture_output=True, text=True, timeout=10)
        if found.returncode != 0 or not found.stdout.strip():
            result["missing"].append(fmt)
    result["ready"] = not result["missing"]
    return result


def run_tex(engine, directory, stem, timeout, env_overrides=None, format_file=None, output_format="pdf"):
    command = [engine]
    if format_file is not None:
        command.append("-fmt=" + str(format_file))
    if output_format == "dvi":
        command.append("-output-format=dvi")
    command += ["-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error",
               "-file-line-error", "-recorder", f"{stem}.tex"]
    env = dict(os.environ)
    env.update(env_overrides or {})
    env.update({"MKTEXFMT": "0", "MKTEXPK": "0", "MKTEXTFM": "0",
                "TEXMFVAR": str(directory / "var"), "TEXMFCONFIG": str(directory / "config"),
                "TEXMFCACHE": str(directory / "cache"), "TEXMFOUTPUT": str(directory),
                "openout_any": "p"})
    try:
        result = subprocess.run(command, cwd=directory, env=env, capture_output=True,
                                text=True, errors="replace", timeout=timeout)
        (directory / f"{stem}.stdout.txt").write_text(result.stdout, encoding="utf-8")
        (directory / f"{stem}.stderr.txt").write_text(result.stderr, encoding="utf-8")
        # Do not print compiler excerpts, which may reproduce manuscript text.
        return {"name": stem, "exit_code": result.returncode,
                "pdf_created": (directory / f"{stem}.pdf").is_file(),
                "dvi_created": (directory / f"{stem}.dvi").is_file(),
                "output_created": (directory / f"{stem}.{output_format}").is_file(),
                "log": str(directory / f"{stem}.log"), "timed_out": False}
    except subprocess.TimeoutExpired as error:
        for suffix, value in (("stdout", error.stdout), ("stderr", error.stderr)):
            if value:
                if isinstance(value, bytes):
                    value = value.decode("utf-8", errors="replace")
                (directory / f"{stem}.{suffix}.txt").write_text(value, encoding="utf-8")
        return {"name": stem, "exit_code": None, "pdf_created": False, "dvi_created": False, "output_created": False,
                "log": str(directory / f"{stem}.log"), "timed_out": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=OUT / f"{PREFIX}_transcription.tex")
    parser.add_argument("--preamble", type=Path, default=OUT / "PREAMBLE.tex")
    parser.add_argument("--engine", choices=("auto", "lualatex", "pdflatex"), default="auto")
    parser.add_argument("--preflight", action="store_true", help="Report runtime readiness only; no input copies or compile")
    parser.add_argument("--probes", action="store_true", help="Also run three synthetic macro/TikZ probes separately")
    parser.add_argument("--isolated-dvi", action="store_true", help="Use the validated local format and official ulem support; produce DVI")
    parser.add_argument("--timeout", type=float, default=180, help="Maximum seconds for each compile invocation")
    args = parser.parse_args()
    overrides = {}
    format_file = None
    output_format = "dvi" if args.isolated_dvi else "pdf"
    if args.isolated_dvi:
        if args.engine not in {"auto", "pdflatex"}:
            parser.error("--isolated-dvi uses the validated pdflatex format")
        support = OUT / "scripts" / "tex_support"
        receipt = support / "synthetic_result.json"
        package = support / "ulem.sty"
        if not receipt.is_file() or not package.is_file():
            print(json.dumps({"compile_started": False, "error": "Run out/scripts/tex_support/run_synthetic.py to initialize the isolated support"}))
            return 2
        metadata = json.loads(receipt.read_text(encoding="utf-8"))
        if metadata.get("all_passed") is not True or hashlib.sha256(package.read_bytes()).hexdigest() != metadata.get("ulem_sha256"):
            print(json.dumps({"compile_started": False, "error": "Isolated support validation or package hash does not match"}))
            return 2
        format_file = Path(metadata["format"])
        overrides = {"TEXMF": "{/usr/local/share/texmf,/etc/texmf,/var/lib/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}",
                     "TEXINPUTS": f".:{support}//:", "TEXFORMATS": f"{format_file.parent}//:"}
        candidates = ["pdflatex"]
    else:
        candidates = ["lualatex", "pdflatex"] if args.engine == "auto" else [args.engine]
    preflight_env = dict(os.environ)
    preflight_env.update(overrides)
    readiness = [preflight(name, env=preflight_env, format_file=format_file) for name in candidates]
    available = next((item for item in readiness if item["ready"]), None)
    if args.preflight or available is None:
        print(json.dumps({"preflight": readiness, "compile_started": False}, indent=2))
        return 0 if available else 2
    source, preamble = args.source.resolve(), args.preamble.resolve()
    if not source.is_file() or not preamble.is_file():
        print(json.dumps({"error": "The specified source or preamble file is missing", "compile_started": False}))
        return 2
    directory = Path(tempfile.mkdtemp(prefix="sp04_texcheck_"))
    # Pure byte copies: no text decoding, substitutions, macro overrides, or
    # parsing of the transcription. The original deliverables stay untouched.
    shutil.copyfile(source, directory / "transcription.tex")
    shutil.copyfile(preamble, directory / "PREAMBLE.tex")
    digest = hashlib.sha256((directory / "transcription.tex").read_bytes()).hexdigest()
    jobs = []
    if args.probes:
        for name, body in PROBES.items():
            stem = "probe_" + name
            (directory / f"{stem}.tex").write_text("\\input{PREAMBLE.tex}\n\\begin{document}\n" + body + "\n\\end{document}\n", encoding="utf-8")
            jobs.append(run_tex(available["executable"], directory, stem, args.timeout, overrides, format_file, output_format))
    (directory / "compile_check.tex").write_text(
        "\\input{PREAMBLE.tex}\n\\begin{document}\n\\input{transcription.tex}\n\\end{document}\n", encoding="utf-8")
    jobs.append(run_tex(available["executable"], directory, "compile_check", args.timeout, overrides, format_file, output_format))
    report = {"directory": str(directory), "engine": available["engine"],
              "source": str(source), "staged_source_sha256": digest,
              "preamble_unchanged": True, "output_format": output_format, "jobs": jobs,
              "all_passed": all(job["exit_code"] == 0 and job["output_created"] for job in jobs)}
    (directory / "result.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
