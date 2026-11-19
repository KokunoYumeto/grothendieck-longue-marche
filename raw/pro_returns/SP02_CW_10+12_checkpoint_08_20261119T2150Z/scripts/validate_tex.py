#!/usr/bin/env python3
"""Non-mutating structural checks for diplomatic LaTeX fragments.

This is a lexical balance check, not a TeX engine and not a reading check.
It ignores comments, escaped punctuation, inline verbatim, and the contents
of common verbatim environments. It checks braces, explicit math delimiters,
and begin/end environment names without expanding macros. Math delimiters and
environments must close within the same explicit brace groups in which they
opened; macro-created groups and TeX mode changes are not inferred.
"""
from __future__ import annotations

import argparse
import bisect
from dataclasses import dataclass, asdict
import json
from pathlib import Path
import re
import sys


VERBATIM_ENVIRONMENTS = {"verbatim", "verbatim*", "Verbatim", "lstlisting", "minted", "comment"}


@dataclass
class Issue:
    line: int
    column: int
    kind: str
    message: str


def strip_comments(text: str) -> str:
    """Replace comments by spaces while retaining offsets and newlines.

    A control symbol consumes exactly its next character, so \\% is escaped
    but a percent after two backslashes starts a comment.
    """
    chars = list(text)
    i = 0
    while i < len(text):
        if text[i] == "\\":
            # Handle inline verbatim before comments; its delimiter may be %.
            match = re.match(r"\\verb\*?(?![A-Za-z])", text[i:])
            if match:
                j = i + len(match.group())
                if j < len(text) and not text[j].isspace():
                    close = text.find(text[j], j + 1)
                    newline = text.find("\n", j + 1)
                    if close >= 0 and (newline < 0 or close < newline):
                        i = close + 1
                        continue
            i += 2
        elif text[i] == "%":
            end = text.find("\n", i)
            if end < 0:
                end = len(text)
            chars[i:end] = " " * (end - i)
            i = end
        else:
            i += 1
    return "".join(chars)


