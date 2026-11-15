#!/usr/bin/env python3
"""Verify the frozen deliverables, record completion, and build the final ZIP.

Only completion records and the external archive are written. No transcription
file is ever rewritten. Source inputs and transient bytecode are excluded.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / 'records'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stamp():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def read_json(name):
    return json.loads((RECORDS / name).read_text())


def main():
    frozen = read_json('transcription_freeze.json')
    assert len(frozen['files']) == 49
    assert all(sha(ROOT / name) == digest for name, digest in frozen['files'].items())
    page_files = sorted((ROOT / 'pages').glob('*.tex'))
    assert [int(re.search(r'scan(\d+)', p.name).group(1)) for p in page_files] == list(range(146, 194))
    combined = ROOT / 'MPL_84_146-193_transcription.tex'
    assert combined.read_text() == '\n'.join(p.read_text() for p in page_files)
    assert combined.read_text().startswith('\\cotefile{84}\n\\scanpage{146}')
    assert '\\documentclass' not in combined.read_text()
    with (ROOT / 'MPL_84_146-193_inventory.csv').open() as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 750 and all(r['transcribed'] == 'yes' for r in rows)
    notes = ROOT / 'MPL_84_146-193_notes.md'
    ids = re.findall(r'^### ([ELT]\d{3}\.\d+|R\d{2})\b', notes.read_text(), re.M)
    assert len(ids) == len(set(ids)) == 208
    notes_review = read_json('final_notes_review.json')
    assert notes_review['final_status'] == 'clean'
    assert notes_review['sha256'] == sha(notes)
    assert read_json('final_package_review.json')['result'] == 'PASS'
    technical = read_json('tex_validation.json')
    assert len(technical['pages']) == 48
    assert not technical['missing_character_warnings']
    for page in technical['pages']:
        assert page['returncode'] == 0
        assert frozen['files'][page['file']] == page['sha256']

    report = {
        'utc': stamp(),
        'status': 'all delivery prerequisites passed',
        'pages': 48,
        'inventory_elements': 750,
        'all_inventory_rows_transcribed': True,
        'doubt_occurrences': 710,
        'research_items': len(ids),
        'research_words_including_registers_and_bibliography': len(notes.read_text().split()),
        'notes_sha256': sha(notes),
        'frozen_transcription_files': len(frozen['files']),
        'frozen_hashes_unchanged': True,
        'compiled_pages': 48,
        'compilation_failures': 0,
        'missing_character_warnings': 0,
        'archive': ROOT.name + '.zip',
        'excluded': ['user-supplied source files', 'scan/crop images', 'temporary renderings', '__pycache__'],
        'limits': 'Reading doubts remain explicit. Technical compilation does not certify manuscript readings. Local research calculations do not prove the omitted global category claims.'
    }
    (RECORDS / 'final_delivery.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    with (ROOT / 'progress.log').open('a') as handle:
        handle.write('final research review clean: 208 items, 208 context-query records, 15 own ideas with confidence and reasons ' + stamp() + '\n')
        handle.write('final package complete: 48 pages, 750 inventory elements, 710 doubtful readings; final ZIP assembly follows ' + stamp() + '\n')
    subprocess.run([sys.executable, str(RECORDS / 'freeze_transcription.py'), 'verify'], check=True)

    files = sorted(p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    forbidden = {'.jpg', '.jpeg', '.png', '.pdf', '.zip', '.pyc'}
    assert not any(p.suffix.lower() in forbidden for p in files)
    destination = ROOT.parent / (ROOT.name + '.zip')
    temporary = destination.with_suffix('.zip.tmp')
    with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            archive.write(path, path.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(temporary) as archive:
        assert archive.testzip() is None
        assert len(archive.namelist()) == len(files)
        for name, digest in frozen['files'].items():
            assert hashlib.sha256(archive.read(name)).hexdigest() == digest
        assert hashlib.sha256(archive.read(notes.name)).hexdigest() == sha(notes)
    temporary.replace(destination)
    print(json.dumps({'archive': str(destination), 'files': len(files),
                      'bytes': destination.stat().st_size, 'sha256': sha(destination),
                      'zip_crc_check': 'passed', 'archived_frozen_hashes': '49/49 unchanged'}, indent=2))


if __name__ == '__main__':
    main()
