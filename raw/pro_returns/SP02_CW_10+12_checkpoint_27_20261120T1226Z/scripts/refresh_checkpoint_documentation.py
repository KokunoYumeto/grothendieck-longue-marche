#!/usr/bin/env python3
"""Refresh exact copies of explicitly scoped root-authored support scripts.

Copies work/record*.py to documentation/root_scripts/ and
work/library_helpers/*.py to scripts/library_helpers/. Explicit audit helpers
and page-scoped audit support files go to documentation/root_audit_work/.
It does not inspect
readings, open images/context, collect witness splits, create an archive, or
upload anything. Existing destination copies are refreshed byte-for-byte;
unrelated and older destination files are retained.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

DEFAULT_OUTPUT = Path(__file__).resolve().parents[1]
DEFAULT_WORK = DEFAULT_OUTPUT.parent / 'work'
AUDIT_PAGE_NAME = re.compile(
    r'audit(?:10|12)_[0-9]{3}(?:_[A-Za-z0-9][A-Za-z0-9_-]*)?\.(?:json|py|md|txt)'
)


def scoped_sources(work: Path = DEFAULT_WORK) -> list[tuple[Path, Path]]:
    """Return validated sources with their output-relative destinations."""
    work = Path(work).resolve()
    groups = [
        (sorted(work.glob('record*.py')), Path('documentation/root_scripts')),
        (sorted((work / 'library_helpers').glob('*.py')), Path('scripts/library_helpers')),
    ]
    audit_sources = set(work.glob('make_audit_crops.py'))
    audit_sources.update(work.glob('record_audit*.json'))
    for pattern in ('audit10_*', 'audit12_*'):
        audit_sources.update(source for source in work.glob(pattern)
                             if AUDIT_PAGE_NAME.fullmatch(source.name))
    groups.append((sorted(audit_sources), Path('documentation/root_audit_work')))
    result = []
    for sources, destination_dir in groups:
        for source in sources:
            current = work
            for part in source.relative_to(work).parts:
                current = current / part
                if current.is_symlink():
                    raise ValueError(f'Refusing a symlink in the scoped copy set: {current}')
            if not source.is_file():
                raise ValueError(f'Refusing a non-file in the scoped copy set: {source}')
            if work not in source.resolve().parents:
                raise ValueError(f'Source is outside the supplied work folder: {source}')
            result.append((source, destination_dir / source.name))
    return result


def refresh(work: Path = DEFAULT_WORK, output: Path = DEFAULT_OUTPUT) -> dict:
    work, output = Path(work).resolve(), Path(output).resolve()
    copied = []
    for source, relative_target in scoped_sources(work):
        target = output
        for part in relative_target.parts:
            target = target / part
            if target.is_symlink():
                raise ValueError(f'Refusing a destination symlink: {target}')
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
        target_hash = hashlib.sha256(target.read_bytes()).hexdigest()
        if source_hash != target_hash:
            raise RuntimeError(f'Byte verification failed for {target}')
        copied.append({'source': str(source), 'destination': str(target),
                       'bytes': target.stat().st_size, 'sha256': target_hash})
    return {'copied_files': len(copied), 'files': copied,
            'note': 'Exact scoped support copies only. No image, witness/context collection, archive creation, or upload.'}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--work', type=Path, default=DEFAULT_WORK)
    ap.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    args = ap.parse_args()
    print(json.dumps(refresh(args.work, args.output), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
