#!/usr/bin/env python3
"""Record a successful single API upload and preserve returned file attributes."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
result = json.loads((root / 'notes/checkpoint16_upload_result.json').read_text())
timing = json.loads((root / 'notes/checkpoint16_upload_timing.json').read_text())
upload = result['structuredContent']
assert not result.get('isError') and upload['status'] == 'succeeded'
assert upload['operation'] == 'create_library_file'
assert upload['file_name'] == 'LM8_PUSH_checkpoint_16.zip'
verified = json.loads((root / 'notes/checkpoint16_archive_verification.out').read_text())
package = json.loads((root / 'notes/checkpoint16_package_result.json').read_text())
archive = Path(verified['archive'])
h = hashlib.sha256()
with archive.open('rb') as stream:
    for block in iter(lambda: stream.read(1 << 20), b''):
        h.update(block)
assert h.hexdigest() == verified['sha256'] == package['sha256']
assert archive.stat().st_size == verified['bytes'] == upload['file_size_bytes']
subprocess.run([sys.executable,
                str(root / 'code/library_upload_helpers_checkpoint14/library_file_transfer.py'),
                'apply-xattrs', str(archive), upload['library_file_id']],
               input=json.dumps(upload.get('xattrs', [])), text=True, check=True)
record = {
    'checkpoint': 16, 'path': str(archive), 'bytes': verified['bytes'],
    'sha256': verified['sha256'], 'captured_utc': package['captured_utc'],
    'scheduled_utc': '2026-11-16T02:00:00Z',
    'upload_started_utc': timing['upload_started_utc'],
    'saved_utc': timing['saved_utc'], 'file_id': upload['file_id'],
    'library_file_id': upload['library_file_id'],
    'current_version_number': upload['current_version_number'],
    'xattrs': upload.get('xattrs', []), 'all_returned_xattrs_applied': True,
    'archive_verification': 'notes/checkpoint16_archive_verification.out',
    'paper_pages': verified['paper_pages'], 'paper_statements': verified['paper_statements'], 'assessment': 'CONTINUE',
    'next_scheduled_checkpoint_utc': '2026-11-16T03:00:00Z',
    'upload_route': 'Single connected create-library-file API call; unavailable credential-file helper was not retried.',
}
(root / 'notes/checkpoint16_saved.json').write_text(json.dumps(record, indent=2) + '\n')
catalog_path = root / 'notes/checkpoint_saved_paths.json'
catalog = json.loads(catalog_path.read_text())
assert '16' not in catalog, 'Checkpoint16 already catalogued; do not repeat save.'
catalog['16'] = {k: record[k] for k in ('path', 'bytes', 'sha256', 'library_file_id', 'saved_utc')}
catalog_path.write_text(json.dumps(catalog, indent=2) + '\n')
print(json.dumps(record, indent=2))
