#!/usr/bin/env python3
"""Read-only consistency checks for the completed MPL_98 package.

Run only once the root has announced that final assembly is ready:
    python scripts/validate_final_package.py

The JSON report goes to stdout; exit status is 0 on success and 1 on error.
No file, hash manifest, audit record, checkpoint, or progress log is written.
The existing verify_frozen.py is called without --log and with bytecode writes
disabled. Transcription text and supplied scans are never interpreted: only
the existing verifier reads frozen transcription bytes, for hashing.

The note count is derived from research/note_plan.json, never hardcoded.
Sentence counts use the explicitly authored `sentences` arrays. A limited
punctuation heuristic additionally warns about possible compound entries.
Confidence checks establish presence of a rating and reason, not their merit.
Markdown link checks establish file existence; URL contents and fragment
anchors are outside this script's scope.
"""

from __future__ import annotations

import argparse
from collections import Counter
import csv
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import unicodedata
from urllib.parse import unquote, urlsplit


ID_RE = re.compile(r"\bMPL98\.[A-Z]+[0-9]+\b")
EVENT_COLUMNS = ["statement_id", "date", "who", "type", "outcome"]
EVENT_TYPES = {
    "targeted proof check",
    "independent re-proof",
    "computation or formal certificate",
    "used and rechecked in this run",
    "carried as background without fault found",
    "refuted, with the refined statement's id",
}
REQUIRED_FILES = [
    "MPL_98_transcription.tex",
    "MPL_98_inventory.csv",
    "MPL_98_doubts.md",
    "MPL_98_notes.md",
    "CHECK_EVENTS.tsv",
    "CHECKPOINT_STATE.md",
    "progress.log",
    "research/note_entries.json",
    "research/note_plan.json",
    "research/context_searches.jsonl",
    "research/frozen_sha256.json",
    "research/root_proof_checks.md",
    "research/primary_sources.md",
    "research/norm_research.md",
    "research/cohomology_research.md",
    "research/boundedness_research.md",
    "research/cohomology_final_review.md",
    "scripts/verify_frozen.py",
]
OWN_EXAMPLE_RE = re.compile(r"\bown\s+idea\b|\b(?:counter)?examples?\b", re.I)
RATING_RE = re.compile(
    r"^(?:(?:very|fairly|moderately)\s+)?"
    r"(?:high|medium|moderate|low|conditional|tentative)"
    r"(?:\s+confidence)?\b", re.I
)
WORD_RE = re.compile(r"[^\W\d_][\w’'-]*", re.UNICODE)


