"""Verify returned attributes and unchanged archive bytes before receipt normalization."""
from pathlib import Path
import hashlib
import json
import os

root=Path(__file__).resolve().parents[1]
archive=root.parent/'LM4_SUCCESSOR_checkpoint_28.zip'
attrs=json.loads((root/'records/checkpoint28_xattrs.json').read_text())
for item in attrs:
    assert os.getxattr(archive,item['name']).decode()==item['value'],item['name']
verified=json.loads((root/'records/checkpoint28_archive_verification.json').read_text())
assert archive.stat().st_size==verified['bytes']
assert hashlib.sha256(archive.read_bytes()).hexdigest()==verified['sha256']
path=root/'records/checkpoint28_upload_result.json'
receipt=json.loads(path.read_text())
assert receipt['results'][0]['status']=='succeeded'
receipt['results'][0]['local_metadata_applied']=True
path.write_text(json.dumps(receipt,indent=2)+'\n')
print('PASS: every returned local attribute; unchanged archive size/SHA256; receipt normalized after verification.')
