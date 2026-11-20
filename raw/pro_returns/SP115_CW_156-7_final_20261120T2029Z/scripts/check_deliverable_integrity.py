#!/usr/bin/env python3
"""Check final deliverable metadata, frozen bytes and blind-audit provenance.

Run only after all root audits and the final transcription freeze are complete.
This performs no editorial reading decisions, OCR or TeX compilation. Original
page hashes in INITIAL_FROZEN_SHA256.json refer to the *_initial.tex snapshots,
not the subsequently adjudicated live pages. Archive name coverage is checked
separately by check_archive_coverage.py.
"""
from collections import Counter
from pathlib import Path
import csv
import hashlib
import json
import re
import sys

from PIL import Image


R = Path(__file__).resolve().parents[1]
HEX256 = re.compile(r"[0-9a-fA-F]{64}\Z")
COLLATION_KINDS = {
    "misread word", "misread symbol or index", "omission", "text not on the page",
    "deletion state (struck given live or live given struck)",
    "insertion or placement", "abbreviation expanded or spelling modernised",
    r"readable ink left as \ill{}", "drawing or diagram", "other",
}
ADJUDICATION_HEADER = [
    "box", "first", "second", "final", "decision",
    "changed_place_ids", "crop", "scan_shows",
]


class IntegrityCheck:
    def __init__(self, root=R):
        self.root = Path(root).resolve()
        self.problems = []
        self.checks = {}
        self.verified_crops = {}
        self.initial_files_checked = 0
        self.initial_snapshots_checked = 0
        self.second_hashes_checked = 0
        self.root_extent_crops_checked = 0
        self.changed_ids = set()
        self.k_by_scan = {}

    def fail(self, message):
        self.problems.append(message)

    def read_json(self, path):
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, ValueError) as exc:
            self.fail(f"Cannot read JSON {path.name}: {exc}")
            return None

    def table(self, path, header, delimiter="\t"):
        try:
            with path.open(newline="", encoding="utf-8") as stream:
                reader = csv.DictReader(stream, delimiter=delimiter)
                if reader.fieldnames != header:
                    self.fail(f"Header mismatch {path.name}: {reader.fieldnames}")
                    return []
                rows = list(reader)
            for index, row in enumerate(rows, 2):
                if None in row or any(value is None for value in row.values()):
                    self.fail(f"Invalid row width {path.name}:{index}")
            return rows
        except (OSError, UnicodeError, csv.Error) as exc:
            self.fail(f"Cannot read table {path.name}: {exc}")
            return []

    def artifact_path(self, value, label, manifest_path=False):
        """Resolve local metadata paths, including historical manifest prefixes."""
        if not isinstance(value, str) or not value.strip():
            self.fail(f"Missing path: {label}")
            return None
        path = Path(value)
        if manifest_path:
            # Reader manifests used absolute workspace paths, out/... paths,
            # and paths relative to out. Rebase only the historical out prefix.
            if path.is_absolute():
                try:
                    path = path.relative_to(self.root)
                except ValueError:
                    positions = [i for i, part in enumerate(path.parts) if part == "out"]
                    if positions:
                        path = Path(*path.parts[positions[-1] + 1:])
            elif path.parts and path.parts[0] == "out":
                path = Path(*path.parts[1:])
        resolved = (self.root / path).resolve()
        try:
            resolved.relative_to(self.root)
        except ValueError:
            self.fail(f"Path outside deliverable: {label}")
            return None
        return resolved

    def hash_matches(self, path, expected, label):
        if not isinstance(expected, str) or not HEX256.fullmatch(expected):
            self.fail(f"Invalid SHA-256: {label}")
            return False
        if path is None:
            return False
        try:
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
        except OSError as exc:
            self.fail(f"Cannot hash {label}: {exc}")
            return False
        if actual != expected.lower():
            self.fail(f"Frozen bytes changed: {label}")
            return False
        return True

    def coordinates(self, value, label):
        if not isinstance(value, (list, tuple)) or len(value) != 4:
            self.fail(f"Missing/invalid coordinates: {label}")
            return None
        converted = []
        for number in value:
            if type(number) is int:
                converted.append(number)
            elif isinstance(number, str) and re.fullmatch(r"-?\d+", number):
                converted.append(int(number))
            else:
                self.fail(f"Non-integer coordinate: {label}")
                return None
        x0, y0, x1, y1 = converted
        if not (0 <= x0 < x1 and 0 <= y0 < y1):
            self.fail(f"Invalid coordinate bounds: {label}")
            return None
        return converted

    def ids(self, value, label, separated=False):
        if separated and isinstance(value, str):
            value = value.split(";") if value else []
        if not isinstance(value, list) or any(
            not isinstance(item, str) or not item.strip() for item in value
        ):
            self.fail(f"Invalid changed_place_ids: {label}")
            return set()
        if len(value) != len(set(value)):
            self.fail(f"Duplicate changed_place_ids: {label}")
        return set(value)

    def keyed_rows(self, rows, label):
        counts = Counter(row.get("box") for row in rows)
        if any(not key or count != 1 for key, count in counts.items()):
            self.fail(f"Missing/duplicate box IDs: {label}")
        return {row.get("box"): row for row in rows if row.get("box")}

    def verify_crop(self, path, label, expected_size=None):
        if path is None:
            return
        try:
            path.relative_to(self.root / "crops")
        except ValueError:
            self.fail(f"Crop is outside crops/: {label}")
            return
        if path not in self.verified_crops:
            try:
                with Image.open(path) as crop:
                    if crop.format != "PNG" or min(crop.size) <= 0:
                        raise ValueError("crop must be a nonempty PNG")
                    size = list(crop.size)
                    crop.verify()  # File structure only; no text/image interpretation.
                self.verified_crops[path] = size
            except (OSError, ValueError, SyntaxError) as exc:
                self.fail(f"Missing/invalid crop {label}: {exc}")
                self.verified_crops[path] = None
        actual_size = self.verified_crops[path]
        if expected_size is not None and actual_size is not None:
            if actual_size != expected_size:
                self.fail(f"Crop output-size mismatch: {label}")

    def check_standard_tables(self):
        rows = self.table(self.root / "SP115_CW_156-7_collation.tsv", [
            "folder", "their_page", "our_scan", "line", "their_reading",
            "codex_reading", "final_reading", "scan_shows", "kind",
            "marked_in_H", "confidence",
        ])
        for index, row in enumerate(rows, 2):
            label = f"collation row {index}"
            if row.get("kind") not in COLLATION_KINDS:
                self.fail(f"Invalid collation kind: {label}")
            try:
                if int(row["their_page"]) + 1 != int(row["our_scan"]):
                    self.fail(f"Page mapping mismatch: {label}")
            except (ValueError, TypeError):
                self.fail(f"Invalid page mapping: {label}")
            if row.get("confidence") not in {"high", "medium", "low"}:
                self.fail(f"Invalid confidence: {label}")
        inventory = self.table(self.root / "SP115_CW_156-7_inventory.csv", [
            "scan", "sheet_kind", "hand", "element", "kind", "position",
            "first_words_or_objects", "transcribed",
        ], ",")
        for index, row in enumerate(inventory, 2):
            label = f"inventory row {index}"
            if row.get("transcribed") != "yes":
                self.fail(f"Untranscribed element: {label}")
            if row.get("kind") not in {
                "text", "display", "diagram", "drawing", "margin note",
                "insertion", "deletion",
            }:
                self.fail(f"Invalid element kind: {label}")
            if row.get("sheet_kind") not in {
                "text", "reused_typed", "typescript", "letter", "list",
                "cancelled_draft", "cover",
            }:
                self.fail(f"Invalid sheet kind: {label}")
        events = self.table(self.root / "CHECK_EVENTS.tsv", [
            "statement_id", "date", "who", "type", "outcome",
        ])
        allowed = {
            "targeted proof check", "independent re-proof",
            "computation or formal certificate", "used and rechecked in this run",
            "carried as background without fault found",
        }
        for index, row in enumerate(events, 2):
            kind = row.get("type") or ""
            if kind not in allowed and not kind.startswith("refuted, with"):
                self.fail(f"Invalid check-event type: row {index}")
        self.checks.update(
            collation_rows=len(rows), inventory_elements=len(inventory),
            check_events=len(events),
        )

    def check_initial_files(self, page, stem):
        files = page.get("files")
        if not isinstance(files, list):
            self.fail(f"Missing frozen initial file list: {stem}")
            return
        listed = set()
        snapshot_checked = False
        for item in files:
            if not isinstance(item, dict):
                self.fail(f"Invalid frozen initial file entry: {stem}")
                continue
            raw = item.get("path")
            if not isinstance(raw, str) or not raw.strip():
                self.fail(f"Missing/invalid frozen initial path: {stem}")
                continue
            if raw in listed:
                self.fail(f"Duplicate frozen initial path: {stem}")
            listed.add(raw)
            actual = raw
            if raw == f"pages/{stem}.tex":
                actual = f"second/{stem}_initial.tex"
            if actual == f"second/{stem}_initial.tex":
                snapshot_checked = True
                self.initial_snapshots_checked += 1
            path = self.artifact_path(actual, f"initial {stem}")
            self.hash_matches(path, item.get("sha256"), f"initial {actual}")
            self.initial_files_checked += 1
        for suffix in ("boxes.tsv", "first.tsv"):
            if f"second/{stem}_{suffix}" not in listed:
                self.fail(f"Initial freeze omits {stem}_{suffix}")
        if not snapshot_checked:
            self.fail(f"Initial freeze has no page hash for {stem}_initial.tex")

    def crop_manifest(self, stem, expected_boxes):
        manifest = self.read_json(self.root / "second" / f"{stem}_crop_manifest.json")
        if isinstance(manifest, dict):
            entries = manifest.get("crops", [])
            source_size = manifest.get("source_size", manifest.get("source_dimensions"))
        elif isinstance(manifest, list):
            entries, source_size = manifest, None
        else:
            return {}, None
        if not isinstance(entries, list) or any(not isinstance(x, dict) for x in entries):
            self.fail(f"Invalid crop-manifest entries: {stem}")
            return {}, None
        indexed = self.keyed_rows(entries, f"crop manifest {stem}")
        if set(indexed) != expected_boxes:
            self.fail(f"Crop-manifest box coverage mismatch: {stem}")
        if source_size is not None and (
            not isinstance(source_size, list) or len(source_size) != 2
            or any(type(x) is not int or x <= 0 for x in source_size)
        ):
            self.fail(f"Invalid source dimensions in crop manifest: {stem}")
            source_size = None
        return indexed, source_size

    def registered_root_crops(self, stem, number):
        path = self.root / "second" / f"{stem}_root_extra_crop.json"
        if not path.exists():
            return {}
        records = self.read_json(path)
        if isinstance(records, dict):
            records = [records]
        if not isinstance(records, list):
            self.fail(f"Invalid root extra-crop provenance: {stem}")
            return {}
        indexed = {}
        for record in records:
            if not isinstance(record, dict):
                self.fail(f"Invalid root extra-crop record: {stem}")
                continue
            box = record.get("box_id")
            label = f"root extra crop {stem} {box}"
            if record.get("scan") != number or not isinstance(box, str) or not box:
                self.fail(f"Invalid scan/box association: {label}")
                continue
            if box in indexed:
                self.fail(f"Duplicate root extra-crop registration: {label}")
                continue
            if not all(isinstance(record.get(key), str) and record[key].strip()
                       for key in ("reason", "created_utc")):
                self.fail(f"Missing root extra-crop provenance: {label}")
                continue
            coords = self.coordinates(record.get("original_pixels"), label)
            crop = self.artifact_path(record.get("crop"), label)
            if coords is not None and crop is not None:
                indexed[box] = {
                    "coordinates": coords, "path": crop,
                    "output_size": record.get("output_size"),
                }
        return indexed

    def check_blind_page(self, page):
        number = page.get("scan")
        if type(number) is not int:
            self.fail("Invalid scan number in initial freeze")
            return 0, 0
        stem = f"H156-01_156-7_scan{number:03d}"
        self.check_initial_files(page, stem)
        second_dir = self.root / "second"
        boxes = self.table(second_dir / f"{stem}_boxes.tsv",
                           ["box", "kind", "x0", "y0", "x1", "y1"])
        first = self.table(second_dir / f"{stem}_first.tsv", ["box", "reading"])
        second_path = second_dir / f"{stem}_second.tsv"
        second = self.table(second_path, ["box", "reading"])
        box_order = [row.get("box") for row in boxes]
        by_box = self.keyed_rows(boxes, f"neutral boxes {stem}")
        box_coords = {
            box: self.coordinates([row.get(key) for key in ("x0", "y0", "x1", "y1")],
                                  f"neutral {stem} {box}")
            for box, row in by_box.items()
        }
        if page.get("boxes") != len(boxes):
            self.fail(f"Initial box-count mismatch: {stem}")
        for label, rows in (("First", first), ("Second", second)):
            if [row.get("box") for row in rows] != box_order:
                self.fail(f"{label} coverage/order mismatch: {stem}")

        comparison = self.read_json(second_dir / f"{stem}_comparison.json")
        decisions = self.read_json(second_dir / f"{stem}_decisions.json")
        review = self.read_json(self.root / "review" / f"scan{number:03d}_final.json")
        adjudications = self.table(second_dir / f"{stem}_adjudication.tsv",
                                  ADJUDICATION_HEADER)
        # Hash validation is independent of the other audit files: a missing
        # comparison/decision record must not suppress a completed audit's hash.
        audit = review.get("blind_audit") if isinstance(review, dict) else None
        completed = isinstance(audit, dict) and isinstance(audit.get("completed_utc"), str) and bool(audit["completed_utc"].strip())
        if completed:
            hash_fields = [key for key in ("second_tsv_sha256", "second_sha256") if key in audit]
            if not hash_fields:
                self.fail(f"Completed blind audit has no second TSV hash: {stem}")
            for field in hash_fields:
                self.hash_matches(second_path, audit[field], f"{stem} blind_audit.{field}")
                self.second_hashes_checked += 1
        else:
            self.fail(f"Completed blind_audit missing: {stem}")
        if not all(isinstance(x, dict) for x in (comparison, decisions, review)):
            return len(boxes), len(adjudications)
        comparison_rows = comparison.get("rows", [])
        if not isinstance(comparison_rows, list) or any(
            not isinstance(x, dict) for x in comparison_rows
        ):
            self.fail(f"Invalid comparison rows: {stem}")
            return len(boxes), len(adjudications)
        self.keyed_rows(comparison_rows, f"comparison {stem}")
        if [row.get("box") for row in comparison_rows] != box_order:
            self.fail(f"Comparison coverage/order mismatch: {stem}")
        if any(type(row.get("different")) is not bool for row in comparison_rows):
            self.fail(f"Invalid comparison different flag: {stem}")
        needed = {row.get("box") for row in comparison_rows if row.get("different") is True}
        if comparison.get("boxes") != len(boxes) or comparison.get("different_boxes") != len(needed):
            self.fail(f"Comparison count mismatch: {stem}")
        adjudicated = self.keyed_rows(adjudications, f"adjudication {stem}")
        if set(adjudicated) != needed:
            self.fail(f"Adjudication difference coverage mismatch: {stem}")
        decision_boxes = decisions.get("boxes")
        if not isinstance(decision_boxes, dict):
            self.fail(f"Missing decision box records: {stem}")
            decision_boxes = {}
        if set(decision_boxes) != needed:
            self.fail(f"Decision difference coverage mismatch: {stem}")
        manifest, source_size = self.crop_manifest(stem, set(by_box))
        root_crops = self.registered_root_crops(stem, number)

        page_ids = set()
        for box, row in adjudicated.items():
            label = f"{stem} {box}"
            decision = decision_boxes.get(box)
            if not isinstance(decision, dict):
                self.fail(f"Missing decision metadata: {label}")
                continue
            for field in ("decision", "evidence"):
                if not isinstance(decision.get(field), str) or not decision[field].strip():
                    self.fail(f"Missing {field}: {label}")
            if not isinstance(row.get("decision"), str) or not row["decision"].strip():
                self.fail(f"Missing adjudication decision: {label}")
            if row.get("decision") != decision.get("decision"):
                self.fail(f"Decision metadata mismatch: {label}")
            evidence = row.get("scan_shows")
            if not isinstance(evidence, str) or not evidence.strip():
                self.fail(f"Missing adjudication evidence: {label}")
                evidence = ""
            supplied_evidence = decision.get("evidence")
            if isinstance(supplied_evidence, str) and supplied_evidence.strip():
                if supplied_evidence not in evidence:
                    self.fail(f"Decision evidence absent from adjudication: {label}")
            coords = self.coordinates(decision.get("box_coords"), f"decision {label}")
            decision_crop = self.artifact_path(decision.get("crop"), f"decision crop {label}")
            registered = root_crops.get(box)
            root_extent = (
                registered is not None
                and registered["coordinates"] == coords
                and registered["path"] == decision_crop
            )
            if coords != box_coords.get(box) and not root_extent:
                self.fail(f"Decision/neutral coordinate mismatch: {label}")
            recorded = re.findall(r"original box\s+(\[[^\]]+\])", evidence)
            try:
                embedded = json.loads(recorded[-1]) if recorded else None
            except ValueError:
                embedded = None
            if self.coordinates(embedded, f"adjudication evidence {label}") != coords:
                self.fail(f"Adjudication evidence coordinate mismatch: {label}")
            if coords is not None and source_size is not None:
                if coords[2] > source_size[0] or coords[3] > source_size[1]:
                    self.fail(f"Crop coordinates exceed source dimensions: {label}")

            row_crop = self.artifact_path(row.get("crop"), f"adjudication crop {label}")
            if row_crop != decision_crop:
                self.fail(f"Decision/adjudication crop mismatch: {label}")
            if isinstance(row.get("crop"), str) and row["crop"] not in evidence:
                self.fail(f"Crop path absent from adjudication evidence: {label}")
            entry = manifest.get(box)
            output_size = None
            if not isinstance(entry, dict):
                self.fail(f"Missing crop manifest entry: {label}")
            else:
                mc = entry.get("original_box", entry.get("coordinates"))
                if self.coordinates(mc, f"crop manifest {label}") != box_coords.get(box):
                    self.fail(f"Crop-manifest coordinate mismatch: {label}")
                manifest_file = next((entry[k] for k in
                                      ("file", "filename", "path", "crop_path", "crop")
                                      if k in entry), None)
                manifest_crop = self.artifact_path(manifest_file, f"crop manifest {label}", True)
                expected_crop = registered["path"] if root_extent else manifest_crop
                if expected_crop != row_crop:
                    self.fail(f"Crop-manifest file mismatch: {label}")
                output_size = registered.get("output_size") if root_extent else entry.get("output_size")
                if not root_extent and output_size is None and "output_width" in entry and "output_height" in entry:
                    output_size = [entry["output_width"], entry["output_height"]]
            self.verify_crop(row_crop, label, output_size)
            if root_extent:
                self.root_extent_crops_checked += 1

            row_ids = self.ids(row.get("changed_place_ids"), f"adjudication {label}", True)
            decision_ids = self.ids(decision.get("changed_place_ids", []), f"decision {label}")
            if row_ids != decision_ids:
                self.fail(f"Changed-place IDs differ between decision and adjudication: {label}")
            page_ids.update(row_ids)

        if not completed:
            return len(boxes), len(adjudications)
        if audit.get("root_checked_every_difference_on_new_blind_crop") is not True:
            self.fail(f"Root difference-inspection attestation missing: {stem}")
        if audit.get("boxes_read") != len(boxes) or audit.get("different_boxes") != len(needed):
            self.fail(f"Blind-audit box count mismatch: {stem}")
        audit_ids = self.ids(audit.get("changed_place_ids"), f"blind_audit {stem}")
        if audit_ids != page_ids:
            self.fail(f"Blind-audit changed_place_ids differ from adjudication union: {stem}")
        if type(audit.get("changed_places")) is not int or audit["changed_places"] != len(page_ids):
            self.fail(f"Unique K count disagrees with changed_place_ids: {stem}")
        # Blind-audit place IDs and collation/review change IDs are distinct
        # namespaces. Validate the audit IDs through their decision/adjudication
        # unions above, without requiring them in review["changes"].
        if page_ids & self.changed_ids:
            self.fail(f"Changed-place ID reused across scans: {stem}")
        self.changed_ids.update(page_ids)
        self.k_by_scan[f"{number:03d}"] = len(page_ids)
        return len(boxes), len(adjudications)

    def run(self):
        self.check_standard_tables()
        for path in self.root.rglob("*"):
            if path.is_file() and path.suffix.lower() in {".jpg", ".jpeg", ".pdf", ".zip"}:
                self.fail(f"Unexpected supplied-input/archive candidate {path.relative_to(self.root)}")
        initial = self.read_json(self.root / "second" / "INITIAL_FROZEN_SHA256.json")
        box_count = adjudication_count = 0
        if isinstance(initial, dict) and isinstance(initial.get("pages"), list):
            pages = initial["pages"]
            scans = [page.get("scan") for page in pages if isinstance(page, dict)]
            if len(scans) != len(pages) or set(scans) != set(range(2, 10)) or len(scans) != 8:
                self.fail("Initial freeze must contain each scan 002–009 exactly once")
            for page in pages:
                if not isinstance(page, dict):
                    self.fail("Invalid page record in initial freeze")
                    continue
                boxes, adjudications = self.check_blind_page(page)
                box_count += boxes
                adjudication_count += adjudications
        else:
            self.fail("Initial blind freeze missing/invalid")
        self.checks.update(
            initial_boxes=box_count,
            initial_frozen_files_checked=self.initial_files_checked,
            initial_snapshots_checked=self.initial_snapshots_checked,
            adjudicated_different_boxes=adjudication_count,
            blind_second_hashes_checked=self.second_hashes_checked,
            registered_root_extent_crops_checked=self.root_extent_crops_checked,
            valid_adjudication_crops=sum(size is not None for size in self.verified_crops.values()),
            unique_K=len(self.changed_ids),
            changed_place_ids=sorted(self.changed_ids),
            K_by_scan=self.k_by_scan,
        )
        if sum(self.k_by_scan.values()) != len(self.changed_ids):
            self.fail("Global unique K count differs from per-scan changed-place union")
        final = self.read_json(self.root / "review" / "FINAL_TRANSCRIPTION_SHA256.json")
        final_ok = True
        if isinstance(final, dict) and isinstance(final.get("files"), list) and final["files"]:
            for item in final["files"]:
                if not isinstance(item, dict):
                    self.fail("Invalid final freeze file record")
                    final_ok = False
                    continue
                path = self.artifact_path(item.get("path"), "final freeze")
                if not self.hash_matches(path, item.get("sha256"), f"final {item.get('path')}"):
                    final_ok = False
        else:
            self.fail("Final transcription freeze missing/invalid")
            final_ok = False
        self.checks["final_hashes_unchanged"] = final_ok
        self.checks["problems"] = self.problems
        return self.checks


def main():
    checker = IntegrityCheck()
    result = checker.run()
    destination = R / "review" / "deliverable_integrity.json"
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if checker.problems else 0


if __name__ == "__main__":
    sys.exit(main())
