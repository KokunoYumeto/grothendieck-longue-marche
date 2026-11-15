#!/usr/bin/env python3
"""Read-only, conservative TeX/TikZ diagnostics; no manuscript images are read."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
from validate import scan_tex  # noqa: E402


def control_tokens(text):
    """Yield control tokens without mistaking the second slash in a row break for an opener."""
    i = 0
    while i < len(text):
        if text[i] != "\\":
            i += 1
            continue
        match = re.match(r"\\[A-Za-z@]+|\\.", text[i:], re.DOTALL)
        if match:
            yield match[0], i
            i += len(match[0])
        else:
            i += 1


def close_group(text, start, opening="[", closing="]"):
    depth = 1
    braces = 0
    i = start + 1
    while i < len(text):
        if text[i] == "\\":
            i += 2
            continue
        char = text[i]
        if opening == "[":
            if char == "{":
                braces += 1
            elif char == "}":
                braces -= 1
        if braces == 0:
            if char == opening:
                depth += 1
            elif char == closing:
                depth -= 1
                if depth == 0:
                    return i
        i += 1
    return None


def split_matrix(body):
    """Split only matrix-level cells, leaving nested macro/environment contents intact."""
    rows = [[]]
    braces = 0
    brackets = 0
    envs = []
    start = 0
    i = 0
    literal_separators = 0
    escaped_separators = 0
    while i < len(body):
        char = body[i]
        if char == "\\":
            env_match = re.match(r"\\(begin|end)\{([^{}]+)\}", body[i:])
            if env_match:
                action, name = env_match.groups()
                if action == "begin":
                    envs.append(name)
                elif envs and envs[-1] == name:
                    envs.pop()
                i += len(env_match[0])
                continue
            if i + 1 < len(body) and body[i + 1] in "\\&" and not (braces or brackets or envs):
                rows[-1].append((body[start:i], start))
                if body[i + 1] == "\\":
                    rows.append([])
                else:
                    escaped_separators += 1
                i += 2
                start = i
                continue
            command = re.match(r"\\[A-Za-z@]+|\\.", body[i:], re.DOTALL)
            i += len(command[0]) if command else 1
            continue
        if char == "{":
            braces += 1
        elif char == "}":
            braces -= 1
        elif braces == 0 and char == "[":
            brackets += 1
        elif braces == 0 and char == "]" and brackets:
            brackets -= 1
        elif char == "&" and not (braces or brackets or envs):
            rows[-1].append((body[start:i], start))
            literal_separators += 1
            i += 1
            start = i
            continue
        i += 1
    rows[-1].append((body[start:], start))
    return rows, literal_separators, escaped_separators


def review_file(path):
    raw = path.read_text(encoding="utf-8")
    text, commands, _ = scan_tex(raw)
    diagnostics = []
    diagrams = []

    def add(level, line, code, message):
        diagnostics.append({"level": level, "line": line, "code": code, "message": message})

    def line_at(position):
        return text[:position].count("\n") + 1

    delimiters = []
    tokens = list(control_tokens(text))
    for token, position in tokens:
        if token in (r"\[", r"\("):
            delimiters.append((token, line_at(position)))
        elif token in (r"\]", r"\)"):
            expected = r"\[" if token == r"\]" else r"\("
            if not delimiters or delimiters[-1][0] != expected:
                add("error", line_at(position), "math-delimiter", f"Unmatched or misordered explicit math delimiter {token}")
            else:
                delimiters.pop()
    for token, line in delimiters:
        add("error", line, "math-delimiter", f"Unclosed explicit math delimiter {token}")
    left_right = []
    for token, position in tokens:
        if token == r"\left":
            left_right.append(line_at(position))
        elif token == r"\right":
            if left_right:
                left_right.pop()
            else:
                add("error", line_at(position), "left-right", "Unpaired right delimiter command")
    for line in left_right:
        add("error", line, "left-right", "Unpaired left delimiter command")

    env_stack = []
    for match in re.finditer(r"\\(begin|end)\{([^{}]+)\}", text):
        action, environment = match.groups()
        if action == "begin":
            if environment == "tikzcd" and "tikzcd" in env_stack:
                add("error", line_at(match.start()), "nested-tikzcd", "A tikzcd environment is nested inside another tikzcd")
            env_stack.append(environment)
        elif env_stack and env_stack[-1] == environment:
            env_stack.pop()

    for begin in re.finditer(r"\\begin\{tikzcd\}", text):
        pos = begin.end()
        while pos < len(text) and text[pos].isspace():
            pos += 1
        options = ""
        if pos < len(text) and text[pos] == "[":
            end = close_group(text, pos)
            if end is None:
                add("error", line_at(pos), "tikz-options", "Unclosed tikzcd option list")
                continue
            options = text[pos + 1:end]
            pos = end + 1
        stop = text.find(r"\end{tikzcd}", pos)
        if stop < 0:
            continue  # The structural validator reports missing environments.
        body = text[pos:stop]
        rows, literals, escaped = split_matrix(body)
        line = line_at(begin.start())
        diagrams.append({"line": line, "row_widths": [len(row) for row in rows], "literal_cell_separators": literals, "escaped_cell_separators": escaped})
        if literals:
            add("warning", line, "tikz-ampersand", f"{literals} literal cell separators remain; an ordinary enclosing macro argument requires ampersand replacement and escaped separators")
        if escaped and not re.search(r"ampersand\s+replacement\s*=\s*\\&", options):
            add("warning", line, "tikz-ampersand-option", "Escaped cell separators occur without a local ampersand replacement option; check consumer-wide settings")
        empty_nodes = "nodes in empty cells" in options
        for r, row in enumerate(rows, 1):
            for c, (cell, offset) in enumerate(row, 1):
                for arrow in re.finditer(r"\\(?:arrow|ar)\[", cell):
                    end = close_group(cell, arrow.end() - 1)
                    if end is None:
                        add("error", line_at(pos + offset + arrow.start()), "arrow-options", "Unclosed arrow option list")
                        continue
                    arrow_options = cell[arrow.end():end]
                    direction = re.match(r"\s*([rldu]+)\s*(?:,|$)", arrow_options)
                    if not direction or re.search(r"\b(?:from|to)\s*=", arrow_options):
                        continue
                    value = direction[1]
                    target_r = r + value.count("d") - value.count("u")
                    target_c = c + value.count("r") - value.count("l")
                    source = f"row {r}, column {c}"
                    target = f"row {target_r}, column {target_c}"
                    arrow_line = line_at(pos + offset + arrow.start())
                    if target_r < 1 or target_r > len(rows) or target_c < 1 or target_c > len(rows[target_r - 1]):
                        add("error", arrow_line, "arrow-target", f"Direction {value!r} from {source} addresses absent {target}")
                    elif not rows[target_r - 1][target_c - 1][0].strip() and not empty_nodes:
                        add("warning", arrow_line, "arrow-empty-target", f"Direction {value!r} from {source} addresses blank {target}; check node creation")
        for anchor in re.finditer(r"\(([A-Za-z][A-Za-z0-9_-]*?)-(\d+)-(\d+)\.[^)]+\)", options):
            name, r_text, c_text = anchor.groups()
            r, c = int(r_text), int(c_text)
            if r < 1 or r > len(rows) or c < 1 or c > len(rows[r - 1]):
                add("error", line, "anchor-target", f"Anchor {name}-{r}-{c} refers outside the encoded matrix")
            elif not rows[r - 1][c - 1][0].strip() and not empty_nodes:
                add("warning", line, "anchor-empty-cell", f"Anchor {name}-{r}-{c} refers to an empty cell without local nodes in empty cells")
    for match in re.finditer(r"\\(?:deleted|unsure)\s*\{\s*[_^]", text):
        add("advisory", line_at(match.start()), "leading-script", "Marked argument begins with a subscript/superscript; its behavior depends on consumer macro definitions")
    return {"file": path.name, "diagrams": diagrams, "diagnostics": diagnostics}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--max-scan", type=int, default=81)
    args = parser.parse_args()
    files = []
    for path in sorted((args.root / "pages").glob("MPL_72_035-081_72_scan*.tex")):
        if int(path.stem[-3:]) <= args.max_scan:
            files.append(review_file(path))
    result = {
        "scope": "Static source diagnostics only; no TeX expansion, compilation, rendering, or image comparison. Inspect findings before changing a fragment.",
        "file_count": len(files),
        "tikzcd_count": sum(len(item["diagrams"]) for item in files),
        "error_count": sum(d["level"] == "error" for f in files for d in f["diagnostics"]),
        "files": [item for item in files if item["diagrams"] or item["diagnostics"]],
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if result["error_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
