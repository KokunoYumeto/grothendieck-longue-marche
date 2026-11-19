#!/usr/bin/env python3
"""Refresh exact copies of explicitly scoped root-authored support scripts.

Copies only work/record*.py to documentation/root_scripts/ and
work/library_helpers/*.py to scripts/library_helpers/. It does not inspect
readings, open images/context, collect witness splits, create an archive, or
upload anything. Existing destination copies are refreshed byte-for-byte;
unrelated and older destination files are retained.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

DEFAULT_OUTPUT = Path(__file__).resolve().parents[1]
DEFAULT_WORK = DEFAULT_OUTPUT.parent / 'work'


def refresh(work: Path = DEFAULT_WORK, output: Path = DEFAULT_OUTPUT) -> dict:
    work, output = Path(work).resolve(), Path(output).resolve()
    groups = [
        (work, 'record*.py', output / 'documentation' / 'root_scripts'),
        (work / 'library_helpers', '*.py', output / 'scripts' / 'library_helpers'),
    ]
    copied = []
    for source_dir, pattern, destination_dir in groups:
        for source in sorted(source_dir.glob(pattern)):
            if source.is_symlink() or not source.is_file():
                raise ValueError(f'Refusing a symlink or non-file in the scoped copy set: {source}')
            if work not in source.resolve().parents:
                raise ValueError(f'Source is outside the supplied work folder: {source}')
            destination_dir.mkdir(parents=True, exist_ok=True)
            target = destination_dir / source.name
            if target.is_symlink():
                raise ValueError(f'Refusing to overwrite a destination symlink: {target}')
            shutil.copyfile(source, target)
            source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
            target_hash = hashlib.sha256(target.read_bytes()).hexdigest()
            if source_hash != target_hash:
                raise RuntimeError(f'Byte verification failed for {target}')
            copied.append({'source': str(source), 'destination': str(target),
                           'bytes': target.stat().st_size, 'sha256': target_hash})
    return {'copied_files': len(copied), 'files': copied,
            'note': 'Exact scoped script copies only. No image, witness/context collection, archive creation, or upload.'}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--work', type=Path, default=DEFAULT_WORK)
    ap.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    args = ap.parse_args()
    print(json.dumps(refresh(args.work, args.output), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
