#!/usr/bin/env python3
"""Check final transcription artifacts without compiling or executing their content.

Run only after all first and blind second readings have been committed.
The default output directory is the parent of this script's directory.
The only file written is OUT/work/final_validation.json.

TSV evidence collections may encode supporting_crops as JSON objects containing
crop and coords (or box), or as a JSON list of those objects. A list of path
strings is also supported when matching supporting_boxes/supporting_coords are
provided. Primary evidence uses crop plus coords, box, or x0/y0/x1/y1.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any


IDENTIFIER = "SP117_CW_97+123+162-1"
EXPECTED_PAGES = 15
COMBINED_NAME = IDENTIFIER + "_transcription.tex"
COLLATION_NAME = IDENTIFIER + "_collation.tsv"
INVENTORY_NAME = IDENTIFIER + "_inventory.csv"
REQUIRED_TOP_LEVEL = (
    COMBINED_NAME,
    IDENTIFIER + "_changes.md",
    COLLATION_NAME,
    INVENTORY_NAME,
    IDENTIFIER + "_doubts.md",
    IDENTIFIER + "_notes.md",
    IDENTIFIER + "_sheet_feedback.md",
    IDENTIFIER + "_hand_log.md",
    "CHECK_EVENTS.tsv",
    "progress.log",
    "PREAMBLE.tex",
)
SHEET_KINDS = {
    "text", "reused_typed", "typescript", "letter", "list",
    "cancelled_draft", "cover",
}
INVENTORY_KINDS = {
    "text", "display", "diagram", "drawing", "margin note",
    "insertion", "deletion",
}
CHANGE_KINDS = {
    "misread word",
    "misread symbol or index",
    "omission",
    "text not on the page",
    "deletion state (struck given live or live given struck)",
    "insertion or placement",
    "abbreviation expanded or spelling modernised",
    r"readable ink left as \ill{}",
    "drawing or diagram",
    "other",
}
CONFIDENCES = {"high", "medium", "low"}
COORDINATE_KEYS = ("x0", "y0", "x1", "y1")
DECISION_KEYS = {
    "box", "first", "second", "final", "decision",
    "changed", "reason", "crop", "coords",
}


@dataclass
class Table:
    columns: list[str]
    rows: list[dict[str, str]]


class Validator:
    def __init__(self, out: Path) -> None:
        self.out = out.resolve()
        self.work = self.out / "work"
        self.second = self.out / "second"
        self.errors: list[str] = []
        self.counts: Counter[str] = Counter()
        self.page_counts: dict[str, dict[str, Any]] = {}
        self.crop_files: set[str] = set()
        self.pages: list[str] = []

    def error(self, where: Any, message: str) -> None:
        self.errors.append(f"{where}: {message}")

    def nonempty_file(self, path: Path, *, report: bool = True) -> bool:
        try:
            if not path.is_file():
                if report:
                    self.error(path, "required file is missing or is not a regular file")
                return False
            if path.stat().st_size == 0:
                if report:
                    self.error(path, "required file is empty")
                return False
            return True
        except OSError as exc:
            if report:
                self.error(path, f"cannot inspect file: {exc}")
            return False

    def read_json(self, path: Path) -> Any:
        if not self.nonempty_file(path):
            return None
        try:
            return json.loads(path.read_text(encoding="utf-8-sig"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            self.error(path, f"cannot read JSON: {exc}")
            return None

    def read_table(self, path: Path, delimiter: str) -> Table | None:
        if not self.nonempty_file(path):
            return None
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle, delimiter=delimiter)
                columns = reader.fieldnames
                if not columns:
                    self.error(path, "table has no header")
                    return None
                if any(not name or name != name.strip() for name in columns):
                    self.error(path, "header names must be nonempty and have no outer whitespace")
                duplicates = [name for name, n in Counter(columns).items() if n > 1]
                if duplicates:
                    self.error(path, f"duplicate header names: {duplicates}")
                rows: list[dict[str, str]] = []
                for row_number, raw in enumerate(reader, 2):
                    if None in raw:
                        self.error(path, f"row {row_number} has more cells than the header")
                    if any(value is None for key, value in raw.items() if key is not None):
                        self.error(path, f"row {row_number} has missing cells")
                    row = {
                        str(key): value if isinstance(value, str) else ""
                        for key, value in raw.items() if key is not None
                    }
                    if any(value != "" for value in row.values()):
                        rows.append(row)
                return Table(list(columns), rows)
        except (OSError, UnicodeError, csv.Error) as exc:
            self.error(path, f"cannot read table: {exc}")
            return None

    def require_columns(self, table: Table, names: set[str], where: Any) -> bool:
        missing = names - set(table.columns)
        if missing:
            self.error(where, f"missing columns: {sorted(missing)}")
            return False
        return True

    @staticmethod
    def unescaped(line: str, index: int) -> bool:
        backslashes = 0
        index -= 1
        while index >= 0 and line[index] == "\\":
            backslashes += 1
            index -= 1
        return backslashes % 2 == 0

    def check_tex(self, path: Path) -> bool:
        if not self.nonempty_file(path):
            return False
        try:
            content = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as exc:
            self.error(path, f"cannot read TeX fragment: {exc}")
            return False
        opened: list[tuple[int, int]] = []
        has_noncomment_content = False
        for line_number, line in enumerate(content.splitlines(), 1):
            for column, character in enumerate(line, 1):
                index = column - 1
                if character == "%" and self.unescaped(line, index):
                    break
                if not character.isspace():
                    has_noncomment_content = True
                if character not in "{}" or not self.unescaped(line, index):
                    continue
                if character == "{":
                    opened.append((line_number, column))
                elif opened:
                    opened.pop()
                else:
                    self.error(path, f"unmatched closing brace at {line_number}:{column}")
        if not has_noncomment_content:
            self.error(path, "TeX fragment contains only comments or whitespace")
        if opened:
            locations = ", ".join(f"{line}:{col}" for line, col in opened[:12])
            suffix = " ..." if len(opened) > 12 else ""
            self.error(path, f"{len(opened)} unmatched opening brace(s) at {locations}{suffix}")
        return True

    def parse_coords(self, value: Any, where: Any) -> list[float] | None:
        parsed = value
        if isinstance(parsed, str):
            raw = parsed.strip()
            if not raw:
                self.error(where, "coordinate box is empty")
                return None
            try:
                parsed = json.loads(raw)
            except json.JSONDecodeError:
                parsed = re.split(r"[\s,;]+", raw.strip("[]() \t\r\n"))
        if isinstance(parsed, dict) and all(key in parsed for key in COORDINATE_KEYS):
            parsed = [parsed[key] for key in COORDINATE_KEYS]
        if not isinstance(parsed, (list, tuple)) or len(parsed) != 4:
            self.error(where, "coordinate box must contain exactly four numbers")
            return None
        coordinates: list[float] = []
        for component in parsed:
            if isinstance(component, bool) or not isinstance(component, (int, float, str)):
                self.error(where, "coordinate box contains a nonnumeric value")
                return None
            try:
                number = float(component)
            except (ValueError, TypeError, OverflowError):
                self.error(where, "coordinate box contains a nonnumeric value")
                return None
            if not math.isfinite(number):
                self.error(where, "coordinate box contains a nonfinite number")
                return None
            coordinates.append(number)
        x0, y0, x1, y1 = coordinates
        if x0 < 0 or y0 < 0 or x1 <= x0 or y1 <= y0:
            self.error(where, "coordinate box must satisfy 0 <= x0 < x1 and 0 <= y0 < y1")
            return None
        return coordinates

    @staticmethod
    def coords_from(record: dict[str, Any]) -> Any:
        if record.get("coords") not in (None, ""):
            return record["coords"]
        if all(key in record for key in COORDINATE_KEYS):
            return [record[key] for key in COORDINATE_KEYS]
        return record.get("box")

    def resolve_crop(self, value: Any, owner: Path, where: Any) -> Path | None:
        if not isinstance(value, str) or not value.strip():
            self.error(where, "crop must name an existing nonempty local file")
            return None
        given = Path(value.strip()).expanduser()
        if given.is_absolute():
            candidates = [given]
        else:
            candidates = [
                self.out / given,
                self.out.parent / given,
                owner.parent / given,
                self.out / "crops" / given,
            ]
        distinct: dict[str, Path] = {}
        for candidate in candidates:
            resolved = candidate.resolve()
            distinct[str(resolved)] = resolved
        existing = [path for path in distinct.values() if path.is_file()]
        if not existing:
            self.error(where, f"crop file does not exist: {value}")
            return None
        if len(existing) > 1:
            self.error(where, f"crop path resolves ambiguously: {value}")
            return None
        path = existing[0]
        if not self.nonempty_file(path):
            return None
        self.crop_files.add(str(path))
        return path

    def check_evidence(self, crop: Any, coords: Any, owner: Path,
                       where: Any, category: str) -> None:
        self.counts[category + "_crop_references"] += 1
        self.resolve_crop(crop, owner, where)
        self.parse_coords(coords, where)

    def decode_collection(self, value: Any, where: Any) -> Any:
        if isinstance(value, str):
            value = value.strip()
            if not value:
                return []
            if value[:1] in "[{":
                try:
                    return json.loads(value)
                except json.JSONDecodeError as exc:
                    self.error(where, f"invalid JSON evidence collection: {exc}")
                    return []
        return value

    def supporting_evidence(self, record: dict[str, Any],
                            owner: Path, where: Any) -> None:
        raw = record.get("supporting_crops")
        if raw in (None, "", []):
            return
        support = self.decode_collection(raw, where)
        if isinstance(support, dict):
            if "crop" in support or "path" in support:
                support = [support]
            else:
                support = [
                    {"crop": crop, "coords": coords}
                    for crop, coords in support.items()
                ]
        elif isinstance(support, str):
            support = [support]
        if not isinstance(support, list):
            self.error(where, "supporting_crops must be a list, object, or path string")
            return
        parallel = self.decode_collection(
            record.get("supporting_boxes", record.get("supporting_coords")), where
        )
        for number, item in enumerate(support, 1):
            label = f"{where}, supporting crop {number}"
            if isinstance(item, dict):
                crop = item.get("crop", item.get("path"))
                coords = self.coords_from(item)
            elif isinstance(item, str):
                crop = item
                if isinstance(parallel, list) and len(parallel) == len(support):
                    coords = parallel[number - 1]
                elif isinstance(parallel, dict):
                    coords = parallel.get(item)
                else:
                    coords = None
            else:
                self.error(label, "supporting crop entry must be an object or path string")
                continue
            self.check_evidence(crop, coords, owner, label, "supporting")

    def inventory_record(self, row: Any, where: Any) -> None:
        if not isinstance(row, dict):
            self.error(where, "inventory entry must be an object")
            return
        if row.get("sheet_kind") not in SHEET_KINDS:
            self.error(where, f"invalid inventory sheet_kind: {row.get('sheet_kind')!r}")
        if row.get("kind") not in INVENTORY_KINDS:
            self.error(where, f"invalid inventory kind: {row.get('kind')!r}")
        if row.get("transcribed") != "yes":
            self.error(where, "inventory transcribed must be exactly yes")

    def change_record(self, row: Any, owner: Path, where: Any) -> None:
        if not isinstance(row, dict):
            self.error(where, "change entry must be an object")
            return
        if row.get("kind") not in CHANGE_KINDS:
            self.error(where, f"invalid change/collation kind: {row.get('kind')!r}")
        if row.get("confidence") not in CONFIDENCES:
            self.error(where, f"invalid confidence: {row.get('confidence')!r}")
        self.check_evidence(row.get("crop"), self.coords_from(row), owner, where, "primary")
        self.supporting_evidence(row, owner, where)

    def load_order(self) -> None:
        path = self.work / "page_order.json"
        data = self.read_json(path)
        entries = data.get("pages") if isinstance(data, dict) else data
        if not isinstance(entries, list):
            self.error(path, "expected a list of page objects, or an object with a pages list")
            return
        self.counts["page_order_entries"] = len(entries)
        if len(entries) != EXPECTED_PAGES:
            self.error(path, f"requires exactly {EXPECTED_PAGES} entries, found {len(entries)}")
        stems: list[str] = []
        for number, entry in enumerate(entries, 1):
            if not isinstance(entry, dict):
                self.error(path, f"entry {number} is not an object")
                continue
            codex_file = entry.get("codex_file")
            if not isinstance(codex_file, str) or not codex_file.strip():
                self.error(path, f"entry {number} lacks a nonempty codex_file")
                continue
            stem = PurePosixPath(codex_file.replace("\\", "/")).stem
            if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.+-]*", stem):
                self.error(path, f"entry {number} has an unsafe or empty codex_file stem")
                continue
            stems.append(stem)
        duplicates = [stem for stem, n in Counter(stems).items() if n > 1]
        if duplicates:
            self.error(path, f"duplicate page stems: {duplicates}")
        self.pages = list(dict.fromkeys(stems))
        self.counts["unique_pages"] = len(self.pages)
        if len(self.pages) != EXPECTED_PAGES:
            self.error(path, f"requires exactly {EXPECTED_PAGES} unique valid page stems")

    def check_top_level(self) -> None:
        for name in REQUIRED_TOP_LEVEL:
            if self.nonempty_file(self.out / name):
                self.counts["required_top_level_files_present"] += 1
        self.check_tex(self.out / COMBINED_NAME)
        inventory_path = self.out / INVENTORY_NAME
        inventory = self.read_table(inventory_path, ",")
        if inventory is not None:
            self.require_columns(inventory, {"sheet_kind", "kind", "transcribed"}, inventory_path)
            self.counts["inventory_rows"] = len(inventory.rows)
            if not inventory.rows:
                self.error(inventory_path, "inventory contains no source entries")
            for number, row in enumerate(inventory.rows, 2):
                self.inventory_record(row, f"{inventory_path}, row {number}")
        collation_path = self.out / COLLATION_NAME
        collation = self.read_table(collation_path, "\t")
        if collation is not None:
            self.require_columns(collation, {
                "folder", "their_page", "our_scan", "line", "their_reading",
                "codex_reading", "final_reading", "scan_shows", "kind",
                "marked_in_H", "confidence",
            }, collation_path)
            self.counts["H_collation_rows"] = len(collation.rows)
            for number, row in enumerate(collation.rows, 2):
                where = f"{collation_path}, row {number}"
                if row.get("kind") not in CHANGE_KINDS:
                    self.error(where, f"invalid collation kind: {row.get('kind')!r}")
                if row.get("confidence") not in CONFIDENCES:
                    self.error(where, f"invalid confidence: {row.get('confidence')!r}")
                if row.get("marked_in_H") not in {"yes", "no"}:
                    self.error(where, "marked_in_H must be yes or no")
                # The user's fixed collation schema carries crop evidence inside
                # scan_shows; it deliberately has no separate crop/coords columns.
                evidence = re.findall(
                    r"(?:Evidence|Additional evidence):\s*([^;]+);\s*original box\s*(\[[^\]]+\])",
                    row.get("scan_shows", ""),
                )
                if not evidence:
                    self.error(where, "scan_shows lacks a crop filename and original pixel box")
                for index, (crop, coords) in enumerate(evidence, 1):
                    self.check_evidence(crop.strip(), coords, collation_path,
                                        f"{where}, evidence {index}", "collation")

    def check_decided_set(self) -> None:
        actual = {
            path.name.removesuffix("_decided.json")
            for path in self.work.glob("*_decided.json") if path.is_file()
        }
        expected = set(self.pages)
        self.counts["decided_report_files_found"] = len(actual)
        for page in sorted(expected - actual):
            self.error(self.work, f"missing decided report for {page}")
        for page in sorted(actual - expected):
            self.error(self.work, f"unexpected decided report outside page_order: {page}")
        if len(actual) != EXPECTED_PAGES:
            self.error(self.work, f"requires exactly {EXPECTED_PAGES} *_decided.json files")

    def check_decided(self, page: str) -> None:
        path = self.work / f"{page}_decided.json"
        data = self.read_json(path)
        if not isinstance(data, dict):
            self.error(path, "decided report must be an object")
            return
        self.counts["decided_reports_read"] += 1
        if data.get("page") != page:
            self.error(path, f"page must be {page!r}")
        changes = data.get("changes")
        if not isinstance(changes, list):
            self.error(path, "changes must be a list")
        else:
            self.counts["decided_change_rows"] += len(changes)
            for number, row in enumerate(changes, 1):
                self.change_record(row, path, f"{path}, change {number}")
        inventory = data.get("inventory")
        if not isinstance(inventory, list) or not inventory:
            self.error(path, "inventory must be a nonempty list")
        else:
            for number, row in enumerate(inventory, 1):
                self.inventory_record(row, f"{path}, inventory entry {number}")
        fragment = self.out / "pages" / f"{page}.tex"
        if self.check_tex(fragment):
            self.counts["page_fragments_read"] += 1

    def box_rows(self, table: Table, where: Any) -> dict[str, dict[str, str]]:
        if "box" in table.columns:
            column = "box"
        elif "box_id" in table.columns:
            column = "box_id"
        else:
            self.error(where, "table must have a box or box_id column")
            return {}
        result: dict[str, dict[str, str]] = {}
        for number, row in enumerate(table.rows, 2):
            raw = row.get(column, "")
            box = raw.strip()
            if not box:
                self.error(where, f"row {number} has an empty box ID")
                continue
            if raw != box:
                self.error(where, f"row {number} box ID has outer whitespace")
            if box in result:
                self.error(where, f"duplicate box ID: {box}")
            else:
                result[box] = row
        return result

    def check_second(self, page: str) -> None:
        tables: dict[str, Table] = {}
        rows_by_kind: dict[str, dict[str, dict[str, str]]] = {}
        for kind in ("boxes", "first", "second", "comparison"):
            path = self.second / f"{page}_{kind}.tsv"
            table = self.read_table(path, "\t")
            if table is None:
                continue
            self.counts["second_tsv_files_read"] += 1
            tables[kind] = table
            rows_by_kind[kind] = self.box_rows(table, path)
        if len(tables) != 4:
            return
        reference = set(rows_by_kind["boxes"])
        if not reference:
            self.error(page, "blind-reading box set is empty")
        for kind, rows in rows_by_kind.items():
            found = set(rows)
            if found != reference:
                missing = sorted(reference - found)
                extra = sorted(found - reference)
                self.error(page, f"{kind} box IDs differ: missing={missing}, extra={extra}")
        self.counts["blind_boxes"] += len(reference)
        for box, row in rows_by_kind["boxes"].items():
            self.parse_coords(self.coords_from(row), f"{page} boxes.tsv, box {box}")
        comparison = tables["comparison"]
        self.require_columns(comparison, {"first", "second", "equal_tokens"},
                             self.second / f"{page}_comparison.tsv")
        differences: dict[str, dict[str, str]] = {}
        for box, row in rows_by_kind["comparison"].items():
            equal = row.get("equal_tokens")
            if equal not in {"yes", "no"}:
                self.error(page, f"comparison box {box}: equal_tokens must be yes or no")
            if equal == "no":
                differences[box] = row
        self.counts["comparison_differences"] += len(differences)
        decision_path = self.second / f"{page}_decisions.json"
        decisions = self.read_json(decision_path)
        decision_map: dict[str, dict[str, Any]] = {}
        changed = 0
        if not isinstance(decisions, list):
            self.error(decision_path, "decisions must be a list")
            decisions = []
        for number, decision in enumerate(decisions, 1):
            where = f"{decision_path}, decision {number}"
            if not isinstance(decision, dict):
                self.error(where, "decision must be an object")
                continue
            missing = DECISION_KEYS - set(decision)
            if missing:
                self.error(where, f"missing decision fields: {sorted(missing)}")
            box = decision.get("box")
            if not isinstance(box, str) or not box.strip():
                self.error(where, "box must be a nonempty string")
                continue
            if box != box.strip():
                self.error(where, "box ID has outer whitespace")
            if box in decision_map:
                self.error(where, f"duplicate decision for box {box}")
            else:
                decision_map[box] = decision
            for key in ("first", "second", "final"):
                if not isinstance(decision.get(key), str):
                    self.error(where, f"{key} must be a string")
            for key in ("decision", "reason"):
                value = decision.get(key)
                if not isinstance(value, str) or not value.strip():
                    self.error(where, f"{key} must be a nonempty string")
            if type(decision.get("changed")) is not bool:
                self.error(where, "changed must be a boolean")
            elif decision["changed"]:
                changed += 1
            compared = differences.get(box)
            if compared is None:
                self.error(where, f"box {box} is not an equal_tokens=no comparison row")
            else:
                for key in ("first", "second"):
                    if decision.get(key) != compared.get(key):
                        self.error(where, f"{key} does not exactly match comparison.tsv")
            self.check_evidence(decision.get("crop"), decision.get("coords"),
                                decision_path, where, "decision")
        missing_decisions = set(differences) - set(decision_map)
        extra_decisions = set(decision_map) - set(differences)
        if missing_decisions:
            self.error(decision_path, f"missing decisions: {sorted(missing_decisions)}")
        if extra_decisions:
            self.error(decision_path, f"unexpected decisions: {sorted(extra_decisions)}")
        if len(decisions) != len(differences):
            self.error(decision_path, "decision count must equal the number of differing comparison rows")
        self.counts["decision_rows"] += len(decisions)
        self.counts["changed_decisions"] += changed
        audit_path = self.second / f"{page}_audit.json"
        audit = self.read_json(audit_path)
        if not isinstance(audit, dict):
            self.error(audit_path, "audit must be an object")
            audit = {}
        else:
            self.counts["audit_files_read"] += 1
        if audit.get("page") != page:
            self.error(audit_path, f"page must be {page!r}")
        readers: list[str] = []
        for key in ("first_reader", "second_reader"):
            value = audit.get(key)
            if not isinstance(value, str) or not value.strip():
                self.error(audit_path, f"{key} must be a nonempty reader identifier")
                readers.append("")
            else:
                readers.append(value.strip().casefold())
        if readers[0] and readers[0] == readers[1]:
            self.error(audit_path, "first_reader and second_reader must be different")
        expected_counts = {
            "boxes": len(reference),
            "differences": len(differences),
            "changed": changed,
        }
        for key, expected in expected_counts.items():
            value = audit.get(key)
            if type(value) is not int or value != expected:
                self.error(audit_path, f"{key} must be integer {expected}, found {value!r}")
        audited = audit.get("audited_utc")
        if not isinstance(audited, str) or not audited.strip():
            self.error(audit_path, "audited_utc must be a nonempty timestamp string")
        self.page_counts[page] = {
            **expected_counts,
            "decisions": len(decisions),
            "first_reader": audit.get("first_reader"),
            "second_reader": audit.get("second_reader"),
        }

    def run(self) -> None:
        self.load_order()
        self.check_top_level()
        self.check_decided_set()
        for page in self.pages:
            self.check_decided(page)
            self.check_second(page)

    def result(self) -> dict[str, Any]:
        self.counts["expected_pages"] = EXPECTED_PAGES
        self.counts["required_top_level_files"] = len(REQUIRED_TOP_LEVEL)
        self.counts["unique_crop_files"] = len(self.crop_files)
        self.counts["errors"] = len(self.errors)
        return {
            "ok": not self.errors,
            "validated_utc": datetime.now(timezone.utc).isoformat(),
            "out": str(self.out),
            "pages": self.pages,
            "counts": dict(sorted(self.counts.items())),
            "per_page": self.page_counts,
            "errors": self.errors,
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out", type=Path, default=Path(__file__).resolve().parents[1],
        help="Final output directory; defaults to the directory containing scripts/.",
    )
    args = parser.parse_args()
    validator = Validator(args.out)
    try:
        validator.run()
    except Exception as exc:
        validator.error("validator", f"unexpected {type(exc).__name__}: {exc}")
    result = validator.result()
    destination = validator.work / "final_validation.json"
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    except OSError as exc:
        print(f"Cannot write {destination}: {exc}", file=sys.stderr)
        return 2
    print(f"{'PASS' if result['ok'] else 'FAIL'}: {destination}")
    if validator.errors:
        for message in validator.errors:
            print(message, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
