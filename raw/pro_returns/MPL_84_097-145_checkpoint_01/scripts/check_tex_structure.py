#!/usr/bin/env python3
"""Syntax-only checks; no images, OCR, or manuscript reading judgments."""
from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path

from package_tools import brace_errors, uncomment


def check(path: Path) -> list[str]:
    text = uncomment(path.read_text(encoding="utf-8"))
    issues = brace_errors(text)
    controls: list[str] = []
    delimiters: list[tuple[str, int]] = []
    position = 0
    line = 1
    dollar_count = 0
    while position < len(text):
        char = text[position]
        if char == "\\" and position + 1 < len(text):
            end = position + 1
            if text[end].isalpha():
                while end < len(text) and text[end].isalpha():
                    end += 1
            else:
                end += 1
            control = text[position + 1:end]
            controls.append(control)
            if control in ("[", "("):
                delimiters.append((control, line))
            elif control in ("]", ")"):
                opening = "[" if control == "]" else "("
                if not delimiters or delimiters[-1][0] != opening:
                    issues.append(f"unmatched math delimiter \\{control} at line {line}")
                else:
                    delimiters.pop()
            line += text[position:end].count("\n")
            position = end
        else:
            if char == "$":
                dollar_count += 1
            if char == "\n":
                line += 1
            position += 1
    for control, line_number in delimiters:
        issues.append(f"unclosed math delimiter \\{control} at line {line_number}")
    if dollar_count % 2:
        issues.append("odd number of unescaped dollar signs")
    if controls.count("left") != controls.count("right"):
        issues.append("counts of \\left and \\right differ")
    environments: list[tuple[str, int]] = []
    for token in re.finditer(r"\\(begin|end)\{([^}]+)\}", text):
        kind, environment = token.groups()
        line_number = text[:token.start()].count("\n") + 1
        if kind == "begin":
            environments.append((environment, line_number))
        elif not environments:
            issues.append(f"unmatched end of {environment} at line {line_number}")
        elif environments[-1][0] != environment:
            issues.append(f"end of {environment} at line {line_number} mismatches {environments[-1][0]}")
        else:
            environments.pop()
    for environment, line_number in environments:
        issues.append(f"unclosed {environment} at line {line_number}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--report", type=Path, help="Optional plain-text report path")
    args = parser.parse_args()
    page_paths = sorted((args.root / "pages").glob("*.tex"))
    findings = [(path.name, issue) for path in page_paths for issue in check(path)]
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    report = [
        f"Mechanical TeX structure check {stamp}",
        f"Page files checked: {len(page_paths)}",
        f"Issues: {len(findings)}",
        "This does not certify compilation, visual transcription, or completeness.",
        "Files: " + ", ".join(path.name for path in page_paths),
        *[name + ": " + issue for name, issue in findings],
    ]
    output = "\n".join(report) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(output, encoding="utf-8")
    print(output, end="")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
