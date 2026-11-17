#!/usr/bin/env python3
"""Build a separate inventory candidate from TeX structure, without image access.

The source-order rows are mechanical evidence of content already represented in
the fragments. They do not prove that the fragments exhaust their source scans.
The existing inventory is read solely for sheet classifications and never changed.
"""
from __future__ import annotations

import argparse
import bisect
import csv
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re

PREFIX = "MPL_12_051-098"
COLUMNS = ["cote", "scan", "sheet_kind", "element", "kind", "position", "first_words_or_objects", "transcribed"]
KINDS = {"deleted": "deletion", "inserted": "insertion", "margin": "margin note", "diagram": "diagram", "figure": "drawing"}
METADATA = {"cotefile", "scanpage", "mspage"}
OVERRIDES = {52: "cancelled_draft", 58: "cancelled_draft", 61: "reused_typed", 72: "reused_typed", 96: "cover"}
DISPLAY_ENVS = {"equation", "equation*", "align", "align*", "gather", "gather*", "multline", "multline*", "displaymath"}


@dataclass
class Event:
    start: int
    end: int
    kind: str
    tag: str


def escaped(source: str, index: int) -> bool:
    n = 0
    index -= 1
    while index >= 0 and source[index] == "\\":
        n += 1
        index -= 1
    return bool(n % 2)


def mask_comments(source: str) -> str:
    chars = list(source)
    i = 0
    while i < len(chars):
        if chars[i] == "%" and not escaped(source, i):
            while i < len(chars) and chars[i] != "\n":
                chars[i] = " "
                i += 1
        i += 1
    return "".join(chars)


def command_at(source: str, index: int) -> tuple[str, int] | None:
    if index >= len(source) or source[index] != "\\" or escaped(source, index):
        return None
    match = re.match(r"\\([A-Za-z]+|.)", source[index:], flags=re.S)
    return (match.group(1), index + len(match.group(0))) if match else None


