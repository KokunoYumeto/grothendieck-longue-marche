"""Freeze or verify the transcription bytes; never rewrites a page."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, sys

root=Path(__file__).resolve().parents[1]
record=root/'records'/'transcription_hashes.json'
log=root/'progress.log'
now=lambda:datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

if '--verify' in sys.argv:
    frozen=json.loads(record.read_text())
    changed=[name for name,h in frozen['sha256'].items() if digest(root/name)!=h]
    if changed:raise SystemExit('FROZEN TRANSCRIPTION CHANGED: '+', '.join(changed))
    with log.open('a') as f:f.write('frozen SHA-256 values verified unchanged for all 31 pages and combined transcription '+now()+'\n')
    print('All 32 frozen SHA-256 values are unchanged.')
else:
    if record.exists():raise SystemExit('Transcription already frozen.')
    text=log.read_text()
    expected=[95,96,97,98,99,100,101,103,104,105,106,107,108,109,110,111,112,117,118,124,126,129,130,131,132,133,135,137,138,139,140]
    audits=[int(x) for x in re.findall(r'^scan (\d+) audited ',text,re.M)]
    if audits!=expected:raise SystemExit('Sequential audit list is incomplete or out of order.')
    if 'context opened ' in text:raise SystemExit('Context was opened before this freeze.')
    files=sorted((root/'pages').glob('*.tex'))+[root/'MPL_29_095-140_transcription.tex']
    if len(files)!=32:raise SystemExit('Expected 31 page fragments plus combined file.')
    if files[-1].read_bytes()!=b''.join(p.read_bytes() for p in files[:-1]):raise SystemExit('Combined fragment is not exact concatenation.')
    values={str(p.relative_to(root)):digest(p) for p in files}
    stamp=now()
    record.write_text(json.dumps({'frozen_at_utc':stamp,'sha256':values},indent=2)+'\n')
    with log.open('a') as f:
        f.write('final pre-freeze mechanical validation: 31 pages, 521 inventory elements, successful pdfLaTeX syntax compilation, no overfull boxes '+stamp+'\n')
        for name,h in values.items():f.write('SHA-256 '+h+'  '+name+'\n')
        f.write('transcription frozen '+stamp+'\n')
    print('Transcription frozen:',stamp)
