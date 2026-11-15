#!/usr/bin/env python3
"""Create one complete, hourly checkpoint ZIP, without uploading it.

Default mode only reports the plan. --create requires that the next hourly slot
is due and refuses overwrite or a checkpoint less than an hour after its
predecessor. Member order, ZIP timestamps, permissions, and compression are
normalized, so an unchanged snapshot and checkpoint number produce the same
archive bytes. Attached source archives/images are never collected.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

PREFIX = 'MPL_136_095-141'
START = datetime(2026, 11, 15, 15, 47, 55, tzinfo=timezone.utc)
CACHE_DIRS = {'__pycache__', '.git', '.cache', 'node_modules'}
EXCLUDED_SUFFIXES = {'.pyc', '.pyo', '.fmt', '.zip', '.aux', '.toc', '.synctex', '.fls', '.fdb_latexmk',
                     '.jpg', '.jpeg', '.png', '.tif', '.tiff', '.webp', '.gif'}
SUPPLIED_FILENAMES = {'PROMPT(20261115-154710).md'}
SUPPORT_SUFFIXES = {'.py', '.tex', '.md', '.json', '.csv', '.log', '.stdout', '.txt'}


def timestamp(value: datetime) -> str:
    return value.strftime('%Y-%m-%d %H:%M:%S UTC')


def collect(root: Path, manifest_name: str) -> dict[str, Path]:
    result = {}
    for path in root.rglob('*'):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if any(part in CACHE_DIRS for part in relative.parts):
            continue
        if relative.parts[0] in {'upload', 'scans', 'context'}:
            continue
        if path.suffix.lower() in EXCLUDED_SUFFIXES:
            continue
        if path.name in SUPPLIED_FILENAMES:
            continue
        if relative.as_posix() == manifest_name:
            continue
        if path.is_symlink():
            raise ValueError(f'Refusing a symlink in checkpoint inputs: {relative}')
        result[relative.as_posix()] = path
    support = root.parent / 'technical_checks'
    if support.is_dir():
        for path in support.rglob('*'):
            if not path.is_file() or path.is_symlink():
                continue
            relative = path.relative_to(support)
            if any(part in CACHE_DIRS or part.startswith('texmf-') for part in relative.parts):
                continue
            if path.suffix.lower() not in SUPPORT_SUFFIXES:
                continue
            # Per-run wrapper source is a reproducible build intermediate.
            # Preserve its diagnostics, while keeping the reusable wrapper source.
            if relative.parts[0] == 'runs' and path.suffix.lower() not in {'.log', '.stdout'}:
                continue
            result['technical_checks/' + relative.as_posix()] = path
    helpers = root.parent / 'library_helpers'
    if helpers.is_dir():
        for path in sorted(helpers.glob('*.py')):
            if path.is_file() and not path.is_symlink():
                result['library_helpers/' + path.name] = path
    return dict(sorted(result.items()))


def signature(path: Path) -> tuple[int, int, int]:
    stat = path.stat()
    return stat.st_size, stat.st_mtime_ns, stat.st_ino


def snapshot(root: Path, manifest_name: str) -> dict[str, bytes]:
    paths = collect(root, manifest_name)
    signatures = {name: signature(path) for name, path in paths.items()}
    data = {name: path.read_bytes() for name, path in paths.items()}
    if collect(root, manifest_name) != paths:
        raise RuntimeError('Checkpoint inputs changed during collection; rerun when writes are idle.')
    changed = [name for name, path in paths.items() if signature(path) != signatures[name]]
    if changed:
        raise RuntimeError('Checkpoint inputs changed during capture: ' + ', '.join(changed))
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--destination', type=Path)
    parser.add_argument('--number', type=int)
    parser.add_argument('--create', action='store_true', help='Actually create the ZIP, if due.')
    args = parser.parse_args()
    root = args.root.resolve()
    destination = (args.destination or root.parent).resolve()
    existing = {}
    for path in destination.glob(PREFIX + '_checkpoint_*.zip'):
        match = re.fullmatch(re.escape(PREFIX) + r'_checkpoint_(\d+)\.zip', path.name)
        if match:
            existing[int(match.group(1))] = path
    expected = max(existing, default=0) + 1
    number = args.number if args.number is not None else expected
    if number != expected or number < 1:
        parser.error(f'Next checkpoint number must be {expected:02d}; no gaps or overwrites.')
    if set(existing) != set(range(1, expected)):
        parser.error('Existing checkpoint numbers have a gap; restore the sequence before creating another.')
    due = START + timedelta(hours=number)
    now = datetime.now(timezone.utc)
    target = destination / f'{PREFIX}_checkpoint_{number:02d}.zip'
    manifest_name = f'records/checkpoint_manifest_{number:02d}.json'
    plan = {
        'mode': 'create' if args.create else 'plan_only',
        'checkpoint': number,
        'scheduled_utc': timestamp(due),
        'current_utc': timestamp(now),
        'due': now >= due,
        'target': str(target),
        'included_file_count': len(collect(root, manifest_name)),
        'source_files_excluded': True,
        'upload_performed': False,
    }
    if not args.create:
        print(json.dumps(plan, indent=2))
        return 0
    if now < due:
        parser.error('Checkpoint is not due until ' + timestamp(due) + '; nothing created.')
    if target.exists():
        parser.error('Refusing to overwrite ' + str(target))
    if existing:
        previous = existing[number - 1]
        elapsed = now.timestamp() - previous.stat().st_mtime
        if elapsed < 3600:
            parser.error('Less than one hour since the preceding local checkpoint; nothing created.')
    data = snapshot(root, manifest_name)
    manifest = {
        'package': PREFIX,
        'checkpoint': number,
        'scheduled_utc': timestamp(due),
        'contents': 'All current authored outputs plus technical scripts, reports, and logs.',
        'excluded': 'Supplied attachments/scans/context sources; caches; compiled PDFs, formats and auxiliary build files.',
        'files': [{'path': name, 'size': len(body), 'sha256': hashlib.sha256(body).hexdigest()}
                  for name, body in data.items()],
    }
    manifest_bytes = (json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    data[manifest_name] = manifest_bytes
    destination.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix='.checkpoint-', suffix='.tmp', dir=destination)
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for name, body in sorted(data.items()):
                info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                archive.writestr(info, body, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        # A hard-link commit is atomic and refuses an existing target.
        os.link(temporary, target)
    finally:
        temporary.unlink(missing_ok=True)
    (root / manifest_name).write_bytes(manifest_bytes)
    plan.update({'files_in_zip': len(data), 'zip_bytes': target.stat().st_size,
                 'sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
    print(json.dumps(plan, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
