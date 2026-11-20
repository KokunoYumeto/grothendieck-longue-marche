#!/usr/bin/env python3
"""Read-only descriptive comparison for the two reminders introduced at 053/054.

Run only after scans054–058 have been committed:

    python deliverable/scripts/measure_workflow058.py \
        > work/workflow058_measurement.json \
        2> work/workflow058_assessment.txt

JSON goes to stdout; the same concise assessment is included in that JSON and
printed to stderr. The script itself writes no files. It reads only its own
source and the specified audit JSON/TSV records, never images or source pages.
Exit codes: 0 = measured; 2 = after cohort not committed; 1 = inconsistent input.
No partial after-cohort statistics are emitted when the commit gate fails.
"""

from __future__ import annotations

import argparse
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
import math
from pathlib import Path
import sys


BEFORE = (48, 49, 50, 51, 52)
AFTER = (54, 55, 56, 57, 58)
DECISIONS = ("first", "alternative", "other", "undecided")
BASELINE = "deliverable/audit/WORKFLOW_REMINDERS_054_BASELINE.json"
BASELINE_SHA256 = "4e6bfc43af6a733504f1e41a63bbd27369c28097de4cb3f2fdc28f1e5e33aa23"
METRICS = "deliverable/audit/METRICS.tsv"


class MeasurementError(ValueError):
    """A missing or inconsistent measurement input; fail without editing it."""


def require(condition: bool, explanation: str) -> None:
    if not condition:
        raise MeasurementError(explanation)


def parse_time(value: str) -> datetime:
    require(isinstance(value, str) and bool(value), f"Missing or invalid timestamp: {value!r}")
    parsed = datetime.fromisoformat(value.replace(" UTC", "+00:00").replace("Z", "+00:00"))
    require(parsed.tzinfo is not None, f"Timestamp has no explicit timezone: {value!r}")
    return parsed.astimezone(timezone.utc)


def iso_time(value: datetime) -> str:
    return value.isoformat().replace("+00:00", "Z")


def nonnegative_integer(value: object, label: str) -> int:
    require(not isinstance(value, bool), f"{label}: boolean is not a count")
    number = int(value)
    require(str(number) == str(value) and number >= 0, f"{label}: invalid count {value!r}")
    return number


