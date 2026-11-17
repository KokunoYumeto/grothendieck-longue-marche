#!/usr/bin/env python3
"""Freeze or verify the reader's completed transcription; never alters page text."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
STEM = 'MPL_57_089-132'
EXPECTED = list(range(89, 98)) + list(range(99, 133))

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('freeze', 'verify'))
    args = parser.parse_args()
    manifest_path = ROOT / 'records/frozen_sha256.json'
    log = ROOT / 'progress.log'
    contents = log.read_text()
    if args.action == 'freeze':
        if manifest_path.exists() or re.search(r'^transcription frozen ', contents, re.M):
            raise SystemExit('Already frozen; refusing to replace the baseline.')
        if re.search(r'^context opened ', contents, re.M):
            raise SystemExit('Context was already opened; refusing a late freeze.')
        scans = sorted(int(n) for n in re.findall(r'^scan (\d{3}) audited ', contents, re.M))
        if scans != EXPECTED:
            raise SystemExit(f'Audit log must contain exactly all 43 scans: {scans}')
        for n in EXPECTED:
            record = json.loads((ROOT / f'records/scan{n:03d}.json').read_text())
            if not record.get('audit', {}).get('utc'):
                raise SystemExit(f'Missing audit record for {n}')
        pages = [ROOT / f'pages/{STEM}_57_scan{n:03d}.tex' for n in EXPECTED]
        combined = ROOT / f'{STEM}_transcription.tex'
        expected_combined = b'\\cotefile{57}\n' + b'\n'.join(p.read_bytes().rstrip() + b'\n' for p in pages)
        # The packaging helper is the canonical concatenator; use it to avoid
        # silently assuming its separator convention.
        from package_tools import combined_bytes
        if combined.read_bytes() != combined_bytes(ROOT):
            raise SystemExit('Combined transcription does not match all page files.')
        stamp = utc()
        hashes = {str(p.relative_to(ROOT)): digest(p) for p in pages + [combined]}
        manifest_path.write_text(json.dumps({'frozen_utc': stamp, 'sha256': hashes}, indent=2) + '\n')
        hash_lines = [f'sha256 {h} {name}' for name, h in hashes.items()]
        with log.open('a') as stream:
            stream.write('notation comparison completed ' + stamp + '\n')
            stream.write('\n'.join(hash_lines) + '\n')
            stream.write('transcription frozen ' + stamp + '\n')
        print(f'Frozen {len(hashes)} files at {stamp}')
    else:
        data = json.loads(manifest_path.read_text())
        failures = [name for name, h in data['sha256'].items() if digest(ROOT / name) != h]
        if failures:
            raise SystemExit('FROZEN HASH MISMATCH: ' + ', '.join(failures))
        stamp = utc()
        with log.open('a') as stream:
            stream.write(f'frozen hashes verified unchanged {stamp}; all {len(data["sha256"])} page/combined SHA-256 values match the pre-context baseline\n')
        print(f'All {len(data["sha256"])} frozen hashes unchanged at {stamp}')

if __name__ == '__main__':
    main()
