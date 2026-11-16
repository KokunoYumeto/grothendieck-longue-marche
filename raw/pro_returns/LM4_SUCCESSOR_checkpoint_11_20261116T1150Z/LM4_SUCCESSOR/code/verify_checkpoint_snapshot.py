"""Independently verify archive bytes, its manifest and prior-version retention."""
from pathlib import Path
import argparse, csv, hashlib, io, json, zipfile

parser = argparse.ArgumentParser()
parser.add_argument('number', type=int)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
archive = root.parent / f'LM4_SUCCESSOR_checkpoint_{args.number:02d}.zip'
prefix = 'LM4_SUCCESSOR/'
manifest_name = prefix + f'records/checkpoint_{args.number:02d}_contents_sha256.tsv'
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None, 'CRC failure'
    names = [e.filename for e in z.infolist() if not e.is_dir()]
    assert len(names) == len(set(names)), 'Duplicate archive names'
    rows = list(csv.DictReader(io.StringIO(z.read(manifest_name).decode()), delimiter='\t'))
    assert set(names) == {prefix + row['path'] for row in rows} | {manifest_name}
    for row in rows:
        data = z.read(prefix + row['path'])
        assert len(data) == int(row['bytes']), row['path']
        assert hashlib.sha256(data).hexdigest() == row['sha256'], row['path']
    retention = list(csv.DictReader(io.StringIO(z.read(prefix + 'records/checkpoint_version_retention.csv').decode())))
    for row in retention:
        assert not row['omission_reason'], row
        data = z.read(prefix + row['retained_path'])
        assert len(data) == int(row['bytes']), row
        assert hashlib.sha256(data).hexdigest() == row['sha256'], row
report = dict(archive=archive.name, bytes=archive.stat().st_size,
              sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),
              entries=len(names), manifest_rows=len(rows),
              prior_entries_retained=len(retention), crc='PASS',
              every_manifest_entry='PASS', every_retained_version='PASS')
print(json.dumps(report, indent=2))
