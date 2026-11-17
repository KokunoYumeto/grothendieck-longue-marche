#!/usr/bin/env python3
"""Preview/apply only tikz-cd ampersand portability edits before freezing.

Default: print a unified diff without writing. With --apply: write page files
and regenerate the combined transcription as the exact page concatenation.
No scan readings, inventory entries, timestamps, or audit records are changed.
"""
from __future__ import annotations

import argparse
import difflib
from pathlib import Path
import re
import sys

PREFIX = "MPL_64_040-077"
BEGIN = r"\begin{tikzcd}"
END = r"\end{tikzcd}"


def option_end(text: str, start: int) -> int:
    square = 0
    braces = 0
    index = start
    while index < len(text):
        char = text[index]
        if char == "\\":
            index += 2
            continue
        if char == "{":
            braces += 1
        elif char == "}":
            braces -= 1
        elif braces == 0 and char == "[":
            square += 1
        elif braces == 0 and char == "]":
            square -= 1
            if square == 0:
                return index
        index += 1
    raise ValueError("Unterminated tikzcd option list")


def replace_columns(body: str) -> tuple[str, int]:
    output: list[str] = []
    depth = 0
    environments: list[str] = []
    count = 0
    index = 0
    while index < len(body):
        char = body[index]
        if char == "%":
            stop = body.find("\n", index)
            stop = len(body) if stop < 0 else stop
            output.append(body[index:stop])
            index = stop
            continue
        if char == "\\":
            environment = re.match(r"\\(begin|end)\{([^}]+)\}", body[index:])
            if environment:
                action, name = environment.groups()
                if action == "begin":
                    environments.append(name)
                elif not environments or environments.pop() != name:
                    raise ValueError("Mismatched nested environment in tikzcd")
                output.append(environment.group())
                index += len(environment.group())
                continue
            control = re.match(r"\\(?:[A-Za-z]+|.)", body[index:], re.S)
            if control:
                output.append(control.group())
                index += len(control.group())
                continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
        if char == "&" and depth == 0 and not environments:
            output.append(r"\&")
            count += 1
        else:
            output.append(char)
        index += 1
    if depth != 0 or environments:
        raise ValueError("Unbalanced tikzcd body")
    return "".join(output), count


def transform(text: str) -> tuple[str, int, int]:
    output: list[str] = []
    cursor = 0
    diagrams = 0
    columns = 0
    while True:
        start = text.find(BEGIN, cursor)
        if start < 0:
            output.append(text[cursor:])
            break
        output.append(text[cursor:start + len(BEGIN)])
        body_start = start + len(BEGIN)
        option_start = body_start
        while option_start < len(text) and text[option_start].isspace():
            option_start += 1
        if option_start < len(text) and text[option_start] == "[":
            stop = option_end(text, option_start)
            options = text[option_start + 1:stop]
            if "ampersand replacement" not in options:
                options = r"ampersand replacement=\&," + options
            elif not re.search(r"ampersand replacement\s*=\s*\\&", options):
                raise ValueError("Existing different ampersand replacement; manual review needed")
            output.append(text[body_start:option_start] + "[" + options + "]")
            body_start = stop + 1
        else:
            output.append(r"[ampersand replacement=\&]")
        finish = text.find(END, body_start)
        if finish < 0:
            raise ValueError("Unterminated tikzcd environment")
        body, replaced = replace_columns(text[body_start:finish])
        output.append(body + END)
        cursor = finish + len(END)
        diagrams += 1
        columns += replaced
    return "".join(output), diagrams, columns


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if "transcription frozen " in (root / "progress.log").read_text(encoding="utf-8"):
            raise ValueError("Transcription is already frozen; refusing edits")
        pages = sorted((root / "pages").glob(f"{PREFIX}_64_scan*.tex"))
        planned: list[tuple[Path, str, str]] = []
        diagrams = columns = 0
        for path in pages:
            old = path.read_text(encoding="utf-8")
            new, nd, nc = transform(old)
            diagrams += nd
            columns += nc
            planned.append((path, old, new))
            if old != new:
                sys.stdout.writelines(difflib.unified_diff(
                    old.splitlines(keepends=True), new.splitlines(keepends=True),
                    fromfile=str(path.relative_to(root)), tofile=str(path.relative_to(root))))
        if args.apply:
            for path, old, new in planned:
                if old != new:
                    path.write_text(new, encoding="utf-8")
            (root / f"{PREFIX}_transcription.tex").write_text(
                "".join(new for _, _, new in planned), encoding="utf-8")
        print(f"{'Applied' if args.apply else 'Preview only:'} {diagrams} diagrams; "
              f"{columns} column separators replaced; "
              f"{sum(old != new for _, old, new in planned)} page files changed.")
        return 0
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
