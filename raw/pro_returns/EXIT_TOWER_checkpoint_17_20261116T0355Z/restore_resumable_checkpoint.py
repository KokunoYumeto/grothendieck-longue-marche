#!/usr/bin/env python3
"""Restore/verify version-3 independently committed checkpoint chunks."""
import argparse
import hashlib
import json
import lzma
from pathlib import Path, PurePosixPath
import sys
import tarfile
import tempfile
import zipfile

runtime = Path(__file__).resolve().parent / 'runtime'
if runtime.is_dir():
    sys.path.insert(0, str(runtime))
from png_exact_preconditioning import restore as restore_png
from pdf_exact_preconditioning import restore as restore_pdf
from png_disk_shared_rows import Decoder


def digest(path):
    with Path(path).open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def safe(name):
    p = PurePosixPath(name)
    if p.is_absolute() or '..' in p.parts or not p.parts:
        raise ValueError('Unsafe checkpoint path')
    return Path(*p.parts)


def iter_encoded(directory, record):
    seen = set()
    for chunk in record['chunks']:
        path = Path(directory) / safe(chunk['name'])
        if path.stat().st_size != chunk['bytes'] or digest(path) != chunk['sha256']:
            raise ValueError('Chunk integrity mismatch')
        with lzma.open(path, 'rb') as f, tarfile.open(fileobj=f, mode='r|') as t:
            names = []
            for item in t:
                if not item.isfile() or item.name in seen or item.name not in record['blobs']:
                    raise ValueError('Unexpected or duplicate blob')
                desc = record['blobs'][item.name]
                if item.size != desc['encoded_bytes']:
                    raise ValueError('Tar member length mismatch')
                encoded = t.extractfile(item).read()
                if len(encoded) != desc['encoded_bytes'] or hashlib.sha256(encoded).hexdigest() != desc['encoded_sha256']:
                    raise ValueError('Encoded blob integrity mismatch')
                seen.add(item.name); names.append(item.name)
                yield item.name, desc, encoded
            if names != chunk['blobs']:
                raise ValueError('Chunk blob sequence mismatch')
    if seen != set(record['blobs']):
        raise ValueError('Missing encoded blob')


def restore(directory, destination=None, compare_source=None):
    directory = Path(directory)
    record = json.loads((directory / 'CHECKPOINT_RESUME.json').read_text())
    if record.get('encoding_version') != 3 or not record.get('complete'):
        raise ValueError('Incomplete or unsupported checkpoint')
    if destination is not None:
        destination = Path(destination)
        if destination.exists() and any(destination.iterdir()):
            raise ValueError('Restoration destination must be empty')
        destination.mkdir(parents=True, exist_ok=True)
    by_blob = {}
    for name, info in record['members'].items():
        safe(name)
        by_blob.setdefault(info['blob'], []).append((name, info))
    source = zipfile.ZipFile(compare_source) if compare_source else None
    restored = 0
    try:
        with tempfile.TemporaryDirectory(prefix='checkpoint_rows_') as temp:
            with Decoder(Path(temp) / 'rows.sqlite3') as rows:
                for name, desc, encoded in iter_encoded(directory, record):
                    codec = desc['codec']
                    if codec == 'png-disk-rows-v2':
                        data = restore_png(rows.decode(encoded))
                    elif codec == 'png-idat-v1':
                        data = restore_png(encoded)
                    elif codec == 'pdf-zlib-v1':
                        data = restore_pdf(encoded)
                    elif codec == 'original':
                        data = encoded
                    else:
                        raise ValueError('Unknown exact codec')
                    sha = hashlib.sha256(data).hexdigest()
                    for original, info in by_blob[name]:
                        if len(data) != info['bytes'] or sha != info['sha256']:
                            raise ValueError('Restored original integrity mismatch: ' + original)
                        if source is not None and source.read(original) != data:
                            raise ValueError('Original byte comparison failed: ' + original)
                        if destination is not None:
                            path = destination / safe(original)
                            path.parent.mkdir(parents=True, exist_ok=True)
                            with path.open('xb') as f:
                                f.write(data)
                        restored += 1
                if rows.count != record['row_count'] or rows.blocks != record['row_blocks']:
                    raise ValueError('Final row dictionary mismatch')
        if restored != len(record['members']):
            raise ValueError('Incomplete member recovery')
        if source is not None:
            names = [i.filename for i in source.infolist() if not i.is_dir()]
            if len(names) != len(set(names)) or set(names) != set(record['members']):
                raise ValueError('Original path set mismatch')
    finally:
        if source is not None:
            source.close()
    return {'all_original_members_verified': True, 'retained_members': restored,
            'unique_blobs_verified': len(by_blob), 'chunks_verified': len(record['chunks']),
            'exact_source_comparison': compare_source is not None}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('directory', nargs='?', type=Path, default=Path(__file__).resolve().parent)
    p.add_argument('destination', nargs='?', type=Path)
    p.add_argument('--verify-only', action='store_true')
    p.add_argument('--compare-source', type=Path)
    a = p.parse_args()
    destination = None if a.verify_only else (a.destination or a.directory / 'restored_checkpoint')
    print(json.dumps(restore(a.directory, destination, a.compare_source), indent=2))
