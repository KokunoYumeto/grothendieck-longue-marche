#!/usr/bin/env python3
"""Package deliverables without sources, earlier archives, or symlinks.

This script never schedules a checkpoint.  The caller is responsible for the
45-minute cadence.  Archives are created with exclusive mode: no existing
checkpoint or final archive is overwritten, renamed, or deleted.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from datetime import datetime, timezone
from pathlib import Path

EXCLUDED_DIRS = {'source', 'sources', 'scans', 'witnesses', 'context', 'upload',
                 'checkpoints', '__pycache__', '.git'}
ARCHIVE_SUFFIXES = {'.zip', '.tar', '.tgz', '.gz', '.bz2', '.xz', '.7z', '.rar'}
IMAGE_SUFFIXES = {'.jpg', '.jpeg', '.png', '.tif', '.tiff', '.webp', '.bmp'}
PROJECT = 'SP02_CW_10+12'


def excluded(relative: Path) -> bool:
    if relative.name.startswith(('.audit_prepare_', '.freeze_prepare_')) and relative.suffix == '.tmp':
        return True
    if relative.suffix.lower() in ARCHIVE_SUFFIXES | IMAGE_SUFFIXES:
        return True
    checkpoint_metadata = (relative.suffix.lower() == '.json'
                           and relative.parts[:2] == ('documentation', 'checkpoints'))
    for index, p in enumerate(relative.parts[:-1]):
        low = p.lower()
        if checkpoint_metadata and index == 1 and low == 'checkpoints':
            continue
        if low in EXCLUDED_DIRS or low.endswith(('_scans', '_witnesses', '_context')):
            return True
    return False


def package(root: Path, archive: Path, dry_run=False) -> dict:
    root = root.resolve()
    archive = archive.resolve()
    if root == archive or root in archive.parents:
        raise ValueError('Archive must be outside the deliverable folder.')
    if not root.is_dir():
        raise ValueError(f'Missing deliverable folder: {root}')
    included, skipped = [], []
    for path in sorted(root.rglob('*')):
        rel = path.relative_to(root)
        if path.is_symlink():
            skipped.append({'path': str(rel), 'reason': 'symlink'})
            continue
        if not path.is_file():
            continue
        if excluded(rel):
            skipped.append({'path': str(rel), 'reason': 'source-or-archive-exclusion'})
            continue
        included.append((path, rel))
    if not included:
        raise ValueError('Refusing to create an empty archive.')
    if dry_run:
        return {'archive': str(archive), 'dry_run': True, 'archive_exists': archive.exists(),
                'included': [str(rel) for _, rel in included], 'file_count': len(included),
                'total_uncompressed_bytes': sum(p.stat().st_size for p, _ in included),
                'skipped': skipped,
                'warning': 'Read-only readiness listing. No archive or destination directory was created.'}
    archive.parent.mkdir(parents=True, exist_ok=True)
    entries = []
    with zipfile.ZipFile(archive, mode='x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for path, rel in included:
            raw = path.read_bytes()
            z.writestr(str(rel), raw)
            entries.append({'path': str(rel), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
    with zipfile.ZipFile(archive) as z:
        bad = z.testzip()
        if bad:
            raise RuntimeError(f'Archive CRC validation failed at {bad}; archive has been left intact.')
    return {'archive': str(archive), 'created_utc': datetime.now(timezone.utc).isoformat(),
            'bytes': archive.stat().st_size, 'sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
            'entries': entries, 'skipped': skipped,
            'warning': 'Packaging validates only ZIP integrity, not transcription completeness.'}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root', type=Path, required=True)
    ap.add_argument('--destination', type=Path, required=True,
                    help='Parent directory for the new archive, outside --root')
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--checkpoint', type=int, metavar='NN')
    group.add_argument('--final', action='store_true')
    ap.add_argument('--dry-run', action='store_true', help='List exactly what would be included; create nothing')
    args = ap.parse_args()
    if args.checkpoint is not None and args.checkpoint < 1:
        ap.error('--checkpoint must be at least 1')
    name = f'{PROJECT}_checkpoint_{args.checkpoint:02d}.zip' if args.checkpoint is not None else f'{PROJECT}.zip'
    print(json.dumps(package(args.root, args.destination / name, args.dry_run), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
