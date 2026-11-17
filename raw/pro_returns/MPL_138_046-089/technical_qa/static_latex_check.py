#!/usr/bin/env python3
r"""Read-only, conservative static checks for the saved LaTeX page fragments.

This is not a TeX interpreter or a compilation test. It never reads images,
archives, context, or files outside the selected pages directory. Custom
annotation commands are assumed to preserve their caller's mode. Findings in
the custom \diagram wrapper are conditional because its definition is not in
the page fragments. An optional JSON result records exact file hashes.
"""
from __future__ import annotations

import argparse
import collections
import datetime
import hashlib
import json
from pathlib import Path
import re

TOK = re.compile(r"\\[A-Za-z@]+|\\.|[{}$^_]")
ENV = re.compile(r"\\(begin|end)\s*\{([^{}]+)\}")
TEXT_ARGS = set("text textrm textsf texttt textsc textbf textit textnormal textsuperscript textsubscript textcircled mbox hbox".split())
TRANSPARENT = set("unsure inserted deleted uline uuline underline margin figure diagram".split())
MATH_ONLY = set("""Delta Gamma Longleftrightarrow Longrightarrow Omega Phi Pi Sigma
Vert alpha bar beta bigl bigr bigwedge boxed bullet cdot cdots chi circ coprod cos
dfrac displaystyle downarrow ell exists forall frac gamma geq in infty lambda
leadsto left leftarrow leftrightarrow leq longleftarrow longleftrightarrow longmapsto longrightarrow mathbb
mathbf mathcal mathfrak mathord mathrm mid middle mp mu ne nu omega operatorname
overbrace overline overset pi pm prod rho right setminus sigma sim simeq sin
subset substack sum supset tau tfrac times to underbrace underset varepsilon
varnothing varphi varprojlim vdots vee vphantom wedge widehat widetilde xi
xrightarrow zeta""".split())
MATH_ENVS = set("array aligned alignedat gathered split matrix pmatrix bmatrix Bmatrix vmatrix Vmatrix cases smallmatrix".split())
DISPLAY_ENVS = set("equation equation* align align* alignat alignat* gather gather* multline multline* displaymath math".split())
# Use an explicit set: keys can themselves contain spaces.
ARROW_KEYS = {"dash", "dashed", "dotted", "tail", "leftrightarrow", "mapsto",
              "very thick", "draw", "bend left", "bend right", "shorten <",
              "shorten >", "near start", "near end"}


def clean_comments(s):
    # Replacing rather than deleting preserves every source offset and line.
    return re.sub(r"\\.|%[^\n]*", lambda m: " " * len(m[0]) if m[0].startswith("%") else m[0], s)


