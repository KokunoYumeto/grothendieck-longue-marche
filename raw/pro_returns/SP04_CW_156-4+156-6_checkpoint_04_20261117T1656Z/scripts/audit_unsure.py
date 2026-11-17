#!/usr/bin/env python3
"""Read-only, mechanical association of page unsure macros with doubts rows.

Output never contains manuscript words or LaTeX arguments. Arguments are
compared exactly, without whitespace/notation/case normalization. Reported
line/column positions belong to the LaTeX file, not the manuscript image.
An association establishes matching recorded payloads on one page; it does
not establish that the row's prose location describes that occurrence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re

OUT = Path(__file__).resolve().parents[1]
PAGE_RE = re.compile(r"^(J156-[46]-\d{2})_(156-[46])_scan(\d{3})\.tex$")


def mask_comments(text):
    """Replace comments with spaces while preserving all offsets/newlines."""
    chars = list(text)
    i = 0
    while i < len(text):
        if text[i] == "\\":
            i += 2
        elif text[i] == "%":
            while i < len(text) and text[i] != "\n":
                chars[i] = " "
                i += 1
        else:
            i += 1
    return "".join(chars)


def unsure_calls(text):
    masked = mask_comments(text)
    calls, errors = [], []
    i = 0
    while i < len(masked):
        if masked[i] != "\\":
            i += 1
            continue
        start = i
        i += 1
        if i >= len(masked):
            break
        if not (masked[i].isalpha() or masked[i] == "@"):
            i += 1
            continue
        end = i
        while end < len(masked) and (masked[end].isalpha() or masked[end] == "@"):
            end += 1
        command = masked[i:end]
        i = end
        if command != "unsure":
            continue
        line = text.count("\n", 0, start) + 1
        column = start - text.rfind("\n", 0, start)
        opening = end
        while opening < len(masked) and masked[opening].isspace():
            opening += 1
        if opening >= len(masked) or masked[opening] != "{":
            errors.append({"line": line, "column": column, "error": "unsure has no braced argument"})
            continue
        depth, cursor = 1, opening + 1
        while cursor < len(masked) and depth:
            char = masked[cursor]
            if char == "\\":
                cursor += 2
                continue
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
            cursor += 1
        if depth:
            errors.append({"line": line, "column": column, "error": "unsure argument is unclosed"})
            continue
        calls.append({"line": line, "column": column, "argument": text[opening+1:cursor-1]})
        # Continue at the argument start to count any nested unsure commands.
        i = opening + 1
    return calls, errors


def candidate_payloads(row):
    """Exact encodings only; no inferred readings or substring matching."""
    result = {}
    reading = row.get("reading")
    if isinstance(reading, str):
        result.setdefault(reading, set()).add("exact_reading_field")
        for call in unsure_calls(reading)[0]:
            result.setdefault(call["argument"], set()).add("identical_unsure_argument_in_reading_field")
    alternatives = row.get("alternatives", [])
    if isinstance(alternatives, str):
        alternatives = [alternatives]
    if isinstance(alternatives, list) and all(isinstance(value, str) for value in alternatives):
        for alternative in alternatives:
            result.setdefault(alternative, set()).add("exact_alternative_field")
        if isinstance(reading, str) and alternatives:
            # Explicit encoding of the declared ordered candidate list in the
            # preamble convention; the resulting string must match exactly.
            result.setdefault("|".join([reading, *alternatives]), set()).add("exact_ordered_candidate_encoding")
    explicit = row.get("unsure_arguments", [])
    if isinstance(explicit, list):
        for argument in explicit:
            if isinstance(argument, str):
                result.setdefault(argument, set()).add("explicit_unsure_arguments_field")
    return result


def audit(out=OUT, done_only=False):
    out = Path(out).resolve()
    pages, unmatched, associations, parse_errors, missing_records = [], [], [], [], []
    totals = {"pages": 0, "unsure_occurrences": 0, "associated_occurrences": 0,
              "unmatched_occurrences": 0, "doubts_rows": 0,
              "doubts_rows_with_exact_associations": 0, "multiply_associated_occurrences": 0}
    for path in sorted((out / "pages").glob("*.tex")):
        match = PAGE_RE.fullmatch(path.name)
        if not match:
            continue
        _, cote, scan = match.groups()
        record_path = out / "records" / f"{cote}_scan{scan}.json"
        record = json.loads(record_path.read_text(encoding="utf-8")) if record_path.is_file() else {}
        done = bool(record.get("status", {}).get("done"))
        if done_only and not done:
            continue
        if not record_path.is_file():
            missing_records.append(path.name)
        doubts = record.get("doubts", [])
        if not isinstance(doubts, list):
            doubts = []
        candidates = {}
        for number, row in enumerate(doubts, 1):
            if not isinstance(row, dict):
                continue
            for payload, methods in candidate_payloads(row).items():
                candidates.setdefault(payload, []).append({"doubts_row": number, "methods": sorted(methods)})
        calls, errors = unsure_calls(path.read_text(encoding="utf-8"))
        used_rows = set()
        associated = multiple = 0
        page_unmatched = []
        for number, call in enumerate(calls, 1):
            payload = call["argument"]
            hits = candidates.get(payload, [])
            location = {"page": path.name, "occurrence": number, "line": call["line"],
                        "column": call["column"],
                        "argument_sha256": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
                        "argument_characters": len(payload)}
            if hits:
                associated += 1
                multiple += len(hits) > 1
                used_rows.update(hit["doubts_row"] for hit in hits)
                associations.append({**location, "associations": hits})
            else:
                unmatched.append(location)
                page_unmatched.append(number)
        parse_errors.extend({"page": path.name, **error} for error in errors)
        page = {"page": path.name, "cote": cote, "scan": int(scan), "record_done": done,
                "unsure_occurrences": len(calls), "associated_occurrences": associated,
                "unmatched_occurrences": len(page_unmatched), "unmatched_occurrence_numbers": page_unmatched,
                "doubts_rows": len(doubts), "doubts_rows_with_exact_associations": len(used_rows),
                "doubts_rows_without_exact_associations": [i for i in range(1, len(doubts)+1) if i not in used_rows],
                "multiply_associated_occurrences": multiple}
        pages.append(page)
        totals["pages"] += 1
        for key in totals:
            if key != "pages":
                totals[key] += page[key]
    return {"scope": "completed pages only" if done_only else "all saved matching page files",
            "totals": totals, "pages": pages, "unmatched_locations": unmatched, "matched_associations": associations,
            "parse_errors": parse_errors, "pages_without_records": missing_records,
            "association_methods": ["exact reading field", "identical unsure argument in reading field",
                                    "exact alternative field", "exact ordered reading/alternatives encoding with literal |",
                                    "explicit unsure_arguments field"],
            "limits": ["No manuscript payloads are emitted or interpreted.",
                       "No spelling, notation, case, or whitespace normalization is performed.",
                       "Line and column identify the LaTeX source, not an ink line.",
                       "An exact payload match on the same page does not establish location correspondence.",
                       "An unmatched item may have a differently encoded or broader doubt row; root review is required."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=OUT)
    parser.add_argument("--done-only", action="store_true")
    args = parser.parse_args()
    result = audit(args.out, args.done_only)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["unmatched_locations"] or result["parse_errors"] or result["pages_without_records"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
