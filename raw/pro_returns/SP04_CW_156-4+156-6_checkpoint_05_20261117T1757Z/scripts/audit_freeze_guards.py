#!/usr/bin/env python3
"""Exercise only synthetic temporary projects; never access real page data."""
from __future__ import annotations

import csv
import json
from pathlib import Path
import tempfile

import manage
from manage import Project, utcnow


def fixture(base, count=120, done=True, audited=True, boolean_status=False, matching_log=True):
    out = base / "out"
    (out / "pages").mkdir(parents=True)
    (out / "records").mkdir()
    mapping = base / "page_map.tsv"
    keys = [("156-4", n) for n in range(2, 90)] + [("156-6", n) for n in range(2, 34)]
    keys = keys[:count]
    now = utcnow()
    (out / "progress.log").write_text(now + "\n", encoding="utf-8")
    columns = ["folder", "cote", "our_scan", "their_page", "codex_file", "hua_file", "hua_has", "context"]
    with mapping.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, columns, delimiter="\t")
        writer.writeheader()
        for cote, scan in keys:
            name = f"SYNTHETIC_{cote}_scan{scan:03d}.tex"
            writer.writerow({"folder": "SYNTHETIC", "cote": cote, "our_scan": scan,
                             "their_page": scan-1, "codex_file": "pages/" + name,
                             "hua_file": "", "hua_has": "text", "context": ""})
            (out / "pages" / name).write_text(f"\\scanpage{{{scan}}} Synthetic fixture.\n")
            record = {"cote": cote, "scan": scan, "changes": [], "doubts": [],
                      "inventory": [{"element": "E01", "kind": "text", "position": "top",
                                     "first_words_or_objects": "synthetic", "sheet_kind": "text",
                                     "hand": "synthetic", "transcribed": "yes"}], "status": {}}
            for flag, enabled in (("done", done), ("audited", audited)):
                if enabled:
                    record["status"][flag] = True if boolean_status else now
            (out / "records" / f"{cote}_scan{scan:03d}.json").write_text(json.dumps(record))
    if matching_log:
        with (out / "progress.log").open("a", encoding="utf-8") as stream:
            for kind, enabled in (("done", done), ("audited", audited)):
                if enabled:
                    for cote, scan in keys:
                        stream.write(f"scan {scan:03d} {kind} {now} cote {cote}\n")
    return Project(out, mapping)


def blocked_case(name, setup, action):
    with tempfile.TemporaryDirectory(prefix="sp04_guard_synthetic_") as directory:
        project = setup(Path(directory))
        try:
            action(project)
        except (ValueError, FileNotFoundError) as error:
            return {"case": name, "blocked": True, "reason": str(error),
                    "freeze_manifest_created": (project.out / "freeze.sha256").exists()}
        return {"case": name, "blocked": False,
                "freeze_manifest_created": (project.out / "freeze.sha256").exists()}


def main():
    results = []
    results.append(blocked_case("freeze_with_119_map_rows", lambda p: fixture(p, count=119), lambda p: p.freeze()))
    results.append(blocked_case("freeze_with_no_done_statuses", lambda p: fixture(p, done=False), lambda p: p.freeze()))
    results.append(blocked_case("freeze_with_no_audit_statuses", lambda p: fixture(p, audited=False), lambda p: p.freeze()))
    results.append(blocked_case("audit_before_all_done", lambda p: fixture(p, done=False, audited=False), lambda p: p.mark_audited("156-4", 2)))
    results.append(blocked_case("audit_out_of_order", lambda p: fixture(p, audited=False), lambda p: p.mark_audited("156-4", 3)))
    results.append(blocked_case("duplicate_audit", lambda p: fixture(p), lambda p: p.mark_audited("156-4", 2)))

    def missing_page(base):
        project = fixture(base)
        project.page_path("156-4", 2).unlink()
        return project
    results.append(blocked_case("freeze_with_missing_page_file", missing_page, lambda p: p.freeze()))

    results.append(blocked_case("freeze_with_boolean_statuses", lambda p: fixture(p, boolean_status=True), lambda p: p.freeze()))
    results.append(blocked_case("freeze_without_matching_log_events", lambda p: fixture(p, matching_log=False), lambda p: p.freeze()))

    def invalid_timestamp(base):
        project = fixture(base)
        record = project.load_record("156-4", 2)
        record["status"]["done"] = "2026-02-30 00:00:00 UTC"
        project._save_record(record)
        return project
    results.append(blocked_case("freeze_with_invalid_calendar_timestamp", invalid_timestamp, lambda p: p.freeze()))

    def mismatched_timestamp(base):
        project = fixture(base)
        log = project.out / "progress.log"
        lines = log.read_text().splitlines()
        lines[1] = "scan 002 done 2000-01-01 00:00:00 UTC cote 156-4"
        log.write_text("\n".join(lines) + "\n")
        return project
    results.append(blocked_case("freeze_with_log_record_timestamp_mismatch", mismatched_timestamp, lambda p: p.freeze()))

    def duplicate_log(base):
        project = fixture(base)
        log = project.out / "progress.log"
        lines = log.read_text().splitlines()
        with log.open("a") as stream:
            stream.write(lines[1] + "\n")
        return project
    results.append(blocked_case("freeze_with_duplicate_completion_event", duplicate_log, lambda p: p.freeze()))

    def wrong_log_order(base):
        project = fixture(base)
        log = project.out / "progress.log"
        lines = log.read_text().splitlines()
        lines[1], lines[2] = lines[2], lines[1]
        log.write_text("\n".join(lines) + "\n")
        return project
    results.append(blocked_case("freeze_with_out_of_order_completion_events", wrong_log_order, lambda p: p.freeze()))

    with tempfile.TemporaryDirectory(prefix="sp04_guard_synthetic_") as directory:
        project = fixture(Path(directory))
        writes = []
        original_atomic = manage.atomic_text

        def track_write(path, value):
            if Path(path).name in {"freeze.sha256", "progress.log"}:
                writes.append(Path(path).name)
            original_atomic(path, value)

        manage.atomic_text = track_write
        try:
            observed = project.freeze()
        finally:
            manage.atomic_text = original_atomic
        results.append({"case": "complete_corroborated_freeze", "accepted": True,
                        "hashed_files": observed["files"], "manifest_and_log_write_order": writes,
                        "manifest_persisted_before_frozen_log_marker": writes == ["freeze.sha256", "progress.log"]})
        locked = False
        try:
            project.mark_audited("156-4", 2)
        except ValueError:
            locked = True
        initial = project.verify_freeze()["ok"]
        page = project.page_path("156-4", 2)
        with page.open("a") as stream:
            stream.write("% synthetic change after freeze\n")
        changed = project.verify_freeze()
        results.append({"case": "post_freeze_checks", "audit_mark_locked": locked,
                        "initial_hashes_valid": initial, "page_mutation_detected": not changed["ok"],
                        "mismatch_count": len(changed["mismatches"])})
    report = {"scope": "synthetic temporary projects only; real pages/records/logs untouched", "results": results,
              "remaining_limits": [
                  "Timestamps and matching logs record explicit attestations; these structural guards do not establish visual reading.",
                  "The manifest detects later byte changes; ordinary filesystem writes are not prevented.",
                  "Manifest and progress log are separate files: the manifest is persisted first; a failure publishing the final log leaves the manifest as a lock and does not return completed success."
              ]}
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
