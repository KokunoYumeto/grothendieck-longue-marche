#!/usr/bin/env python3
"""Mechanical inventory normalization and TeX concordances; no scan/context access.

Writes only under records/. Never overwrites the original inventory or a page.
Abbreviation entries are lexical candidates, including ordinary sentence endings.
No abbreviation meaning, reading, or mathematical equivalence is assigned.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import json
from pathlib import Path
import re

PREFIX = "MPL_12_051-098"
ALPHABETS = {"mathbb", "mathcal", "mathfrak", "mathbf", "mathrm", "mathit", "mathsf", "mathtt", "mathnormal", "boldsymbol", "mathscr", "operatorname"}
LETTERS = set("alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa varkappa lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega ell wp Re Im".split())


def compact(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def escaped(text: str, index: int) -> bool:
    n = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        n += 1
        index -= 1
    return bool(n % 2)


def mask_comments(text: str) -> str:
    chars = list(text)
    i = 0
    while i < len(chars):
        if chars[i] == "%" and not escaped(text, i):
            while i < len(chars) and chars[i] != "\n":
                chars[i] = " "
                i += 1
        i += 1
    return "".join(chars)


def argument(text: str, start: int) -> tuple[str, str, int] | None:
    i = start
    while i < len(text) and text[i].isspace():
        i += 1
    if i == len(text):
        return None
    if text[i] == "{":
        depth = 1
        j = i + 1
        while j < len(text):
            if not escaped(text, j):
                if text[j] == "{":
                    depth += 1
                elif text[j] == "}":
                    depth -= 1
                    if depth == 0:
                        return text[i + 1:j], text[i:j + 1], j + 1
            j += 1
        return None
    if text[i] == "\\":
        match = re.match(r"\\(?:[A-Za-z]+|.)", text[i:], flags=re.S)
        if match:
            return match.group(0), match.group(0), i + len(match.group(0))
    return text[i], text[i], i + 1


def write_csv(path: Path, columns: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def normalize_inventory(base: Path) -> dict:
    source = base / f"{PREFIX}_inventory.csv"
    target = base / "records" / f"{PREFIX}_inventory_normalized_original.csv"
    with source.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = list(reader.fieldnames or [])
        original = list(reader)
    rows = [dict(row) for row in original]
    changes = []
    for line, row in enumerate(rows, 2):
        if row["kind"] in {"title", "formula"}:
            old = row["kind"]
            row["kind"] = {"title": "text", "formula": "display"}[old]
            changes.append({"csv_line": line, "scan": row["scan"], "column": "kind", "old": old, "new": row["kind"]})
        if int(row["scan"]) == 96 and row["sheet_kind"] == "title_only":
            row["sheet_kind"] = "cover"
            changes.append({"csv_line": line, "scan": row["scan"], "column": "sheet_kind", "old": "title_only", "new": "cover"})
    for before, after in zip(original, rows):
        for key in columns:
            if key not in {"kind", "sheet_kind"}:
                assert before[key] == after[key], (key, before, after)
    assert len(original) == len(rows)
    exact = defaultdict(list)
    prefixes = defaultdict(list)
    source_only = []
    for line, row in enumerate(rows, 2):
        value = compact(row["first_words_or_objects"])
        exact[(row["scan"], row["kind"], value)].append({"csv_line": line, "element": row["element"]})
        prefixes[(row["scan"], row["kind"], value[:64])].append({"csv_line": line, "element": row["element"], "full_field": value})
        position = compact(row["position"])
        if re.fullmatch(r"(?:within page\s*;?\s*)?(?:TeX|source)\s+lines?\b.*", position, flags=re.I):
            source_only.append({"csv_line": line, "scan": row["scan"], "element": row["element"], "kind": row["kind"], "position": row["position"]})
    duplicate_exact = [{"scan": key[0], "kind": key[1], "prefix": key[2], "rows": values} for key, values in exact.items() if len(values) > 1]
    duplicate_prefix = [{"scan": key[0], "kind": key[1], "prefix_64_chars": key[2], "rows": values} for key, values in prefixes.items() if len(values) > 1 and len({row['full_field'] for row in values}) > 1]
    write_csv(target, columns, rows)
    report = {
        "source": str(source), "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "candidate": str(target), "row_count": len(rows), "changed_cells": changes,
        "all_original_rows_preserved": True, "original_order_preserved": True,
        "positions_and_prefix_fields_unchanged": True,
        "duplicate_exact_field_groups": duplicate_exact,
        "duplicate_64_character_prefix_groups": duplicate_prefix,
        "source_line_only_rows": source_only,
        "source_line_only_counts_by_scan": dict(Counter(row["scan"] for row in source_only)),
        "source_line_only_count": len(source_only),
        "limitation": "Duplicate groups are lexical candidates only; no semantic identity or deletion is inferred. Source-line-only classification does not establish the rows' generation history.",
    }
    (base / "records" / "normalized_original_inventory_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    return report


def concordance(base: Path) -> dict:
    abbreviations = defaultdict(list)
    alphabet = defaultdict(list)
    letters = defaultdict(list)
    hashes = {}
    # Unicode-letter tokens ending in a literal dot, length bounded only to make
    # the lexical candidate list useful. This intentionally does not decide which
    # occurrences are actual abbreviations rather than sentence-final words.
    token_pattern = re.compile(r"(?<![\w\\])(?:[^\W\d_]{1,12}\.)+(?![^\W\d_])", flags=re.UNICODE)
    multi_pattern = re.compile(r"(?<![\w\\])(?:[^\W\d_]{1,4}\.\s+){1,3}[^\W\d_]{1,4}\.(?![^\W\d_])", flags=re.UNICODE)
    for page in sorted((base / "pages").glob(f"{PREFIX}_12_scan*.tex")):
        scan = int(re.search(r"scan(\d{3})\.tex$", page.name).group(1))
        raw = page.read_text(encoding="utf-8")
        text = mask_comments(raw)
        hashes[page.name] = hashlib.sha256(page.read_bytes()).hexdigest()
        found = set()
        for pattern, category in ((token_pattern, "dot-terminated token"), (multi_pattern, "spaced dot sequence"), (re.compile(r"(?<!\w)[Nn]°"), "number-sign token")):
            for match in pattern.finditer(text):
                value = match.group(0)
                key = (match.start(), value)
                if key in found:
                    continue
                found.add(key)
                abbreviations[value].append({"scan": scan, "line": text.count("\n", 0, match.start()) + 1, "offset": match.start(), "category": category})
        for match in re.finditer(r"\\([A-Za-z]+)(\*?)", text):
            if escaped(text, match.start()):
                continue
            name = match.group(1)
            occurrence = {"scan": scan, "line": text.count("\n", 0, match.start()) + 1, "offset": match.start()}
            if name in ALPHABETS:
                arg = argument(text, match.end())
                if arg:
                    content, syntax, end = arg
                    alphabet[(name + match.group(2), content)].append({**occurrence, "exact_tex": text[match.start():end], "argument_syntax": syntax})
            if name in LETTERS:
                letters["\\" + name].append(occurrence)

    def scan_list(values: list[dict]) -> str:
        return ",".join(f"{n:03d}" for n in sorted({row["scan"] for row in values}))

    def references(values: list[dict]) -> str:
        return "; ".join(f"{row['scan']:03d}:L{row['line']}" for row in values)

    abbreviation_rows = [{"string": key, "count": len(values), "scans": scan_list(values), "source_locations": references(values), "status": "lexical candidate; meaning and abbreviation status not interpreted"} for key, values in sorted(abbreviations.items(), key=lambda item: (-len(item[1]), item[0]))]
    alphabet_rows = [{"macro": "\\" + key[0], "argument": key[1], "count": len(values), "scans": scan_list(values), "source_locations": references(values)} for key, values in sorted(alphabet.items(), key=lambda item: (item[0][0], -len(item[1]), item[0][1]))]
    letter_rows = [{"command": key, "count": len(values), "scans": scan_list(values), "source_locations": references(values)} for key, values in sorted(letters.items(), key=lambda item: (-len(item[1]), item[0]))]
    records = base / "records"
    write_csv(records / "abbreviation_concordance.csv", ["string", "count", "scans", "source_locations", "status"], abbreviation_rows)
    write_csv(records / "math_alphabet_concordance.csv", ["macro", "argument", "count", "scans", "source_locations"], alphabet_rows)
    write_csv(records / "math_letter_command_concordance.csv", ["command", "count", "scans", "source_locations"], letter_rows)
    details = {
        "method": "Literal mechanical extraction from comment-masked TeX; no image/context access or interpretation of meanings.",
        "source_sha256": hashes,
        "abbreviation_candidates": [{"string": key, "occurrences": values} for key, values in sorted(abbreviations.items())],
        "alphabet_macros": [{"macro": "\\" + key[0], "argument": key[1], "occurrences": values} for key, values in sorted(alphabet.items())],
        "letter_commands": [{"command": key, "occurrences": values} for key, values in sorted(letters.items())],
        "limitations": ["Dot-terminated tokens include sentence-final words and other false candidates.", "Single and spaced multi-token candidates may overlap and are not additive counts.", "TeX source lines are not physical manuscript line numbers.", "Identical macro spelling is counted literally; no equivalence between alphabets, letters or readings is inferred.", "Occurrences in deleted, inserted, doubtful and marginal content are retained together and remain locatable in the source."],
    }
    (records / "mechanical_notation_concordance.json").write_text(json.dumps(details, ensure_ascii=False, indent=2) + "\n")
    summary = {
        "pages": len(hashes), "distinct_abbreviation_candidates": len(abbreviation_rows),
        "distinct_alphabet_macro_arguments": len(alphabet_rows),
        "recurring_alphabet_macro_arguments": sum(row["count"] > 1 for row in alphabet_rows),
        "distinct_letter_commands": len(letter_rows),
        "alphabet_macro_total_counts": dict(Counter({"\\" + name: sum(len(values) for (macro, _), values in alphabet.items() if macro == name) for name in sorted({key[0] for key in alphabet})})),
        "most_frequent_dot_candidates": abbreviation_rows[:30],
    }
    (records / "mechanical_concordance_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    base = args.base.resolve()
    normalized = normalize_inventory(base)
    summary = concordance(base)
    print(json.dumps({
        "normalized_inventory": normalized["candidate"], "rows": normalized["row_count"],
        "changed_cells": len(normalized["changed_cells"]),
        "exact_duplicate_groups": len(normalized["duplicate_exact_field_groups"]),
        "prefix_duplicate_groups": len(normalized["duplicate_64_character_prefix_groups"]),
        "source_line_only_rows": normalized["source_line_only_count"],
        "concordance_counts": {key: value for key, value in summary.items() if key != "most_frequent_dot_candidates"},
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
