#!/usr/bin/env python3
"""Propose or apply the three explicitly authorized LaTeX syntax repairs.

Default: dry run. Add --apply only before the transcription is frozen.
No image/context access and no changes to wording, formula objects, or arrows.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


STEM = "MPL_22+23_002-016"
TIKZCD = re.compile(r"\\begin\{tikzcd\}(?:\[([^\]]*)\])?([\s\S]*?)\\end\{tikzcd\}")
NESTED_OLD = r"\deleted{$\unsure{\Omega^r}$}"
NESTED_NEW = r"\deleted{\unsure{\Omega^r}}"


def escaped_ampersands(body: str) -> tuple[str, int]:
    pieces = []
    count = 0
    for position, char in enumerate(body):
        if char == "&":
            backslashes = 0
            before = position - 1
            while before >= 0 and body[before] == "\\":
                backslashes += 1
                before -= 1
            if backslashes % 2 == 0:
                pieces.append("\\")
                count += 1
        pieces.append(char)
    return "".join(pieces), count


def repair(name: str, source: str) -> tuple[str, dict]:
    changes = {"tikzcd_options_added": 0, "tikzcd_separators_escaped": 0,
               "nested_dollar_pairs_removed": 0, "array_math_delimiter_pairs_added": 0}

    def replace_diagram(match: re.Match) -> str:
        options = match.group(1)
        body = match.group(2)
        option_match = re.search(r"ampersand\s+replacement\s*=\s*([^,]+)", options or "")
        if option_match and option_match.group(1).strip() != r"\&":
            raise ValueError(f"{name}: existing ampersand replacement differs from the authorized value")
        if not option_match:
            options = (options + "," if options else "") + r"ampersand replacement=\&"
            changes["tikzcd_options_added"] += 1
        body, escaped = escaped_ampersands(body)
        changes["tikzcd_separators_escaped"] += escaped
        return r"\begin{tikzcd}[" + options + "]" + body + r"\end{tikzcd}"

    result = TIKZCD.sub(replace_diagram, source)
    if name == f"{STEM}_23_scan004.tex":
        count = result.count(NESTED_OLD)
        if count > 1:
            raise ValueError(f"{name}: nested-dollar target occurs more than once; manual review required")
        if count:
            result = result.replace(NESTED_OLD, NESTED_NEW)
            changes["nested_dollar_pairs_removed"] = 1
        elif NESTED_NEW not in result:
            raise ValueError(f"{name}: neither original nor repaired nested-dollar target is present")
    if name == f"{STEM}_23_scan006.tex":
        old_start = r"\diagram{\begin{array}{cc}"
        old_end = r"\end{array}}"
        new_start = r"\diagram{\[\begin{array}{cc}"
        new_end = r"\end{array}\]}"
        if old_start in result:
            if result.count(old_start) != 1 or result.count(old_end) != 1:
                raise ValueError(f"{name}: array delimiter target is ambiguous; manual review required")
            result = result.replace(old_start, new_start, 1).replace(old_end, new_end, 1)
            changes["array_math_delimiter_pairs_added"] = 1
        elif new_start not in result or new_end not in result:
            raise ValueError(f"{name}: neither original nor repaired array delimiter target is present")
    return result, changes


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--apply", action="store_true", help="write the authorized syntax changes before freeze")
    args = parser.parse_args()
    root = args.root.resolve()
    log_path = root / "progress.log"
    if args.apply and log_path.exists() and re.search(r"(?m)^transcription frozen\b", log_path.read_text()):
        raise SystemExit("The transcription is frozen. No file was changed.")
    pending = []
    for path in sorted((root / "pages").glob(f"{STEM}_*_scan*.tex")):
        before = path.read_bytes()
        result, changes = repair(path.name, before.decode("utf-8"))
        after = result.encode("utf-8")
        if before != after:
            pending.append((path, before, after, changes))
    report = {"timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
              "mode": "applied" if args.apply else "dry_run", "files": []}
    for path, before, after, changes in pending:
        if args.apply:
            # Recheck the same bytes immediately before writing; concurrent
            # manual transcription changes must not be overwritten.
            if path.read_bytes() != before:
                raise SystemExit(f"{path.name} changed since preparation; stopped without overwriting it")
            path.write_bytes(after)
        report["files"].append({"file": str(path.relative_to(root)),
                                "before_sha256": digest(before),
                                "after_sha256": digest(after), **changes})
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    print(rendered, end="")
    if args.apply:
        (root / "records" / "syntax_repair_log.json").write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
