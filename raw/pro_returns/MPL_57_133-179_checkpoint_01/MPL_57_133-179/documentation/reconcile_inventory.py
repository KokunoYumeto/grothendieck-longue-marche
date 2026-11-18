#!/usr/bin/env python3
"""Propose one inventory row per editorial macro, without changing page files.

Default: write a candidate CSV and review reports under documentation/. Existing
non-editorial rows are preserved byte-for-field, in their existing relative
order within each scan. --apply explicitly replaces only the inventory, after
backing it up and confirming the inputs have not changed during processing.
Explicit display environments are reported separately: no existing display row
is removed, rewritten, or silently split by this program.
"""
from __future__ import annotations

import argparse
import collections
import csv
import dataclasses
import datetime
import difflib
import hashlib
import io
import json
import re
import unicodedata
from pathlib import Path

PREFIX = "MPL_57_133-179"
FIELDS = ["cote", "scan", "sheet_kind", "element", "kind", "position",
          "first_words_or_objects", "transcribed"]
EDITORIAL = {"deleted": "deletion", "inserted": "insertion", "margin": "margin note"}
DISPLAY_ENVS = {"equation", "equation*", "displaymath", "align", "align*",
                "alignat", "alignat*", "gather", "gather*", "multline", "multline*",
                "flalign", "flalign*", "eqnarray", "eqnarray*"}
FORMAT_COMMANDS = {"unsure", "deleted", "inserted", "margin", "uline", "uuline",
                   "underline", "text", "textrm", "mathrm", "mathcal", "mathfrak",
                   "mathbb", "mathbf", "textbf", "textit", "operatorname", "ensuremath"}
SYMBOLS = {
    "α": " alpha ", "β": " beta ", "γ": " gamma ", "δ": " delta ",
    "μ": " mu ", "µ": " mu ", "ν": " nu ", "ρ": " rho ", "λ": " lambda ",
    "ξ": " xi ", "φ": " varphi ", "θ": " theta ", "Σ": " sum ",
    "∑": " sum ", "Π": " prod ", "∏": " prod ", "→": " to ",
    "←": " to ", "⇒": " to ", "≥": " geq ", "≤": " leq ",
    "×": " times ", "∈": " in ", "≠": " ne ", "′": " prime ",
    "’": "'", "…": " ", "_": " ",
}


@dataclasses.dataclass
class Span:
    name: str
    start: int
    end: int
    body_start: int
    body_end: int
    line: int
    body: str


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def commands(text: str):
    """Yield TeX control tokens; comments and escaped backslashes are respected."""
    i = 0
    while i < len(text):
        if text[i] == "%":
            stop = text.find("\n", i)
            i = len(text) if stop < 0 else stop + 1
        elif text[i] == "\\":
            start = i
            i += 1
            if i >= len(text):
                break
            if text[i].isalpha():
                j = i + 1
                while j < len(text) and text[j].isalpha():
                    j += 1
                yield text[i:j], start, j
                i = j
            else:
                yield text[i], start, i + 1
                i += 1
        else:
            i += 1


def skip_space_comments(text: str, i: int) -> int:
    while i < len(text):
        if text[i].isspace():
            i += 1
        elif text[i] == "%":
            j = text.find("\n", i)
            i = len(text) if j < 0 else j + 1
        else:
            break
    return i


def group(text: str, i: int) -> tuple[int, int]:
    i = skip_space_comments(text, i)
    if i >= len(text) or text[i] != "{":
        raise ValueError(f"Expected a braced argument near character {i}")
    start = i
    depth = 1
    i += 1
    while i < len(text):
        c = text[i]
        if c == "%":
            j = text.find("\n", i)
            i = len(text) if j < 0 else j + 1
            continue
        if c == "\\":
            i += 1
            if i < len(text) and text[i].isalpha():
                while i < len(text) and text[i].isalpha():
                    i += 1
            else:
                i += 1
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if not depth:
                return start, i
        i += 1
    raise ValueError(f"Unclosed argument beginning near character {start}")


def macro_spans(text: str, names: set[str]) -> list[Span]:
    result = []
    for name, start, stop in commands(text):
        if name not in names:
            continue
        left, right = group(text, stop)
        result.append(Span(name, start, right + 1, left + 1, right,
                           text.count("\n", 0, start) + 1, text[left + 1:right]))
    return result


