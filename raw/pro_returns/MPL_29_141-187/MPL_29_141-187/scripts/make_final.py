#!/usr/bin/env python3
"""Build the final ZIP from completed deliverables, excluding supplied sources.

Run the structural and editorial checks before this script. It never changes a
transcription, never overwrites an archive, and does not upload the resulting ZIP.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, re, zipfile
from make_checkpoint import gather, PACKAGE

root=Path(__file__).resolve().parents[1]
target=root.parent/(PACKAGE+'.zip')
if target.exists():raise SystemExit('Refusing to overwrite '+str(target))
files,skipped=gather(root)
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f:
    f.write(f'final ZIP prepared {stamp}; all required deliverables and work documentation; supplied sources and earlier checkpoints excluded\n')
with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    z.comment=(PACKAGE+' final package created '+stamp).encode()
    for path in files:z.write(path,PACKAGE+'/'+path.relative_to(root).as_posix())
with zipfile.ZipFile(target) as z:
    bad=z.testzip()
    if bad:raise RuntimeError('ZIP CRC failure: '+bad)
    names=z.namelist()
    page_names=[n for n in names if re.search(r'/pages/MPL_29_141-187_29_scan\d+\.tex$',n)]
    assert len(page_names)==47
    assert not any(re.search(r'\.(jpg|jpeg|png|pdf|zip)$',n,re.I) for n in names)
    assert not any('/context/' in n or '/upload/' in n for n in names)
    for line in (root/'progress.log').read_text().splitlines():
        m=re.fullmatch(r'sha256 ([0-9a-f]{64}) (.+)',line)
        if m:assert hashlib.sha256(z.read(PACKAGE+'/'+m[2])).hexdigest()==m[1],m[2]
print('Final ZIP:',target)
print('Created UTC:',stamp)
print('Files:',len(files),'Page fragments:',len(page_names),'Excluded entries:',len(skipped))
print('Bytes:',target.stat().st_size)
print('SHA-256:',hashlib.sha256(target.read_bytes()).hexdigest())
print('CRC and all48 archived frozen hashes: PASS')
