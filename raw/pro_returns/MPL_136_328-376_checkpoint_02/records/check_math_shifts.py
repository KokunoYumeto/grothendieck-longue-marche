#!/usr/bin/env python3
"""Read-only lexical check of explicit TeX math shifts, without interpreting text.

This supplements validate_package.py; it is not a TeX compiler. Text boxes and
TikZ pictures receive local mode scopes, so ordinary math inside those boxes
does not generate a false nested-math finding. The authorized editorial macros
are treated as transparent wrappers. Implicit math inside custom macros and
TikZ-CD cells cannot be certified by this lexical check.
"""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path

from validate_package import without_comments


TEXT_COMMANDS = {
    "text", "mbox", "hbox", "textrm", "textsf", "texttt", "textbf", "textit",
    "textsl", "textsc", "textnormal", "emph", "textcircled",
}
MATH_ENVS = {
    "math", "displaymath", "equation", "equation*", "align", "align*", "gather",
    "gather*", "multline", "multline*", "flalign", "flalign*", "alignat",
    "alignat*", "eqnarray", "eqnarray*",
}


def inspect(text: str) -> list[tuple[int, str]]:
    source = without_comments(text)
    findings: list[tuple[int, str]] = []
    # A mode is (opening token, character offset), or None for ordinary text.
    mode: tuple[str, int] | None = None
    groups: list[tuple[bool, tuple[str, int] | None]] = []
    env_scopes: list[tuple[str, tuple[str, int] | None]] = []
    pending_text = False
    i = 0

    def issue(position: int, message: str) -> None:
        findings.append((source.count("\n", 0, position) + 1, message))

    while i < len(source):
        char = source[i]
        if char.isspace():
            i += 1
            continue
        if char == "\\":
            match = re.match(r"\\([A-Za-z@]+|.)", source[i:], re.DOTALL)
            if not match:
                break
            token = match.group(1)
            end = i + len(match.group(0))
            if token in {"(", "["}:
                if mode is not None:
                    issue(i, f"Explicit \\{token} opens inside active {mode[0]} math")
                else:
                    mode = ("\\" + token, i)
            elif token in {")", "]"}:
                expected = "\\" + (")" if mode and mode[0] == "\\(" else "]")
                if mode is None or "\\" + token != expected or mode[0] not in {"\\(", "\\["}:
                    issue(i, f"Explicit \\{token} has no matching opening shift")
                else:
                    mode = None
            elif token == "rotatebox":
                angle = re.match(r"(?:\s*\[[^\]]*\])?\s*\{[^{}]*\}\s*", source[end:])
                if angle:
                    # graphicx typesets the following content argument in a text box.
                    end += len(angle.group(0))
                    pending_text = True
                    i = end
                    continue
            elif token in {"begin", "end"}:
                env = re.match(r"\s*\{([^{}]+)\}", source[end:])
                if env:
                    name = env.group(1)
                    end += len(env.group(0))
                    if name in MATH_ENVS:
                        if token == "begin":
                            if mode is not None:
                                issue(i, f"Math environment {name} opens inside active {mode[0]} math")
                            env_scopes.append((name, mode))
                            mode = (name, i)
                        elif env_scopes and env_scopes[-1][0] == name:
                            if mode is None or mode[0] != name:
                                issue(i, f"Math mode changed before end of {name}")
                            mode = env_scopes.pop()[1]
                    elif name in {"tikzpicture", "tikzcd"}:
                        if token == "begin":
                            env_scopes.append((name, mode))
                            mode = None
                        elif env_scopes and env_scopes[-1][0] == name:
                            if mode is not None:
                                issue(i, f"Explicit math shift remains open at end of {name}")
                            mode = env_scopes.pop()[1]
            pending_text = token in TEXT_COMMANDS
            i = end
            continue
        if char == "{":
            groups.append((pending_text, mode))
            if pending_text:
                mode = None
            pending_text = False
        elif char == "}":
            if groups:
                text_scope, prior_mode = groups.pop()
                if text_scope:
                    if mode is not None:
                        issue(i, "Explicit math remains open at end of a text box")
                    mode = prior_mode
            pending_text = False
        elif char == "$":
            token = "$$" if source[i:i+2] == "$$" else "$"
            if mode is None:
                mode = (token, i)
            elif mode[0] == token:
                mode = None
            else:
                issue(i, f"Explicit {token} occurs inside active {mode[0]} math")
            i += len(token)
            pending_text = False
            continue
        else:
            pending_text = False
        i += 1
    if mode is not None:
        issue(mode[1], f"Unclosed explicit math shift/environment {mode[0]}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, required=True)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    count = 0
    total = 0
    for path in sorted((args.root / "pages").glob("MPL_136_328-376_136_scan*.tex")):
        match = re.fullmatch(r"MPL_136_328-376_136_scan(\d{3})\.tex", path.name)
        if not match or int(match.group(1)) > args.through:
            continue
        contents = path.read_bytes()
        count += 1
        found = inspect(contents.decode("utf-8"))
        total += len(found)
        for line, message in found:
            print(f"REVIEW: {path.name}:{line}: {message}")
    print(f"Explicit math-shift check: {count} page files; {total} finding(s).")
    print("This is a lexical check, not compilation; custom-macro and TikZ-cell mode behavior is not certified.")
    return int(bool(total))


if __name__ == "__main__":
    raise SystemExit(main())
