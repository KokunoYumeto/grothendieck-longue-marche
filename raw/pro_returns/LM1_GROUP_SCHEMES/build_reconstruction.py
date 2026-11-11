#!/usr/bin/env python3
"""Rebuild the chat-delivered reconstruction. No network access.

Requirements: Python 3, Node.js, LuaLaTeX, BibTeX, and the TeX
packages named in LM1_GROUP_SCHEMES_paper.tex.

This helper was supplied after the workspace outage and was not run
in the research session. It preserves the supplied stdout certificates.
"""
from pathlib import Path
import csv
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parent
MAIN = ROOT / "LM1_GROUP_SCHEMES_paper.tex"
BIB = ROOT / "LM1_GROUP_SCHEMES_references.bib"
SECTIONS = [
    ROOT / "sections" / name
    for name in ["00_conventions.tex", "A.tex", "B.tex", "C.tex",
                 "D.tex", "E.tex", "F.tex"]
]
PROGRAM_NAMES = [
    "ab_reconstructed",
    "c_replacement",
    "d_reconstructed",
    "e_arithmetic_replacement",
    "e_groups_replacement",
    "e_fermat",
]
PROGRAMS = [ROOT / "code" / (name + ".js") for name in PROGRAM_NAMES]
OUTPUTS = [ROOT / "code" / (name + ".out") for name in PROGRAM_NAMES]
REQUIRED = [
    MAIN, BIB, ROOT / "results.csv", ROOT / "readings.csv",
    ROOT / "report.md", ROOT / "code" / "e_additional.py",
    *SECTIONS, *PROGRAMS, *OUTPUTS,
]
missing = [str(p.relative_to(ROOT)) for p in REQUIRED if not p.is_file()]
if missing:
    raise SystemExit("Missing delivered inputs:\n" + "\n".join(missing))

# Explicitly disclosed transcription repairs; no mathematical source
# or bibliographic content is silently invented.
repairs = {
    ROOT / "sections" / "A.tex": [
        ("Its unique fixed line is",
         "Its unique line on which the operator acts pointwise as the identity is")
    ],
    ROOT / "sections" / "F.tex": [
        (r"$(\mathbb Z/n)^r and", r"$(\mathbb Z/n)^r$ and")
    ],
    ROOT / "code" / "d_reconstructed.js": [
        ("p[0]===a&&p[1]===b&&p[1]===b",
         "p[0]===a&&p[1]===b")
    ],
}
for path, replacements in repairs.items():
    old = path.read_text(encoding="utf-8")
    new = old
    for before, after in replacements:
        new = new.replace(before, after)
    if new != old:
        path.write_text(new, encoding="utf-8")

with (ROOT / "results.csv").open(encoding="utf-8", newline="") as stream:
    rows = list(csv.DictReader(stream))
expected = {
    f"{part}.{i}"
    for part, count in [("A", 11), ("B", 23), ("C", 11),
                        ("D", 21), ("E", 28), ("F", 3)]
    for i in range(1, count + 1)
}
ids = [row["id"] for row in rows]
if len(ids) != 97 or len(set(ids)) != 97 or set(ids) != expected:
    raise SystemExit("The statement register must contain exactly the 97 expected IDs.")
allowed = {"Proved", "Refuted", "Known", "Open", "Unfinished"}
if any(row["status"] not in allowed for row in rows):
    raise SystemExit("Unrecognized statement status.")

with (ROOT / "readings.csv").open(encoding="utf-8", newline="") as stream:
    readings = list(csv.DictReader(stream))
if len(readings) != 57 or len({r["id"] for r in readings}) != 57:
    raise SystemExit("The reconstructed readings register must have 57 unique rows.")

tex = "\n".join(p.read_text(encoding="utf-8") for p in [MAIN, *SECTIONS])
paper_ids = re.findall(r"\\begin\{statement\}\{([^}]+)\}", tex)
if len(paper_ids) != 97 or set(paper_ids) != expected:
    raise SystemExit("The paper's numbered statements do not match the register.")
cited = set()
for match in re.finditer(
    r"\\cite[a-zA-Z]*\s*(?:
$$
[^
$$
]*\]\s*){0,2}\{([^}]*)\}", tex
):
    cited.update(k.strip() for k in match.group(1).split(",") if k.strip())
bib_keys = set(re.findall(
    r"@\w+\s*\{\s*([^,\s]+)", BIB.read_text(encoding="utf-8")
))
unresolved = sorted(cited - bib_keys)
if unresolved:
    raise SystemExit(
        "Unresolved citation keys; recover or verify their actual sources "
        "before continuing:\n" + "\n".join(unresolved)
    )

LOGS = ROOT / "build"
LOGS.mkdir(exist_ok=True)

def run(command, log_name):
    completed = subprocess.run(
        command, cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        check=False,
    )
    (LOGS / log_name).write_text(completed.stdout, encoding="utf-8")
    if completed.returncode:
        raise SystemExit(
            f"Command failed with code {completed.returncode}: {command}\n"
            f"See build/{log_name}"
        )
    return completed.stdout

for program, expected_output in zip(PROGRAMS, OUTPUTS):
    actual = run(["node", str(program)], program.stem + ".rerun.out")
    supplied = expected_output.read_text(encoding="utf-8")
    if actual.strip() != supplied.strip():
        raise SystemExit(
            f"Output mismatch for {program.name}; "
            "the supplied certificate has not been overwritten."
        )

stem = MAIN.stem
run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", MAIN.name],
    "lualatex-pass1.txt")
run(["bibtex", stem], "bibtex.txt")
run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", MAIN.name],
    "lualatex-pass2.txt")
run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", MAIN.name],
    "lualatex-pass3.txt")
final_log = (ROOT / (stem + ".log")).read_text(
    encoding="utf-8", errors="replace"
)
if "There were undefined references" in final_log or "Citation" in final_log and "undefined" in final_log:
    raise SystemExit("The final TeX log still contains unresolved references or citations.")

PDF = ROOT / (stem + ".pdf")
if not PDF.is_file() or not PDF.read_bytes().startswith(b"%PDF-"):
    raise SystemExit("No valid PDF header was produced.")

ARCHIVE = ROOT / "LM1_GROUP_SCHEMES_reconstruction.zip"
members = [*REQUIRED, Path(__file__).resolve(), PDF, *sorted(LOGS.iterdir())]
with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED) as archive:
    for path in members:
        archive.write(path, path.relative_to(ROOT))

print("Compiled the reconstruction and matched all six JavaScript outputs.")
print("Statement rows: 97. Reading rows: 57.")
print("Archive:", ARCHIVE.name)
print("Visual PDF review has not been performed by this helper.")
print("The report's mathematical and recovery limitations remain in force.")
