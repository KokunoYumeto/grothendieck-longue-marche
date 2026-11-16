#!/usr/bin/env python3
"""Read-only lexical review; never reads images, context, or prose notes.

Only structural metadata, delimiter tokens, macro names, and byte equality
are examined. No mathematical or palaeographical interpretation is made.
"""
from __future__ import annotations

import argparse
import collections
import csv
import datetime
import hashlib
import io
import json
import re
from pathlib import Path

PREFIX = "MPL_90+91_002-018"
EXPECTED = [(90, n) for n in range(2, 26)] + [(91, n) for n in range(2, 19) if n not in (4, 15)]
EDITORIAL = set("cotefile scanpage mspage deleted inserted margin uline uuline diagram figure unsure illegible".split())
STANDARD = set("""Delta Gamma Leftrightarrow Omega Rightarrow S alpha bar begin beta bigcap
bigcup bullet cap cdot check circ coprod delta dim end eta exists forall frac geq hat
hookrightarrow in kappa lambda ldots left leftarrow leq longrightarrow mapsto mathcal
mathrm mu ne operatorname otimes pi prime prod psi qquad quad right rightsquigarrow
sim simeq subset sum supset text textsuperscript tilde times to underline varepsilon
varinjlim varnothing varphi varprojlim wedge widehat widetilde xrightarrow""".split())
TIKZ = {"arrow", "draw", "fill", "node"}
CONTROL_SYMBOLS = set("\\,;!:|{}[]()%&$#_^~ /'\"`=.-+<>" )


def escaped(text: str, index: int) -> bool:
    count = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        count += 1
        index -= 1
    return bool(count % 2)


def clean_comments(text: str) -> str:
    output = list(text)
    comment = False
    for index, char in enumerate(text):
        if char == "\n":
            comment = False
        elif comment:
            output[index] = " "
        elif char == "%" and not escaped(text, index):
            output[index] = " "
            comment = True
    return "".join(output)


