"""Freeze or verify the exact final fragments; this does not compile LaTeX."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, sys
from build_reports import ROOT, ORDER, PREFIX

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
manifest=ROOT/'TRANSCRIPTION_SHA256.tsv'
mode=sys.argv[1]
if mode=='freeze':
    paths=[ROOT/'pages'/f'147_scan{n:03d}.tex' for n in ORDER]
    paths.append(ROOT/f'{PREFIX}_transcription.tex')
    if manifest.exists():
        raise SystemExit('Already frozen. Verify the existing manifest.')
    rows=[{'path':str(p.relative_to(ROOT)),'sha256':digest(p)} for p in paths]
    with manifest.open('w',newline='') as f:
        w=csv.DictWriter(f,['path','sha256'],delimiter='\t');w.writeheader();w.writerows(rows)
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'transcription frozen {stamp}\n')
        for r in rows:f.write(f'SHA-256 {r["path"]} {r["sha256"]}\n')
    print(f'Frozen {len(rows)} files at {stamp}')
elif mode=='verify':
    with manifest.open() as f:rows=list(csv.DictReader(f,delimiter='\t'))
    changed=[r['path'] for r in rows if digest(ROOT/r['path'])!=r['sha256']]
    if changed:raise SystemExit('Frozen transcription changed: '+', '.join(changed))
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'transcription hashes verified unchanged {stamp}: {len(rows)} files\n')
    print(f'Verified unchanged: {len(rows)} files')
else:
    raise SystemExit('Use freeze or verify')
