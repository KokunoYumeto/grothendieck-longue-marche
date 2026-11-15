#!/usr/bin/env python3
"""Record literal context searches and mechanically check numbered note metadata.

Run again after editing the notes. Only the notes and the two exact supplied
context files are read; no transcription, image, archive, or external source
is inspected. Exit status is 1 for metadata coverage issues, 0 otherwise.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import tempfile
import unicodedata


ALLOWED_KINDS = (
    "self-flagged",
    "unproved claim",
    "conjecture",
    "unpursued implication",
    "withdrawn in the same text",
    "reading question",
    "own idea",
)
HEADING = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
NOTE_ID = re.compile(r"^([EOAPC]\d+)\b")
FIELD = re.compile(
    r"(?<!\w)(?:\*\*)?"
    r"(?P<label>File/location|Location|Kind|Confidence|Context queries|Context comparison)"
    r"(?:\*\*)?[ \t]*:[ \t]*(?:\*\*)?[ \t]*",
    re.IGNORECASE,
)
CHECK_NAMES = {
    "unique_id": "Unique ID",
    "location": "Nonempty File/location",
    "kind": "Allowed Kind",
    "own_idea_confidence": "Own-idea Confidence (low/medium/high)",
    "context_queries": "Nonempty Context queries",
    "context_comparison": "Nonempty Context comparison text",
}


def normalize(text: str) -> str:
    """Casefold and remove Unicode combining marks, retaining punctuation."""
    return "".join(
        char for char in unicodedata.normalize("NFD", text.casefold())
        if unicodedata.category(char) != "Mn"
    )


def snapshot(path: Path, label: str) -> tuple[dict, list[str]]:
    data = path.read_bytes()
    lines = data.decode("utf-8-sig").splitlines()
    return {
        "file": label,
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "lines": len(lines),
    }, lines


def parse_fields(lines: list[str], first_line: int) -> dict:
    fields: dict[str, list[dict]] = {}
    for offset, line in enumerate(lines):
        matches = list(FIELD.finditer(line))
        for index, match in enumerate(matches):
            label = match["label"].casefold()
            if label == "location":
                label = "file/location"
            end = matches[index + 1].start() if index + 1 < len(matches) else len(line)
            value = line[match.end():end].strip()
            # Comparisons may be wrapped across physical lines in one paragraph.
            if label == "context comparison" and index + 1 == len(matches):
                following = offset + 1
                while following < len(lines):
                    continuation = lines[following]
                    if not continuation.strip() or FIELD.search(continuation) or HEADING.match(continuation):
                        break
                    value += "\n" + continuation
                    following += 1
            fields.setdefault(label, []).append({
                "line": first_line + offset,
                "text": value.strip(),
            })
    return fields


def one_field(fields: dict, name: str) -> str:
    values = fields.get(name, [])
    return values[0]["text"] if len(values) == 1 else ""


def parse_queries(text: str) -> list[str]:
    # The final full stop is sentence punctuation in this notes template.
    value = text.strip()
    if value.endswith("."):
        value = value[:-1]
    return [part.strip() for part in value.split(";") if part.strip()]


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=path.parent, prefix=path.name + ".", delete=False
    ) as handle:
        temporary = Path(handle.name)
        handle.write(text)
    temporary.replace(path)


def main() -> int:
    work = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--notes", type=Path, default=work / "MPL_93_002-046_notes.md")
    args = parser.parse_args()
    context = work.parent / "context_sources"
    output = work / "research" / "context_search_by_note.json"
    report = work / "research" / "context_search_coverage.md"

    notes_meta, lines = snapshot(args.notes, str(args.notes.resolve()))
    sources = []
    source_lines = []
    for relative in ("README.md", "notes/RESULTS_STATE.md"):
        label = "context_sources/" + relative
        metadata, text_lines = snapshot(context / relative, label)
        sources.append(metadata)
        source_lines.extend(
            (label, number, text, normalize(text))
            for number, text in enumerate(text_lines, 1)
        )

    headings = [
        (index, len(match[1]), match[2])
        for index, line in enumerate(lines)
        if (match := HEADING.match(line))
    ]
    notes = []
    for heading_index, (start, level, title) in enumerate(headings):
        identifier = NOTE_ID.match(title)
        if not identifier:
            continue
        stop = next(
            (position for position, depth, _ in headings[heading_index + 1:] if depth <= level),
            len(lines),
        )
        fields = parse_fields(lines[start + 1:stop], start + 2)
        queries = []
        for field in fields.get("context queries", []):
            for query in parse_queries(field["text"]):
                normalized = normalize(query)
                queries.append({
                    "query": query,
                    "query_line": field["line"],
                    "normalized_query": normalized,
                    "matches": [
                        {"file": filename, "line": number, "text": text}
                        for filename, number, text, searchable in source_lines
                        if normalized and normalized in searchable
                    ],
                })
        notes.append({
            "id": identifier[1],
            "heading": title,
            "heading_line": start + 1,
            "fields": fields,
            "queries": queries,
        })

    counts = Counter(note["id"] for note in notes)
    for note in notes:
        fields = note["fields"]
        kind = one_field(fields, "kind").strip().removesuffix(".").casefold()
        confidence = one_field(fields, "confidence")
        checks = {
            "unique_id": counts[note["id"]] == 1,
            "location": bool(one_field(fields, "file/location")),
            "kind": kind in ALLOWED_KINDS,
            "own_idea_confidence": (
                bool(re.match(r"^(low|medium|high)(?=$|[;,.: \t])", confidence, re.I))
                if kind == "own idea" else None
            ),
            "context_queries": len(fields.get("context queries", [])) == 1 and bool(note["queries"]),
            "context_comparison": bool(one_field(fields, "context comparison")),
        }
        note["checks"] = checks
        note["issues"] = [CHECK_NAMES[key] for key, value in checks.items() if value is False]

    query_count = sum(len(note["queries"]) for note in notes)
    matched_queries = sum(bool(query["matches"]) for note in notes for query in note["queries"])
    coverage = {
        "status": "PASS" if notes and not any(note["issues"] for note in notes) else "ISSUES",
        "note_count": len(notes),
        "unique_id_count": len(counts),
        "ids_by_group": dict(sorted(Counter(note["id"][0] for note in notes).items())),
        "duplicate_ids": {key: value for key, value in counts.items() if value > 1},
        "query_count": query_count,
        "queries_with_matches": matched_queries,
        "queries_with_empty_matches": query_count - matched_queries,
        "checks": {
            key: {
                "applicable": sum(note["checks"][key] is not None for note in notes),
                "passed": sum(note["checks"][key] is True for note in notes),
                "failed_note_occurrences": [
                    {"id": note["id"], "heading_line": note["heading_line"]}
                    for note in notes if note["checks"][key] is False
                ],
            }
            for key in CHECK_NAMES
        },
    }
    generated = datetime.now(timezone.utc).isoformat(timespec="seconds")
    result = {
        "schema_version": 1,
        "generated_at_utc": generated,
        "method": {
            "corpus": "Only context_sources/README.md and context_sources/notes/RESULTS_STATE.md; no recursive search.",
            "matching": "Literal substring within each physical source line after Unicode casefold, NFD normalization, and removal of combining marks (case- and accent-insensitive). Punctuation and whitespace are retained; no stemming, regular-expression, semantic, or cross-line matching.",
            "queries": "Semicolon-separated Context queries values; surrounding whitespace and one final sentence full stop are removed. Query order and duplicates are retained. Empty matches are explicit [] lists.",
            "coverage": "Mechanical presence/uniqueness and enum checks only; location accuracy, mathematical content, attribution, and the adequacy of context comparisons are not assessed.",
            "allowed_kinds": list(ALLOWED_KINDS),
            "own_idea_confidence": "One nonempty Confidence field starting low, medium, or high; its full qualification is retained.",
        },
        "inputs": {"notes": notes_meta, "context_files": sources},
        "coverage": coverage,
        "notes": notes,
    }
    atomic_write(output, json.dumps(result, ensure_ascii=False, indent=2) + "\n")

    rows = [
        "# Context-search and note-metadata coverage", "",
        f"Generated: {generated}. Status: **{coverage['status']}**.", "",
        f"Notes snapshot: `{args.notes.name}`; SHA-256 `{notes_meta['sha256']}`.", "",
        f"{len(notes)} note occurrences; {len(counts)} unique IDs. Groups: "
        + ", ".join(f"{key}: {value}" for key, value in coverage["ids_by_group"].items()) + ".", "",
        f"{query_count} query occurrences: {matched_queries} have literal matches; "
        f"{query_count - matched_queries} have explicit empty match lists.", "",
        "| Check | Applicable | Passed | Failed IDs (heading line) |",
        "|---|---:|---:|---|",
    ]
    for key, label in CHECK_NAMES.items():
        check = coverage["checks"][key]
        failures = ", ".join(
            f"{item['id']} (L{item['heading_line']})" for item in check["failed_note_occurrences"]
        ) or "None"
        rows.append(f"| {label} | {check['applicable']} | {check['passed']} | {failures} |")
    if not notes:
        rows.extend(["", "**Issue: no E/O/A/P/C numbered note headings were found.**"])
    rows.extend([
        "", "Allowed Kinds: " + "; ".join(ALLOWED_KINDS) + ".", "",
        "## Search method and scope", "", result["method"]["matching"], "",
        result["method"]["queries"], "", result["method"]["coverage"], "",
        "Exactly two supplied context files were searched:", "",
    ])
    rows.extend(f"- `{source['file']}` — SHA-256 `{source['sha256']}`." for source in sources)
    rows.extend([
        "", "Per-note fields, query terms, and matching file/line/text records are in "
        "`context_search_by_note.json`. This is a snapshot; rerun after any notes change.", "",
        "Invocation from the work directory:", "", "```sh",
        "python tools/build_research_records.py", "```", "",
    ])
    atomic_write(report, "\n".join(rows))
    print(f"{coverage['status']}: {len(notes)} notes, {query_count} queries, "
          f"{matched_queries} matched queries, {query_count - matched_queries} empty queries")
    print(output)
    print(report)
    for note in notes:
        if note["issues"]:
            print(f"{note['id']} (L{note['heading_line']}): " + "; ".join(note["issues"]))
    return 0 if coverage["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
