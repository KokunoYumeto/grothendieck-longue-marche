#!/usr/bin/env python3
"""Package only this deliverable directory, with an internal SHA-256 manifest."""
import datetime
import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT.parent / 'MPL_91_059-098.zip'
MANIFEST = ROOT / 'records/package_manifest.json'

files = sorted(p for p in ROOT.rglob('*')
               if p.is_file() and '__pycache__' not in p.parts and p != MANIFEST)
assert not any(p.suffix.lower() in {'.zip', '.jpg', '.jpeg', '.png', '.pdf'} for p in files)
entries = {p.relative_to(ROOT).as_posix(): {
    'bytes': p.stat().st_size,
    'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
} for p in files}
MANIFEST.write_text(json.dumps({
    'time_utc': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    'scope': 'Every packaged file except this manifest itself.',
    'files': entries,
}, indent=2) + '\n')
files.append(MANIFEST)
with zipfile.ZipFile(OUTPUT, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for path in sorted(files):
        archive.write(path, path.relative_to(ROOT).as_posix())
with zipfile.ZipFile(OUTPUT) as archive:
    assert archive.testzip() is None
    assert len(archive.namelist()) == len(files)
    for name, entry in entries.items():
        data = archive.read(name)
        assert len(data) == entry['bytes']
        assert hashlib.sha256(data).hexdigest() == entry['sha256']
    frozen = json.loads(archive.read('records/frozen_sha256.json'))
    for name, digest in frozen.items():
        assert hashlib.sha256(archive.read(name)).hexdigest() == digest
print(json.dumps({
    'path': str(OUTPUT),
    'file_count': len(files),
    'bytes': OUTPUT.stat().st_size,
    'sha256': hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
    'zip_crc_and_manifest': 'passed',
    'all_39_frozen_hashes_in_archive': 'unchanged',
}, indent=2))
