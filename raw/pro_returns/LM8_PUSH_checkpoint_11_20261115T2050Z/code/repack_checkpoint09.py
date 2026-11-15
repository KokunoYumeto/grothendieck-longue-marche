#!/usr/bin/env python3
"""Repackage the immutable 19:00 snapshot below the upload limit.

No source checkpoint is overwritten. Raw JSONL is losslessly XZ-compressed.
Gzip proof payloads are losslessly transcoded, with compression-wrapper changes
accounted for explicitly. Interrupted wrappers are superseded only where their
complete and partial decoded records are already retained and hash-identified.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import gzip
import hashlib
import json
import lzma
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / 'LM8_PUSH_checkpoint_09.zip'
OUTDIR = ROOT.parent / 'checkpoint09_compact'
OUTDIR.mkdir(exist_ok=True)
DEST = OUTDIR / SOURCE.name
CACHE = OUTDIR / 'compressed_logs'
CACHE.mkdir(exist_ok=True)
LIMIT = 536870912
CHUNK = 1024 * 1024
FILTERS = [{'id': lzma.FILTER_LZMA2, 'preset': 3, 'dict_size': 64 * 1024 * 1024}]

def digest_file(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(CHUNK), b''):
            h.update(chunk)
    return h.hexdigest()

if DEST.exists():
    raise SystemExit('Refusing to overwrite compact checkpoint ' + str(DEST))
with zipfile.ZipFile(SOURCE) as z:
    old_manifest = json.loads(z.read('PACKAGE_MANIFEST.json'))
    originals = {e['path']: e for e in old_manifest['files']}
    names = z.namelist()
    jobs = [i.filename for i in z.infolist()
            if i.file_size >= 10_000_000 and
            (i.filename.endswith('.jsonl') or i.filename.endswith('.jsonl.gz'))]
    wrappers = [i.filename for i in z.infolist()
                if i.file_size >= 10_000_000 and i.filename.endswith('.gz.incomplete_stream')]
    wrapper_maps = []
    for name in wrappers:
        valid = name.removesuffix('.incomplete_stream')
        record = json.loads(z.read(valid + '.archive.json'))
        partial = valid + '.partial_record'
        assert record['raw_compressed_sha256'] == originals[name]['sha256']
        assert partial in names and valid in jobs
        assert hashlib.sha256(z.read(partial)).hexdigest() == record['partial_record_sha256']
        wrapper_maps.append({
            'original_path': name,
            'original_bytes': originals[name]['bytes'],
            'original_sha256': originals[name]['sha256'],
            'superseded_by_payload_from': valid,
            'complete_payload_bytes': record['decoded_complete_record_bytes'],
            'complete_payload_sha256': record['complete_record_sha256'],
            'partial_record_path': partial,
            'partial_record_sha256': record['partial_record_sha256'],
            'reason': 'Interrupted gzip serialization superseded by the complete decoded records and separately retained partial record; original compression bytes remain in the unchanged oversized local checkpoint, not this compact package.',
        })

def compress_one(name):
    dest_name = name + ('.payload.xz' if name.endswith('.gz') else '.xz')
    path = CACHE / dest_name
    path.parent.mkdir(parents=True, exist_ok=True)
    ledger = path.with_suffix(path.suffix + '.json')
    if path.exists() and ledger.exists():
        result = json.loads(ledger.read_text())
        assert result['original_sha256'] == originals[name]['sha256']
        assert result['xz_sha256'] == digest_file(path)
        return result
    h = hashlib.sha256()
    count = 0
    with zipfile.ZipFile(SOURCE) as z, z.open(name) as raw:
        reader = gzip.GzipFile(fileobj=raw) if name.endswith('.gz') else raw
        with lzma.LZMAFile(path, 'wb', filters=FILTERS) as out:
            for chunk in iter(lambda: reader.read(CHUNK), b''):
                h.update(chunk)
                count += len(chunk)
                out.write(chunk)
        if reader is not raw:
            reader.close()
    # Independently read the new stream back; compare every decoded byte's hash.
    check = hashlib.sha256()
    check_count = 0
    with lzma.open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(CHUNK), b''):
            check.update(chunk)
            check_count += len(chunk)
    assert check.hexdigest() == h.hexdigest() and check_count == count
    if not name.endswith('.gz'):
        assert h.hexdigest() == originals[name]['sha256']
    for entry in wrapper_maps:
        if entry['superseded_by_payload_from'] == name:
            assert count == entry['complete_payload_bytes']
            assert h.hexdigest() == entry['complete_payload_sha256']
    result = {
        'original_path': name,
        'original_bytes': originals[name]['bytes'],
        'original_sha256': originals[name]['sha256'],
        'stored_path': dest_name,
        'decoded_bytes': count,
        'decoded_sha256': h.hexdigest(),
        'xz_bytes': path.stat().st_size,
        'xz_sha256': digest_file(path),
        'kind': 'gzip_payload' if name.endswith('.gz') else 'raw_bytes',
        'restoration': 'Exact decoded proof bytes; recreated gzip wrapper need not have the original wrapper hash.' if name.endswith('.gz') else 'Exact original file bytes.',
    }
    ledger.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'compressed': name, 'decoded_bytes': count, 'xz_bytes': result['xz_bytes']}), flush=True)
    return result

print(json.dumps({'source': str(SOURCE), 'large_logs': len(jobs), 'superseded_wrappers': len(wrappers)}), flush=True)
with ThreadPoolExecutor(max_workers=4) as pool:
    pending = [pool.submit(compress_one, name) for name in jobs]
    transforms = [f.result() for f in as_completed(pending)]
transforms.sort(key=lambda x: x['original_path'])

compression_map = {
    'checkpoint': '09',
    'scheduled_utc': '2026-11-15T19:00:00Z',
    'kind': 'Upload-limit recovery of the SAME frozen checkpoint, not an additional work snapshot',
    'original_zip_sha256': 'e594317a692df7d6aa88cfa0f58ebc551a8c7ebf70e153854e37da52ef8f4ada',
    'original_zip_bytes': 1676331231,
    'upload_limit_bytes': LIMIT,
    'transforms': transforms,
    'superseded_compression_wrappers': wrapper_maps,
    'all_complete_and_partial_proof_records_retained': True,
    'mathematical_sources_and_pdf_unchanged': True,
    'paper_pages': 392,
    'paper_statements': 241,
}

RESTORE = '''#!/usr/bin/env python3
"""Restore compressed log payloads; existing files are never overwritten."""
from pathlib import Path
import argparse,gzip,hashlib,json,lzma
p=argparse.ArgumentParser();p.add_argument('--destination',type=Path);a=p.parse_args()
base=Path(__file__).resolve().parent;dest=a.destination or base
mapping=json.loads((base/'CHECKPOINT_COMPRESSION_MAP.json').read_text())
for e in mapping['transforms']:
    target=dest/e['original_path'];target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists():
        print('EXISTS, unchanged:',target);continue
    h=hashlib.sha256();count=0
    with lzma.open(base/e['stored_path'],'rb') as inp, target.open('xb') as raw:
        out=gzip.GzipFile(filename='',mode='wb',fileobj=raw,compresslevel=1,mtime=0) if e['kind']=='gzip_payload' else raw
        while True:
            b=inp.read(1024*1024)
            if not b:break
            h.update(b);count+=len(b);out.write(b)
        if out is not raw:out.close()
    assert h.hexdigest()==e['decoded_sha256'] and count==e['decoded_bytes']
    print('RESTORED verified payload:',target)
print('Interrupted compression wrappers are superseded; their complete and partial decoded records remain in the listed files. See CHECKPOINT_COMPRESSION_MAP.json.')
'''

NOTE = '''# Checkpoint09 upload-limit recovery

The scheduled19:00UTC snapshot was captured once, packaged as the original
LM8_PUSH_checkpoint_09.zip, and passed the full ZIP CRC check. Its1,676,331,231
bytes exceeded the536,870,912-byte upload limit, so that upload was rejected.
The original archive remains unchanged. This compact package is a repackaging
of that SAME frozen snapshot; it is not a later or additional research checkpoint.

The392-page PDF,241-statement register, source files, proofs, audits, code,
and ordinary records are byte-for-byte unchanged. Large raw JSONL files are
stored as XZ streams; their exact original bytes were hashed, compressed,
decompressed again, and verified. Large gzip proof logs are stored as XZ of
their exact decoded contents, also fully verified. Compression wrappers are
serialization only: recreating a gzip stream preserves every proof record but
need not preserve its old gzip header or deflate bytes. Original hashes remain
recorded. Interrupted large gzip wrappers are superseded by their valid complete
record payload and separately retained partial record; the mapping lists both.
No complete or partial mathematical computation record is discarded.

CHECKPOINT_COMPRESSION_MAP.json lists every conversion and superseded wrapper,
with original and decoded hashes. ORIGINAL_PACKAGE_MANIFEST.json describes
the original frozen snapshot. PACKAGE_MANIFEST.json describes this actual
compact archive. RESTORE_LARGE_LOGS.py restores each compressed log at its
original path, verifies its decoded hash, and refuses to overwrite existing files.
All computations marked incomplete remain incomplete.

The failed oversized container is superseded by this compact checkpoint for
future checkpoint_history. The work inside it is retained here as specified
above; retaining redundant compression-wrapper bytes would exceed the upload
limit without preserving additional proof content. This is the explicit
accounting for that omitted intermediate container and its serialization files.
'''

entries = []
skip = set(jobs) | set(wrappers) | {'PACKAGE_MANIFEST.json'}
with zipfile.ZipFile(SOURCE) as old, zipfile.ZipFile(DEST, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    def add(name, data, compression=zipfile.ZIP_DEFLATED):
        z.writestr(name, data, compress_type=compression)
        entries.append({'path': name, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
    for name in old.namelist():
        if name in skip:
            continue
        data = old.read(name)
        if name == 'LM8_PUSH_report.md':
            data += ('\n\n' + NOTE).encode()
        add(name, data)
    for e in transforms:
        path = CACHE / e['stored_path']
        z.write(path, e['stored_path'], compress_type=zipfile.ZIP_STORED)
        entries.append({'path': e['stored_path'], 'bytes': e['xz_bytes'], 'sha256': e['xz_sha256']})
    add('ORIGINAL_PACKAGE_MANIFEST.json', json.dumps(old_manifest, indent=2).encode() + b'\n')
    add('CHECKPOINT_COMPRESSION_MAP.json', json.dumps(compression_map, indent=2).encode() + b'\n')
    add('RESTORE_LARGE_LOGS.py', RESTORE.encode())
    add('notes/checkpoint09_upload_recovery.md', NOTE.encode())
    add('code/repack_checkpoint09.py', Path(__file__).read_bytes())
    if (ROOT/'notes/pbc_checkpoint09_compression_audit.md').exists():
        add('notes/pbc_checkpoint09_compression_audit.md', (ROOT/'notes/pbc_checkpoint09_compression_audit.md').read_bytes())
    final_manifest = {'created_utc': datetime.now(timezone.utc).isoformat(),
                      'kind': 'checkpoint09 upload-limit recovery', 'files': entries,
                      'file_count': len(entries), 'compression_map': 'CHECKPOINT_COMPRESSION_MAP.json'}
    z.writestr('PACKAGE_MANIFEST.json', json.dumps(final_manifest, indent=2) + '\n')
with zipfile.ZipFile(DEST) as z:
    bad = z.testzip()
    assert bad is None, bad
result = {'file': str(DEST), 'bytes': DEST.stat().st_size, 'sha256': digest_file(DEST),
          'files': len(entries), 'below_upload_limit': DEST.stat().st_size <= LIMIT}
(OUTDIR/'repack_result.json').write_text(json.dumps(result, indent=2) + '\n')
(ROOT/'notes/checkpoint09_upload_recovery.md').write_text(NOTE)
(ROOT/'notes/checkpoint09_compression_map.json').write_text(json.dumps(compression_map, indent=2) + '\n')
print(json.dumps(result, indent=2), flush=True)
assert result['below_upload_limit'], 'Repacked archive still exceeds upload limit; retain it and improve a separate packaging candidate.'
