"""Independently verify archive bytes, its manifest and prior-version retention."""
from pathlib import Path
import argparse, csv, hashlib, io, json
from checkpoint_archive_io import CheckpointReader, IMAGE_BUNDLE

parser = argparse.ArgumentParser()
parser.add_argument('number', type=int)
parser.add_argument('--archive', type=Path, default=None,
                    help='Optional lossless delivery encoding of the same numbered snapshot.')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
archive = args.archive or root.parent / f'LM4_SUCCESSOR_checkpoint_{args.number:02d}.zip'
prefix = 'LM4_SUCCESSOR/'
manifest_name = prefix + f'records/checkpoint_{args.number:02d}_contents_sha256.tsv'
with CheckpointReader(archive) as z:
    assert z.testzip() is None, 'CRC failure'
    names = z.names()
    assert len(names) == len(set(names)), 'Duplicate archive names'
    rows = list(csv.DictReader(io.StringIO(z.read(manifest_name).decode()), delimiter='\t'))
    assert set(names) == {prefix + row['path'] for row in rows} | {manifest_name}
    for row in rows:
        data = z.read(prefix + row['path'])
        assert len(data) == int(row['bytes']), row['path']
        assert hashlib.sha256(data).hexdigest() == row['sha256'], row['path']
    if z.tar is not None:
        packaging = json.loads(z.read(prefix + f'records/checkpoint_{args.number:02d}_packaging.json'))
        assert hashlib.sha256(z.tar_bytes).hexdigest() == packaging['image_bundle_sha256']
        assert len(z.tar_bytes) == packaging['image_bundle_bytes']
        assert len(z.members) == packaging['image_paths']
    physical_entries = len(z.direct)
    retention = list(csv.DictReader(io.StringIO(z.read(prefix + 'records/checkpoint_version_retention.csv').decode())))
    for row in retention:
        assert not row['omission_reason'], row
        data = z.read(prefix + row['retained_path'])
        assert len(data) == int(row['bytes']), row
        assert hashlib.sha256(data).hexdigest() == row['sha256'], row
report = dict(archive=archive.name, bytes=archive.stat().st_size,
              sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),
              entries=len(names), physical_zip_entries=physical_entries, manifest_rows=len(rows),
              prior_entries_retained=len(retention), crc='PASS',
              every_manifest_entry='PASS', every_retained_version='PASS')
print(json.dumps(report, indent=2))
