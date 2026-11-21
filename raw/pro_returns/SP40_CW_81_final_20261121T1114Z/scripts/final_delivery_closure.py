#!/usr/bin/env python3
"""Append final transport evidence; preserve the selected ZIP's existing members.

Run only after root review and the two completed, single-launch final transports.
No codecs, manuscript checks, global event edits, or source-tree rebuilds occur.
The final closed-container measurement is written outside the delivery ZIP.
"""
import argparse
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
from datetime import datetime, timezone
import zipfile

OUT = Path(__file__).resolve().parents[1]
CHECKS = OUT / "checks"
PREFIX = "_final_delivery_closure/"
TRANSPORT = "_checkpoint_transport/"
LIMIT = 536870912
FIELDS = ["statement_id", "date", "who", "type", "outcome"]
META = ["orig_filename", "filename", "date_time", "compress_type", "comment", "extra",
        "create_system", "create_version", "extract_version", "reserved", "flag_bits",
        "volume", "internal_attr", "external_attr", "header_offset", "CRC",
        "compress_size", "file_size", "_raw_time"]


def need(condition, message):
    if not condition:
        raise ValueError(message)


def utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def measured(path):
    with path.open("rb") as handle:
        sha = hashlib.file_digest(handle, "sha256").hexdigest()
    return {"path": str(path), "bytes": path.stat().st_size, "sha256": sha}


def absent(path):
    need(not path.exists() and not path.is_symlink(), f"Refusing existing path: {path}")


def table(data):
    reader = csv.DictReader(io.StringIO(data.decode("utf-8"), newline=""), delimiter="\t")
    need(reader.fieldnames == FIELDS, "Unexpected CHECK_EVENTS columns")
    rows = list(reader)
    need(all(list(row) == FIELDS and None not in row.values() for row in rows), "Malformed event row")
    return rows


def row_bytes(rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=FIELDS, delimiter="\t", lineterminator="\r\n")
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def members(archive):
    infos = archive.infolist()
    names = [info.filename for info in infos]
    need(len(names) == len(set(names)), "Duplicate ZIP member names")
    return infos, names


def metadata(info):
    values = [getattr(info, key) for key in META]
    return [value.hex() if isinstance(value, bytes) else list(value) if isinstance(value, tuple)
            else value for value in values]


def equal_stream(left, right, limit=None):
    total, sha = 0, hashlib.sha256()
    while limit is None or total < limit:
        amount = 1048576 if limit is None else min(1048576, limit - total)
        a, b = left.read(amount), right.read(amount)
        need(a == b, "Direct byte comparison failed")
        if not a:
            need(limit is None, "Premature end of preserved local-record prefix")
            break
        sha.update(a)
        total += len(a)
    return {"bytes": total, "sha256": sha.hexdigest()}


def frozen_check(raw, transported):
    data = raw.read("freeze_manifest.json")
    need(transported.read("freeze_manifest.json") == data, "Frozen manifest bytes changed")
    frozen = json.loads(data)["sha256"]
    need(len(frozen) == 25 and sum(name.startswith("pages/") for name in frozen) == 24
         and "SP40_CW_81_transcription.tex" in frozen,
         "Expected the 25-file frozen manifest")
    checks = []
    for name, expected in frozen.items():
        original = raw.read(name)
        need(digest(original) == expected, f"Raw frozen hash mismatch: {name}")
        need(transported.read(name) == original, f"Transport frozen bytes mismatch: {name}")
        checks.append([name, len(original), expected])
    return {"manifest_sha256": digest(data), "file_columns": ["path", "bytes", "sha256"], "files": checks}


