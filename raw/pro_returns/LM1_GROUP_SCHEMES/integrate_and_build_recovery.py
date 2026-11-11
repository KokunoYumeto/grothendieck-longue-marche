#!/usr/bin/env python3
"""Integrate the recovery addendum; optionally verify, build, and archive.

Usage:
    python3 integrate_and_build_recovery.py
    python3 integrate_and_build_recovery.py --build
    python3 integrate_and_build_recovery.py --build --render

Run from the reconstructed edition's root, or pass --root PATH.
This helper was supplied as source and was not executed against the
complete edition during the conversation.
"""

from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile


COUNTS = {"A": 11, "B": 23, "C": 12, "D": 21, "E": 28, "F": 3}
EXPECTED_IDS = {
    f"{part}.{number}"
    for part, count in COUNTS.items()
    for number in range(1, count + 1)
}
EXPECTED_STATUSES = {
    "proved": 72,
    "refuted": 16,
    "known": 4,
    "open": 5,
    "unfinished": 1,
}
PROGRAMS = [
    ("node", "ab_reconstructed", "js"),
    ("node", "c_replacement", "js"),
    ("node", "d_reconstructed", "js"),
    ("node", "e_arithmetic_replacement", "js"),
    ("node", "e_groups_replacement", "js"),
    ("node", "e_fermat", "js"),
    ("python", "e_additional", "py"),
]
MAIN = "LM1_GROUP_SCHEMES_paper"
UPDATE_START = "<!-- BEGIN RECOVERY UPDATE C12 -->"
UPDATE_END = "<!-- END RECOVERY UPDATE C12 -->"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def normalize_id(value):
    match = re.fullmatch(r"([A-F])\.?(\d+)", str(value).strip())
    require(match is not None, f"Invalid statement ID: {value!r}")
    return f"{match.group(1)}.{int(match.group(2))}"


def read_text(path):
    require(path.is_file(), f"Missing required file: {path}")
    return path.read_text(encoding="utf-8")


