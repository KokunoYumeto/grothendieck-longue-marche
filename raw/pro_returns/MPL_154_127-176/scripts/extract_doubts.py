#!/usr/bin/env python3
"""Extract editorial uncertainty markers as a mechanical staging table.

Usage:
    python scripts/extract_doubts.py --root /path/to/package
    python scripts/extract_doubts.py --root /path/to/package --scans 127-146

The utility snapshots the currently existing, correctly named page fragments
before parsing them. It extracts every lexical \\unsure and \\illegible command
outside comments and verbatim-like text. Each argument is located by balanced
brace parsing, with escaped braces and comments respected. Nested uncertainty
commands produce their own rows as well as remaining intact in outer arguments.

CSV columns:
    scan,tex_line,macro,complete_argument,source_snippet

tex_line is the one-based source line where the command begins. macro includes
its leading backslash. complete_argument is the exact source between the outer
argument braces; whitespace, comments, line breaks, and nested commands are
preserved. The short source_snippet is whitespace-normalized and may contain
ellipsis markers; it is only a navigation aid.

The default output is records/doubts_extracted.csv. This is a staging table,
not an interpretation, ranking, resolution, or final editorial judgment. The
utility does not read images or context archives and never edits page fragments.
Snapshot bytes, source hashes, and diagnostic metadata remain in temporary
storage. A nonzero exit status reports parse failures or sources changed during
the run; successfully parsed rows are still written for review.
An explicit --scans selection limits the snapshot and requires every selected
filename to exist. Later fragments are not opened.
"""

from __future__ import annotations

import argparse
from bisect import bisect_right
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import tempfile


PAGE_RE = re.compile(r"MPL_154_127-176_154_scan([0-9]{3})\.tex\Z")
TARGETS = {"unsure", "illegible"}
HEADER = ["scan", "tex_line", "macro", "complete_argument", "source_snippet"]
VERBATIM_ENVIRONMENTS = {"verbatim", "verbatim*", "lstlisting", "minted"}


def letter(char: str) -> bool:
    return "A" <= char <= "Z" or "a" <= char <= "z" or char == "@"


def control_word(source: str, position: int) -> tuple[str, int]:
    end = position + 1
    if end < len(source) and letter(source[end]):
        start = end
        while end < len(source) and letter(source[end]):
            end += 1
        return source[start:end], end
    return source[end:end + 1], min(end + 1, len(source))


def comment_end(source: str, position: int) -> int:
    end = source.find("\n", position)
    return len(source) if end < 0 else end


def skip_ignorable(source: str, position: int) -> int:
    while position < len(source):
        if source[position].isspace():
            position += 1
        elif source[position] == "%":
            position = comment_end(source, position)
        else:
            break
    return position


def verb_end(source: str, position: int) -> int:
    if position < len(source) and source[position] == "*":
        position += 1
    if position >= len(source):
        raise ValueError("unterminated verb command")
    delimiter = source[position]
    end = source.find(delimiter, position + 1)
    if end < 0:
        raise ValueError("unterminated verb command")
    return end + 1


def braced_argument(source: str, position: int) -> tuple[int, int]:
    """Return the opening-brace index and the index after its matching close."""
    start = skip_ignorable(source, position)
    if start >= len(source) or source[start] != "{":
        raise ValueError("editorial marker has no following braced argument")
    depth = 1
    position = start + 1
    while position < len(source):
        char = source[position]
        if char == "\\":
            name, position = control_word(source, position)
            if name == "verb":
                position = verb_end(source, position)
            continue
        if char == "%":
            position = comment_end(source, position)
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return start, position + 1
        position += 1
    raise ValueError("editorial marker argument has no matching closing brace")


def short_snippet(source: str, start: int, end: int, context_chars: int) -> str:
    left = max(0, start - context_chars)
    right = min(len(source), end + context_chars)
    marker = source[start:end]
    if len(marker) > 100:
        marker = marker[:68] + " … " + marker[-29:]
    snippet = source[left:start] + marker + source[end:right]
    snippet = re.sub(r"\s+", " ", snippet).strip()
    if left:
        snippet = "… " + snippet
    if right < len(source):
        snippet += " …"
    return snippet


def extract(source: str, scan: int, context_chars: int) -> tuple[list[dict], list[dict], int]:
    line_starts = [0] + [match.end() for match in re.finditer("\n", source)]
    rows = []
    errors = []
    markers_seen = 0
    position = 0
    while position < len(source):
        if source[position] == "%":
            position = comment_end(source, position)
            continue
        if source[position] != "\\":
            position += 1
            continue
        start = position
        name, position = control_word(source, position)
        line = bisect_right(line_starts, start)
        if name == "verb":
            try:
                position = verb_end(source, position)
            except ValueError as exc:
                errors.append({"tex_line": line, "message": str(exc)})
                break
            continue
        if name == "begin":
            try:
                argument_start, argument_end = braced_argument(source, position)
            except ValueError:
                continue
            environment = source[argument_start + 1:argument_end - 1].strip()
            if environment in VERBATIM_ENVIRONMENTS:
                terminator = "\\end{" + environment + "}"
                end = source.find(terminator, argument_end)
                if end < 0:
                    errors.append({"tex_line": line, "message": "unterminated verbatim-like environment"})
                    break
                position = end + len(terminator)
            continue
        if name not in TARGETS:
            continue
        markers_seen += 1
        try:
            argument_start, argument_end = braced_argument(source, position)
        except ValueError as exc:
            errors.append({"tex_line": line, "macro": "\\" + name, "message": str(exc)})
            continue
        rows.append({
            "scan": str(scan),
            "tex_line": str(line),
            "macro": "\\" + name,
            "complete_argument": source[argument_start + 1:argument_end - 1],
            "source_snippet": short_snippet(source, start, argument_end, context_chars),
        })
        # Continue after the command, not after the argument: nested markers
        # must be extracted independently while their original text is retained.
    return rows, errors, markers_seen


