#!/usr/bin/env python3
"""Freeze or verify the twelve transcription files without modifying their text."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'transcription_sha256.tsv'
def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def log(s):
    with (ROOT/'progress.log').open('a') as f:f.write(s+'\n')
command=sys.argv[1] if len(sys.argv)>1 else ''
if command=='freeze':
    if MANIFEST.exists():raise SystemExit('Refusing to replace an existing freeze manifest.')
    files=sorted((ROOT/'pages').glob('*.tex'))+[ROOT/'SP62_CW_162-1+162-6_transcription.tex']
    if len(files)!=12:raise SystemExit('Expected exactly 11 pages and one combined fragment.')
    rows=[(str(p.relative_to(ROOT)),digest(p)) for p in files]
    with MANIFEST.open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['file','sha256']);w.writerows(rows)
    log('transcription frozen '+now())
    for name,sha in rows:log('SHA256 '+sha+' '+name)
    print('Frozen twelve transcription files.')
elif command=='verify':
    with MANIFEST.open() as f:rows=list(csv.DictReader(f,delimiter='\t'))
    if len(rows)!=12:raise SystemExit('Wrong frozen-file count.')
    failed=[r['file'] for r in rows if digest(ROOT/r['file'])!=r['sha256']]
    if failed:raise SystemExit('Hash mismatch: '+', '.join(failed))
    log('frozen transcription hashes unchanged '+now()+'; all 12 SHA-256 digests verified')
    print('All twelve frozen SHA-256 digests are unchanged.')
else:raise SystemExit('Usage: freeze_transcription.py freeze|verify')
