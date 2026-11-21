"""Freeze image-only audit inputs after all supplied pages have been accepted."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import assemble
import validate

BASE = Path(__file__).resolve().parents[1]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def prepare():
    target = BASE / 'second' / 'input_manifest.json'
    if target.exists():
        raise ValueError('Audit inputs are already frozen')
    reports = assemble.load_reports()
    assert len(reports) == 23
    assert not validate.validate()['errors']
    assert all(r.get('accepted_utc') for r in reports)
    assert not list((BASE / 'second').glob('*_second.tsv'))
    assemble.build()
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    manifest = {'frozen_utc': stamp, 'pages': {}}
    for report in reports:
        page = report['page']
        manifest['pages'][page] = {
            'first_reader': report['reader'],
            'boxes_sha256': sha(BASE / 'second' / f'{page}_boxes.tsv'),
            'first_sha256': sha(BASE / 'second' / f'{page}_first.tsv'),
            'first_page_sha256': sha(BASE / 'pages' / f'{page}.tex'),
        }
    target.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    with (BASE / 'progress.log').open('a') as log:
        log.write(f'audit inputs frozen {stamp}: 23 page box lists and first readings; input_manifest.json records SHA-256\n')
    print(json.dumps({'frozen_utc': stamp, 'pages': len(reports)}))

if __name__ == '__main__':
    prepare()
