"""Freeze or verify the exact transcription bytes; never edit transcription."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys

out = Path(__file__).resolve().parents[1]
files = sorted((out/'pages').glob('142_scan*.tex')) + [out/'SP72_C13_142_transcription.tex']
assert len(files) == 25
hashes = {str(p.relative_to(out)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
record = out/'documentation/frozen_transcription_sha256.json'
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
if len(sys.argv)>1 and sys.argv[1]=='check':
    assert json.loads(record.read_text()) == hashes, 'Frozen transcription changed.'
    with (out/'progress.log').open('a') as f:
        f.write(f'transcription hashes unchanged {stamp}: all 24 pages and combined transcription verified\n')
    print('All 25 frozen SHA-256 hashes unchanged.')
else:
    assert not record.exists(), 'Refusing to overwrite a freeze record.'
    reports = [json.loads(p.read_text()) for p in (out/'documentation/decided').glob('scan*.json')]
    assert len(reports)==24 and all(r.get('audit_complete') for r in reports)
    record.write_text(json.dumps(hashes, indent=2)+'\n')
    with (out/'progress.log').open('a') as f:
        f.write(f'transcription frozen {stamp}\n')
        for path, sha in hashes.items(): f.write(f'SHA-256 {sha} {path}\n')
    print('Frozen 24 pages and combined transcription.')
