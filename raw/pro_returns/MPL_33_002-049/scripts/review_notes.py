#!/usr/bin/env python3
"""Read-only checks of the research-note manifest, rendered notes, and searches.

No file is written. Default mode treats not-yet-built notes/search records as
pending warnings. --complete requires both final products. Sentence counts and
quotation markers are syntactic checks, not judgments of mathematical content.

Context searches may be a mapping keyed by note ID or a list of records carrying
id/note_id/note. A typical note record has nonempty terms and a files/searches
mapping keyed by each source path; an explicitly recorded zero-hit search is
valid. Every note must cover all three supplied files. File/filename/path/source
fields and query/queries/term/terms/search_terms fields are also recognized.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re

PREFIX = "MPL_33_002-049"
ID_PATTERN = r"[A-Z]\d{2,}"
SOURCE_FILES = (
    "README.md",
    "notes/RESULTS_STATE.md",
    "same_cote_33/MPL_33_098-146_notes.md",
)
KINDS = {
    "conjecture", "unproved claim", "unpursued implication", "own idea",
    "reading question", "self-flagged", "withdrawn in the same text",
}
ABBREVIATIONS = (
    "i.e.", "e.g.", "p.ex.", "t.f.", "N.B.", "cf.", "resp.", "loc.",
    "dim.", "th.", "prop.", "cor.", "constr.", "conn.", "géom.", "hyp.",
    "int.", "coeff.", "fct.", "sép.", "alg.", "cat.", "supp.", "pr.",
    "fig.", "eq.", "no.", "nos.", "pp.", "p.", "vol.", "etc.", "Dr.", "Mr.",
)


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def sentence_count(body: str) -> int:
    text = body
    # Drop URL punctuation while retaining a Markdown link's visible label.
    text = re.sub(r"\[([^\]]+)\]\(https?://[^\s]+?\)", r"\1", text)
    text = re.sub(r"https?://[^\s)>]+", " URL ", text)
    text = re.sub(r"`+[^`]+`+", " CODE ", text)
    for pattern in (
        r"(?<!\\)\$\$.*?(?<!\\)\$\$",
        r"(?<!\\)\$(?!\$).*?(?<!\\)\$",
        r"\\\[.*?\\\]", r"\\\(.*?\\\)",
    ):
        text = re.sub(pattern, " MATH ", text, flags=re.S)
    text = re.sub(r"\.{2,}|…", " ELLIPSIS ", text)
    # Section numbers inside quoted headings ("5. Systems ...", "19.6. ...")
    # are not complete prose sentences.
    text = re.sub(r'([“«"]\s*\d+(?:\.\d+)*\.)(?=\s)',
                  lambda match: match.group(0).replace(".", "·"), text)
    for abbreviation in sorted(ABBREVIATIONS, key=len, reverse=True):
        text = re.sub(r"(?<!\w)" + re.escape(abbreviation),
                      lambda match: match.group(0).replace(".", "·"), text, flags=re.I)
    text = re.sub(r"(?<=\d)\.(?=\d)", "·", text)
    ends = []
    for match in re.finditer(r"[.!?]+[\"”’»\)\]]*(?=\s|$)", text):
        after = text[match.end():].lstrip()
        # A sentence-ending period inside an attributed quotation may be followed
        # by a lowercase continuation; avoid counting that as a new sentence.
        if after and after[0].islower() and match.group(0).startswith("."):
            continue
        ends.append(match.end())
    count = len(ends)
    remainder = text[ends[-1]:] if ends else text
    if re.search(r"\w", remainder):
        count += 1
    return count


def has_quote(note: dict) -> bool:
    for key in ("quote", "quotes", "quotation", "source_quote", "source_quotes"):
        if note.get(key):
            return True
    body = str(note.get("body", ""))
    return any(re.search(pattern, body, re.S) for pattern in (
        r"“[^”]+”", r"«[^»]+»", r'"[^"\n]+"', r"``.+?''", r"`[^`]+`",
    ))


def canonical_source(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    candidate = value.replace("\\", "/").strip()
    for source in SOURCE_FILES:
        if candidate == source or candidate.endswith("/" + source):
            return source
        if candidate == source.rsplit("/", 1)[-1]:
            return source
    return None


def query_strings(value: object) -> list[str]:
    if isinstance(value, str):
        return [value.strip()] if value.strip() else []
    if isinstance(value, list):
        return [part for child in value for part in query_strings(child)]
    if isinstance(value, dict):
        result = []
        for key, child in value.items():
            if key in {"q", "query", "term", "terms", "search_terms", "queries"}:
                result.extend(query_strings(child))
        return result
    return []


def find_note_records(data: object) -> dict[str, list[object]]:
    records = defaultdict(list)

    def visit(value: object, source_hint: str | None = None) -> None:
        if isinstance(value, list):
            for item in value:
                visit(item, source_hint)
        elif isinstance(value, dict):
            identifier = next((value.get(key) for key in ("id", "note_id", "note")
                               if isinstance(value.get(key), str)
                               and re.fullmatch(ID_PATTERN, value[key])), None)
            if identifier:
                records[identifier].append({"source": source_hint, "record": value}
                                           if source_hint else value)
                return
            for key, item in value.items():
                hint = canonical_source(key) or source_hint
                if re.fullmatch(ID_PATTERN, str(key)):
                    records[key].append({"source": hint, "record": item} if hint else item)
                else:
                    visit(item, hint)

    visit(data)
    return dict(records)


def search_coverage(records: list[object]) -> tuple[dict[str, int], set[str]]:
    coverage = Counter()
    empty_queries = set()

    def visit(value: object, inherited: list[str], source_hint: str | None = None) -> None:
        own = list(inherited)
        if isinstance(value, dict):
            for key in ("terms", "term", "queries", "query", "search_terms", "q"):
                if key in value:
                    own.extend(query_strings(value[key]))
            source = source_hint
            for key in ("file", "filename", "file_name", "path", "source", "source_file"):
                source = canonical_source(value.get(key)) or source
            if source:
                if own:
                    coverage[source] += 1
                else:
                    empty_queries.add(source)
            for key, item in value.items():
                child_source = canonical_source(key)
                if child_source:
                    # The presence of a source key and query terms records an
                    # executed zero-hit search even when its value is [].
                    if own:
                        coverage[child_source] += 1
                    else:
                        empty_queries.add(child_source)
                    visit(item, own, child_source)
                elif isinstance(item, (dict, list)):
                    visit(item, own, source)
        elif isinstance(value, list):
            if source_hint and inherited:
                coverage[source_hint] += 1
            for child in value:
                visit(child, inherited, source_hint)

    for record in records:
        visit(record, [])
    return dict(coverage), empty_queries - set(coverage)


def scan_numbers(value: str) -> set[int]:
    found = {int(number) for number in re.findall(r"(?<!\d)\d{1,3}(?!\d)", value)}
    for match in re.finditer(r"(?<!\d)(\d{1,3})\s*[-–]\s*(\d{1,3})(?!\d)", value):
        start, end = map(int, match.groups())
        if start <= end:
            found.update(range(start, end + 1))
    if "odd" in value.lower():
        found = {number for number in found if number % 2}
    return found


def markdown_cells(line: str) -> list[str]:
    # GFM table delimiters must be escaped even inside inline code.
    cuts = []
    for i, char in enumerate(line):
        if char != "|":
            continue
        backslashes = 0
        j = i - 1
        while j >= 0 and line[j] == "\\":
            backslashes += 1
            j -= 1
        if not backslashes % 2:
            cuts.append(i)
    return [line[a + 1:b].strip() for a, b in zip(cuts, cuts[1:])]


def source_plain(text: str) -> str:
    # Preserve words and mathematical tokens; remove only editorial wrappers
    # for a literal-phrase comparison. This never writes a normalized source.
    previous = None
    while previous != text:
        previous = text
        text = re.sub(r"\\(?:uline|uuline|inserted|deleted|margin|fbox|text)\{([^{}]*)\}", r"\1", text)
        text = re.sub(r"\\unsure\{([^{}]*)\}", lambda m: m.group(1).split("|")[0], text)
    return normalized(text.replace("\\|", "|").replace("[Question]", "Question"))


def review(root: Path, complete: bool = False) -> dict:
    errors = []
    warnings = []

    def issue(kind: str, identifier: str, message: str, *, warning: bool = False) -> None:
        (warnings if warning else errors).append({"kind": kind, "note": identifier, "message": message})

    manifest_path = root / "records/research_note_manifest.json"
    if not manifest_path.is_file():
        return {"ok": False, "errors": [{"kind": "missing_manifest", "note": "", "message": str(manifest_path)}],
                "warnings": [], "counts": {}}
    try:
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"ok": False, "errors": [{"kind": "manifest_unreadable", "note": "", "message": str(exc)}],
                "warnings": [], "counts": {}}
    notes = payload.get("notes") if isinstance(payload, dict) else payload
    if not isinstance(notes, list) or any(not isinstance(note, dict) for note in notes):
        return {"ok": False, "errors": [{"kind": "manifest_schema", "note": "", "message": "Expected a list of note objects or an object with a notes list."}],
                "warnings": [], "counts": {}}
    ids = [str(note.get("id", "")) for note in notes]
    for identifier, count in Counter(ids).items():
        if not re.fullmatch(ID_PATTERN, identifier):
            issue("invalid_id", identifier, "Expected an uppercase prefix followed by at least two digits.")
        if count > 1:
            issue("duplicate_id", identifier, f"Occurs {count} times in the manifest.")
    sentence_counts = {}
    kinds = Counter()
    page_lines = {}
    for page in (root / "pages").glob(f"{PREFIX}_33_scan[0-9][0-9][0-9].tex"):
        scan = int(re.search(r"scan(\d+)", page.name).group(1))
        page_lines[scan] = page.read_text(encoding="utf-8").splitlines()
    checked_numeric_locators = 0
    for note in notes:
        identifier = str(note.get("id", ""))
        kind = str(note.get("kind", "")).strip()
        base_kind = next((candidate for candidate in KINDS
                          if kind == candidate or kind.startswith(candidate + ":")), kind)
        kinds[base_kind] += 1
        if base_kind not in KINDS:
            issue("invalid_kind", identifier, f"Unrecognized kind: {kind!r}")
        for key in ("scans", "lines", "body"):
            if not isinstance(note.get(key), str) or not note[key].strip():
                issue("missing_field", identifier, f"{key} must be a nonempty string.")
        declared_scans = scan_numbers(str(note.get("scans", "")))
        for part in str(note.get("lines", "")).split(";"):
            prefix = re.match(r"\s*((?:\d{1,3}\s*[/,]\s*)*\d{1,3})\s*:\s*(.*)", part)
            targets = scan_numbers(prefix.group(1)) if prefix else declared_scans
            locator = prefix.group(2) if prefix else part
            numbers = [int(number) for number in re.findall(r"(?<!\d)\d{1,3}(?!\d)", locator)]
            for scan in sorted(targets):
                if not numbers:
                    continue
                if scan not in page_lines:
                    issue("locator_scan_missing", identifier, f"Numeric locator refers to unavailable current scan {scan:03}.")
                    continue
                if prefix and scan not in declared_scans:
                    issue("locator_scan_undeclared", identifier, f"Line locator names scan {scan:03}, absent from the scans field.")
                for number in numbers:
                    checked_numeric_locators += 1
                    if not 1 <= number <= len(page_lines[scan]):
                        issue("line_locator_out_of_range", identifier,
                              f"Scan {scan:03}, line {number}, exceeds available range 1–{len(page_lines[scan])}.")
        body = str(note.get("body", ""))
        count = sentence_count(body)
        sentence_counts[identifier] = count
        if not 1 <= count <= 4:
            issue("sentence_count", identifier, f"Heuristic body count is {count}; expected 1–4 sentences (math, links, abbreviations masked).")
        if base_kind != "own idea" and not has_quote(note):
            if "$" in body or "\\(" in body:
                issue("quotation_marker_review", identifier,
                      "No explicit quotation marker; mathematical notation is present. Confirm that the source wording/formula is adequately quoted.", warning=True)
            else:
                issue("missing_source_quote", identifier, "Source-related note has no recognized quotation or source_quote field.")
        if base_kind == "own idea":
            confidence = str(note.get("confidence", "")).strip()
            if not re.search(r"\b(?:high|medium|low)\b", confidence, re.I):
                issue("missing_confidence", identifier, "Own idea needs an explicit high/medium/low confidence level.")
            reason = str(note.get("reason") or note.get("confidence_reason") or "").strip()
            # A descriptive confidence field such as 'high: [reason]' is valid.
            if not reason:
                reason = re.sub(r"^(?:high|medium|low)\b\s*(?::|for|because|—|-)?\s*", "", confidence, flags=re.I)
            if len(re.findall(r"\w+", reason)) < 4:
                issue("missing_confidence_reason", identifier, "Own idea confidence needs a substantive reason, separately or in the confidence field.")
        terms = note.get("terms")
        if not isinstance(terms, list) or not any(isinstance(term, str) and term.strip() for term in terms):
            issue("missing_search_terms", identifier, "Per-note context terms must be a nonempty list of nonempty strings.")

    notes_path = root / f"{PREFIX}_notes.md"
    rendered_count = 0
    table_count = 0
    table_rows = 0
    standing_quotes_checked = 0
    if not notes_path.is_file():
        issue("notes_pending", "", "Rendered research notes do not yet exist.", warning=not complete)
    else:
        rendered = notes_path.read_text(encoding="utf-8")
        expected_width = None
        in_standing_section = False
        for line_number, line in enumerate(rendered.splitlines(), 1):
            if line.startswith("## V. Standing"):
                in_standing_section = True
            elif in_standing_section and line.startswith("## "):
                in_standing_section = False
            if not (line.startswith("|") and line.rstrip().endswith("|")):
                expected_width = None
                continue
            cells = markdown_cells(line.rstrip())
            if expected_width is None:
                expected_width = len(cells)
                table_count += 1
            table_rows += 1
            if len(cells) != expected_width:
                issue("markdown_table_width", "",
                      f"Notes Markdown line {line_number}: {len(cells)} cells, expected {expected_width}; check unescaped pipes.")
            if not in_standing_section or len(cells) < 2:
                continue
            loci = list(re.finditer(r"(?<!\d)(\d{3}):(\d+)(?:\s*[-–]\s*(\d+))?", cells[0]))
            source_parts = []
            for locus in loci:
                scan, first = int(locus.group(1)), int(locus.group(2))
                last = int(locus.group(3) or first)
                if scan not in page_lines:
                    issue("standing_scan_missing", "", f"Table line {line_number} refers to unavailable scan {scan:03}.")
                elif not 1 <= first <= last <= len(page_lines[scan]):
                    issue("standing_locator_out_of_range", "",
                          f"Table line {line_number}: scan {scan:03} lines {first}–{last}, available 1–{len(page_lines[scan])}.")
                else:
                    source_parts.extend(page_lines[scan][first - 1:last])
            if source_parts:
                source_text = source_plain(" ".join(source_parts))
                for quotation in re.findall(r"“([^”]+)”", cells[1]):
                    standing_quotes_checked += 1
                    quoted = source_plain(quotation)
                    if quoted not in source_text:
                        issue("standing_literal_phrase_review", "",
                              f"Table line {line_number}, locus {cells[0]}: quoted phrase {quotation!r} is not a literal match after removing editorial wrappers.", warning=True)
        matches = list(re.finditer(r"^#{1,6}\s+(" + ID_PATTERN + r")(?=[\s.:—–-]|$).*$", rendered, re.M))
        rendered_ids = [match.group(1) for match in matches]
        rendered_count = len(rendered_ids)
        for identifier, count in Counter(rendered_ids).items():
            if count != 1:
                issue("rendered_duplicate_id", identifier, f"Rendered note heading occurs {count} times.")
        for identifier in sorted(set(ids) - set(rendered_ids)):
            issue("rendered_id_missing", identifier, "Manifest note has no matching rendered heading.", warning=not complete)
        for identifier in sorted(set(rendered_ids) - set(ids)):
            issue("rendered_id_extra", identifier, "Rendered note heading is absent from the manifest.")
        sections = {}
        for i, match in enumerate(matches):
            end = matches[i + 1].start() if i + 1 < len(matches) else len(rendered)
            sections[match.group(1)] = normalized(rendered[match.end():end])
        for note in notes:
            identifier = str(note.get("id", ""))
            if identifier not in sections:
                continue
            if normalized(str(note.get("body", ""))) not in sections[identifier]:
                issue("rendered_body_differs", identifier, "Manifest body is not preserved verbatim, allowing whitespace reflow, in its rendered note.")
            if str(note.get("kind", "")).startswith("own idea"):
                confidence = normalized(str(note.get("confidence", "")))
                if confidence and confidence not in sections[identifier]:
                    issue("rendered_confidence_missing", identifier, "Own-idea confidence/reason is not preserved in its rendered note.")

    search_path = root / "records/context_search.json"
    coverage_count = 0
    if not search_path.is_file():
        issue("context_search_pending", "", "Per-note context search record does not yet exist.", warning=not complete)
    else:
        try:
            search_data = json.loads(search_path.read_text(encoding="utf-8"))
            records = find_note_records(search_data)
            for identifier in ids:
                if identifier not in records:
                    issue("context_note_missing", identifier, "No per-note context search record found.")
                    continue
                coverage, empty = search_coverage(records[identifier])
                missing = set(SOURCE_FILES) - set(coverage)
                if missing:
                    issue("context_source_missing", identifier, "No search with nonempty query terms recorded for: " + ", ".join(sorted(missing)))
                else:
                    coverage_count += 1
                if empty:
                    issue("context_empty_queries", identifier, "Source entries lack recorded nonempty search terms: " + ", ".join(sorted(empty)))
        except (OSError, json.JSONDecodeError) as exc:
            issue("context_search_unreadable", "", str(exc))

    return {"ok": not errors, "mode": "complete" if complete else "construction",
            "counts": {"manifest_notes": len(notes), "unique_ids": len(set(ids)), "rendered_note_headings": rendered_count,
                       "notes_with_all_three_context_sources": coverage_count,
                       "numeric_line_locator_endpoints_checked": checked_numeric_locators,
                       "markdown_tables": table_count, "markdown_table_rows": table_rows,
                       "standing_source_quotations_checked": standing_quotes_checked,
                       "body_sentence_distribution": dict(sorted(Counter(sentence_counts.values()).items())),
                       "kinds": dict(sorted(kinds.items()))},
            "errors": errors, "warnings": warnings,
            "scope": "Read-only structural review. Empty search results are valid when query terms and all source files are explicitly recorded. Sentence/quote checks do not verify mathematical content or the fidelity of quotations."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, nargs="?", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--complete", action="store_true", help="Require final rendered notes and context-search coverage")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = review(args.root.resolve(), args.complete)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("PASS" if result["ok"] else "FAIL", f"({result.get('mode', 'manifest')})")
        print(json.dumps(result["counts"], ensure_ascii=False, indent=2))
        for category in ("errors", "warnings"):
            for item in result[category]:
                print(f"{category[:-1].upper()} {item['note']} [{item['kind']}]: {item['message']}")
        print(result.get("scope", ""))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
