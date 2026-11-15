#!/usr/bin/env python3
"""Repair TikZ-CD column-separator tokenization without rewriting content.

Preview:
    python scripts/repair_tikzcd_ampersands.py --root /path/to/package --scans 127-139
Apply the authorized syntax repair:
    python scripts/repair_tikzcd_ampersands.py --root /path/to/package --scans 127-139 --apply

Only explicitly selected page filenames are opened. The utility adds
``ampersand replacement=\\&`` to each tikzcd environment that lacks that option,
and inserts a backslash before its literal top-level column separators.
Existing ampersand-replacement options, escaped ampersands, comments, braced
content, arrow options, and nested environments are left unchanged. All edits
are insertions: no original byte is deleted, substituted, or reordered.

Original changed files and a machine-readable edit manifest are retained in a
temporary directory outside the deliverable. A concise repair report is the
only additional output written to the package. Concurrent changes cause a file
to be skipped rather than overwritten. No images or context archives are read.
This utility does not check manuscript meaning, labels, paths, or source fidelity.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import tempfile


WHITESPACE = b" \t\r\n\f"
PAGE_PREFIX = "MPL_154_127-176_154_scan"
OPTION = b"ampersand replacement=\\&"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def letter(value: int) -> bool:
    return 65 <= value <= 90 or 97 <= value <= 122 or value == 64


def control(data: bytes, position: int) -> tuple[bytes, int]:
    end = position + 1
    if end < len(data) and letter(data[end]):
        start = end
        while end < len(data) and letter(data[end]):
            end += 1
        return data[start:end], end
    return data[end:end + 1], min(end + 1, len(data))


def comment_end(data: bytes, position: int) -> int:
    end = data.find(b"\n", position)
    return len(data) if end < 0 else end


def skip_space(data: bytes, position: int) -> int:
    while position < len(data):
        if data[position] in WHITESPACE:
            position += 1
        elif data[position] == 37:
            position = comment_end(data, position)
        else:
            break
    return position


def without_comments(data: bytes) -> bytes:
    result = bytearray(data)
    position = 0
    while position < len(data):
        if data[position] == 92:
            _, position = control(data, position)
        elif data[position] == 37:
            end = comment_end(data, position)
            result[position:end] = b" " * (end - position)
            position = end
        else:
            position += 1
    return bytes(result)


def delimited(data: bytes, position: int, opening: int, closing: int) -> tuple[int, int] | None:
    position = skip_space(data, position)
    if position >= len(data) or data[position] != opening:
        return None
    start = position
    position += 1
    depth = 1
    braces = 0
    quoted = False
    while position < len(data):
        value = data[position]
        if value == 92:
            _, position = control(data, position)
            continue
        if value == 37:
            position = comment_end(data, position)
            continue
        if opening == 91:
            if value == 34 and braces == 0:
                quoted = not quoted
            if quoted:
                position += 1
                continue
            if value == 123:
                braces += 1
            elif value == 125:
                braces -= 1
                if braces < 0:
                    raise ValueError("unbalanced brace inside optional argument")
        if opening == 123 or braces == 0:
            if value == opening:
                depth += 1
            elif value == closing:
                depth -= 1
                if depth == 0:
                    return start, position + 1
        position += 1
    raise ValueError("unterminated TeX argument while locating environment syntax")


def environment_argument(data: bytes, position: int) -> tuple[bytes, int] | None:
    argument = delimited(data, position, 123, 125)
    if argument is None:
        return None
    start, end = argument
    return without_comments(data[start + 1:end - 1]).strip(), end


def verb_end(data: bytes, position: int) -> int:
    if position < len(data) and data[position] == 42:
        position += 1
    if position >= len(data):
        raise ValueError("unterminated verb command")
    delimiter = data[position:position + 1]
    end = data.find(delimiter, position + 1)
    if end < 0:
        raise ValueError("unterminated verb command")
    return end + 1


def tikzcd_environments(data: bytes) -> list[tuple[int, int, int, int]]:
    """Return begin start/end and end start/end offsets, without reading labels."""
    stack: list[tuple[int, int]] = []
    environments = []
    position = 0
    while position < len(data):
        if data[position] == 37:
            position = comment_end(data, position)
            continue
        if data[position] != 92:
            position += 1
            continue
        start = position
        name, position = control(data, position)
        if name == b"verb":
            position = verb_end(data, position)
            continue
        if name not in (b"begin", b"end"):
            continue
        argument = environment_argument(data, position)
        if argument is None:
            continue
        environment, position = argument
        if name == b"begin" and environment in (b"verbatim", b"verbatim*", b"lstlisting", b"minted"):
            terminator = b"\\end{" + environment + b"}"
            end = data.find(terminator, position)
            if end < 0:
                raise ValueError("unterminated verbatim-like environment")
            position = end + len(terminator)
            continue
        if environment != b"tikzcd":
            continue
        if name == b"begin":
            stack.append((start, position))
        elif not stack:
            raise ValueError("tikzcd end has no matching begin")
        else:
            begin_start, begin_end = stack.pop()
            environments.append((begin_start, begin_end, start, position))
    if stack:
        raise ValueError("tikzcd begin has no matching end")
    return sorted(environments)


def has_replacement_option(contents: bytes) -> bool:
    active = without_comments(contents)
    parts = []
    start = 0
    depth = 0
    quoted = False
    position = 0
    while position < len(active):
        value = active[position]
        if value == 92:
            _, position = control(active, position)
            continue
        if value == 123:
            depth += 1
        elif value == 125:
            depth -= 1
        elif value == 34 and depth == 0:
            quoted = not quoted
        elif value == 44 and depth == 0 and not quoted:
            parts.append(active[start:position])
            start = position + 1
        position += 1
    parts.append(active[start:])
    for part in parts:
        key = re.sub(rb"\s+", b" ", part.split(b"=", 1)[0].strip())
        if key == b"ampersand replacement" or key.endswith(b"/ampersand replacement"):
            return True
    return False


def column_separators(data: bytes, start: int, end: int) -> list[int]:
    """Locate only active, unbraced ampersands in this matrix environment."""
    positions = []
    position = start
    braces = 0
    nested: list[bytes] = []
    while position < end:
        value = data[position]
        if value == 37:
            position = comment_end(data, position)
            continue
        if value == 92:
            name, position = control(data, position)
            if name == b"verb":
                position = verb_end(data, position)
            elif name in (b"begin", b"end"):
                argument = environment_argument(data, position)
                if argument is not None:
                    environment, position = argument
                    if name == b"begin":
                        nested.append(environment)
                    elif not nested or nested.pop() != environment:
                        raise ValueError("mismatched nested environment inside tikzcd")
            elif name in (b"ar", b"arrow"):
                argument = delimited(data, position, 91, 93)
                if argument is not None:
                    position = argument[1]
            continue
        if value == 123:
            braces += 1
        elif value == 125:
            braces -= 1
            if braces < 0:
                raise ValueError("unbalanced braced content inside tikzcd")
        elif value == 38 and braces == 0 and not nested:
            positions.append(position)
        position += 1
    if braces or nested:
        raise ValueError("unclosed group or nested environment inside tikzcd")
    return positions


def repair_plan(data: bytes) -> tuple[bytes, list[dict], list[dict]]:
    insertions: list[tuple[int, int, bytes]] = []
    environments = []
    for begin_start, begin_end, end_start, _ in tikzcd_environments(data):
        option = delimited(data, begin_end, 91, 93)
        if option is not None and option[1] > end_start:
            raise ValueError("optional argument extends beyond tikzcd environment")
        line = data.count(b"\n", 0, begin_start) + 1
        if option is not None and has_replacement_option(data[option[0] + 1:option[1] - 1]):
            environments.append({"begin_line": line, "action": "already configured", "separator_insertions": 0})
            continue
        if option is None:
            insertions.append((begin_end, 0, b"[" + OPTION + b"]"))
            body_start = begin_end
        else:
            contents = without_comments(data[option[0] + 1:option[1] - 1]).strip()
            insertions.append((option[0] + 1, 0, OPTION + (b"," if contents else b"")))
            body_start = option[1]
        separators = column_separators(data, body_start, end_start)
        insertions.extend((position, 1, b"\\") for position in separators)
        environments.append({"begin_line": line, "action": "add ampersand replacement", "separator_insertions": len(separators)})
    pieces = []
    cursor = 0
    edits = []
    for position, priority, value in sorted(insertions, key=lambda item: (item[0], item[1])):
        pieces.append(data[cursor:position])
        pieces.append(value)
        cursor = position
        edits.append({"byte_offset": position, "priority": priority, "insert_ascii": value.decode("ascii")})
    pieces.append(data[cursor:])
    return b"".join(pieces), environments, edits


def scans_from_argument(value: str) -> tuple[int, ...]:
    scans = set()
    for part in value.split(","):
        match = re.fullmatch(r"([0-9]{3})(?:-([0-9]{3}))?", part.strip())
        if match is None:
            raise ValueError("--scans must use three-digit scans or ranges")
        first, last = int(match.group(1)), int(match.group(2) or match.group(1))
        if first < 127 or last > 176 or first > last:
            raise ValueError("--scans must be increasing ranges within 127–176")
        scans.update(range(first, last + 1))
    return tuple(sorted(scans))


def apply_insertions(path: Path, original: bytes, revised: bytes) -> None:
    if path.read_bytes() != original:
        raise ValueError("source changed after it was read; no repair applied")
    mode = stat.S_IMODE(path.stat().st_mode)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(prefix=".tikzcd-repair-", suffix=".tmp", dir=path.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(revised)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temporary, mode)
        if path.read_bytes() != original:
            raise ValueError("source changed before atomic replacement; no repair applied")
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--scans", required=True, help="explicit edit scope, for example 127-139")
    parser.add_argument("--apply", action="store_true", help="apply the insertion-only repairs; otherwise preview")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    root = args.root.expanduser().resolve()
    if not root.is_dir():
        parser.error("--root must be an existing package directory")
    try:
        selected = scans_from_argument(args.scans)
    except ValueError as exc:
        parser.error(str(exc))
    # Fix the exact filename scope before reading or editing any fragment.
    filenames = tuple(f"pages/{PAGE_PREFIX}{scan}.tex" for scan in selected)
    work = Path(tempfile.mkdtemp(prefix="mpl154-tikzcd-repair-"))
    report = args.report.resolve() if args.report else root / "MPL_154_127-176_tikzcd_syntax_repair_report.txt"
    records = []
    errors = []
    for relative in filenames:
        try:
            path = (root / relative).resolve()
            if root not in path.parents:
                raise ValueError("source resolves outside package root")
            original = path.read_bytes()
            revised, environments, edits = repair_plan(original)
            record = {"relative_path": relative, "sha256_before": sha256(original), "sha256_after": sha256(revised), "environments": environments, "insertions": edits, "changed": bool(edits), "applied": False}
            if edits and args.apply:
                backup = work / "before" / relative
                backup.parent.mkdir(parents=True, exist_ok=True)
                backup.write_bytes(original)
                apply_insertions(path, original, revised)
                record["applied"] = True
            records.append(record)
        except (OSError, ValueError) as exc:
            errors.append({"relative_path": relative, "message": str(exc)})
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    manifest = {"timestamp_utc": timestamp, "mode": "apply" if args.apply else "preview", "source_root": str(root), "filenames_first": filenames, "records": records, "errors": errors}
    (work / "repair_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    changed = [record for record in records if record["changed"]]
    count_env = sum(item["action"] == "add ampersand replacement" for record in records for item in record["environments"])
    count_amp = sum(item["separator_insertions"] for record in records for item in record["environments"])
    lines = [
        "MPL 154: TikZ-CD mechanical syntax repair report",
        "Generated: " + timestamp,
        "Mode: " + manifest["mode"],
        "Explicit scan scope: " + args.scans,
        f"Selected files: {len(filenames)}; files with repairs: {len(changed)}; errors: {len(errors)}.",
        f"Added ampersand-replacement options: {count_env}; inserted separator backslashes: {count_amp}.",
        "All edits are insertions. Every original byte remains in its original order.",
        "No labels, paths, images, or context archives were interpreted.", "",
    ]
    for record in records:
        state = "APPLIED" if record["applied"] else "PLANNED" if record["changed"] else "UNCHANGED"
        lines.append(record["relative_path"] + " | " + state)
        for item in record["environments"]:
            lines.append(f"  line {item['begin_line']}: {item['action']}; separator backslashes: {item['separator_insertions']}")
        if record["changed"]:
            lines.extend(["  SHA256 before: " + record["sha256_before"], "  SHA256 after:  " + record["sha256_after"]])
    for error in errors:
        lines.append("ERROR: " + error["relative_path"] + ": " + error["message"])
    lines.extend(["", "Temporary original-byte backups and edit manifest: " + str(work), "", "LIMITATION: This report establishes only the specified syntax transformation; source fidelity requires the separate manuscript audit."])
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{'Applied' if args.apply else 'Planned'} repairs in {len(changed)} file(s): {count_env} option(s), {count_amp} separator backslash(es); {len(errors)} error(s).")
    for error in errors:
        print("ERROR: " + error["relative_path"] + ": " + error["message"])
    print("Report: " + str(report))
    print("Temporary records: " + str(work))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
