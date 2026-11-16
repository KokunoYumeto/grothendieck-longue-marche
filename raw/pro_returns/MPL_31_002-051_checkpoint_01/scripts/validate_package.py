#!/usr/bin/env python3
"""Mechanical checks only; neither visual completeness nor reading accuracy is certified.

Use --phase checkpoint while the work is in progress.  The final default checks
the complete package, the second-reading records, and the frozen-file digests.
No file is written.  Only standard-library modules are used.
"""

from __future__ import annotations

import argparse
import collections
import csv
import datetime as dt
import hashlib
import io
import json
from pathlib import Path
import re
import sys


PREFIX = "MPL_31_002-051"
SCANS = tuple(n for n in range(2, 52) if n not in {34, 40, 41, 46})
FIELDS = ["cote", "scan", "sheet_kind", "element", "kind", "position",
          "first_words_or_objects", "transcribed"]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
STATE = {"cotefile", "scanpage", "mspage", "deleted", "inserted", "margin",
         "uline", "uuline", "diagram", "figure", "unsure", "illegible"}
PROHIBITED = {"documentclass", "usepackage", "RequirePackage", "newcommand",
              "renewcommand", "providecommand", "DeclareRobustCommand", "def",
              "gdef", "edef", "xdef", "newenvironment", "renewenvironment",
              "includegraphics", "pgfimage", "pdfximage", "includepdf", "epsfig",
              "input", "include"}
TIMESTAMP = re.compile(r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?: UTC|Z|\+00:00)")


def without_comments(text):
    """Keep line/character positions stable; recognize escaped percent signs."""
    out = list(text)
    for match in re.finditer(r"%", text):
        p = match.start() - 1
        while p >= 0 and text[p] == "\\":
            p -= 1
        if (match.start() - 1 - p) % 2:
            continue
        end = text.find("\n", match.start())
        end = len(text) if end < 0 else end
        out[match.start():end] = " " * (end - match.start())
    return "".join(out)


def group_at(text, pos):
    while pos < len(text) and text[pos].isspace():
        pos += 1
    if pos == len(text) or text[pos] != "{":
        return None
    start, depth, i = pos + 1, 1, pos + 1
    while i < len(text):
        if text[i] == "\\":
            i += 2
            continue
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if not depth:
                return text[start:i], i + 1
        i += 1
    return None


def md_cells(line):
    """Split table cells without splitting escaped or code-span pipes."""
    line = line.strip().strip("|")
    cells, current, ticks, i = [], [], 0, 0
    while i < len(line):
        if line[i] == "\\" and i + 1 < len(line):
            current.extend(line[i:i + 2])
            i += 2
            continue
        if line[i] == "`":
            j = i
            while j < len(line) and line[j] == "`":
                j += 1
            run = j - i
            ticks = 0 if ticks == run else (run if not ticks else ticks)
            current.extend(line[i:j])
            i = j
            continue
        if line[i] == "|" and not ticks:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(line[i])
        i += 1
    cells.append("".join(current).strip())
    return cells


