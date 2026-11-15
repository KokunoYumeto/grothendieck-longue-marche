#!/usr/bin/env python3
"""Write a new immutable checkpoint or final archive from the complete work tree."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, zipfile

parser = argparse.ArgumentParser()
parser.add_argument('destination', type=Path)
parser.add_argument('--label', required=True)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
destination = args.destination.resolve()
if destination.exists():
    raise SystemExit('Refusing to overwrite an existing package: '+str(destination))
excluded = {'B_146_ranges', 'B_148_ranges', '__pycache__'}
files = sorted(p for p in root.rglob('*') if p.is_file()
               and not excluded.intersection(p.relative_to(root).parts)
               and p.suffix != '.zip')
manifest = root / ('package_manifest_'+args.label+'.json')
files = [p for p in files if p != manifest]
record = {
    'label': args.label,
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'excluded': {
        'B_146_ranges and B_148_ranges': 'Exact HTTP range fragments duplicated by the retained assembled original PDFs.',
        '__pycache__': 'Reproducible Python bytecode.',
        '*.zip': 'Avoid recursive inclusion of an earlier archive; all its individual substantive files are retained.'
    },
    'files': [dict(path=str(p.relative_to(root)), bytes=p.stat().st_size,
                   sha256=hashlib.file_digest(p.open('rb'), 'sha256').hexdigest())
              for p in files]
}
manifest.write_text(json.dumps(record, indent=2)+'\n')
files.append(manifest)
with zipfile.ZipFile(destination, 'x', compression=zipfile.ZIP_DEFLATED,
                     compresslevel=6, allowZip64=True) as archive:
    for p in files:
        archive.write(p, str(p.relative_to(root)))
with zipfile.ZipFile(destination) as archive:
    bad = archive.testzip()
    if bad is not None:
        raise RuntimeError('Archive CRC failed: '+bad)
print(json.dumps({'path':str(destination), 'files':len(files),
                  'bytes':destination.stat().st_size,
                  'sha256':hashlib.file_digest(destination.open('rb'), 'sha256').hexdigest()}, indent=2))
