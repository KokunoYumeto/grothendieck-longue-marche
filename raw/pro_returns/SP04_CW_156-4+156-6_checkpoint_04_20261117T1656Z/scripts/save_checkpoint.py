#!/usr/bin/env python3
"""Create one due hourly checkpoint and save it through the official helper.

Preparation alone has no side effects. Running this script is the root's
explicit instruction to checkpoint/upload. The helper is invoked once; there
are no automatic retries. Library success is checked per returned item.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys

from manage import DEFAULT_MAP, DEFAULT_OUT, Project, atomic_text, utcnow

DEFAULT_HELPER = Path(__file__).resolve().parent / "library_helpers_r_wds6xe" / "scripts" / "library_upload.py"


def save_checkpoint(out=DEFAULT_OUT, page_map=DEFAULT_MAP, helper=DEFAULT_HELPER):
    helper = Path(helper).resolve()
    if not helper.is_file():
        raise FileNotFoundError(f"Official upload helper is missing: {helper}")
    project = Project(out, page_map)
    # The existing checkpoint guard rejects an early invocation before making
    # any checkpoint or upload. It also prevents a second immediate snapshot.
    created = project.checkpoint()
    local_path = Path(created["checkpoint"]).resolve()
    request = {"uploads": [{"local_path": str(local_path),
                            "purpose": "create_library_file",
                            "library_artifact_type": "other"}]}
    completed = subprocess.run(
        [sys.executable, str(helper)],
        input=json.dumps(request, ensure_ascii=False) + "\n",
        text=True, encoding="utf-8", capture_output=True, check=False,
    )
    receipt_dir = project.out / "library_receipts"
    receipt_path = receipt_dir / f"checkpoint_{created['number']:02d}.json"
    parsed = None
    try:
        parsed = json.loads(completed.stdout)
    except json.JSONDecodeError:
        pass
    # Receipt is documentary metadata, not a checkpoint substitute. The ZIP
    # remains the original byte-identical snapshot; the next ZIP includes this
    # receipt and the current upload-status log entry.
    receipt = {
        "recorded_utc": utcnow(), "checkpoint": str(local_path),
        "checkpoint_number": created["number"], "checkpoint_bytes": created["bytes"],
        "official_helper": str(helper), "helper_exit_code": completed.returncode,
        "helper_result": parsed,
    }
    atomic_text(receipt_path, json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    results = parsed.get("results") if isinstance(parsed, dict) else None
    if completed.returncode != 0 or not isinstance(results, list) or len(results) != 1:
        project._append_log(f"checkpoint {created['number']:02d} upload outcome unverified {utcnow()} receipt {receipt_path.relative_to(project.out)}")
        return {
            "checkpoint": str(local_path), "library_saved": "unverified",
            "receipt": str(receipt_path), "helper_exit_code": completed.returncode,
            "message": "One helper invocation ended without a single verifiable success result. Do not automatically retry the write.",
            "helper_error": completed.stderr.strip(), "exit_code": 1,
        }
    item = results[0]
    if not isinstance(item, dict) or item.get("status") != "succeeded":
        project._append_log(f"checkpoint {created['number']:02d} upload not confirmed {utcnow()} receipt {receipt_path.relative_to(project.out)}")
        return {
            "checkpoint": str(local_path), "library_saved": False,
            "receipt": str(receipt_path), "result": item,
            "message": "The item's Library status did not report succeeded. Inspect its reported error before any further action.",
            "exit_code": 1,
        }
    required_strings = ("library_file_id", "file_id", "file_name", "local_path", "purpose")
    if any(not isinstance(item.get(key), str) or not item[key] for key in required_strings):
        project._append_log(f"checkpoint {created['number']:02d} upload success metadata incomplete {utcnow()} receipt {receipt_path.relative_to(project.out)}")
        return {
            "checkpoint": str(local_path), "library_saved": "reported_success_metadata_incomplete",
            "receipt": str(receipt_path), "result": item,
            "message": "Library reported success but expected identity fields are missing; do not repeat the create.", "exit_code": 1,
        }
    if Path(item["local_path"]).resolve() != local_path or item["purpose"] != "create_library_file":
        project._append_log(f"checkpoint {created['number']:02d} upload correlation unverified {utcnow()} receipt {receipt_path.relative_to(project.out)}")
        return {
            "checkpoint": str(local_path), "library_saved": "reported_success_correlation_unverified",
            "receipt": str(receipt_path), "result": item,
            "message": "Returned success does not match the requested local path/purpose; do not repeat the create.", "exit_code": 1,
        }
    metadata_ok = item.get("local_metadata_applied") is True
    project._append_log(
        f"checkpoint {created['number']:02d} saved {utcnow()} library_file_id {item['library_file_id']} "
        f"file_id {item['file_id']} local_metadata_applied {str(metadata_ok).lower()}"
    )
    return {
        "checkpoint": str(local_path), "library_saved": True,
        "library_file_id": item["library_file_id"], "file_id": item["file_id"],
        "file_name": item["file_name"], "path": item.get("path"),
        "current_version_number": item.get("current_version_number"),
        "local_metadata_applied": metadata_ok, "receipt": str(receipt_path),
        "message": "Checkpoint saved and identity metadata applied." if metadata_ok else
                   "Checkpoint is saved, but local identity metadata was not fully applied; do not repeat the create.",
        "exit_code": 0 if metadata_ok else 2,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--page-map", type=Path, default=DEFAULT_MAP)
    parser.add_argument("--helper", type=Path, default=DEFAULT_HELPER)
    args = parser.parse_args()
    try:
        result = save_checkpoint(args.out, args.page_map, args.helper)
    except (OSError, ValueError) as error:
        print(json.dumps({"verified_complete": False, "error": str(error),
                          "message": "Inspect the reported error and current checkpoint state before another write."}, ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result["exit_code"]


if __name__ == "__main__":
    raise SystemExit(main())
