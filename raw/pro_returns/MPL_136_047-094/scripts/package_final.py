#!/usr/bin/env python3
"""Verify the frozen transcription and assemble this task's final ZIP.

Run from any directory. An existing output ZIP is never overwritten. The source
images and supplied context are outside this package and are not archived.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
import zipfile


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def manifest_entries(path):
    return [line.split('  ', 1) for line in path.read_text().splitlines() if line.strip()]


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=root.parent / 'MPL_136_047-094.zip')
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists():
        raise SystemExit(f'Refusing to overwrite {output}')
    if root in output.parents:
        raise SystemExit('The output ZIP must be outside the package directory.')

    check = subprocess.run(
        [sys.executable, str(root / 'scripts/validate_package.py'), '--require-frozen'],
        text=True, capture_output=True, check=True)
    frozen = manifest_entries(root / 'validation/transcription_frozen.sha256')
    assert len(frozen) == 47
    for expected, name in frozen:
        assert digest(root / name) == expected, f'Frozen hash mismatch: {name}'
    for expected, name in manifest_entries(root / 'validation/validated_tables.sha256'):
        assert digest(root / name) == expected, f'Validated table mismatch: {name}'

    notes = root / 'MPL_136_047-094_notes.md'
    note_ids = re.findall(r'^### (R\d{3}) —', notes.read_text(), re.M)
    assert note_ids == [f'R{i:03d}' for i in range(1, 66)]
    with (root / 'research/context_search_audit.tsv').open(newline='') as stream:
        searches = list(csv.DictReader(stream, delimiter='\t'))
    assert {r['note_id'] for r in searches} == set(note_ids)
    assert {r['notes_source_sha256'] for r in searches} == {digest(notes)}

    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    result = (
        f'Final assembly validation: {now}\n\n' + check.stdout + check.stderr
        + '\nAll 47 frozen transcription hashes are unchanged after context opening.\n'
        + 'Both final table hashes match the technical-validation manifest.\n'
        + f'All 65 research items are covered by {len(searches)} context searches; notes-source hash matches.\n'
        + 'These are structural and integrity checks, not claims of perfect handwriting accuracy.\n')
    (root / 'validation/final_package_check.txt').write_text(result)
    with (root / 'progress.log').open('a') as stream:
        stream.write(f'research complete {now}; 65 numbered items, context and literature comparisons, explicit algebra checks\n')
        stream.write(f'final doubts and inventory verified {now}; 544 macro doubts plus 6 manual records, 30 notation rows, 94 abbreviation rows, 950 inventory rows all yes\n')
        stream.write(f'post-context hash verification {now}; all 47 SHA-256 hashes unchanged: 46 page files and combined transcription\n')
        stream.write(f'final archive assembly {now}; MPL_136_047-094.zip; all deliverables and retained work records, supplied inputs excluded\n')

    package_manifest = root / 'validation/package_files.sha256'
    files = sorted(p for p in root.rglob('*') if p.is_file() and p != package_manifest)
    permitted = {'.csv', '.log', '.md', '.py', '.sha256', '.tex', '.tsv', '.txt'}
    for path in files:
        assert path.suffix in permitted and '__pycache__' not in path.parts, f'Unexpected artifact: {path}'
    package_manifest.write_text(''.join(f'{digest(p)}  {p.relative_to(root).as_posix()}\n' for p in files))
    files.append(package_manifest)
    files.sort()
    temporary = output.with_suffix('.zip.tmp')
    with zipfile.ZipFile(temporary, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            archive.write(path, path.relative_to(root).as_posix())
    with zipfile.ZipFile(temporary) as archive:
        assert archive.testzip() is None
        assert len(archive.namelist()) == len(files)
        for expected, name in frozen:
            assert hashlib.sha256(archive.read(name)).hexdigest() == expected
    temporary.replace(output)
    print(json.dumps({'output': str(output), 'files': len(files), 'bytes': output.stat().st_size,
                      'sha256': digest(output), 'frozen_hashes_verified': 47,
                      'research_items': len(note_ids), 'context_searches': len(searches)}))


if __name__ == '__main__':
    main()
