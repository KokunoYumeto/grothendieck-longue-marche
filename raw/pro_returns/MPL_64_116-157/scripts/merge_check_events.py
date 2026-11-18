#!/usr/bin/env python3
"""Build the five-column check ledger from research/*events.tsv.

The source ledgers remain unchanged. This program normalizes spelling/format,
never upgrades a verification level, and distinguishes direct note coverage
from explicitly cited supporting appendix checks. No transcription is read or
written. Rerun after another source ledger is added.
"""
from __future__ import annotations

import argparse
import collections
import csv
import datetime as dt
import hashlib
import io
import json
import os
from pathlib import Path
import re
import tempfile


HEADER = ("statement_id", "date", "who", "type", "outcome")
ALLOWED_TYPES = frozenset({
    "targeted proof check",
    "independent re-proof",
    "computation or formal certificate",
    "used and rechecked in this run",
    "carried as background without fault found",
})
TYPE_ALIASES = {"used and rechecked": "used and rechecked in this run"}
BACKGROUND = "carried as background without fault found"
REFUTED_PREFIX = "refuted, with refined statement "
REGISTER_DOT = re.compile(
    r"^(LM\d+(?:_[A-Z0-9]+)*|EXIT_TOWER|PUSH_\d+|MPL_\d+_\d+-\d+)"
    r"\.((?:[A-Z]\.[A-Za-z0-9].*)|(?:RN\d+-\d+))$"
)
NOTE_ID = re.compile(r"^([A-Z]\d{2,})(?=$|[.\-])")
APPENDIX_ID = re.compile(r"^(AC\d{2,})(?=$|[.\-])")
REFINEMENT_IN_TYPE = re.compile(r"^refuted, with refined statement (\S+)$")
REFINEMENT_IN_OUTCOME = re.compile(
    r"[Rr]efined statement(?:\s+ID)?\s*[:=]?\s*([A-Z]\d+\.[A-Za-z0-9_.-]+)"
)


def canonical_id(value: str) -> str:
    """Only obvious register/context namespace aliases, never LIT/AC names."""
    match = REGISTER_DOT.fullmatch(value)
    return f"{match[1]} {match[2]}" if match else value


def allowed_type(value: str) -> bool:
    match = REFINEMENT_IN_TYPE.fullmatch(value)
    return value in ALLOWED_TYPES or bool(match and match[1] != "id")


def canonical_date(value: str) -> str:
    """Keep day-only precision; normalize explicit times to UTC ISO 8601."""
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return dt.date.fromisoformat(value).isoformat()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC", value):
        parsed = dt.datetime.strptime(value, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=dt.timezone.utc)
    else:
        parsed = dt.datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
        if parsed.tzinfo is None or parsed.utcoffset() is None:
            raise ValueError("timestamp must include UTC or an explicit timezone offset")
    return parsed.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def atomic_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", newline="", dir=path.parent,
                                     prefix=path.name + ".", suffix=".tmp", delete=False) as handle:
        handle.write(text)
        temporary = Path(handle.name)
    os.replace(temporary, path)


def read_note_blocks(text: str) -> dict[str, str]:
    blocks: dict[str, str] = {}
    for match in re.finditer(r"^### ([A-Z]\d{2,})\s+—[^\n]*\n(.*?)(?=^#{1,3} |\Z)",
                             text, re.M | re.S):
        if match[1] in blocks:
            raise ValueError(f"duplicate main note ID {match[1]}")
        blocks[match[1]] = match[2]
    return blocks


