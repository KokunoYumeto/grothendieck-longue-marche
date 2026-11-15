#!/usr/bin/env python3
"""Create one complete hourly checkpoint, never early and never overwriting.

Default is a read-only dry run. --create writes the next numbered ZIP outside
the deliverable directory. The script never uploads or edits deliverables.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile

PREFIX = "MPL_33_002-049"
EXCLUDED_DIRS = {"upload", "uploads", "scans", "sources", "source", "context",
                 "same_cote_33", "__pycache__", ".git", ".pytest_cache"}
EXCLUDED_NAMES = {"PROMPT(3).md", f"{PREFIX}_scans.zip", f"{PREFIX}_context.zip"}


def eligible(relative: Path) -> bool:
    return not (
        any(part in EXCLUDED_DIRS or part.startswith(".") for part in relative.parts)
        or relative.name in EXCLUDED_NAMES
        or relative.suffix.lower() in {".zip", ".pyc", ".pyo"}
        or re.fullmatch(r"MPL_33_002-049_33_scan\d{3}(?:_[ab])?\.jpg", relative.name)
    )


def collect(root: Path, workspace: Path) -> list[tuple[Path, str]]:
    selected = {}
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if path.is_file() and eligible(rel):
            if path.is_symlink():
                raise ValueError(f"Refusing a symlink: {path}")
            selected[rel.as_posix()] = path
    support = workspace / "support"
    if support.is_dir():
        for path in sorted(support.rglob("*")):
            rel = path.relative_to(workspace)
            if path.is_file() and eligible(rel):
                if path.is_symlink():
                    raise ValueError(f"Refusing a symlink: {path}")
                selected[rel.as_posix()] = path
    # Root-level generated utility scripts are included without looking into
    # uploaded material, the scan tree, or the context archive.
    for path in sorted(workspace.iterdir()):
        if path.is_file() and path.suffix.lower() in {".py", ".sh", ".js", ".mjs"}:
            if path.is_symlink():
                raise ValueError(f"Refusing a symlink: {path}")
            selected["support/workspace_root_scripts/" + path.name] = path
    return [(selected[rel], rel) for rel in sorted(selected)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, nargs="?", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--create", action="store_true", help="Create the due checkpoint; otherwise only describe it")
    args = parser.parse_args()
    root = args.root.resolve()
    workspace = root.parent
    first_line = (root / "progress.log").open(encoding="utf-8").readline().strip()
    started = datetime.strptime(first_line, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
    existing = []
    for path in workspace.glob(f"{PREFIX}_checkpoint_*.zip"):
        match = re.fullmatch(re.escape(PREFIX) + r"_checkpoint_(\d+)\.zip", path.name)
        if match:
            existing.append(int(match.group(1)))
    number = max(existing, default=0) + 1
    due = started + timedelta(hours=number)
    now = datetime.now(timezone.utc)
    output = workspace / f"{PREFIX}_checkpoint_{number:02}.zip"
    files = collect(root, workspace)
    info = {"mode": "create" if args.create else "dry-run", "next_number": number,
            "due_utc": due.strftime("%Y-%m-%d %H:%M:%S UTC"),
            "current_utc": now.strftime("%Y-%m-%d %H:%M:%S UTC"),
            "due_now": now >= due, "output": str(output), "file_count": len(files),
            "uncompressed_bytes": sum(path.stat().st_size for path, _ in files)}
    if not args.create:
        print(json.dumps(info, indent=2))
        return 0
    if now < due:
        print(json.dumps({**info, "error": "Checkpoint is not due; no ZIP created."}, indent=2))
        return 2
    if output.exists():
        print(json.dumps({**info, "error": "Output already exists; never overwrite."}, indent=2))
        return 2

    # Read all files to a stable in-memory snapshot before creating the ZIP.
    snapshot = []
    source_states = []
    for path, relative in files:
        before = path.stat()
        data = path.read_bytes()
        after = path.stat()
        state = (after.st_size, after.st_mtime_ns)
        if (before.st_size, before.st_mtime_ns) != state:
            raise RuntimeError(f"File changed while checkpoint snapshot was read: {path}; retry after the edit completes")
        snapshot.append((relative, data))
        source_states.append((path, state))
    if any((p.stat().st_size, p.stat().st_mtime_ns) != state for p, state in source_states):
        raise RuntimeError("A file changed during the checkpoint snapshot; retry after the edit completes")
    manifest = [f"Complete checkpoint {number:02}", f"Created {now.strftime('%Y-%m-%d %H:%M:%S UTC')}",
                "Supplied scans, prompt, context, previous ZIPs, and caches are excluded.",
                "All current deliverables, notes, logs, records, and support scripts are included.", "", "SHA-256  relative path"]
    manifest.extend(f"{hashlib.sha256(data).hexdigest()}  {relative}" for relative, data in snapshot)
    fd, temporary = tempfile.mkstemp(prefix=f".{PREFIX}_checkpoint_{number:02}_", suffix=".tmp", dir=workspace)
    os.close(fd)
    temp = Path(temporary)
    try:
        with ZipFile(temp, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
            for relative, data in snapshot:
                archive.writestr(relative, data)
            archive.writestr(f"records/checkpoint_{number:02}_snapshot.txt", "\n".join(manifest) + "\n")
        with ZipFile(temp) as archive:
            bad = archive.testzip()
            if bad:
                raise RuntimeError(f"ZIP integrity failure: {bad}")
        # Hard-link publication is atomic and fails rather than overwriting.
        os.link(temp, output)
    finally:
        temp.unlink(missing_ok=True)
    print(json.dumps({**info, "created": True, "bytes": output.stat().st_size,
                      "sha256": hashlib.sha256(output.read_bytes()).hexdigest()}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
