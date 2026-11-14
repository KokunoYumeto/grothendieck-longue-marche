#!/usr/bin/env python3
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
MANIFEST = {'archive_name': 'LM7_PUSH_checkpoint_08.zip', 'archive_size': 2102127751, 'archive_sha256': 'e0eae671f7e4ac43039abc9d300c2fd68ffabaca7f13a02b992e1d2f4675b057', 'archive_entries': 10016, 'parts': [{'file_name': 'LM7_PUSH_checkpoint_08.zip.001', 'file_size_bytes': 469762048, 'workspace_path': '/workspace/scratch/2a103c25eb9b/LM7_PUSH_checkpoint_08.zip.001', 'sha256': 'e1a2f45b611c8164f0d5d54f488a59fb77bf72466d4b27debffb1ac276b9e502'}, {'file_name': 'LM7_PUSH_checkpoint_08.zip.002', 'file_size_bytes': 469762048, 'workspace_path': '/workspace/scratch/2a103c25eb9b/LM7_PUSH_checkpoint_08.zip.002', 'sha256': '8f6d258f7ff7aeca39b515d9ee2738594f5e6e7181ff0a36746b48ba9d736ede'}, {'file_name': 'LM7_PUSH_checkpoint_08.zip.003', 'file_size_bytes': 469762048, 'workspace_path': '/workspace/scratch/2a103c25eb9b/LM7_PUSH_checkpoint_08.zip.003', 'sha256': '6def45b0a2d28fbaafdffe2a3d32f3c1e764351cfdd562441190d0aa4c1cb0d1'}, {'file_name': 'LM7_PUSH_checkpoint_08.zip.004', 'file_size_bytes': 469762048, 'workspace_path': '/workspace/scratch/2a103c25eb9b/LM7_PUSH_checkpoint_08.zip.004', 'sha256': '9cdebef8c8fe36720604b831660ed50cadcab2468f994421909178012702b4d4'}, {'file_name': 'LM7_PUSH_checkpoint_08.zip.005', 'file_size_bytes': 223079559, 'workspace_path': '/workspace/scratch/2a103c25eb9b/LM7_PUSH_checkpoint_08.zip.005', 'sha256': '13a28a4818077611e9114f2706b0acfb418fb91a8b6f46e5f53d8db904476454'}], 'joined_parts_hash_matches_original': True, 'single_file_limit_bytes': 536870912}

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
