#!/usr/bin/env python3
"""Verify the frozen source and create the final, source-excluding ZIP.

This script never writes page files or the combined transcription.
It verifies already-created notes, logs the final hash check, runs structural
validation, inventories the work files, and packages every work file.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
WORKING = ROOT / 'working'
PREFIX = 'MPL_116+117'
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

hashes = []
for line in (WORKING/'frozen_sha256.txt').read_text().splitlines():
    expected, name = line.split('  ', 1)
    actual = hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
    assert expected == actual, f'Frozen file changed: {name}'
    hashes.append(dict(file=name,expected_sha256=expected,actual_sha256=actual,unchanged=True))
assert len(hashes)==35

notes = (ROOT/f'{PREFIX}_notes.md').read_text()
assert len(re.findall(r'^\| \*\*(?:STRATA|PATHS|BISITE|RESIDUE) [^*]+\*\* —', notes, re.M))==255
assert len(re.findall(r'^### NR(?:0[1-9]|1[0-2]|K[123]) —', notes, re.M))==15
searches = json.loads((WORKING/'context_search_log.json').read_text())
assert searches['query_count']==385
assert (WORKING/'final_notes_mechanical_review.md').is_file()

obs=WORKING/'observations.md'
old=obs.read_text()
banner='> First-pass process record, superseded by the audited frozen transcription and final research notes wherever they differ.\n\n'
if not old.startswith(banner):
    obs.write_text(banner+old)

record=dict(checked_utc=now,scope='34 page files and combined diplomatic transcription',
            unchanged_count=35,context_opened_after_freeze=True,files=hashes)
(WORKING/'final_hash_verification.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
with (ROOT/'progress.log').open('a') as log:
    log.write(f'research notes completed {now}: 44 main mathematical notes; 5 planning answers; 255 DSS and 15 NR individual comparisons; 13 post-freeze reading questions; dedicated reservations and title/count sections.\n')
    log.write(f'context searches recorded {now}: 385 queries, including all 130 named note items and all 255 DSS comparisons.\n')
    log.write(f'support-task boundary {now}: assistants catalogued context and checked references, file structure and coverage; the manuscript image readings and transcription were performed by the root in one stream.\n')
    log.write(f'final SHA-256 verification {now}: all 35 frozen transcription hashes verified unchanged after context comparison; no page or combined-transcription bytes changed.\n')

checks=[
    [sys.executable,str(ROOT/'scripts/review_final_notes.py')],
    [sys.executable,str(ROOT/'scripts/validate_package.py'),str(ROOT),'--final']
]
outputs=[]
for cmd in checks:
    p=subprocess.run(cmd,capture_output=True,text=True)
    outputs.append(p.stdout+p.stderr)
    assert p.returncode==0, p.stdout+p.stderr
(WORKING/'qa/final_validation.log').write_text('\n'.join(outputs))
with (ROOT/'progress.log').open('a') as log:
    log.write(f'final structural checks passed {now}: 34 ordered page files, exact combined concatenation, 592 inventory rows all yes, 34 recorded visual audits, freeze-before-context ordering, complete research-note coverage.\n')
    log.write(f'final packaging {now}: work files only; original attached scans and contextual sources excluded; next hourly checkpoint would fall at 19:03:51 UTC and is not yet due.\n')

manifest=WORKING/'final_file_manifest.json'
entries=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or p==manifest: continue
    rel=p.relative_to(ROOT)
    assert rel.parts[0] not in {'scans','context','upload'}
    assert p.suffix.lower() not in {'.jpg','.jpeg','.png'}
    entries.append(dict(file=str(rel),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
manifest.write_text(json.dumps(dict(created_utc=now,excludes='This manifest itself; original attachments are outside the work directory.',files=entries),ensure_ascii=False,indent=2)+'\n')

archive=ROOT.parent/f'{PREFIX}.zip'
paths=sorted(p for p in ROOT.rglob('*') if p.is_file())
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in paths:
        z.write(p,p.relative_to(ROOT))
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert sorted(z.namelist())==sorted(str(p.relative_to(ROOT)) for p in paths)
    for p in paths:
        assert hashlib.sha256(z.read(str(p.relative_to(ROOT)))).digest()==hashlib.sha256(p.read_bytes()).digest()
print(json.dumps(dict(archive=str(archive),bytes=archive.stat().st_size,files=len(paths),
    sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),frozen_hashes_unchanged=35,
    pages=34,inventory_elements=592,dss_comparisons=255,nr_comparisons=15,crc_and_content_check='PASS'),indent=2))
