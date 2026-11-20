#!/usr/bin/env python3
"""Structural checks for SP60_CW_71; no compilation, OCR, or content decisions.

Usage:
    python3 scripts/validate_package.py OUTPUT_DIRECTORY
    python3 scripts/validate_package.py OUTPUT_DIRECTORY --zip FINAL.zip
    python3 scripts/validate_package.py OUTPUT_DIRECTORY --incomplete

The script reads only the deliverables named below. It never reads source
images or witnesses. A successful run certifies structural consistency, not
the correctness, completeness, or palaeographic accuracy of a transcription.

Assembly convention: page files are retained byte for byte in numeric order.
Whitespace may separate files, and one leading \\cotefile{71} may be added when
it is not already at the beginning of the first page. No other additions,
omissions, or textual substitutions are allowed in the combined fragment.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import io
import re
import sys
import unicodedata
import zipfile
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path, PurePosixPath


PREFIX = "SP60_CW_71"
SCANS = tuple(range(38, 49))
H_TEXT_SCANS = {38, 47, 48}
COLLATION_HEADER = [
    "folder", "their_page", "our_scan", "line", "their_reading",
    "codex_reading", "final_reading", "scan_shows", "kind", "marked_in_H",
    "confidence",
]
INVENTORY_HEADER = [
    "scan", "sheet_kind", "hand", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
CHECK_HEADER = ["statement_id", "date", "who", "type", "outcome"]
DECISION_HEADER = [
    "scan", "id", "place", "C", "H", "final", "scan_shows", "confidence",
    "against_C", "against_H", "kind", "marked_in_H", "record_type",
    "consequential",
]
DOUBT_HEADER = [
    "scan", "place", "reading", "alternatives", "confidence", "status", "reason",
]
ACKNOWLEDGEMENT_HEADER = [
    "scan", "tex_line", "page_sha256", "recorded_utc", "who", "acknowledgement",
]
ERROR_SHEET_CATEGORIES = [
    ("Symbols and indices", "misread symbol or index"),
    ("Words", "misread word"),
    ("Omissions", "omission"),
    ("Drawings and diagrams", "drawing or diagram"),
    ("Readable ink left as illegible", r"readable ink left as \ill{}"),
    ("Insertion or placement", "insertion or placement"),
    ("Deletion state", "deletion state (struck given live or live given struck)"),
    ("Abbreviation or spelling normalization", "abbreviation expanded or spelling modernised"),
    ("Text not on the page", "text not on the page"),
    ("Other", "other"),
]
COLLATION_KINDS = {
    "misread word", "misread symbol or index", "omission",
    "text not on the page",
    "deletion state (struck given live or live given struck)",
    "insertion or placement",
    "abbreviation expanded or spelling modernised",
    r"readable ink left as \ill{}", "drawing or diagram", "other",
}
SHEET_KINDS = {
    "text", "reused_typed", "typescript", "letter", "list",
    "cancelled_draft", "cover",
}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion",
    "deletion",
}
IMAGE_SUFFIXES = {
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".tif", ".tiff", ".bmp",
    ".svg", ".heic", ".avif", ".jp2",
}
MANDATORY = [
    f"{PREFIX}_transcription.tex", f"{PREFIX}_changes.md",
    f"{PREFIX}_collation.tsv", f"{PREFIX}_doubts.md",
    f"{PREFIX}_inventory.csv", f"{PREFIX}_notes.md", "CHECK_EVENTS.tsv",
    "progress.log", f"{PREFIX}_sheet_feedback.md", f"{PREFIX}_hand_log.md",
]


@dataclass
class Findings:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    checks: int = 0
    metadata: dict = field(default_factory=dict)

    def require(self, condition: bool, message: str) -> None:
        self.checks += 1
        if not condition:
            self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)


def page_name(scan: int) -> str:
    folder = "J71-05" if scan <= 42 else "J71-06"
    return f"{folder}_71_scan{scan:03}.tex"


def line_at(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def braced_argument(text: str, start: int) -> str | None:
    """Extract a literal balanced macro argument; do not expand or interpret it."""
    i = start
    while i < len(text) and text[i].isspace():
        i += 1
    if i >= len(text) or text[i] != "{":
        return None
    first = i + 1
    depth = 1
    i += 1
    while i < len(text):
        if text[i] == "\\":
            i += 2  # an escaped brace or percent sign is not structural
            continue
        if text[i] == "%":
            end = text.find("\n", i)
            i = len(text) if end < 0 else end + 1
            continue
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[first:i]
        i += 1
    return None


def lex_tex(text: str) -> tuple[list[tuple[str, str, int]], list[str]]:
    """Return structural tokens, ignoring comments and escaped punctuation.

    Control words are consumed whole, so \\% is not a comment and the brace in
    \\{ is not a group. \\verb and common verbatim environments are skipped.
    This is deliberately a lexer, not a TeX macro-expansion engine.
    """
    tokens: list[tuple[str, str, int]] = []
    problems: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c == "%":
            end = text.find("\n", i)
            i = n if end < 0 else end + 1
            continue
        if c == "\\":
            start = i
            i += 1
            if i == n:
                problems.append(f"line {line_at(text, start)}: trailing backslash")
                break
            if text[i].isalpha() or text[i] == "@":
                j = i + 1
                while j < n and (text[j].isalpha() or text[j] == "@"):
                    j += 1
                command = text[i:j]
                i = j
                if command == "verb":
                    if i < n and text[i] == "*":
                        i += 1
                    if i >= n or text[i] in "\r\n":
                        problems.append(f"line {line_at(text, start)}: malformed verb")
                        continue
                    delim = text[i]
                    end = text.find(delim, i + 1)
                    newline = text.find("\n", i + 1)
                    if end < 0 or (newline >= 0 and newline < end):
                        problems.append(f"line {line_at(text, start)}: unclosed verb")
                        i = n if newline < 0 else newline + 1
                    else:
                        i = end + 1
                    continue
                if command in {"begin", "end"}:
                    match = re.match(r"\s*\{([A-Za-z@*][A-Za-z0-9@*_-]*)\}", text[i:])
                    if not match:
                        problems.append(
                            f"line {line_at(text, start)}: malformed {command}"
                        )
                        continue
                    env = match.group(1)
                    tokens.append((command, env, start))
                    i += match.end()
                    if command == "begin" and env in {"verbatim", "verbatim*", "Verbatim"}:
                        end_token = "\\end{" + env + "}"
                        end = text.find(end_token, i)
                        if end < 0:
                            problems.append(
                                f"line {line_at(text, start)}: unclosed {env}"
                            )
                            i = n
                        else:
                            tokens.append(("end", env, end))
                            i = end + len(end_token)
                    continue
                if command in {"cotefile", "scanpage", "documentclass"}:
                    match = re.match(r"\s*\{([^{}]*)\}", text[i:])
                    if match:
                        tokens.append((command, match.group(1), start))
                    else:
                        tokens.append((command, "", start))
                if command in {"unsure", "illegible"}:
                    argument = braced_argument(text, i)
                    if argument is not None:
                        tokens.append((command, argument, start))
                continue
            symbol = text[i]
            if symbol in "[]()":
                tokens.append(("math_control", symbol, start))
            i += 1
            continue
        if c in "{}":
            tokens.append(("brace", c, i))
        elif c == "$":
            delimiter = "$$" if text[i:i + 2] == "$$" else "$"
            tokens.append(("dollar", delimiter, i))
            i += len(delimiter)
            continue
        i += 1
    return tokens, problems


def validate_tex(name: str, text: str, findings: Findings) -> list[tuple[str, str, int]]:
    tokens, lexical_problems = lex_tex(text)
    for problem in lexical_problems:
        findings.require(False, f"{name}: {problem}")
    braces: list[int] = []
    envs: list[tuple[str, int]] = []
    controls: list[tuple[str, int]] = []
    dollar: tuple[str, int] | None = None
    for kind, value, pos in tokens:
        loc = f"{name}:{line_at(text, pos)}"
        if kind == "brace":
            if value == "{":
                braces.append(pos)
            elif braces:
                braces.pop()
            else:
                findings.require(False, f"{loc}: unmatched closing brace")
        elif kind == "begin":
            envs.append((value, pos))
        elif kind == "end":
            if not envs:
                findings.require(False, f"{loc}: unmatched end of {value}")
            elif envs[-1][0] != value:
                findings.require(False, f"{loc}: end of {value} while {envs[-1][0]} is open")
            else:
                envs.pop()
        elif kind == "math_control":
            if value in "[(":
                controls.append((value, pos))
            else:
                expected = "[" if value == "]" else "("
                if not controls or controls[-1][0] != expected:
                    findings.require(False, f"{loc}: unmatched \\{value}")
                else:
                    controls.pop()
        elif kind == "dollar":
            if dollar is None:
                dollar = (value, pos)
            elif dollar[0] == value:
                dollar = None
            else:
                findings.require(False, f"{loc}: mixed {dollar[0]} and {value} math delimiters")
        elif kind == "documentclass":
            findings.require(False, f"{loc}: documentclass in a fragment")
    for pos in braces:
        findings.require(False, f"{name}:{line_at(text, pos)}: unclosed brace")
    for env, pos in envs:
        findings.require(False, f"{name}:{line_at(text, pos)}: unclosed environment {env}")
    for control, pos in controls:
        findings.require(False, f"{name}:{line_at(text, pos)}: unclosed \\{control}")
    if dollar:
        findings.require(False, f"{name}:{line_at(text, dollar[1])}: unclosed {dollar[0]}")
    findings.checks += 4
    return tokens


def read_utf8(path: Path, findings: Findings) -> str | None:
    try:
        return path.read_bytes().decode("utf-8")
    except (OSError, UnicodeError) as exc:
        findings.require(False, f"cannot read {path.name} as UTF-8: {exc}")
        return None


def read_table(path: Path, header: list[str], delimiter: str,
               findings: Findings, required: bool) -> list[dict[str, str]]:
    if not path.is_file():
        if required:
            findings.require(False, f"missing {path.name}")
        return []
    text = read_utf8(path, findings)
    if text is None:
        return []
    try:
        reader = csv.DictReader(io.StringIO(text), delimiter=delimiter, strict=True)
        findings.require(reader.fieldnames == header,
                         f"{path.name}: header must be {header!r}; got {reader.fieldnames!r}")
        if reader.fieldnames != header:
            return []
        rows = []
        for row in reader:
            findings.require(None not in row and all(v is not None for v in row.values()),
                             f"{path.name}: malformed row ending at physical line {reader.line_num}")
            if None not in row and all(v is not None for v in row.values()):
                rows.append(row)
        return rows
    except csv.Error as exc:
        findings.require(False, f"{path.name}: CSV/TSV parse error: {exc}")
        return []


def numeric(value: str, name: str, findings: Findings) -> int | None:
    try:
        return int(value)
    except ValueError:
        findings.require(False, f"{name}: expected integer, got {value!r}")
        return None


def validate_assembly(combined: str, pages: list[str], findings: Findings) -> None:
    # Each page is matched literally; only the whitespace *between* files is flexible.
    body = combined
    if pages and not any(t[0] == "cotefile" for t in lex_tex(pages[0])[0]):
        prefix = re.match(r"\s*\\cotefile\{71\}\s*", body)
        findings.require(prefix is not None, "combined fragment must begin with cotefile{71}")
        if prefix:
            body = body[prefix.end():]
    cursor = 0
    for index, page in enumerate(pages):
        # The exact original file, including its leading/trailing whitespace, must occur.
        while cursor < len(body) and body[cursor].isspace() and not body.startswith(page, cursor):
            cursor += 1
        if not body.startswith(page, cursor):
            findings.require(False, f"combined fragment differs from page {index + 1} at assembly offset {cursor}")
            return
        cursor += len(page)
    findings.require(not body[cursor:].strip(), "combined fragment contains content after the last page")
    findings.checks += 1


def prohibited_member(name: str) -> str | None:
    parts = PurePosixPath(name).parts
    suffix = PurePosixPath(name).suffix.lower()
    lower_parts = {part.lower() for part in parts}
    if name.startswith("/") or ".." in parts:
        return "unsafe absolute or parent-traversal path"
    if suffix in IMAGE_SUFFIXES:
        return "image excluded by the task"
    if suffix in {".zip", ".pdf"}:
        return "nested archive or source PDF excluded by the task"
    if lower_parts.intersection({"source", "upload", "scans", "witnesses", "hua", "codex"}):
        return "source/witness directory excluded by the task"
    if any(part.endswith("_scans") or part.endswith("_witnesses") or part.endswith("_context") for part in lower_parts):
        return "attached source directory excluded by the task"
    return None


def validate_zip(path: Path, output: Path, findings: Findings, incomplete: bool) -> None:
    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            findings.require(len(names) == len(set(names)), "ZIP has duplicate member names")
            bad_crc = archive.testzip()
            findings.require(bad_crc is None, f"ZIP CRC failure: {bad_crc}")
            files = [name for name in names if not name.endswith("/")]
            for name in files:
                reason = prohibited_member(name)
                findings.require(reason is None, f"ZIP member {name}: {reason}")
            # Accept either a flat archive or one enclosing directory.
            root_prefix = ""
            if "progress.log" not in files:
                candidates = [n[:-len("progress.log")] for n in files if n.endswith("/progress.log")]
                if len(candidates) == 1:
                    root_prefix = candidates[0]
            by_relative = {n[len(root_prefix):]: n for n in files if n.startswith(root_prefix)}
            if not incomplete:
                for relative in MANDATORY + [f"pages/{page_name(s)}" for s in SCANS]:
                    findings.require(relative in by_relative, f"ZIP missing {relative}")
            for relative, member in by_relative.items():
                local = output / relative
                if local.is_file():
                    findings.require(archive.read(member) == local.read_bytes(),
                                     f"ZIP member differs from local deliverable: {relative}")
    except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
        findings.require(False, f"ZIP validation failed: {exc}")


def canonical_kind(value: str) -> str:
    """Canonicalize typography in a metadata label, not transcription text."""
    value = value.replace("`", "").strip()
    while "\\\\" in value:
        value = value.replace("\\\\", "\\")
    return value


def normalized_words(value: str) -> list[str]:
    """A deliberately coarse string signature used only for doubt coverage."""
    value = html.unescape(value)
    wrappers = (
        "unsure|deleted|inserted|uline|uuline|text|textrm|mathrm|mathit|"
        "mathscr|mathcal|mathbf|mathbb|mathfrak|operatorname"
    )
    value = re.sub(r"\\(?:" + wrappers + r")\b", "", value)
    value = re.sub(r"\\([A-Za-z]+)", r" \1 ", value)
    value = unicodedata.normalize("NFKD", value).casefold()
    value = "".join(c for c in value if not unicodedata.combining(c))
    return re.findall(r"[a-z0-9]+", value)


def doubt_candidate(argument: str, record: dict[str, str]) -> bool:
    """Possible textual correspondence, never a certified source-place match.

    Only reading/alternative fields are compared. Short symbols require a
    complete token match; longer readings permit containment or close textual
    similarity. Many markers may share a record for recurring notation.
    """
    alternatives = argument.split("|")
    fields = [record["reading"], record["alternatives"]]
    for alternative in alternatives:
        words = normalized_words(alternative)
        signature = "".join(words)
        if not signature:
            continue
        for value in fields:
            value_words = normalized_words(value)
            value_signature = "".join(value_words)
            if not value_signature:
                continue
            if signature == value_signature:
                return True
            if len(signature) <= 2:
                if len(words) == 1 and signature in value_words:
                    return True
                continue
            if signature in value_signature or (
                len(value_signature) >= 3 and value_signature in signature
            ):
                return True
            if min(len(signature), len(value_signature)) >= 8:
                ratio = min(len(signature), len(value_signature)) / max(len(signature), len(value_signature))
                if ratio >= 0.75 and SequenceMatcher(None, signature, value_signature).ratio() >= 0.9:
                    return True
    return False


def validate_uncertainties(page_data: dict[int, str], doubts: list[dict[str, str]],
                           findings: Findings,
                           acknowledgements: list[dict[str, str]] | None = None) -> None:
    """Flag possible missing or stale doubt records without exposing readings."""
    approved = {}
    acknowledgement_report = []
    for row in acknowledgements or []:
        scan = numeric(row["scan"], "uncertainty acknowledgement scan", findings)
        tex_line = numeric(row["tex_line"], "uncertainty acknowledgement line", findings)
        if scan is None or tex_line is None:
            continue
        digest_valid = bool(re.fullmatch(r"[0-9a-fA-F]{64}", row["page_sha256"]))
        findings.require(digest_valid, f"scan {scan}, line {tex_line}: invalid acknowledgement SHA-256")
        current = (scan in page_data and digest_valid
                   and hashlib.sha256(page_data[scan].encode("utf-8")).hexdigest() == row["page_sha256"].lower())
        acknowledgement_report.append({**row, "current": current})
        if not current:
            findings.warning(f"scan {scan}, line {tex_line}: uncertainty acknowledgement is stale or its page is absent; it was not applied")
            continue
        key = (scan, tex_line)
        findings.require(key not in approved, f"scan {scan}, line {tex_line}: duplicate uncertainty acknowledgement")
        approved[key] = row
    findings.metadata["uncertainty_acknowledgements"] = acknowledgement_report
    by_scan = defaultdict(list)
    for row in doubts:
        if row["scan"].isdigit():
            by_scan[int(row["scan"])].append(row)
    summary = []
    for scan, text in sorted(page_data.items()):
        candidates = by_scan[scan]
        active = [r for r in candidates if r["status"] in {"remaining", "retained"}]
        resolved = [r for r in candidates if r["status"] == "resolved"]
        totals = Counter()
        missing_lines = []
        resolved_lines = []
        for kind, argument, pos in lex_tex(text)[0]:
            if kind not in {"unsure", "illegible"}:
                continue
            totals[kind] += 1

            def matches(record: dict[str, str]) -> bool:
                if kind == "illegible":
                    fields = record["reading"] + " " + record["alternatives"]
                    return any(word.startswith("illeg") for word in normalized_words(fields))
                return doubt_candidate(argument, record)

            if any(matches(r) for r in active):
                totals["active_candidate"] += 1
            elif (scan, line_at(text, pos)) in approved:
                totals["manual_acknowledgement"] += 1
            elif any(matches(r) for r in resolved):
                totals["resolved_only"] += 1
                resolved_lines.append(line_at(text, pos))
            else:
                totals["no_candidate"] += 1
                missing_lines.append(line_at(text, pos))
        if missing_lines:
            findings.warning(
                f"scan {scan}: {len(missing_lines)} uncertainty marker(s) lack an approximate active-doubt "
                f"match at source lines {sorted(set(missing_lines))}; manual bookkeeping review needed"
            )
        if resolved_lines:
            findings.warning(
                f"scan {scan}: {len(resolved_lines)} uncertainty marker(s) match only resolved doubt records "
                f"at source lines {sorted(set(resolved_lines))}; check for a stale marker/status"
            )
        summary.append({"scan": scan, "active_records": len(active), **dict(totals)})
    findings.metadata["uncertainties"] = summary
    findings.checks += sum(r.get("unsure", 0) + r.get("illegible", 0) for r in summary)


def validate_bookkeeping(output: Path, collation: list[dict[str, str]],
                         page_data: dict[int, str], findings: Findings) -> None:
    decisions = read_table(output / "decisions.tsv", DECISION_HEADER, "\t", findings, False)
    doubts = read_table(output / "doubt_records.tsv", DOUBT_HEADER, "\t", findings, False)
    if (output / "decisions.tsv").exists():
        ids = Counter((r["scan"], r["id"]) for r in decisions)
        duplicate_ids = [f"{scan}/{identifier}" for (scan, identifier), count in ids.items() if count > 1]
        findings.require(not duplicate_ids, f"duplicate decision IDs: {duplicate_ids}")
        changes = [r for r in decisions if r["against_C"] == "yes" or r["against_H"] == "yes"]
        places = defaultdict(list)
        for row in changes:
            key = (row["scan"], " ".join(row["place"].casefold().split()))
            places[key].append(row["id"])
        repeated_places = [
            {"scan": key[0], "ids": identifiers}
            for key, identifiers in places.items() if len(identifiers) > 1
        ]
        for item in repeated_places:
            findings.warning(f"scan {item['scan']}: repeated change-place label for IDs {item['ids']}; verify distinct-place counting")
        for row in decisions:
            identifier = row["id"]
            findings.require(row["against_C"] in {"yes", "no"} and row["against_H"] in {"yes", "no"},
                             f"decision {identifier}: invalid witness-change flag")
            findings.require(row["confidence"] in {"high", "medium", "low"},
                             f"decision {identifier}: invalid confidence")
            if row in changes:
                kind = canonical_kind(row["kind"])
                findings.require(kind in COLLATION_KINDS, f"decision {identifier}: unrecognized error category")
                if kind != row["kind"]:
                    findings.warning(f"decision {identifier}: category label uses noncanonical typography; normalized for category counts")
        expected = []
        for row in decisions:
            if row["against_H"] != "yes":
                continue
            scan = numeric(row["scan"], f"decision {row['id']}", findings)
            if scan is None:
                continue
            findings.require(scan in H_TEXT_SCANS, f"decision {row['id']}: H text absent on this scan")
            expected.append(tuple([
                "J71-05" if scan <= 42 else "J71-06", str(scan - 1), str(scan),
                row["place"], row["H"], row["C"], row["final"], row["scan_shows"],
                row["kind"], row["marked_in_H"], row["confidence"],
            ]))
        actual = [tuple(row[key] for key in COLLATION_HEADER) for row in collation]
        projected = Counter(expected) == Counter(actual)
        findings.require(projected, "H collation is not the exact multiset projection of against_H=yes decisions")
        category_counts = []
        for label, kind in ERROR_SHEET_CATEGORIES:
            selected = [r for r in changes if canonical_kind(r["kind"]) == kind]
            category_counts.append({
                "category": label, "places": len(selected),
                "against_C": sum(r["against_C"] == "yes" for r in selected),
                "against_H": sum(r["against_H"] == "yes" for r in selected),
            })
        findings.metadata["decisions"] = {
            "rows": len(decisions), "changes": len(changes),
            "against_C": sum(r["against_C"] == "yes" for r in changes),
            "against_H": sum(r["against_H"] == "yes" for r in changes),
            "against_both": sum(r["against_C"] == "yes" and r["against_H"] == "yes" for r in changes),
            "retention_rows": len(decisions) - len(changes),
            "exact_unique_change_places": len(places),
            "repeated_place_labels": repeated_places,
            "H_projection_exact": projected,
            "category_counts": category_counts,
        }
    if (output / "doubt_records.tsv").exists():
        places = defaultdict(list)
        for row in doubts:
            key = (row["scan"], " ".join(row["place"].casefold().split()))
            places[key].append(row["status"])
            findings.require(row["status"] in {"remaining", "resolved", "retained"},
                             f"doubt record on scan {row['scan']}: unrecognized status")
        for (scan, _), statuses in places.items():
            if len(statuses) > 1:
                findings.warning(f"scan {scan}: repeated doubt-place label with statuses {statuses}; append-only rendering does not supersede an earlier record")
        findings.metadata["doubt_statuses"] = dict(Counter(r["status"] for r in doubts))
        acknowledgements = read_table(
            output / "UNCERTAINTY_ACKNOWLEDGEMENTS.tsv", ACKNOWLEDGEMENT_HEADER,
            "\t", findings, False,
        )
        validate_uncertainties(page_data, doubts, findings, acknowledgements)
    elif page_data:
        findings.warning("No doubt_records.tsv: approximate in-place uncertainty correspondence was not checked")


def validate_progress(output: Path, scans: list[int], findings: Findings, incomplete: bool) -> None:
    path = output / "progress.log"
    if not path.is_file():
        return
    text = read_utf8(path, findings)
    if text is None:
        return
    lines = text.splitlines()
    findings.require(bool(lines) and bool(re.search(r"\d{4}-\d{2}-\d{2}.*UTC", lines[0])),
                     "progress.log first line must record the UTC start time")
    done = [int(m.group(1)) for line in lines if (m := re.match(r"scan\s+(\d+)\s+done\b", line))]
    audited = [int(m.group(1)) for line in lines if (m := re.match(r"scan\s+(\d+)\s+audited\b", line))]
    findings.require(set(scans) <= set(done), "progress.log lacks done entries for present pages")
    findings.require(done == sorted(done), "progress.log done entries are not in scan order")
    for label, entries in [("done", done), ("audited", audited)]:
        duplicates = [scan for scan, count in Counter(entries).items() if count > 1]
        if duplicates:
            findings.warning(f"progress.log has repeated {label} entries for scans {duplicates}")
    if not incomplete:
        findings.require(set(SCANS) <= set(audited), "progress.log does not yet record every second reading")
    freeze_indices = [i for i, line in enumerate(lines) if line.startswith("transcription frozen ")]
    metadata = {"done": done, "audited": audited, "frozen": bool(freeze_indices)}
    if not freeze_indices:
        if not incomplete:
            findings.require(False, "progress.log lacks a transcription frozen event")
        findings.metadata["progress"] = metadata
        return
    freeze_index = freeze_indices[-1]
    hashes = {}
    for line in lines[freeze_index + 1:]:
        # Accept sha256sum, 'sha256 HASH PATH', or 'SHA256 PATH HASH'.
        match = re.match(r"(?:sha256\s+)?([0-9a-fA-F]{64})\s+\*?(.+?)\s*$", line, re.I)
        if match:
            digest, relative = match.groups()
        else:
            match = re.match(r"sha256\s+(.+?)\s+([0-9a-fA-F]{64})\s*$", line, re.I)
            if not match:
                continue
            relative, digest = match.groups()
        relative = relative.removeprefix("./")
        hashes[relative] = digest.lower()
    expected = [f"pages/{page_name(scan)}" for scan in scans] + [f"{PREFIX}_transcription.tex"]
    verified = 0
    for relative in expected:
        findings.require(relative in hashes, f"frozen hash missing from progress.log: {relative}")
        local = output / relative
        if relative in hashes and local.is_file():
            digest = hashlib.sha256(local.read_bytes()).hexdigest()
            equal = digest == hashes[relative]
            findings.require(equal, f"frozen transcription hash changed: {relative}")
            verified += equal
    confirmed = any(re.search(r"hashes.*unchanged|unchanged.*hashes", line, re.I)
                    for line in lines[freeze_index + 1:])
    if not incomplete:
        findings.require(confirmed, "progress.log lacks the final confirmation that frozen hashes are unchanged")
    metadata.update({"hashes_verified": verified, "hashes_expected": len(expected), "unchanged_confirmation": confirmed})
    findings.metadata["progress"] = metadata


def write_report(path: Path, findings: Findings, scans: list[int], incomplete: bool) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [
        "# SP60_CW_71 — Structural metadata review\n\n",
        f"Generated {now}. Scope: {'working checkpoint' if incomplete else 'final package'} structure.\n\n",
        "This report is generated from deliverable structure and bookkeeping metadata. It does not inspect source scans or witnesses, judge readings, interpret mathematics, certify inventory completeness, or compile TeX. Approximate doubt matches are string candidates, not confirmed identification of manuscript places.\n\n",
        f"Result: **{'FAIL' if findings.errors else 'PASS'}**, {findings.checks} structural checks, {len(findings.warnings)} warning(s). Present scans: {', '.join(str(s) for s in scans)}.\n\n",
    ]
    pending = findings.metadata.get("missing_final_docs", [])
    if pending:
        lines.append("Required final documents still pending: " + ", ".join(f"`{name}`" for name in pending) + ".\n\n")
    decisions = findings.metadata.get("decisions")
    if decisions:
        lines += [
            "## Decision bookkeeping\n\n",
            f"{decisions['rows']} decision rows: {decisions['changes']} changes and {decisions['retention_rows']} retained-reading rows. Changes against C: {decisions['against_C']}; against H: {decisions['against_H']}; against both: {decisions['against_both']}. Exact unique scan/place labels: {decisions['exact_unique_change_places']}. H collation projection exact: {decisions['H_projection_exact']}.\n\n",
            "The counts below use one recorded primary category per change row. They do not establish that differently worded place labels are distinct manuscript locations. Category typography is normalized for counting.\n\n",
            "| Error-sheet category | Change rows | Against C | Against H |\n|---|---:|---:|---:|\n",
        ]
        for row in decisions["category_counts"]:
            lines.append(f"| {row['category']} | {row['places']} | {row['against_C']} | {row['against_H']} |\n")
    uncertainties = findings.metadata.get("uncertainties")
    if uncertainties is not None:
        lines += [
            "\n## Approximate uncertainty coverage\n\n",
            "Each in-place marker is compared with reading/alternative fields on the same scan. Recurring notation permits several markers to share a doubt row. A primary-reader acknowledgement can resolve a failed approximate match only while its recorded page SHA-256 is current. Remaining missing candidates and matches only to resolved rows are warnings; they do not establish a transcription defect.\n\n",
            "| Scan | Unsure | Illegible | Active doubt rows | Active candidate | Manual acknowledgement | Resolved only | No candidate |\n|---|---:|---:|---:|---:|---:|---:|---:|\n",
        ]
        for row in uncertainties:
            lines.append("| " + " | ".join(str(row.get(key, 0)) for key in ["scan", "unsure", "illegible", "active_records", "active_candidate", "manual_acknowledgement", "resolved_only", "no_candidate"]) + " |\n")
        acknowledgements = findings.metadata.get("uncertainty_acknowledgements", [])
        if acknowledgements:
            lines += [
                "\n### Primary-reader manual mappings\n\n",
                "These are the primary reader's supplied mappings to existing active doubt records, not additional manuscript judgments by the validator. They are bound to the full page-file hashes stored in `UNCERTAINTY_ACKNOWLEDGEMENTS.tsv`; a later page edit makes a mapping stale until deliberately reviewed.\n\n",
                "| Scan | TeX line | Hash current | Primary-reader acknowledgement |\n|---|---:|---|---|\n",
            ]
            for row in acknowledgements:
                message = row["acknowledgement"].replace("|", "&#124;").replace("\n", "<br>")
                lines.append(f"| {row['scan']} | {row['tex_line']} | {'yes' if row['current'] else 'no'} | {message} |\n")
    progress = findings.metadata.get("progress")
    if progress:
        lines += [
            "\n## Progress and freeze\n\n",
            f"Done entries: {len(progress['done'])}. Audited entries: {len(progress['audited'])}. Freeze recorded: {progress['frozen']}.\n\n",
        ]
        if progress["frozen"]:
            lines.append(f"Current frozen hashes verified: {progress.get('hashes_verified', 0)}/{progress.get('hashes_expected', 0)}. Final unchanged confirmation: {progress.get('unchanged_confirmation', False)}.\n\n")
        else:
            lines.append("Freeze is intentionally pending until the primary reader completes every second reading and final assembly.\n\n")
    lines.append("## Errors\n\n")
    lines.extend(f"- {message}\n" for message in findings.errors)
    if not findings.errors:
        lines.append("None.\n")
    lines.append("\n## Warnings\n\n")
    lines.extend(f"- {message}\n" for message in findings.warnings)
    if not findings.warnings:
        lines.append("None.\n")
    lines += [
        "\n## Final bookkeeping procedure\n\n",
        "1. Complete all second readings; consolidate superseded place decisions and doubt statuses while preserving the audit history.\n",
        "2. Generate every required final document and the combined fragment. Recheck the H projection and category counts.\n",
        "3. Append `transcription frozen <UTC time>` to `progress.log`, followed by one `sha256 <64-hex digest> <relative path>` line for each page and the combined fragment. Hash only finalized UTF-8 bytes.\n",
        "4. Recompute those hashes before packaging. If any differ, investigate and deliberately establish a new freeze after the change; do not silently replace the recorded values.\n",
        "5. After successful comparison, append `frozen hashes unchanged <UTC time>`. Run the validator in final mode and then with `--zip` against the final archive.\n\n",
        "`record.py` is append-only: it does not automatically supersede doubts, deduplicate places, or rebuild the H collation after an existing decision row is edited. Its `render()` also rewrites the combined transcription, so finish rendering before freezing.\n",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("output_directory", type=Path)
    parser.add_argument("--zip", dest="zip_path", type=Path, help="also check an existing final/checkpoint ZIP")
    parser.add_argument("--incomplete", action="store_true", help="allow a contiguous partial set of completed pages")
    parser.add_argument("--report", type=Path, help="write a structural metadata report without quoting readings")
    args = parser.parse_args()
    output = args.output_directory.resolve()
    result = Findings()
    result.require(output.is_dir(), f"output directory does not exist: {output}")
    if not output.is_dir():
        print("FAIL: " + result.errors[0])
        return 1
    result.metadata["missing_final_docs"] = [relative for relative in MANDATORY if not (output / relative).is_file()]
    if not args.incomplete:
        for relative in MANDATORY:
            result.require((output / relative).is_file(), f"missing required deliverable: {relative}")
    expected = {page_name(scan): scan for scan in SCANS}
    page_dir = output / "pages"
    actual = {p.name for p in page_dir.glob("*.tex")} if page_dir.is_dir() else set()
    result.require(actual <= set(expected), f"unexpected page filenames: {sorted(actual - set(expected))}")
    present_scans = [scan for scan in SCANS if page_name(scan) in actual]
    if args.incomplete:
        result.require(present_scans == list(SCANS[:len(present_scans)]),
                       "checkpoint pages must be a contiguous prefix of scans 038–048")
    else:
        result.require(actual == set(expected), f"missing page files: {sorted(set(expected) - actual)}")
    page_texts = []
    page_data = {}
    for scan in present_scans:
        name = page_name(scan)
        text = read_utf8(page_dir / name, result)
        if text is None:
            continue
        page_texts.append(text)
        page_data[scan] = text
        tokens = validate_tex(name, text, result)
        markers = [value for kind, value, _ in tokens if kind == "scanpage"]
        result.require(len(markers) == 1 and markers[0].isdigit() and int(markers[0]) == scan,
                       f"{name}: expected exactly one scanpage{{{scan}}}; got {markers}")
        cotes = [value for kind, value, _ in tokens if kind == "cotefile"]
        result.require((not cotes) or (scan == 38 and cotes == ["71"]),
                       f"{name}: cotefile allowed only once, as 71, in scan 038")
    combined_path = output / f"{PREFIX}_transcription.tex"
    if combined_path.is_file():
        combined = read_utf8(combined_path, result)
        if combined is not None:
            tokens = validate_tex(combined_path.name, combined, result)
            cotes = [value for kind, value, _ in tokens if kind == "cotefile"]
            result.require(cotes == ["71"], f"combined fragment must contain exactly one cotefile{{71}}; got {cotes}")
            markers = [value for kind, value, _ in tokens if kind == "scanpage"]
            result.require(markers == [str(scan) for scan in present_scans],
                           f"combined fragment scan order is {markers}, expected {present_scans}")
            if len(page_texts) == len(present_scans):
                validate_assembly(combined, page_texts, result)
    required = not args.incomplete
    collation = read_table(output / f"{PREFIX}_collation.tsv", COLLATION_HEADER, "\t", result, required)
    for index, row in enumerate(collation, 2):
        loc = f"collation row {index}"
        scan = numeric(row["our_scan"], loc, result)
        their = numeric(row["their_page"], loc, result)
        result.require(scan in H_TEXT_SCANS, f"{loc}: H has no transcribed text for scan {scan}")
        if scan is not None:
            result.require(scan in present_scans, f"{loc}: page {scan} is not present")
            result.require(their == scan - 1, f"{loc}: their_page must be our_scan - 1")
            result.require(row["folder"] == ("J71-05" if scan <= 42 else "J71-06"),
                           f"{loc}: incorrect folder")
        result.require(row["kind"] in COLLATION_KINDS, f"{loc}: unrecognized kind {row['kind']!r}")
        result.require(row["confidence"] in {"high", "medium", "low"}, f"{loc}: invalid confidence")
        result.require(bool(row["marked_in_H"].strip()), f"{loc}: marked_in_H is empty")
        for key in ("line", "their_reading", "codex_reading", "final_reading", "scan_shows"):
            result.require(bool(row[key].strip()), f"{loc}: {key} is empty")
    inventory = read_table(output / f"{PREFIX}_inventory.csv", INVENTORY_HEADER, ",", result, required)
    inventory_scans = set()
    for index, row in enumerate(inventory, 2):
        loc = f"inventory row {index}"
        scan = numeric(row["scan"], loc, result)
        inventory_scans.add(scan)
        result.require(scan in present_scans, f"{loc}: scan {scan} has no page file")
        result.require(row["transcribed"] == "yes", f"{loc}: transcribed must be yes")
        result.require(row["sheet_kind"] in SHEET_KINDS, f"{loc}: invalid sheet_kind")
        result.require(row["kind"] in ELEMENT_KINDS, f"{loc}: invalid element kind")
        for key in ("hand", "element", "position", "first_words_or_objects"):
            result.require(bool(row[key].strip()), f"{loc}: {key} is empty")
    result.require(set(present_scans) <= inventory_scans,
                   f"inventory lacks scans {sorted(set(present_scans) - inventory_scans)}")
    events = read_table(output / "CHECK_EVENTS.tsv", CHECK_HEADER, "\t", result, required)
    for index, row in enumerate(events, 2):
        for key in CHECK_HEADER:
            result.require(bool(row[key].strip()), f"CHECK_EVENTS row {index}: {key} is empty")
    validate_bookkeeping(output, collation, page_data, result)
    validate_progress(output, present_scans, result, args.incomplete)
    for path in output.rglob("*"):
        if path.is_file():
            relative = path.relative_to(output).as_posix()
            # A separately requested archive may live under OUTPUT; do not reject itself.
            if args.zip_path is not None and path.resolve() == args.zip_path.resolve():
                continue
            reason = prohibited_member(relative)
            result.require(reason is None, f"output file {relative}: {reason}")
    if args.zip_path is not None:
        validate_zip(args.zip_path, output, result, args.incomplete)
    if args.report is not None:
        write_report(args.report, result, present_scans, args.incomplete)
    print(f"{'FAIL' if result.errors else 'PASS'}: {result.checks} structural checks; "
          f"{len(present_scans)} page files; {len(collation)} collation rows; "
          f"{len(inventory)} inventory rows; {len(events)} check events.")
    for message in result.errors:
        print("ERROR: " + message)
    for message in result.warnings:
        print("WARNING: " + message)
    print("Scope: structural validation only; no TeX compilation or manuscript/content verification.")
    if args.report is not None:
        print(f"Metadata report: {args.report}")
    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())
