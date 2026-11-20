#!/usr/bin/env python3
"""Freeze or verify the 26 transcription files, without editing their bytes."""
import argparse
import hashlib
import os
import re
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
SCANS = (17,18,20,22,25,27,28,29,33,34,36,38,40,41,42,43,44,45,46,47,48,49,50,51,52)
NAMES = [f'pages/16_scan{n:03}.tex' for n in SCANS] + ['SP65_C13_16_transcription.tex']


def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def append(text):
    with (ROOT/'progress.log').open('a') as handle:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())


def hashes():
    return {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in NAMES}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['freeze', 'verify'])
    parser.add_argument('--no-log', action='store_true', help='Verify only; do not append a progress entry')
    args = parser.parse_args()
    log = (ROOT/'progress.log').read_text()
    current = hashes()
    if args.action == 'freeze':
        if args.no_log:
            parser.error('--no-log applies only to verification')
        if re.search(r'^transcription frozen\b', log, re.M):
            raise ValueError('A freeze is already recorded')
        audits = [int(n) for n in re.findall(r'^scan (\d+) audited ', log, re.M)]
        if audits != list(SCANS):
            raise ValueError('All 25 second image readings must precede freezing')
        stamp = now()
        append('transcription frozen '+stamp+'\n' +
               ''.join(f'sha256 {current[name]} {name}\n' for name in NAMES))
        print(f'Frozen {len(current)} transcription files: {stamp}')
    else:
        if len(re.findall(r'^transcription frozen\b', log, re.M)) != 1:
            raise ValueError('Exactly one freeze must be recorded')
        entries = re.findall(r'^sha256 ([0-9a-f]{64}) (.+)$', log, re.M)
        frozen = {name: digest for digest,name in entries}
        if len(entries) != len(NAMES) or set(frozen) != set(NAMES):
            raise ValueError('Frozen hash target set differs from the 26 transcription files')
        changed = [name for name in NAMES if frozen[name] != current[name]]
        if changed:
            raise ValueError('Frozen bytes changed: '+', '.join(changed))
        stamp = now()
        if not args.no_log:
            append('frozen hashes checked unchanged '+stamp+'\n')
        print(f'All 26 frozen SHA-256 values are unchanged: {stamp}')


if __name__ == '__main__':
    main()
