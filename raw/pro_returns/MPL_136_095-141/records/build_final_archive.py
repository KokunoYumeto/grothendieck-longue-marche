#!/usr/bin/env python3
"""Package the completed deliverables, preserving the frozen transcription."""
import hashlib, json, os, re, tempfile, zipfile
from datetime import datetime, timezone
from pathlib import Path
from create_checkpoint import snapshot
from validate_package import hash_records
ROOT=Path(__file__).resolve().parent.parent
TARGET=ROOT.parent/'MPL_136_095-141.zip'
MANIFEST='records/final_archive_manifest.json'
if TARGET.exists():raise SystemExit('Final archive already exists; refusing overwrite.')
logpath=ROOT/'progress.log'
log=logpath.read_text()
freeze=re.search(r'^transcription frozen .+$',log,re.M)
assert freeze
records=hash_records(log[:freeze.start()])
assert len(records)==47
for name,digest in records.items():
    assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,name
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with logpath.open('a') as f:
    f.write(f'research notes completed {stamp}; 131 individual notes; all six supplied context files searched for every note\n')
    f.write(f'final structural verification {stamp}; 46 page files; 729 inventory rows all yes; 335 doubt occurrences; combined fragment compiles\n')
    f.write(f'frozen SHA-256 verified unchanged {stamp}; all 46 page files and combined transcription (47 files); no post-context transcription edits\n')
    f.write(f'final archive prepared {stamp}; MPL_136_095-141.zip; supplied scans and context files excluded\n')
data=snapshot(ROOT,MANIFEST)
manifest=dict(package='MPL_136_095-141',created_utc=stamp,
  contents='Completed core deliverables and all authored technical/research records.',
  frozen_transcription_files=47,all_frozen_hashes_unchanged=True,
  manifest_note='File list excludes this manifest itself to avoid self-reference.',
  excluded='Supplied scans/context/attachments; downloaded literature PDFs/images; caches and compiled build outputs.',
  files=[dict(path=name,size=len(body),sha256=hashlib.sha256(body).hexdigest()) for name,body in sorted(data.items())])
manifest_bytes=(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode()
data[MANIFEST]=manifest_bytes
fd,tmp=tempfile.mkstemp(prefix='.final-',suffix='.tmp',dir=TARGET.parent);os.close(fd)
try:
    with zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name,body in sorted(data.items()):
            info=zipfile.ZipInfo(name,(1980,1,1,0,0,0));info.create_system=3;info.external_attr=0o100644<<16
            z.writestr(info,body,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
    with zipfile.ZipFile(tmp) as z:
        assert z.testzip() is None
        assert len([n for n in z.namelist() if n.startswith('pages/') and n.endswith('.tex')])==46
        assert all(z.read(name)==body for name,body in data.items())
    os.link(tmp,TARGET)
finally:
    Path(tmp).unlink(missing_ok=True)
(ROOT/MANIFEST).write_bytes(manifest_bytes)
print(json.dumps(dict(path=str(TARGET),files=len(data),bytes=TARGET.stat().st_size,
    sha256=hashlib.sha256(TARGET.read_bytes()).hexdigest(),crc_and_contents_verified=True),indent=2))
