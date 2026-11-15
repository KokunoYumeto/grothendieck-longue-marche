#!/usr/bin/env python3
"""Freeze audited transcription hashes, or verify the existing freeze.

No mode edits a page or the combined fragment. Context is never opened here.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
PREFIX = 'MPL_134-8_043-087'
SCANS = [n for n in range(43, 88) if n != 60]
LOG = ROOT / 'progress.log'
MANIFEST = ROOT / 'records/transcription_freeze.json'


def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def snapshot():
    paths = [ROOT / 'pages' / f'{PREFIX}_134-8_scan{n:03d}.tex' for n in SCANS]
    combined = ROOT / f'{PREFIX}_transcription.tex'
    assert combined.read_bytes() == b''.join(p.read_bytes() for p in paths)
    return [{'file': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size,
             'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
            for p in paths + [combined]]


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--freeze', action='store_true')
parser.add_argument('--record-verification', action='store_true')
args = parser.parse_args()
assert not (args.freeze and args.record_verification)
state = LOG.read_text()
files = snapshot()
if args.freeze:
    assert not MANIFEST.exists()
    assert not re.search(r'^(transcription frozen|context opened) ', state, re.M)
    done = [int(x) for x in re.findall(r'^134-8 scan (\d{3}) done ', state, re.M)]
    audits = [int(x) for x in re.findall(r'^scan (\d{3}) audited ', state, re.M)]
    assert done == SCANS and audits == SCANS
    qa = json.loads((ROOT / 'records/latex_qa_combined_final.json').read_text())
    entry = qa['pages'][0]
    assert entry['returncode'] == 0 and not entry['errors']
    assert entry['source_sha256'] == files[-1]['sha256']
    stamp = utc()
    data = {'frozen_utc': stamp, 'scope': '44 page fragments and exact combined transcription', 'files': files}
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    with LOG.open('a') as f:
        for item in files:
            f.write('SHA256 ' + item['file'] + ' ' + item['sha256'] + '\n')
        f.write('transcription frozen ' + stamp + '\n')
    print('Frozen', len(files), 'transcription files at', stamp)
else:
    data = json.loads(MANIFEST.read_text())
    assert data['files'] == files, 'A transcription file changed after freeze'
    stamp = utc()
    if args.record_verification:
        with LOG.open('a') as f:
            f.write('transcription hashes unchanged: all 44 page files and combined transcription verified ' + stamp + '\n')
    print('All 45 frozen hashes unchanged at', stamp)
