#!/usr/bin/env python3
"""Create a lexical notation/tooling report without inspecting source images.

Counts describe TeX tokens only; they make no assertion about manuscript readings.
No page fragment or context file is changed or opened outside the pages directory.
"""
from __future__ import annotations

import collections
import csv
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from mechanical_tex_check import escaped, option_text, strip_comments


ROOT = Path(__file__).resolve().parents[1]
GREEK_COMMANDS = set("alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda mu nu xi pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega".split())
ARROW_COMMANDS = set("arrow ar to gets rightarrow leftarrow leftrightarrow Rightarrow Leftarrow Leftrightarrow longrightarrow longleftarrow longleftrightarrow Longrightarrow Longleftarrow Longleftrightarrow mapsto longmapsto hookrightarrow hookleftarrow xrightarrow xleftarrow downarrow uparrow updownarrow Downarrow Uparrow Updownarrow leadsto rightsquigarrow".split())
MATH_ENVS = {"tikzcd", "aligned", "array", "gathered", "cases", "equation", "equation*", "align", "align*"}


def command_matches(source):
    return [m for m in re.finditer(r"\\([A-Za-z]+)\b", source) if not escaped(source, m.start())]


def suppress_text_groups(source):
    chars = list(source)
    for m in re.finditer(r"\\(?:text|textnormal|textit|textsf|texttt|operatorname)\*?\s*\{", source):
        if escaped(source, m.start()):
            continue
        start = m.end() - 1
        depth = 1
        i = start + 1
        while i < len(source) and depth:
            if source[i] == "{" and not escaped(source, i):
                depth += 1
            elif source[i] == "}" and not escaped(source, i):
                depth -= 1
            i += 1
        for j in range(m.start(), i):
            if chars[j] != "\n":
                chars[j] = " "
    return "".join(chars)


def math_only(source):
    source = suppress_text_groups(source)
    chars = ["\n" if c == "\n" else " " for c in source]
    delimiters = []
    environments = []
    pattern = r"\\(?:begin|end)\s*\{[^}]+\}|\\[\[\]()]|\$\$?"
    position = 0
    for m in re.finditer(pattern, source):
        if escaped(source, m.start()):
            continue
        active = bool(delimiters) or any(e in MATH_ENVS for e in environments)
        if active:
            chars[position:m.start()] = source[position:m.start()]
        token = m.group()
        env = re.fullmatch(r"\\(begin|end)\s*\{([^}]+)\}", token)
        if env:
            if env.group(1) == "begin":
                environments.append(env.group(2))
            elif environments:
                environments.pop()
        elif token in (r"\(", r"\["):
            delimiters.append(token)
        elif token in (r"\)", r"\]"):
            if delimiters:
                delimiters.pop()
        elif token in ("$", "$$"):
            if delimiters and delimiters[-1] == token:
                delimiters.pop()
            else:
                delimiters.append(token)
        position = m.end()
    if delimiters or any(e in MATH_ENVS for e in environments):
        chars[position:] = source[position:]
    return "".join(chars)


def script_count(source, marker, character):
    expression = re.escape(marker) + r"\s*(?:" + re.escape(character) + r"|\{\s*" + re.escape(character) + r"\s*\})"
    return sum(not escaped(source, m.start()) for m in re.finditer(expression, source))


