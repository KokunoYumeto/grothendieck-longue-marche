#!/usr/bin/env python3
"""Inventory exact TeX tokens without inspecting images or judging readings."""
from __future__ import annotations

import re
import sys
import unicodedata
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from package_tools import uncomment

STATE = set("cotefile scanpage mspage deleted inserted margin uline uuline diagram figure unsure illegible".split())
DEPENDENCIES = {
    "amsmath": set("boxed operatorname overset substack text underset xrightarrow".split()),
    "amsfonts/amssymb": set("mathbb mathfrak".split()),
    "tikz-cd/TikZ": set("arrow draw node".split()),
    "mathtools": set("underbracket overbracket".split()),
}
CORE = set("""Big Gamma Lambda Longleftrightarrow Longrightarrow Phi Psi Rightarrow Theta Vert
alpha amalg bar begin beta big bigl bigotimes bigr cap cdot chi circ delta downarrow end equiv
eta exists flat forall frac gamma hookrightarrow hspace in lambda langle ldots left longleftarrow
longleftrightarrow longmapsto longrightarrow mapsto mathbin mathcal mathrel mathrm mid middle mu
natural ne newline nu omega oplus otimes overbrace overline phantom pi prime psi qquad quad rangle
rho right sigma sim simeq subset sum tau textcircled textstyle times underbrace underline uparrow
varepsilon varphi varpi vee wedge widetilde wr xi zeta""".split())
QUOTE_CHARS = set("«»‘’‚‛“”„‟‹›ʼ′″")
EXCLAMATION = re.compile(r"\^(?:!|\{\s*!\s*\})")
HOM_PRIME = re.compile(r"(?:\\(?:operatorname|mathrm|mathsf|text)\{\s*Hom\s*\}|Hom)\s*(?:'|\^(?:\\prime|\{\s*\\prime\s*\}))")
BRACKET_PRIME = re.compile(r"\](?:\s*\})*\s*(?:'|\^(?:\\prime|\{\s*\\prime\s*\}))")


def is_nonascii_quote(char: str) -> bool:
    return ord(char) > 127 and (
        char in QUOTE_CHARS
        or unicodedata.category(char) in {"Pi", "Pf"}
        or any(word in unicodedata.name(char, "") for word in ("QUOTATION", "APOSTROPHE", "PRIME"))
    )


def tokens(text: str):
    text = uncomment(text)
    index = 0
    while index < len(text):
        if text[index] == "\\" and index + 1 < len(text):
            end = index + 1
            if text[end].isalpha():
                while end < len(text) and text[end].isalpha():
                    end += 1
                yield text[index + 1:end], text[:index].count("\n") + 1
            else:
                end += 1
            index = end
        else:
            index += 1


def main() -> None:
    paths = sorted((ROOT / "pages").glob("*.tex"))
    groups = {name: [] for name in ("Exclamation exponents", "Primes on Hom", "Primes after square brackets", "All Hom token lines", "Non-ASCII quotation marks", "Literal double quotes")}
    commands = defaultdict(list)
    counts = defaultdict(int)
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for command, line in tokens(text):
            commands[command].append((path.name, line))
        for number, line in enumerate(text.splitlines(), 1):
            record = (path.name, number, line)
            for title, pattern in (("Exclamation exponents", EXCLAMATION), ("Primes on Hom", HOM_PRIME), ("Primes after square brackets", BRACKET_PRIME)):
                matches = list(pattern.finditer(line))
                if matches:
                    groups[title].append(record)
                    counts[title] += len(matches)
            if "Hom" in line:
                groups["All Hom token lines"].append(record)
            if any(is_nonascii_quote(char) for char in line):
                groups["Non-ASCII quotation marks"].append(record)
                counts["Non-ASCII quotation marks"] += sum(is_nonascii_quote(char) for char in line)
            if '"' in line:
                groups["Literal double quotes"].append(record)
                counts["Literal double quotes"] += line.count('"')
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    output = ["# Mechanical notation-token inventory", "", f"Created: {stamp}. Page files examined: {len(paths)}.", "", "This is a source-token snapshot during the principal agent's visual audit. It does not decide whether any sign is correct, does not inspect an image or context, and does not freeze or change any transcription. Snippets reproduce complete source lines exactly. Line numbers may change during later audits.", "", "## Counts", "", "| Category | Matching lines | Matching tokens / characters |", "|---|---:|---:|"]
    for title, entries in groups.items():
        output.append(f"| {title} | {len(entries)} | {counts[title] if title in counts else '—'} |")
    quote_arrow = sum("\\arrow" in line for _, _, line in groups["Literal double quotes"])
    output.extend(["", f"{quote_arrow} of {len(groups['Literal double quotes'])} literal-double-quote lines contain a `\\arrow` command. This is a lexical observation; the snippets below preserve the complete lines for review.", "", "## Command classification", "", "The allowed editorial-state macro set is treated separately from core LaTeX and named package dependencies. Package commands below are not undefined if their listed packages are loaded. `\\uline` and `\\uuline` are allowed state macros; the optional harness supplies them through `ulem`. The allowed `\\figure` command requires overriding LaTeX's existing command in that harness.", "", "| Dependency | Commands currently present |", "|---|---|"])
    for dependency, members in DEPENDENCIES.items():
        present = sorted(members & commands.keys())
        output.append("| " + dependency + " | " + (", ".join("`\\" + name + "`" for name in present) if present else "None") + " |")
    classified = CORE | STATE | set().union(*DEPENDENCIES.values())
    unclassified = sorted(commands.keys() - classified)
    output.extend(["", "Unclassified named commands: " + (", ".join("`\\" + name + "`" for name in unclassified) if unclassified else "none."), "", "All named commands were tokenized with escaped backslashes respected; the second backslash of a row break is not mistaken for a new command.", ""])
    for command in unclassified:
        output.append("- `\\" + command + "`: " + "; ".join(f"{name}:{line}" for name, line in commands[command]))
    for title, entries in groups.items():
        output.extend(["", "## " + title, ""])
        if not entries:
            output.append("No matches.")
        for name, line_number, line in entries:
            output.extend([f"### {name}, line {line_number}", "", "```latex", line, "```", ""])
    destination = ROOT / "scripts/mechanical_qa/notation_token_inventory.md"
    destination.write_text("\n".join(output) + "\n", encoding="utf-8")
    print(destination)
    print(f"Files: {len(paths)}; exclamation exponents: {counts['Exclamation exponents']}; Hom-prime tokens: {counts['Primes on Hom']}; bracket-prime tokens: {counts['Primes after square brackets']}; non-ASCII quote characters: {counts['Non-ASCII quotation marks']}; literal double quotes: {counts['Literal double quotes']}")
    print("Unclassified named commands: " + (", ".join(unclassified) if unclassified else "none"))
    print("mathtools bracket commands currently present: " + ", ".join(sorted(DEPENDENCIES['mathtools'] & commands.keys())))


if __name__ == "__main__":
    main()
