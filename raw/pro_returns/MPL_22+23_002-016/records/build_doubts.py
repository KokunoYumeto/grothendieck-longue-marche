#!/usr/bin/env python3
"""Build the doubts deliverable from the principal transcriber's records only.

No page transcription, image, or context file is opened. Reading and reason
strings are carried through verbatim, apart from Markdown cell escaping.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from collections import Counter
from pathlib import Path


STEM = "MPL_22+23_002-016"
EXPECTED = [(22, n) for n in range(2, 31)] + [(23, n) for n in range(2, 17)]

def explicit_alternatives(reading: str, reason: str) -> str:
    """Repeat explicit alternative separators from the current source record.

    No page/row-index mapping is retained: audit changes to a reading must also
    change this derived column. Pipes nested in formula braces/parentheses are
    left alone (for example the recorded literal {K_b|K_a} separators).
    The complete reading/reason fields are preserved in adjacent columns.
    """
    depth = 0
    start = 0
    segments = []
    for index, char in enumerate(reading):
        if char in "({[":
            depth += 1
        elif char in ")}]":
            depth = max(0, depth - 1)
        elif char == ";" and depth == 0:
            segments.append(reading[start:index])
            start = index + 1
    segments.append(reading[start:])
    alternatives = []
    for segment in segments:
        depth = 0
        pipes = []
        for index, char in enumerate(segment):
            if char in "({[":
                depth += 1
            elif char in ")}]":
                depth = max(0, depth - 1)
            elif char == "|" and depth == 0:
                pipes.append(index)
        for index, position in enumerate(pipes):
            end = pipes[index + 1] if index + 1 < len(pipes) else len(segment)
            candidate = segment[position + 1:end].strip()
            if candidate:
                alternatives.append(candidate)
    # This explicitly labelled form is also unambiguous in a source reason.
    for match in re.finditer(r"\bAlternative:\s*([^;\n]+)", reason, re.I):
        candidate = match.group(1).strip()
        if candidate:
            alternatives.append(candidate)
    return "; ".join(dict.fromkeys(alternatives)) if alternatives else "—"


def cell(value: object) -> str:
    """HTML code formatting preserves source punctuation inside Markdown tables."""
    text = str(value)
    return "<code>" + html.escape(text, quote=False).replace("|", "&#124;").replace("\n", "<br>") + "</code>"


def sections(markdown: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"(?m)^#{1,6}\s+(.+)\s*$", markdown))
    result = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        result.append((match.group(1), markdown[match.start():end].rstrip()))
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    root = args.root.resolve()
    records = root / "records"
    notation_path = records / "notation.md"
    notation = notation_path.read_text(encoding="utf-8")
    parts = sections(notation)
    table_sections = [body for title, body in parts if "notation" in title.lower()]
    if not table_sections:
        raise SystemExit("notation.md contains no notation heading; no deliverable was written")
    out = ["\n\n".join(table_sections), "", "# Doubts and reading records", "",
           "This table carries forward every doubt entry in the principal transcriber's page records, "
           "in cote and scan order. Approximate locations are the source record's own locators; "
           "no line number has been invented. Readings and reasons are preserved as supplied. "
           "Some high-confidence entries document unusual visible wording or notation that was deliberately retained.", "",
           "The alternatives column repeats alternatives explicitly recorded in the source fields. "
           "An em dash means that no separate alternative has been entered in that column; "
           "the complete reading and reason remain available beside it.", "",
           "| Cote / file | Scan | Approximate line / location | Reading as recorded | Alternatives | Confidence | Reason / observation as recorded |",
           "|---|---:|---|---|---|---|---|"]
    page_count = 0
    doubt_count = 0
    confidence_counts = Counter()
    low_counts = Counter()
    missing = []
    pages_without_doubts = []
    for cote, scan in EXPECTED:
        path = records / f"{STEM}_{cote}_scan{scan:03d}.json"
        if not path.exists():
            missing.append((cote, scan))
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        page_count += 1
        doubts = data.get("doubts", [])
        if not doubts:
            pages_without_doubts.append((cote, scan))
        for index, doubt in enumerate(doubts, 1):
            if isinstance(doubt, dict):
                location = doubt.get("location", doubt.get("line", ""))
                reading = doubt.get("reading", "")
                reason = doubt.get("reason", "")
                confidence = doubt.get("confidence", "")
                alternative = doubt.get("alternatives", explicit_alternatives(reading, reason))
            else:
                if len(doubt) != 4:
                    raise ValueError(f"{path.name}, doubt {index}: expected four source fields")
                location, reading, reason, confidence = doubt
                alternative = explicit_alternatives(reading, reason)
            if confidence not in {"high", "medium", "low"}:
                raise ValueError(f"{path.name}, doubt {index}: unrecognized confidence {confidence!r}")
            values = [str(cote), f"{scan:03d}", cell(location), cell(reading), cell(alternative), confidence, cell(reason)]
            out.append("| " + " | ".join(values) + " |")
            doubt_count += 1
            confidence_counts[confidence] += 1
            if confidence == "low":
                low_counts[(cote, scan)] += 1
    out += ["", "## Record coverage", "",
            f"This build includes {page_count} of the expected 44 page records and {doubt_count} doubt entries "
            f"({confidence_counts['high']} high, {confidence_counts['medium']} medium, {confidence_counts['low']} low confidence)."]
    if missing:
        out += ["", "Page records not yet present: " + "; ".join(f"{cote} scan {scan:03d}" for cote, scan in missing) + "."]
    if pages_without_doubts:
        out += ["", "Records with an empty doubts list: " + "; ".join(f"{cote} scan {scan:03d}" for cote, scan in pages_without_doubts) + ". An empty list reports the existing record; it does not certify error-free reading."]
    out += ["", "# Abbreviations", ""]
    abbreviation_sections = [body for title, body in parts if re.search(r"abbrevi|abrév", title, re.I)]
    if abbreviation_sections:
        for section in abbreviation_sections:
            # The heading above provides the section title; preserve its body.
            out.append(section.split("\n", 1)[1].lstrip("\n") if "\n" in section else "")
    else:
        out.append("No abbreviation expansions have yet been supplied in the notation record. "
                   "This draft adds none. The principal transcriber can add the verified abbreviation "
                   "list to an Abbreviations section in `records/notation.md` and rerun this builder.")
    out += ["", "# Legibility and remaining uncertainty", "",
            "This legibility note is derived from the principal transcriber's page records. "
            "Those records repeatedly identify faint marginal handwriting, overlapping cancellations, "
            "typewriter overstrikes, tiny interlinear additions, and writing at the physical page edges "
            "as the least secure passages. Some readable typescript is also recorded because its visible "
            "wording or notation is unusual; the high-confidence entries preserve those observations.", ""]
    if low_counts:
        selected = sorted(low_counts.items(), key=lambda item: (-item[1], item[0]))[:8]
        out.append("The largest recorded concentrations of low-confidence entries in this build are " +
                   "; ".join(f"{cote} scan {scan:03d} ({count})" for (cote, scan), count in selected) +
                   ". These counts identify review priorities within the recorded doubts; they do not measure every possible reading error.")
    out += ["", "This builder aggregates the principal transcriber's records and performs no independent image reading. "
            "The page-by-page visual audits and transcription freeze are documented in `progress.log`; "
            "the notation table records the cross-page comparison. "
            "Regeneration updates this metadata report without changing any page transcription.", ""]
    # Preserve any non-notation, non-abbreviation source notes after the required
    # doubts sections, so the provenance statement is not silently discarded.
    other = [body for title, body in parts if "notation" not in title.lower() and not re.search(r"abbrevi|abrév", title, re.I)]
    if other:
        out += ["# Source notation-record notes", "", "\n\n".join(other), ""]
    target = root / f"{STEM}_doubts.md"
    target.write_text("\n".join(out), encoding="utf-8")
    print(json.dumps({"output": str(target), "page_records": page_count,
                      "doubt_entries": doubt_count, "confidence_counts": dict(confidence_counts),
                      "missing_page_records": missing}, ensure_ascii=False))


if __name__ == "__main__":
    main()
