#!/usr/bin/env python3
r"""Read-only mechanical audit of research notes, plus actual context searches.

Default invocation (safe while notes are still a draft):
    python scripts/audit_research_notes.py

After the root has finished writing the notes:
    python scripts/audit_research_notes.py --final

The script reads the notes and all supplied .md/.tex/.txt/.rst/.csv/.tsv
context sources. It never opens PDFs or images and never writes notes,
context sources, or frozen TeX. It writes only two JSON reports:
    records/research_notes_audit.json
    records/note_context_searches.json

Every comment of the form
    <!-- context-query G01: graphe|Hom\(|Poincar -->
is searched against every discovered context text file. Searches use
Python regular expressions, Unicode, case-insensitive by default, one
physical source line at a time. There is no accent folding or TeX decoding.
All matching lines are counted; only the first --max-matches-per-file
examples per query/file are retained, each capped at 160 characters.
Negative per-file results are explicit. No complete supplied file is copied.

Sentence counts are heuristic warnings, not editorial judgments. Code,
math, common abbreviations, decimals, initials and links are masked before
counting, but quoted fragments and unusual notation can still mislead.
Broad heading ranges may span excluded scans without being invalid;
an explicitly listed unavailable single scan is an error.

Exit 0 means no structural errors in this snapshot (warnings may remain);
exit 1 means structural errors, or warnings with --strict-warnings;
exit 2 means an input/configuration failure. Without --final the report is
always explicitly a draft audit and cannot certify completion.
"""

from __future__ import annotations

import argparse
import bisect
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
from typing import Any


WORK_DEFAULT = Path(__file__).resolve().parents[1]
SCAN_MIN, SCAN_MAX = 87, 132
EXCLUDED_SCANS = {105, 110, 119, 125, 130}
EXPECTED_SCANS = set(range(SCAN_MIN, SCAN_MAX + 1)) - EXCLUDED_SCANS
TEXT_SUFFIXES = {".md", ".markdown", ".tex", ".txt", ".rst", ".csv", ".tsv"}
ID_SOURCE = r"[A-Z]{1,8}[0-9]{2,4}(?:[a-z])?"
ID_RE = re.compile(r"\b(" + ID_SOURCE + r")\b")
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$", re.MULTILINE)
NOTE_START_RE = re.compile(r"^(" + ID_SOURCE + r")(?=\s|[—–:.-]|$)")
QUERY_RE = re.compile(
    r"<!--\s*context-query\s+([A-Za-z][A-Za-z0-9_.-]*)\s*:\s*(.*?)\s*-->",
    re.IGNORECASE | re.DOTALL,
)
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
PLACEHOLDER_RE = re.compile(
    r"\b(?:TODO|FIXME|TBD)\b|\b[A-Z0-9_]*INSERT[A-Z0-9_]*\b"
)
SCAN_LIST_RE = re.compile(
    r"\bscans?\s+("
    r"\d{1,3}(?:\s*[–—-]\s*\d{1,3})?"
    r"(?:\s*(?:,\s*(?:(?:and|et)\s+)?|(?:and|et)\s+)"
    r"\d{1,3}(?:\s*[–—-]\s*\d{1,3})?)*"
    r")",
    re.IGNORECASE,
)
SCAN_ITEM_RE = re.compile(r"(\d{1,3})(?:\s*[–—-]\s*(\d{1,3}))?")
CONTEXT_COTES = r"(?:14|16|47|54|44)"
BACKTICK = chr(96)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def clip(value: str, limit: int = 160) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    return value if len(value) <= limit else value[: limit - 1] + "…"


def normalized_heading(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip()).casefold()


def line_offsets(text: str) -> list[int]:
    return [0] + [m.end() for m in re.finditer("\n", text)]


def line_number(offsets: list[int], position: int) -> int:
    return bisect.bisect_right(offsets, position)


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=path.parent,
        prefix=path.name + ".", suffix=".tmp", delete=False
    ) as stream:
        temp_path = Path(stream.name)
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    temp_path.replace(path)


def source_role(path: Path) -> str:
    name = path.name.lower()
    if name == "readme.md":
        return "README"
    if name == "results_state.md":
        return "RESULTS_STATE"
    if name.endswith("_transcription.tex"):
        return "C"
    if name.endswith("_notes.md"):
        return "CN"
    if name.endswith("_doubts.md"):
        return "doubts"
    return "additional_text"


