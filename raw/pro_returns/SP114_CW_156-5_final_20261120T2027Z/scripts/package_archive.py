"""Package the complete current work, excluding supplied inputs and earlier ZIPs.

UTC is supplied by the authoritative clock tool. This script does not use the
execution host's wall clock for audit events. It never overwrites an archive.
"""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

p = argparse.ArgumentParser()
p.add_argument('--output', required=True)
p.add_argument('--utc', required=True)
p.add_argument('--kind', choices=['checkpoint', 'final'], required=True)
a = p.parse_args()
root = Path(__file__).resolve().parents[1]
out = Path(a.output).resolve()
if out.exists():
    raise SystemExit('Refusing to overwrite an existing archive: ' + str(out))
if root == out or root in out.parents:
    raise SystemExit('Archive must be outside the deliverable tree')
manifest_dir = root / 'review/archive_manifests'
manifest_dir.mkdir(exist_ok=True)
with (root / 'progress.log').open('a') as f:
    f.write(f'{a.kind} archive {out.name} prepared {a.utc}: all current deliverables, review records, scripts, and saved crops; supplied inputs and earlier ZIPs excluded.\n')
files = sorted(q for q in root.rglob('*') if q.is_file()
               and q.suffix.lower() != '.zip' and '__pycache__' not in q.parts)
manifest = {
    'archive': out.name, 'kind': a.kind, 'utc': a.utc,
    'input_policy': 'Supplied scans, witnesses, prompt attachments and source context excluded. No earlier ZIPs included.',
    'files_before_manifest': [
        {'path': str(q.relative_to(root)), 'bytes': q.stat().st_size,
         'sha256': hashlib.sha256(q.read_bytes()).hexdigest()} for q in files
    ]
}
mp = manifest_dir / (out.stem + '.json')
mp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
files.append(mp)
out.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(out, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for q in sorted(set(files)):
        z.write(q, str(q.relative_to(root)))
with zipfile.ZipFile(out) as z:
    bad = z.testzip()
    if bad:
        raise SystemExit('ZIP integrity failure at ' + bad)
result = {'archive': str(out), 'bytes': out.stat().st_size,
          'sha256': hashlib.sha256(out.read_bytes()).hexdigest(),
          'files': len(set(files)), 'zip_integrity': 'passed'}
print(json.dumps(result))
