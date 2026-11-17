"""Independently verify restored immutable ZIPs and their internal manifests."""
from pathlib import Path
import csv, hashlib, io, json, zipfile

root = Path(__file__).resolve().parents[1]
expected = {
    1: (44814828, '0a61367214c199870d0d9a18af84ce9394e7a1697b34b9aff47c41d726ebcc77'),
    2: (58136845, '1035ad953059016e1bc103f9d1b9fd01fb90f61fbde3d976979eceb7a31e376a'),
    3: (75537887, 'c853ebc2ba76430b6ac781a262987ed0b7bb64ab1741498f1cac7470ddc2f20d'),
    4: (91147760, '774a5dc89565efcaa970d69ea829027544c70e3b6b2cde788ab18f7f609f2f80'),
    5: (110861605, '2b5f8ab2b5c933fe3d082a7e58297496a1b9057a16bab752b56c451ee13336c3'),
    6: (128721004, '177d897174cbc86dbce8c535d0adb55cf18cbd35244688897b3afaf1814885a8'),
}
results = []
for number, (size, sha) in expected.items():
    path = root.parent / f'LM4_SUCCESSOR_checkpoint_{number:02d}.zip'
    assert path.stat().st_size == size, path
    assert hashlib.sha256(path.read_bytes()).hexdigest() == sha, path
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None, path
        manifest = f'LM4_SUCCESSOR/records/checkpoint_{number:02d}_contents_sha256.tsv'
        rows = list(csv.DictReader(io.StringIO(archive.read(manifest).decode()), delimiter='\t'))
        named = {manifest}
        for row in rows:
            name = 'LM4_SUCCESSOR/' + row['path']
            data = archive.read(name)
            assert len(data) == int(row['bytes']), (path, name)
            assert hashlib.sha256(data).hexdigest() == row['sha256'], (path, name)
            assert name not in named, (path, name)
            named.add(name)
        assert named == set(archive.namelist()), (path, 'unmanifested entries')
        results.append(dict(checkpoint=number, filename=path.name, bytes=size,
                            sha256=sha, entries=len(named), manifest_entries=len(rows),
                            crc='PASS', all_manifest_bytes='PASS'))
report = dict(status='PASS', checkpoints=results)
(root/'records/recovered_checkpoint_integrity.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
