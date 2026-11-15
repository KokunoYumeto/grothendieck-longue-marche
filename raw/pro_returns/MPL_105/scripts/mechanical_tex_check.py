#!/usr/bin/env python3
"""Check TeX structure without evaluating or interpreting manuscript content.

This reports only filenames, line numbers and technical diagnostics. It never
opens manuscript images or context files and never modifies page fragments.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
from pathlib import Path


EXPECTED = tuple(n for n in range(2, 54) if n not in {9, 24, 29, 42})
STATE = set("cotefile scanpage mspage deleted inserted margin uline uuline diagram figure unsure illegible".split())
STANDARD = set("""
Delta Downarrow Lambda Leftarrow Leftrightarrow Longleftrightarrow Longrightarrow
Omega Phi Pi Psi Rightarrow Sigma Updownarrow Vert alpha arrow begin beta big boxed
boxtimes bullet cap cdot cdots circ colon cup draw end eta exists forall gamma geq
hline hookrightarrow hspace in infty int joinrel ldots left leftarrow leq lhook
linewidth longrightarrow mapsto mathbf mathbin mathcal mathrm mathtt mid multicolumn
ne node operatorname otimes overbrace overline overset partial phantom pi pounds
prime psi qquad quad rho right rightarrow rule setminus sigma sim simeq stackrel
subset substack sup supset text textcircled textit textnormal textsf texttt theta
times to tikzcdmatrixname underbrace underline underset varinjlim varnothing varphi varprojlim vert
wedge widehat widetilde xi xrightarrow H b c
""".split())


def strip_comments(source: str) -> str:
    result = list(source)
    for i, char in enumerate(source):
        if char != "%":
            continue
        backslashes = 0
        j = i - 1
        while j >= 0 and source[j] == "\\":
            backslashes += 1
            j -= 1
        if backslashes % 2:
            continue
        j = i
        while j < len(source) and source[j] != "\n":
            result[j] = " "
            j += 1
    return "".join(result)


def escaped(text: str, i: int) -> bool:
    j = i - 1
    while j >= 0 and text[j] == "\\":
        j -= 1
    return (i - j - 1) % 2 == 1


def split_matrix(text: str):
    rows = [[]]
    depth = 0
    bracket_depth = 0
    start = 0
    i = 0
    while i < len(text):
        char = text[i]
        if char == "{" and not escaped(text, i):
            depth += 1
        elif char == "}" and not escaped(text, i):
            depth -= 1
        elif char == "[" and depth == 0 and not escaped(text, i):
            bracket_depth += 1
        elif char == "]" and depth == 0 and not escaped(text, i):
            bracket_depth -= 1
        elif char == "&" and depth == bracket_depth == 0 and not escaped(text, i):
            rows[-1].append((start, text[start:i]))
            start = i + 1
        elif text[i:i + 2] == "\\\\" and depth == bracket_depth == 0:
            rows[-1].append((start, text[start:i]))
            rows.append([])
            start = i + 2
            i += 1
        i += 1
    rows[-1].append((start, text[start:]))
    if len(rows) > 1 and len(rows[-1]) == 1 and not rows[-1][0][1].strip():
        rows.pop()
    return rows


def option_text(text: str, start: int):
    while start < len(text) and text[start].isspace():
        start += 1
    if start >= len(text) or text[start] != "[":
        return None
    depth = 1
    braces = 0
    i = start + 1
    while i < len(text):
        char = text[i]
        if char == "{" and not escaped(text, i):
            braces += 1
        elif char == "}" and not escaped(text, i):
            braces -= 1
        elif braces == 0 and char == "[" and not escaped(text, i):
            depth += 1
        elif braces == 0 and char == "]" and not escaped(text, i):
            depth -= 1
            if depth == 0:
                return text[start + 1:i]
        i += 1
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    issues = []
    pages = sorted((root / "pages").glob("*.tex"))
    diagram_count = 0
    arrow_count = 0
    markers = {}
    for path in pages:
        source = strip_comments(path.read_text(encoding="utf-8"))
        relative = path.relative_to(root).as_posix()

        def issue(offset, kind, detail):
            issues.append({"file": relative, "line": source.count("\n", 0, offset) + 1,
                           "kind": kind, "detail": detail})

        braces = []
        for i, char in enumerate(source):
            if char == "{" and not escaped(source, i):
                braces.append(i)
            elif char == "}" and not escaped(source, i):
                if braces:
                    braces.pop()
                else:
                    issue(i, "brace", "Unmatched closing brace")
        for i in braces:
            issue(i, "brace", "Unmatched opening brace")

        environments = []
        for match in re.finditer(r"\\(begin|end)\s*\{([^}]+)\}", source):
            if escaped(source, match.start()):
                continue
            command, name = match.groups()
            if command == "begin":
                environments.append((name, match.start()))
            elif not environments:
                issue(match.start(), "environment", f"Unmatched end of {name}")
            else:
                opened, _ = environments.pop()
                if opened != name:
                    issue(match.start(), "environment", f"End of {name} closes {opened}")
        for name, offset in environments:
            issue(offset, "environment", f"Unclosed environment {name}")

        math_stack = []
        math_patterns = r"\\[\[\]()]|\$\$?"
        pairs = {r"\(": r"\)", r"\[": r"\]", "$": "$", "$$": "$$"}
        for match in re.finditer(math_patterns, source):
            if escaped(source, match.start()):
                continue
            token = match.group()
            if math_stack and token == pairs[math_stack[-1][0]]:
                math_stack.pop()
            elif token in pairs:
                math_stack.append((token, match.start()))
            else:
                issue(match.start(), "math delimiter", f"Unmatched {token}")
        for token, offset in math_stack:
            issue(offset, "math delimiter", f"Unclosed {token}")

        for match in re.finditer(r"\\([A-Za-z]+)\b", source):
            if escaped(source, match.start()):
                continue
            command = match.group(1)
            if command not in STANDARD | STATE:
                issue(match.start(), "macro", f"Unknown or nonstandard command \\{command}")

        scan_markers = re.findall(r"\\scanpage\s*\{(\d+)\}", source)
        markers[path.name] = scan_markers
        name_match = re.fullmatch(r"MPL_105_105_scan(\d{3})\.tex", path.name)
        if not name_match:
            issue(0, "filename", "Unexpected page filename")
        elif scan_markers != [str(int(name_match.group(1)))]:
            issue(0, "marker", "scanpage count or value differs from filename")

        for diagram in re.finditer(r"\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}", source, re.S):
            diagram_count += 1
            matrix = diagram.group(1)
            # Remove optional environment options, preserving offsets.
            lead = len(matrix) - len(matrix.lstrip())
            if lead < len(matrix) and matrix[lead] == "[":
                opts = option_text(matrix, lead)
                if opts is not None:
                    stop = lead + len(opts) + 2
                    matrix = " " * stop + matrix[stop:]
            rows = split_matrix(matrix)
            for reference in re.finditer(r"\\tikzcdmatrixname\s*-\s*(\d+)\s*-\s*(\d+)", diagram.group(1)):
                rr, cc = map(int, reference.groups())
                if not (1 <= rr <= len(rows) and 1 <= cc <= len(rows[rr - 1])):
                    issue(diagram.start(1) + reference.start(), "TikZ target",
                          f"Named matrix reference row {rr}, column {cc} is outside the explicit matrix")
            for r, row in enumerate(rows, 1):
                for c, (cell_offset, cell) in enumerate(row, 1):
                    for arrow in re.finditer(r"\\(?:arrow|ar)\b", cell):
                        arrow_count += 1
                        options = option_text(cell, arrow.end())
                        if options is None:
                            continue
                        # Suppress labels when looking for direction options.
                        option_keys = re.sub(r'"(?:[^"\\]|\\.)*"', '""', options)
                        from_match = re.search(r"(?:^|,)\s*from\s*=\s*(\d+)\s*-\s*(\d+)", option_keys)
                        to_match = re.search(r"(?:^|,)\s*to\s*=\s*(\d+)\s*-\s*(\d+)", option_keys)
                        fr, fc = tuple(map(int, from_match.groups())) if from_match else (r, c)
                        if to_match:
                            tr, tc = map(int, to_match.groups())
                        else:
                            direction = re.search(r"(?:^|,)\s*([udlr]+)\s*(?:,|$)", option_keys)
                            if direction is None:
                                continue
                            d = direction.group(1)
                            tr = fr + d.count("d") - d.count("u")
                            tc = fc + d.count("r") - d.count("l")
                        for role, rr, cc in (("from", fr, fc), ("to", tr, tc)):
                            if not (1 <= rr <= len(rows) and 1 <= cc <= len(rows[rr - 1])):
                                issue(diagram.start(1) + cell_offset + arrow.start(), "TikZ target",
                                      f"Arrow {role} row {rr}, column {cc} is outside the explicit matrix")

    expected_names = {f"MPL_105_105_scan{n:03d}.tex" for n in EXPECTED}
    if {p.name for p in pages} != expected_names:
        issues.append({"file": "pages/", "line": 0, "kind": "coverage",
                       "detail": "Page filename set differs from the expected 48 scans"})
    python_count = 0
    for path in sorted((root / "scripts").glob("*.py")):
        python_count += 1
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except SyntaxError as exc:
            issues.append({"file": path.relative_to(root).as_posix(), "line": exc.lineno,
                           "kind": "Python syntax", "detail": exc.msg})
    print(json.dumps({"pages": len(pages), "scanpage_markers": sum(map(len, markers.values())),
                      "tikzcd_diagrams": diagram_count, "arrows": arrow_count,
                      "python_scripts": python_count, "issues": issues}, indent=2))
    return bool(issues)


if __name__ == "__main__":
    raise SystemExit(main())
