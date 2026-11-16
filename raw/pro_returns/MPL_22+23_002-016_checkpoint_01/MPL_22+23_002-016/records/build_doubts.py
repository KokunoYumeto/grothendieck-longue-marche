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

# Alternatives already explicitly supplied in the source reading/reason fields.
# These are copied into a separate column for usability; they do not replace or
# change the complete source reading or reason in the adjacent columns.
# The index is the one-based doubt-row position within that page's record.
RECORDED_ALTERNATIVES = {
    (22, 7, 1): "fraktur g",
    (22, 10, 8): "A'",
    (22, 11, 1): "la condition",
    (22, 13, 1): "b)",
    (22, 13, 5): "algèbre de Cohen",
    (22, 15, 2): "et est complet",
    (22, 17, 4): "A—B",
    (22, 18, 2): "4.12.",
    (22, 20, 2): "Cas :",
    (22, 20, 5): "valuation non / possibilité",
    (22, 21, 1): "lieu; faut",
    (22, 21, 3): "2.40.1",
    (22, 21, 5): "quelconque",
    (22, 21, 6): "arrow",
    (22, 21, 7): "p; ceux-ci; en lequel",
    (22, 22, 1): "k",
    (22, 22, 3): "p=0",
    (22, 22, 7): "xn",
    (22, 23, 2): "dim A>0",
    (22, 23, 3): "formᵗ",
    (22, 23, 5): "dash rather than 1",
    (22, 23, 6): "u",
    (22, 24, 3): "seraient",
    (22, 24, 4): "extension",
    (22, 25, 4): "φ",
    (22, 25, 6): "abbreviated tt",
    (22, 27, 1): "K",
    (22, 27, 4): "l'existence",
    (22, 29, 4): "notin",
    (22, 29, 6): "F_0",
    (23, 5, 2): "O_S",
    (23, 6, 1): "underline E",
    (23, 6, 6): "M",
    (23, 6, 8): "-k",
    (23, 7, 1): "xi",
    (23, 7, 2): "incidental",
    (23, 9, 1): "Suites",
    (23, 9, 2): "zeta",
    (23, 9, 6): "Tout",
    (23, 10, 1): "G(U)",
    (23, 10, 5): "R(U)",
}


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
                alternative = doubt.get("alternatives", RECORDED_ALTERNATIVES.get((cote, scan, index), "—"))
            else:
                if len(doubt) != 4:
                    raise ValueError(f"{path.name}, doubt {index}: expected four source fields")
                location, reading, reason, confidence = doubt
                alternative = RECORDED_ALTERNATIVES.get((cote, scan, index), "—")
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
    out += ["", "# Legibility and remaining uncertainty — draft", "",
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
    out += ["", "The final visual audit and cross-page notation comparison remain the principal transcriber's responsibility. "
            "This generated report does not establish that either step has occurred. "
            "Regeneration updates the report from the records without changing any page transcription.", ""]
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
