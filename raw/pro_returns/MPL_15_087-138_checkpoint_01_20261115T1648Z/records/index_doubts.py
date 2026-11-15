#!/usr/bin/env python3
"""Index every unsure/illegible macro without interpreting its reading.

Run from anywhere; default package root is this script's parent directory's
parent. Output defaults to records/doubt_occurrences.json in that package.
The optional --max-scan provides an explicit in-progress snapshot boundary.
Only the index is written. Source files and the doubt register are untouched.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


PREFIX = "MPL_15_087-138"
CONTROL_RE = re.compile(r"\\([A-Za-z]+|.)", re.S)


def mask_comments(text: str) -> str:
    """Replace unescaped TeX comments with spaces, retaining exact offsets."""
    result = list(text)
    i = 0
    while i < len(text):
        if text[i] == "\\":
            i += 2
        elif text[i] == "%":
            while i < len(text) and text[i] != "\n":
                result[i] = " "
                i += 1
        else:
            i += 1
    return "".join(result)


def balanced_argument(masked: str, start: int) -> tuple[int, int]:
    """Return inclusive opening/closing brace offsets for the next argument."""
    while start < len(masked) and masked[start].isspace():
        start += 1
    if start >= len(masked) or masked[start] != "{":
        raise ValueError("Macro has no following braced argument")
    depth = 1
    i = start + 1
    while i < len(masked):
        char = masked[i]
        if char == "\\":
            i += 2
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return start, i
        i += 1
    raise ValueError("Macro argument has an unclosed opening brace")


def index_page(path: Path, root: Path, scan: int) -> tuple[dict, list[dict]]:
    raw = path.read_bytes()
    # Decode without newline conversion so argument strings preserve source bytes.
    text = raw.decode("utf-8")
    masked = mask_comments(text)
    records = []
    for token in CONTROL_RE.finditer(masked):
        name = token[1]
        if name not in ("unsure", "illegible"):
            continue
        lineno = text.count("\n", 0, token.start()) + 1
        column = token.start() - text.rfind("\n", 0, token.start())
        try:
            opening, closing = balanced_argument(masked, token.end())
        except ValueError as exc:
            raise ValueError(f"{path.name}:{lineno}:{column}: {exc}") from exc
        records.append({
            "page_filename": path.name,
            "relative_path": path.relative_to(root).as_posix(),
            "scan": scan,
            "source_line": lineno,
            "source_column": column,
            "macro": name,
            "argument": text[opening + 1:closing],
            "argument_end_line": text.count("\n", 0, closing) + 1,
        })
    metadata = {
        "page_filename": path.name,
        "relative_path": path.relative_to(root).as_posix(),
        "scan": scan,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "occurrence_count": len(records),
    }
    return metadata, records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--max-scan", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output or root / "records/doubt_occurrences.json"
    pages = []
    occurrences = []
    for path in sorted((root / "pages").glob(f"{PREFIX}_15_scan*.tex")):
        match = re.fullmatch(rf"{PREFIX}_15_scan(\d{{3}})\.tex", path.name)
        if not match:
            continue
        scan = int(match[1])
        if args.max_scan is not None and scan > args.max_scan:
            continue
        metadata, records = index_page(path, root, scan)
        pages.append(metadata)
        occurrences.extend(records)
    counts = Counter(record["macro"] for record in occurrences)
    result = {
        "schema_version": 1,
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "scope": "Mechanical source index; no reading judgment or register-coverage assertion.",
        "source_line_convention": "1-based source lines and Unicode-character columns; all nested macro arguments retained verbatim.",
        "max_scan_requested": args.max_scan,
        "page_count": len(pages),
        "occurrence_count": len(occurrences),
        "counts": {name: counts[name] for name in ("unsure", "illegible")},
        "pages": pages,
        "occurrences": occurrences,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(output), "pages": len(pages), "occurrences": len(occurrences), "counts": result["counts"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
