#!/usr/bin/env python3
"""Freeze or verify the 24 final fragments and their exact concatenation."""
from pathlib import Path
import argparse
import datetime
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
SCANS = tuple(range(52, 65)) + tuple(range(66, 77))
NAMES = [f'pages/142_scan{n:03}.tex' for n in SCANS] + ['SP71_C13_142_transcription.tex']

def utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def digest(name):
    return hashlib.sha256((ROOT / name).read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--freeze', action='store_true')
    group.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    log = ROOT / 'progress.log'
    text = log.read_text()
    if args.freeze:
        if re.search(r'^transcription frozen ', text, re.M):
            raise SystemExit('Already frozen: refusing a second baseline.')
        for status in ('done', 'audited'):
            found = [int(x) for x in re.findall(rf'^scan (\d{{3}}) {status} ', text, re.M)]
            if tuple(found) != SCANS:
                raise SystemExit(f'Ordered {status} coverage is incomplete.')
        concatenated = b''.join((ROOT / name).read_bytes() for name in NAMES[:-1])
        if concatenated != (ROOT / NAMES[-1]).read_bytes():
            raise SystemExit('Combined fragment differs from ordered page concatenation.')
        records = [f'sha256 {digest(name)} {name}\n' for name in NAMES]
        with log.open('a') as f:
            f.write(f'transcription frozen {utc()}\n')
            f.writelines(records)
        print('Frozen 24 page fragments and the combined transcription.')
    else:
        records = re.findall(r'^sha256 ([0-9a-f]{64}) (.+)$', text, re.M)
        if len(records) != 25 or [name for _, name in records] != NAMES:
            raise SystemExit('Expected precisely the 25 ordered freeze records.')
        mismatches = [name for expected, name in records if digest(name) != expected]
        if mismatches:
            raise SystemExit('Changed since freeze: ' + ', '.join(mismatches))
        if re.search(r'^hashes unchanged ', text, re.M):
            print('All 25 hashes still match; existing confirmation preserved.')
        else:
            with log.open('a') as f:
                f.write(f'hashes unchanged {utc()}\n')
            print('All 25 hashes unchanged; confirmation recorded.')

if __name__ == '__main__':
    main()
