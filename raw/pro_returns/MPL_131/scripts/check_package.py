#!/usr/bin/env python3
"""Read-only package and hash preflight; does not create ZIPs or alter logs.

Usage:
  python scripts/check_package.py
  python scripts/check_package.py --hashes
  python scripts/check_package.py --archive /absolute/path/MPL_131.zip

--hashes prints validator-compatible SHA-256 records for the 38 page fragments
and the combined transcription. The caller controls when these records are
appended to progress.log and when the freeze marker is written.

--archive compares an existing ZIP with the complete current work tree,
excluding Python bytecode/cache directories. Archive paths must be relative to
the work root, without an enclosing directory. Run comparison immediately after
creating an archive, before further work changes its inputs.
"""
from __future__ import annotations

import argparse
import hashlib
import sys
import zipfile
from pathlib import Path, PurePosixPath

SCANS = [n for n in range(2, 43) if n not in {11, 19, 22}]
REQUIRED = ['MPL_131_transcription.tex', 'MPL_131_doubts.md',
            'MPL_131_inventory.csv', 'MPL_131_notes.md', 'progress.log']


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path,
                        default=Path(__file__).resolve().parents[1])
    parser.add_argument('--hashes', action='store_true')
    parser.add_argument('--archive', type=Path)
    parser.add_argument('--final', action='store_true',
                        help='require every final deliverable, including notes')
    args = parser.parse_args()
    root = args.root.resolve()
    errors = []
    files = {}
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root)
        if '__pycache__' in relative.parts or path.suffix in {'.pyc', '.pyo'}:
            continue
        if path.is_symlink():
            errors.append(f'Symlink requires explicit review before packaging: {relative}')
        elif path.is_file():
            name = relative.as_posix()
            files[name] = path
            if path.suffix.lower() in {'.jpg', '.jpeg', '.png', '.pdf', '.zip'}:
                errors.append(f'Unexpected image/source/archive in work tree: {name}')

    page_names = [f'pages/MPL_131_131_scan{scan:03d}.tex' for scan in SCANS]
    transcription_names = page_names + ['MPL_131_transcription.tex']
    if args.hashes or args.final:
        for name in transcription_names:
            if name not in files:
                errors.append(f'Missing transcription file: {name}')
    if args.final:
        for name in REQUIRED:
            if name not in files:
                errors.append(f'Missing final deliverable: {name}')

    if args.hashes and not errors:
        for name in transcription_names:
            print(f'sha256 {digest(files[name].read_bytes())} {name}')

    if args.archive:
        try:
            with zipfile.ZipFile(args.archive) as archive:
                entries = [item for item in archive.infolist() if not item.is_dir()]
                names = [item.filename for item in entries]
                if len(names) != len(set(names)):
                    errors.append('ZIP contains duplicate file paths')
                for name in names:
                    path = PurePosixPath(name)
                    if path.is_absolute() or '..' in path.parts or '\\' in name:
                        errors.append(f'Unsafe ZIP path: {name}')
                for name in sorted(files.keys() - set(names)):
                    errors.append(f'Missing from ZIP: {name}')
                for name in sorted(set(names) - files.keys()):
                    errors.append(f'Unexpected ZIP entry: {name}')
                for name in sorted(files.keys() & set(names)):
                    if digest(files[name].read_bytes()) != digest(archive.read(name)):
                        errors.append(f'ZIP content differs from work tree: {name}')
                bad = archive.testzip()
                if bad:
                    errors.append(f'ZIP CRC failure: {bad}')
        except (OSError, zipfile.BadZipFile) as exc:
            errors.append(f'Cannot inspect ZIP: {exc}')

    for error in errors:
        print('ERROR:', error, file=sys.stderr)
    if not args.hashes:
        print(f'Work-tree files eligible for packaging: {len(files)}; '
              f'total bytes: {sum(p.stat().st_size for p in files.values())}; '
              f'errors: {len(errors)}.')
        if args.archive and not errors:
            print('ZIP entries and file hashes match the complete eligible work tree.')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
