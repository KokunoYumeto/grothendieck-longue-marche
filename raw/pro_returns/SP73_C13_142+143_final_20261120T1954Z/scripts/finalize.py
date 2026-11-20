"""Freeze, verify, then package the completed transcription without compiling it."""
from pathlib import Path
from datetime import datetime, timezone
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'SP73_C13_142+143'
PAGES = [f'142_scan{n:03}' for n in
         [101,102,103,104,106,108,109,110,111,112,113,114,115,116,117,118,120,121]]
PAGES += [f'143_scan{n:03}' for n in range(2,8)]
MANIFEST = ROOT / 'state' / 'transcription_sha256.json'
EXPECTED_NAMES = ['pages/' + page + '.tex' for page in PAGES]
EXPECTED_NAMES.append(PREFIX + '_transcription.tex')

def stamp():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def log(line):
    with (ROOT / 'progress.log').open('a') as stream:
        stream.write(line + '\n')

def verify():
    manifest = json.loads(MANIFEST.read_text())
    if set(manifest.get('sha256', {})) != set(EXPECTED_NAMES):
        raise SystemExit('Frozen manifest must name exactly the 25 expected transcription files.')
    if any(not isinstance(value, str) or not re.fullmatch(r'[0-9a-f]{64}', value)
           for value in manifest['sha256'].values()):
        raise SystemExit('Frozen manifest contains an invalid SHA-256 value.')
    mismatches = [name for name, expected in manifest['sha256'].items()
                  if digest(ROOT / name) != expected]
    if mismatches:
        raise SystemExit('Frozen transcription changed: ' + ', '.join(mismatches))
    return manifest

mode = sys.argv[1]
if mode == 'freeze':
    if MANIFEST.exists():
        raise SystemExit('A frozen manifest already exists; do not overwrite it.')
    subprocess.run([sys.executable, str(ROOT / 'scripts' / 'validate_deliverables.py')], check=True)
    for page in PAGES:
        record = json.loads((ROOT / 'state' / f'{page}_accepted.json').read_text())
        if not record.get('audited_at') or not record.get('audit_main_review', {}).get('approved'):
            raise SystemExit('Unfinished second reading: ' + page)
    names = EXPECTED_NAMES
    manifest = {'frozen_at': stamp(), 'sha256': {name: digest(ROOT / name) for name in names}}
    MANIFEST.write_text(json.dumps(manifest, indent=2) + '\n')
    log('transcription frozen ' + manifest['frozen_at'])
    for name, value in manifest['sha256'].items():
        log('SHA-256 ' + value + ' ' + name)
    print(json.dumps({'frozen': len(names), 'at': manifest['frozen_at']}))
elif mode == 'verify':
    manifest = verify()
    log('frozen SHA-256 verification unchanged for all ' + str(len(manifest['sha256'])) +
        ' transcription files ' + stamp())
    print(json.dumps({'unchanged': len(manifest['sha256'])}))
elif mode == 'package':
    manifest = verify()
    subprocess.run([sys.executable, str(ROOT / 'scripts' / 'validate_deliverables.py')], check=True)
    destination = ROOT.parent / (PREFIX + '.zip')
    if destination.exists():
        raise SystemExit('Final archive already exists; never overwrite without review.')
    log('final package verified: all ' + str(len(manifest['sha256'])) +
        ' frozen transcription SHA-256 values unchanged ' + stamp())
    files = [path for path in sorted(ROOT.rglob('*')) if path.is_file()
             and path.suffix.lower() != '.zip' and '__pycache__' not in path.parts]
    with ZipFile(destination, 'x', compression=ZIP_DEFLATED, compresslevel=6) as archive:
        for path in files:
            archive.write(path, path.relative_to(ROOT))
    with ZipFile(destination) as archive:
        bad = archive.testzip()
        if bad:
            raise SystemExit('Archive CRC failure: ' + bad)
        for name, expected in manifest['sha256'].items():
            if hashlib.sha256(archive.read(name)).hexdigest() != expected:
                raise SystemExit('Archive transcription mismatch: ' + name)
    print(json.dumps({'path': str(destination), 'bytes': destination.stat().st_size,
                      'files': len(files), 'verified_frozen_files': len(manifest['sha256'])}))
else:
    raise SystemExit('Use freeze, verify, or package.')
