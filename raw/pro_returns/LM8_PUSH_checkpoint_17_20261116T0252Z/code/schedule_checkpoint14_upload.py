#!/usr/bin/env python3
"""Run the current Library prepared-upload helper at the authorized hourly time."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time

root = Path(__file__).resolve().parents[1]
archive = root.parent / 'LM8_PUSH_checkpoint_14.zip'
verification = json.loads((root / 'notes/checkpoint14_archive_verification.out').read_text())
assert verification['status'] == 'PASS'
assert archive.stat().st_size == verification['bytes']
assert hashlib.sha256(archive.read_bytes()).hexdigest() == verification['sha256']
deadline = datetime(2026, 11, 16, 0, 0, 0, tzinfo=timezone.utc)
while True:
    remaining = (deadline - datetime.now(timezone.utc)).total_seconds()
    if remaining <= 0:
        break
    time.sleep(min(20, remaining))
started = datetime.now(timezone.utc).isoformat()
request = {'uploads': [{'local_path': str(archive), 'purpose': 'create_library_file'}]}
helper = root / 'code/library_upload_helpers_checkpoint14/library_upload.py'
with (root / 'notes/checkpoint14_upload_prepared.out').open('w') as out, \
        (root / 'notes/checkpoint14_upload_prepared.err').open('w') as err:
    process = subprocess.run(['python3', str(helper)], input=json.dumps(request) + '\n',
                             text=True, stdout=out, stderr=err, cwd=root)
record = {'checkpoint': 14, 'route': 'current prepared-upload helper',
          'upload_started_utc': started,
          'helper_finished_utc': datetime.now(timezone.utc).isoformat(),
          'helper_exit_code': process.returncode,
          'archive': str(archive), 'archive_sha256': verification['sha256']}
(root / 'notes/checkpoint14_upload_prepared_attempt.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2), flush=True)