def write_changed(root, path, value):
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old == value:
        return
    if old is not None:
        backup = root / "build" / "pre_addendum" / path.relative_to(root)
        backup.parent.mkdir(parents=True, exist_ok=True)
        if not backup.exists():
            backup.write_text(old, encoding="utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames
        rows = list(reader)
    require(fields is not None, f"Missing CSV header: {path}")
    return fields, rows


def csv_text(fields, rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


def cell(value):
    if isinstance(value, list):
        return "; ".join(str(item) for item in value)
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def bib_keys(text):
    return set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", text))


def integrate(root):
    addendum_path = root / "sections" / "C12_addendum.tex"
    addendum = read_text(addendum_path)
    require(
        re.search(r"\\begin\{statement\}\{C\.12\}\{Proved\}", addendum),
        "The addendum must contain the proved C.12 statement.",
    )

    main_path = root / f"{MAIN}.tex"
    main_text = read_text(main_path)
    new_input = r"\input{sections/C12_addendum.tex}"
    if new_input not in main_text:
        anchor = re.search(r"\\input\{sections/C(?:\.tex)?\}", main_text)
        require(anchor is not None, "Cannot locate the Part C input.")
        main_text = (
            main_text[:anchor.end()]
            + "\n"
            + new_input
            + main_text[anchor.end():]
        )
        write_changed(root, main_path, main_text)

    bibliography_path = root / "LM1_GROUP_SCHEMES_references.bib"
    bibliography = read_text(bibliography_path)
    extra_bibliography = read_text(root / "evidence" / "C12_references.bib")
    existing = bib_keys(bibliography)
    additional = bib_keys(extra_bibliography)
    require(len(additional) == 5, "Expected five addendum bibliography keys.")
    if not additional.issubset(existing):
        require(
            not (additional & existing),
            "Only part of the addendum bibliography is present; review manually.",
        )
        bibliography += (
            "\n\n% C12 recovery addendum references\n"
            + extra_bibliography.rstrip()
            + "\n"
        )
        write_changed(root, bibliography_path, bibliography)

    result_path = root / "results.csv"
    fields, rows = read_csv(result_path)
    required_fields = {
        "id", "statement", "status", "where_proved", "depends_on",
        "manuscript_passages", "depends_on_doubtful_reading", "notes",
    }
    require(
        required_fields.issubset(fields),
        "results.csv does not have the expected metadata columns.",
    )
    result = json.loads(read_text(root / "evidence" / "C12_result.json"))
    require(normalize_id(result["id"]) == "C.12", "Wrong addendum result ID.")
    new_row = {field: cell(result.get(field, "")) for field in fields}
    new_row["id"] = "C.12"
    new_row["status"] = "Proved"

    updated = []
    found_c11 = False
    for row in rows:
        statement_id = normalize_id(row["id"])
        if statement_id == "C.12":
            continue
        if statement_id == "C.10":
            note = " C.12 extends the square-determinant image conclusion to Z/4."
            if note.strip() not in row["notes"]:
                row["notes"] += note
        if statement_id == "C.11":
            found_c11 = True
            row["statement"] = (
                "Full abstract descriptions of the descended Artinian source "
                "groups, and comparison of A_s(Z), A_p(Z) with their ordinary "
                "integral word subgroups, remain unproved here. The finite "
                "Z/4 image question formerly included here is resolved by C.12."
            )
            row["status"] = "Open"
            row["where_proved"] = (
                "C.11: remaining source-section questions; "
                "C.12: the settled Z/4 projective image"
            )
            if not re.search(r"\bC\.?12\b", row["depends_on"]):
                row["depends_on"] = (
                    row["depends_on"].rstrip("; ") + "; C.12"
                ).lstrip("; ")
            row["notes"] = (
                "C.12 proves image PSL2(Z/4), order 24, and excludes "
                "[diag(3,1)]. Keep the broader source-section and integral "
                "comparison questions unresolved. The older bounded-search "
                "output is preserved as historical computation evidence."
            )
        updated.append(row)
        if statement_id == "C.11":
            updated.append(new_row)
    require(found_c11, "Cannot find the existing C.11 result.")
    write_changed(root, result_path, csv_text(fields, updated))

    repairs = [
        (
            root / "sections" / "A.tex",
            "Its unique fixed line is",
            "Its unique line on which the operator acts pointwise "
            "as the identity is",
        ),
        (
            root / "sections" / "F.tex",
            r"indexed by $(\mathbb Z/n)^r and",
            r"indexed by $(\mathbb Z/n)^r$ and",
        ),
        (
            root / "code" / "d_reconstructed.js",
            "p[0]===a&&p[1]===b&&p[1]===b",
            "p[0]===a&&p[1]===b",
        ),
    ]
    for path, old, new in repairs:
        contents = read_text(path)
        if old in contents:
            write_changed(root, path, contents.replace(old, new))

    report_path = root / "report.md"
    report = read_text(report_path)
    report = re.sub(
        re.escape(UPDATE_START) + r".*?" + re.escape(UPDATE_END) + r"\n*",
        "",
        report,
        flags=re.S,
    )
    lines = report.splitlines(keepends=True)
    first = next((i for i, line in enumerate(lines) if line.strip()), None)
    require(
        first is not None and lines[first].lstrip().startswith("|"),
        "report.md must begin with its full outcome table.",
    )
    position = first
    while position < len(lines) and lines[position].lstrip().startswith("|"):
        position += 1
    update = read_text(root / "RECOVERY_UPDATE.md").rstrip()
    insertion = (
        "\n"
        + UPDATE_START
        + "\n"
        + update
        + "\n"
        + UPDATE_END
        + "\n\n"
    )
    write_changed(
        root,
        report_path,
        "".join(lines[:position]) + insertion + "".join(lines[position:]),
    )


def verify_registers(root):
    _, results = read_csv(root / "results.csv")
    ids = [normalize_id(row["id"]) for row in results]
    require(len(ids) == len(set(ids)), "Duplicate statement IDs.")
    require(set(ids) == EXPECTED_IDS, "The result ID set is not the expected 98.")
    statuses = collections.Counter(
        row["status"].strip().lower() for row in results
    )
    require(
        dict(statuses) == EXPECTED_STATUSES,
        f"Unexpected status totals: {dict(statuses)}",
    )
    _, readings = read_csv(root / "readings.csv")
    require(len(readings) == 57, "Expected the 57-row reading register.")

    paths = [root / f"{MAIN}.tex"]
    paths += [
        root / "sections" / name
        for name in (
            "00_conventions.tex", "A.tex", "B.tex", "C.tex",
            "C12_addendum.tex", "D.tex", "E.tex", "F.tex",
        )
    ]
    combined = "\n".join(read_text(path) for path in paths)
    theorem_ids = re.findall(
        r"\\begin\{statement\}\{([A-F]\.\d+)\}", combined
    )
    require(
        len(theorem_ids) == 98 and set(theorem_ids) == EXPECTED_IDS,
        "The LaTeX statement IDs do not match results.csv.",
    )
    bibliography = read_text(root / "LM1_GROUP_SCHEMES_references.bib")
    cited = set()
    pattern = r"\\cite[a-zA-Z]*\*?(?:
$$
[^
$$
]*\]){0,2}\{([^}]+)\}"
    for match in re.finditer(pattern, combined):
        cited.update(key.strip() for key in match.group(1).split(","))
    missing = cited - bib_keys(bibliography)
    require(not missing, f"Missing bibliography keys: {sorted(missing)}")
    return {
        "statements": len(ids),
        "statuses": dict(statuses),
        "readings": len(readings),
        "citation_keys_checked": len(cited),
    }


def run_logged(root, command, label):
    result = subprocess.run(
        command, cwd=root, capture_output=True, text=True, check=False
    )
    log_directory = root / "build" / "verification"
    log_directory.mkdir(parents=True, exist_ok=True)
    (log_directory / f"{label}.stdout").write_text(
        result.stdout, encoding="utf-8"
    )
    (log_directory / f"{label}.stderr").write_text(
        result.stderr, encoding="utf-8"
    )
    require(result.returncode == 0, f"{label} failed; see its saved logs.")
    return result.stdout


