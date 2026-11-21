"""Freeze or verify the exact final fragments; this does not compile LaTeX."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, sys, io, json
from build_reports import ROOT, ORDER, PREFIX
from integrity import atomic_write, verify_freeze

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
manifest=ROOT/'TRANSCRIPTION_SHA256.tsv'
mode=sys.argv[1]
if mode=='freeze':
    for n in ORDER:
        r=json.loads((ROOT/'adjudicated'/f'147_scan{n:03d}.json').read_text())
        if not r.get('audit_completed'):
            raise SystemExit(f'Cannot freeze before every blind audit is approved: {n:03d}')
    paths=[ROOT/'pages'/f'147_scan{n:03d}.tex' for n in ORDER]
    paths.append(ROOT/f'{PREFIX}_transcription.tex')
    if manifest.exists():
        raise SystemExit('Already frozen. Verify the existing manifest.')
    rows=[{'path':str(p.relative_to(ROOT)),'sha256':digest(p)} for p in paths]
    buffer=io.StringIO(newline='')
    w=csv.DictWriter(buffer,['path','sha256'],delimiter='\t');w.writeheader();w.writerows(rows)
    atomic_write(manifest,buffer.getvalue().encode(),exclusive=True)
    verify_freeze()
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'transcription frozen {stamp}\n')
        for r in rows:f.write(f'SHA-256 {r["path"]} {r["sha256"]}\n')
    print(f'Frozen {len(rows)} files at {stamp}')
elif mode=='verify':
    rows=verify_freeze()
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'transcription hashes verified unchanged {stamp}: {len(rows)} files\n')
    print(f'Verified unchanged: {len(rows)} files')
else:
    raise SystemExit('Use freeze or verify')