def main():
    records = ROOT / "records"
    records.mkdir(exist_ok=True)
    invocation = subprocess.run([sys.executable, str(ROOT / "scripts/mechanical_tex_check.py")],
                                text=True, stdout=subprocess.PIPE, check=False)
    structure = json.loads(invocation.stdout)
    command_counts = collections.Counter()
    command_pages = collections.defaultdict(set)
    page_counts = []
    unicode_greek = []
    extra_issues = []
    for path in sorted((ROOT / "pages").glob("*.tex")):
        source = strip_comments(path.read_text(encoding="utf-8"))
        scan = int(re.search(r"scan(\d+)\.tex$", path.name).group(1))
        commands = command_matches(source)
        local = collections.Counter(m.group(1) for m in commands)
        command_counts.update(local)
        for name in local:
            command_pages[name].add(scan)
        math = math_only(source)
        prime_runs = list(re.finditer(r"'+", math))
        no_heads = 0
        draw_heads = 0
        draws_without_explicit_heads = 0
        for m in commands:
            if m.group(1) not in {"arrow", "ar", "draw"}:
                continue
            options = option_text(source, m.end()) or ""
            keys = re.sub(r'"(?:[^"\\]|\\.)*"', '""', options)
            if m.group(1) in {"arrow", "ar"} and re.search(r"(?:^|,)\s*no head\s*(?:,|$)", keys):
                no_heads += 1
            if m.group(1) == "draw":
                if "->" in keys or "<-" in keys or re.search(r"(?:^|,)\s*[<>]-?", keys):
                    draw_heads += 1
                else:
                    draws_without_explicit_heads += 1
        for m in re.finditer("[\u0370-\u03ff\u1f00-\u1fff]", source):
            unicode_greek.append({"file": path.name, "line": source.count("\n", 0, m.start()) + 1,
                                  "codepoint": f"U+{ord(m.group()):04X}"})
        stack = []
        for number, line in enumerate(source.splitlines(), 1):
            for m in re.finditer(r"\\(begin|end)\s*\{([^}]+)\}", line):
                if escaped(line, m.start()):
                    continue
                if m.group(1) == "begin":
                    stack.append(m.group(2))
                elif stack and stack[-1] == m.group(2):
                    stack.pop()
            ending = re.search(r"(\\+)\s*$", line)
            if ending and len(ending.group(1)) % 2 and any(e in {"aligned", "array", "tikzcd"} for e in stack):
                extra_issues.append({"file": f"pages/{path.name}", "line": number,
                                     "kind": "row separator", "detail": "Odd backslash count at row ending"})
        page_counts.append({
            "scan": f"{scan:03d}", "prime_marks_in_math": sum(len(m.group()) for m in prime_runs),
            "prime_runs_in_math": len(prime_runs), "prime_command": local["prime"],
            "sup_bang": script_count(source, "^", "!"), "sub_bang": script_count(source, "_", "!"),
            "sup_star": script_count(source, "^", "*"), "sub_star": script_count(source, "_", "*"),
            "overline": local["overline"], "bar": local["bar"], "widetilde": local["widetilde"],
            "tilde": local["tilde"], "mathcal": local["mathcal"], "mathfrak": local["mathfrak"],
            "mathbb": local["mathbb"], "underline": local["underline"],
            "uline": local["uline"], "uuline": local["uuline"],
            "arrow_commands_all": sum(local[name] for name in ARROW_COMMANDS),
            "tikz_arrow_commands": local["arrow"] + local["ar"], "tikz_arrow_no_head": no_heads,
            "draw_commands_with_explicit_heads": draw_heads,
            "draw_commands_without_explicit_heads": draws_without_explicit_heads,
            "greek_commands": sum(local[name] for name in GREEK_COMMANDS),
        })
    report = {
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "scope": "Lexical tooling checks only; no images or context opened; no page files edited.",
        "structure": structure, "additional_issues": extra_issues,
        "literal_greek": unicode_greek, "page_counts": page_counts,
        "commands": {name: {"count": command_counts[name], "scans": sorted(command_pages[name])}
                     for name in sorted(command_counts)},
    }
    (records / "mechanical_notation_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (records / "mechanical_notation_counts.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(page_counts[0]))
        writer.writeheader()
        writer.writerows(page_counts)
    totals = {name: sum(row[name] for row in page_counts) for name in page_counts[0] if name != "scan"}
    lines = [
        "# Mechanical notation and syntax report", "", f"Generated: {report['generated_utc']}", "",
        "Scope: lexical checks of the 48 TeX fragments only. No manuscript images or context were opened; no page file was edited.", "",
        f"Checked {structure['pages']} fragments, {structure['scanpage_markers']} scan markers, {structure['tikzcd_diagrams']} tikz-cd environments and {structure['arrows']} diagram arrow commands.", "",
        f"Structural issues: {len(structure['issues'])}; additional row-separator issues: {len(extra_issues)}; literal Unicode Greek characters: {len(unicode_greek)}.", "",
        "Brace balance, environment nesting, math delimiters, macro-name allowlist and explicit matrix arrow targets passed when the issue count is zero. This does not establish visual fidelity or mathematical correctness. Full TeX compilation was unavailable because the installed engine lacks pdflatex.fmt; it was not repeated for this report.", "",
        "## Token-count conventions", "",
        "Counts are lexical. Prime marks count apostrophes in mathematical regions, excluding text/typographic-text/operator-name groups; prime commands are listed separately. Script counts recognize direct forms such as `^!` and `^{!}`. They do not normalize compound superscripts or infer a sign hidden inside an annotation. Arrow/no-head counts distinguish explicit `no head` options; drawing counts report whether a local option explicitly supplies arrowheads, without inferring inherited TikZ styles.", "",
        "Complete page-by-page counts are in `mechanical_notation_counts.csv`; the JSON report includes command counts and the scans using each command.", "",
        "## Aggregate construction counts", "", "| Construction | Count |", "|---|---:|",
    ]
    lines.extend(f"| `{name}` | {count} |" for name, count in totals.items())
    lines.extend(["", "## Command-name inventory", "", f"{len(command_counts)} distinct alphabetic command names; all are in the technical checker's standard-math/TikZ or permitted-state macro allowlist.", "",
                  ", ".join(f"`\\{name}`" for name in sorted(command_counts)), "", "## Mechanical issues", ""])
    problems = structure["issues"] + extra_issues
    if problems:
        lines.extend(f"- `{p['file']}`, line {p['line']}: {p['kind']}: {p['detail']}" for p in problems)
    else:
        lines.append("None detected.")
    (records / "mechanical_notation_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"reports": ["records/mechanical_notation_report.md", "records/mechanical_notation_report.json", "records/mechanical_notation_counts.csv"],
                      "issues": problems, "literal_greek": unicode_greek,
                      "distinct_commands": len(command_counts)}, indent=2))


if __name__ == "__main__":
    main()
