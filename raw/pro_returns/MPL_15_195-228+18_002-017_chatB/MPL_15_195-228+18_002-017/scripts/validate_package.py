#!/usr/bin/env python3
"""Read-only mechanical checks for the MPL 15/18 transcription package.

This program checks file structure and textual bookkeeping. It does not read
images, invoke OCR, evaluate mathematics, or establish transcription accuracy
or visual completeness. Run it only after the responsible reader has saved
the material to be checked.

Recommended frozen-hash records in progress.log (one per file):
    sha256 <relative/path> <64 lowercase hexadecimal characters>
    transcription frozen YYYY-MM-DD HH:MM:SS UTC
The ordinary sha256sum form '<digest>  <relative/path>' is also accepted.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


PREFIX = "MPL_15_195-228+18_002-017"
EXPECTED = [(15, n) for n in range(195, 229)] + [
    (18, n) for n in range(2, 18) if n != 8
]
FIRST = {(15, 195), (18, 2)}
COLUMNS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
SHEET_KINDS = {"text", "reused_typed", "typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}
TIME_RE = re.compile(
    r"(?P<time>\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}"
    r"(?:\.\d+)?(?: UTC|Z|\+00:00))$"
)
HASH_RE = re.compile(r"^[0-9a-fA-F]{64}$")


def page_name(cote: int, scan: int) -> str:
    return f"{PREFIX}_{cote}_scan{scan:03d}.tex"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def utc_time(text: str):
    """Parse an explicit UTC timestamp, without treating local time as UTC."""
    found = TIME_RE.search(text.strip())
    if not found:
        return None
    stamp = found.group("time").replace(" UTC", "+00:00").replace("Z", "+00:00")
    try:
        value = datetime.fromisoformat(stamp)
    except ValueError:
        return None
    return value.astimezone(timezone.utc)


def mask_tex(text: str) -> str:
    """Preserve offsets/newlines while masking comments and verbatim snippets.

    A backslash consumes its following nonletter character as a control
    symbol; this correctly distinguishes escaped percent/braces from a
    percent/braces following a double backslash. Macro arguments remain.
    """
    out = list(text)
    i = 0
    while i < len(text):
        c = text[i]
        if c == "%":
            j = text.find("\n", i)
            if j < 0:
                j = len(text)
            out[i:j] = " " * (j - i)
            i = j
        elif c == "\\":
            verb = re.match(r"\\verb\*?(?![A-Za-z])", text[i:])
            if verb:
                delim_at = i + len(verb.group(0))
                if delim_at < len(text) and text[delim_at] not in "\r\n":
                    end = text.find(text[delim_at], delim_at + 1)
                    if end >= 0:
                        out[i:end + 1] = [
                            "\n" if x == "\n" else " " for x in text[i:end + 1]
                        ]
                        i = end + 1
                        continue
            if i + 1 < len(text) and not text[i + 1].isalpha():
                out[i:i + 2] = "  "
                i += 2
            else:
                i += 1
        else:
            i += 1
    return "".join(out)


def brace_issues(masked: str) -> list[dict]:
    stack = []
    issues = []
    line = 1
    for at, char in enumerate(masked):
        if char == "\n":
            line += 1
        elif char == "{":
            stack.append((at, line))
        elif char == "}":
            if stack:
                stack.pop()
            else:
                issues.append({"kind": "unmatched_close", "line": line, "offset": at})
    issues.extend(
        {"kind": "unmatched_open", "line": line, "offset": at}
        for at, line in stack
    )
    return issues


def doubt_occurrences(text: str, masked: str, relative_path: str) -> list[dict]:
    occurrences = []
    for found in re.finditer(r"\\(unsure|illegible)\s*\{", masked):
        begin = found.end()
        level = 1
        end = begin
        while end < len(masked):
            char = masked[end]
            if char == "{":
                level += 1
            elif char == "}":
                level -= 1
                if level == 0:
                    break
            end += 1
        occurrences.append({
            "file": relative_path,
            "line": text.count("\n", 0, found.start()) + 1,
            "macro": found.group(1),
            "argument": text[begin:end],
            "argument_closed": level == 0,
        })
    return occurrences


def parse_hash_record(line: str):
    """Accept explicit sha256 records and the standard sha256sum layout."""
    line = line.strip()
    match = re.match(r"(?i)^sha-?256\s+(.+?)\s+([0-9a-f]{64})$", line)
    if match:
        return match.group(1).strip(), match.group(2).lower()
    match = re.match(r"(?i)^([0-9a-f]{64})\s+\*?(.+)$", line)
    if match:
        return match.group(2).strip(), match.group(1).lower()
    match = re.match(r"(?i)^sha-?256\s+([0-9a-f]{64})\s+(.+)$", line)
    if match:
        return match.group(2).strip(), match.group(1).lower()
    return None


class Validator:
    def __init__(self, root: Path, partial: bool):
        self.root = root.resolve()
        self.partial = partial
        self.errors = []
        self.warnings = []
        self.report = {
            "package": PREFIX,
            "root": str(self.root),
            "mode": "partial" if partial else "final",
            "scope": "Mechanical structure only; no claim of visual completeness or accuracy.",
            "expected_page_count": len(EXPECTED),
        }
        self.page_data = {}
        self.page_keys = []

    def error(self, code: str, detail, **extra):
        self.errors.append({"code": code, "detail": detail, **extra})

    def warn(self, code: str, detail, **extra):
        self.warnings.append({"code": code, "detail": detail, **extra})

    def read(self, path: Path):
        try:
            data = path.read_bytes()
            return data, data.decode("utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            self.error("file_read", str(exc), file=str(path.relative_to(self.root)))
            return None

    def check_pages(self):
        folder = self.root / "pages"
        expected_names = {page_name(*key) for key in EXPECTED}
        actual = {p.name for p in folder.glob("*.tex")} if folder.is_dir() else set()
        missing = [key for key in EXPECTED if page_name(*key) not in actual]
        extra = sorted(actual - expected_names)
        if extra:
            self.error("unexpected_pages", extra)
        if missing and not self.partial:
            self.error("missing_pages", [page_name(*key) for key in missing])
        present = [key for key in EXPECTED if page_name(*key) in actual]
        if present != EXPECTED[:len(present)]:
            self.error("nonsequential_pages", "Saved pages do not form a prefix of the prescribed reading order.")
        self.page_keys = present
        self.report["present_page_count"] = len(present)
        self.report["missing_pages"] = [{"cote": c, "scan": n} for c, n in missing]
        checks = []
        doubts = []
        for key in present:
            relative = "pages/" + page_name(*key)
            result = self.read(self.root / relative)
            if result is None:
                continue
            data, text = result
            self.page_data[key] = data
            masked = mask_tex(text)
            scan_markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", masked)
            cote_markers = re.findall(r"\\cotefile\s*\{\s*(\d+)\s*\}", masked)
            if scan_markers != [str(key[1])]:
                self.error("scanpage_marker", {"expected": key[1], "found": scan_markers}, file=relative)
            expected_cotes = [str(key[0])] if key in FIRST else []
            if cote_markers != expected_cotes:
                self.error("cotefile_marker", {"expected": expected_cotes, "found": cote_markers}, file=relative)
            leading = masked.lstrip()
            expected_leading = (
                rf"\\cotefile\s*\{{\s*{key[0]}\s*\}}\s*\\scanpage\s*\{{\s*{key[1]}\s*\}}"
                if key in FIRST else rf"\\scanpage\s*\{{\s*{key[1]}\s*\}}"
            )
            if not re.match(expected_leading, leading):
                self.error("page_start", "Required marker(s) are not at the start of the page fragment.", file=relative)
            problems = brace_issues(masked)
            if problems:
                self.error("unbalanced_braces", problems, file=relative)
            if re.search(r"\\(?:documentclass|usepackage)\b|\\(?:begin|end)\s*\{document\}", masked):
                self.error("preamble_in_fragment", "A document wrapper or preamble command appears in a page fragment.", file=relative)
            if not re.search(r"\\scanpage\s*\{[^}]+\}\s*\S", masked):
                self.error("empty_page_body", "No body follows the scanpage marker.", file=relative)
            occurrences = doubt_occurrences(text, masked, relative)
            doubts.extend(occurrences)
            for occurrence in occurrences:
                if occurrence["macro"] == "illegible" and not re.fullmatch(r"\s*\d+\s*", occurrence["argument"]):
                    self.error("illegible_count", occurrence, file=relative)
            checks.append({
                "cote": key[0], "scan": key[1], "file": relative,
                "bytes": len(data), "sha256": sha256(data),
                "doubt_count": len(occurrences),
            })
        self.report["pages"] = checks
        self.report["doubt_macro_counts"] = dict(Counter(d["macro"] for d in doubts))
        self.report["doubt_occurrences"] = doubts

    def check_combined(self):
        path = self.root / f"{PREFIX}_transcription.tex"
        if not path.exists():
            if not self.partial:
                self.error("missing_combined", path.name)
            self.report["combined"] = {"present": False}
            return
        result = self.read(path)
        if result is None:
            return
        data, text = result
        concatenated = b"".join(self.page_data[k] for k in EXPECTED if k in self.page_data)
        matches = data == concatenated
        if not matches:
            self.error("combined_concatenation", "Combined file does not exactly equal the saved page files concatenated in prescribed order.")
        masked = mask_tex(text)
        problems = brace_issues(masked)
        if problems:
            self.error("combined_braces", problems)
        self.report["combined"] = {
            "present": True, "file": path.name, "bytes": len(data),
            "sha256": sha256(data), "matches_page_concatenation": matches,
        }

    def check_inventory(self):
        path = self.root / f"{PREFIX}_inventory.csv"
        if not path.exists():
            self.error("missing_inventory", path.name)
            return
        try:
            with path.open(encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle)
                if reader.fieldnames != COLUMNS:
                    self.error("inventory_columns", {"expected": COLUMNS, "found": reader.fieldnames})
                    return
                rows = list(reader)
        except (OSError, UnicodeError, csv.Error) as exc:
            self.error("inventory_read", str(exc))
            return
        seen_elements = set()
        page_rows = defaultdict(list)
        last_page_index = -1
        for line, row in enumerate(rows, 2):
            if None in row:
                self.error("inventory_row_width", "Extra fields in CSV row.", line=line)
            if any(row.get(col) is None for col in COLUMNS):
                self.error("inventory_row_width", "Missing fields in CSV row.", line=line)
                continue
            try:
                key = int(row["cote"]), int(row["scan"])
            except ValueError:
                self.error("inventory_page_key", {"cote": row["cote"], "scan": row["scan"]}, line=line)
                continue
            if key not in EXPECTED:
                self.error("inventory_unexpected_page", list(key), line=line)
                continue
            index = EXPECTED.index(key)
            if index < last_page_index:
                self.error("inventory_order", "Page rows are out of prescribed order.", line=line)
            last_page_index = max(last_page_index, index)
            page_rows[key].append(row)
            if key not in self.page_keys:
                self.error("inventory_unsaved_page", list(key), line=line)
            if row["sheet_kind"] not in SHEET_KINDS:
                self.error("inventory_sheet_kind", row["sheet_kind"], line=line)
            if row["kind"] not in ELEMENT_KINDS:
                self.error("inventory_element_kind", row["kind"], line=line)
            if row["transcribed"] != "yes":
                self.error("inventory_not_transcribed", row["transcribed"], line=line)
            for col in ("element", "position", "first_words_or_objects"):
                if not row[col].strip():
                    self.error("inventory_blank_field", col, line=line)
            element_key = (*key, row["element"])
            if element_key in seen_elements:
                self.error("inventory_duplicate_element", list(element_key), line=line)
            seen_elements.add(element_key)
        for key in self.page_keys:
            if key not in page_rows:
                self.error("inventory_missing_page", list(key))
            elif len({r["sheet_kind"] for r in page_rows[key]}) != 1:
                self.error("inventory_sheet_kind_conflict", list(key))
        self.report["inventory"] = {
            "rows": len(rows),
            "pages": [{"cote": k[0], "scan": k[1], "rows": len(page_rows[k])}
                      for k in EXPECTED if k in page_rows],
        }

    def check_auxiliary(self):
        auxiliary = {}
        for suffix in ("doubts.md", "notes.md"):
            path = self.root / f"{PREFIX}_{suffix}"
            present = path.is_file()
            auxiliary[suffix] = {"present": present}
            if present:
                size = path.stat().st_size
                auxiliary[suffix]["bytes"] = size
                if size == 0:
                    self.error("empty_auxiliary", path.name)
            elif not self.partial:
                self.error("missing_auxiliary", path.name)
        self.report["auxiliary"] = auxiliary

    def check_progress(self):
        path = self.root / "progress.log"
        if not path.exists():
            self.error("missing_progress", "progress.log")
            return
        result = self.read(path)
        if result is None:
            return
        _, text = result
        lines = text.splitlines()
        if not lines or utc_time(lines[0]) is None:
            self.error("progress_start", "The first line must contain the initial current UTC timestamp.")
        done = defaultdict(list)
        audited = defaultdict(list)
        freeze_lines = []
        context_lines = []
        hashes = []
        timestamped = []
        for number, line in enumerate(lines, 1):
            stamp = utc_time(line)
            if stamp:
                timestamped.append((number, stamp))
            match = re.match(r"^(\d+)\s+scan\s+(\d+)\s+done\b", line)
            if match:
                key = int(match.group(1)), int(match.group(2))
                done[key].append(number)
                if stamp is None:
                    self.error("done_timestamp", line, line=number)
            match = re.match(r"^(?:(\d+)\s+)?scan\s+(\d+)\s+audited\b", line)
            if match:
                scan = int(match.group(2))
                matches = ([ (int(match.group(1)), scan) ] if match.group(1)
                           else [k for k in EXPECTED if k[1] == scan])
                if len(matches) != 1 or matches[0] not in EXPECTED:
                    self.error("audit_page_key", line, line=number)
                else:
                    audited[matches[0]].append(number)
                if stamp is None:
                    self.error("audit_timestamp", line, line=number)
            if line.startswith("transcription frozen"):
                freeze_lines.append(number)
                if stamp is None:
                    self.error("freeze_timestamp", line, line=number)
            if line.startswith("context opened"):
                context_lines.append(number)
                if stamp is None:
                    self.error("context_timestamp", line, line=number)
            parsed_hash = parse_hash_record(line)
            if parsed_hash:
                hashes.append((number, *parsed_hash))
        for (old_line, old_stamp), (new_line, new_stamp) in zip(timestamped, timestamped[1:]):
            if new_stamp < old_stamp:
                self.warn("timestamp_order", {"previous_line": old_line, "line": new_line,
                                              "reason": "UTC timestamp decreases; inspect the record."})
        ordered_done = sorted((v[0], k) for k, v in done.items())
        if [key for _, key in ordered_done] != self.page_keys:
            self.error("progress_done_sequence", {
                "expected": [list(k) for k in self.page_keys],
                "found": [list(k) for _, k in ordered_done],
            })
        for key, occurrences in done.items():
            if len(occurrences) != 1:
                self.error("duplicate_done", {"page": list(key), "lines": occurrences})
        for key, occurrences in audited.items():
            if key not in done or occurrences[0] < done[key][0]:
                self.error("audit_before_done", {"page": list(key), "lines": occurrences})
        frozen = bool(freeze_lines)
        if len(freeze_lines) > 1:
            self.warn("multiple_freezes", freeze_lines)
        if not self.partial and not frozen:
            self.error("missing_freeze", "No transcription frozen record.")
        if context_lines and (not frozen or min(context_lines) < min(freeze_lines)):
            self.error("context_before_freeze", {"context_lines": context_lines, "freeze_lines": freeze_lines})
        if not self.partial and not context_lines:
            self.error("missing_context_open_record", "No context opened record.")
        checks = []
        if frozen:
            freeze_at = min(freeze_lines)
            for key in EXPECTED:
                occurrences = audited.get(key, [])
                if not occurrences or min(occurrences) > freeze_at:
                    self.error("missing_prefreeze_audit", list(key))
            expected_paths = ["pages/" + page_name(*k) for k in EXPECTED]
            expected_paths.append(f"{PREFIX}_transcription.tex")
            logged = defaultdict(list)
            for number, recorded_path, digest in hashes:
                candidate = Path(recorded_path)
                if candidate.is_absolute():
                    try:
                        relative = str(candidate.resolve().relative_to(self.root))
                    except ValueError:
                        self.warn("hash_outside_package", recorded_path, line=number)
                        continue
                else:
                    relative = recorded_path.removeprefix("./")
                logged[relative].append((number, digest))
            for relative in expected_paths:
                records = [(n, d) for n, d in logged[relative] if n <= freeze_at]
                if not records:
                    self.error("missing_frozen_hash", relative)
                    continue
                try:
                    current = sha256((self.root / relative).read_bytes())
                except OSError as exc:
                    self.error("frozen_hash_read", str(exc), file=relative)
                    continue
                matches = all(digest == current for _, digest in records)
                if not matches:
                    self.error("frozen_hash_changed", relative)
                checks.append({"file": relative, "sha256": current,
                               "logged_lines": [n for n, _ in records], "unchanged": matches})
            later_verifications = [n for n, line in enumerate(lines, 1)
                                   if n > freeze_at and re.search(r"(?i)(hash|sha-?256).*(unchanged|verified)", line)]
            if not self.partial and not later_verifications:
                self.error("missing_final_hash_statement", "No post-freeze statement that hashes were verified or unchanged.")
            if context_lines and later_verifications and max(later_verifications) < max(context_lines):
                self.error("hash_statement_before_context", "Final hash verification precedes context opening.")
        self.report["progress"] = {
            "lines": len(lines), "done_pages": len(done), "audited_pages": len(audited),
            "freeze_lines": freeze_lines, "context_open_lines": context_lines,
            "frozen_hash_checks": checks,
        }

    def run(self):
        self.check_pages()
        self.check_combined()
        self.check_inventory()
        self.check_auxiliary()
        self.check_progress()
        self.report["errors"] = self.errors
        self.report["warnings"] = self.warnings
        self.report["mechanical_checks_passed"] = not self.errors
        return self.report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="Package directory (default: this script's parent package).")
    parser.add_argument("--partial", action="store_true",
                        help="Allow the unread tail of pages and unfinished final-stage files; check all existing records.")
    parser.add_argument("--compact", action="store_true", help="Emit JSON without indentation.")
    args = parser.parse_args()
    report = Validator(args.root, args.partial).run()
    json.dump(report, sys.stdout, ensure_ascii=False, indent=None if args.compact else 2)
    sys.stdout.write("\n")
    return 0 if report["mechanical_checks_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