def inline_anchors(line: str) -> list[dict[str, Any]]:
    """Extract explicit context locations without inferring a missing cote."""
    found: list[dict[str, Any]] = []
    patterns = [
        re.compile(
            rf"\b({CONTEXT_COTES})[:/](\d{{1,3}})"
            r"(?:\s*[–—-]\s*(\d{1,3}))?"
        ),
        re.compile(
            r"\bcote\s+(\d+)\s*,?\s*scans?\s+(\d+)"
            r"(?:\s*[–—-]\s*(\d+))?", re.IGNORECASE
        ),
        re.compile(r"^\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|"),
    ]
    for pattern in patterns:
        for match in pattern.finditer(line):
            anchor = {"cote": int(match.group(1)), "scan": int(match.group(2))}
            if match.lastindex and match.lastindex >= 3 and match.group(3):
                anchor["scan_end"] = int(match.group(3))
            if anchor not in found:
                found.append(anchor)
    return found[:6]


def source_lines(text: str, suffix: str) -> list[dict[str, Any]]:
    cote = scan = None
    heading_anchor = None
    heading = None
    result = []
    for number, line in enumerate(text.splitlines(), 1):
        c = re.search(r"\\cotefile\{(\d+)\}", line)
        s = re.search(r"\\scanpage\{(\d+)\}", line)
        if c:
            cote, scan = int(c.group(1)), None
        if s:
            scan = int(s.group(1))
        direct = inline_anchors(line)
        if re.match(r"^#{1,6}\s", line):
            heading = clip(line)
            heading_anchor = direct[0] if direct else None
        elif re.match(r"^\*\*Location:\*\*", line) and direct:
            heading_anchor = direct[0]
        anchor = None
        if suffix == ".tex" and cote is not None and scan is not None:
            anchor = {"cote": cote, "scan": scan, "origin": "tex_markers"}
        elif direct:
            anchor = dict(direct[0], origin="explicit_on_line")
        elif heading_anchor:
            anchor = dict(heading_anchor, origin="preceding_heading_or_location")
        register = re.search(
            r"\*\*((?:LM\d+|LM\d+_PUSH|WG\d*|FLAGGED_\d+)[^*]{0,70})\*\*",
            line,
        )
        result.append({
            "line": number,
            "text": line,
            "anchor": anchor,
            "explicit_anchors": direct,
            "heading": heading,
            "register_id": register.group(1) if register else None,
        })
    return result