def validate_text(text: str, name: str = "<text>") -> dict:
    """Return a JSON-compatible result without changing the supplied text."""
    s = strip_comments(text)
    starts = [0] + [m.end() for m in re.finditer("\n", text)]
    issues: list[Issue] = []
    braces: list[int] = []
    maths: list[tuple[str, int, tuple[int, ...]]] = []
    envs: list[tuple[str, int, tuple[int, ...]]] = []
    counts = {"brace_pairs": 0, "math_pairs": 0, "environment_pairs": 0}

    def issue(pos: int, kind: str, message: str) -> None:
        row = bisect.bisect_right(starts, pos) - 1
        issues.append(Issue(row + 1, pos - starts[row] + 1, kind, message))

    def open_math(token: str, pos: int) -> None:
        # Keep group identities as well as depth: closing one brace group and
        # opening another at the same depth must not hide a crossed boundary.
        maths.append((token, pos, tuple(braces)))

    def close_math(expected: str, token: str, pos: int) -> None:
        if not maths:
            issue(pos, "math", f"Unmatched closing delimiter {token}")
        elif maths[-1][0] != expected:
            issue(pos, "math", f"Closing {token} does not match open {maths[-1][0]}")
        else:
            opened_groups = maths[-1][2]
            if tuple(braces) != opened_groups:
                issue(pos, "math", f"Closing {token} crosses a brace-group boundary "
                      f"(opened at depth {len(opened_groups)}, closed at depth {len(braces)})")
            maths.pop()
            counts["math_pairs"] += 1

    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "\\":
            if i + 1 == len(s):
                issue(i, "control", "Trailing backslash has no following character")
                i += 1
                continue
            verb = re.match(r"\\verb\*?(?![A-Za-z])", s[i:])
            if verb:
                j = i + len(verb.group())
                if j >= len(s) or s[j].isspace():
                    issue(i, "verbatim", "Missing non-space delimiter after \\verb")
                    i = j
                    continue
                end = s.find(s[j], j + 1)
                newline = s.find("\n", j + 1)
                if end < 0 or (newline >= 0 and newline < end):
                    issue(i, "verbatim", "Inline \\verb does not close on its line")
                    i = newline if newline >= 0 else len(s)
                else:
                    i = end + 1
                continue
            control = re.match(r"\\[A-Za-z@]+", s[i:])
            if control:
                command = control.group()
                after = i + len(command)
                if command in (r"\begin", r"\end"):
                    arg = re.match(r"\s*\{([^{}\n]+)\}", s[after:])
                    if not arg:
                        issue(i, "environment", f"{command} lacks a simple {{environment}} argument")
                    else:
                        env = arg.group(1).strip()
                        endarg = after + arg.end()
                        if command == r"\begin":
                            if env in VERBATIM_ENVIRONMENTS:
                                pattern = re.compile(r"\\end\s*\{" + re.escape(env) + r"\}")
                                end = pattern.search(text, endarg)
                                if not end:
                                    issue(i, "environment", f"Unclosed verbatim environment {env}")
                                    i = len(s)
                                else:
                                    counts["environment_pairs"] += 1
                                    i = end.end()
                                continue
                            envs.append((env, i, tuple(braces)))
                        elif not envs:
                            issue(i, "environment", f"Unmatched \\end{{{env}}}")
                        elif envs[-1][0] != env:
                            issue(i, "environment", f"\\end{{{env}}} does not match \\begin{{{envs[-1][0]}}}")
                        else:
                            opened_groups = envs[-1][2]
                            if tuple(braces) != opened_groups:
                                issue(i, "environment", f"\\end{{{env}}} crosses a brace-group boundary "
                                      f"(opened at depth {len(opened_groups)}, closed at depth {len(braces)})")
                            envs.pop()
                            counts["environment_pairs"] += 1
                i = after
                continue
            token = s[i:i + 2]
            if token in (r"\[", r"\("):
                open_math(token, i)
            elif token == r"\]":
                close_math(r"\[", token, i)
            elif token == r"\)":
                close_math(r"\(", token, i)
            # Every other control symbol, including \{, \}, \$, \%, and
            # \\, is consumed without treating its second character as syntax.
            i += 2
        elif ch == "{":
            braces.append(i)
            i += 1
        elif ch == "}":
            if braces:
                braces.pop()
                counts["brace_pairs"] += 1
            else:
                issue(i, "brace", "Unmatched closing brace }")
            i += 1
        elif ch == "$":
            token = "$$" if s.startswith("$$", i) else "$"
            # A text-producing macro inside inline math can itself contain
            # inline math, e.g. $a\text{for $i$ odd}$. At a strictly deeper
            # group, start a nested dollar pair rather than closing the outer
            # pair across that group. This remains a lexical allowance: the
            # checker does not decide whether that macro switches TeX modes.
            nested_group = bool(maths and len(braces) > len(maths[-1][2])
                                and tuple(braces[:len(maths[-1][2])]) == maths[-1][2])
            if maths and maths[-1][0] in ("$", "$$") and nested_group:
                open_math(token, i)
            elif maths and maths[-1][0] == token:
                close_math(token, token, i)
            elif maths and maths[-1][0] in ("$", "$$"):
                issue(i, "math", f"Delimiter {token} does not match open {maths[-1][0]}")
            else:
                # A dollar pair within a \text{...} group of display math
                # can be valid. This lexical check permits that nesting and
                # deliberately does not infer TeX's current mode.
                open_math(token, i)
            i += len(token)
        else:
            i += 1

    for pos in braces:
        issue(pos, "brace", "Unclosed opening brace {")
    for token, pos, _groups in maths:
        issue(pos, "math", f"Unclosed math delimiter {token}")
    for env, pos, _groups in envs:
        issue(pos, "environment", f"Unclosed environment {env}")
    issues.sort(key=lambda x: (x.line, x.column, x.kind))
    return {"file": name, "ok": not issues, "counts": counts, "issues": [asdict(x) for x in issues]}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="LaTeX files or directories (directories recurse over *.tex)")
    parser.add_argument("--json", action="store_true", help="Write the complete report as JSON to stdout")
    args = parser.parse_args(argv)
    files: list[Path] = []
    for path in args.paths:
        if path.is_dir():
            files.extend(sorted(path.rglob("*.tex")))
        else:
            files.append(path)
    files = list(dict.fromkeys(files))
    if not files:
        parser.error("No LaTeX files found")
    results: list[dict] = []
    for file in files:
        try:
            results.append(validate_text(file.read_text(encoding="utf-8"), str(file)))
        except (OSError, UnicodeError) as exc:
            results.append({"file": str(file), "ok": False, "counts": {}, "issues": [asdict(Issue(0, 0, "io", str(exc)))]})
    report = {"checker": "lexical balance only; no macro expansion or compilation", "ok": all(x["ok"] for x in results), "files": len(results), "results": results}
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        for result in results:
            print(f"{'PASS' if result['ok'] else 'FAIL'} {result['file']}")
            for item in result["issues"]:
                print(f"  {item['line']}:{item['column']} [{item['kind']}] {item['message']}")
        print(f"{sum(x['ok'] for x in results)}/{len(results)} files passed lexical balance checks; no compilation performed.")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
