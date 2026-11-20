#!/usr/bin/env python3
"""Package deliverables without sources, earlier archives, or symlinks.

This script never schedules a checkpoint.  The caller is responsible for the
45-minute cadence.  Archives are prepared in an exclusive temporary file in
the destination directory, closed and CRC-checked, then published by an
exclusive hard link.  No existing checkpoint or final archive is overwritten,
renamed, or deleted.  Only the tool-owned temporary file is cleaned up; an
interrupted process may leave that temporary file without occupying the final
archive name. Final mode requires readiness and binds the temporary archive
to its required input hashes, protected tree membership, and absent paths.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
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


def final_membership(names: set[str], readiness: dict) -> None:
    """Reject omitted gate inputs or changed protected archive membership."""
    missing = set(readiness['input_sha256']) - names
    if missing:
        raise ValueError(f'Final archive omits readiness inputs: {sorted(missing)}')
    for tree, expected in readiness['protected_tree_membership'].items():
        actual = {name for name in names if name == tree or name.startswith(tree + '/')}
        if actual != set(expected):
            raise ValueError(f'Final archive protected tree differs from readiness: {tree}')
    for absent in readiness['protected_absent_paths']:
        if any(name == absent or name.startswith(absent + '/') for name in names):
            raise ValueError(f'Final archive contains a required-absent path: {absent}')


def package(root: Path, archive: Path, dry_run=False, *, final=False) -> dict:
    root = root.resolve()
    archive = archive.resolve()
    if root == archive or root in archive.parents:
        raise ValueError('Archive must be outside the deliverable folder.')
    if not root.is_dir():
        raise ValueError(f'Missing deliverable folder: {root}')
    readiness = None
    if final:
        import validate_final_readiness
        readiness = validate_final_readiness.validate_readiness(root)
        if readiness.get('ok') is not True:
            raise ValueError('Final readiness gate did not pass.')
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
    if final:
        final_membership({str(rel) for _, rel in included}, readiness)
    if dry_run:
        return {'archive': str(archive), 'dry_run': True, 'archive_exists': archive.exists(),
                'included': [str(rel) for _, rel in included], 'file_count': len(included),
                'total_uncompressed_bytes': sum(p.stat().st_size for p, _ in included),
                'skipped': skipped,
                'warning': 'Read-only readiness listing. No archive or destination directory was created.'}
    archive.parent.mkdir(parents=True, exist_ok=True)
    if archive.exists():
        raise FileExistsError(f'Refusing to replace an existing archive: {archive}')
    entries = []
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f'.{archive.name}.prepare_', suffix='.tmp', dir=archive.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, 'w+b') as stream:
            with zipfile.ZipFile(stream, mode='w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
                for path, rel in included:
                    raw = path.read_bytes()
                    z.writestr(str(rel), raw)
                    entries.append({'path': str(rel), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
            stream.flush()
            os.fsync(stream.fileno())
        with zipfile.ZipFile(temporary) as z:
            bad = z.testzip()
            if bad:
                raise RuntimeError(f'Archive CRC validation failed at {bad}; final archive was not published.')
            if final:
                names = z.namelist()
                if len(names) != len(set(names)):
                    raise ValueError('Final archive contains duplicate members.')
                final_membership(set(names), readiness)
                for name, expected in readiness['input_sha256'].items():
                    if hashlib.sha256(z.read(name)).hexdigest() != expected:
                        raise ValueError(f'Final archive bytes differ from readiness: {name}')
        archive_size = temporary.stat().st_size
        archive_hash = hashlib.sha256(temporary.read_bytes()).hexdigest()
        # The same-directory hard link is exclusive even if another writer
        # creates the final name after the initial existence check.
        os.link(temporary, archive)
    except BaseException:
        # Never remove the final path, including after a publication race.
        # A cleanup failure may leave only this uniquely named temporary file.
        try:
            temporary.unlink()
        except OSError:
            pass
        raise
    result = {'archive': str(archive), 'created_utc': datetime.now(timezone.utc).isoformat(),
              'bytes': archive_size, 'sha256': archive_hash,
              'entries': entries, 'skipped': skipped,
              'warning': 'Packaging validates only ZIP integrity, not transcription completeness.'}
    if final:
        result['final_readiness_bound'] = True
        result['warning'] = 'Final readiness inputs, protected membership and absence requirements match the archive.'
    try:
        temporary.unlink()
    except OSError as exc:
        # The verified final archive is already committed; a temporary-name
        # cleanup failure must not turn that successful publication into an
        # apparent packaging failure.
        result['temporary_cleanup_warning'] = f'{temporary}: {exc}'
    return result


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
    print(json.dumps(package(args.root, args.destination / name, args.dry_run,
                             final=args.final), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
