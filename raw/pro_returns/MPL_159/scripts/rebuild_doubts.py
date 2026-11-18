#!/usr/bin/env python3
"""Rebuild the doubts occurrence table, without changing any page fragment.

By default this reports whether a rebuild would change the file. --write makes
the update. The existing notation/preamble and all later level-two sections
(for example abbreviations and legibility) are preserved byte for byte.

--notation-source can supply an explicitly maintained replacement for the
notation section; the script never invents or normalizes notation readings.
The source may contain the heading '## Notation table', or just its body.

Confidence is retained by exact prior occurrence, then by an unambiguous
same-reading match on that scan. Newly introduced/unmatched entries default to
low; this is a conservative table-management default, not a visual assessment.
An explicit --default-confidence can change that default. No research context
or source images are read by this script.
"""

from __future__ import annotations

import argparse
from collections import defaultdict, deque
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re

from check_tex_structure import argument, strip_comments


HEADING = "## Doubts by page"
NOTATION_HEADING = "## Notation table"
MISSING_ALT = "Unresolved; no secure alternative"


@dataclass
class Occurrence:
    scan: int
    line: int
    offset: int
    macro: str
    reading: str
    alternative: str


def split_alternative(body: str) -> tuple[str, str]:
    """Interpret the first unescaped top-level | as the task's separator."""
    depth = 0
    i = 0
    while i < len(body):
        if body[i] == "\\":
            match = re.match(r"\\(?:[A-Za-z@]+|.)", body[i:])
            i += len(match.group(0)) if match else 1
            continue
        if body[i] == "{":
            depth += 1
        elif body[i] == "}":
            depth -= 1
        elif body[i] == "|" and depth == 0:
            return body[:i], body[i + 1:]
        i += 1
    return body, MISSING_ALT


def occurrences(path: Path) -> tuple[list[Occurrence], str]:
    raw = path.read_bytes()
    text = strip_comments(raw.decode("utf-8"))
    scan = int(re.search(r"scan(\d+)\.tex$", path.name).group(1))
    result = []
    i = 0
    while i < len(text):
        if text[i] != "\\":
            i += 1
            continue
        match = re.match(r"\\([A-Za-z@]+|.)", text[i:])
        if not match:
            i += 1
            continue
        end = i + len(match.group(0))
        macro = match.group(1)
        if macro in {"unsure", "illegible"}:
            body, _ = argument(text, end)
            if body is None:
                raise ValueError(f"{path.name}: unclosed or missing {macro} argument")
            if macro == "illegible":
                reading = f"Unreadable: {body} word(s)"
                alternative = "No recoverable reading"
            else:
                reading, alternative = split_alternative(body)
            result.append(Occurrence(scan, text.count("\n", 0, i) + 1, i,
                                     macro, reading, alternative))
        # Do not skip the argument: nested doubts are separate occurrences.
        i = end
    return result, hashlib.sha256(raw).hexdigest()


def split_markdown_row(line: str) -> list[str]:
    parts = []
    start = 0
    for i, char in enumerate(line):
        if char != "|":
            continue
        count = 0
        j = i - 1
        while j >= 0 and line[j] == "\\":
            count += 1
            j -= 1
        if count % 2:
            continue
        parts.append(line[start:i].strip())
        start = i + 1
    parts.append(line[start:].strip())
    if parts and not parts[0]:
        parts.pop(0)
    if parts and not parts[-1]:
        parts.pop()
    return [part.replace("\\|", "|") for part in parts]


def uncode(value: str) -> str:
    match = re.fullmatch(r"(`+)(.*)\1", value, flags=re.S)
    return match.group(2).strip() if match else value


def canonical(value: str) -> str:
    return " ".join(value.split())


def prior_confidences(text: str) -> tuple[dict, dict]:
    exact = defaultdict(deque)
    broad = defaultdict(set)
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        fields = split_markdown_row(line)
        if len(fields) != 6 or fields[0] != "159" or fields[-1] not in {"high", "medium", "low"}:
            continue
        match = re.search(r"TeX line (\d+)", fields[2])
        if not fields[1].isdigit() or not match:
            continue
        scan = int(fields[1])
        reading = canonical(uncode(fields[3]))
        alternative = canonical(uncode(fields[4]))
        key = (scan, int(match.group(1)), reading, alternative)
        exact[key].append(fields[-1])
        broad[(scan, reading, alternative)].add(fields[-1])
    return exact, broad


