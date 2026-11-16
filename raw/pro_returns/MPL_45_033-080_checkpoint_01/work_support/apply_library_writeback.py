#!/usr/bin/env python3
"""Apply one successful Library write result to its original local file.

Receives the COMPLETE create/replace tool result as one JSON object on stdin.
This script does not upload anything. Invoke immediately after the create call,
inside the same code-mode invocation. Unknown or ambiguous results fail closed.
"""
import argparse
import json
from pathlib import Path
import subprocess
import sys

def dicts(value):
    if isinstance(value, dict):
        yield value
        for key, child in value.items():
            if key == "text" and isinstance(child, str):
                try:
                    parsed = json.loads(child)
                except (ValueError, TypeError):
                    continue
                yield from dicts(parsed)
            elif isinstance(child, (dict, list)):
                yield from dicts(child)
    elif isinstance(value, list):
        for child in value:
            yield from dicts(child)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("original_path", type=Path)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    local_path = args.original_path
    if not local_path.is_absolute() or not local_path.is_file():
        parser.error("original_path must be an absolute regular file")
    if not args.receipt.is_absolute():
        parser.error("receipt must be absolute")
    response = json.load(sys.stdin)
    if not isinstance(response, dict) or response.get("isError") is True:
        raise ValueError("Library create/replace did not return success")
    candidates = [obj for obj in dicts(response)
                  if isinstance(obj.get("library_file_id"), str)
                  and obj["library_file_id"]]
    ids = {obj["library_file_id"] for obj in candidates}
    if len(ids) != 1:
        raise ValueError("Write result has no unique Library identity; inspect it without re-uploading")
    for obj in candidates:
        if obj.get("status") not in (None, "succeeded", "success"):
            raise ValueError("Write result contains a non-success item")
    library_file_id = next(iter(ids))
    arrays = [obj["xattrs"] for obj in candidates if obj.get("xattrs") is not None]
    if any(not isinstance(array, list) for array in arrays):
        raise ValueError("Write result xattrs must be complete arrays")
    normalized_arrays = {json.dumps(a, sort_keys=True) for a in arrays}
    if len(normalized_arrays) > 1:
        raise ValueError("Write result contains conflicting xattrs")
    xattrs = arrays[0] if arrays else []
    # The maintained helper validates and applies the whole returned array.
    helper = Path(__file__).resolve().parent / "library_file_transfer.py"
    result = subprocess.run(
        [sys.executable, str(helper), "apply-xattrs", str(local_path), library_file_id],
        input=json.dumps(xattrs), text=True, capture_output=True)
    if result.returncode:
        sys.stderr.write(result.stderr)
        raise RuntimeError("Library upload succeeded but local identity writeback failed; do not re-upload")
    receipt = {"local_path": str(local_path), "library_file_id": library_file_id,
               "local_metadata_applied": True}
    for key in ("file_id", "file_name", "path", "current_version_number"):
        values = {json.dumps(obj[key], sort_keys=True) for obj in candidates
                  if key in obj and obj[key] is not None}
        if len(values) > 1:
            raise ValueError("Write result metadata conflict for " + key)
        if values:
            receipt[key] = json.loads(next(iter(values)))
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8")
    print(json.dumps(receipt, ensure_ascii=False))

if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError) as error:
        sys.exit("Library writeback: " + str(error))

