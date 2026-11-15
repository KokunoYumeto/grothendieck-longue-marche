#!/usr/bin/env python3
"""Restore or exhaustively verify a reversible EXIT_TOWER checkpoint encoding."""
import argparse, hashlib, json, lzma, tarfile, zipfile
from pathlib import Path, PurePosixPath
from png_exact_preconditioning import restore as restore_png
from pdf_exact_preconditioning import restore as restore_pdf

def safe_relative(name):
    p = PurePosixPath(name)
    if p.is_absolute() or '..' in p.parts or not p.parts:
        raise ValueError(f'Unsafe member name: {name!r}')
    return Path(*p.parts)

def restore(directory, destination=None, compare_source=None):
    directory = Path(directory)
    record = json.loads((directory/'TRANSFER_ENCODING.json').read_text())
    if record['encoding_version'] != 2:
        raise ValueError('Unsupported checkpoint encoding version')
    if destination is not None:
        destination = Path(destination)
        if destination.exists() and any(destination.iterdir()):
            raise ValueError('Restoration destination must be empty')
        destination.mkdir(parents=True, exist_ok=True)
    by_blob = {}
    for name, info in record['members'].items():
        safe_relative(name)
        by_blob.setdefault(info['blob'], []).append((name, info))
    payload = directory/record['payload_file']
    if hashlib.file_digest(payload.open('rb'),'sha256').hexdigest() != record['payload_sha256']:
        raise ValueError('Payload hash mismatch')
    original = zipfile.ZipFile(compare_source) if compare_source else None
    seen = set()
    restored = 0
    try:
        # LZMAFile handles standard concatenated XZ streams. tarfile's own
        # r|xz adapter uses a single LZMADecompressor and stops at stream one.
        with lzma.open(payload, 'rb') as decoded, tarfile.open(fileobj=decoded, mode='r|') as t:
            for item in t:
                if not item.isfile() or item.name not in by_blob or item.name in seen:
                    raise ValueError('Unexpected encoded member')
                encoded = t.extractfile(item).read()
                description = record['blobs'][item.name]
                if len(encoded) != description['encoded_bytes']:
                    raise ValueError('Encoded member length mismatch')
                if hashlib.sha256(encoded).hexdigest() != description['encoded_sha256']:
                    raise ValueError('Encoded member hash mismatch')
                if description['codec'] == 'png-idat-v1':
                    data = restore_png(encoded)
                elif description['codec'] == 'pdf-zlib-v1':
                    data = restore_pdf(encoded)
                elif description['codec'] == 'original':
                    data = encoded
                else:
                    raise ValueError('Unknown reversible member codec')
                digest = hashlib.sha256(data).hexdigest()
                for name, info in by_blob[item.name]:
                    if len(data) != info['bytes'] or digest != info['sha256']:
                        raise ValueError(f'Original member verification failed: {name}')
                    if original is not None and original.read(name) != data:
                        raise ValueError(f'Exact source byte comparison failed: {name}')
                    if destination is not None:
                        path = destination/safe_relative(name)
                        path.parent.mkdir(parents=True, exist_ok=True)
                        path.write_bytes(data)
                    restored += 1
                seen.add(item.name)
        if seen != set(by_blob) or restored != record['retained_members']:
            raise ValueError('Incomplete restored checkpoint')
        if original is not None:
            if set(record['members']) != {i.filename for i in original.infolist() if not i.is_dir()}:
                raise ValueError('Original path set mismatch')
    finally:
        if original is not None:
            original.close()
    return {'all_original_members_verified': True, 'retained_members': restored,
        'unique_blobs_verified': len(seen), 'exact_source_comparison': compare_source is not None,
        'destination': str(destination.resolve()) if destination is not None else None}

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('directory', type=Path, nargs='?', default=Path(__file__).resolve().parent)
    p.add_argument('destination', type=Path, nargs='?')
    p.add_argument('--verify-only', action='store_true')
    p.add_argument('--compare-source', type=Path)
    a = p.parse_args()
    destination = None if a.verify_only else (a.destination or a.directory/'restored_checkpoint')
    print(json.dumps(restore(a.directory, destination, a.compare_source), indent=2))
