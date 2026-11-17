#!/usr/bin/env python3
"""Verify an immutable hourly archive against its checked manuscript and ledger."""
from pathlib import Path
import argparse
import csv
import hashlib
import io
import json
import re
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument('number', type=int)
args = parser.parse_args()
ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
archive = BASE / f'GT_TOWER_CHECK_checkpoint_{args.number:02d}.zip'
metadata = json.loads(archive.with_suffix('.zip.json').read_text())
sha = hashlib.sha256(archive.read_bytes()).hexdigest()
assert sha == metadata['sha256']
prefix = ROOT.name + '/'
with zipfile.ZipFile(archive) as z:
    names = z.namelist()
    assert len(names) == metadata['files']
    assert all(n.startswith(prefix) for n in names)
    forbidden = {'background', 'downloads', '__pycache__', '.texruntime', '.gapruntime'}
    assert not any(forbidden.intersection(Path(n).parts) for n in names)
    assert not any(n.endswith('.zip') for n in names)
    report = z.read(prefix + 'GT_TOWER_CHECK_report.md').decode()
    assert report.splitlines()[0] == 'INCOMPLETE'
    assert report.splitlines()[2].startswith('| Item | Statements |')
    for item in ('P.1', 'A.1', 'A.2', 'A.3', 'A.4', 'A.5', 'A.6', 'A.7',
                 'B.1', 'B.2', 'B.3', 'B.4', 'B.5', 'C.1', 'C.2', 'C.3',
                 'Lead 1', 'Lead 2', 'Lead 3', 'Lead 4', 'Lead 5', 'Lead 6'):
        assert f'| {item} |' in report
    reader = csv.DictReader(io.StringIO(z.read(prefix + 'GT_TOWER_CHECK_results.csv').decode()))
    assert reader.fieldnames == ['id', 'statement', 'status', 'where_proved',
                                 'depends_on', 'answers', 'checks', 'notes']
    rows = list(reader)
    assert len({r['id'] for r in rows}) == len(rows)
    pre = json.loads(z.read(prefix + f'notes/checkpoint_provenance/checkpoint_{args.number:02d}_prearchive.json'))
    assert len(rows) == pre['statement_count']
    statuses = {s: sum(r['status'] == s for r in rows) for s in ('Proved', 'Known', 'Open')}
    assert statuses == pre['statuses']
    paper_sha = hashlib.sha256(z.read(prefix + 'GT_TOWER_CHECK_paper.pdf')).hexdigest()
    qa = json.loads(z.read(prefix + 'notes/pdf_qa/manifest.json'))
    assert paper_sha == qa['pdf_sha256'] == pre['pdf_sha256']
    assert all(r['visually_inspected'] for r in qa['pages'])
    assert len(qa['pages']) == pre['visually_inspected_pages']
    log = z.read(prefix + 'GT_TOWER_CHECK_paper.log').decode()
    assert not re.search(r'Overfull|undefined|multiply defined|Fatal error', log)
    retention = json.loads(z.read(prefix + f'notes/checkpoint_{args.number:02d}_retention.json'))
    assert not retention['omitted']
    for record in retention['preserved_prior_bytes']:
        assert record['retained_as'] in names
    record = {
        'checkpoint': archive.name, 'zip_sha256': sha,
        'bytes': archive.stat().st_size, 'entries': len(names),
        'paper_sha256': paper_sha, 'paper_pages': qa['pdf_pages'],
        'statements': len(rows), 'statuses': statuses,
        'actual_visually_inspected_pages': len(qa['pages']),
        'previous_omissions': 0,
        'preserved_previous_versions': len(retention['preserved_prior_bytes']),
        'status': 'Verified ZIP, exact checked manuscript, complete ledger and retained prior versions.'}
path = ROOT / f'notes/checkpoint_provenance/checkpoint_{args.number:02d}_verified.json'
path.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
