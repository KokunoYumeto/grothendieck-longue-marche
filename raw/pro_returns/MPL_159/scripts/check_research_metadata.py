#!/usr/bin/env python3
"""Check research-note metadata and event-reference integrity, not mathematics.

Supported note format:
    ### N001 — Title
    **Kind:** ... · **Source:** ... · **Quote:** ...

Every note must reference a context-search ID such as [Q001] and have an event
row with statement_id N001. Context-search IDs are read from registry cells,
without evaluating search results or consulting supplied context source files.
Sentence counting is intentionally omitted because formulas and abbreviations
make it unreliable. No notes or event records are changed.
"""

from __future__ import annotations

import argparse
import csv
from datetime import date, datetime
import io
import json
from pathlib import Path
import re


EVENT_COLUMNS = ["statement_id", "date", "who", "type", "outcome"]
EVENT_TYPES = {
    "targeted proof check", "independent re-proof",
    "computation or formal certificate", "used and rechecked in this run",
    "carried as background without fault found",
}
NOTE_KINDS = {
    "conjecture", "unproved claim", "unpursued implication", "own idea",
    "reading question", "self-flagged", "withdrawn in the same text",
    "standing question", "title", "page count",
}


def validate_research(root: Path, partial: bool = False) -> dict:
    errors = []
    warnings = []
    details = {}
    events_path = root / "CHECK_EVENTS.tsv"
    event_ids = set()
    event_rows = []
    if not events_path.is_file():
        if not partial:
            errors.append("Missing CHECK_EVENTS.tsv")
    else:
        reader = csv.DictReader(io.StringIO(events_path.read_text(encoding="utf-8-sig")), delimiter="\t")
        if reader.fieldnames != EVENT_COLUMNS:
            errors.append(f"CHECK_EVENTS.tsv columns must be exactly {EVENT_COLUMNS}")
        seen_rows = set()
        for line, row in enumerate(reader, 2):
            event_rows.append(row)
            if None in row or any(row.get(column) is None for column in EVENT_COLUMNS):
                errors.append(f"CHECK_EVENTS.tsv line {line}: malformed column count")
                continue
            for column in EVENT_COLUMNS:
                if not row[column].strip():
                    errors.append(f"CHECK_EVENTS.tsv line {line}: empty {column}")
            event_ids.add(row["statement_id"].strip())
            event_type = row["type"].strip()
            if event_type not in EVENT_TYPES and not event_type.startswith("refuted"):
                errors.append(f"CHECK_EVENTS.tsv line {line}: unrecognized event type {event_type!r}")
            if event_type.startswith("refuted") and not re.search(
                r"(?:refin|replac|correct|N\d{3}|[A-Z][A-Z0-9_-]*\.[A-Z0-9])",
                event_type + " " + row["outcome"], flags=re.I
            ):
                warnings.append(f"CHECK_EVENTS.tsv line {line}: refutation should identify the refined statement")
            try:
                if len(row["date"].strip()) == 10:
                    date.fromisoformat(row["date"].strip())
                else:
                    datetime.fromisoformat(row["date"].strip().replace(" UTC", "+00:00").replace("Z", "+00:00"))
            except ValueError:
                errors.append(f"CHECK_EVENTS.tsv line {line}: date is not a valid ISO date/UTC timestamp")
            key = tuple(row[column] for column in EVENT_COLUMNS)
            if key in seen_rows:
                warnings.append(f"CHECK_EVENTS.tsv line {line}: identical event row occurs more than once")
            seen_rows.add(key)
    details["event_rows"] = len(event_rows)
    details["statement_ids_with_events"] = len(event_ids)

    notes_path = root / "MPL_159_notes.md"
    if not notes_path.is_file():
        details["notes_present"] = False
        if not partial:
            errors.append("Missing MPL_159_notes.md")
        return {"ok": not errors, "details": details, "errors": errors, "warnings": warnings}
    text = notes_path.read_text(encoding="utf-8")
    details["notes_present"] = True
    matches = list(re.finditer(r"(?m)^###\s+(N\d{3,})\s+[—–-]\s+(.+)$", text))
    if not matches:
        errors.append("No research-note headings of the form '### N001 — Title'")
    note_ids = []
    referenced_queries = set()
    for index, match in enumerate(matches):
        note_id, title = match.groups()
        if note_id in note_ids:
            errors.append(f"Duplicate research-note ID: {note_id}")
        note_ids.append(note_id)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.end():end]
        metadata = re.search(r"(?ms)^\*\*Kind:\*\*.*?(?=\n\s*\n|\Z)", body)
        fields = None
        if metadata:
            fields = re.fullmatch(
                r"\*\*Kind:\*\*\s*(.*?)\s*·\s*\*\*Source:\*\*\s*(.*?)\s*·\s*\*\*Quote:\*\*\s*(.*?)\s*",
                metadata.group(0), flags=re.S,
            )
        if fields is None:
            errors.append(f"{note_id}: missing or malformed Kind/Source/Quote metadata paragraph")
        else:
            kind, source, quote = fields.groups()
            for field, value in zip(("Kind", "Source", "Quote"), fields.groups()):
                if not value.strip():
                    errors.append(f"{note_id}: empty {field} metadata")
            if not any(candidate in kind.lower() for candidate in NOTE_KINDS):
                warnings.append(f"{note_id}: note kind is outside the expected vocabulary")
            if "159" not in source or not re.search(r"scan|whole|package|all", source, re.I):
                warnings.append(f"{note_id}: Source should make cote 159 and scan/package scope explicit")
            if "own idea" in kind.lower():
                after_metadata = body[metadata.end():]
                if not re.search(r"confidence", after_metadata, re.I):
                    errors.append(f"{note_id}: own idea has no explicit confidence statement")
                if not re.search(r"reason|because|since|based on", after_metadata, re.I):
                    errors.append(f"{note_id}: own idea has no explicit reason for its confidence")
            if not body[metadata.end():].strip():
                errors.append(f"{note_id}: no note body after metadata")
        queries = set(re.findall(r"\[(Q\d{3,})\]", body))
        if not queries:
            errors.append(f"{note_id}: no context-search pointer such as [Q001]")
        referenced_queries.update(queries)
        if note_id not in event_ids:
            errors.append(f"{note_id}: no CHECK_EVENTS.tsv row for this note ID")
    unknown_note_events = sorted(event_ids.intersection({value for value in event_ids if re.fullmatch(r"N\d{3,}", value)}) - set(note_ids))
    if unknown_note_events:
        errors.append("Event rows refer to undefined note IDs: " + ", ".join(unknown_note_events))
    details["note_count"] = len(note_ids)
    details["context_query_ids_referenced"] = len(referenced_queries)

    registry = root / "context_searches.tsv"
    if referenced_queries:
        if not registry.is_file():
            errors.append("Notes reference context queries but context_searches.tsv is missing")
        else:
            rows = csv.reader(io.StringIO(registry.read_text(encoding="utf-8-sig")), delimiter="\t")
            registered = set()
            widths = set()
            for row in rows:
                if not row:
                    continue
                widths.add(len(row))
                for cell in row:
                    value = cell.strip()
                    if re.fullmatch(r"Q\d{3,}", value):
                        registered.add(value)
            if len(widths) > 1:
                errors.append("context_searches.tsv has inconsistent column counts")
            absent = sorted(referenced_queries - registered)
            if absent:
                errors.append("Undefined context-search IDs: " + ", ".join(absent))
            details["context_query_ids_registered"] = len(registered)
    return {"ok": not errors, "details": details, "errors": errors, "warnings": warnings}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--partial", action="store_true")
    args = parser.parse_args()
    result = validate_research(args.root.resolve(), args.partial)
    result["scope"] = "Metadata and cross-reference integrity only; no evaluation of claims or source readings."
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
