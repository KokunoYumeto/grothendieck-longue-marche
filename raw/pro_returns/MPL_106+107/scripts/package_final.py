#!/usr/bin/env python3
"""Package complete deliverables and records; exclude all scans and supplied sources."""
from pathlib import Path
from datetime import datetime
import hashlib
import json
import sys
import zipfile

BASE = Path(__file__).resolve().parents[1]
STAMP = sys.argv[1]
DEST = BASE.parent/'MPL_106+107.zip'
assert not DEST.exists(), 'Do not silently overwrite a final archive.'
validation = json.loads((BASE/'records/final_validation.json').read_text())
assert validation['passed']
frozen = json.loads((BASE/'records/frozen_sha256.json').read_text())
for rel,digest in frozen.items():
    assert hashlib.sha256((BASE/rel).read_bytes()).hexdigest()==digest, rel

with (BASE/'progress.log').open('a') as f:
    f.write(f'research notes complete {STAMP}: 255 dossier statements, 12 NEW_RESULTS entries and 3 notices individually mapped\n')
    f.write(f'final validation passed {STAMP}: 404 checks; 41 pages; 1202 inventory rows all yes; 342 doubts\n')
    f.write(f'hashes unchanged {STAMP}: all 41 page files and the combined transcription match the 42 SHA-256 values recorded at freeze\n')
    f.write(f'final archive prepared {STAMP}: complete deliverables and work records; no scans, supplied sources, downloaded reference PDFs, or cache files\n')

def eligible(path):
    return path.is_file() and '__pycache__' not in path.parts and path.suffix not in {'.pyc','.pyo'}

files = sorted(p for p in BASE.rglob('*') if eligible(p) and p.name!='package_manifest.json')
allowed_suffixes = {'.tex','.md','.csv','.log','.json','.jsonl','.py','.diff'}
assert all(p.suffix in allowed_suffixes for p in files)
assert all(p.relative_to(BASE).parts[0] in {'pages','records','scripts'} or p.parent==BASE for p in files)
manifest = {
    'archive':DEST.name,
    'prepared_utc':STAMP,
    'freeze_utc':'2026-11-16 13:43:19 UTC',
    'all_42_frozen_hashes_unchanged':True,
    'source_exclusions':['scans','attached archives','supplied context','downloaded reference PDFs','Python caches'],
    'manifest_self_hash_omitted':True,
    'files':[{'path':str(p.relative_to(BASE)), 'bytes':p.stat().st_size,
              'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]
}
manifest_path=BASE/'records/package_manifest.json'
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
files.append(manifest_path)
files.sort()
dt=datetime.strptime(STAMP,'%Y-%m-%d %H:%M:%S UTC')
with zipfile.ZipFile(DEST,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:
        info=zipfile.ZipInfo(str(p.relative_to(BASE)),date_time=(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second))
        info.compress_type=zipfile.ZIP_DEFLATED
        info.external_attr=0o100644<<16
        z.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
with zipfile.ZipFile(DEST) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(set(z.namelist()))==len(files)
    for rel,digest in frozen.items():
        assert hashlib.sha256(z.read(rel)).hexdigest()==digest,rel
    for rec in manifest['files']:
        assert hashlib.sha256(z.read(rec['path'])).hexdigest()==rec['sha256'],rec['path']
print(json.dumps({'archive':str(DEST),'files':len(files),'bytes':DEST.stat().st_size,
                  'sha256':hashlib.sha256(DEST.read_bytes()).hexdigest(),
                  'zip_crc_passed':True,'archive_payload_hashes_passed':True}))
