#!/usr/bin/env python3
"""Create a complete checkpoint or final ZIP; never upload or overwrite a ZIP.

The checkpoint schedule begins at 2026-11-17 19:41:17 UTC and repeats hourly.
A dry run reports the planned selection and schedule without changing any files.
Images, copied source/context trees, nested ZIPs and compiled temporary files are
excluded. Everything else written under the work directory is retained.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

PREFIX = "MPL_12_051-098"
FIRST_DUE = datetime(2026, 11, 17, 19, 41, 17, tzinfo=timezone.utc)
EXCLUDED_DIRS = {"upload", "uploads", "attachment", "attachments", "source", "sources", "scan", "scans", "crop", "crops", "context", "contexts", "hua_project", "__pycache__", ".git"}
EXCLUDED_SUFFIXES = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp", ".gif", ".webp", ".pbm", ".pgm", ".ppm", ".pdf", ".zip", ".pyc", ".pyo", ".aux", ".toc", ".lof", ".lot", ".out", ".fls", ".fdb_latexmk", ".xdv", ".dvi", ".bcf", ".blg", ".bbl", ".tmp", ".temp", ".swp", ".swo"}


def utc(value: datetime) -> str:
    return value.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def atomic_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    os.replace(temporary, path)


def excluded_reason(relative: Path, path: Path, extra: list[str]) -> str | None:
    if path.is_symlink():
        return "symbolic link; target not followed"
    parts = [part.lower() for part in relative.parts]
    if any(part in EXCLUDED_DIRS or part.startswith(("context_", "context-", "scans_", "scans-", "attachments_", "attachments-")) for part in parts[:-1]):
        return "source, context, image or cache directory"
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return "source image/PDF, nested archive or compiled temporary file"
    if relative.name.endswith((".synctex.gz", ".run.xml", "~")):
        return "compiled or editor temporary file"
    if "syntaxcheck" in parts and path.suffix.lower() == ".log":
        return "compiler temporary log (retain compile_status.txt and harness instead)"
    if any(relative.match(pattern) for pattern in extra):
        return "explicit source-copy exclusion"
    return None


def selected_files(base: Path, extra: list[str]) -> tuple[list[Path], list[dict]]:
    selected: list[Path] = []
    excluded: list[dict] = []
    for path in sorted(base.rglob("*")):
        if not path.is_file() and not path.is_symlink():
            continue
        relative = path.relative_to(base)
        reason = excluded_reason(relative, path, extra)
        if reason:
            excluded.append({"path": relative.as_posix(), "reason": reason})
        else:
            selected.append(path)
    return selected, excluded


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["checkpoint", "final"])
    parser.add_argument("--base", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output-directory", type=Path)
    parser.add_argument("--exclude", action="append", default=[], help="Additional relative-path glob for a copied source tree/file")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    base = args.base.resolve()
    outdir = (args.output_directory or base.parent).resolve()
    if outdir == base or base in outdir.parents:
        raise SystemExit("Output directory must lie outside the work tree, to prevent recursive archives.")
    now = datetime.now(timezone.utc).replace(microsecond=0)
    state_path = base / "records" / "checkpoint_state.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    indices = []
    if outdir.exists():
        for path in outdir.glob(f"{PREFIX}_checkpoint_*.zip"):
            match = re.fullmatch(rf"{PREFIX}_checkpoint_(\d+)\.zip", path.name)
            if match:
                indices.append(int(match.group(1)))
    indices.append(int(state.get("last_number", 0)))
    number = max(indices, default=0) + 1
    slot = int((now - FIRST_DUE).total_seconds() // 3600)
    previous_slot = int(state.get("last_scheduled_slot", -1))
    due = now >= FIRST_DUE and slot > previous_slot
    due_at = FIRST_DUE + timedelta(hours=max(0, slot))
    next_due = FIRST_DUE + timedelta(hours=max(0, previous_slot + 1))
    filename = f"{PREFIX}_checkpoint_{number:02d}.zip" if args.mode == "checkpoint" else f"{PREFIX}.zip"
    target = outdir / filename
    files, excluded = selected_files(base, args.exclude)
    plan = {
        "mode": args.mode, "now_utc": utc(now), "first_checkpoint_due_utc": utc(FIRST_DUE),
        "checkpoint_due_now": due, "scheduled_slot": slot, "next_unsaved_due_utc": utc(next_due),
        "target": str(target), "would_overwrite": target.exists(),
        "included_files": [path.relative_to(base).as_posix() for path in files],
        "excluded_files": excluded,
    }
    if args.dry_run:
        print(json.dumps(plan, ensure_ascii=False, indent=2))
        return 0
    if args.mode == "checkpoint" and not state and max(indices, default=0) > 0:
        raise SystemExit("Existing checkpoints have no local schedule-state record; restore the last checkpoint state before creating another, to avoid an extra checkpoint in the same hour.")
    if target.exists():
        raise SystemExit(f"Refusing to overwrite {target}")
    if args.mode == "checkpoint" and not due:
        raise SystemExit(f"No checkpoint due. Next unsaved scheduled time: {utc(next_due)}")
    log_path = base / "progress.log"
    if not log_path.exists():
        raise SystemExit("progress.log is missing")
    if args.mode == "final":
        if "transcription frozen " not in log_path.read_text(encoding="utf-8"):
            raise SystemExit("Final packaging requires a transcription frozen entry in progress.log")
        validation = subprocess.run([sys.executable, str(base / "records" / "validate_structure.py"), str(base)], capture_output=True, text=True)
        if validation.returncode:
            print(validation.stdout, file=sys.stderr)
            raise SystemExit("Final structural validation failed; no archive written")
    else:
        validation = None

    # Snapshot file bytes once; never read excluded source images/context files.
    contents: dict[str, bytes] = {}
    signatures: dict[Path, tuple[int, int]] = {}
    for path in files:
        before = path.stat()
        data = path.read_bytes()
        after = path.stat()
        if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
            raise SystemExit(f"File changed during snapshot; retry when writes finish: {path.name}")
        contents[path.relative_to(base).as_posix()] = data
        signatures[path] = (after.st_size, after.st_mtime_ns)
    line = (f"checkpoint {number:02d} created {utc(now)}\n" if args.mode == "checkpoint" else f"final ZIP created {utc(now)}\n")
    old_log = contents["progress.log"]
    log_append = (b"" if old_log.endswith(b"\n") else b"\n") + line.encode("utf-8")
    contents["progress.log"] = old_log + log_append
    virtual_records: dict[str, str] = {}
    if args.mode == "checkpoint":
        new_state = {
            "first_due_utc": utc(FIRST_DUE), "last_number": number,
            "last_scheduled_slot": slot, "last_scheduled_due_utc": utc(due_at),
            "last_created_utc": utc(now), "last_filename": filename,
            "next_due_utc": utc(FIRST_DUE + timedelta(hours=slot + 1)),
            "persistence_status": "local ZIP created; Library upload must be performed separately",
        }
        virtual_records["records/checkpoint_state.json"] = json.dumps(new_state, ensure_ascii=False, indent=2) + "\n"
    if validation:
        virtual_records["records/packaging/final_validation.json"] = validation.stdout
    for relative, text in virtual_records.items():
        contents[relative] = text.encode("utf-8")
    manifest_relative = f"records/packaging/checkpoint_{number:02d}_manifest.json" if args.mode == "checkpoint" else "records/packaging/final_manifest.json"
    manifest = {
        "mode": args.mode, "filename": filename, "snapshot_utc": utc(now),
        "scheduled_due_utc": utc(due_at) if args.mode == "checkpoint" else None,
        "excluded_files": excluded,
        "files": {relative: {"size_bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()} for relative, data in sorted(contents.items())},
        "note": "This manifest does not list its own checksum. No original attachments, copied scan images or context-source files are included.",
    }
    manifest_text = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    contents[manifest_relative] = manifest_text.encode("utf-8")
    for path, signature in signatures.items():
        current = path.stat()
        if (current.st_size, current.st_mtime_ns) != signature:
            raise SystemExit(f"File changed while snapshot was assembled; retry: {path.name}")
    outdir.mkdir(parents=True, exist_ok=True)
    created_here = False
    try:
        with target.open("xb") as handle:
            created_here = True
            with ZipFile(handle, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
                for relative, data in sorted(contents.items()):
                    info = ZipInfo(relative, date_time=now.timetuple()[:6])
                    info.compress_type = ZIP_DEFLATED
                    info.external_attr = 0o600 << 16
                    archive.writestr(info, data, compresslevel=9)
        with ZipFile(target) as archive:
            if archive.testzip() is not None:
                raise RuntimeError("ZIP integrity check failed")
    except BaseException:
        if created_here:
            target.unlink(missing_ok=True)
        raise
    # Commit records only after a successfully verified ZIP exists. Its copy of
    # progress.log already contains this same exact UTC line.
    with log_path.open("ab") as handle:
        handle.write(log_append)
    for relative, text in virtual_records.items():
        atomic_text(base / relative, text)
    atomic_text(base / manifest_relative, manifest_text)
    result = {
        "created": str(target), "mode": args.mode, "snapshot_utc": utc(now),
        "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
        "file_count": len(contents), "size_bytes": target.stat().st_size,
        "next_checkpoint_due_utc": utc(FIRST_DUE + timedelta(hours=slot + 1)) if args.mode == "checkpoint" else None,
        "upload_required": True,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