def scan_selection(value: str | None) -> set[int] | None:
    if value is None:
        return None
    selected: set[int] = set()
    for item in value.split(","):
        match = re.fullmatch(r"([0-9]{3})(?:-([0-9]{3}))?", item.strip())
        if match is None:
            raise ValueError("--scans must use three-digit scans or ranges")
        first = int(match.group(1))
        last = int(match.group(2) or first)
        if first < 127 or last > 176 or first > last:
            raise ValueError("--scans must be increasing ranges within 127–176")
        selected.update(range(first, last + 1))
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--scans", help="optional explicit scan range, for example 127-146; default is all currently available fragments")
    parser.add_argument("--output", type=Path, help="CSV destination; defaults to records/doubts_extracted.csv")
    parser.add_argument("--context-chars", type=int, default=40, help="source characters retained before and after a marker in its short snippet")
    args = parser.parse_args()
    root = args.root.expanduser().resolve()
    if not root.is_dir() or args.context_chars < 0:
        parser.error("--root must be an existing directory and --context-chars cannot be negative")
    try:
        selected = scan_selection(args.scans)
    except ValueError as exc:
        parser.error(str(exc))
    output = args.output.resolve() if args.output else root / "records" / "doubts_extracted.csv"
    work = Path(tempfile.mkdtemp(prefix="mpl154-doubts-extraction-"))
    snapshot = work / "snapshot"
    (snapshot / "pages").mkdir(parents=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    # Capture the filename inventory before reading the bytes of any fragment.
    try:
        names = tuple(sorted(path.name for path in (root / "pages").iterdir() if PAGE_RE.fullmatch(path.name) and 127 <= int(PAGE_RE.fullmatch(path.name).group(1)) <= 176 and (selected is None or int(PAGE_RE.fullmatch(path.name).group(1)) in selected)))
    except OSError as exc:
        parser.error(str(exc))
    if not names:
        parser.error("no correctly named page fragments are available")
    if selected is not None:
        present = {int(PAGE_RE.fullmatch(name).group(1)) for name in names}
        missing = sorted(selected - present)
        if missing:
            parser.error("requested scan filenames are missing: " + ", ".join(map(str, missing)))
    files = []
    errors = []
    for name in names:
        relative = "pages/" + name
        try:
            path = (root / relative).resolve()
            if root not in path.parents:
                raise ValueError("page path resolves outside the package root")
            data = path.read_bytes()
            (snapshot / relative).write_bytes(data)
            files.append({"relative_path": relative, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})
        except (OSError, ValueError) as exc:
            errors.append({"relative_path": relative, "message": str(exc)})
    rows = []
    markers_seen = 0
    for record in files:
        relative = record["relative_path"]
        try:
            source = (snapshot / relative).read_bytes().decode("utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append({"relative_path": relative, "message": str(exc)})
            continue
        scan = int(PAGE_RE.fullmatch(Path(relative).name).group(1))
        extracted, failures, seen = extract(source, scan, args.context_chars)
        rows.extend(extracted)
        markers_seen += seen
        errors.extend({"relative_path": relative, **failure} for failure in failures)
        record["extracted_rows"] = len(extracted)
        record["markers_seen"] = seen
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=HEADER, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    changed = []
    for record in files:
        try:
            if hashlib.sha256((root / record["relative_path"]).read_bytes()).hexdigest() != record["sha256"]:
                changed.append(record["relative_path"])
        except OSError:
            changed.append(record["relative_path"])
    counts = {"\\" + name: sum(row["macro"] == "\\" + name for row in rows) for name in sorted(TARGETS)}
    manifest = {"captured_at_utc": timestamp, "source_root": str(root), "scan_selection": args.scans, "filenames_first": names, "files": files, "markers_seen": markers_seen, "rows_written": len(rows), "macro_counts": counts, "errors": errors, "changed_since_snapshot": changed, "output": str(output)}
    (work / "extraction_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Captured {len(names)} filenames at {timestamp}; parsed {len(files)} snapshot files.")
    print(f"Wrote {len(rows)} rows from {markers_seen} uncertainty markers; parse/read errors: {len(errors)}.")
    print("Macro counts: " + json.dumps(counts, sort_keys=True))
    for error in errors:
        location = error["relative_path"] + (":" + str(error["tex_line"]) if "tex_line" in error else "")
        print("ERROR: " + location + ": " + error["message"])
    for relative in changed:
        print("CHANGED SINCE SNAPSHOT: " + relative)
    print("Staging CSV: " + str(output))
    print("Temporary snapshot and metadata: " + str(work))
    print("No editorial interpretation or judgment was made.")
    return 1 if errors or changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
