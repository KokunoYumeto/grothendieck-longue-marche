"""Independently restore the actual checkpoint21 PNG container with system tar.

This deliberately does not import the packaging or logical-reader code.
All extracted paths are checked against the actual archived digest manifest.
"""
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
import csv
import hashlib
import io
import json
import subprocess
import tarfile
import tempfile
import zipfile

root = Path(__file__).resolve().parents[1]
archive = root.parent/'LM4_SUCCESSOR_checkpoint_21.zip'
prefix = 'LM4_SUCCESSOR/'
bundle_name = prefix+'verification_images.tar'
manifest_name = prefix+'records/checkpoint_21_contents_sha256.tsv'
with zipfile.ZipFile(archive) as z:
    rows = list(csv.DictReader(io.StringIO(z.read(manifest_name).decode()), delimiter='\t'))
    image_rows = [r for r in rows if r['path'].lower().endswith('.png')]
    expected = {prefix+r['path']:r for r in image_rows}
    assert len(expected) == len(image_rows)
    packaging = json.loads(z.read(prefix+'records/checkpoint_21_packaging.json'))
    bundle = z.read(bundle_name)
    assert hashlib.sha256(bundle).hexdigest() == packaging['image_bundle_sha256']
    assert len(bundle) == packaging['image_bundle_bytes']
    with tempfile.TemporaryDirectory(prefix='lm4-checkpoint21-system-tar-') as directory:
        temp = Path(directory)
        tar_path = temp/'verification_images.tar'
        tar_path.write_bytes(bundle)
        seen = {}
        with tarfile.open(tar_path, 'r:') as tf:
            for member in tf.getmembers():
                p = PurePosixPath(member.name)
                assert not p.is_absolute() and '..' not in p.parts
                assert p.parts[0] == 'LM4_SUCCESSOR'
                assert member.name in expected and member.name not in seen
                assert member.isfile() or member.islnk()
                if member.islnk():
                    assert member.linkname in seen and seen[member.linkname] == 'regular'
                seen[member.name] = 'regular' if member.isfile() else 'hardlink'
        assert set(seen) == set(expected)
        subprocess.run(['tar','-xf',str(tar_path)],cwd=temp,check=True)
        total_bytes = 0
        for name, row in expected.items():
            path = temp/name
            assert path.is_file() and not path.is_symlink()
            data = path.read_bytes()
            assert len(data) == int(row['bytes']), name
            assert hashlib.sha256(data).hexdigest() == row['sha256'], name
            total_bytes += len(data)
        report = {
            'archive':archive.name,
            'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
            'system_tar_restore':'PASS',
            'every_original_png_path_and_byte':'PASS',
            'image_paths':len(expected),
            'regular_image_payloads':list(seen.values()).count('regular'),
            'hardlink_image_paths':list(seen.values()).count('hardlink'),
            'logical_image_bytes':total_bytes,
            'image_bundle_sha256':hashlib.sha256(bundle).hexdigest(),
            'completed_at':datetime.now(timezone.utc).isoformat(),
            'independence':'No import of packaging or logical-reader implementation; native tar extraction.'
        }
print(json.dumps(report,indent=2))