def note_target(statement_id: str, note_ids: set[str]) -> str | None:
    match = NOTE_ID.match(statement_id)
    return match[1] if match and match[1] in note_ids else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workdir", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--expected-notes", type=int, default=71)
    parser.add_argument("--require-complete", action="store_true",
                        help="Exit 1 if any main note lacks a direct ID/refinement event.")
    args = parser.parse_args()
    workdir = args.workdir.resolve()
    research = workdir / "research"
    notes_path = workdir / "MPL_64_116-157_notes.md"
    master_path = workdir / "CHECK_EVENTS.tsv"
    errors: list[str] = []
    warnings: list[str] = []
    normalizations: list[dict] = []
    duplicates: list[dict] = []
    sources: list[dict] = []
    entries: list[dict] = []
    seen: dict[tuple[str, ...], int] = {}
    notes_bytes = b""
    try:
        notes_bytes = notes_path.read_bytes()
        note_blocks = read_note_blocks(notes_bytes.decode("utf-8"))
    except (OSError, UnicodeError, ValueError) as exc:
        note_blocks = {}
        errors.append(f"Main notes: {exc}")
    note_ids = set(note_blocks)
    if len(note_ids) != args.expected_notes:
        errors.append(f"Expected {args.expected_notes} main notes, found {len(note_ids)}")
    source_paths = sorted(research.glob("*events.tsv"))
    if not source_paths:
        errors.append("No research/*events.tsv source ledgers found")

    for path in source_paths:
        source = {"file": str(path.relative_to(workdir)), "sha256": None, "data_rows": 0}
        sources.append(source)
        try:
            source_bytes = path.read_bytes()
            source["sha256"] = hashlib.sha256(source_bytes).hexdigest()
            rows = list(csv.reader(io.StringIO(source_bytes.decode("utf-8-sig"), newline=""),
                                   delimiter="\t", strict=True))
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"{source['file']}: {exc}")
            continue
        if not rows or tuple(rows[0]) != HEADER:
            errors.append(f"{source['file']}: expected exact header {HEADER}")
            continue
        for line_number, original in enumerate(rows[1:], start=2):
            if not original or not any(original):
                warnings.append(f"{source['file']}:{line_number}: skipped blank row")
                continue
            source["data_rows"] += 1
            provenance = {"file": source["file"], "line": line_number}
            if len(original) != 5:
                errors.append(f"{source['file']}:{line_number}: {len(original)} columns, expected 5")
                continue
            row = [field.strip() for field in original]
            if any(not field for field in row):
                errors.append(f"{source['file']}:{line_number}: empty required field")
                continue
            if any(any(char in field for char in "\t\r\n") for field in row):
                errors.append(f"{source['file']}:{line_number}: embedded tab/newline in field")
                continue
            row[0] = canonical_id(row[0])
            try:
                row[1] = canonical_date(row[1])
            except ValueError as exc:
                errors.append(f"{source['file']}:{line_number}: invalid date {row[1]!r}: {exc}")
                continue
            row[3] = TYPE_ALIASES.get(row[3], row[3])
            if path.name in {"modular_events.tsv", "analytic_review_events.tsv"}:
                run_label = "MPL_64_116-157/modular_context"
                if run_label not in row[2]:
                    row[2] += "; run " + run_label
            refined_id = None
            refuted_match = REFINEMENT_IN_TYPE.fullmatch(row[3])
            if refuted_match and refuted_match[1] != "id":
                refined_id = refuted_match[1]
            elif row[3] == REFUTED_PREFIX + "id":
                found = REFINEMENT_IN_OUTCOME.search(row[4])
                if found:
                    refined_id = found[1].rstrip(".")
                    row[3] = REFUTED_PREFIX + refined_id
                else:
                    errors.append(f"{source['file']}:{line_number}: generic refutation type "
                                  "but no actual refinement ID found in outcome")
                    continue
            if not allowed_type(row[3]):
                errors.append(f"{source['file']}:{line_number}: unrecognized type {row[3]!r}")
                continue
            # The C/R/U sections document the manuscript or paper, not new proofs.
            # Retain their observations but do not promote them to mathematical checks.
            target = note_target(row[0], note_ids)
            documentary = bool(target and target[0] in "CRU")
            if documentary and row[3] != BACKGROUND:
                row[3] = BACKGROUND
            changes = {HEADER[i]: {"from": original[i], "to": row[i]}
                       for i in range(5) if original[i] != row[i]}
            if changes:
                normalizations.append({**provenance, "changes": changes,
                                       "documentary_reclassification": documentary and original[3].strip() != BACKGROUND})
            key = tuple(row)
            if key in seen:
                index = seen[key]
                entries[index]["sources"].append(provenance)
                duplicates.append({**provenance, "same_as": entries[index]["sources"][0]})
                continue
            seen[key] = len(entries)
            entries.append({"row": row, "sources": [provenance], "refined_id": refined_id})

    direct: dict[str, list[int]] = {key: [] for key in note_blocks}
    supporting: dict[str, list[int]] = {key: [] for key in note_blocks}
    appendix_refs = {key: set(re.findall(r"\bAC\d{2,}\b", body)) for key, body in note_blocks.items()}
    for index, entry in enumerate(entries):
        targets = set()
        for candidate in (entry["row"][0], entry["refined_id"]):
            target = note_target(candidate, note_ids) if candidate else None
            if target:
                targets.add(target)
        for target in targets:
            direct[target].append(index)
        appendix = APPENDIX_ID.match(entry["row"][0])
        if appendix:
            for key, refs in appendix_refs.items():
                if appendix[1] in refs:
                    supporting[key].append(index)
    missing_direct = [key for key in note_blocks if not direct[key]]
    missing_any = [key for key in note_blocks if not direct[key] and not supporting[key]]
    supporting_only = [key for key in note_blocks if not direct[key] and supporting[key]]
    note_coverage = []
    for key in note_blocks:
        note_coverage.append({
            "note_id": key,
            "direct_event_count": len(direct[key]),
            "supporting_appendix_event_count": len(supporting[key]),
            "direct_statement_ids": list(dict.fromkeys(entries[i]["row"][0] for i in direct[key])),
            "direct_types": sorted({entries[i]["row"][3] for i in direct[key]}),
            "supporting_statement_ids": list(dict.fromkeys(entries[i]["row"][0] for i in supporting[key])),
        })
    report = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "notes_file": str(notes_path.relative_to(workdir)),
        "notes_sha256": hashlib.sha256(notes_bytes).hexdigest() if notes_bytes else None,
        "main_note_count": len(note_blocks),
        "sources": sources,
        "source_row_count": sum(source["data_rows"] for source in sources),
        "unique_event_count": len(entries),
        "duplicate_exact_rows_removed": len(duplicates),
        "duplicates": duplicates,
        "normalizations": normalizations,
        "allowed_exact_types": sorted(ALLOWED_TYPES),
        "allowed_refutation_type_regex": REFINEMENT_IN_TYPE.pattern,
        "type_counts": dict(sorted(collections.Counter(entry["row"][3] for entry in entries).items())),
        "errors": errors,
        "warnings": warnings,
        "direct_covered_note_count": len(note_blocks) - len(missing_direct),
        "supporting_only_note_ids": supporting_only,
        "missing_direct_note_ids": missing_direct,
        "missing_any_note_ids": missing_any,
        "note_coverage": note_coverage,
        "master_written": not errors,
        "events_with_provenance": entries,
    }
    if not errors:
        buffer = io.StringIO(newline="")
        writer = csv.writer(buffer, delimiter="\t", lineterminator="\n")
        writer.writerow(HEADER)
        writer.writerows(entry["row"] for entry in entries)
        atomic_text(master_path, buffer.getvalue())
        # Validate the exact written artifact, including physical-line simplicity.
        written = list(csv.reader(io.StringIO(master_path.read_text()), delimiter="\t"))
        assert tuple(written[0]) == HEADER
        assert all(len(row) == 5 for row in written)
        assert len(written) - 1 == len(entries) == len({tuple(row) for row in written[1:]})
        assert all(allowed_type(row[3]) for row in written[1:])
        report["master_sha256"] = hashlib.sha256(master_path.read_bytes()).hexdigest()
    atomic_text(research / "check_ledger_coverage.json", json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    lines = ["# Check-ledger coverage", "", f"Generated: {report['generated_at']}", "",
             f"Sources: {len(sources)}; source rows: {report['source_row_count']}; unique events: {len(entries)}; "
             f"exact duplicate rows removed: {len(duplicates)}.", "",
             f"Main-note coverage by direct ID or explicit refinement: **{len(note_blocks)-len(missing_direct)}/{len(note_blocks)}**.", "",
             "A direct event may be carried background; coverage is not a claim of proof. "
             "Appendix checks are reported separately and do not fill the direct-ID coverage requirement.", "",
             "Missing direct IDs: " + (", ".join(missing_direct) or "none") + ".", "",
             "Supporting appendix checks only: " + (", ".join(supporting_only) or "none") + ".", "",
             "Missing both direct and explicitly cited appendix events: " + (", ".join(missing_any) or "none") + ".", "",
             "## Validation", "", "- Master written: " + str(not errors).lower() + ".",
             "- Errors: " + ("; ".join(errors) or "none") + ".",
             "- Warnings: " + ("; ".join(warnings) or "none") + ".", "",
             "## Per-note coverage", "",
             "| Note | Direct events | Direct types | Supporting appendix IDs |",
             "|---|---:|---|---|"]
    for item in note_coverage:
        lines.append(f"| {item['note_id']} | {item['direct_event_count']} | "
                     f"{'; '.join(item['direct_types']) or '—'} | {', '.join(item['supporting_statement_ids']) or '—'} |")
    lines += ["", "## Normalization and provenance", "",
              "Exact row provenance, source hashes, original and normalized fields, and any duplicates are retained in "
              "check_ledger_coverage.json. Source ledgers are not modified. Date-only events retain date-only precision. "
              "C/R/U documentary entries are carried as background; independent proof-review entries retain their actual stated types.", ""]
    atomic_text(research / "check_ledger_coverage.md", "\n".join(lines))
    summary = {key: report[key] for key in ("main_note_count", "source_row_count", "unique_event_count",
                "duplicate_exact_rows_removed", "direct_covered_note_count", "missing_direct_note_ids",
                "supporting_only_note_ids", "missing_any_note_ids", "errors", "warnings", "master_written")}
    summary["source_files"] = [source["file"] for source in sources]
    summary["normalization_count"] = len(normalizations)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 2 if errors else (1 if args.require_complete and missing_direct else 0)


if __name__ == "__main__":
    raise SystemExit(main())
