#!/usr/bin/env python3
"""Package frozen deliverables and work records, with coverage and CRC checks."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import zipfile
import validate_package as package

root = Path(__file__).resolve().parent.parent
archive = root.parent / 'MPL_67_002-052.zip'
if archive.exists():
    raise SystemExit('Final archive already exists; inspect it before replacing anything.')
package.require_valid(root, final=True)
items = json.loads((root/'records/research_items.json').read_text(encoding='utf-8'))
with (root/'records/context_search_ledger.tsv').open(encoding='utf-8', newline='') as handle:
    searches = {row['note_id'] for row in csv.DictReader(handle, delimiter='\t')}
assert len(items) == 76 and len({item['id'] for item in items}) == 76
assert {item['id'] for item in items} <= searches
assert all(item['context'] and item['rs'] and item['body'] for item in items)
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a', encoding='utf-8') as handle:
    handle.write('final archive snapshot cutoff ' + now + '\n')
package.verify_freeze(root, record=True)
manifest = root/'records/package_manifest.tsv'
paths = sorted(p for p in root.rglob('*') if p.is_file()
               and '__pycache__' not in p.parts and p.suffix not in {'.pyc', '.zip'}
               and p != manifest)
assert not any(p.suffix.lower() in {'.jpg', '.jpeg', '.png', '.pdf'} for p in paths)
with manifest.open('w', encoding='utf-8', newline='') as handle:
    writer = csv.writer(handle, delimiter='\t', lineterminator='\n')
    writer.writerow(['path', 'bytes', 'sha256'])
    for path in paths:
        writer.writerow([path.relative_to(root).as_posix(), path.stat().st_size,
                         hashlib.sha256(path.read_bytes()).hexdigest()])
paths = sorted(paths + [manifest])
with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipped:
    for path in paths:
        zipped.write(path, path.relative_to(root).as_posix())
with zipfile.ZipFile(archive, 'r') as zipped:
    expected = [path.relative_to(root).as_posix() for path in paths]
    assert zipped.namelist() == expected
    assert zipped.testzip() is None
    assert len([name for name in expected if name.startswith('pages/') and name.endswith('.tex')]) == 46
print(json.dumps({'archive': str(archive), 'members': len(paths),
                  'bytes': archive.stat().st_size, 'utc': now,
                  'sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
                  'coverage': 'all deliverables and records; no input sources or previous archives',
                  'crc': 'passed'}, ensure_ascii=False))
