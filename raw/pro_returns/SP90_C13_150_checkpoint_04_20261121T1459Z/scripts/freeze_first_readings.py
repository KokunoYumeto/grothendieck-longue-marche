"""Preserve the pre-audit box lists and independently comparable first readings.

This is separate from the final transcription freeze. It may be run only after
all 25 first readings have been approved and logged. It never reads images or
chooses a transcription.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, re

ROOT=Path(__file__).resolve().parents[1]
STATE=ROOT/'reference/first_readings_frozen.json'
EXPECTED=list(range(25,34))+list(range(36,52))

def main():
    p=argparse.ArgumentParser();p.add_argument('--verify',action='store_true');a=p.parse_args()
    files=[ROOT/'second'/f'150_scan{s:03}_{suffix}.tsv' for s in EXPECTED for suffix in ('boxes','first')]
    missing=[str(x.relative_to(ROOT)) for x in files if not x.is_file()]
    if missing:raise RuntimeError('Missing pre-audit records: '+str(missing))
    hashes={str(x.relative_to(ROOT)):hashlib.sha256(x.read_bytes()).hexdigest() for x in files}
    if a.verify:
        if json.loads(STATE.read_text())['sha256']!=hashes:raise RuntimeError('Pre-audit records have changed')
        print(json.dumps({'files':len(files),'unchanged':True}));return
    if STATE.exists():raise FileExistsError('Pre-audit records already frozen')
    done=[int(x) for x in re.findall(r'^scan (\d+) done ',(ROOT/'progress.log').read_text(),re.M)]
    if sorted(done)!=EXPECTED:raise RuntimeError('All 25 first readings must be approved and logged')
    stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    STATE.write_text(json.dumps({'frozen_at':stamp,'sha256':hashes},indent=2)+'\n')
    with (ROOT/'progress.log').open('a') as f:f.write(f'first-reading box records frozen {stamp}: {len(files)} files; independent image-only second phase begins\n')
    print(json.dumps({'files':len(files),'utc':stamp}))

if __name__=='__main__':main()
