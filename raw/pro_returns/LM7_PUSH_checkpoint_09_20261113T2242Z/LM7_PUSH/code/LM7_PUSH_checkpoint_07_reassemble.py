#!/usr/bin/env python3
"""Reassemble the exact immutable LM7_PUSH checkpoint 07 ZIP.

Save both .zip.001 and .zip.002 parts beside this script, then run:
    python LM7_PUSH_checkpoint_07_reassemble.py
The script never overwrites an existing archive.  It verifies every part,
the complete SHA-256 digest and every ZIP entry before reporting success.
"""
from pathlib import Path
from hashlib import sha256
import json
import zipfile

HERE = Path(__file__).resolve().parent
NAME = 'LM7_PUSH_checkpoint_07.zip'
EXPECTED = '5f6d77e47dd8a29eddae51a18214927fdb917ce02af244d2d0e8740af590d3c8'
SIZE = 894790136


def main():
    target = HERE / NAME
    if target.exists():
        raise SystemExit('The archive already exists; it has not been overwritten.')
    parts = [HERE / (NAME + '.001'), HERE / (NAME + '.002')]
    if not all(p.is_file() for p in parts):
        raise SystemExit('Save both numbered parts beside this script before running it.')
    total = sum(p.stat().st_size for p in parts)
    if total != SIZE:
        raise SystemExit('Part sizes do not match the verified archive; no output was created.')
    digest = sha256()
    for part in parts:
        with part.open('rb') as stream:
            while block := stream.read(8 * 1024 * 1024):
                digest.update(block)
    if digest.hexdigest() != EXPECTED:
        raise SystemExit('The parts failed the SHA-256 check; no output was created.')
    with target.open('xb') as output:
        for part in parts:
            with part.open('rb') as stream:
                while block := stream.read(8 * 1024 * 1024):
                    output.write(block)
    with zipfile.ZipFile(target) as archive:
        bad = archive.testzip()
        if bad is not None:
            raise SystemExit('ZIP verification failed at ' + bad)
        count = len(archive.namelist())
    if count != 5179:
        raise SystemExit('Unexpected ZIP entry count.')
    print(json.dumps({'archive': str(target), 'size_bytes': SIZE,
                      'sha256': EXPECTED, 'all_zip_entries_verified': count}, indent=2))


if __name__ == '__main__':
    main()
