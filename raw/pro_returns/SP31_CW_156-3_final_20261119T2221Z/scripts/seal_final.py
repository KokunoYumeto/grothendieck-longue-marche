#!/usr/bin/env python3
"""Record the actual end-of-research check of all frozen transcription bytes."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import re

out=Path(__file__).resolve().parents[1]
log=out/'progress.log'
s=log.read_text()
assert 'transcription frozen ' in s and 'context opened ' in s
rows=re.findall(r'^SHA256 (.+) ([0-9a-f]{64})$',s,re.M)
assert len(rows)==25, len(rows)
for name,expected in rows:
 actual=hashlib.sha256((out/name).read_bytes()).hexdigest()
 assert actual==expected,(name,expected,actual)
pages=sorted((out/'pages').glob('*.tex'))
assert len(pages)==24
assert (out/'SP31_CW_156-3_transcription.tex').read_bytes()==b''.join(p.read_bytes() for p in pages)
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with log.open('a') as f:
 f.write('research notes complete '+stamp+'; 65 principal notes on all24 scans, full C-note audit and check events integrated; supporting proofs assessed by root.\n')
 f.write('final frozen hashes unchanged '+stamp+'; all24 page files and combined transcription match the25 SHA256 records written before context opening; exact byte concatenation verified; no post-freeze TeX edits.\n')
print('All 25 frozen hashes unchanged; '+stamp)
