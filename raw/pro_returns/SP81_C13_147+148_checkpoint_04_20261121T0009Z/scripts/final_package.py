"""Package only deliverables and work evidence; original attachments and halves stay out."""
from pathlib import Path
import json, zipfile, hashlib

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'work/manifest.json').read_text())
assert len(manifest) == 24
validation = json.loads((root / 'work/final_validation.json').read_text())
assert validation['approved_pages'] == 24 and validation['audited_pages'] == 24
assert not validation['errors'], 'Resolve the completeness/evidence gate before packaging.'
for m in manifest:
    page = m['page']
    report = json.loads((root / 'work' / (page + '_final.json')).read_text())
    assert report.get('root_approved') and report.get('audit'), page
    for suffix in ('boxes.tsv', 'first.tsv', 'second.tsv', 'comparison.json', 'adjudications.tsv'):
        assert (root / 'second' / (page + '_' + suffix)).is_file(), (page, suffix)
frozen = json.loads((root / 'work/frozen_hashes.json').read_text())['hashes']
for name, digest in frozen.items():
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest, name
assert 'frozen hashes verified unchanged' in (root / 'progress.log').read_text()
files = sorted(p for p in root.rglob('*') if p.is_file() and 'packets' not in p.relative_to(root).parts and '__pycache__' not in p.parts)
assert not any(p.suffix.lower() == '.zip' for p in files)
# JPEG display encodings of saved evidence crops are work documentation and
# occur in earlier checkpoints. Original scans, witnesses and halves reside
# outside edition; no file from those input directories is selected here.
assert not any(any(part in ('source', 'halves', 'upload') for part in p.relative_to(root).parts)
               for p in files)
out = root.parent / 'deliveries/SP81_C13_147+148.zip'
out.parent.mkdir(exist_ok=True)
assert not out.exists(), 'Do not silently overwrite a final package.'
with zipfile.ZipFile(out, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for p in files: z.write(p, p.relative_to(root).as_posix())
with zipfile.ZipFile(out) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(files)
print(json.dumps({'file': str(out), 'bytes': out.stat().st_size, 'files': len(files), 'sha256': hashlib.sha256(out.read_bytes()).hexdigest()}))
