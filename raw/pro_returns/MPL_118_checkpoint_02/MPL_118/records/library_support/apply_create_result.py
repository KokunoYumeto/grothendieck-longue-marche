#!/usr/bin/env python3
"""Apply a single Library create response to its original local ZIP.
No network or Library reads; delegates metadata writeback to the current skill helper.
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

def parse_response(raw):
    if not isinstance(raw, dict):
        raise ValueError("expected a complete create CallToolResult object")
    if raw.get("isError") is True:
        raise ValueError("Library create returned isError")
    if raw.get("structuredContent") is not None:
        return raw["structuredContent"]
    values = []
    for block in raw.get("content", []):
        if isinstance(block, dict) and block.get("type") == "text":
            try:
                values.append(json.loads(block["text"]))
            except (ValueError, KeyError):
                pass
    return values if values else raw

def objects(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from objects(child)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("local_path", type=Path)
    p.add_argument("--record", type=Path, help="write minimal identity metadata here")
    args = p.parse_args()
    if not args.local_path.is_absolute() or not args.local_path.is_file():
        raise ValueError("local_path must be an existing absolute file")
    result = parse_response(json.load(sys.stdin))
    nodes = list(objects(result))
    ids = {n["library_file_id"] for n in nodes if isinstance(n.get("library_file_id"), str)}
    if len(ids) != 1:
        raise ValueError(f"expected exactly one Library identity, found {len(ids)}")
    library_id = ids.pop()
    arrays = [n["xattrs"] for n in nodes if isinstance(n.get("xattrs"), list) and n["xattrs"]]
    distinct_arrays = {json.dumps(a, sort_keys=True, separators=(",", ":")) for a in arrays}
    if len(distinct_arrays) > 1:
        raise ValueError("conflicting xattrs arrays; preserve response and inspect")
    xattrs = json.loads(distinct_arrays.pop()) if distinct_arrays else []
    for a in xattrs:
        if not isinstance(a, dict) or not isinstance(a.get("name"), str) or not isinstance(a.get("value"), str):
            raise ValueError("malformed xattrs array")
    helper = Path(__file__).resolve().parent / "library_file_transfer.py"
    done = subprocess.run(
        [sys.executable, str(helper), "apply-xattrs", str(args.local_path), library_id],
        input=json.dumps(xattrs), text=True, capture_output=True,
    )
    if done.returncode:
        raise RuntimeError(done.stderr.strip() or "metadata helper failed")
    metadata = {
        "local_path": str(args.local_path),
        "library_file_id": library_id,
        "metadata_applied_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "xattrs": xattrs,
    }
    keys = ("file_id", "file_name", "filename", "path", "version", "version_id", "version_number", "current_version_number")
    identity_nodes = [n for n in nodes if n.get("library_file_id") == library_id]
    for key in keys:
        values = [n[key] for n in identity_nodes if key in n]
        if values and all(v == values[0] for v in values):
            metadata[key] = values[0]
    if args.record:
        args.record.parent.mkdir(parents=True, exist_ok=True)
        if args.record.exists():
            raise ValueError("refusing to overwrite an existing upload record")
        args.record.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k:v for k,v in metadata.items() if k != "xattrs"}, ensure_ascii=False))

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"create metadata writeback failed: {exc}", file=sys.stderr)
        sys.exit(1)

