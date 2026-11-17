"""Losslessly re-encode the captured checkpoint, retaining the original ZIP.

The native file limit is 512 MiB. This is the same nineteenth snapshot,
not an additional checkpoint: every entry name and uncompressed byte is
verified against the already captured immutable archive. Earlier ZIPs
and the original checkpoint19 container remain untouched.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil
import zipfile

root = Path(__file__).resolve().parents[1]
original = root.parent/'LM4_SUCCESSOR_checkpoint_19.zip'
target = root.parent/'checkpoint19_delivery'/'LM4_SUCCESSOR_checkpoint_19.zip'
assert not target.exists()
target.parent.mkdir(exist_ok=True)
original_hash = hashlib.sha256(original.read_bytes()).hexdigest()
assert original_hash == '7f9f65bd019248784f05771a41d957ce5dd896911556e507979ca962c9434508'
shutil.copyfile(root/'records/checkpoint19_archive_verification.json',
                root/'records/checkpoint19_raw_archive_verification.json')
text_extensions = {'.json','.csv','.tsv','.md','.tex','.log','.py','.txt',
                   '.smt2','.out','.bib','.lua','.fragment','.stdout',
                   '.html','.cpp','.err','.in','.stderr','.empty'}
count = changed_methods = 0
started = datetime.now(timezone.utc).isoformat()
with zipfile.ZipFile(original) as source, zipfile.ZipFile(target,'x') as destination:
    destination.comment = source.comment
    for info in source.infolist():
        data = source.read(info.filename)
        newinfo = zipfile.ZipInfo(info.filename, info.date_time)
        for attr in ('comment','extra','create_system','create_version',
                     'extract_version','internal_attr','external_attr'):
            setattr(newinfo, attr, getattr(info,attr))
        method = zipfile.ZIP_LZMA if Path(info.filename).suffix in text_extensions else info.compress_type
        changed_methods += method != info.compress_type
        destination.writestr(newinfo,data,compress_type=method,compresslevel=6)
        count += 1
        if count % 500 == 0:
            print('Encoded entries:', count, flush=True)
assert hashlib.sha256(original.read_bytes()).hexdigest() == original_hash
with zipfile.ZipFile(original) as source, zipfile.ZipFile(target) as destination:
    assert source.namelist() == destination.namelist()
    assert destination.testzip() is None
    for info in source.infolist():
        assert source.read(info.filename) == destination.read(info.filename), info.filename
record = {
    'scope':'Same checkpoint19 snapshot, lossless ZIP encoding for the 512 MiB native file limit; original archive retained unchanged.',
    'started_at':started,'completed_at':datetime.now(timezone.utc).isoformat(),
    'original_path':str(original),'original_bytes':original.stat().st_size,
    'original_sha256':original_hash,'delivery_path':str(target),
    'delivery_bytes':target.stat().st_size,
    'delivery_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
    'entries':count,'method_changes':changed_methods,
    'original_unchanged':'PASS','entry_names_order_and_every_byte':'PASS',
    'delivery_crc':'PASS','native_limit_bytes':536870912,
    'fits_native_limit':target.stat().st_size<=536870912,
    'method':'ZIP LZMA (method14) for text; original method for binary artifacts.'}
(root/'records/checkpoint19_delivery_encoding.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2),flush=True)
assert record['fits_native_limit'], 'Exact same snapshot still exceeds the native limit.'
