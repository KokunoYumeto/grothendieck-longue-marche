"""Verify saved attributes and immutable bytes before normalizing one receipt.

Run only after capture, independent archive verification and saving.
"""
from pathlib import Path
import hashlib
import json
import os


def main():
    root = Path(__file__).resolve().parents[1]
    archive = root.parent / 'LM4_SUCCESSOR_checkpoint_30.zip'
    attrs = json.loads((root / 'records/checkpoint30_xattrs.json').read_text())
    assert attrs, 'Returned identity attributes must be present.'
    for item in attrs:
        assert os.getxattr(archive, item['name']).decode() == item['value'], item['name']
    verified = json.loads((root / 'records/checkpoint30_archive_verification.json').read_text())
    assert verified['archive'] == archive.name
    assert archive.stat().st_size == verified['bytes'] <= 536870912
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == verified['sha256']
    path = root / 'records/checkpoint30_upload_result.json'
    receipt = json.loads(path.read_text())
    assert len(receipt['results']) == 1
    result = receipt['results'][0]
    assert result['status'] == 'succeeded' and result['file_name'] == archive.name
    result['local_metadata_applied'] = True
    path.write_text(json.dumps(receipt, indent=2) + '\n')
    print('PASS: every returned local attribute; unchanged archive size/SHA256; '
          'single receipt normalized only after verification.')


if __name__ == '__main__':
    main()
