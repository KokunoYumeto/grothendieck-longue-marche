#!/usr/bin/env python3
"""Prepare an immutable checkpoint ZIP only when the actual 45-minute gate is due.

Default invocation reports status without writing anything. --create packages
the contents of out/ at the ZIP root, including records, scripts and crops, but
omits every file with a .zip suffix. No earlier checkpoint is overwritten,
renamed, deleted, or included. The tool never uploads and never modifies
run_state.json, progress.log, or another deliverable. After a successful durable
save, the caller must update last_checkpoint_utc and checkpoint_number using
the values printed here; preserving the upload result is the caller's job.

The gate uses the real UTC clock. There is intentionally no clock override or
force option. Boundaries are anchored to run_state.json's started_utc.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import tempfile
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path


PERIOD = timedelta(minutes=45)
SOURCE_DIRECTORIES = {
    'source', 'upload', 'SP33_CW_156-5_scans', 'SP33_CW_156-5_witnesses',
    'SP33_CW_156-5_context', 'SP33_CW_156-5_sweep3',
}


def parse_utc(value: str) -> datetime:
    if not isinstance(value, str):
        raise ValueError("A run-state timestamp is not a string")
    if value.endswith(" UTC"):
        parsed = datetime.strptime(value, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
    else:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError("A run-state timestamp has no timezone")
        parsed = parsed.astimezone(timezone.utc)
    return parsed


def utc_text(value: datetime) -> str:
    return value.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def next_gate(state: dict) -> tuple[datetime, int]:
    start = parse_utc(state["started_utc"])
    last = parse_utc(state.get("last_checkpoint_utc", state["started_utc"]))
    count = state.get("checkpoint_number", 0)
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        raise ValueError("checkpoint_number must be a nonnegative integer")
    if last < start:
        raise ValueError("last_checkpoint_utc precedes started_utc")
    # A delayed checkpoint must not allow an immediate catch-up checkpoint at a
    # boundary already passed when it was saved. The schedule stays anchored.
    last_boundary = math.floor((last - start).total_seconds() / PERIOD.total_seconds())
    boundary_number = max(count + 1, last_boundary + 1)
    return start + boundary_number * PERIOD, count + 1


def source_files(root: Path) -> list[Path]:
    files = []
    for path in sorted(root.rglob("*")):
        if path.relative_to(root).parts[0] in SOURCE_DIRECTORIES:
            raise ValueError(f"Original source-material directory found inside output; refusing inclusion: {path.relative_to(root).parts[0]}")
        if path.is_symlink():
            raise ValueError(f"Refusing a symlink in checkpoint source: {path.relative_to(root)}")
        if path.is_file() and path.suffix.lower() != ".zip":
            files.append(path)
    return files


def signature(path: Path) -> tuple[int, int, int, int]:
    value = path.stat()
    return value.st_dev, value.st_ino, value.st_size, value.st_mtime_ns


def create_archive(root: Path, destination: Path, metadata: dict) -> tuple[int, int]:
    if destination.exists():
        raise FileExistsError(f"Checkpoint already exists; it will not be overwritten: {destination}")
    files = source_files(root)
    if not files:
        raise ValueError("No checkpoint source files found")
    before = {p: signature(p) for p in files}
    destination.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary_name = tempfile.mkstemp(prefix=".checkpoint-", suffix=".partial", dir=destination.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(handle, "wb") as stream:
            with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
                for path in files:
                    archive.write(path, path.relative_to(root).as_posix())
                archive.comment = json.dumps(metadata, ensure_ascii=True, sort_keys=True).encode("utf-8")
            stream.flush()
            os.fsync(stream.fileno())
        if source_files(root) != files or any(signature(p) != before[p] for p in files):
            raise RuntimeError("Output changed during checkpoint creation; no checkpoint was committed. Retry when page saving is idle.")
        # Hard-link publication is atomic and cannot replace an existing filename.
        os.link(temporary, destination)
        return len(files), destination.stat().st_size
    finally:
        temporary.unlink(missing_ok=True)


def self_test() -> None:
    base = {"started_utc": "2026-11-19 20:23:06 UTC", "last_checkpoint_utc": "2026-11-19 20:23:06 UTC", "checkpoint_number": 0}
    due, number = next_gate(base)
    assert utc_text(due) == "2026-11-19 21:08:06 UTC" and number == 1
    base.update(last_checkpoint_utc="2026-11-19 21:10:06 UTC", checkpoint_number=1)
    due, number = next_gate(base)
    assert utc_text(due) == "2026-11-19 21:53:06 UTC" and number == 2
    base.update(last_checkpoint_utc="2026-11-19 22:00:00 UTC", checkpoint_number=1)
    due, number = next_gate(base)
    assert utc_text(due) == "2026-11-19 22:38:06 UTC" and number == 2
    assert parse_utc("2026-11-19T20:23:06Z") == parse_utc("2026-11-19 20:23:06 UTC")
    with tempfile.TemporaryDirectory(prefix="synthetic-package-filter-") as temporary:
        root = Path(temporary)
        wanted = ['notes.md', 'proofs/check.md', 'records/result.json', 'crops/detail.jpg', 'scripts/check.py']
        for name in wanted + ['old.zip', 'old_uppercase.ZIP']:
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b'synthetic file-list fixture; not a real archive or image')
        assert [p.relative_to(root).as_posix() for p in source_files(root)] == sorted(wanted)
        (root / 'SP33_CW_156-5_context').mkdir()
        try:
            source_files(root)
        except ValueError as exc:
            assert 'source-material directory' in str(exc)
        else:
            raise AssertionError('Original source-material directory was not rejected')
    print("Synthetic schedule and file-list filter checks passed; no real output files or archives created.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--destination-directory", type=Path)
    parser.add_argument("--create", action="store_true", help="Create a ZIP if the actual UTC gate has passed")
    parser.add_argument("--self-test", action="store_true", help="Test pure schedule arithmetic without reading state or creating files")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    root = args.out.resolve()
    destination_directory = (args.destination_directory or root.parent / "checkpoints").resolve()
    if destination_directory == root or destination_directory.is_relative_to(root):
        parser.error("Checkpoint destination must be outside the output tree")
    state_path = root / "records" / "run_state.json"
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
        due, number = next_gate(state)
        now = datetime.now(timezone.utc)
        if parse_utc(state["started_utc"]) > now or parse_utc(state.get("last_checkpoint_utc", state["started_utc"])) > now:
            raise ValueError("Run-state timestamps are in the future relative to the actual UTC clock")
        destination = destination_directory / f"SP33_CW_156-5_checkpoint_{number:02d}.zip"
        status = {
            "actual_utc": utc_text(now), "next_boundary_utc": utc_text(due),
            "checkpoint_number": number, "due": now >= due,
            "archive": str(destination), "created": False,
            "state_update": "Caller updates last_checkpoint_utc and checkpoint_number only after durable save succeeds.",
        }
        if not args.create:
            print(json.dumps(status, indent=2))
            return 0
        if now < due:
            print(json.dumps(status, indent=2))
            print("Checkpoint refused: the actual 45-minute boundary has not arrived.")
            return 3
        metadata = {"created_utc": utc_text(now), "boundary_utc": utc_text(due), "checkpoint_number": number}
        count, size = create_archive(root, destination, metadata)
        status.update(created=True, created_utc=utc_text(now), files=count, bytes=size)
        print(json.dumps(status, indent=2))
        return 0
    except (ValueError, KeyError, OSError, RuntimeError) as exc:
        parser.exit(2, str(exc) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