def normalized_output(value):
    return value.replace("\r\n", "\n").rstrip("\n")


def build(root, render):
    verification = verify_registers(root)
    node = shutil.which("node")
    lualatex = shutil.which("lualatex")
    bibtex = shutil.which("bibtex")
    require(node and lualatex and bibtex, "Node, LuaLaTeX, and BibTeX are required.")

    computations = []
    for interpreter, stem, extension in PROGRAMS:
        source = root / "code" / f"{stem}.{extension}"
        expected = root / "code" / f"{stem}.out"
        read_text(source)
        expected_output = read_text(expected)
        executable = node if interpreter == "node" else sys.executable
        actual = run_logged(root, [executable, str(source)], stem)
        require(
            normalized_output(actual) == normalized_output(expected_output),
            f"Output mismatch for {stem}; original and fresh outputs are preserved.",
        )
        computations.append({
            "program": source.relative_to(root).as_posix(),
            "matched_supplied_output": True,
            "stdout_sha256": hashlib.sha256(actual.encode()).hexdigest(),
        })

    (root / "build").mkdir(exist_ok=True)
    latex_command = [
        lualatex, "-interaction=nonstopmode", "-halt-on-error",
        "-file-line-error", "-output-directory=build", f"{MAIN}.tex",
    ]
    run_logged(root, latex_command, "lualatex-1")
    run_logged(root, [bibtex, f"build/{MAIN}"], "bibtex")
    run_logged(root, latex_command, "lualatex-2")
    run_logged(root, latex_command, "lualatex-3")

    log = read_text(root / "build" / f"{MAIN}.log")
    require(
        not re.search(
            r"undefined (?:references|citations)|"
            r"(?:Reference|Citation) .*? undefined",
            log,
            flags=re.I,
        ),
        "Unresolved references or citations remain in the LaTeX log.",
    )
    generated_pdf = root / "build" / f"{MAIN}.pdf"
    require(generated_pdf.is_file(), "LuaLaTeX produced no PDF.")
    require(
        generated_pdf.read_bytes().startswith(b"%PDF-"),
        "The generated file has no PDF header.",
    )
    final_pdf = root / f"{MAIN}.pdf"
    shutil.copyfile(generated_pdf, final_pdf)

    verification["computations"] = computations
    verification["pdf_sha256"] = hashlib.sha256(
        final_pdf.read_bytes()
    ).hexdigest()
    verification["overfull_box_warnings"] = len(
        re.findall(r"Overfull \\[hv]box", log)
    )
    verification["visual_review_performed"] = False

    if render:
        pdftoppm = shutil.which("pdftoppm")
        require(pdftoppm, "pdftoppm is required for --render.")
        page_directory = root / "build" / "pages"
        page_directory.mkdir(parents=True, exist_ok=True)
        run_logged(
            root,
            [
                pdftoppm, "-png", "-r", "100",
                str(final_pdf), str(page_directory / "page"),
            ],
            "render",
        )
        verification["rendered_page_images"] = len(
            list(page_directory.glob("page-*.png"))
        )

    verification_path = root / "build" / "verification.json"
    verification_path.write_text(
        json.dumps(verification, indent=2) + "\n", encoding="utf-8"
    )

    members = []
    for pattern in ("*.tex", "*.bib", "*.csv", "*.md", "*.py", "*.pdf"):
        members.extend(root.glob(pattern))
    for directory in ("sections", "code", "evidence"):
        members.extend(
            path for path in (root / directory).rglob("*") if path.is_file()
        )
    members.append(verification_path)
    members.extend(
        path for path in (root / "build" / "verification").rglob("*")
        if path.is_file()
    )
    members.append(root / "build" / f"{MAIN}.log")

    archive = root.parent / "LM1_GROUP_SCHEMES_reconstructed_20261111.zip"
    with zipfile.ZipFile(
        archive, "w", compression=zipfile.ZIP_DEFLATED
    ) as handle:
        for path in sorted(set(members)):
            handle.write(
                path,
                (Path("LM1_GROUP_SCHEMES") / path.relative_to(root)).as_posix(),
            )

    print(json.dumps({
        "archive": str(archive),
        "pdf": str(final_pdf),
        "verification": verification,
        "notice": "Rendering is not visual review. Inspect the final PDF.",
    }, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parent
    )
    parser.add_argument("--build", action="store_true")
    parser.add_argument("--render", action="store_true")
    arguments = parser.parse_args()
    require(not arguments.render or arguments.build, "--render requires --build.")
    root = arguments.root.resolve()
    integrate(root)
    verification = verify_registers(root)
    if arguments.build:
        build(root, arguments.render)
    else:
        print(json.dumps({
            "integration": "completed",
            "register_verification": verification,
            "full_pdf_build_performed": False,
            "visual_review_performed": False,
        }, indent=2))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Recovery integration/build failed: {error}", file=sys.stderr)
        raise SystemExit(1)
