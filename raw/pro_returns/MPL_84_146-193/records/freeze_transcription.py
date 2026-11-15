"""Freeze or verify the transcription without reading any contextual source.

Run from any directory: python records/freeze_transcription.py freeze|verify
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def freeze():
    log = ROOT / 'progress.log'
    prior = log.read_text()
    if 'transcription frozen ' in prior or 'context opened ' in prior:
        raise RuntimeError('A freeze/context event already exists; refusing to replace it.')
    pages = [ROOT / f'pages/MPL_84_146-193_84_scan{n}.tex' for n in range(146, 194)]
    assert all(p.is_file() for p in pages)
    assert len(list((ROOT / 'pages').glob('*.tex'))) == 48
    assert sorted(map(int, re.findall(r'^84 scan (\d+) done ', prior, re.M))) == list(range(146, 194))
    assert sorted(map(int, re.findall(r'^scan (\d+) audited ', prior, re.M))) == list(range(146, 194))
    combined = ROOT / 'MPL_84_146-193_transcription.tex'
    assert combined.read_text() == '\n'.join(p.read_text() for p in pages)
    assert combined.read_text().startswith('\\cotefile{84}\n\\scanpage{146}')
    with (ROOT / 'MPL_84_146-193_inventory.csv').open() as f:
        rows = list(csv.DictReader(f))
    assert set(int(r['scan']) for r in rows) == set(range(146, 194))
    assert all(r['transcribed'] == 'yes' for r in rows)
    report = json.loads((ROOT / 'records/tex_validation.json').read_text())
    assert len(report['pages']) == 48
    for item in report['pages']:
        assert item['returncode'] == 0, item['file']
        assert digest(ROOT / item['file']) == item['sha256'], item['file']
    hashes = {str(p.relative_to(ROOT)): digest(p) for p in pages + [combined]}
    stamp = utc()
    out = {'utc': stamp, 'algorithm': 'SHA-256', 'files': hashes}
    (ROOT / 'records/transcription_freeze.json').write_text(json.dumps(out, indent=2) + '\n')
    with log.open('a') as f:
        f.write(f'notation comparison and inventory audit completed {stamp}\n')
        for name, h in hashes.items():
            f.write(f'SHA-256 {h} {name}\n')
        f.write(f'transcription frozen {stamp}\n')
    print(f'Frozen {len(pages)} page files and combined transcription; inventory {len(rows)} elements; {stamp}')


def verify():
    record = json.loads((ROOT / 'records/transcription_freeze.json').read_text())
    bad = [name for name, h in record['files'].items() if digest(ROOT / name) != h]
    if bad:
        raise RuntimeError('Frozen hashes changed: ' + ', '.join(bad))
    stamp = utc()
    with (ROOT / 'progress.log').open('a') as f:
        f.write(f'frozen hashes verified unchanged: all 48 page files and combined transcription {stamp}\n')
    print('All 49 frozen SHA-256 hashes unchanged; ' + stamp)


if __name__ == '__main__':
    {'freeze': freeze, 'verify': verify}[sys.argv[1]]()