def parse_page(source: str) -> tuple[list[Event], list[dict]]:
    clean = mask_comments(source)
    diagnostics: list[dict] = []
    groups: dict[int, int] = {}
    stack: list[int] = []
    for i, char in enumerate(clean):
        if escaped(clean, i):
            continue
        if char == "{":
            stack.append(i)
        elif char == "}":
            if stack:
                groups[stack.pop()] = i + 1
            else:
                diagnostics.append({"offset": i, "type": "brace", "issue": "closing brace without opener"})
    for i in stack:
        diagnostics.append({"offset": i, "type": "brace", "issue": "opening brace without closer"})

    macros: list[Event] = []
    macro_contents: dict[int, tuple[int, int]] = {}
    metadata: list[Event] = []
    displays: list[Event] = []
    environments: list[Event] = []
    env_stack: list[tuple[str, int]] = []
    bracket_stack: list[int] = []
    dollars: list[int] = []
    i = 0
    while i < len(clean):
        token = command_at(clean, i)
        if token:
            name, after = token
            j = after
            while j < len(clean) and clean[j].isspace():
                j += 1
            if name in KINDS or name in METADATA:
                if j not in groups:
                    diagnostics.append({"offset": i, "type": "argument", "issue": f"\\{name} lacks a balanced braced argument"})
                else:
                    event = Event(i, groups[j], KINDS.get(name, "metadata"), name)
                    (macros if name in KINDS else metadata).append(event)
                    if name in KINDS:
                        macro_contents[i] = (j + 1, groups[j] - 1)
            elif name in {"begin", "end"} and j in groups:
                env = clean[j + 1:groups[j] - 1].strip()
                if name == "begin":
                    env_stack.append((env, i))
                elif not env_stack:
                    diagnostics.append({"offset": i, "type": "environment", "issue": f"end of {env} without begin"})
                elif env_stack[-1][0] != env:
                    diagnostics.append({"offset": i, "type": "environment", "issue": f"end of {env} while {env_stack[-1][0]} is open"})
                else:
                    _, start = env_stack.pop()
                    environments.append(Event(start, groups[j], "environment", env))
            elif name == "[":
                if bracket_stack:
                    diagnostics.append({"offset": i, "type": "math", "issue": "nested display opener"})
                bracket_stack.append(i)
            elif name == "]":
                if bracket_stack:
                    displays.append(Event(bracket_stack.pop(), after, "display", "display-brackets"))
                else:
                    diagnostics.append({"offset": i, "type": "math", "issue": "display closer without opener"})
            i = after
            continue
        if clean[i] == "$" and not escaped(clean, i):
            dollars.append(i)
        i += 1
    for start in bracket_stack:
        diagnostics.append({"offset": start, "type": "math", "issue": "display opener without closer"})
    for env, start in env_stack:
        diagnostics.append({"offset": start, "type": "environment", "issue": f"unclosed environment {env}"})
    if len(dollars) % 2:
        diagnostics.append({"offset": dollars[-1], "type": "math", "issue": "odd number of unescaped dollar delimiters in page"})
    inline_math = [(dollars[k], dollars[k + 1] + 1) for k in range(0, len(dollars) - 1, 2)]

    for event in environments:
        if event.tag in DISPLAY_ENVS:
            displays.append(Event(event.start, event.end, "display", event.tag))
        elif event.tag in {"tikzcd", "tikzpicture"}:
            kind = "diagram" if event.tag == "tikzcd" else "drawing"
            if not any(m.kind == kind and m.start <= event.start and event.end <= m.end for m in macros):
                macros.append(Event(event.start, event.end, kind, event.tag))

    # Discard nested display containers that represent exactly the same display.
    displays = [e for e in displays if not any(o is not e and o.start <= e.start and e.end <= o.end for o in displays)]
    events = macros + displays
    by_start = {e.start: e for e in events + metadata}
    def flush(destination: list[Event], start: int | None, end: int) -> None:
        if start is None:
            return
        while start < end and clean[start].isspace():
            start += 1
        while end > start and clean[end - 1].isspace():
            end -= 1
        if start == end:
            return
        # A state macro spanning an entire paragraph already supplies that row.
        # Inline state changes remain additional rows within a live text block.
        remainder = list(clean[start:end])
        for macro in macros:
            if macro.tag in {"deleted", "inserted", "margin"} and start <= macro.start and macro.end <= end:
                for k in range(macro.start - start, macro.end - start):
                    remainder[k] = " "
        residual = "".join(remainder)
        residual = re.sub(r"\\(?:hfill|quad|qquad|newline|par)\b|\\\\", "", residual)
        if not re.sub(r"[\s{}]", "", residual):
            return
        destination.append(Event(start, end, "text", "paragraph"))

    def collect_text(range_start: int, range_end: int) -> list[Event]:
        destination: list[Event] = []
        i = range_start
        paragraph_start: int | None = None
        while i < range_end:
            event = by_start.get(i)
            if event and event.end <= range_end:
                if event.kind in {"display", "diagram", "drawing", "margin note", "metadata"}:
                    flush(destination, paragraph_start, i)
                    paragraph_start = None
                    i = event.end
                    continue
                if event.tag in {"deleted", "inserted"}:
                    if paragraph_start is None:
                        paragraph_start = i
                    i = event.end
                    continue
            if clean[i] == "\n":
                separator = re.match(r"\n[ \t]*\n(?:[ \t]*\n)*", clean[i:range_end])
                if separator:
                    flush(destination, paragraph_start, i)
                    paragraph_start = None
                    i += len(separator.group(0))
                    continue
            if paragraph_start is None and not clean[i].isspace():
                paragraph_start = i
            if i in groups and groups[i] <= range_end:
                i = groups[i]
            else:
                i += 1
        flush(destination, paragraph_start, range_end)
        return destination

    text_events = collect_text(0, len(clean))
    # A wrapper enclosing several paragraphs does not erase their distinct text
    # blocks. A single enclosed paragraph is already covered by its state row.
    for macro in macros:
        if macro.tag in {"deleted", "inserted", "margin"} and macro.start in macro_contents:
            content_start, content_end = macro_contents[macro.start]
            children = collect_text(content_start, content_end)
            if len(children) > 1:
                text_events.extend(children)
    events.extend(text_events)
    events.sort(key=lambda e: (e.start, 0 if e.kind == "text" else 1, -e.end))

    # A conservative math-context check. TikZ-CD entries have implicit math mode.
    math_ranges = inline_math + [(e.start, e.end) for e in displays]
    math_ranges += [(e.start, e.end) for e in environments if e.tag == "tikzcd"]
    for i, char in enumerate(clean):
        if char in "_^" and not escaped(clean, i) and not any(a <= i < b for a, b in math_ranges):
            diagnostics.append({"offset": i, "type": "math-context", "issue": f"unescaped {char} outside detected math spans; manual review"})
    for match in re.finditer(r"\\rotatebox\b", clean):
        diagnostics.append({"offset": match.start(), "type": "package", "issue": "rotatebox comes from graphicx (normally loaded transitively by TikZ); dependency review only, not a detected syntax error"})
    line_starts = [0] + [m.end() for m in re.finditer("\n", source)]
    for d in diagnostics:
        d["line"] = bisect.bisect_right(line_starts, d["offset"])
        d["column"] = d["offset"] - line_starts[d["line"] - 1] + 1
    return events, diagnostics


def literal_prefix_keys(value: str) -> list[str]:
    """Whitespace normalization and removal of one literal state wrapper only."""
    value = re.sub(r"\s+", " ", value).strip()
    keys = [value]
    match = re.match(r"\\(?:deleted|inserted|margin|diagram|figure)\s*\{", value)
    if match:
        keys.append(value[match.end():].strip())
    return [key for key in keys if key]


def literal_prefix_match(left: str, right: str) -> bool:
    if left == right and len(left) >= 4:
        return True
    shorter = left if len(left) <= len(right) else right
    return sum(not c.isspace() for c in shorter) >= 12 and (left.startswith(right) or right.startswith(left))