def line(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def braced_end(text: str, index: int) -> int | None:
    if index >= len(text) or text[index] != "{":
        return None
    depth = 1
    for end in range(index + 1, len(text)):
        if not escaped(text, end):
            if text[end] == "{":
                depth += 1
            elif text[end] == "}":
                depth -= 1
        if depth == 0:
            return end
    return None


def math_errors(text: str, offset: int = 0) -> list[tuple[int, str]]:
    """Check explicit delimiters, separating explicit text-macro arguments."""
    errors: list[tuple[int, str]] = []
    chars = list(text)
    cursor = 0
    for match in re.finditer(r"\\(?:text|mbox|hbox|textsuperscript)\b\s*\{", text):
        if match.start() < cursor:
            continue
        begin = match.end() - 1
        end = braced_end(text, begin)
        if end is None:
            continue
        errors.extend(math_errors(text[begin + 1:end], offset + begin + 1))
        for index in range(begin + 1, end):
            if chars[index] != "\n":
                chars[index] = " "
        cursor = end + 1
    scan = "".join(chars)
    current: tuple[str, int] | None = None
    tokens = re.finditer(r"\\[A-Za-z]+|\\[^A-Za-z]|\$\$|\$", scan)
    for match in tokens:
        token = match.group()
        if token not in ("$", "$$", r"\(", r"\)", r"\[", r"\]"):
            continue
        pos = offset + match.start()
        if token in (r"\)", r"\]"):
            expected = r"\(" if token == r"\)" else r"\["
            if current is None or current[0] != expected:
                errors.append((pos, f"closing math delimiter {token!r} lacks matching opening delimiter"))
            else:
                current = None
        elif token in (r"\(", r"\["):
            if current is not None:
                errors.append((pos, f"math delimiter {token!r} opens while {current[0]!r} is active"))
            else:
                current = (token, pos)
        elif current is None:
            current = (token, pos)
        elif current[0] == token:
            current = None
        else:
            errors.append((pos, f"math delimiter {token!r} conflicts with active {current[0]!r}"))
    if current:
        errors.append((current[1], f"unclosed explicit math delimiter {current[0]!r}"))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    errors: list[str] = []
    risks: list[str] = []
    facts: list[str] = []
    snapshot: dict[Path, bytes] = {}

    def read(path: Path) -> str:
        raw = path.read_bytes()
        snapshot[path] = raw
        return raw.decode("utf-8-sig")

    inventory_path = root / f"{PREFIX}_inventory.csv"
    rows = list(csv.DictReader(io.StringIO(read(inventory_path))))
    by_page: dict[tuple[int, int], list[dict[str, str]]] = collections.defaultdict(list)
    full_rows: dict[tuple[str, ...], int] = {}
    grouped_keys = []
    for row_number, row in enumerate(rows, 2):
        key = int(row["cote"]), int(row["scan"])
        if not grouped_keys or grouped_keys[-1] != key:
            grouped_keys.append(key)
        by_page[key].append(row)
        full_key = tuple(row.values())
        if full_key in full_rows:
            errors.append(f"Inventory row {row_number}: duplicate full row of row {full_rows[full_key]}.")
        full_rows[full_key] = row_number
        for match in re.finditer(r"\b(?:lines?|ll?\.)\s*(\d+)\s*[-–—]\s*(\d+)", row["position"], re.I):
            if int(match.group(1)) > int(match.group(2)):
                risks.append(f"Inventory row {row_number}: descending numerical line-range label.")
    if grouped_keys != EXPECTED:
        errors.append("Inventory page groups are not in the exact required 39-page order.")

    macro_counts: collections.Counter[str] = collections.Counter()
    environment_counts: collections.Counter[str] = collections.Counter()
    audited = 0
    for cote, scan in EXPECTED:
        stem = f"{PREFIX}_{cote}_scan{scan:03d}"
        json_path = root / "records" / (stem + ".json")
        tex_path = root / "pages" / (stem + ".tex")
        record = json.loads(read(json_path))
        if (record.get("cote"), record.get("scan")) != (cote, scan):
            errors.append(f"{json_path.name}: cote/scan metadata differs from filename.")
        elements = record.get("elements", [])
        group = by_page[(cote, scan)]
        expected_ids = [f"E{n:02d}" for n in range(1, len(group) + 1)]
        if [row["element"] for row in group] != expected_ids:
            errors.append(f"{stem}: inventory element labels are not consecutive E01…En in row order.")
        if len(elements) != len(group):
            errors.append(f"{stem}: JSON/inventory element counts differ.")
        seen = {}
        for index, (element, row) in enumerate(zip(elements, group), 1):
            expected = [row["kind"], row["position"], row["first_words_or_objects"]]
            if element != expected:
                errors.append(f"{stem} E{index:02d}: JSON element differs from inventory fields.")
            if record.get("sheet_kind") != row["sheet_kind"]:
                errors.append(f"{stem} E{index:02d}: sheet_kind differs between JSON and inventory.")
            content_key = tuple(expected)
            if content_key in seen:
                risks.append(f"{stem}: elements E{seen[content_key]:02d} and E{index:02d} have identical kind/position/anchor fields.")
            seen[content_key] = index
        if "audited_utc" in record:
            audited += 1
            try:
                completed = datetime.datetime.strptime(record["completed_utc"], "%Y-%m-%d %H:%M:%S UTC")
                audit = datetime.datetime.strptime(record["audited_utc"], "%Y-%m-%d %H:%M:%S UTC")
                if audit < completed:
                    errors.append(f"{json_path.name}: audit timestamp precedes completion timestamp.")
            except (ValueError, KeyError):
                risks.append(f"{json_path.name}: completion/audit timestamp could not be mechanically compared.")

        clean = clean_comments(read(tex_path))
        for offset, message in math_errors(clean):
            risks.append(f"{tex_path.name}:{line(clean, offset)}: {message}.")
        env_stack: list[tuple[str, int]] = []
        for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", clean):
            action, environment = match.groups()
            if action == "begin":
                env_stack.append((environment, match.start()))
                environment_counts[environment] += 1
            elif not env_stack or env_stack[-1][0] != environment:
                errors.append(f"{tex_path.name}:{line(clean, match.start())}: mismatched environment end {environment!r}.")
            else:
                env_stack.pop()
        for environment, offset in env_stack:
            errors.append(f"{tex_path.name}:{line(clean, offset)}: unclosed environment {environment!r}.")
        left_right: list[int] = []
        for match in re.finditer(r"\\(left|right)\b", clean):
            if match.group(1) == "left":
                left_right.append(match.start())
            elif left_right:
                left_right.pop()
            else:
                errors.append(f"{tex_path.name}:{line(clean, match.start())}: right delimiter without left delimiter.")
        for offset in left_right:
            errors.append(f"{tex_path.name}:{line(clean, offset)}: left delimiter without right delimiter.")
        for match in re.finditer(r"\\([A-Za-z]+)|\\([^A-Za-z])", clean):
            command, symbol = match.groups()
            if symbol is not None:
                if not symbol.isspace() and symbol not in CONTROL_SYMBOLS:
                    risks.append(f"{tex_path.name}:{line(clean, match.start())}: unlisted control symbol {symbol!r}.")
                continue
            macro_counts[command] += 1
            if command not in EDITORIAL | STANDARD | TIKZ:
                risks.append(f"{tex_path.name}:{line(clean, match.start())}: macro \\{command} outside the explicit known allowlist.")
            if command in EDITORIAL:
                index = match.end()
                while index < len(clean) and clean[index].isspace():
                    index += 1
                if index >= len(clean) or clean[index] != "{":
                    risks.append(f"{tex_path.name}:{line(clean, match.start())}: editorial macro \\{command} uses an unbraced argument; confirm its single-token scope.")
                elif braced_end(clean, index) is None:
                    errors.append(f"{tex_path.name}:{line(clean, match.start())}: editorial macro \\{command} has an unclosed braced argument.")

    changed = [path.relative_to(root).as_posix() for path, raw in snapshot.items() if path.read_bytes() != raw]
    if changed:
        risks.append("Inputs changed during this review; rerun for a stable snapshot: " + ", ".join(changed))
    facts.extend([
        f"Pages/JSON page records checked: {len(EXPECTED)}/{len(EXPECTED)}.",
        f"Inventory rows: {len(rows)}; page groups: {len(grouped_keys)}.",
        f"Page records carrying audit timestamps at review time: {audited}/39.",
        f"Distinct macro names: {len(macro_counts)}; environment counts: {dict(sorted(environment_counts.items()))}.",
        f"Snapshot stable throughout mechanical review: {'no' if changed else 'yes'}.",
    ])
    output = ["MECHANICAL REVIEW " + datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")]
    output += ["INFO: " + value for value in facts]
    output += ["ERROR: " + value for value in errors]
    output += ["RISK: " + value for value in risks]
    output += [f"RESULT: {len(errors)} structural errors; {len(risks)} lexical/advisory risks."]
    output += ["LIMIT: This is not TeX compilation or a review of readings, mathematical content, inventory completeness against scans, or physical page order."]
    output += ["Snapshot SHA-256:"]
    output += [hashlib.sha256(raw).hexdigest() + "  " + path.relative_to(root).as_posix()
               for path, raw in sorted(snapshot.items())]
    report = "\n".join(output) + "\n"
    if args.report:
        args.report.write_text(report, encoding="utf-8")
    print("\n".join(output[:len(output) - len(snapshot) - 1]))
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
