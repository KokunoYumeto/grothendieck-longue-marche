"""Verify ZIP contents, exclusions, table counts, and frozen transcription bytes."""
import argparse, csv, hashlib, io, re, zipfile
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('archive', type=Path)
a = p.parse_args()
forbidden = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.tif', '.tiff', '.bmp', '.zip', '.pyc'}
with zipfile.ZipFile(a.archive) as z:
    names = z.namelist()
    assert len(names) == len(set(names)), 'Duplicate archive entries'
    assert z.testzip() is None, 'CRC failure'
    assert all(Path(n).suffix.lower() not in forbidden for n in names)
    assert all('__pycache__' not in Path(n).parts for n in names)
    assert all(not n.startswith('/') and '..' not in Path(n).parts for n in names)
    assert all(not n.startswith(('source/', 'upload/', 'views/')) for n in names)
    log = z.read('progress.log').decode()
    hashes = {name: digest for digest, name in re.findall(r'^([0-9a-f]{64})  (.+)$', log, re.M)}
    assert len(hashes) == 26
    for name, digest in hashes.items():
        assert hashlib.sha256(z.read(name)).hexdigest() == digest, name
    pages = sorted(n for n in names if n.startswith('pages/') and n.endswith('.tex'))
    assert len(pages) == 25
    assert z.read('SP63_C13_15_transcription.tex') == b'\n'.join(z.read(n) for n in pages)
    for name, delimiter, expected in [
        ('decisions.tsv', '\t', 77),
        ('SP63_C13_15_collation.tsv', '\t', 410),
        ('SP63_C13_15_inventory.csv', ',', 593),
        ('CHECK_EVENTS.tsv', '\t', 14),
    ]:
        rows = list(csv.DictReader(io.StringIO(z.read(name).decode()), delimiter=delimiter))
        assert len(rows) == expected, (name, len(rows))
    assert 'RESULT (complete): 0 error(s), 0 pending/warning item(s).' in z.read('mechanical_validation.txt').decode()
    assert 'all 26 frozen transcription SHA-256 hashes unchanged' in log
print(f'Archive verified: {len(names)} files; 25 pages; all 26 frozen hashes match; CRC and exclusions pass.')
