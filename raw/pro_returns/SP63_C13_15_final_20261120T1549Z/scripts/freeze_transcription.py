"""Freeze or verify the exact 25 page fragments and combined transcription."""
from workflow import ROOT, PREFIX, utc
from audit_record import ORDER
from pathlib import Path
import argparse, hashlib, re

p = argparse.ArgumentParser()
p.add_argument('mode', choices=['freeze', 'verify'])
a = p.parse_args()
paths = [ROOT / 'pages' / f'15_scan{s}.tex' for s in ORDER]
paths.append(ROOT / f'{PREFIX}_transcription.tex')
log_path = ROOT / 'progress.log'
log = log_path.read_text()
assert [int(s) for s in re.findall(r'^scan (\d+) done ', log, re.M)] == ORDER
assert [int(s) for s in re.findall(r'^scan (\d+) audited ', log, re.M)] == ORDER
assert paths[-1].read_bytes() == b'\n'.join(p.read_bytes() for p in paths[:-1])
actual = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
if a.mode == 'freeze':
    assert 'transcription frozen ' not in log, 'The transcription is already frozen.'
    with log_path.open('a') as f:
        f.write('transcription frozen ' + utc() + '\n')
        for name, digest in actual.items():
            f.write(f'{digest}  {name}\n')
    print('Frozen 26 SHA-256 digests.')
else:
    recorded = {name: digest for digest, name in re.findall(r'^([0-9a-f]{64})  (.+)$', log, re.M)}
    assert recorded == actual, 'Frozen transcription hashes differ.'
    with log_path.open('a') as f:
        f.write('all 26 frozen transcription SHA-256 hashes unchanged ' + utc() + '\n')
    print('All 26 frozen transcription hashes are unchanged.')
