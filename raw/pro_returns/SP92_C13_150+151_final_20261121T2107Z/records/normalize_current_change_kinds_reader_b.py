#!/usr/bin/env python3
"""Normalize current changes.kind only; preserve every other record field."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path

W = Path("/workspace/scratch/d7279cb02214/SP92_C13_150+151_work")
allowed = {
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
mapping = {
    "deletion state": "deletion state (struck given live or live given struck)",
}
changes = []
files_checked = []
for path in sorted((W / "records").glob("???_scan???.json")):
    raw = path.read_bytes()
    original = json.loads(raw)
    current = deepcopy(original)
    local = []
    for i, row in enumerate(current.get("changes", [])):
        old = row["kind"]
        if old in mapping:
            row["kind"] = mapping[old]
            local.append({
                "path": ["changes", i, "kind"],
                "change_id": row["id"],
                "before": old,
                "after": row["kind"],
            })
        assert row["kind"] in allowed, (path.name, row["id"], row["kind"])
    files_checked.append(path.name)
    if not local:
        assert current == original
        continue
    restored = deepcopy(current)
    for item in local:
        restored["changes"][item["path"][1]]["kind"] = item["before"]
    assert restored == original, "A non-kind field changed."
    assert path.read_bytes() == raw, "Concurrent record edit detected."
    output = (json.dumps(current, ensure_ascii=False, indent=2) + "\n").encode()
    assert json.loads(output) == current
    path.write_bytes(output)
    assert json.loads(path.read_bytes()) == current
    changes.append({
        "file": str(path.relative_to(W)),
        "sha256_before": sha256(raw).hexdigest(),
        "sha256_after": sha256(output).hexdigest(),
        "edits": local,
    })

log = {
    "task": "Normalize only current changes.kind to permitted collation kinds",
    "reader": "/root/reader_b",
    "model": "GPT-6 Astra Pro",
    "effort": "not exposed",
    "run": "SP92",
    "utc": datetime.now(timezone.utc).isoformat(),
    "mapping": mapping,
    "allowed_values": sorted(allowed),
    "record_files_checked": files_checked,
    "changes": changes,
    "checks": {
        "all_current_kind_values_permitted": True,
        "only_current_changes_kind_modified": True,
        "count_flags_unchanged": True,
        "row_ids_counts_order_unchanged": True,
        "historical_snapshots_audit_originals_and_second_boxes_unchanged": True,
        "no_page_or_tsv_written": True,
        "no_images_or_new_readings": True,
        "no_compilation_or_assembly": True,
        "json_round_trip": True,
    },
}
out = W / "records/normalize_current_change_kinds_reader_b.json"
out.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({
    "log": str(out),
    "record_files_checked": len(files_checked),
    "kind_fields_normalized": sum(len(x["edits"]) for x in changes),
    "checks": "passed",
}))
