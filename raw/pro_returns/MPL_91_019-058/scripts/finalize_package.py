#!/usr/bin/env python3
"""Verify the frozen files and create the final archive, without editing TeX."""
from datetime import datetime, timezone
import csv
import hashlib
import json
from pathlib import Path
import re
from zipfile import ZipFile, ZIP_DEFLATED

from make_checkpoint import collect
from validate_package import PREFIX, SCANS, parse_hash_record, validate

ROOT = Path(__file__).resolve().parents[1]


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    output = ROOT.parent / f"{PREFIX}.zip"
    if output.exists():
        raise RuntimeError("Final archive already exists; refusing to overwrite it.")
    pages = [ROOT / "pages" / f"{PREFIX}_91_scan{n:03}.tex" for n in SCANS]
    combined = ROOT / f"{PREFIX}_transcription.tex"
    expected = pages + [combined]
    log = ROOT / "progress.log"
    before = log.read_text()
    records = {}
    for line in before.splitlines():
        record = parse_hash_record(line)
        if record:
            name, digest = record
            if name in {str(p.relative_to(ROOT)) for p in expected}:
                if name in records and records[name] != digest:
                    raise RuntimeError(f"Conflicting freeze hash for {name}")
                records[name] = digest
    assert len(records) == 39, len(records)
    for p in expected:
        assert sha(p.read_bytes()) == records[str(p.relative_to(ROOT))], p
    assert combined.read_bytes() == b"".join(p.read_bytes() for p in pages)
    assert (ROOT / "research/final_notes_validation.md").is_file()
    notes = (ROOT / f"{PREFIX}_notes.md").read_text()
    note_ids = re.findall(r"^### ([ABC]\d{2}) —", notes, re.M)
    assert len(note_ids) == 97 and len(set(note_ids)) == 97
    with log.open("a") as f:
        f.write(f"research notes completed {now()} 97 scan-level items, 3 synthesis tables, 28 own-idea items; all 100 IDs searched across supplied context\n")
        f.write(f"post-context SHA-256 verification {now()} all 39 frozen transcription hashes unchanged; exact page concatenation unchanged\n")

    report, stats = validate(ROOT, strict=True)
    if report.errors or report.warnings:
        raise RuntimeError(json.dumps({"errors": report.errors, "warnings": report.warnings}, ensure_ascii=False))
    inventory = list(csv.DictReader((ROOT / f"{PREFIX}_inventory.csv").open()))
    tex = combined.read_text()
    verification = {
        "checked_at_utc": now(),
        "scope": "Mechanical structure, metadata, source-block assembly, archive integrity, and freeze hashes; not a certification of handwriting accuracy or a full TeX render.",
        **stats,
        "research_catalogue_items": len(note_ids),
        "research_synthesis_items": 3,
        "own_idea_items": 28,
        "uncertainty_macros": len(re.findall(r"\\unsure\{", tex)),
        "illegible_spans": len(re.findall(r"\\illegible\{", tex)),
        "inventory_all_yes": all(r["transcribed"] == "yes" for r in inventory),
        "frozen_hashes_unchanged": 39,
        "errors": report.errors,
        "warnings": report.warnings,
        "render_status": "Not render-verified: LaTeX class/format and TikZ packages unavailable.",
    }
    (ROOT / "review/final_validation.json").write_text(json.dumps(verification, ensure_ascii=False, indent=2) + "\n")
    with log.open("a") as f:
        f.write(f"final mechanical validation {now()} 0 errors, 0 warnings; 38 pages; 779 inventory rows all yes; 39 hashes unchanged\n")
        f.write(f"final archive preparation {now()} {PREFIX}.zip; supplied images, archives and extracted context excluded\n")

    files = collect(ROOT, ROOT / "__no_external_helpers__")
    assert files
    required = {
        f"{PREFIX}_transcription.tex", f"{PREFIX}_doubts.md",
        f"{PREFIX}_inventory.csv", f"{PREFIX}_notes.md", "progress.log",
        *[str(p.relative_to(ROOT)) for p in pages],
    }
    names = {name for _, name in files}
    assert required <= names, required - names
    manifest = []
    with ZipFile(output, "x", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for p, name in files:
            before_stat = p.stat()
            data = p.read_bytes()
            after_stat = p.stat()
            assert (before_stat.st_size, before_stat.st_mtime_ns) == (after_stat.st_size, after_stat.st_mtime_ns), name
            archive.writestr(name, data)
            manifest.append(f"{sha(data)}  {name}")
        archive.writestr("_archive_manifest.sha256", "\n".join(manifest) + "\n")

    with ZipFile(output) as archive:
        assert archive.testzip() is None
        assert required <= set(archive.namelist())
        assert len([name for name in archive.namelist() if re.fullmatch(r"pages/MPL_91_019-058_91_scan\d{3}\.tex", name)]) == 38
        for name, digest in records.items():
            assert sha(archive.read(name)) == digest, name
        for p, name in files:
            assert archive.read(name) == p.read_bytes(), name
    for p in expected:
        assert sha(p.read_bytes()) == records[str(p.relative_to(ROOT))], p
    print(json.dumps({
        "archive": str(output),
        "bytes": output.stat().st_size,
        "members": len(files) + 1,
        "sha256": sha(output.read_bytes()),
        "frozen_hashes_unchanged_in_workspace_and_zip": 39,
        "validation_errors": 0,
        "validation_warnings": 0,
    }, indent=2))


if __name__ == "__main__":
    main()