def preserve_physical_positions(rows: list[dict], originals: list[dict]) -> dict:
    """Carry over only unambiguous literal-prefix matches to actual page regions."""
    candidates: dict[int, list[int]] = {}
    reverse: dict[int, list[int]] = {}
    physical_originals = []
    for index, original in enumerate(originals):
        position = original.get("position", "").strip()
        # These descriptions only locate the TeX, not a region of the scan.
        if not position or position.startswith("TeX ") or re.fullmatch(r"within page;\s*TeX line.*", position, flags=re.I):
            continue
        physical_originals.append(index)
    for index, row in enumerate(rows):
        options = []
        for j in physical_originals:
            original = originals[j]
            old_kind = {"title": "text", "formula": "display"}.get(original["kind"], original["kind"])
            if int(original["scan"]) != int(row["scan"]) or old_kind != row["kind"]:
                continue
            if any(literal_prefix_match(a, b) for a in literal_prefix_keys(row["first_words_or_objects"]) for b in literal_prefix_keys(original["first_words_or_objects"])):
                options.append(j)
                reverse.setdefault(j, []).append(index)
        candidates[index] = options
    matched = []
    unmatched = []
    for index, row in enumerate(rows):
        options = candidates[index]
        if len(options) == 1 and len(reverse[options[0]]) == 1:
            original_index = options[0]
            original = originals[original_index]
            row["position"] = original["position"].strip() + "; " + row["position"]
            matched.append({"scan": row["scan"], "candidate_element": row["element"], "original_csv_line": original_index + 2, "original_element": original["element"], "physical_position": original["position"], "method": "unique bidirectional literal prefix match; whitespace normalized; one state wrapper may be ignored"})
        else:
            row["position"] += "; physical position unassigned"
            unmatched.append({"scan": row["scan"], "element": row["element"], "kind": row["kind"], "reason": "no unique literal match to original physical-region metadata"})
    return {
        "matched_count": len(matched), "unassigned_count": len(unmatched),
        "original_rows_with_physical_metadata": len(physical_originals),
        "matches": matched, "unassigned": unmatched,
        "limitation": "TeX source order and line spans do not establish physical page coordinates. Unassigned positions require visual review by the sole transcription reader; they have not been guessed.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--prefix-length", type=int, default=160)
    args = parser.parse_args()
    base = args.base.resolve()
    current = base / f"{PREFIX}_inventory.csv"
    output = (args.output or base / "records" / f"{PREFIX}_inventory_candidate.csv").resolve()
    report_path = (args.report or base / "records" / "inventory_candidate_report.json").resolve()
    if output == current.resolve():
        raise SystemExit("Refusing to overwrite the existing inventory; review the candidate separately.")
    sheet_map: dict[int, str] = {}
    original_rows: list[dict] = []
    if current.exists():
        with current.open(encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                original_rows.append(row)
                sheet_map[int(row["scan"])] = row["sheet_kind"]
    sheet_map.update(OVERRIDES)
    rows: list[dict] = []
    report = {"method": "TeX structure only; no scan-image access or semantic readings", "candidate": str(output), "pages": {}, "diagnostics": [], "source_sha256": {}}
    for page in sorted((base / "pages").glob(f"{PREFIX}_12_scan*.tex")):
        match = re.search(r"scan(\d{3})\.tex$", page.name)
        if not match:
            continue
        scan = int(match.group(1))
        source = page.read_text(encoding="utf-8")
        report["source_sha256"][page.name] = hashlib.sha256(page.read_bytes()).hexdigest()
        events, diagnostics = parse_page(source)
        line_starts = [0] + [m.end() for m in re.finditer("\n", source)]
        kinds: dict[str, int] = {}
        for index, event in enumerate(events, 1):
            first = bisect.bisect_right(line_starts, event.start)
            last = bisect.bisect_right(line_starts, max(event.start, event.end - 1))
            prefix = re.sub(r"\s+", " ", mask_comments(source[event.start:event.end])).strip()[:args.prefix_length]
            rows.append({
                "cote": "12", "scan": f"{scan:03d}", "sheet_kind": sheet_map.get(scan, "text"),
                "element": f"e{index:03d}", "kind": event.kind,
                "position": f"TeX lines {first}-{last}; chars {event.start + 1}-{event.end}",
                "first_words_or_objects": prefix, "transcribed": "yes",
            })
            kinds[event.kind] = kinds.get(event.kind, 0) + 1
        report["pages"][f"{scan:03d}"] = {"rows": len(events), "kinds": kinds, "sheet_kind": sheet_map.get(scan, "text")}
        for d in diagnostics:
            report["diagnostics"].append({"scan": scan, "file": page.name, **d})
    report["physical_positions"] = preserve_physical_positions(rows, original_rows)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    report["row_count"] = len(rows)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"candidate": str(output), "report": str(report_path), "pages": len(report["pages"]), "rows": len(rows), "physical_positions_preserved": report["physical_positions"]["matched_count"], "physical_positions_unassigned": report["physical_positions"]["unassigned_count"], "diagnostics": report["diagnostics"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