def discover_sources(context: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    sources, excluded = [], []
    for path in sorted(p for p in context.rglob("*") if p.is_file()):
        relative = str(path.relative_to(context))
        if path.suffix.lower() not in TEXT_SUFFIXES:
            excluded.append({
                "path": relative,
                "reason": "non-text/PDF/image excluded from this lexical audit; contents not opened by this script",
                "bytes": path.stat().st_size,
            })
            continue
        raw = path.read_bytes()
        text = raw.decode("utf-8-sig")
        sources.append({
            "path": relative,
            "absolute_path": str(path),
            "role": source_role(path),
            "sha256": digest(raw),
            "bytes": len(raw),
            "line_count": len(text.splitlines()),
            "_lines": source_lines(text, path.suffix.lower()),
        })
    return sources, excluded


def sentence_estimate(body: str) -> int:
    text = COMMENT_RE.sub(" ", body)
    fence = re.compile(
        rf"(?ms)^[ \t]*(?:{BACKTICK}{{3,}}|~{{3,}}).*?"
        rf"^[ \t]*(?:{BACKTICK}{{3,}}|~{{3,}})[ \t]*$"
    )
    text = fence.sub(" ", text)
    text = re.sub(rf"(?s){BACKTICK}+.*?{BACKTICK}+", " CODE ", text)
    for pattern in (
        r"(?s)\$\$.*?\$\$", r"(?s)\\\[.*?\\\]",
        r"(?s)\\\(.*?\\\)", r"(?s)(?<!\\)\$(?!\$).*?(?<!\\)\$"
    ):
        text = re.sub(pattern, " MATH ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"https?://\S+", " URL ", text)
    abbreviations = re.compile(
        r"\b(?:e\.g\.|i\.e\.|cf\.|etc\.|vs\.|viz\.|ibid\.|"
        r"Thm\.|Prop\.|Lem\.|Def\.|No\.|Nos\.|p\.|pp\.|n\.|"
        r"vol\.|Fig\.|Dr\.)", re.IGNORECASE
    )
    text = abbreviations.sub(lambda m: m.group().replace(".", "·"), text)
    text = re.sub(r"\b(?:[A-Z]\.){2,}", lambda m: m.group().replace(".", "·"), text)
    text = re.sub(r"(?<=\d)\.(?=\d)", "·", text)
    text = re.sub(r"\b([A-Z])\.(?=\d)", r"\1·", text)
    text = re.sub(r"\b([A-Z])\.(?=\s*[A-Z][a-z])", r"\1·", text)
    pieces = re.split(r"""[.!?]+(?:["'”’)\]*_}]+)?(?=\s+|$)""", text)
    return sum(bool(re.search(r"[A-Za-zÀ-ž]", part)) for part in pieces)


def heading_scan_refs(title: str) -> list[dict[str, Any]]:
    cotes = list(re.finditer(r"\bcote\s+(\d+)", title, re.IGNORECASE))
    refs = []
    for match in SCAN_LIST_RE.finditer(title):
        preceding = [c for c in cotes if c.start() < match.start()]
        cote = int(preceding[-1].group(1)) if preceding else 14
        for item in SCAN_ITEM_RE.finditer(match.group(1)):
            first = int(item.group(1))
            last = int(item.group(2)) if item.group(2) else first
            refs.append({
                "cote": cote, "first": first, "last": last,
                "range": item.group(2) is not None,
                "literal": item.group(0),
            })
    for match in re.finditer(
        r"\b14[:/](\d{1,3})(?:\s*[–—-]\s*(\d{1,3}))?", title
    ):
        refs.append({
            "cote": 14, "first": int(match.group(1)),
            "last": int(match.group(2) or match.group(1)),
            "range": match.group(2) is not None, "literal": match.group(0),
        })
    return refs


def is_external_id(text: str, position: int) -> bool:
    left = re.sub(r"[*_" + BACKTICK + r"]", "", text[max(0, position - 60):position])
    return bool(re.search(
        r"\b(?:CN|R|WG\d*|LM\d*(?:_PUSH)?|Doubts?)\s+"
        r"(?:WG\d*\s+)?$", left, re.IGNORECASE
    ))


def audit(args: argparse.Namespace) -> tuple[dict[str, Any], dict[str, Any]]:
    notes_path = args.notes.resolve()
    raw_notes = notes_path.read_bytes()
    text = raw_notes.decode("utf-8-sig")
    offsets = line_offsets(text)
    issues: list[dict[str, Any]] = []

    def add(severity: str, code: str, message: str, **details: Any) -> None:
        issues.append(dict(severity=severity, code=code, message=message, **details))

    headings = [
        {"level": len(m.group(1)), "title": m.group(2), "start": m.start(),
         "body_start": m.end(), "line": line_number(offsets, m.start())}
        for m in HEADING_RE.finditer(text)
    ]
    grouped_headings = defaultdict(list)
    for heading in headings:
        grouped_headings[normalized_heading(heading["title"])].append(heading["line"])
    for title, lines in grouped_headings.items():
        if len(lines) > 1:
            add("error", "duplicate_heading", "Repeated Markdown heading.",
                heading=clip(title), lines=lines)

    notes = []
    for index, heading in enumerate(headings):
        identifier = NOTE_START_RE.match(heading["title"])
        if not identifier:
            continue
        end = next(
            (h["start"] for h in headings[index + 1:] if h["level"] <= heading["level"]),
            len(text),
        )
        note = dict(heading, id=identifier.group(1), end=end)
        note["body"] = text[note["body_start"]:end]
        notes.append(note)
    if not notes:
        add("error", "no_note_headings", "No note headings matching the documented ID format.")
    id_lines = defaultdict(list)
    for note in notes:
        id_lines[note["id"]].append(note["line"])
    for identifier, lines in id_lines.items():
        if len(lines) > 1:
            add("error", "duplicate_note_id", "Note ID is defined more than once.",
                note_id=identifier, lines=lines)

    for match in PLACEHOLDER_RE.finditer(text):
        add("error", "placeholder", "Unfilled INSERT/TODO/FIXME/TBD placeholder.",
            line=line_number(offsets, match.start()), token=match.group())

    markers = []
    for ordinal, match in enumerate(QUERY_RE.finditer(text), 1):
        owner = next((n for n in notes if n["start"] <= match.start() < n["end"]), None)
        marker = {
            "query_index": ordinal, "note_id": match.group(1),
            "regex": match.group(2).strip(),
            "marker_line": line_number(offsets, match.start()),
            "owner_note_id": owner["id"] if owner else None,
            "owner_heading_line": owner["line"] if owner else None,
        }
        markers.append(marker)
        if owner is None:
            add("error", "orphan_context_query", "Context query is outside a note.",
                note_id=marker["note_id"], line=marker["marker_line"])
        elif marker["note_id"] != owner["id"]:
            add("error", "context_query_id_mismatch", "Marker ID differs from its note heading.",
                note_id=owner["id"], marker_id=marker["note_id"], line=marker["marker_line"])
    all_context_comment_starts = list(re.finditer(r"<!--\s*context-query\b", text, re.I))
    if len(all_context_comment_starts) != len(markers):
        add("error", "malformed_context_query", "Some context-query comments could not be parsed.",
            starts=len(all_context_comment_starts), parsed=len(markers))
    for identifier, count in Counter(m["note_id"] for m in markers).items():
        if count > 1:
            add("error", "duplicate_context_query_id", "More than one query uses this note ID.",
                note_id=identifier, count=count)

    known_ids = set(id_lines)
    known_prefixes = {re.match(r"[A-Z]+", n).group() for n in known_ids}
    cross_refs = []
    note_summaries = []
    for note in notes:
        own_markers = [m for m in markers if m["owner_heading_line"] == note["line"]]
        correct = [m for m in own_markers if m["note_id"] == note["id"]]
        if not correct:
            add("error", "missing_context_query", "Note has no correctly labelled context-query.",
                note_id=note["id"], line=note["line"])
        body_without_comments = COMMENT_RE.sub(" ", note["body"])
        if not body_without_comments.strip():
            add("error", "empty_note", "Note has no prose outside its comments.",
                note_id=note["id"], line=note["line"])
        estimate = sentence_estimate(note["body"])
        if estimate > 4:
            add("warning", "sentence_count_over_four",
                "Approximate sentence count exceeds four; review formulas, quotations and abbreviations.",
                note_id=note["id"], line=note["line"], estimate=estimate)

        refs = heading_scan_refs(note["title"])
        own_refs = [r for r in refs if r["cote"] == 14]
        if not own_refs:
            add("warning", "no_heading_scan_reference",
                "No cote-14 scan location was parsed from this note heading.",
                note_id=note["id"], line=note["line"])
        for ref in own_refs:
            first, last = ref["first"], ref["last"]
            if last < first or first < SCAN_MIN or last > SCAN_MAX:
                add("error", "invalid_heading_scan_range", "Heading scan reference is out of range.",
                    note_id=note["id"], line=note["line"], reference=ref)
            elif not ref["range"] and first not in EXPECTED_SCANS:
                add("error", "unavailable_heading_scan",
                    "A singly listed heading scan was excluded from the supplied set.",
                    note_id=note["id"], line=note["line"], reference=ref)
            elif ref["range"]:
                omitted = sorted(EXCLUDED_SCANS.intersection(range(first, last + 1)))
                if omitted:
                    add("info", "broad_heading_range",
                        "Valid broad range spans excluded scans; this is not an assertion that each was supplied.",
                        note_id=note["id"], line=note["line"], reference=ref,
                        excluded_within_range=omitted)

        # Leave positions intact when masking comments/code to retain exact line numbers.
        body = COMMENT_RE.sub(lambda m: " " * len(m.group()), note["body"])
        body = re.sub(
            rf"(?s){BACKTICK}+.*?{BACKTICK}+",
            lambda m: " " * len(m.group()), body
        )
        for match in ID_RE.finditer(body):
            target = match.group(1)
            if is_external_id(body, match.start()):
                continue
            prefix = re.match(r"[A-Z]+", target).group()
            left = re.sub(r"[*_]", "", body[max(0, match.start() - 30):match.start()])
            explicit = bool(re.search(r"\b(?:notes?|entries|entry|items?|see)\s*$", left, re.I))
            if target not in known_ids and prefix not in known_prefixes and not explicit:
                continue
            reference = {
                "from_note_id": note["id"], "target_id": target,
                "line": line_number(offsets, note["body_start"] + match.start()),
                "exists": target in known_ids,
            }
            cross_refs.append(reference)
            if target not in known_ids:
                add("error" if explicit else "warning", "missing_note_cross_reference",
                    "Possible local note reference has no matching heading; external register IDs may need review.",
                    **reference)
        for match in re.finditer(r"\]\(#([A-Za-z][A-Za-z0-9-]*)\)", body):
            target = re.match(r"(" + ID_SOURCE + r")(?:-|$)", match.group(1).upper())
            if target and target.group(1) not in known_ids:
                add("error", "missing_linked_note_id", "Markdown note link targets an undefined note ID.",
                    note_id=note["id"], target_id=target.group(1),
                    line=line_number(offsets, note["body_start"] + match.start()))
        note_summaries.append({
            "note_id": note["id"], "heading_line": note["line"],
            "heading": note["title"], "approximate_sentences": estimate,
            "context_query_count": len(correct), "heading_scan_refs": refs,
        })

    sources, excluded = discover_sources(args.context_dir.resolve())
    roles = {s["role"] for s in sources}
    for role in {"C", "CN", "doubts", "README", "RESULTS_STATE"} - roles:
        add("error", "missing_context_source", "A required supplied context role was not found.", role=role)
    flags = 0 if args.case_sensitive else re.IGNORECASE
    query_results = []
    for marker in markers:
        entry = dict(marker)
        entry["files"] = []
        try:
            if not marker["regex"]:
                raise re.error("empty context-query regular expression")
            regex = re.compile(marker["regex"], flags)
        except re.error as exc:
            entry["regex_error"] = str(exc)
            add("error", "invalid_context_regex", "Context-query regex could not be compiled.",
                note_id=marker["note_id"], line=marker["marker_line"], detail=str(exc))
            for source in sources:
                entry["files"].append({
                    "path": source["path"], "role": source["role"],
                    "status": "not_searched_invalid_regex", "matching_lines": None,
                    "match_count": None, "matches": [],
                })
            query_results.append(entry)
            continue
        for source in sources:
            matching_lines, match_count, matches = 0, 0, []
            for line in source["_lines"]:
                line_matches = list(regex.finditer(line["text"]))
                if not line_matches:
                    continue
                matching_lines += 1
                match_count += len(line_matches)
                if len(matches) < args.max_matches_per_file:
                    first_match = line_matches[0]
                    # Centre the excerpt around the first hit when a line is long.
                    begin = max(0, first_match.start() - 55)
                    raw_excerpt = line["text"][begin:begin + 158]
                    excerpt = ("…" if begin else "") + raw_excerpt
                    if begin + 158 < len(line["text"]):
                        excerpt += "…"
                    matches.append({
                        "line": line["line"], "anchor": line["anchor"],
                        "explicit_anchors": line["explicit_anchors"],
                        "register_id": line["register_id"],
                        "excerpt": clip(excerpt),
                    })
            entry["files"].append({
                "path": source["path"], "role": source["role"],
                "status": "matched" if matching_lines else "negative",
                "matching_lines": matching_lines, "match_count": match_count,
                "reported_matches": len(matches),
                "omitted_matching_lines": matching_lines - len(matches),
                "matches": matches,
            })
        entry["total_matching_lines"] = sum(f["matching_lines"] for f in entry["files"])
        entry["negative_in_all_sources"] = entry["total_matching_lines"] == 0
        query_results.append(entry)

    inventory = [{k: v for k, v in source.items() if not k.startswith("_")} for source in sources]
    notes_hash = digest(raw_notes)
    if digest(notes_path.read_bytes()) != notes_hash:
        add("error", "notes_changed_during_run", "Notes changed during the audit; rerun after writing finishes.")
    for source in sources:
        if digest(Path(source["absolute_path"]).read_bytes()) != source["sha256"]:
            add("error", "context_changed_during_run", "Context source changed during the search.",
                path=source["path"])
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    errors = sum(i["severity"] == "error" for i in issues)
    warnings = sum(i["severity"] == "warning" for i in issues)
    status = (
        "draft_snapshot_only" if not args.final else
        ("final_snapshot_has_structural_errors" if errors else "final_mechanical_checks_passed")
    )
    common = {
        "generated_at_utc": now,
        "stage": "final_requested_by_caller" if args.final else "draft",
        "status": status,
        "notes_path": str(notes_path), "notes_sha256": notes_hash,
        "context_dir": str(args.context_dir.resolve()),
        "context_text_source_count": len(sources),
        "context_source_inventory": inventory,
        "excluded_context_files": excluded,
        "note_count": len(notes), "query_count": len(markers),
        "limits": {
            "no_mathematical_or_reading_validation": True,
            "sentence_count_is_heuristic": True,
            "regex_matches_are_leads_not_verified_parallels": True,
            "no_frozen_transcription_writes": True,
            "draft_is_not_completion": not args.final,
        },
    }
    main_report = dict(common)
    main_report.update({
        "summary": {
            "errors": errors, "warnings": warnings,
            "info": sum(i["severity"] == "info" for i in issues),
            "issue_counts": dict(Counter(i["code"] for i in issues)),
        },
        "issues": issues, "notes": note_summaries, "local_cross_references": cross_refs,
    })
    searches = dict(common)
    searches.update({
        "search_semantics": {
            "engine": "Python stdlib re", "case_sensitive": args.case_sensitive,
            "unit": "one physical line", "unicode": True,
            "accent_folding": False, "tex_decoding": False,
            "all_lines_searched": True, "all_matches_counted": True,
            "maximum_reported_lines_per_query_per_file": args.max_matches_per_file,
            "maximum_excerpt_characters": 160,
            "negative_status_means_no_regex_match_not_no_conceptual_parallel": True,
        },
        "queries": query_results,
    })
    return main_report, searches


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--notes", type=Path, default=WORK_DEFAULT / "MPL_14_087-132_notes.md")
    parser.add_argument("--context-dir", type=Path, default=WORK_DEFAULT.parent / "context")
    parser.add_argument("--records-dir", type=Path, default=WORK_DEFAULT / "records")
    parser.add_argument("--final", action="store_true",
                        help="Caller declares writing finished; label this snapshot as a final mechanical audit.")
    parser.add_argument("--strict-warnings", action="store_true",
                        help="Exit 1 for heuristic warnings as well as structural errors.")
    parser.add_argument("--case-sensitive", action="store_true",
                        help="Use case-sensitive regex searches (default is case-insensitive Unicode).")
    parser.add_argument("--max-matches-per-file", type=int, default=6,
                        help="Maximum retained matching lines per query/source; all hits are still counted.")
    args = parser.parse_args()
    if args.max_matches_per_file < 1 or args.max_matches_per_file > 100:
        parser.error("--max-matches-per-file must be between 1 and 100")
    if not args.context_dir.is_dir():
        parser.error("--context-dir does not exist")
    try:
        report, searches = audit(args)
        audit_path = args.records_dir / "research_notes_audit.json"
        searches_path = args.records_dir / "note_context_searches.json"
        atomic_json(audit_path, report)
        atomic_json(searches_path, searches)
    except (OSError, UnicodeError) as exc:
        print(json.dumps({"status": "input_or_output_error", "error": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps({
        "status": report["status"], "note_count": report["note_count"],
        "query_count": report["query_count"],
        "context_text_source_count": report["context_text_source_count"],
        "summary": report["summary"], "notes_sha256": report["notes_sha256"],
        "audit_report": str(audit_path.resolve()), "context_search_report": str(searches_path.resolve()),
        "next_step": "Rerun with --final after root finishes the notes." if not args.final else
                     "Review any warnings; this checks mechanics and searches, not mathematical truth.",
    }, ensure_ascii=False, indent=2))
    return int(bool(report["summary"]["errors"] or
                    (args.strict_warnings and report["summary"]["warnings"])))


if __name__ == "__main__":
    raise SystemExit(main())