class AuditInputs:
    """Cache and fingerprint only the explicitly requested audit text files."""

    def __init__(self, workspace: Path):
        self.workspace = workspace
        self.contents: dict[str, bytes] = {}

    def read(self, relative_path: str) -> bytes:
        if relative_path not in self.contents:
            self.contents[relative_path] = (self.workspace / relative_path).read_bytes()
        return self.contents[relative_path]

    def json(self, relative_path: str) -> dict:
        value = json.loads(self.read(relative_path))
        require(isinstance(value, dict), f"{relative_path}: expected a JSON object")
        return value

    def verify_unchanged(self) -> None:
        for relative_path, original in self.contents.items():
            require(
                (self.workspace / relative_path).read_bytes() == original,
                f"Input changed during measurement: {relative_path}; rerun after the commit completes",
            )

    def manifest(self) -> list[dict]:
        return [
            {"path": path, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
            for path, data in sorted(self.contents.items())
        ]


def read_metrics(inputs: AuditInputs) -> dict[int, dict]:
    reader = csv.DictReader(io.StringIO(inputs.read(METRICS).decode("utf-8")), delimiter="\t")
    needed = {
        "scan", "marks", "committed_utc", "reader_started_utc",
        "reader_finished_utc", "page_views", "crop_views",
    }
    require(needed.issubset(reader.fieldnames or []), f"{METRICS}: missing required columns")
    indexed = {}
    for row in reader:
        scan = int(row["scan"])
        require(scan not in indexed, f"{METRICS}: duplicate scan {scan:03d}")
        indexed[scan] = row
    return indexed


def after_commit_blockers(workspace: Path, metrics: dict[int, dict]) -> list[dict]:
    blockers = []
    for scan in AFTER:
        missing = []
        if scan not in metrics or not metrics[scan].get("committed_utc"):
            missing.append("committed METRICS.tsv row")
        for relative_path in (
            f"deliverable/audit/scan{scan:03d}.json",
            f"deliverable/audit/receipts/scan{scan:03d}.json",
        ):
            if not (workspace / relative_path).is_file():
                missing.append(relative_path)
        if missing:
            blockers.append({"scan": scan, "missing": missing})
    return blockers


def measure_page(inputs: AuditInputs, metrics: dict[int, dict], scan: int) -> dict:
    label = f"scan{scan:03d}"
    require(scan in metrics, f"{label}: no committed metrics row")
    metric = metrics[scan]
    report_path = f"deliverable/audit/{label}.json"
    receipt_path = f"deliverable/audit/receipts/{label}.json"
    report = inputs.json(report_path)
    receipt = inputs.json(receipt_path)
    require(int(report["scan"]) == scan == int(receipt["scan"]), f"{label}: scan mismatch")
    commit = parse_time(metric["committed_utc"])
    require(parse_time(receipt["committed_utc"]) == commit, f"{label}: commit timestamps disagree")

    rows = report["rows"]
    require(isinstance(rows, list) and bool(rows), f"{label}: no primary rows")
    identifiers = [row["id"] for row in rows]
    require(len(identifiers) == len(set(identifiers)), f"{label}: duplicate mark identifiers")
    require(all(int(row["scan"]) == scan for row in rows), f"{label}: wrong page in primary rows")
    marks = nonnegative_integer(metric["marks"], f"{label} marks")
    require(marks == len(rows), f"{label}: report and metrics mark counts differ")
    require(receipt["submission_rows"] == rows, f"{label}: report rows differ from committed submission")
    require(
        receipt["metadata"] == {key: value for key, value in report.items() if key != "rows"},
        f"{label}: report metadata differ from committed metadata",
    )
    require(
        [(row["id"], row["decision"]) for row in receipt["rows"]]
        == [(row["id"], row["decision"]) for row in rows],
        f"{label}: committed decision identities or values differ",
    )

    decisions = Counter(row["decision"] for row in rows)
    require(set(decisions).issubset(DECISIONS), f"{label}: unexpected decision category")
    primary_start = report.get("started_utc") or report.get("reader_started_utc")
    primary_finish = report.get("finished_utc") or report.get("reader_finished_utc")
    intervals = report.get("reader_intervals")
    interval_source = "reader_intervals"
    if intervals is None:
        reader = report.get("reader") or report.get("who")
        require(
            isinstance(reader, str) and bool(reader) and "coordinator" not in reader.lower(),
            f"{label}: no individual intervals or identifiable single primary reader",
        )
        intervals = [{"reader": reader, "started_utc": primary_start, "finished_utc": primary_finish, "marks": marks}]
        interval_source = "single_primary_report_interval"
    require(isinstance(intervals, list) and bool(intervals), f"{label}: missing individual reader intervals")
    readers = [interval["reader"] for interval in intervals]
    require(len(readers) == len(set(readers)), f"{label}: repeated primary reader interval")
    ownership = report.get("row_readers")
    if ownership is None and len(readers) == 1:
        ownership = {ident: readers[0] for ident in identifiers}
    require(isinstance(ownership, dict), f"{label}: missing individual mark ownership")
    require(set(ownership) == set(identifiers), f"{label}: mark ownership does not match report rows")
    ownership_counts = Counter(ownership.values())
    require(set(readers) == set(ownership_counts), f"{label}: interval and row reader identities differ")
    starts, finishes, elapsed = [], [], []
    reader_records = []
    for interval in intervals:
        start = parse_time(interval["started_utc"])
        finish = parse_time(interval["finished_utc"])
        require(start <= finish <= commit, f"{label}: primary interval outside commit window")
        assigned = nonnegative_integer(interval["marks"], f"{label} reader marks")
        require(assigned == ownership_counts[interval["reader"]], f"{label}: reader mark count mismatch")
        seconds = (finish - start).total_seconds()
        starts.append(start)
        finishes.append(finish)
        elapsed.append(seconds)
        reader_records.append({
            "reader": interval["reader"],
            "marks": assigned,
            "started_utc": iso_time(start),
            "finished_utc": iso_time(finish),
            "elapsed_seconds": seconds,
        })
    earliest, latest = min(starts), max(finishes)
    require(
        parse_time(metric["reader_started_utc"]) == parse_time(primary_start) == earliest,
        f"{label}: earliest primary start differs across records",
    )
    require(
        parse_time(metric["reader_finished_utc"]) == parse_time(primary_finish) == latest,
        f"{label}: latest primary finish differs across records",
    )
    page_views = nonnegative_integer(metric["page_views"], f"{label} page views")
    crop_views = nonnegative_integer(metric["crop_views"], f"{label} crop views")
    require(page_views + crop_views == len(report["views"]), f"{label}: metrics and report view totals differ")
    default_owner = readers[0] if len(readers) == 1 else None
    require(all(view.get("reader", default_owner) in ownership_counts for view in report["views"]), f"{label}: nonprimary or missing view owner")
    accepted_seconds = (commit - earliest).total_seconds()
    primary_seconds = math.fsum(elapsed)
    require(accepted_seconds > 0 and primary_seconds > 0, f"{label}: zero timing denominator")
    return {
        "scan": scan,
        "marks": marks,
        "committed_utc": iso_time(commit),
        "earliest_primary_start_utc": iso_time(earliest),
        "latest_primary_finish_utc": iso_time(latest),
        "accepted_page_seconds": accepted_seconds,
        "primary_elapsed_seconds": primary_seconds,
        "page_primary_span_seconds": (latest - earliest).total_seconds(),
        "primary_reader_count": len(intervals),
        "primary_interval_source": interval_source,
        "primary_reader_intervals": reader_records,
        "page_views": page_views,
        "crop_views": crop_views,
        "decision_counts": {decision: decisions[decision] for decision in DECISIONS},
    }


def measure_cohort(inputs: AuditInputs, metrics: dict[int, dict], scans: tuple[int, ...]) -> dict:
    pages = [measure_page(inputs, metrics, scan) for scan in scans]
    marks = sum(page["marks"] for page in pages)
    accepted = math.fsum(page["accepted_page_seconds"] for page in pages)
    primary = math.fsum(page["primary_elapsed_seconds"] for page in pages)
    crops = sum(page["crop_views"] for page in pages)
    decisions = {key: sum(page["decision_counts"][key] for page in pages) for key in DECISIONS}
    return {
        "scans": list(scans),
        "page_count": len(pages),
        "marks": marks,
        "accepted_page_seconds_sum": accepted,
        "primary_elapsed_seconds_sum": primary,
        "page_primary_span_seconds_sum": math.fsum(page["page_primary_span_seconds"] for page in pages),
        "primary_reader_intervals_count": sum(page["primary_reader_count"] for page in pages),
        "accepted_marks_per_hour": 3600 * marks / accepted,
        "primary_marks_per_hour": 3600 * marks / primary,
        "crop_views": crops,
        "page_views": sum(page["page_views"] for page in pages),
        "crops_per_mark": crops / marks,
        "decision_counts": decisions,
        "undecided_share": decisions["undecided"] / marks,
        "pages": pages,
    }


def verify_baseline(baseline: dict, before: dict) -> list[str]:
    saved = baseline["common_before_cohort"]
    for key, expected in saved.items():
        actual = before[key]
        if isinstance(expected, float):
            matched = math.isclose(actual, expected, rel_tol=1e-12, abs_tol=1e-6)
        else:
            matched = actual == expected
        require(matched, f"Immutable baseline mismatch for {key}: recorded {expected!r}, recomputed {actual!r}")
    return list(saved)


def comparison(before: dict, after: dict) -> dict:
    keys = (
        "marks", "accepted_page_seconds_sum", "primary_elapsed_seconds_sum",
        "accepted_marks_per_hour", "primary_marks_per_hour", "crop_views",
        "page_views", "crops_per_mark",
    )
    changes = {}
    for key in keys:
        b, a = before[key], after[key]
        changes[key] = {
            "before": b,
            "after": a,
            "absolute_change": a - b,
            "relative_change_percent": 100 * (a / b - 1) if b else None,
        }
    changes["undecided_share"] = {
        "before": before["undecided_share"],
        "after": after["undecided_share"],
        "percentage_point_change": 100 * (after["undecided_share"] - before["undecided_share"]),
    }
    changes["decision_count_changes"] = {
        key: after["decision_counts"][key] - before["decision_counts"][key] for key in DECISIONS
    }
    return changes


def assessment(before: dict, after: dict, changes: dict) -> str:
    def decisions(cohort: dict) -> str:
        return ", ".join(f"{cohort['decision_counts'][key]} {key}" for key in DECISIONS)

    return "\n".join([
        "Descriptive workflow comparison: scans048–052 before; scans054–058 after.",
        "All ten pages are committed; the original common baseline matches the recomputation.",
        "",
        "Measure | Before | After",
        f"Marks | {before['marks']} | {after['marks']}",
        f"Sum of accepted page windows, seconds | {before['accepted_page_seconds_sum']:.6f} | {after['accepted_page_seconds_sum']:.6f}",
        f"Marks per summed accepted-page-window hour | {before['accepted_marks_per_hour']:.2f} | {after['accepted_marks_per_hour']:.2f}",
        f"Sum of individual primary reader intervals, seconds | {before['primary_elapsed_seconds_sum']:.6f} | {after['primary_elapsed_seconds_sum']:.6f}",
        f"Marks per summed individual-primary-reader hour | {before['primary_marks_per_hour']:.2f} | {after['primary_marks_per_hour']:.2f}",
        f"Primary crop views | {before['crop_views']} | {after['crop_views']}",
        f"Primary page views | {before['page_views']} | {after['page_views']}",
        f"Primary crops per mark | {before['crops_per_mark']:.3f} | {after['crops_per_mark']:.3f}",
        f"Decisions before: {decisions(before)}.",
        f"Decisions after: {decisions(after)}.",
        "",
        "Descriptive relative changes: accepted-window rate "
        f"{changes['accepted_marks_per_hour']['relative_change_percent']:+.1f}%; "
        "individual-primary-interval rate "
        f"{changes['primary_marks_per_hour']['relative_change_percent']:+.1f}%; "
        f"crops per mark {changes['crops_per_mark']['relative_change_percent']:+.1f}%.",
        "Accepted page windows run from each page's earliest primary start to its commit; their sum omits interpage dispatch gaps. "
        "Individual primary intervals run from each reader's recorded start to final own-review finish, include waiting and revision gaps, "
        "and are not continuous active-reading or CPU time. Overlapping readers' intervals are summed separately. "
        "These individual-reader sums differ from the page primary spans used in some earlier findings. Rates include undecided marks; "
        "view counts are primary views, with independent-peer views excluded.",
        "The documented direct cases remain: M1026 crop metadata correction used 0 new ink views and changed 0 readings; "
        "M1051's own revision took 12 seconds and 1 new view, broadened uncertainty, and settled 0 additional marks.",
        "After-cohort results are descriptive. Different page content and mark difficulty, reader allocation, peer questions and revision gaps "
        "prevent attributing the differences to the reminders. Decision counts are not an accuracy measurement or a count of newly settled marks. "
        "Both reminders clarify existing inspection requirements.",
    ])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--workspace", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    workspace = args.workspace.resolve()
    inputs = AuditInputs(workspace)
    baseline = inputs.json(BASELINE)
    baseline_digest = hashlib.sha256(inputs.read(BASELINE)).hexdigest()
    require(baseline_digest == BASELINE_SHA256, "Original baseline bytes changed; refusing to replace or reinterpret the baseline")
    require(tuple(baseline["common_before_cohort"]["scans"]) == BEFORE, "Unexpected common-before cohort")
    require(tuple(baseline["planned_after_scans"]) == AFTER, "Unexpected planned-after cohort")
    metrics = read_metrics(inputs)
    blockers = after_commit_blockers(workspace, metrics)
    if blockers:
        result = {
            "status": "blocked_uncommitted_after_pages",
            "planned_after_scans": list(AFTER),
            "blockers": blockers,
            "baseline_sha256": baseline_digest,
            "message": "No after-cohort results computed. Rerun after every planned after page is committed.",
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        print(result["message"] + " Missing: " + ", ".join(f"scan{item['scan']:03d}" for item in blockers), file=sys.stderr)
        return 2

    before = measure_cohort(inputs, metrics, BEFORE)
    after = measure_cohort(inputs, metrics, AFTER)
    matched_fields = verify_baseline(baseline, before)
    changes = comparison(before, after)
    text = assessment(before, after, changes)
    result = {
        "schema_version": 1,
        "status": "complete_descriptive_comparison",
        "measured_utc": iso_time(datetime.now(timezone.utc)),
        "scope": "Text-only measurement of committed audit records; no new ink inspection, adjudication, OCR or source-page access.",
        "reminders": baseline["changes"],
        "baseline_verification": {
            "path": BASELINE,
            "sha256": baseline_digest,
            "original_bytes_unchanged": True,
            "recomputed_values_match": True,
            "matched_fields": matched_fields,
            "numeric_tolerance": {"relative": 1e-12, "absolute": 1e-6},
        },
        "before": before,
        "after": after,
        "descriptive_changes": changes,
        "measurement_definitions": {
            "accepted_page_seconds_sum": "Sum across pages of committed_utc minus earliest individual primary started_utc; interpage dispatch gaps are omitted.",
            "primary_elapsed_seconds_sum": "Sum across individual primary readers of final finished_utc minus started_utc; overlapping intervals count separately, including waits and revision gaps.",
            "page_primary_span_seconds_sum": "Additional context only: sum across pages of latest primary finish minus earliest primary start; not the denominator of primary_marks_per_hour in this comparison.",
            "accepted_marks_per_hour": "3600 * all recorded marks / accepted_page_seconds_sum, including undecided marks.",
            "primary_marks_per_hour": "3600 * all recorded marks / primary_elapsed_seconds_sum, including undecided marks; not a continuous active-work or CPU-time rate.",
            "views": "Committed primary page/crop totals from METRICS.tsv, checked against the number of logged primary views in scanNNN.json. No path deduplication; independent-peer views excluded. Source images are not opened to reclassify views.",
            "decision_counts": "Final committed decision category for every row in scanNNN.json; not an accuracy metric or transition count.",
            "commit_gate": "Every planned after page must have a metrics commit, report and receipt; commit timestamps, report content and receipt content must agree.",
        },
        "documented_direct_effects": [
            {"mark": "M1026", "change": "Crop metadata correction", "new_ink_views": 0, "reading_changes": 0, "source": BASELINE},
            {"mark": "M1051", "change": "Own revision broadened uncertainty", "own_revision_elapsed_seconds": 12, "new_own_views": 1, "newly_settled_marks": 0, "source": BASELINE},
        ],
        "measurement_limits": baseline["measurement_limits"] + [
            "Individual primary-reader elapsed intervals include waiting and revision gaps, are summed separately when overlapping, and are not continuous active-reading or CPU time.",
            "After results and all before/after changes are descriptive; reader allocation, peer questions and revision gaps can also differ.",
            "Decision distributions do not measure accuracy against independent ground truth or identify newly settled marks.",
            "The specific M1026 and M1051 observations do not establish an effect size for either reminder across the after cohort.",
        ],
        "inputs": inputs.manifest(),
        "measurement_script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "assessment": text,
    }
    inputs.verify_unchanged()
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    print(text, file=sys.stderr)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (MeasurementError, OSError, KeyError, TypeError, ValueError) as error:
        print(json.dumps({"status": "error", "message": str(error)}, ensure_ascii=False, indent=2))
        print(f"Measurement refused: {error}", file=sys.stderr)
        sys.exit(1)
