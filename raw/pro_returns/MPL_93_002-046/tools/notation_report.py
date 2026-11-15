#!/usr/bin/env python3
"""Produce a mechanical notation report; no image access or reading decisions."""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
import importlib.util
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "MPL_93_002-046"
EXPECTED = {n for n in range(3, 47) if n not in {26, 35}}
spec = importlib.util.spec_from_file_location("validator", ROOT / "tools/validate_package.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def positions(items):
    return "; ".join(f"{scan:03d}:{','.join(map(str, sorted(set(lines))))}"
                     for scan, lines in sorted(items.items())) or "—"


def count_table(title, variants, occurrences):
    out = [f"## {title}", "", "| Literal spelling | Occurrences | Scan:line |",
           "|---|---:|---|"]
    for token in variants:
        found = occurrences.get(token, {})
        count = sum(map(len, found.values()))
        literal = "``` " + token + " ```" if "`" in token else "`" + token + "`"
        out.append(f"| {literal} | {count} | {positions(found)} |")
    return out + [""]


def main():
    command_occurrences = defaultdict(lambda: defaultdict(list))
    spelling_occurrences = defaultdict(lambda: defaultdict(list))
    alphabet_occurrences = defaultdict(lambda: defaultdict(list))
    math_apostrophes = defaultdict(list)
    math_envs = set("math displaymath equation equation* align align* aligned alignedat gather gather* gathered multline multline* flalign flalign* split cases matrix pmatrix bmatrix Bmatrix vmatrix Vmatrix smallmatrix array tikzcd".split())
    for file in sorted((ROOT / "pages").glob("*.tex")):
        scan = int(re.search(r"scan(\d+)\.tex$", file.name)[1])
        text = validator.no_comments(file.read_text(encoding="utf-8"))
        for match in re.finditer(r"\\([A-Za-z@]+|[^A-Za-z@])", text):
            if re.fullmatch(r"[A-Za-z@]+", match[1]):
                command_occurrences["\\" + match[1]][scan].append(text.count("\n", 0, match.start()) + 1)
        for match in re.finditer(r"\\(mathcal|mathscr|mathbb|mathfrak|mathbf|mathit|mathrm|mathsf|mathtt|mathnormal|boldsymbol|bm)\s*\{([^{}]*)\}", text):
            argument = match[2].strip()
            # Preserve notation tokens only, without excerpts from prose.
            if len(argument) <= 40:
                key = "\\" + match[1] + "{" + argument + "}"
                alphabet_occurrences[key][scan].append(text.count("\n", 0, match.start()) + 1)
        patterns = {
            "^!": r"\^!",
            "^{!}": r"\^\{\s*!\s*\}",
            "^\\prime": r"\^\\prime\b",
            "^{\\prime}": r"\^\{\s*\\prime\s*\}",
            "^{\\prime\\prime}": r"\^\{\s*\\prime\s*\\prime\s*\}",
            "``": r"``",
            "''": r"''",
            "«": "«", "»": "»",
        }
        for key, pattern in patterns.items():
            for match in re.finditer(pattern, text):
                spelling_occurrences[key][scan].append(text.count("\n", 0, match.start()) + 1)
        # A deliberately lexical classification: math delimiters/environments
        # are tracked, but textual macro arguments inside math are not inferred.
        inline_dollar = False
        explicit_depth = 0
        env_stack = []
        token_re = re.compile(r"\\(?:begin|end)\s*\{[^}]+\}|\\[()\[\]]|\\(?:[A-Za-z@]+|.)|\$\$?|'+", re.S)
        for match in token_re.finditer(text):
            token = match[0]
            if token.startswith("\\begin"):
                env_stack.append(re.search(r"\{([^}]+)\}", token)[1])
            elif token.startswith("\\end"):
                if env_stack:
                    env_stack.pop()
            elif token in {"\\(", "\\["}:
                explicit_depth += 1
            elif token in {"\\)", "\\]"}:
                explicit_depth = max(0, explicit_depth - 1)
            elif token in {"$", "$$"}:
                inline_dollar = not inline_dollar
            elif token.startswith("'") and (inline_dollar or explicit_depth or any(e in math_envs for e in env_stack)):
                math_apostrophes[(scan, len(token))].append(text.count("\n", 0, match.start()) + 1)
    log = (ROOT / "progress.log").read_text(encoding="utf-8")
    done = [int(x) for x in re.findall(r"^93 scan (\d+) done ", log, re.M)]
    audited = [int(x) for x in re.findall(r"^scan (\d+) audited ", log, re.M)]
    out = ["# Mechanical notation and completion report", "",
           "Generated " + datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC") + ".", "",
           "This report extracts literal LaTeX syntax and log markers only. It does not inspect scans, compare glyphs, infer readings, or certify diplomatic accuracy. Line numbers refer to page `.tex` files, not manuscript lines.", "",
           "## Completion markers", "",
           f"- Expected scans: {', '.join(f'{n:03d}' for n in sorted(EXPECTED))}.",
           f"- Done markers: {len(done)} entries, {len(set(done))} distinct; missing={sorted(EXPECTED-set(done))}; unexpected={sorted(set(done)-EXPECTED)}; duplicates={dict((n,c) for n,c in Counter(done).items() if c>1)}.",
           f"- Audited markers: {len(audited)} entries, {len(set(audited))} distinct; missing={sorted(EXPECTED-set(audited))}; unexpected={sorted(set(audited)-EXPECTED)}; duplicates={dict((n,c) for n,c in Counter(audited).items() if c>1)}.", ""]
    out += count_table("Greek letter variants", ["\\phi", "\\varphi", "\\Phi", "\\rho", "\\varrho", "\\epsilon", "\\varepsilon", "\\theta", "\\vartheta"], command_occurrences)
    alphabet_commands = ["\\mathcal", "\\mathscr", "\\mathbb", "\\mathfrak", "\\mathbf", "\\mathit", "\\mathrm", "\\mathsf", "\\mathtt", "\\mathnormal", "\\boldsymbol", "\\bm"]
    # Command totals are concise; per-argument spellings below allow comparison.
    out += ["## Math alphabets", "", "| Command | Occurrences | Scans |", "|---|---:|---|"]
    for command in alphabet_commands:
        occurrences = command_occurrences.get(command, {})
        out.append(f"| `{command}` | {sum(map(len, occurrences.values()))} | {', '.join(f'{n:03d}' for n in sorted(occurrences)) or '—'} |")
    out += ["", "### Repeated or script-alphabet arguments", "", "| Literal spelling | Occurrences | Scans |", "|---|---:|---|"]
    for spelling, occurrences in sorted(alphabet_occurrences.items()):
        count = sum(map(len, occurrences.values()))
        if count > 1 or spelling.startswith(("\\mathcal", "\\mathscr", "\\mathbb", "\\mathfrak")):
            escaped = spelling.replace("|", "\\|")
            out.append(f"| `{escaped}` | {count} | {', '.join(f'{n:03d}' for n in sorted(occurrences))} |")
    out += [""]
    out += count_table("Explicit prime and exclamation exponent syntax", ["^!", "^{!}", "^\\prime", "^{\\prime}", "^{\\prime\\prime}"], spelling_occurrences)
    out += count_table("Prime command", ["\\prime", "\\backprime"], command_occurrences)
    out += ["### Apostrophe runs in lexical math spans", "",
            "These counts are candidates for prime notation, not reading decisions. Textual macro arguments within a math span may also contain apostrophes.", "",
            "| Scan | Apostrophes per run | Number of runs | Lines |", "|---|---:|---:|---|"]
    for (scan, length), lines in sorted(math_apostrophes.items()):
        out.append(f"| {scan:03d} | {length} | {len(lines)} | {', '.join(map(str,sorted(set(lines))))} |")
    out += [""]
    out += count_table("Quotation markup", ["``", "''", "«", "»"], spelling_occurrences)
    out += count_table("Quotation commands", ["\\og", "\\fg", "\\guillemotleft", "\\guillemotright", "\\textquotedblleft", "\\textquotedblright"], command_occurrences)
    out += ["Doubled apostrophes above are literal token counts and include any doubled primes; unequal opening/closing totals alone do not establish a quotation error.", ""]
    out += count_table("Relation and arrow spellings", ["\\le", "\\leq", "\\leqq", "\\ge", "\\geq", "\\geqq", "\\ne", "\\neq", "\\to", "\\rightarrow", "\\longrightarrow", "\\mapsto", "\\longmapsto", "\\subset", "\\subseteq", "\\simeq", "\\cong"], command_occurrences)
    run = subprocess.run([sys.executable, str(ROOT / "tools/validate_package.py"), "--partial"], capture_output=True, text=True)
    out += ["## Structural validator", "", "```text", run.stdout.rstrip(), "```", ""]
    target = ROOT / f"{PREFIX}_mechanical_notation_report.md"
    target.write_text("\n".join(out), encoding="utf-8")
    print(target)
    print(f"Done: {len(set(done))}/42; audited: {len(set(audited))}/42; validator exit: {run.returncode}")
    print("Greek counts:", "; ".join(f"{key}={sum(map(len,command_occurrences.get(key,{}).values()))}" for key in ["\\phi","\\varphi","\\rho","\\varrho"]))
    print("Exclamation exponents:", sum(map(len,spelling_occurrences.get("^!",{}).values())) + sum(map(len,spelling_occurrences.get("^{!}",{}).values())))
    return run.returncode


if __name__ == "__main__":
    raise SystemExit(main())
