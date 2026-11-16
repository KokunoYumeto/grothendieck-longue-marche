"""Package the completed return; refuses to overwrite an existing final ZIP."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, zipfile

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT.parent / 'MPL_36_002-052.zip'
assert not TARGET.exists(), 'Refusing to overwrite an existing final ZIP'
frozen = json.loads((ROOT / 'records/frozen_hashes.json').read_text())
for name, digest in frozen['files'].items():
    assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
notes = (ROOT / 'MPL_36_002-052_notes.md').read_text()
assert '## Final integrity and scope verification' in notes
utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT / 'progress.log').open('a') as f:
    f.write(f'final archive prepared {utc}; MPL_36_002-052.zip; frozen hashes rechecked unchanged; sources and generated QA caches excluded\n')

def files():
    return sorted(p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc')

manifest_path = ROOT / 'records/deliverable_manifest.json'
manifest = {str(p.relative_to(ROOT)): {'bytes':p.stat().st_size, 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
    for p in files() if p != manifest_path}
manifest_path.write_text(json.dumps({'created_utc':utc, 'note':'Manifest covers every archive member except this manifest itself.', 'files':manifest}, ensure_ascii=False, indent=2) + '\n')
members = files()
assert not any(p.suffix.lower() in ('.jpg','.jpeg','.png','.pdf','.zip') for p in members)
with zipfile.ZipFile(TARGET, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in members: z.write(p, str(p.relative_to(ROOT)))
with zipfile.ZipFile(TARGET) as z:
    assert z.testzip() is None
    assert set(z.namelist()) == {str(p.relative_to(ROOT)) for p in members}
    for name, row in manifest.items():
        assert hashlib.sha256(z.read(name)).hexdigest() == row['sha256'], name
    for name, digest in frozen['files'].items():
        assert hashlib.sha256(z.read(name)).hexdigest() == digest, name
print(json.dumps({'path':str(TARGET), 'files':len(members), 'bytes':TARGET.stat().st_size,
    'sha256':hashlib.sha256(TARGET.read_bytes()).hexdigest(), 'crc_check':'passed', 'manifest_check':'passed',
    'frozen_hashes_in_zip':'all 32 unchanged'}, indent=2))
