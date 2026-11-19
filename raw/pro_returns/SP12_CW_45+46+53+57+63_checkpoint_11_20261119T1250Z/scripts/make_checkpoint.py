#!/usr/bin/env python3
"""Create at most one output checkpoint when a new 45-minute threshold is due.

The clock starts at the first UTC timestamp in progress.log (for this task,
2026-11-19 04:35:45 UTC). Delayed invocations create one current snapshot rather
than backfilling several identical ZIPs. ZIPs and SHA-256 manifests are numbered
sequentially under checkpoints/. Existing files are never overwritten.

Only output files are packaged. Sources, scans, context, witnesses, input and
attachment directories, image files, archives, symlinks, and caches are skipped.
Keep originals outside the output tree. No transcription or editorial checks
are performed. --dry-run inspects bookkeeping metadata without writing files.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
from datetime import datetime, timedelta, timezone
import zipfile


INTERVAL_SECONDS = 45 * 60
STAMP_FORMAT = "%Y-%m-%d %H:%M:%S UTC"
STAMP = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC")
FORMAT = "archival-output-checkpoint-v1"
EMBEDDED_MANIFEST = "CHECKPOINT_MANIFEST.json"
SOURCE_NAME = re.compile(
    r"(?:^|[._\s-])(?:sources?|scans?|contexts?|witness(?:es)?|inputs?|"
    r"attachments?|originals?|images?)(?:$|[._\s-])", re.IGNORECASE
)
CACHE_DIRS = {
    "__pycache__", "cache", "caches", "node_modules", "venv",
    ".venv", ".git", ".svn", ".hg", ".cache", ".pytest_cache",
    ".mypy_cache", ".ruff_cache", ".ipynb_checkpoints",
}
EXCLUDED_SUFFIXES = {
    ".zip", ".7z", ".rar", ".tar", ".gz", ".tgz", ".bz2", ".xz",
    ".jpg", ".jpeg", ".png", ".tif", ".tiff", ".jp2", ".jpx",
    ".webp", ".gif", ".bmp", ".heic", ".heif", ".raw", ".psd",
    ".pyc", ".pyo", ".tmp", ".temp", ".bak", ".swp", ".lock",
}


def utc_stamp(value: datetime) -> str:
    return value.astimezone(timezone.utc).strftime(STAMP_FORMAT)


def parse_stamp(value: str) -> datetime:
    return datetime.strptime(value, STAMP_FORMAT).replace(tzinfo=timezone.utc)


def regular_file(path: Path) -> bool:
    try:
        return stat.S_ISREG(path.lstat().st_mode)
    except OSError:
        return False


def checkpoint_pattern(prefix: str) -> re.Pattern[str]:
    return re.compile(
        rf"^{re.escape(prefix)}_checkpoint_(\d+)(?:\.zip|\.manifest\.json)$"
    )


def checkpoint_files(root: Path) -> list[Path]:
    pattern = checkpoint_pattern(root.name)
    result = []
    for directory in (root, root / "checkpoints"):
        if directory.is_symlink():
            raise ValueError(f"Checkpoint directory is a symlink: {directory}")
        if not directory.exists():
            continue
        if not directory.is_dir():
            raise ValueError(f"Checkpoint directory is not a directory: {directory}")
        result.extend(path for path in directory.iterdir() if pattern.fullmatch(path.name))
    return result


def schedule(root: Path, current: datetime) -> dict:
    progress = root / "progress.log"
    if not regular_file(progress):
        raise ValueError("progress.log must be an existing regular, non-symlinked file.")
    log = progress.read_text(encoding="utf-8")
    first = STAMP.search(log)
    if first is None:
        raise ValueError("No UTC timestamp found in progress.log.")
    origin = parse_stamp(first.group(0))
    elapsed = int((current - origin).total_seconds())
    if elapsed < 0:
        raise ValueError("The first progress timestamp is later than the current UTC time.")
    current_threshold = elapsed // INTERVAL_SECONDS
    completed_threshold = 0
    numbers = []
    pattern = checkpoint_pattern(root.name)
    for path in checkpoint_files(root):
        numbers.append(int(pattern.fullmatch(path.name).group(1)))
        if not path.name.endswith(".manifest.json"):
            continue
        if not regular_file(path):
            raise ValueError(f"Checkpoint manifest is not a regular file: {path.name}")
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("format") != FORMAT:
            raise ValueError(f"Unrecognized checkpoint manifest format: {path.name}")
        if record.get("origin_utc") != utc_stamp(origin):
            raise ValueError(f"Checkpoint origin differs from progress.log: {path.name}")
        zip_name = record.get("zip_filename", "")
        if not isinstance(zip_name, str) or Path(zip_name).name != zip_name:
            raise ValueError(f"Unsafe ZIP filename in checkpoint manifest: {path.name}")
        if not regular_file(path.parent / zip_name):
            raise ValueError(f"Completed checkpoint ZIP is missing/non-regular: {zip_name}")
        completed_threshold = max(completed_threshold, int(record["threshold_number"]))
    # The append-only log also retains state if a checkpoint is moved out of
    # this directory after successful creation.
    for line in log.splitlines():
        if not line.startswith("CHECKPOINT_COMPLETE ") or " | " not in line:
            continue
        record = json.loads(line.split(" | ", 1)[1])
        if record.get("origin_utc") == utc_stamp(origin):
            completed_threshold = max(completed_threshold, int(record["threshold_number"]))
            numbers.append(int(record["checkpoint_number"]))
    return {
        "origin": origin, "current": current, "elapsed_seconds": elapsed,
        "threshold_number": current_threshold,
        "completed_threshold": completed_threshold,
        "checkpoint_number": max(numbers, default=0) + 1,
        "due": current_threshold > completed_threshold,
    }


def excluded_name(name: str, is_directory: bool) -> str | None:
    lower = name.lower()
    if lower.startswith(".") or lower in CACHE_DIRS:
        return "cache or hidden bookkeeping file"
    if is_directory and "checkpoint" in lower:
        return "earlier checkpoints"
    if is_directory and lower in {"work_crops", "work-crops"}:
        return "working crops"
    if SOURCE_NAME.search(name):
        return "source, scan, context, witness, or attachment"
    if not is_directory:
        if Path(name).suffix.lower() in EXCLUDED_SUFFIXES:
            return "archive, image, or temporary file"
        if name.endswith("~"):
            return "backup file"
        if re.search(r"_checkpoint_\d+\.manifest\.json$", name, re.IGNORECASE):
            return "earlier checkpoint manifest"
    return None


def collect_files(root: Path) -> tuple[list[Path], list[dict]]:
    selected, excluded = [], []
    for directory, dirs, files in os.walk(root, followlinks=False):
        base = Path(directory)
        kept = []
        for name in sorted(dirs):
            path = base / name
            reason = "symlink" if path.is_symlink() else excluded_name(name, True)
            if reason:
                excluded.append({"path": path.relative_to(root).as_posix() + "/", "reason": reason})
            else:
                kept.append(name)
        dirs[:] = kept
        for name in sorted(files):
            path = base / name
            reason = excluded_name(name, False)
            # These generated tooling names contain "context" but are not
            # original context material. Keep the exception local to their
            # exact output directories, safe suffixes and timestamp patterns.
            relative = path.relative_to(root)
            generated_context_tool = (
                len(relative.parts) == 2
                and (
                    (relative.parts[0] == "scripts" and name in {
                        "check_tex_math_context.py", "test_tex_math_context.py"
                    })
                    or (relative.parts[0] == "diagnostics" and re.fullmatch(
                        r"(?:tex_math_context_\d{8}_\d{6}_\d{6}\.(?:md|json)|"
                        r"math_context_checker_install_\d{8}_\d{6}_\d{6}_"
                        r"(?:hashes\.json|tests\.txt))", name
                    ))
                )
            )
            if generated_context_tool and reason == "source, scan, context, witness, or attachment":
                reason = None
            if not regular_file(path):
                reason = "symlink or non-regular file"
            if reason:
                excluded.append({"path": path.relative_to(root).as_posix(), "reason": reason})
            else:
                selected.append(path)
    return sorted(selected, key=lambda p: p.relative_to(root).as_posix()), excluded


def signature(value: os.stat_result) -> tuple:
    return value.st_dev, value.st_ino, value.st_size, value.st_mtime_ns


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


@contextmanager
def checkpoint_lock(root: Path):
    path = root / ".checkpoint.lock"
    try:
        descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        raise RuntimeError(
            f"Checkpoint lock already exists: {path}. A previous run may still be active; "
            "remove the lock only after confirming that no checkpoint process is running."
        ) from None
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(f"pid={os.getpid()} UTC={utc_stamp(datetime.now(timezone.utc))}\n")
        yield
    finally:
        path.unlink()


def create_checkpoint(root: Path, state: dict) -> tuple[Path, Path]:
    directory = root / "checkpoints"
    directory.mkdir(exist_ok=True)
    if directory.is_symlink() or not directory.is_dir():
        raise ValueError("checkpoints must be a regular directory.")
    basename = f"{root.name}_checkpoint_{state['checkpoint_number']:03d}"
    zip_path = directory / (basename + ".zip")
    manifest_path = directory / (basename + ".manifest.json")
    for path in (zip_path, manifest_path):
        if path.exists() or path.is_symlink():
            raise FileExistsError(f"Refusing to overwrite existing file: {path}")
    selected, excluded = collect_files(root)
    if not selected:
        raise ValueError("No eligible output files to include in the checkpoint.")
    manifest = {
        "format": FORMAT,
        "checkpoint_number": state["checkpoint_number"],
        "threshold_number": state["threshold_number"],
        "previous_completed_threshold": state["completed_threshold"],
        "interval_seconds": INTERVAL_SECONDS,
        "origin_utc": utc_stamp(state["origin"]),
        "created_utc": utc_stamp(state["current"]),
        "elapsed_seconds": state["elapsed_seconds"],
        "zip_filename": zip_path.name,
        "files": [], "excluded": excluded,
        "note": "Output snapshot only; no editorial verification. The completion event is appended to progress.log after this snapshot.",
    }
    zip_created = manifest_created = complete = False
    signatures = {}
    try:
        with zipfile.ZipFile(zip_path, mode="x", compression=zipfile.ZIP_DEFLATED) as archive:
            zip_created = True
            for path in selected:
                relative = path.relative_to(root).as_posix()
                if relative == EMBEDDED_MANIFEST:
                    raise ValueError(f"Reserved checkpoint metadata filename already exists: {relative}")
                descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
                with os.fdopen(descriptor, "rb") as source:
                    before = os.fstat(source.fileno())
                    if not stat.S_ISREG(before.st_mode):
                        raise ValueError(f"Output is no longer a regular file: {relative}")
                    info = zipfile.ZipInfo.from_file(path, arcname=relative, strict_timestamps=False)
                    info.compress_type = zipfile.ZIP_DEFLATED
                    digest = hashlib.sha256()
                    size = 0
                    with archive.open(info, mode="w", force_zip64=True) as member:
                        for block in iter(lambda: source.read(1024 * 1024), b""):
                            member.write(block)
                            digest.update(block)
                            size += len(block)
                    if signature(before) != signature(os.fstat(source.fileno())):
                        raise RuntimeError(f"Output changed during packaging; retry when stable: {relative}")
                    signatures[path] = signature(before)
                    manifest["files"].append({"path": relative, "bytes": size, "sha256": digest.hexdigest()})
            # Refuse a mixed snapshot if any selected file changed or if the
            # set of eligible output files changed while the archive was built.
            if collect_files(root)[0] != selected:
                raise RuntimeError("Output filenames changed during packaging; retry when stable.")
            for path, expected in signatures.items():
                if signature(path.lstat()) != expected:
                    raise RuntimeError(f"Output changed during packaging: {path.relative_to(root)}")
            archive.writestr(EMBEDDED_MANIFEST, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        manifest["zip_sha256"] = sha256_file(zip_path)
        with manifest_path.open("x", encoding="utf-8") as handle:
            manifest_created = True
            handle.write(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        complete = True
        completion = datetime.now(timezone.utc)
        log_record = {
            "checkpoint_number": state["checkpoint_number"],
            "threshold_number": state["threshold_number"],
            "origin_utc": utc_stamp(state["origin"]),
            "elapsed_seconds": state["elapsed_seconds"],
            "file_count": len(manifest["files"]),
            "zip": zip_path.relative_to(root).as_posix(),
            "zip_sha256": manifest["zip_sha256"],
            "manifest": manifest_path.relative_to(root).as_posix(),
            "manifest_sha256": sha256_file(manifest_path),
        }
        with (root / "progress.log").open("a", encoding="utf-8") as handle:
            handle.write("\nCHECKPOINT_COMPLETE " + utc_stamp(completion) + " | " + json.dumps(log_record, ensure_ascii=False, separators=(",", ":")) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        return zip_path, manifest_path
    finally:
        # Only remove files this invocation created and failed to complete.
        # Earlier checkpoints and the existing output files are never changed.
        if not complete:
            for path, created in ((manifest_path, manifest_created), (zip_path, zip_created)):
                if created:
                    path.unlink(missing_ok=True)


def describe(state: dict) -> None:
    elapsed_minutes, elapsed_seconds = divmod(state["elapsed_seconds"], 60)
    print(f"Origin: {utc_stamp(state['origin'])}")
    print(f"Current UTC: {utc_stamp(state['current'])}")
    print(f"Elapsed: {elapsed_minutes} minutes {elapsed_seconds} seconds")
    print(f"Current threshold: {state['threshold_number']}; last completed threshold: {state['completed_threshold']}")
    if state["due"]:
        print(f"Checkpoint {state['checkpoint_number']:03d} is due.")
    else:
        next_threshold = max(state["threshold_number"], state["completed_threshold"]) + 1
        next_time = state["origin"] + timedelta(seconds=next_threshold * INTERVAL_SECONDS)
        print(f"No new checkpoint is due. Next threshold: {utc_stamp(next_time)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Output root; defaults to this script's parent output directory.")
    parser.add_argument("--dry-run", action="store_true", help="Report the schedule without creating a lock, ZIP, manifest, or log entry.")
    args = parser.parse_args()
    try:
        supplied_root = args.root.expanduser()
        if supplied_root.is_symlink() or not supplied_root.is_dir():
            raise ValueError("Output root must be an existing, non-symlinked directory.")
        root = supplied_root.resolve()
        state = schedule(root, datetime.now(timezone.utc))
        if args.dry_run or not state["due"]:
            describe(state)
            if args.dry_run:
                print("Dry run: no files were written.")
            return 0
        with checkpoint_lock(root):
            # Re-read state after acquiring the lock so concurrent invocations
            # cannot create two checkpoints for the same threshold.
            state = schedule(root, datetime.now(timezone.utc))
            describe(state)
            if not state["due"]:
                return 0
            zip_path, manifest_path = create_checkpoint(root, state)
            print(f"Created: {zip_path}")
            print(f"Manifest: {manifest_path}")
            print("Appended completion time, archive hash, and manifest reference/hash to progress.log.")
        return 0
    except (OSError, ValueError, KeyError, RuntimeError, zipfile.BadZipFile) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
