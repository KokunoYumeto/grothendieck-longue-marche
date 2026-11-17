#!/usr/bin/env python3
"""Conservative lexical checks; never read or print manuscript prose.

Run with python -B to avoid creating bytecode. Results are structural warnings,
not a TeX compiler result or a verdict on the underlying manuscript readings.
"""

from pathlib import Path
import argparse
import re
import runpy


TOKEN = re.compile(r"\\(?:([A-Za-z]+)|.)", re.S)
EXTRA_MACROS = {"xhookrightarrow"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    strip = runpy.run_path(str(root / "support" / "validate.py"))["without_comments"]
    # Freeze the filename set for this invocation; subsequent pages are ignored.
    paths = tuple(sorted((root / "pages").glob("*.tex")))
    problems = []
    count_environments = count_diagrams = count_arrows = 0
    command_names = set()
    for path in paths:
        text = strip(path.read_text(encoding="utf-8"))
        stack = []
        math_stack = []
        dollars = TOKEN.sub("", text).count("$")
        if dollars % 2:
            problems.append(f"{path.name}: odd number of unescaped dollar signs ({dollars})")
        for token in TOKEN.finditer(text):
            command = token.group(1)
            if not command:
                delimiter = token.group(0)[1:]
                line = text.count("\n", 0, token.start()) + 1
                if delimiter in {"[", "("}:
                    math_stack.append((delimiter, line))
                elif delimiter in {"]", ")"}:
                    opening = {"]": "[", ")": "("}[delimiter]
                    if not math_stack or math_stack[-1][0] != opening:
                        problems.append(f"{path.name}:{line}: unmatched math delimiter \\{delimiter}")
                    else:
                        math_stack.pop()
                continue
            command_names.add(command)
            line = text.count("\n", 0, token.start()) + 1
            location = f"{path.name}:{line}"
            if command in EXTRA_MACROS:
                problems.append(f"{location}: \\{command} requires an additional definition/package")
            if command in {"begin", "end"}:
                argument = re.match(r"\s*\{([^{}]+)\}", text[token.end():])
                if argument is None:
                    problems.append(f"{location}: malformed environment delimiter")
                    continue
                environment = argument.group(1)
                if command == "begin":
                    stack.append((environment, line))
                    count_environments += 1
                    count_diagrams += environment == "tikzcd"
                elif not stack:
                    problems.append(f"{location}: unmatched end {environment}")
                elif stack[-1][0] != environment:
                    problems.append(f"{location}: end {environment} mismatches begin {stack[-1][0]} at line {stack[-1][1]}")
                else:
                    stack.pop()
            if command != "arrow":
                continue
            count_arrows += 1
            start = token.end()
            while start < len(text) and text[start].isspace():
                start += 1
            if start >= len(text) or text[start] != "[":
                continue  # Other supported tikz-cd arrow syntaxes not checked.
            depth, braces, quoted = 1, 0, False
            pos = start + 1
            while pos < len(text) and depth:
                char = text[pos]
                if char == '"' and text[pos - 1] != "\\":
                    quoted = not quoted
                if not quoted:
                    if char == "{":
                        braces += 1
                    elif char == "}":
                        braces -= 1
                    elif char == "[" and braces == 0:
                        depth += 1
                    elif char == "]" and braces == 0:
                        depth -= 1
                pos += 1
            if depth:
                problems.append(f"{location}: arrow options have no detected closing bracket")
            options = text[start + 1:pos - 1]
            if re.search(r'"\\\x27', options):
                problems.append(f"{location}: backslash-apostrophe immediately after arrow-label quote; tikz-cd swap suffix should be an unescaped apostrophe")
        for environment, line in stack:
            problems.append(f"{path.name}:{line}: unmatched begin {environment}")
        for delimiter, line in math_stack:
            problems.append(f"{path.name}:{line}: unmatched math delimiter \\{delimiter}")
    print("Snapshot:", ", ".join(path.stem.rsplit("scan", 1)[-1] for path in paths))
    print(f"Checked {len(paths)} pages, {count_environments} environments, {count_diagrams} tikzcd diagrams, {count_arrows} arrow commands.")
    print("Control-word tokens:", " ".join(sorted(command_names)))
    for problem in problems:
        print("REVIEW:", problem)
    print(f"Structural warnings: {len(problems)}.")
    print("No manuscript prose or labels are emitted. Arrow destinations and full PGF grammar require a real compile or manual inspection.")
    return bool(problems)


if __name__ == "__main__":
    raise SystemExit(main())
