#!/usr/bin/env python3
"""Create immutable delivery parts of the verified checkpoint 08 archive."""
from pathlib import Path
from hashlib import sha256
import json

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT.parent
validation = json.loads((WORK / 'LM7_PUSH_checkpoint_08_validation.json').read_text())
archive = Path(validation['archive'])
assert archive.stat().st_size == validation['size_bytes']
limit = 448 * 1024 * 1024
parts = []
joined = sha256()
with archive.open('rb') as source:
    index = 1
    remaining = validation['size_bytes']
    while remaining:
        amount = min(limit, remaining)
        path = WORK / (archive.name + f'.{index:03d}')
        part_hash = sha256()
        with path.open('xb') as out:
            left = amount
            while left:
                block = source.read(min(8 * 1024 * 1024, left))
                assert block
                out.write(block)
                part_hash.update(block)
                joined.update(block)
                left -= len(block)
        parts.append({'file_name': path.name, 'file_size_bytes': amount,
                      'workspace_path': str(path), 'sha256': part_hash.hexdigest()})
        remaining -= amount
        index += 1
    assert source.read(1) == b''
assert joined.hexdigest() == validation['sha256']
assert len(parts) == 5
record = {'archive_name': archive.name, 'archive_size': validation['size_bytes'],
          'archive_sha256': validation['sha256'], 'archive_entries': validation['files'],
          'parts': parts, 'joined_parts_hash_matches_original': True,
          'single_file_limit_bytes': 512 * 1024 * 1024}
manifest = ROOT / 'research/checkpoint08_delivery_parts.json'
assert not manifest.exists()
manifest.write_text(json.dumps(record, indent=2) + '\n')
script = '''#!/usr/bin/env python3
"""Reassemble the exact immutable LM7_PUSH checkpoint 08 ZIP.

Save all five numbered parts beside this file and run:
    python LM7_PUSH_checkpoint_08_reassemble.py
Every part and the complete ZIP are checked. Existing output is preserved.
"""
from pathlib import Path
from hashlib import sha256
import json
import zipfile

HERE = Path(__file__).resolve().parent
MANIFEST = ''' + repr(record) + '''

def blocks(path):
    with path.open('rb') as stream:
        while block := stream.read(8 * 1024 * 1024):
            yield block

def main():
    target = HERE / MANIFEST['archive_name']
    if target.exists():
        raise SystemExit('The archive already exists and has not been overwritten.')
    joined = sha256()
    for item in MANIFEST['parts']:
        part = HERE / item['file_name']
        if not part.is_file() or part.stat().st_size != item['file_size_bytes']:
            raise SystemExit('Missing or wrong-sized part: ' + part.name)
        digest = sha256()
        for block in blocks(part):
            digest.update(block)
            joined.update(block)
        if digest.hexdigest() != item['sha256']:
            raise SystemExit('SHA-256 mismatch in ' + part.name + '; no output created.')
    if joined.hexdigest() != MANIFEST['archive_sha256']:
        raise SystemExit('Complete SHA-256 mismatch; no output created.')
    with target.open('xb') as output:
        for item in MANIFEST['parts']:
            for block in blocks(HERE / item['file_name']):
                output.write(block)
    if target.stat().st_size != MANIFEST['archive_size']:
        raise SystemExit('Output size mismatch.')
    with zipfile.ZipFile(target) as archive:
        bad = archive.testzip()
        if bad is not None:
            raise SystemExit('ZIP verification failed at ' + bad)
        count = len(archive.namelist())
    if count != MANIFEST['archive_entries']:
        raise SystemExit('Unexpected ZIP entry count.')
    print(json.dumps({'archive': str(target), 'size_bytes': target.stat().st_size,
                      'sha256': MANIFEST['archive_sha256'],
                      'all_zip_entries_verified': count}, indent=2))

if __name__ == '__main__':
    main()
'''
target = WORK / 'LM7_PUSH_checkpoint_08_reassemble.py'
assert not target.exists()
target.write_text(script)
(ROOT / 'code' / target.name).write_text(script)
record['reassembly_script'] = str(target)
print(json.dumps(record, indent=2))
