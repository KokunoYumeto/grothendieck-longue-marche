#!/usr/bin/env python3
"""Freeze, validate, and archive a uniquely numbered research checkpoint.

Run ``prepare NN`` in the active project, build and inspect the frozen
copy, then run ``pack NN`` in the active project.  No existing checkpoint
is overwritten.  Mathematical verification remains in the cited programs.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import shutil
import zipfile

root = Path(__file__).resolve().parent.parent
workspace = root.parent
parser = argparse.ArgumentParser()
parser.add_argument('action', choices=['prepare', 'pack'])
parser.add_argument('number', type=int)
args = parser.parse_args()
stem = f'LM7_PUSH_checkpoint_{args.number:02d}'
frozen = workspace / 'checkpoint_work' / stem / 'LM7_PUSH'
archive = workspace / (stem + '.zip')
assert not archive.exists(), 'An earlier checkpoint may not be overwritten.'

if args.action == 'prepare':
    assert not frozen.exists(), 'The frozen copy already exists.'
    shutil.copytree(root, frozen, ignore=shutil.ignore_patterns(
        'build', '__pycache__', '*.pyc', 'renders',
        'library_file_transfer.py', 'library_identity.json'))
    inputs = frozen / 'inputs'
    inputs.mkdir(exist_ok=True)
    attached = workspace / 'upload' / 'LM7_PUSH_background.zip'
    if attached.exists():
        shutil.copy2(attached, inputs / attached.name)
    (frozen / 'research' / 'checkpoint_scope.json').write_text(json.dumps({
        'checkpoint': stem,
        'scope': 'Active research checkpoint; task remains INCOMPLETE.',
        'frozen_from': str(root),
        'earlier_checkpoint_omissions': [],
    }, indent=2) + '\n')
    print(json.dumps({'frozen_project': str(frozen), 'archive': str(archive)}))
else:
    summary = json.loads((frozen / 'build' / 'typesetting_summary.json').read_text())
    assert summary['overfull_boxes_over_2pt'] == 0
    assert not summary['undefined_citations']
    assert not summary['undefined_references']
    qa = json.loads((frozen / 'research' / 'visual_qa.json').read_text())
    pdf = frozen / 'LM7_PUSH_paper.pdf'
    assert qa['pdf_sha256'] == hashlib.sha256(pdf.read_bytes()).hexdigest()
    assert qa['visually_inspected']
    with (frozen / 'LM7_PUSH_results.csv').open() as stream:
        rows = list(csv.DictReader(stream))
    assert len({r['id'] for r in rows}) == len(rows)
    ledger = json.loads((frozen / 'research' / 'task_ledger.json').read_text())
    assert len(ledger) == 29
    assert (frozen / 'LM7_PUSH_report.md').read_text().startswith('INCOMPLETE\n')
    def include(path):
        rel = path.relative_to(frozen)
        if '__pycache__' in rel.parts or 'renders' in rel.parts:
            return False
        if path.suffix == '.pyc':
            return False
        if rel.parts[0] == 'build':
            return path.suffix in {'.log', '.json', '.blg', '.bbl'}
        return path.is_file()
    paths = sorted(p for p in frozen.rglob('*') if p.is_file() and include(p))
    manifest = frozen / 'research' / 'checkpoint_manifest.tsv'
    paths = [p for p in paths if p != manifest]
    lines = ['path\tsize_bytes\tsha256']
    for path in paths:
        data = path.read_bytes()
        lines.append(f'{path.relative_to(frozen)}\t{len(data)}\t{hashlib.sha256(data).hexdigest()}')
    manifest.write_text('\n'.join(lines) + '\n')
    paths.append(manifest)
    with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for path in paths:
            z.write(path, 'LM7_PUSH/' + str(path.relative_to(frozen)))
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        assert len(z.namelist()) == len(paths)
    result = {
        'archive': str(archive), 'files': len(paths),
        'numbered_statements': len(rows), 'coverage_rows': len(ledger),
        'size_bytes': archive.stat().st_size,
        'sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
        'all_zip_entries_verified': True,
    }
    (workspace / (stem + '_validation.json')).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
