#!/usr/bin/env python3
"""Apply root-approved B31 uncertainty encoding only, after reader_c unlock."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json
import os
import tempfile

ROOT = Path(__file__).resolve().parent.parent
OLD = r"\unsure{\overline j|\illegible{1}}"
NEW = r"\unsure{\overline j}"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def replace_encoding(value):
    hits = []
    for n in (1, 2):
        old = OLD.replace("\\", "\\" * n)
        new = NEW.replace("\\", "\\" * n)
        if old in value:
            hits.append((old, new, n))
    if len(hits) != 1 or value.count(hits[0][0]) != 1:
        raise ValueError("Expected exactly one B31 encoding token")
    old, new, n = hits[0]
    return value.replace(old, new, 1), n


def main():
    receipt_path = ROOT / "work/reports/math_illegible_encoding_receipt.json"
    if receipt_path.exists():
        raise SystemExit("Receipt exists; refusing to overwrite it.")
    immutable_paths = [
        "work/second/150_scan005_first.tsv",
        "work/second/150_scan005_second.tsv",
        "work/second/150_scan005_second_observations.tsv",
        "work/second/150_scan005_comparison.json",
        "work/second/150_scan005_comparison_meta.json",
        "work/second/150_scan005_edits.json",
        "work/second/150_scan005_edits_receipt.json",
    ]
    immutable = {rel: sha((ROOT / rel).read_bytes()) for rel in immutable_paths}
    prepared = []
    rel = "work/pages/150_scan005.tex"
    before = (ROOT / rel).read_bytes()
    text, n = replace_encoding(before.decode("utf-8"))
    prepared.append((ROOT / rel, before, text.encode("utf-8"), [{
        "selector": {"unique_token": OLD}, "old": OLD, "new": NEW,
    }]))

    report_rel = "work/reports/150_scan005/report.json"
    before = (ROOT / report_rel).read_bytes()
    report = json.loads(before)
    fixed_boxes_before = json.dumps(report.get("audit_boxes"), ensure_ascii=False, sort_keys=True)
    audit_pairs_before = [(x.get("first"), x.get("second")) for x in report.get("audit_changes", [])]
    targets = [
        ("changes", {"id": "P27b"}, "final"),
        ("doubts", {"place": "P27 second cancelled formula"}, "reading"),
        ("audit_changes", {"place": "B31"}, "final"),
    ]
    logs = []
    for collection, selector, field in targets:
        hits = [x for x in report[collection] if all(x.get(k) == v for k, v in selector.items())]
        if len(hits) != 1:
            raise ValueError("Report selector is not unique")
        item = hits[0]
        old = item[field]
        new, multiplicity = replace_encoding(old)
        item[field] = new
        logs.append({"collection": collection, "selector": selector, "field": field,
                     "old": old, "new": new, "tex_backslash_multiplicity": multiplicity})
        if collection == "doubts":
            assert "barred j" in item["alternatives"] and "unrecoverable" in item["alternatives"]
            alternative_prose = item["alternatives"]
    assert fixed_boxes_before == json.dumps(report.get("audit_boxes"), ensure_ascii=False, sort_keys=True)
    assert audit_pairs_before == [(x.get("first"), x.get("second")) for x in report.get("audit_changes", [])]
    prepared.append((ROOT / report_rel, before,
                     (json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode(), logs))

    for suffix in ("root_decisions.json", "adjudications.json"):
        rel = "work/second/150_scan005_" + suffix
        before = (ROOT / rel).read_bytes()
        rows = json.loads(before)
        matches = [x for x in rows if x.get("box") == "B31"]
        assert len(matches) == 1
        old = matches[0]["final"]
        new, multiplicity = replace_encoding(old)
        matches[0]["final"] = new
        prepared.append((ROOT / rel, before,
                         (json.dumps(rows, ensure_ascii=False, indent=2) + "\n").encode(), [{
            "selector": {"box": "B31"}, "field": "final",
            "old": old, "new": new, "tex_backslash_multiplicity": multiplicity,
        }]))

    rel = "work/second/150_scan005_adjudicated.tsv"
    before = (ROOT / rel).read_bytes()
    text = before.decode("utf-8")
    rows = list(csv.DictReader(io.StringIO(text), delimiter="\t"))
    matches = [x for x in rows if x["box"] == "B31"]
    assert len(matches) == 1
    old = matches[0]["final"]
    new, multiplicity = replace_encoding(old)
    encoded_old = OLD.replace("\\", "\\" * multiplicity)
    encoded_new = NEW.replace("\\", "\\" * multiplicity)
    assert text.count(encoded_old) == 1
    new_text = text.replace(encoded_old, encoded_new, 1)
    new_rows = list(csv.DictReader(io.StringIO(new_text), delimiter="\t"))
    for a, b in zip(rows, new_rows):
        assert a["first"] == b["first"] and a["second"] == b["second"]
        if a["box"] != "B31":
            assert a == b
        else:
            assert b["final"] == new
            assert all(a[k] == b[k] for k in a if k != "final")
    prepared.append((ROOT / rel, before, new_text.encode(), [{
        "selector": {"box": "B31"}, "field": "final", "old": old, "new": new,
    }]))

    receipt = {
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "authorization": "Root approved the syntax-only B31 encoding remedy; reader_c explicitly sent 005 unlocked before application.",
        "scope": "Preferred barred j, raised placement, cancellation and unresolved status preserved. Only the forbidden mathematical illegible alternative is encoded using the existing unsure macro.",
        "old_token": OLD, "new_token": NEW,
        "unrecoverable_alternative_retained_in_doubts_prose": alternative_prose,
        "immutable_file_sha256": immutable,
        "fixed_report_audit_boxes_and_first_second_pairs": "Verified unchanged in memory.",
        "deferred_to_root_aggregation": [
            "work/SP89_C13_149+150_transcription.tex",
            "work/SP89_C13_149+150_changes.md",
            "work/SP89_C13_149+150_doubts.md",
            "work/SP89_C13_149+150_collation.tsv",
        ],
        "historical_edit_plan_and_receipt": "Preserved byte-for-byte; this receipt bridges the later encoding state.",
        "compilation": "Not performed.",
        "status": "validated; applying",
        "files": [{
            "path": str(path.relative_to(ROOT)),
            "before_sha256": sha(before), "after_sha256": sha(after),
            "operations": logs, "applied": False,
        } for path, before, after, logs in prepared],
    }
    with receipt_path.open("x", encoding="utf-8") as stream:
        json.dump(receipt, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    staged = []
    try:
        for path, before, after, logs in prepared:
            fd, name = tempfile.mkstemp(prefix="math_encoding_", suffix=path.suffix,
                                        dir=ROOT / "scratch")
            tmp = Path(name)
            with os.fdopen(fd, "wb") as stream:
                stream.write(after)
            os.chmod(tmp, path.stat().st_mode & 0o777)
            staged.append((path, before, after, tmp))
        for i, (path, before, after, tmp) in enumerate(staged):
            if path.read_bytes() != before:
                raise RuntimeError("Concurrent file change: " + str(path))
            os.replace(tmp, path)
            assert path.read_bytes() == after
            receipt["files"][i]["applied"] = True
            receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
        for rel, expected in immutable.items():
            assert sha((ROOT / rel).read_bytes()) == expected, rel
        receipt["status"] = "applied"
        receipt["completed_utc"] = datetime.now(timezone.utc).isoformat()
    except Exception as exc:
        receipt["status"] = "interrupted; inspect applied flags"
        receipt["error"] = repr(exc)
        raise
    finally:
        for path, before, after, tmp in staged:
            if tmp.exists():
                tmp.unlink()
        receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    print("B31 encoding applied to", len(prepared), "live files; fixed/history hashes unchanged.")
    print("Receipt:", receipt_path)
    print("Combined and generated aggregates deferred to root.")


if __name__ == "__main__":
    main()