def compare_delivery(selected_path, delivery_path, expected, raw_path):
    """Full finite identity projection, including serialized ZIP metadata and local records."""
    rows = []
    with zipfile.ZipFile(selected_path) as base, zipfile.ZipFile(delivery_path) as delivery:
        originals, names = members(base)
        after, after_names = members(delivery)
        need(after_names == names + list(expected), "Delivery member order or membership changed")
        need(delivery.comment == base.comment, "ZIP archive comment changed")
        for index, (before, current) in enumerate(zip(originals, after)):
            before_meta = metadata(before)
            need(before_meta == metadata(current), f"ZIP metadata changed: {before.filename}")
            with base.open(before) as a, delivery.open(current) as b:
                result = equal_stream(a, b)
            rows.append([index, index, before.filename, result["bytes"], result["sha256"], before_meta])
            if (index + 1) % 500 == 0:
                print(json.dumps({"stage": "member_comparison", "completed": index + 1,
                                  "total": len(originals)}), flush=True)
        for name, data in expected.items():
            need(delivery.read(name) == data, f"Embedded supplemental bytes changed: {name}")
        with zipfile.ZipFile(raw_path) as raw:
            freeze = frozen_check(raw, delivery)
            need(delivery.read("CHECK_EVENTS.tsv") == raw.read("CHECK_EVENTS.tsv"), "Main event table changed")
        prefix_length, comment = base.start_dir, base.comment.hex()
    with selected_path.open("rb") as a, delivery_path.open("rb") as b:
        local_prefix = equal_stream(a, b, prefix_length)
    return {"member_columns": ["selected_index", "delivery_index", "path", "bytes", "sha256", "zip_metadata"],
            "zip_metadata_columns": META, "zip_metadata_hex_fields": ["comment", "extra"],
            "members": rows, "archive_comment_hex": comment, "local_record_prefix": local_prefix,
            "frozen25": freeze,
            "forward": "Copy the selected container and append precisely the listed supplemental members.",
            "inverse": "Select each delivery_index in members, in listed selected_index order; the direct comparisons recover every selected member path, bytes and ZIP metadata.",
            "original_container_preservation": "Raw, v1 and v2 container files remain separately preserved; this member projection does not reconstruct their central-directory byte sequences."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selection", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    absent(args.output.absolute())
    selection_path, output = args.selection.resolve(), args.output.resolve()
    need(selection_path == CHECKS / "final_helper_transport_selection.json", "Unexpected final selection path")
    need(output.name == "SP40_CW_81.zip", "Unexpected delivery basename")
    part = output.with_name(output.name + ".part")
    proof_path = CHECKS / "final_delivery_closed_file.json"
    proof_part = proof_path.with_name(proof_path.name + ".part")
    for path in (output, part, proof_path, proof_part):
        absent(path)
    evidence_paths = sorted(CHECKS.glob("final_helper_transport*"))
    need(all(path.is_file() and not path.is_symlink() for path in evidence_paths), "Unexpected helper evidence path")
    evidence = {path: path.read_bytes() for path in evidence_paths}
    selection = json.loads(evidence[selection_path])
    need(selection["selected_variant"] == "v2" and selection["size_limit_bytes"] == LIMIT, "Expected size-gated final v2")
    source_records = {key: selection[key + "_archive"] for key in ("raw", "v1", "v2")}
    source_paths = {key: Path(value["path"]).resolve() for key, value in source_records.items()}
    need(len(set(source_paths.values())) == 3 and output not in source_paths.values(), "Archives must have distinct paths")
    for key, path in source_paths.items():
        need(path.name == "SP40_CW_81.zip", "Original archive basename differs")
        absent(path.with_name(path.name + ".part"))
        need(measured(path) == source_records[key], f"Actual {key} archive differs from selection")
    need(source_records["v1"]["bytes"] > LIMIT, "Actual completed v1 did not exceed the v2 launch gate")
    need(source_records["v2"]["bytes"] < LIMIT, "Selected completed v2 fails the strict delivery gate")
    need(selection["selected_archive"] == source_records["v2"], "Selected archive differs from v2")
    need(selection["selected_headroom_bytes"] == LIMIT - source_records["v2"]["bytes"], "Stale selection headroom")
    raw_identity = {"basename": source_paths["raw"].name, "bytes": source_records["raw"]["bytes"],
                    "sha256": source_records["raw"]["sha256"]}
    added, copied, references, projected, changes, completions = {}, [], [], [], [], {}

    def add(name, data, origin):
        name = PREFIX + name
        need(name not in added, f"Duplicate supplemental name: {name}")
        added[name] = data
        copied.append({"entry": name, "bytes": len(data), "sha256": digest(data), "source": origin})
        return name

    for path, data in evidence.items():
        add("evidence/" + path.name, data, {"external_path": str(path)})
    attribution = selection["delegated_execution_attribution"]
    need(attribution["authorizing_agent"] == "/root" and attribution["operator"] != "/root",
         "Expected explicit delegated transport attribution")
    external_bytes = {}
    with zipfile.ZipFile(source_paths["raw"]) as raw:
        _, raw_names = members(raw)
        main_events = raw.read("CHECK_EVENTS.tsv")
        main_rows = table(main_events)
        need(main_events.endswith(b"\n"), "Main event table lacks an append boundary")
        script_data = Path(__file__).resolve().read_bytes()
        need(raw.read("scripts/final_delivery_closure.py") == script_data, "Executing closure script differs from raw snapshot")
        for variant in ("v1", "v2"):
            def helper(suffix):
                return json.loads(evidence[CHECKS / ("final_helper_transport_" + variant + "_" + suffix + ".json")])

            launch, completion = helper("launch"), helper("process_completion")
            completed = completion["completion_stdout"]
            terminal = completion["observed_terminal_result"]
            need(selection["launch_attempt_counts"][variant] == launch[variant + "_launch_attempt_number"] == 1,
                 "Expected one recorded launch per variant")
            need(selection["observed_exit_codes"][variant] == completion["exit_code"] == terminal["exit_code"] == 0,
                 "Transport did not complete with exit zero")
            need(completion["session_id"] == attribution["sessions"][variant], "Delegated session mismatch")
            records = []
            for line in terminal["output"].splitlines():
                try:
                    value = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if isinstance(value, dict) and value.get("stage") == "complete":
                    records.append(value)
            need(records == [completed], "Actual completion stdout record mismatch")
            archive_record = source_records[variant]
            need(completed["stage"] == "complete" and completed["output"] == archive_record["path"]
                 and completed["output_bytes"] == archive_record["bytes"]
                 and completed["output_sha256"] == archive_record["sha256"], "Completed container measurement mismatch")
            need(completed["source_bytes"] == raw_identity["bytes"] and completed["source_sha256"] == raw_identity["sha256"],
                 "Completed source measurement mismatch")
            need(completed["below_512_mib"] == (archive_record["bytes"] < LIMIT)
                 and completed["headroom_bytes"] == LIMIT - archive_record["bytes"]
                 and completed["bytes_saved"] == raw_identity["bytes"] - archive_record["bytes"], "Completed size fields mismatch")
            argv = launch["argv"]
            packer_name = "checkpoint_transport_pack.py" if variant == "v1" else "checkpoint_transport_pack_v2.py"
            need(len(argv) > 1 and (Path(launch["cwd"]) / argv[1]).resolve() == OUT / "scripts" / packer_name,
                 "Launch packer script binding mismatch")
            def argument(flag):
                need(argv.count(flag) == 1, f"Missing or repeated launch argument: {flag}")
                return argv[argv.index(flag) + 1]
            def launched_path(flag):
                return (Path(launch["cwd"]) / argument(flag)).resolve()
            need(launched_path("--source") == source_paths["raw"]
                 and launched_path("--output") == source_paths[variant]
                 and argument("--expected-source-sha256") == raw_identity["sha256"], "Launch archive binding mismatch")
            need(launch["cache_argument_is_parent"] is True, "Unexpected cache launch record")
            if variant == "v1":
                need(launch["raw_snapshot_exit_code_reported_by_root"] == 0
                     and launch["expected_raw_bytes"] == raw_identity["bytes"]
                     and launch["expected_raw_sha256"] == launch["actual_raw_sha256"] == raw_identity["sha256"],
                     "v1 launch raw snapshot binding mismatch")
            else:
                need(launch["v1_observed_exit_code"] == 0 and launch["v1_actual_bytes"] == source_records["v1"]["bytes"]
                     and launch["v1_actual_sha256"] == source_records["v1"]["sha256"] and launch["gate_bytes"] == LIMIT
                     and launch["gate_passed_by_actual_v1_size"] is True and launch["v1_relaunched"] is False,
                     "v2 actual completed-v1 gate record mismatch")
            audit_record, event_record = selection["audit_files"][variant], selection["exact_event_copies"][variant]
            audit_path, event_path = Path(audit_record["path"]).resolve(), Path(event_record["path"]).resolve()
            audit_data, event_data = audit_path.read_bytes(), event_path.read_bytes()
            for path, data in ((audit_path, audit_data), (event_path, event_data)):
                need(path not in evidence or evidence[path] == data, "Helper/external evidence bytes differ")
            external_bytes.update({audit_path: audit_data, event_path: event_data})
            need(launched_path("--audit") == audit_path and Path(completed["audit"]).resolve() == audit_path,
                 "Audit path binding mismatch")
            need(digest(audit_data) == audit_record["sha256"] and measured(event_path) == event_record,
                 "External audit/event measurement mismatch")
            with zipfile.ZipFile(source_paths[variant]) as transport:
                _, names = members(transport)
                need(not any(name == PREFIX[:-1] or name.startswith(PREFIX) for name in names),
                     "Closure namespace already present")
                need(transport.read(TRANSPORT + "byte_audit.json") == audit_data, "Embedded/external audit bytes differ")
                need(transport.read(TRANSPORT + "CHECK_EVENTS.tsv") == event_data, "Embedded/external event bytes differ")
                manifest_data = transport.read(TRANSPORT + "manifest.json")
                manifest, audit = json.loads(manifest_data), json.loads(audit_data)
                need(manifest["format"] == "checkpoint-lossless-png-transport"
                     and manifest["format_version"] == int(variant[1:]), "Unexpected transport manifest")
                need(manifest["source_archive"] == audit["source_archive"] == raw_identity, "Raw archive identity mismatch")
                need([entry["path"] for entry in manifest["entries"]] == raw_names, "Raw manifest member projection mismatch")
                need(audit == selection["full_packaging_audits"][variant] and audit["mismatched_original_files"] == 0,
                     "Completed packaging audit mismatch")
                need(completed["original_entries_verified"] == audit["final_transport_original_entry_byte_comparisons_passed"]
                     == len(raw_names), "Completed original-entry count mismatch")
                if variant == "v2":
                    selected_freeze = frozen_check(raw, transport)
                    need(transport.read("scripts/final_delivery_closure.py") == script_data, "Selected closure script differs")
                    need(transport.read("CHECK_EVENTS.tsv") == main_events, "Selected main event table differs")
            audit_target = add(variant + "/byte_audit.json", audit_data, {"archive": archive_record, "entry": TRANSPORT + "byte_audit.json"})
            event_target = add(variant + "/CHECK_EVENTS.tsv", event_data, {"archive": archive_record, "entry": TRANSPORT + "CHECK_EVENTS.tsv"})
            manifest_target = (add("v1/manifest.json", manifest_data, {"archive": archive_record, "entry": TRANSPORT + "manifest.json"})
                               if variant == "v1" else TRANSPORT + "manifest.json")
            need(audit["all_original_paths_and_hashes"] == TRANSPORT + "manifest.json"
                 and audit["check_event_record"] == TRANSPORT + "CHECK_EVENTS.tsv", "Unexpected audit reference strings")
            rows = table(event_data)
            need(len(rows) == 1 and rows[0] == selection["actual_CHECK_EVENTS_rows"][len(projected)], "Exact final event row mismatch")
            old = rows[0]
            literal = TRANSPORT + "byte_audit.json"
            need(old["outcome"].count(literal) == 1 and old["who"].startswith("/root; "), "Unexpected raw event reference/attribution")
            new = dict(old)
            new["who"] = attribution["operator"] + old["who"][len("/root"):] + (
                f"; delegated by {attribution['authorizing_agent']}; recorded session {completion['session_id']}")
            restored = dict(new, who=old["who"])
            need(restored == old, "Event attribution inverse failed")
            changes.append({"variant": variant, "raw_event_entry": event_target, "raw_row_index": 0,
                            "cumulative_row_index": len(main_rows) + len(projected), "field": "who",
                            "old": old["who"], "new": new["who"], "all_other_fields_equal": True,
                            "inverse": "Replace this cumulative row's who with old; the complete original table bytes are at raw_event_entry."})
            projected.append(new)
            references.append({"variant": variant, "original_archive": archive_record,
                               "audit": {"entry": audit_target, "/all_original_paths_and_hashes": {"literal": TRANSPORT + "manifest.json", "target": manifest_target},
                                         "/check_event_record": {"literal": TRANSPORT + "CHECK_EVENTS.tsv", "target": event_target}},
                               "event": {"entry": event_target, "row": 0, "field": "outcome", "literal": literal,
                                         "character_start": old["outcome"].index(literal), "target": audit_target},
                               "manifest": {"entry": manifest_target, "source_archive": source_records["raw"],
                                            "storage_path_pointer_constructor": "/entries/{i}/storage/path for every integer i from 0 through entry_count-1",
                                            "entry_count": len(manifest["entries"]), "storage_paths_resolve_in": archive_record,
                                            "delivery_payload_scope": "Selected v2 existing members" if variant == "v2" else "Separately preserved v1 archive; its payloads are not added to this delivery"}})
            completions[variant] = completed
    refmap = {"schema": "final-delivery-reference-map-v1", "copied_artifacts": copied,
              "version_references": references, "original_completed_container_metrics": completions,
              "event_attribution_projection": changes,
              "main_event_prefix": {"entry": "CHECK_EVENTS.tsv", "bytes": len(main_events), "sha256": digest(main_events)},
              "final_container_metrics": "Measured after the last append; external out/checks/final_delivery_closed_file.json"}
    # Serialize before add() extends copied: this finite table covers previously copied artifacts only.
    add("reference_map.json", encoded(refmap), {"constructor": "This script; mappings above"})
    readme = (
        "FINAL DELIVERY CLOSURE\n\n"
        "All pre-existing selected-v2 members retain their order, bytes and ZIP metadata. The main CHECK_EVENTS.tsv remains exact.\n"
        "Use ordinary unzip to access _final_delivery_closure/. RESTORE_CHECKPOINT.py restores/verifies only the raw snapshot entries in its unchanged manifest.\n"
        "The v1 manifest is exact evidence. Every v1 /entries/{i}/storage/path resolves in the separately preserved v1 archive identified in reference_map.json; its WebP payloads are not added here.\n"
        "The selected v2 manifest and payloads remain at their existing paths. Audit/event path strings are resolved explicitly by reference_map.json.\n"
        "The cumulative supplemental CHECK_EVENTS.tsv begins with the exact original main table bytes, followed by the two completed events with explicit delegated attribution and one root packaging event. Exact raw per-version tables and reversible who-field changes are retained.\n"
        "Original completed v1/v2 size/hash/gate fields describe their separately preserved original containers. The embedded root receipt describes completed pre-receipt comparisons. Finished delivery size/hash/gate results are external in out/checks/final_delivery_closed_file.json, measured after the last append.\n"
        "Original raw/v1/v2 descriptors:\n" + json.dumps(source_records, ensure_ascii=False, indent=2) + "\n"
    ).encode("utf-8")
    add("README.txt", readme, {"constructor": "This script"})
    output.parent.mkdir(parents=True, exist_ok=True)
    with source_paths["v2"].open("rb") as source, part.open("xb") as target:
        shutil.copyfileobj(source, target, 1048576)
        target.flush()
        os.fsync(target.fileno())
    initial = measured(part)
    need(initial["bytes"] == source_records["v2"]["bytes"] and initial["sha256"] == source_records["v2"]["sha256"],
         "Initial container copy differs")

    def append_files(items):
        with zipfile.ZipFile(part, "a", compression=zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=True) as archive:
            _, names = members(archive)
            need(not set(names).intersection(items), "Append would replace an existing member")
            for name, data in items.items():
                archive.writestr(name, data)

    append_files(added)
    before_receipt = compare_delivery(source_paths["v2"], part, added, source_paths["raw"])
    need(before_receipt["frozen25"] == selected_freeze, "Frozen verification mapping changed")
    interim = measured(part)
    when = utc()
    receipt = {"schema": "final-delivery-root-receipt-v1", "completed_utc": when,
               "scope": "Completed pre-receipt ZIP-member, metadata, local-record-prefix, supplemental-byte, and frozen25 comparisons; no codec execution",
               "original_containers": source_records, "original_completed_container_metrics": completions,
               "pre_receipt_container": interim, "pre_receipt_container_scope": "Closed staging ZIP before this receipt and cumulative event table were appended",
               "projection": before_receipt, "pre_receipt_supplemental_members": list(added),
               "supplemental_artifact_checks": [{"entry": name, "bytes": len(data), "sha256": digest(data)} for name, data in added.items()],
               "event_attribution_projection": changes,
               "final_container_metrics": "External only, measured after the last append: out/checks/final_delivery_closed_file.json"}
    root_event = {"statement_id": "SP40-FINAL-CLOSURE-" + source_records["v2"]["sha256"] + "-MEMBER-PRESERVATION",
                  "date": when, "who": "/root; GPT-6 Astra Pro; inherited effort setting not separately exposed; final_delivery_closure.py",
                  "type": "computation or formal certificate",
                  "outcome": f"Completed pre-receipt packaging checks: {len(before_receipt['members'])} selected-v2 member paths, ordered bytes and ZIP metadata compared exactly; the preserved local-record prefix and {len(added)} supplemental entries compared exactly; all 25 raw-manifest frozen files and the main event table matched. Actual original v1/v2 completion records, archive sizes/hashes, and embedded/external audits/events were checked. This records finite storage comparisons. The root receipt names the measured pre-receipt staging container; the final closed delivery metrics and repeated post-receipt comparison are recorded externally in out/checks/final_delivery_closed_file.json."}
    new_ids = [row["statement_id"] for row in projected + [root_event]]
    need(len(set(new_ids)) == 3 and not set(new_ids).intersection(row["statement_id"] for row in main_rows), "New event ID collision")
    cumulative = main_events + row_bytes(projected + [root_event])
    need(cumulative[:len(main_events)] == main_events and table(cumulative) == main_rows + projected + [root_event],
         "Cumulative event projection failed")
    closing = {PREFIX + "root_verification.json": encoded(receipt), PREFIX + "CHECK_EVENTS.tsv": cumulative}
    append_files(closing)
    added.update(closing)
    after_receipt = compare_delivery(source_paths["v2"], part, added, source_paths["raw"])
    need(after_receipt == before_receipt, "Post-receipt member projection differs")
    need(sorted(CHECKS.glob("final_helper_transport*")) == evidence_paths, "Helper evidence membership changed during closure")
    for path, data in list(evidence.items()) + list(external_bytes.items()):
        need(path.read_bytes() == data, f"Evidence bytes changed during closure: {path}")
    for key, path in source_paths.items():
        need(measured(path) == source_records[key], f"Original {key} container changed during closure")
    need(part.stat().st_size < LIMIT, "Final closed delivery exceeds the strict size gate")
    # Same-directory hard-link publication fails atomically if output already exists.
    os.link(part, output)
    part.unlink()
    final = measured(output)
    need(final["bytes"] < LIMIT, "Published closed delivery fails strict size gate")
    proof = {"schema": "final-delivery-closed-file-v1", "completed_utc": utc(), "delivery": final,
             "size_limit_bytes": LIMIT, "below_512_mib": final["bytes"] < LIMIT,
             "headroom_bytes": LIMIT - final["bytes"], "original_containers_unchanged": source_records,
             "original_completed_container_metrics": completions, "selection": measured(selection_path),
             "closure_script": {"raw_entry": "scripts/final_delivery_closure.py", "sha256": digest(script_data)},
             "root_receipt": {"entry": PREFIX + "root_verification.json", "sha256": digest(closing[PREFIX + "root_verification.json"])},
             "post_receipt_projection_equals_embedded_pre_receipt_projection": True,
             "original_member_count": len(after_receipt["members"]), "local_record_prefix": after_receipt["local_record_prefix"],
             "all_supplemental_entries_read_back_exactly": [{"entry": name, "bytes": len(data), "sha256": digest(data)} for name, data in added.items()],
             "frozen25": after_receipt["frozen25"], "main_events_preserved_exactly": True,
             "cumulative_events_main_prefix_bytes": len(main_events), "cumulative_events_rows": len(main_rows) + 3,
             "no_codec_or_manuscript_checks_executed": True, "no_global_events_history_progress_modified": True}
    with proof_part.open("xb") as handle:
        handle.write(encoded(proof))
        handle.flush()
        os.fsync(handle.fileno())
    os.link(proof_part, proof_path)
    proof_part.unlink()
    print(json.dumps({"stage": "complete", "delivery": final, "headroom_bytes": proof["headroom_bytes"],
                      "proof": measured(proof_path)}, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
