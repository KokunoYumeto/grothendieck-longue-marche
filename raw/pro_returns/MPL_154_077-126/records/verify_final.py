#!/usr/bin/env python3
"""Read-only final consistency check, optionally against the delivery ZIP."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import csv
import hashlib
import json
import re
import zipfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    scans = [n for n in range(77, 127) if n != 99]
    pages = [f'pages/MPL_154_077-126_154_scan{n:03d}.tex' for n in scans]
    combined = 'MPL_154_077-126_transcription.tex'
    required = set(pages + [combined, 'MPL_154_077-126_doubts.md',
        'MPL_154_077-126_inventory.csv', 'MPL_154_077-126_notes.md',
        'progress.log', 'records/frozen_hashes.json'])
    assert all((root / name).is_file() for name in required)
    manifest = json.loads((root / 'records/frozen_hashes.json').read_text())
    assert set(manifest['files']) == set(pages + [combined])
    for name, digest in manifest['files'].items():
        assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest, name
    assert (root / combined).read_bytes() == b''.join((root / name).read_bytes() for name in pages)
    inventory = list(csv.DictReader((root / 'MPL_154_077-126_inventory.csv').open()))
    assert len(inventory) == 626
    assert {int(row['scan']) for row in inventory} == set(scans)
    assert all(row['transcribed'] == 'yes' for row in inventory)
    notes = (root / 'MPL_154_077-126_notes.md').read_text()
    note_ids = re.findall(r'^#### ([CROT][0-9]+[abc]?) —', notes, re.M)
    queries = json.loads((root / 'records/context_queries.json').read_text())
    searches = json.loads((root / 'records/context_search_summary.json').read_text())
    assert len(note_ids) == len(set(note_ids)) == 75
    assert set(note_ids) == set(queries) == set(searches['note_hits'])
    assert len(searches['context_file_sha256']) == 4
    assert not re.search(r'^\+', notes, re.M)
    assert not any(ord(ch) < 32 and ch not in '\r\n\t' for ch in notes)
    result = {
        'checked_utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'scan_count': len(pages), 'inventory_rows': len(inventory),
        'frozen_hashes_unchanged': len(manifest['files']),
        'combined_is_exact_concatenation': True,
        'research_note_count': len(note_ids), 'matching_context_queries': len(queries),
        'context_files_searched': len(searches['context_file_sha256']),
    }
    if args.archive:
        with zipfile.ZipFile(args.archive) as archive:
            names = archive.namelist()
            assert len(names) == len(set(names)), 'Duplicate ZIP member'
            assert required.issubset(names), 'Missing required ZIP member'
            assert archive.testzip() is None, 'CRC failure'
            forbidden_names = {'STATEMENTS_WITH_STATUS.md', 'RESULTS_STATE.md',
                'Esquisse_cote119_copy1_API_transcription.tex',
                'PROMPT(20261114-232512).md'}
            forbidden_suffixes = {'.jpg', '.jpeg', '.png', '.gif', '.pdf',
                '.zip', '.pyc', '.fmt', '.aux'}
            for name in names:
                path = Path(name)
                assert not path.is_absolute() and '..' not in path.parts, name
                assert path.name not in forbidden_names, name
                assert path.suffix.lower() not in forbidden_suffixes, name
                assert not {'context', 'scans', 'upload', '__pycache__'}.intersection(path.parts), name
            for name, digest in manifest['files'].items():
                assert hashlib.sha256(archive.read(name)).hexdigest() == digest, name
            assert archive.read(combined) == b''.join(archive.read(name) for name in pages)
            assert archive.read('records/frozen_hashes.json') == (root / 'records/frozen_hashes.json').read_bytes()
            result['archive'] = {
                'name': args.archive.name, 'members': len(names),
                'bytes': args.archive.stat().st_size, 'crc_ok': True,
                'frozen_hashes_unchanged': len(manifest['files']),
                'sha256': hashlib.sha256(args.archive.read_bytes()).hexdigest(),
            }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