def code_cell(value: str) -> str:
    value = canonical(value).replace("|", "\\|")
    runs = [len(match.group(0)) for match in re.finditer(r"`+", value)]
    fence = "`" * (max(runs, default=0) + 1)
    pad = " " if value.startswith("`") or value.endswith("`") else ""
    return fence + pad + value + pad + fence


def section_bounds(text: str, heading: str) -> tuple[int, int] | None:
    match = re.search(r"(?m)^" + re.escape(heading) + r"[ \t]*$", text)
    if not match:
        return None
    after = re.search(r"(?m)^## ", text[match.end():])
    end = match.end() + after.start() if after else len(text)
    return match.start(), end


def build(root: Path, default_confidence: str, notation_source: Path | None) -> tuple[str, dict, dict]:
    target = root / "MPL_159_doubts.md"
    original = target.read_text(encoding="utf-8")
    old_text = original
    if notation_source:
        replacement = notation_source.read_text(encoding="utf-8").strip()
        if not replacement.startswith(NOTATION_HEADING):
            replacement = NOTATION_HEADING + "\n\n" + replacement
        bounds = section_bounds(old_text, NOTATION_HEADING)
        if bounds is None:
            raise ValueError("Cannot replace missing notation section")
        old_text = old_text[:bounds[0]] + replacement + "\n\n" + old_text[bounds[1]:]
    bounds = section_bounds(old_text, HEADING)
    if bounds is None:
        raise ValueError(f"Cannot find {HEADING!r} in doubts file")
    exact, broad = prior_confidences(original)
    pages = sorted((root / "pages").glob("MPL_159_159_scan*.tex"))
    rows = []
    page_hashes = {}
    counts = {"unsure": 0, "illegible": 0, "preserved_confidences": 0, "defaulted_confidences": 0}
    for page in pages:
        found, digest = occurrences(page)
        page_hashes[page] = digest
        for occ in found:
            reading, alternative = canonical(occ.reading), canonical(occ.alternative)
            key = (occ.scan, occ.line, reading, alternative)
            broad_key = (occ.scan, reading, alternative)
            if exact.get(key):
                confidence = exact[key].popleft()
                counts["preserved_confidences"] += 1
            elif len(broad.get(broad_key, set())) == 1:
                confidence = next(iter(broad[broad_key]))
                counts["preserved_confidences"] += 1
            else:
                confidence = "low" if occ.macro == "illegible" else default_confidence
                counts["defaulted_confidences"] += 1
            counts[occ.macro] += 1
            rows.append(f"| 159 | {occ.scan} | TeX line {occ.line} | {code_cell(reading)} | {code_cell(alternative)} | {confidence} |")
    table = (
        HEADING + "\n\n"
        "Each row is one occurrence of a doubt macro, in page and source order. "
        "Line numbers refer to the page TeX file. Confidence labels retain the "
        "reader's existing assessments where identifiable; newly unmatched "
        f"entries default to {default_confidence}, without a new visual assessment.\n\n"
        "| Cote | Scan | Approximate line / place | Reading | Alternative | Confidence |\n"
        "|---|---:|---|---|---|---|\n" + "\n".join(rows) + "\n\n"
    )
    result = old_text[:bounds[0]] + table + old_text[bounds[1]:]
    metadata = {"page_count": len(pages), "occurrences": len(rows), **counts,
                "would_change": result != original,
                "notation_replaced": notation_source is not None}
    return result, metadata, {"original": original, "page_hashes": page_hashes}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true", help="Replace only the doubts table (and explicitly supplied notation)")
    parser.add_argument("--notation-source", type=Path)
    parser.add_argument("--default-confidence", choices=("low", "medium", "high"), default="low")
    args = parser.parse_args()
    root = args.root.resolve()
    result, metadata, state = build(root, args.default_confidence, args.notation_source)
    if args.write:
        target = root / "MPL_159_doubts.md"
        if target.read_text(encoding="utf-8") != state["original"]:
            raise RuntimeError("Doubts file changed during generation; no write performed")
        for path, digest in state["page_hashes"].items():
            if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                raise RuntimeError(f"Page changed during generation: {path.name}; no write performed")
        if metadata["would_change"]:
            temp = target.with_suffix(".md.tmp")
            temp.write_text(result, encoding="utf-8")
            temp.replace(target)
        metadata["written"] = metadata["would_change"]
    print(json.dumps(metadata, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