def display_spans(text: str) -> list[Span]:
    result = []
    opened = []
    environments = []
    for name, start, stop in commands(text):
        if name == "[":
            opened.append((start, stop))
        elif name == "]":
            if not opened:
                raise ValueError("Unpaired \\] display delimiter")
            left, body_left = opened.pop()
            result.append(Span("bracket display", left, stop, body_left, start,
                               text.count("\n", 0, left) + 1, text[body_left:start]))
        elif name in {"begin", "end"}:
            left, right = group(text, stop)
            env = text[left + 1:right].strip()
            if env not in DISPLAY_ENVS:
                continue
            if name == "begin":
                environments.append((env, start, right + 1))
            else:
                if not environments or environments[-1][0] != env:
                    raise ValueError(f"Unpaired display environment {env}")
                env, opening, body_left = environments.pop()
                result.append(Span(env, opening, right + 1, body_left, start,
                                   text.count("\n", 0, opening) + 1, text[body_left:start]))
    if opened or environments:
        raise ValueError("Unclosed display environment")
    # Also support TeX's $$...$$, skipping comments and escaped control symbols.
    i = 0
    dollars = None
    while i < len(text):
        if text[i] == "%":
            stop = text.find("\n", i)
            i = len(text) if stop < 0 else stop + 1
        elif text[i] == "\\":
            i += 2
        elif text.startswith("$$", i):
            if dollars is None:
                dollars = i
            else:
                result.append(Span("double-dollar display", dollars, i + 2,
                                   dollars + 2, i, text.count("\n", 0, dollars) + 1,
                                   text[dollars + 2:i]))
                dollars = None
            i += 2
        else:
            i += 1
    if dollars is not None:
        raise ValueError("Unclosed double-dollar display")
    # A named environment enclosed by \\[...\\] is one explicit display, not two.
    result.sort(key=lambda s: (s.start, -s.end))
    return [s for i, s in enumerate(result)
            if not any(t.start <= s.start and t.end >= s.end for t in result[:i])]


def normalize(value: str) -> str:
    for source, target in SYMBOLS.items():
        value = value.replace(source, target)
    value = re.sub(r"\\([A-Za-z]+)",
                   lambda m: " " if m.group(1) in FORMAT_COMMANDS else " " + m.group(1) + " ", value)
    value = unicodedata.normalize("NFKD", value)
    value = "".join(c for c in value if not unicodedata.combining(c))
    return " ".join(re.findall(r"[a-z0-9]+", value.lower()))


def similarity(left: str, right: str) -> float:
    a, b = normalize(left), normalize(right)
    if not a or not b:
        return 0.0
    if a == b:
        return 1.0
    aa, bb = a.split(), b.split()
    # A short symbol match is too ambiguous to inherit a broad position.
    if min(len(a), len(b)) < 3:
        return 0.30 if (a in b or b in a) else 0.0
    if a in b or b in a:
        return 0.92 if min(len(aa), len(bb)) >= 2 else 0.67
    shared = len(set(aa) & set(bb))
    overlap = shared / max(1, min(len(set(aa)), len(set(bb))))
    sequence = difflib.SequenceMatcher(None, a[:250], b[:250]).ratio()
    return 0.55 * overlap + 0.45 * sequence


def excerpt(body: str, length: int = 220) -> str:
    value = " ".join(body.split())
    if len(value) <= length:
        return value
    return value[:length].rsplit(" ", 1)[0] + " …"


def best_match(body: str, rows: list[dict]) -> tuple[dict | None, float]:
    ranked = sorted(((similarity(body, row["first_words_or_objects"]), index, row)
                     for index, row in enumerate(rows)), key=lambda x: (-x[0], x[1]))
    if not ranked:
        return None, 0.0
    score, _, row = ranked[0]
    return (row if score >= 0.62 else None), score


def guess_anchor(row: dict, text: str, spans: list[Span]) -> tuple[float | None, str]:
    value = row["first_words_or_objects"]
    candidates = [(similarity(value, s.body), s.line) for s in spans]
    candidates += [(similarity(value, line), index)
                   for index, line in enumerate(text.splitlines(), 1) if line.strip()]
    if candidates:
        score, line = max(candidates, key=lambda pair: (pair[0], -pair[1]))
        if score >= 0.72:
            return float(line), f"textual anchor, score {score:.3f}"
    return None, "interpolated order only"


