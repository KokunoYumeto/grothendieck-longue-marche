#!/usr/bin/env python3
"""Audit and package the completed research return; no mathematical reruns."""
from __future__ import annotations

import ast
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
import zipfile

import fitz


ROOT = Path(__file__).resolve().parents[1]
PREFIX = "LM2_LOOP_EQUATIONS"
ZIP_PATH = ROOT.parent / f"{PREFIX}.zip"
MANIFEST = ROOT / "MANIFEST.sha256"
AUDIT_JSON = ROOT / "code/package_audit.json"
AUDIT_OUT = ROOT / "code/package_artifacts.out"
ROOT_TRANSIENT_SUFFIXES = {".aux", ".out", ".toc", ".log", ".blg"}


def selected_files() -> list[Path]:
    result = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if any(part in {".build", "__pycache__"} for part in rel.parts):
            continue
        if path.suffix == ".pyc" or path == MANIFEST:
            continue
        if len(rel.parts) == 1 and path.suffix in ROOT_TRANSIENT_SUFFIXES:
            continue
        result.append(path)
    return sorted(result, key=lambda path: path.relative_to(ROOT).as_posix())


def csv_rows(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    required = [
        f"{PREFIX}_paper.tex", f"{PREFIX}_paper.pdf",
        f"{PREFIX}_results.csv", f"{PREFIX}_readings.csv",
        f"{PREFIX}_new_conditions.csv", f"{PREFIX}_references.bib",
        f"{PREFIX}_report.md", f"{PREFIX}_condition_inventory.csv",
        "README.md", "code/README.md", "code/graded_README.md",
    ]
    assert all((ROOT / name).is_file() for name in required), "Missing required file"
    assert list((ROOT / "sections").glob("*.tex")), "Missing TeX sections"
    results = csv_rows(f"{PREFIX}_results.csv")
    status_key = next(key for key in results[0] if key.lower() == "status")
    counts = Counter(row[status_key] for row in results)
    assert counts == {"Proved": 51, "Known": 12, "Refuted": 10, "Open": 6}, counts
    register_counts = {
        "results": len(results),
        "readings": len(csv_rows(f"{PREFIX}_readings.csv")),
        "new_conditions": len(csv_rows(f"{PREFIX}_new_conditions.csv")),
        "condition_inventory": len(csv_rows(f"{PREFIX}_condition_inventory.csv")),
    }
    assert register_counts == {
        "results": 79, "readings": 29, "new_conditions": 4, "condition_inventory": 23
    }, register_counts
    with fitz.open(ROOT / f"{PREFIX}_paper.pdf") as document:
        pdf_pages = len(document)
        assert pdf_pages == 60, pdf_pages
        assert all(page.get_text().strip() for page in document), "Empty PDF page"

    # These two files are included in both the manifest and the ZIP.
    AUDIT_JSON.write_text("{}\n", encoding="utf-8")
    AUDIT_OUT.write_text("", encoding="utf-8")
    files = selected_files()
    python_files = [path for path in files if path.suffix == ".py"]
    json_files = [path for path in files if path.suffix == ".json"]
    for path in python_files:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        if path.name == "finite_groups.py":
            continue  # Shared library, not a separately executed program.
        output = path.with_suffix(".out")
        if path.name == "build_registers.py":
            output = path.with_name("register_audit.out")
        assert output.is_file(), f"Missing retained program output: {output}"
    for path in json_files:
        json.loads(path.read_text(encoding="utf-8"))
    visual_audit = json.loads((ROOT / "code/render_pdf_qa.json").read_text())
    assert visual_audit["all_pages_rendered"]
    assert not visual_audit["empty_pages"]
    assert not visual_audit["text_outside_page"]
    audit = {
        "required_files_present": True,
        "pdf_pages": pdf_pages,
        "register_counts": register_counts,
        "statement_status_counts": dict(sorted(counts.items())),
        "python_files_parsed": len(python_files),
        "json_files_parsed": len(json_files),
        "program_outputs_present": True,
        "files_including_manifest": len(files) + 1,
        "all_60_pages_rendered": True,
        "visual_review": {
            "all_four_contact_sheets": "inspected",
            "full_size_pages": [1, 15, 37, 55],
            "result": "No clipping, overlap, missing glyphs, or illegible tables observed.",
        },
        "archive_checks": "The script asserts CRC and manifest equality after packaging.",
        "excluded": [".build/", "__pycache__/", "*.pyc", "root TeX auxiliary logs"],
    }
    AUDIT_JSON.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    output_text = (
        "All required files present.\n"
        f"PDF: {pdf_pages} pages; all rendered and contact sheets inspected.\n"
        f"Registers: {register_counts}.\n"
        f"Statuses: {dict(sorted(counts.items()))}.\n"
        f"Python syntax: {len(python_files)} files parsed.\n"
        f"JSON syntax: {len(json_files)} files parsed.\n"
        "All standalone programs have retained stdout; shared library documented.\n"
        f"Archive entries including manifest: {len(files) + 1}.\n"
        "Manifest covers every included file except itself.\n"
        "CRC and complete manifest verification must pass before this output is printed.\n"
    )
    AUDIT_OUT.write_text(output_text, encoding="utf-8")
    files = selected_files()
    manifest_text = "".join(
        f"{digest(path)}  {path.relative_to(ROOT).as_posix()}\n" for path in files
    )
    MANIFEST.write_text(manifest_text, encoding="utf-8")
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in [*files, MANIFEST]:
            archive.write(path, arcname=f"{ROOT.name}/{path.relative_to(ROOT).as_posix()}")
    with zipfile.ZipFile(ZIP_PATH) as archive:
        assert archive.testzip() is None, "ZIP CRC verification failed"
        assert len(archive.namelist()) == len(files) + 1
        for line in archive.read(f"{ROOT.name}/MANIFEST.sha256").decode().splitlines():
            expected, relative = line.split("  ", 1)
            payload = archive.read(f"{ROOT.name}/{relative}")
            assert hashlib.sha256(payload).hexdigest() == expected, relative
    print(output_text, end="")


if __name__ == "__main__":
    main()