class Checker:
    def __init__(self, path):
        self.path = path
        self.raw = path.read_text(encoding="utf-8")
        self.s = clean_comments(self.raw)
        self.findings = []
        self.groups = {}
        self.envs = {}
        self.ulines = []
        self.arrows = []
        self.commands = collections.Counter(m[0][1:] for m in TOK.finditer(self.s)
                                            if re.fullmatch(r"\\[A-Za-z@]+", m[0]))

    def line(self, pos):
        return self.s.count("\n", 0, pos) + 1

    def add(self, code, pos, message, severity="review", context=()):
        self.findings.append({"file": self.path.name, "line": self.line(pos),
            "code": code, "severity": severity, "message": message,
            "context": list(context)})

    def skip_space(self, i, end):
        while i < end and self.s[i].isspace():
            i += 1
        return i

    def group(self, i, end):
        i = self.skip_space(i, end)
        if i < end and self.s[i] == "{" and i in self.groups:
            return i, self.groups[i]
        return None

    def brackets(self, i, end):
        i = self.skip_space(i, end)
        if i >= end or self.s[i] != "[":
            return None
        start = i
        depth = 1
        i += 1
        while i < end:
            if self.s[i] == "\\":
                m = re.match(r"\\[A-Za-z@]+|\\.", self.s[i:])
                i += len(m[0]) if m else 1
                continue
            if self.s[i] == "{" and i in self.groups:
                i = self.groups[i] + 1
                continue
            if self.s[i] == "[":
                depth += 1
            elif self.s[i] == "]":
                depth -= 1
                if not depth:
                    return start, i
            i += 1
        self.add("unclosed_option", start, "Unclosed optional-argument bracket.", "error")
        return None

    def structure(self):
        stack = []
        for m in TOK.finditer(self.s):
            if m[0] == "{":
                stack.append(m.start())
            elif m[0] == "}":
                if stack:
                    self.groups[stack.pop()] = m.start()
                else:
                    self.add("brace", m.start(), "Extra closing brace.", "error")
        for pos in stack:
            self.add("brace", pos, "Unclosed opening brace.", "error")
        stack = []
        for m in ENV.finditer(self.s):
            kind, name = m.groups()
            if kind == "begin":
                stack.append(m)
            elif not stack:
                self.add("environment", m.start(), f"Unmatched end of {name}.", "error")
            else:
                op = stack.pop()
                if op[2] != name:
                    self.add("environment", m.start(), f"End {name} mismatches {op[2]}.", "error")
                self.envs[op.start()] = (op.end(), m.start(), m.end(), name)
        for m in stack:
            self.add("environment", m.start(), f"Unclosed environment {m[2]}.", "error")

    def scan(self, start, end, mode="text", context=()):
        i = start
        while i < end:
            m = TOK.search(self.s, i, end)
            if not m:
                break
            t, pos = m[0], m.start()
            i = m.end()
            if t == "{" and pos in self.groups:
                close = self.groups[pos]
                self.scan(i, close, mode, context)
                i = close + 1
            elif t in {"$", r"\[", r"\("}:
                close_token = {"$": "$", r"\[": r"\]", r"\(": r"\)"}[t]
                close = None
                for mm in TOK.finditer(self.s, i, end):
                    if mm[0] == close_token:
                        close = mm
                        break
                if close is None:
                    self.add("math_delimiter", pos, f"No closing {close_token} in this scope.", "error", context)
                    continue
                if mode == "math":
                    self.add("math_delimiter_in_math", pos,
                        f"Explicit {t} begins inside existing math; check whether a text-producing macro was intended.",
                        "hazard", context)
                self.scan(i, close.start(), "math", context + (t,))
                i = close.end()
            elif t in {r"\]", r"\)"}:
                self.add("math_delimiter", pos, f"Unexpected {t} in this scope.", "error", context)
            elif t in {"^", "_"} and mode == "text":
                self.add("script_in_text", pos, f"Raw {t} is outside recognized math mode.",
                         "conditional" if "diagram" in context else "hazard", context)
            elif t == r"\begin" and pos in self.envs:
                content, stop, finish, name = self.envs[pos]
                opt = self.brackets(content, stop)
                if opt:
                    content = opt[1] + 1
                if name in {"array", "tabular", "tabular*", "alignedat"}:
                    g = self.group(content, stop)
                    if g:
                        content = g[1] + 1
                if name in MATH_ENVS and mode != "math":
                    self.add("math_environment_in_text", pos,
                        f"{name} needs an enclosing math mode; its wrapper definition is not supplied in these fragments.",
                        "conditional" if "diagram" in context else "hazard", context)
                child_mode = "math" if name in MATH_ENVS | DISPLAY_ENVS | {"tikzcd"} else "text"
                self.scan(content, stop, child_mode, context + (name,))
                i = finish
            elif t.startswith("\\"):
                cmd = t[1:]
                if cmd in {"scanpage", "cotefile"}:
                    g = self.group(i, end)
                    if g:
                        i = g[1] + 1
                    continue
                if cmd == "arrow":
                    opt = self.brackets(i, end)
                    if opt:
                        self.check_arrow(pos, *opt)
                        # Quoted TikZ-cd labels are in math mode by default.
                        self.scan(opt[0] + 1, opt[1], "math", context + ("arrow options",))
                        i = opt[1] + 1
                    continue
                if cmd in MATH_ONLY and mode != "math":
                    self.add("math_command_in_text", pos,
                        f"{t} is outside recognized math mode.",
                        "conditional" if "diagram" in context else "hazard", context)
                if cmd in TEXT_ARGS | TRANSPARENT | {"ensuremath"}:
                    g = self.group(i, end)
                    if g:
                        a, b = g
                        if cmd in {"uline", "uuline"} and mode == "math":
                            self.ulines.append({"file": self.path.name, "line": self.line(pos),
                                "command": cmd, "argument": self.s[a+1:b], "context": list(context)})
                        child_mode = "text" if cmd in TEXT_ARGS else "math" if cmd == "ensuremath" else mode
                        self.scan(a + 1, b, child_mode, context + (cmd,))
                        i = b + 1

    def check_arrow(self, pos, a, b):
        # Split pgfkeys at top-level commas, preserving brace-protected labels.
        parts, part, depth, quoted = [], a + 1, 0, False
        for i in range(a + 1, b):
            ch = self.s[i]
            if ch == "{" and (i == 0 or self.s[i-1] != "\\"):
                depth += 1
            elif ch == "}" and (i == 0 or self.s[i-1] != "\\"):
                depth -= 1
            elif ch == '"' and depth == 0:
                quoted = not quoted
            elif ch == "," and depth == 0 and not quoted:
                parts.append(self.s[part:i].strip())
                part = i + 1
        parts.append(self.s[part:b].strip())
        direction = None
        for p in parts:
            if not p:
                continue
            if p.startswith('"'):
                if p.count('"') < 2:
                    self.add("arrow_quote", pos, "Unclosed quoted arrow label.", "error")
                continue
            if re.fullmatch(r"[udlr\s]+", p):
                direction = re.sub(r"\s+", "", p)
                # tikz-cd's undelimited-token direction parser skips spaces.
                continue
            key = p.split("=", 1)[0].strip()
            if key not in ARROW_KEYS:
                self.add("arrow_option_review", pos, f"Unrecognized by this limited allowlist: {p!r}.", "review")
        self.arrows.append({"file": self.path.name, "line": self.line(pos), "offset": pos, "options": parts,
                            "direction": direction})

    def run(self):
        self.structure()
        self.scan(0, len(self.s))
        return self


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pages", type=Path, default=Path(__file__).resolve().parents[1] / "pages")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    checks = [Checker(p).run() for p in sorted(args.pages.glob("*.tex"))]
    result = {
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "scope": "Read-only saved LaTeX fragments; no scans, images, archives, or context read.",
        "limitations": ["Static heuristics, not TeX expansion or compilation.",
            "Custom annotations preserve caller mode for analysis; unknown definitions can change behavior.",
            "No judgement of wording, mathematical correctness, or intended diagram geometry.",
            "Arrow option allowlist is deliberately limited; reviews need human verification."],
        "files": [{"name": c.path.name, "sha256": hashlib.sha256(c.raw.encode()).hexdigest(),
                   "lines": len(c.raw.splitlines())} for c in checks],
        "findings": [f for c in checks for f in c.findings],
        "underlining_in_math": [f for c in checks for f in c.ulines],
        "arrow_options": [f for c in checks for f in c.arrows],
    }
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Read {len(checks)} page files; {len(result['findings'])} conservative findings.")
    for f in result["findings"]:
        print(f"{f['file']}:{f['line']}: {f['severity']} {f['code']}: {f['message']} [{'/'.join(f['context'])}]")
    print("\nUnderlining calls in recognized math mode:")
    for f in result["underlining_in_math"]:
        print(f"{f['file']}:{f['line']}: \\{f['command']}{{{f['argument']}}}")
    print(f"\nReviewed syntax of {len(result['arrow_options'])} arrow option lists.")


if __name__ == "__main__":
    main()