class Validator:
    def __init__(self, base: Path):
        self.base = base.resolve()
        self.errors: list[dict] = []
        self.warnings: list[dict] = []
        self.counts: dict = {}
        self.details: dict = {}
        self.text_cache: dict[Path, str | None] = {}

    def label(self, path: Path) -> str:
        try:
            return str(path.resolve().relative_to(self.base))
        except ValueError:
            return str(path)

    def error(self, code: str, message: str, where: str = ""):
        self.errors.append({"code": code, "where": where, "message": message})

    def warning(self, code: str, message: str, where: str = ""):
        self.warnings.append({"code": code, "where": where, "message": message})

    def check_controls(self, value: str, where: str, allowed: str = ""):
        bad = []
        formats = []
        for i, char in enumerate(value):
            if char in allowed:
                continue
            category = unicodedata.category(char)
            if category in {"Cc", "Cs"} or char == "\ufffd":
                bad.append((i, f"U+{ord(char):04X}"))
            elif category == "Cf":
                formats.append((i, f"U+{ord(char):04X}"))
        if bad:
            self.error("control_or_replacement_character",
                       f"{len(bad)} forbidden characters; first offsets/codepoints: {bad[:10]}",
                       where)
        if formats:
            self.warning("unicode_format_character",
                         f"Review {len(formats)} Unicode format characters: {formats[:10]}",
                         where)

    def inspect_strings(self, value, where: str):
        if isinstance(value, str):
            self.check_controls(value, where)
        elif isinstance(value, dict):
            for key, child in value.items():
                self.check_controls(str(key), where + "/<key>")
                self.inspect_strings(child, where + "/" + str(key))
        elif isinstance(value, list):
            for i, child in enumerate(value):
                self.inspect_strings(child, f"{where}[{i}]")

    def text(self, path: Path) -> str | None:
        path = path.resolve()
        if path not in self.text_cache:
            try:
                self.text_cache[path] = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                self.error("unreadable_utf8_file", str(exc), self.label(path))
                self.text_cache[path] = None
        return self.text_cache[path]

    @staticmethod
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON object key: {key!r}")
            result[key] = value
        return result

    def records(self, relative: str, jsonl: bool = False) -> list[dict]:
        source = self.text(self.base / relative)
        if source is None:
            return []
        try:
            if jsonl:
                data = [json.loads(line, object_pairs_hook=self.unique_object)
                        for line in source.splitlines() if line.strip()]
            else:
                data = json.loads(source, object_pairs_hook=self.unique_object)
        except (ValueError, json.JSONDecodeError) as exc:
            self.error("invalid_json", str(exc), relative)
            return []
        self.inspect_strings(data, relative)
        if not isinstance(data, list):
            self.error("record_list_required", "Expected a JSON list of records.", relative)
            return []
        good = []
        for i, item in enumerate(data):
            if not isinstance(item, dict):
                self.error("record_object_required", "Expected an object.", f"{relative}[{i}]")
                continue
            ident = item.get("id")
            if not isinstance(ident, str) or ID_RE.fullmatch(ident) is None:
                self.error("invalid_note_id", repr(ident), f"{relative}[{i}]")
                continue
            good.append(item)
        counts = Counter(item["id"] for item in good)
        duplicate = sorted(k for k, n in counts.items() if n != 1)
        if duplicate:
            self.error("duplicate_note_ids", ", ".join(duplicate), relative)
        return good

    def required(self, extra: list[str]):
        required = list(dict.fromkeys(REQUIRED_FILES + extra))
        for name in required:
            path = Path(name)
            if not path.is_absolute():
                path = self.base / path
            if not path.is_file():
                self.error("required_file_missing", "Required file does not exist.", name)
            elif path.stat().st_size == 0:
                self.error("required_file_empty", "Required file is empty.", name)
        self.counts["required_files"] = len(required)

    def note_records(self):
        notes = self.records("research/note_entries.json")
        plan = self.records("research/note_plan.json")
        searches = self.records("research/context_searches.jsonl", jsonl=True)
        note_ids = {x["id"] for x in notes}
        plan_ids = {x["id"] for x in plan}
        search_ids = {x["id"] for x in searches}
        self.counts.update(note_entries=len(notes), planned_notes=len(plan),
                           context_search_records=len(searches))
        if not plan_ids:
            self.error("empty_note_plan", "The expected ID set must be nonempty.")
        for label, actual in [("merged entries", note_ids), ("context searches", search_ids)]:
            if actual != plan_ids:
                self.error("note_id_set_mismatch",
                           f"Missing: {sorted(plan_ids-actual)}; unexpected: {sorted(actual-plan_ids)}",
                           label)
        total_sentences = 0
        own_notes = []
        for item in notes:
            ident = item["id"]
            sentences = item.get("sentences")
            if not isinstance(sentences, list) or not 1 <= len(sentences) <= 4:
                self.error("sentence_count", "Expected 1–4 explicitly authored sentence entries.", ident)
                continue
            total_sentences += len(sentences)
            for i, sentence in enumerate(sentences, 1):
                if not isinstance(sentence, str) or not sentence.strip():
                    self.error("empty_sentence", "Sentence must be a nonempty string.", f"{ident}:{i}")
                    continue
                # Only a warning: punctuation inside quotations/references is ambiguous.
                plain = re.sub(r"\\\(.*?\\\)|\\\[.*?\\\]|\$[^$]*\$", " MATH ", sentence)
                plain = re.sub(r"\b(?:e\.g|i\.e|et al|cf|etc|pp?|no|nos|Fig|Prop|Thm)\.",
                               "ABBR", plain, flags=re.I)
                if re.search(r"[.!?][”’\"')\]]*\s+[A-Z][a-z]", plain):
                    self.warning("possible_multiple_sentences",
                                 "One authored sentence entry may contain more than one sentence; review punctuation.",
                                 f"{ident}:{i}")
            kind = item.get("kind", "")
            if isinstance(kind, str) and OWN_EXAMPLE_RE.search(kind):
                own_notes.append(ident)
                confidence = item.get("confidence")
                reason = item.get("confidence_reason") or item.get("reason")
                if not isinstance(confidence, str) or not confidence.strip():
                    self.error("confidence_missing", "Own-idea/example note needs a confidence statement.", ident)
                    continue
                match = RATING_RE.match(confidence.strip())
                if match is None:
                    self.warning("confidence_rating_unparsed",
                                 "Confidence exists but its rating is not one of the recognized textual levels.", ident)
                inline_reason = confidence.strip()[match.end():] if match else ""
                inline_reason = re.sub(
                    r"^[\s:;,—–-]*(?:(?:for|because|by|based on|from|given|owing to)\b)?",
                    "", inline_reason, flags=re.I
                )
                explicit_reason = isinstance(reason, str) and len(WORD_RE.findall(reason)) >= 2
                if not explicit_reason and len(WORD_RE.findall(inline_reason)) < 2:
                    self.error("confidence_reason_missing",
                               "Supply an explicit reason or a confidence statement containing a reason.", ident)
        self.counts["authored_sentence_entries"] = total_sentences
        self.counts["own_idea_or_example_notes"] = len(own_notes)
        self.details["confidence_required_ids"] = own_notes
        return notes, plan_ids

    @staticmethod
    def normalized(value: str) -> str:
        return " ".join(unicodedata.normalize("NFC", value).split())

    def rendered_notes(self, notes: list[dict], expected: set[str]):
        relative = "MPL_98_notes.md"
        source = self.text(self.base / relative)
        if source is None:
            return
        self.check_controls(source, relative, allowed="\n\r\t")
        headings = []
        for match in re.finditer(r"(?m)^ {0,3}#{1,6}\s+(.+)$", source):
            ids = ID_RE.findall(match.group(1))
            if ids:
                if len(ids) != 1:
                    self.error("ambiguous_note_heading", repr(ids), relative)
                headings.append((ids[0], match.start(), match.end()))
        counts = Counter(ident for ident, _, _ in headings)
        duplicates = sorted(k for k, n in counts.items() if n > 1)
        if duplicates:
            self.error("duplicate_note_headings", ", ".join(duplicates), relative)
        actual = set(counts)
        if actual != expected:
            self.error("rendered_note_ids_mismatch",
                       f"Missing headings: {sorted(expected-actual)}; unexpected: {sorted(actual-expected)}",
                       relative)
        blocks = {}
        for i, (ident, start, end) in enumerate(headings):
            stop = headings[i+1][1] if i+1 < len(headings) else len(source)
            blocks.setdefault(ident, self.normalized(source[end:stop]))
        for item in notes:
            ident = item["id"]
            if ident not in blocks:
                continue
            sentences = item.get("sentences", [])
            if isinstance(sentences, list):
                for n, sentence in enumerate(sentences, 1):
                    if isinstance(sentence, str) and self.normalized(sentence) not in blocks[ident]:
                        self.warning("rendered_sentence_not_literal",
                                     "Authored sentence not found literally after whitespace/NFC normalization; check formatting or assembly.",
                                     f"{ident}:{n}")
            kind = item.get("kind", "")
            confidence = item.get("confidence", "")
            if (isinstance(kind, str) and OWN_EXAMPLE_RE.search(kind)
                    and isinstance(confidence, str) and confidence.strip()
                    and self.normalized(confidence) not in blocks[ident]):
                self.error("rendered_confidence_missing",
                           "The own-idea/example confidence statement is absent from its note block.", ident)
        self.counts["rendered_note_headings"] = len(headings)

    def event_ledger(self):
        relative = "CHECK_EVENTS.tsv"
        source = self.text(self.base / relative)
        if source is None:
            return
        self.check_controls(source, relative, allowed="\t\r\n")
        try:
            reader = csv.reader(io.StringIO(source, newline=""), delimiter="\t", strict=True)
            rows = list(reader)
        except csv.Error as exc:
            self.error("invalid_tsv", str(exc), relative)
            return
        if not rows or rows[0] != EVENT_COLUMNS:
            self.error("ledger_columns", f"Expected exactly {EVENT_COLUMNS}; got {rows[0] if rows else []}", relative)
        event_count = 0
        type_counts = Counter()
        for row_number, row in enumerate(rows[1:], 2):
            if len(row) != len(EVENT_COLUMNS):
                self.error("ledger_field_count", f"Expected 5 fields; found {len(row)}.", f"{relative}:{row_number}")
                continue
            for column, value in zip(EVENT_COLUMNS, row):
                self.check_controls(value, f"{relative}:{row_number}:{column}")
                if not value.strip():
                    self.error("ledger_empty_field", "Field is empty.", f"{relative}:{row_number}:{column}")
            if row[3] not in EVENT_TYPES:
                self.error("ledger_event_type", repr(row[3]), f"{relative}:{row_number}")
            type_counts[row[3]] += 1
            event_count += 1
        if event_count == 0:
            self.error("ledger_empty", "No check events were present.", relative)
        self.counts["check_events"] = event_count
        self.details["event_type_counts"] = dict(sorted(type_counts.items()))

    @staticmethod
    def without_code(source: str) -> str:
        result = []
        fence = None
        for line in source.splitlines():
            match = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
            if match:
                mark = match.group(1)
                if fence is None:
                    fence = (mark[0], len(mark))
                elif mark[0] == fence[0] and len(mark) >= fence[1]:
                    fence = None
                continue
            if fence is None:
                result.append(re.sub(r"(`+).*?\1", "", line))
        return "\n".join(result)

    @staticmethod
    def link_targets(source: str):
        """Common inline/reference Markdown targets, including nested parentheses."""
        for match in re.finditer(r"!?\[[^\]\n]*\]\(", source):
            i = match.end()
            while i < len(source) and source[i].isspace():
                i += 1
            if i < len(source) and source[i] == "<":
                end = source.find(">", i+1)
                if end >= 0:
                    yield source[i+1:end]
                continue
            target = []
            depth = 0
            while i < len(source):
                char = source[i]
                if char == "\\" and i+1 < len(source):
                    target.append(source[i+1])
                    i += 2
                    continue
                if char == "(" :
                    depth += 1
                elif char == ")":
                    if depth == 0:
                        break
                    depth -= 1
                elif char.isspace() and depth == 0:
                    break
                target.append(char)
                i += 1
            if target:
                yield "".join(target)
        for match in re.finditer(r"(?m)^ {0,3}\[(?!\^)[^\]\n]+\]:\s*(?:<([^>]+)>|(\S+))", source):
            yield match.group(1) or match.group(2)
        for match in re.finditer(r"<(sandbox:[^>]+|file:[^>]+)>", source):
            yield match.group(1)

    def markdown_links(self):
        # Only documents, not transcription fragments, scans, or source archives.
        documents = sorted(set(self.base.glob("*.md"))
                           | set((self.base / "research").glob("*.md"))
                           | set((self.base / "scripts").glob("*.md")))
        checked = external = fragments = 0
        for path in documents:
            source = self.text(path)
            if source is None:
                continue
            self.check_controls(source, self.label(path), allowed="\n\r\t")
            for target in self.link_targets(self.without_code(source)):
                try:
                    parsed = urlsplit(target)
                except ValueError as exc:
                    self.error("invalid_link_target", str(exc), self.label(path))
                    continue
                if target.startswith("#"):
                    fragments += 1
                    continue
                if parsed.scheme and parsed.scheme not in {"sandbox", "file"}:
                    external += 1
                    continue
                if parsed.netloc and parsed.scheme != "file":
                    external += 1
                    continue
                filename = unquote(parsed.path)
                if not filename:
                    fragments += 1
                    continue
                local = Path(filename)
                if not local.is_absolute():
                    local = path.parent / local
                local = local.resolve()
                checked += 1
                if not local.exists():
                    self.error("broken_local_link", target, self.label(path))
                else:
                    try:
                        local.relative_to(self.base)
                    except ValueError:
                        self.warning("link_outside_package",
                                     f"Exists locally but is outside package root: {target}", self.label(path))
                if parsed.fragment:
                    fragments += 1
        self.counts.update(markdown_documents=len(documents), local_file_links=checked,
                           external_links_not_fetched=external, fragment_anchors_not_verified=fragments)

    def frozen_hashes(self):
        manifest_path = self.base / "research/frozen_sha256.json"
        source = self.text(manifest_path)
        if source is not None:
            try:
                manifest = json.loads(source, object_pairs_hook=self.unique_object)
                files = manifest.get("files", {})
                if not isinstance(files, dict) or len(files) != 44:
                    self.error("frozen_manifest_count", "Expected the 44 original frozen transcription entries.", self.label(manifest_path))
                self.counts["frozen_manifest_files"] = len(files) if isinstance(files, dict) else None
                self.details["frozen_utc"] = manifest.get("frozen_utc")
            except (ValueError, AttributeError) as exc:
                self.error("invalid_frozen_manifest", str(exc), self.label(manifest_path))
        verifier = self.base / "scripts/verify_frozen.py"
        if not verifier.is_file():
            self.error("hash_verifier_missing", "Cannot run the existing frozen verifier.", self.label(verifier))
            return
        environment = dict(os.environ)
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        try:
            result = subprocess.run([sys.executable, "-B", str(verifier)],
                                    cwd=self.base, env=environment,
                                    capture_output=True, text=True, timeout=60, check=False)
        except (OSError, subprocess.TimeoutExpired) as exc:
            self.error("hash_verifier_failed", str(exc), self.label(verifier))
            return
        self.details["frozen_verifier"] = {
            "command": [sys.executable, "-B", "scripts/verify_frozen.py"],
            "log_flag_supplied": False,
            "returncode": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
        }
        if result.returncode:
            self.error("frozen_hash_mismatch", result.stderr.strip() or result.stdout.strip(), self.label(verifier))

    def report(self):
        return {
            "status": "passed" if not self.errors else "failed",
            "base": str(self.base),
            "read_only": True,
            "counts": self.counts,
            "details": self.details,
            "errors": self.errors,
            "warnings": self.warnings,
            "limitations": [
                "Mechanical consistency only; no manuscript reading or mathematical certification.",
                "The expected note count is derived from note_plan.json; its ID set is checked against both other registries.",
                "Sentence counts use the authored sentences arrays; punctuation warnings require human review.",
                "Confidence checks establish explicit presence of a rating and reason, not their evidential adequacy.",
                "Markdown file targets are checked locally; external URL contents and fragment anchors are not verified.",
                "Frozen transcription bytes are read only by the existing verifier, without its --log option.",
            ],
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base", type=Path, default=Path(__file__).resolve().parents[1],
                        help="Completed package directory (default: script's parent work directory).")
    parser.add_argument("--require", action="append", default=[], metavar="PATH",
                        help="Additional required file, relative to the package root unless absolute.")
    args = parser.parse_args()
    validator = Validator(args.base)
    validator.required(args.require)
    notes, expected = validator.note_records()
    validator.rendered_notes(notes, expected)
    validator.event_ledger()
    validator.markdown_links()
    validator.frozen_hashes()
    print(json.dumps(validator.report(), ensure_ascii=False, indent=2))
    return 1 if validator.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