def csv_bytes(rows: list[dict], fields=FIELDS) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def align_displays(spans: list[Span], rows: list[dict]) -> list[int | None]:
    """Monotone bookkeeping alignment; count deficits force explicit split proposals.

    Do not mistake a short inventory formula/description for a missing element
    merely because lexical similarity is weak. If enough display rows exist,
    map at most one explicit display to a row. When there are too few rows,
    partition consecutive displays among the existing rows for review.
    """
    n, m = len(spans), len(rows)
    if not n:
        return []
    if not m:
        return [None] * n
    scores = [[similarity(span.body, row["first_words_or_objects"]) for row in rows]
              for span in spans]
    neg = float("-inf")
    dp = [[neg] * (m + 1) for _ in range(n + 1)]
    previous = {}
    dp[0][0] = 0.0
    if n <= m:
        for j in range(1, m + 1):
            dp[0][j] = 0.0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                skip = dp[i][j - 1]
                match = dp[i - 1][j - 1] + scores[i - 1][j - 1]
                if match >= skip:
                    dp[i][j] = match
                    previous[i, j] = (i - 1, j - 1, True)
                else:
                    dp[i][j] = skip
                    previous[i, j] = (i, j - 1, False)
        answer = [None] * n
        i, j = n, m
        while i:
            ii, jj, matched = previous[i, j]
            if matched:
                answer[i - 1] = j - 1
            i, j = ii, jj
        return answer
    for j in range(1, m + 1):
        for i in range(j, n + 1):
            for k in range(j - 1, i):
                value = dp[k][j - 1] + sum(scores[t][j - 1] for t in range(k, i))
                if value > dp[i][j]:
                    dp[i][j] = value
                    previous[i, j] = k
    answer = [None] * n
    i, j = n, m
    while j:
        k = previous[i, j]
        for t in range(k, i):
            answer[t] = j - 1
        i, j = k, j - 1
    return answer


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", nargs="?", type=Path,
                        default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--apply", action="store_true",
                        help="Explicitly apply regenerated editorial rows; display proposals remain review-only")
    args = parser.parse_args()
    root = args.package.resolve()
    docs = root / "documentation"
    inventory = root / f"{PREFIX}_inventory.csv"
    before = inventory.read_bytes()
    reader = csv.DictReader(io.StringIO(before.decode("utf-8")))
    if reader.fieldnames != FIELDS:
        raise ValueError(f"Unexpected inventory columns: {reader.fieldnames}")
    originals = list(reader)
    by_scan = collections.defaultdict(list)
    for row in originals:
        by_scan[int(row["scan"])].append(row)
    page_scans = {int(m.group(1)) for p in (root / "pages").glob("*.tex")
                  if (m := re.fullmatch(r"MPL_57_133-179_57_scan(\d+)\.tex", p.name))}
    if page_scans != set(by_scan):
        raise ValueError("Page-file and inventory scan sets differ; cannot infer a missing sheet_kind")
    candidates = []
    page_hashes = {}
    report = {"generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "input_inventory_sha256": digest(before), "applied": False,
              "scans": [], "display_proposals": [], "limitations": [
                  "No scan/image or context access; no claim of manuscript completeness.",
                  "All non-editorial rows are preserved field-for-field in their original relative order per scan.",
                  "Editorial occurrence order is exact; relative placement among non-editorial rows uses textual anchors and interpolation.",
                  "Broad-position matching is heuristic; exact TeX line numbers are authoritative for the generated rows.",
                  "Display matching is a monotone bookkeeping alignment, not verification against the image.",
                  "Display proposals require review and are never automatically applied."]}
    for scan, rows in sorted(by_scan.items()):
        page = root / "pages" / f"{PREFIX}_57_scan{scan:03d}.tex"
        data = page.read_bytes()
        page_hashes[page.name] = digest(data)
        text = data.decode("utf-8")
        sheet_kinds = {row["sheet_kind"] for row in rows}
        if len(sheet_kinds) != 1:
            raise ValueError(f"Conflicting sheet_kind values on scan {scan}: {sheet_kinds}")
        sheet_kind = next(iter(sheet_kinds))
        editorial = macro_spans(text, set(EDITORIAL))
        displays = display_spans(text)
        diagrams = macro_spans(text, {"diagram", "figure"})
        noneditorial = [row for row in rows if row["kind"] not in EDITORIAL.values()]
        original_ids = {row["element"] for row in noneditorial}
        generated = []
        mappings = []
        for index, span in enumerate(editorial, 1):
            kind = EDITORIAL[span.name]
            match, score = best_match(span.body, [r for r in rows if r["kind"] == kind])
            element = f"{scan}.ed{index:03d}"
            if element in original_ids:
                raise ValueError(f"Generated element id collides with preserved row: {element}")
            position = f"TeX line {span.line}"
            if match:
                # Idempotent regeneration does not accumulate repeated TeX-line prefixes.
                broad = re.sub(r"^TeX line \d+(?:;\s*)?", "", match["position"]).strip()
                if broad:
                    position += "; " + broad
            row = dict(zip(FIELDS, ["57", str(scan), sheet_kind, element, kind,
                                   position, excerpt(span.body), "yes"]))
            generated.append((span.line, span.start, row))
            mappings.append({"element": element, "macro": span.name, "line": span.line,
                             "start_character": span.start, "end_character": span.end,
                             "matched_old_element": match["element"] if match else None,
                             "match_score": round(score, 3),
                             "nested_within": [f"{scan}.ed{j:03d}" for j, outer in enumerate(editorial, 1)
                                               if outer.start < span.start and outer.end >= span.end]})

        # Merge into the unchanged non-editorial backbone. Unknown anchors are
        # interpolated; increasing anchors preserve its original relative order.
        anchors = [guess_anchor(row, text, displays + diagrams) for row in noneditorial]
        known = [(-1, 0.0)] + [(i, a) for i, (a, _) in enumerate(anchors) if a is not None]
        known.append((len(noneditorial), float(len(text.splitlines()) + 1)))
        adjusted = [None] * len(noneditorial)
        for (left_i, left), (right_i, right) in zip(known, known[1:]):
            right = max(left, right)
            for i in range(left_i + 1, right_i + 1):
                if i < len(adjusted):
                    adjusted[i] = left + (right - left) * (i - left_i) / (right_i - left_i)
        for i in range(1, len(adjusted)):
            adjusted[i] = max(adjusted[i], adjusted[i - 1])
        pending = iter(generated)
        current = next(pending, None)
        merged = []
        for row, anchor in zip(noneditorial, adjusted):
            while current and current[0] < anchor:
                merged.append(current[2])
                current = next(pending, None)
            merged.append(row)
        while current:
            merged.append(current[2])
            current = next(pending, None)
        assert [r for r in merged if r["kind"] not in EDITORIAL.values()] == noneditorial
        candidates.extend(merged)

        actual_display_rows = [r for r in rows if r["kind"] == "display"]
        # A row may have been reclassified during an audit even though its
        # corresponding fragment remains an explicit display. Keep that row
        # unchanged in the candidate; propose its kind for review separately.
        diagram_rows = [r for r in rows if r["kind"] == "diagram"]
        surplus_diagrams = len(diagram_rows) - sum(s.name == "diagram" for s in diagrams)
        kind_review_ids = set()
        if surplus_diagrams > 0:
            kind_candidates = []
            for span in displays:
                match, score = best_match(span.body, diagram_rows)
                _, display_score = best_match(span.body, actual_display_rows)
                if match and score >= 0.72 and score >= display_score + 0.15:
                    kind_candidates.append((score, span, match))
            for score, span, match in sorted(kind_candidates, key=lambda item: -item[0]):
                if len(kind_review_ids) >= surplus_diagrams:
                    break
                if match["element"] in kind_review_ids:
                    continue
                kind_review_ids.add(match["element"])
                report["display_proposals"].append({
                    "action": "review row kind: diagram to display", "scan": scan,
                    "existing_element": match["element"],
                    "explicit_displays": [{"scan": scan, "line": span.line,
                        "display_type": span.name, "first_words_or_objects": excerpt(span.body),
                        "match_score": round(score, 3)}],
                    "reason": "Diagram rows outnumber diagram macros, and this row strongly matches an explicit display. Candidate preserves its current kind; subsequent display alignment provisionally counts it as a display."})
        display_rows = [r for r in rows if r["kind"] == "display" or r["element"] in kind_review_ids]
        mapped_displays = collections.defaultdict(list)
        unmatched = []
        display_alignment = []
        for span, row_index in zip(displays, align_displays(displays, display_rows)):
            match = display_rows[row_index] if row_index is not None else None
            score = similarity(span.body, match["first_words_or_objects"]) if match else 0.0
            item = {"scan": scan, "line": span.line, "display_type": span.name,
                    "first_words_or_objects": excerpt(span.body), "match_score": round(score, 3)}
            if match:
                item["existing_element"] = match["element"]
                mapped_displays[match["element"]].append(item)
            else:
                unmatched.append(item)
            display_alignment.append(item)
        for element, items in mapped_displays.items():
            if len(items) > 1:
                report["display_proposals"].append({"action": "review split of existing row",
                    "scan": scan, "existing_element": element, "explicit_displays": items,
                    "reason": "Explicit displays outnumber display rows. Monotone textual alignment proposes this row for splitting; verify the assignment before editing."})
        for item in unmatched:
            report["display_proposals"].append({"action": "review unmatched explicit display",
                "scan": scan, "explicit_displays": [item],
                "reason": "An explicit display environment has no display inventory row; inspect other element kinds before adding a row."})
        report["scans"].append({"scan": scan, "sheet_kind": sheet_kind,
            "editorial_macro_count": len(editorial),
            "editorial_counts": dict(collections.Counter(EDITORIAL[s.name] for s in editorial)),
            "old_editorial_rows": sum(r["kind"] in EDITORIAL.values() for r in rows),
            "preserved_noneditorial_rows": len(noneditorial),
            "explicit_display_count": len(displays), "existing_display_rows": len(actual_display_rows),
            "provisional_display_rows_for_alignment": len(display_rows),
            "display_alignment": display_alignment,
            "editorial_mappings": mappings,
            "noneditorial_anchors": [{"element": r["element"], "estimated_line": round(a, 3),
                                       "method": method} for r, a, (_, method) in zip(noneditorial, adjusted, anchors)]})

    report["source_page_sha256"] = page_hashes
    candidate_path = docs / "inventory_reconciled_candidate.csv"
    candidate_data = csv_bytes(candidates)
    candidate_path.write_bytes(candidate_data)
    report["candidate_inventory_sha256"] = digest(candidate_data)
    report["candidate_rows"] = len(candidates)
    report["original_rows"] = len(originals)
    report["editorial_rows"] = sum(r["kind"] in EDITORIAL.values() for r in candidates)
    report["preserved_noneditorial_rows"] = sum(r["kind"] not in EDITORIAL.values() for r in candidates)
    if args.apply:
        if inventory.read_bytes() != before:
            raise RuntimeError("Inventory changed during reconciliation; candidate not applied")
        for name, expected in page_hashes.items():
            if digest((root / "pages" / name).read_bytes()) != expected:
                raise RuntimeError(f"Page {name} changed during reconciliation; candidate not applied")
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        backup = docs / f"inventory_before_reconciliation_{stamp}.csv"
        backup.write_bytes(before)
        temporary = inventory.with_suffix(".csv.pending")
        temporary.write_bytes(candidate_data)
        temporary.replace(inventory)
        report["applied"] = True
        report["backup_inventory"] = str(backup)
    (docs / "inventory_reconciliation_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    proposal_rows = []
    for proposal in report["display_proposals"]:
        for item in proposal["explicit_displays"]:
            proposal_rows.append({"scan": item["scan"], "action": proposal["action"],
                "existing_element": proposal.get("existing_element", ""), "tex_line": item["line"],
                "first_words_or_objects": item["first_words_or_objects"], "reason": proposal["reason"]})
    (docs / "inventory_display_proposals.csv").write_bytes(csv_bytes(proposal_rows,
        ["scan", "action", "existing_element", "tex_line", "first_words_or_objects", "reason"]))
    print(json.dumps({k: report[k] for k in ["applied", "original_rows", "candidate_rows",
        "editorial_rows", "preserved_noneditorial_rows"]} | {
        "candidate": str(candidate_path), "display_proposal_count": len(report["display_proposals"]),
        "report": str(docs / "inventory_reconciliation_report.json")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