def utc_from_line(line):
    match = TIMESTAMP.search(line)
    if not match:
        return None
    try:
        return dt.datetime.fromisoformat(match.group().replace(" UTC", "+00:00").replace("Z", "+00:00"))
    except ValueError:
        return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--phase", choices=("checkpoint", "final"), default="final")
    ap.add_argument("--join", choices=("auto", "exact", "newline", "blank-line"), default="auto",
                    help="Allowed byte separator between complete page files; auto accepts these three conventions.")
    args = ap.parse_args()
    root, final = args.root.resolve(), args.phase == "final"
    issues = []
    report = {"root": str(root), "phase": args.phase, "expected_scans": list(SCANS), "issues": issues}

    def issue(level, code, message, **extra):
        issues.append(dict(level=level, code=code, message=message, **extra))

    def pending(code, message, **extra):
        issue("error" if final else "warning", code, message, **extra)

    def read(path, required=True):
        if not path.is_file():
            if required:
                pending("missing_file", "Required file is absent.", file=str(path.relative_to(root)))
            return None, None
        data = path.read_bytes()
        try:
            return data, data.decode("utf-8-sig")
        except UnicodeDecodeError as exc:
            issue("error", "encoding", "File is not valid UTF-8.", file=str(path.relative_to(root)), offset=exc.start)
            return data, None

    expected = {n: root / "pages" / f"{PREFIX}_31_scan{n:03d}.tex" for n in SCANS}
    page_data, counts, commands = {}, {}, collections.Counter()
    present = [n for n, p in expected.items() if p.is_file()]
    missing = sorted(set(SCANS) - set(present))
    report["present_scans"], report["missing_scans"] = present, missing
    report["complete_expected_pages"] = not missing
    if missing:
        pending("missing_pages", "Expected page files are absent.", scans=missing)
    pages_dir = root / "pages"
    extras = sorted(p.name for p in pages_dir.glob("*.tex") if p not in expected.values())
    if extras:
        issue("error", "unexpected_pages", "Unexpected TeX files are present in pages/.", files=extras)

    for n in present:
        path = expected[n]
        data, text = read(path)
        page_data[n] = data
        if text is None:
            continue
        name = str(path.relative_to(root))
        clean = without_comments(text)
        page_commands = collections.Counter(re.findall(r"\\([A-Za-z@]+)", clean))
        commands.update(page_commands)
        counts[n] = {key: page_commands[key] for key in sorted(STATE) if page_commands[key]}
        markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)
        if markers != [str(n)] and not (len(markers) == 1 and int(markers[0]) == n):
            issue("error", "scan_marker", "Page must contain exactly its own scanpage marker.", file=name, markers=markers)
        cote = re.findall(r"\\cotefile\s*\{([^}]*)\}", clean)
        if cote != (["31"] if n == SCANS[0] else []):
            issue("error", "cote_marker", "cotefile{31} belongs before the first scan only.", file=name, markers=cote)
        header = (r"\s*\\cotefile\s*\{31\}" if n == SCANS[0] else r"\s*")
        header += rf"\s*\\scanpage\s*\{{\s*0*{n}\s*\}}"
        if not re.match(header, clean):
            issue("error", "page_start", "Page header is absent or preceded by transcription content.", file=name)
        forbidden = sorted(PROHIBITED & page_commands.keys())
        if forbidden or re.search(r"\\(?:begin|end)\s*\{document\}", clean):
            issue("error", "fragment_or_image_command", "Fragment contains preamble, macro-definition, external-input, or image commands.", file=name, commands=forbidden)

        stack, i = [], 0
        while i < len(clean):
            if clean[i] == "\\":
                i += 2
                continue
            if clean[i] == "{":
                stack.append(i)
            elif clean[i] == "}":
                if stack:
                    stack.pop()
                else:
                    issue("error", "unmatched_closing_brace", "Closing brace has no opening brace.", file=name, line=clean.count("\n", 0, i) + 1)
            i += 1
        if stack:
            issue("error", "unclosed_braces", "Opening braces remain unclosed.", file=name,
                  lines=[clean.count("\n", 0, p) + 1 for p in stack])
        envs = []
        for match in re.finditer(r"\\(begin|end)\s*\{([^}]+)\}", clean):
            op, env = match.groups()
            if op == "begin":
                envs.append(env)
            elif envs and envs[-1] == env:
                envs.pop()
            else:
                issue("error", "environment_mismatch", "Environment closing does not match the current open environment.", file=name, environment=env)
        if envs:
            issue("error", "unclosed_environments", "Environments remain open.", file=name, environments=envs)
        for match in re.finditer(r"\\([A-Za-z@]+)", clean):
            macro = match.group(1)
            if macro not in STATE:
                continue
            arg = group_at(clean, match.end())
            if arg is None:
                issue("error", "state_macro_argument", "State macro lacks one balanced braced argument.", file=name, macro=macro, line=clean.count("\n", 0, match.start()) + 1)
                continue
            value = arg[0]
            if macro == "illegible" and not re.fullmatch(r"\s*[1-9]\d*\s*", value):
                issue("error", "illegible_count", "illegible requires a positive estimated word count.", file=name)
            if macro == "unsure" and not value.strip():
                issue("error", "empty_unsure", "unsure has an empty reading.", file=name)
            if macro == "diagram" and not re.search(r"\\begin\s*\{(?:tikzcd|array)\}", value):
                issue("warning", "diagram_environment", "Review diagram argument: no tikzcd or array environment was found.", file=name)
            if macro == "figure" and not re.search(r"\\(?:begin\s*\{tikzpicture\}|tikz\b)", value):
                issue("warning", "drawing_environment", "Review figure argument: no TikZ drawing command was found.", file=name)
    report["state_macro_counts_by_scan"] = {f"{n:03d}": counts.get(n, {}) for n in present}
    report["other_command_inventory"] = {key: commands[key] for key in sorted(commands) if key not in STATE}

    combined_path = root / f"{PREFIX}_transcription.tex"
    combined, combined_text = read(combined_path, required=final)
    if combined is not None and len(page_data) == len(present):
        separators = {"exact": b"", "newline": b"\n", "blank-line": b"\n\n"}
        allowed = separators if args.join == "auto" else {args.join: separators[args.join]}
        matches = [key for key, sep in allowed.items() if combined == sep.join(page_data[n] for n in present)]
        report["concatenation_convention"] = matches
        if not matches:
            issue("error", "combined_mismatch", "Combined transcription does not equal the ordered page bytes with the allowed separator.")

    inv_path = root / f"{PREFIX}_inventory.csv"
    _, inv_text = read(inv_path, required=bool(present) or final)
    inv_counts, identifiers = collections.Counter(), set()
    if inv_text is not None:
        try:
            reader = csv.DictReader(io.StringIO(inv_text))
            if reader.fieldnames != FIELDS:
                issue("error", "inventory_header", "CSV header must match the requested ordered columns.", found=reader.fieldnames, expected=FIELDS)
            else:
                for row_number, row in enumerate(reader, 2):
                    if not any(row.values()):
                        continue
                    if None in row or any(value is None for value in row.values()):
                        issue("error", "inventory_width", "CSV row has an incorrect number of fields.", row=row_number)
                        continue
                    try:
                        n = int(row["scan"])
                    except ValueError:
                        issue("error", "inventory_scan", "CSV scan value is not an integer.", row=row_number)
                        continue
                    inv_counts[n] += 1
                    if row["cote"].strip() != "31" or n not in SCANS:
                        issue("error", "inventory_scope", "CSV row names a cote or scan outside this package.", row=row_number)
                    if n not in present:
                        issue("error", "inventory_page_absent", "CSV row has no corresponding page file.", row=row_number, scan=n)
                    if row["transcribed"].strip() != "yes":
                        issue("error", "inventory_unfinished", "CSV element is not marked transcribed=yes.", row=row_number)
                    if row["kind"].strip() not in KINDS or row["sheet_kind"].strip() not in SHEET_KINDS:
                        issue("error", "inventory_category", "CSV row uses an unsupported kind or sheet_kind.", row=row_number)
                    identity = (n, row["element"])
                    if identity in identifiers:
                        issue("warning", "inventory_duplicate_id", "Element identifier repeats within a scan.", row=row_number, scan=n)
                    identifiers.add(identity)
                    if any(not row[field].strip() for field in FIELDS):
                        issue("warning", "inventory_blank_field", "CSV row contains an empty field.", row=row_number)
        except csv.Error as exc:
            issue("error", "inventory_parse", str(exc))
    for n in present:
        if not inv_counts[n]:
            issue("error", "inventory_missing_scan", "Page file has no inventory rows.", scan=n)
    report["inventory_rows_by_scan"] = {f"{n:03d}": inv_counts[n] for n in sorted(inv_counts)}

    _, doubts = read(root / f"{PREFIX}_doubts.md", required=bool(present) or final)
    doubt_rows, table_header = collections.Counter(), None
    if doubts is not None:
        report["notation_heading_found"] = bool(re.search(r"(?im)^#{1,6}\s+.*notation", doubts))
        for line_number, line in enumerate(doubts.splitlines(), 1):
            if not line.lstrip().startswith("|"):
                table_header = None
                continue
            cells = md_cells(line)
            lowered = [cell.lower().strip(" *`") for cell in cells]
            scan_col = next((i for i, cell in enumerate(lowered) if "scan" in cell), None)
            confidence_col = next((i for i, cell in enumerate(lowered) if "confidence" in cell), None)
            if scan_col is not None and confidence_col is not None:
                table_header = (scan_col, confidence_col, len(cells))
                continue
            if not table_header or all(re.fullmatch(r"[:\-\s]+", cell) for cell in cells):
                continue
            sc, cc, width = table_header
            if len(cells) != width:
                issue("warning", "doubts_table_width", "A doubt table row has an unexpected cell count; literal pipes may need escaping.", line=line_number)
                continue
            scan_cell = cells[sc].strip(" *`")
            if re.fullmatch(r"\d{1,3}", scan_cell):
                doubt_rows[int(scan_cell)] += 1
            else:
                issue("info", "doubt_scan_unparsed", "A doubt row uses a scan value other than a single integer; it was excluded from the per-scan comparison.", line=line_number)
            if cells[cc].lower().strip(" *`") not in {"high", "medium", "low"}:
                issue("warning", "doubt_confidence", "Review confidence cell: expected high, medium, or low.", line=line_number)
        report["doubt_comparison_by_scan"] = {
            f"{n:03d}": {"macros": counts.get(n, {}).get("unsure", 0) + counts.get(n, {}).get("illegible", 0),
                         "table_rows": doubt_rows[n]} for n in present}
        uncovered = [n for n in present if counts.get(n, {}).get("unsure", 0) + counts.get(n, {}).get("illegible", 0) and not doubt_rows[n]]
        if uncovered:
            issue("warning", "doubt_rows_not_found", "Doubt macros occur on scans with no individually parsed doubt-table rows; inspect coverage manually.", scans=uncovered)
        report["doubt_count_limit"] = "Counts are diagnostic only: a table row can group recurring doubts, and counts cannot establish correspondence."

    notes_path = root / f"{PREFIX}_notes.md"
    if final and (not notes_path.is_file() or not notes_path.stat().st_size):
        issue("error", "research_notes_missing", "Research notes file is absent or empty.")

    _, log = read(root / "progress.log")
    if log is not None:
        lines = log.splitlines()
        if not lines or utc_from_line(lines[0]) is None:
            issue("error", "start_timestamp", "First progress.log line must contain a UTC timestamp.")
        done, audits, freezes, contexts, unchanged = {}, {}, [], [], []
        known_files = {p.name: p for p in expected.values() if p.is_file()}
        if combined_path.is_file():
            known_files[combined_path.name] = combined_path
        hashes = collections.defaultdict(list)
        for index, line in enumerate(lines):
            done_match = re.match(r"31\s+scan\s+(\d+)\s+done\b", line)
            audit_match = re.match(r"(?:31\s+)?scan\s+(\d+)\s+audited\b", line)
            event = False
            if done_match:
                done.setdefault(int(done_match[1]), []).append(index)
                event = True
            if audit_match:
                audits.setdefault(int(audit_match[1]), []).append(index)
                event = True
            if re.match(r"transcription frozen\b", line):
                freezes.append(index)
                event = True
            if re.match(r"context opened\b", line):
                contexts.append(index)
                event = True
            if re.search(r"(?i)(?:hash.*(?:unchanged|verified|match)|(?:unchanged|verified|match).*hash)", line):
                unchanged.append(index)
            if event and utc_from_line(line) is None:
                issue("error", "event_timestamp", "Progress event lacks a valid UTC timestamp.", line=index + 1)
            digest_match = re.search(r"\b([0-9a-fA-F]{64})\b", line)
            if digest_match:
                for name in known_files:
                    if re.search(re.escape(name) + r"(?=$|[\s\"'])", line):
                        hashes[name].append((index, digest_match[1].lower()))
        for n in present:
            if n not in done:
                issue("error", "done_record_missing", "Written page lacks its done record.", scan=n)
            if final and n not in audits:
                issue("error", "audit_record_missing", "Page lacks its second-reading audit record.", scan=n)
        first_done_order = [n for n, indexes in sorted(done.items(), key=lambda pair: pair[1][0])]
        if first_done_order != sorted(first_done_order):
            issue("error", "done_order", "First done records are not in scan order.")
        if any(n not in SCANS for n in set(done) | set(audits)):
            issue("error", "log_scan_scope", "Done or audit records name scans outside this package.")
        if audits and done and min(min(v) for v in audits.values()) < max(min(v) for v in done.values()):
            issue("error", "audit_before_first_pass_end", "A second-reading audit was logged before the last first-pass completion.")
        if final and not freezes:
            issue("error", "freeze_record_missing", "No transcription frozen record was found.")
        if freezes and audits and freezes[0] < max(max(v) for v in audits.values()):
            issue("error", "freeze_before_audit_end", "Freeze record precedes a second-reading audit.")
        if final and not contexts:
            issue("error", "context_record_missing", "No context opened record was found.")
        if contexts and (not freezes or contexts[0] <= freezes[0]):
            issue("error", "context_before_freeze", "Context opening was logged before a completed transcription freeze.")
        if final and not any(i > (contexts[-1] if contexts else -1) for i in unchanged):
            issue("error", "final_hash_record_missing", "No explicit post-context hash-verification record was found.")
        digest_status = {}
        for name, path in known_files.items():
            pre_context = [digest for i, digest in hashes[name] if not contexts or i < contexts[0]]
            current = hashlib.sha256(path.read_bytes()).hexdigest()
            digest_status[name] = {"sha256": current, "recorded_before_context": bool(pre_context),
                                   "matches_all_recorded": bool(pre_context) and all(h == current for h in pre_context)}
            if (final or freezes) and not pre_context:
                issue("error", "freeze_hash_missing", "File has no SHA-256 recorded before context opening.", file=name)
            if pre_context and any(h != current for h in pre_context):
                issue("error", "freeze_hash_changed", "Current file bytes differ from a recorded frozen SHA-256.", file=name)
        report["digest_verification"] = digest_status
        report["progress_records"] = {"done_scans": sorted(done), "audited_scans": sorted(audits),
                                      "freeze_records": len(freezes), "context_open_records": len(contexts),
                                      "hash_verification_records": len(unchanged)}

    severity_counts = collections.Counter(item["level"] for item in issues)
    report["issue_counts"] = dict(severity_counts)
    report["status"] = "failed" if severity_counts["error"] else ("passed_with_warnings" if severity_counts["warning"] else "passed")
    report["limits"] = [
        "No image, archive, or context file is opened by this script.",
        "No visual completeness, handwriting accuracy, manuscript order, or semantic inventory coverage is certified.",
        "Command inventory and literal brace/environment checks do not prove LaTeX compilation or that every command is standard.",
        "Deletion/insertion attachment, diagram geometry, math-symbol readings, and illegible versus unsure usage require visual review.",
        "Research-note substance, abbreviations, and correspondence between individual doubt marks and rows require manual review."
    ]
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 2 if severity_counts["error"] else 0


if __name__ == "__main__":
    sys.exit(main())
