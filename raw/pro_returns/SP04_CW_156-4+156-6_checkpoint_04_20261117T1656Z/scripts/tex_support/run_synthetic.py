#!/usr/bin/env python3
"""Build an isolated format and validate only invented exact-preamble probes.

No manuscript/page/witness/context input is accepted. No system path is written.
The supplied preamble and official CTAN ulem.sty are copied byte-for-byte.
"""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
PREAMBLE = HERE.parents[1] / "PREAMBLE.tex"
ULEM_SHA256 = "c97c15736b46cf13071c52070c07aa933fc8253748422d0df56e97286b563685"
PROBES = {
    "diplomatic_math": r"""\cotefile{synthetic}\scanpage{0}\mspage{0}
Text \unsure{word}, \deleted{word}, \inserted{word},
\uline{underlined}, \uuline{double underlined}.
$\unsure{x_i}$, $\deleted{x_i}$, $\inserted{x_i}$, \deleted{$x_i$}.
\[\deleted{x_i+y_j}=\unsure{z^!}.\]
\margin{Synthetic marginal annotation.}
""",
    "nested_deletions": r"""\deleted{outer \deleted{inner} outer}.
$\deleted{x+\deleted{y}}$.
\deleted{outer $\deleted{x_i}$ outer}.
\deleted{outer \inserted{added} outer}.
""",
    "tikz": r"""\diagram{\begin{tikzcd}[ampersand replacement=\&]
X_i \arrow[r,"{\deleted{f}}"] \arrow[d,"g"'] \& Y^! \arrow[d,"h"] \\
Z \arrow[r,"{\unsure{k}}"'] \& T
\end{tikzcd}}
\figure{\begin{tikzpicture}\draw[->] (0,0)--(1,1);
\node at (0,0) {$\deleted{x_i}$};\node at (1,1) {$\unsure{y^!}$};
\end{tikzpicture}}
""",
}


def stamp():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def log(event):
    with (HERE / "setup.log").open("a", encoding="utf-8") as stream:
        stream.write(stamp() + " " + json.dumps(event, ensure_ascii=False) + "\n")


def invoke(command, directory, env, label):
    log({"action": label, "argv": command, "cwd": str(directory),
         "environment_overrides": {k: env[k] for k in ["TEXMF", "TEXMFVAR", "TEXMFCONFIG", "TEXMFCACHE", "TEXMFOUTPUT", "MKTEXFMT", "MKTEXPK", "MKTEXTFM", "openout_any"]}})
    result = subprocess.run(command, cwd=directory, env=env, capture_output=True,
                            text=True, errors="replace", timeout=90)
    (directory / (label + ".stdout.txt")).write_text(result.stdout, encoding="utf-8")
    (directory / (label + ".stderr.txt")).write_text(result.stderr, encoding="utf-8")
    outcome = {"action": label, "returncode": result.returncode,
               "stdout_file": str(directory / (label + ".stdout.txt")),
               "stderr_file": str(directory / (label + ".stderr.txt"))}
    log(outcome)
    return result


def main():
    package = HERE / "ulem.sty"
    if not PREAMBLE.is_file() or not package.is_file():
        raise SystemExit("Supplied preamble or official local ulem package is missing")
    if digest(package) != ULEM_SHA256:
        raise SystemExit("Local ulem source differs from the recorded CTAN retrieval")
    engine = shutil.which("pdftex")
    if engine is None:
        raise SystemExit("pdftex executable is unavailable")
    work = Path(tempfile.mkdtemp(prefix="sp04_exact_tex_"))
    env = dict(os.environ)
    env.update(TEXMF="{/usr/local/share/texmf,/etc/texmf,/var/lib/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}",
               TEXMFVAR=str(work / "var"), TEXMFCONFIG=str(work / "config"),
               TEXMFCACHE=str(work / "cache"), TEXMFOUTPUT=str(work),
               MKTEXFMT="0", MKTEXPK="0", MKTEXTFM="0", openout_any="p")
    shutil.copyfile(PREAMBLE, work / "PREAMBLE.tex")
    shutil.copyfile(package, work / "ulem.sty")
    log({"action": "isolated_setup", "work_directory": str(work),
         "preamble_source": str(PREAMBLE), "preamble_sha256": digest(PREAMBLE),
         "staged_preamble_sha256": digest(work / "PREAMBLE.tex"),
         "ulem_sha256": digest(package), "input_scope": "synthetic probes only"})
    initialization = [engine, "-ini", "-etex", "-interaction=nonstopmode", "-halt-on-error",
                      "-progname=pdflatex", "-jobname=pdflatex", "pdflatex.ini"]
    built = invoke(initialization, work, env, "format_initialization")
    if built.returncode != 0 or not (work / "pdflatex.fmt").is_file():
        result = {"work_directory": str(work), "status": "blocked_format_initialization",
                  "returncode": built.returncode, "tail": built.stdout.splitlines()[-20:]}
        (HERE / "synthetic_result.json").write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps(result, indent=2))
        return 1
    results = []
    for name, body in PROBES.items():
        (work / (name + ".tex")).write_text("\\input{PREAMBLE.tex}\n\\begin{document}\n" + body + "\n\\end{document}\n", encoding="utf-8")
        command = [engine, "-fmt=" + str(work / "pdflatex.fmt"), "-progname=pdflatex", "-output-format=dvi",
                   "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", name + ".tex"]
        compiled = invoke(command, work, env, name)
        item = {"probe": name, "returncode": compiled.returncode,
                "dvi_created": (work / (name + ".dvi")).is_file(),
                "log": str(work / (name + ".log"))}
        if compiled.returncode != 0:
            item["tail"] = compiled.stdout.splitlines()[-20:]
        results.append(item)
    unchanged = digest(PREAMBLE) == digest(work / "PREAMBLE.tex")
    result = {"work_directory": str(work), "format": str(work / "pdflatex.fmt"),
              "preamble_unchanged": unchanged, "ulem_sha256": digest(package), "probes": results,
              "all_passed": unchanged and all(r["returncode"] == 0 and r["dvi_created"] for r in results),
              "output_kind": "DVI", "manuscript_content_accessed": False}
    # Preserve administrative evidence with the helper, excluding the generated
    # format (it is reproducible from the logged initialization command).
    evidence = HERE / "synthetic_evidence"
    evidence.mkdir(exist_ok=True)
    for item in work.iterdir():
        if item.is_file() and (item.suffix in {".log", ".txt", ".dvi"} or item.name in {name + ".tex" for name in PROBES}):
            shutil.copyfile(item, evidence / item.name)
    result["preserved_evidence"] = str(evidence)
    (HERE / "synthetic_result.json").write_text(json.dumps(result, indent=2) + "\n")
    log({"action": "synthetic_validation_complete", "result": result})
    print(json.dumps(result, indent=2))
    return 0 if result["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
