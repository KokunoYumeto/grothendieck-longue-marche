"""Recompress saved PNG evidence without changing any decoded pixels or metadata.

Pillow is used only as a PNG encoder, with optimize=True and compress_level=9.
The candidate IDAT chunks replace the original IDAT chunks; every other original
PNG chunk is preserved byte for byte. A candidate is accepted only when IHDR
matches and reopening it confirms identical mode, size and raw-pixel SHA-256.
Existing checkpoints and non-PNG files are never touched. UTC is caller-supplied.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
from io import BytesIO
import json
import os
from pathlib import Path
import struct
import tempfile
import time

from PIL import Image


SIGNATURE = b'\x89PNG\r\n\x1a\n'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def chunks(data):
    if data[:8] != SIGNATURE:
        raise ValueError('Not a PNG')
    out = []
    position = 8
    while position < len(data):
        length = struct.unpack('>I', data[position:position + 4])[0]
        end = position + length + 12
        if end > len(data):
            raise ValueError('Truncated PNG chunk')
        out.append((data[position + 4:position + 8],
                    data[position + 8:end - 4], data[position:end]))
        position = end
    return out


def signature(data):
    with Image.open(BytesIO(data)) as image:
        image.load()
        if getattr(image, 'is_animated', False):
            raise ValueError('Animated PNG is outside the crop recompression scope')
        return image.mode, image.size, digest(image.tobytes())


def recompress(path, root):
    original = path.read_bytes()
    old_chunks = chunks(original)
    before_mode, before_size, before_raw = signature(original)
    with Image.open(BytesIO(original)) as image:
        image.load()
        encoded = BytesIO()
        image.save(encoded, format='PNG', optimize=True, compress_level=9)
    new_chunks = chunks(encoded.getvalue())
    old_ihdr = next(data for kind, data, _ in old_chunks if kind == b'IHDR')
    new_ihdr = next(data for kind, data, _ in new_chunks if kind == b'IHDR')
    row = {
        'path': str(path.relative_to(root)),
        'before_bytes': len(original),
        'before_file_sha256': digest(original),
        'before_mode': before_mode,
        'before_size': list(before_size),
        'before_raw_pixel_sha256': before_raw,
    }
    if old_ihdr != new_ihdr:
        row.update(status='unchanged: encoder changed IHDR', after_bytes=len(original),
                   after_file_sha256=row['before_file_sha256'], after_mode=before_mode,
                   after_size=list(before_size), after_raw_pixel_sha256=before_raw,
                   pixels_verified=True, non_IDAT_chunks_preserved=True, saved_bytes=0)
        return row
    # Palette entries affect decoded colour despite the same indexed bytes.
    old_palette = [data for kind, data, _ in old_chunks if kind == b'PLTE']
    new_palette = [data for kind, data, _ in new_chunks if kind == b'PLTE']
    if old_palette != new_palette:
        row.update(status='unchanged: encoder changed palette', after_bytes=len(original),
                   after_file_sha256=row['before_file_sha256'], after_mode=before_mode,
                   after_size=list(before_size), after_raw_pixel_sha256=before_raw,
                   pixels_verified=True, non_IDAT_chunks_preserved=True, saved_bytes=0)
        return row
    compressed_chunks = b''.join(raw for kind, _, raw in new_chunks if kind == b'IDAT')
    candidate_parts = [SIGNATURE]
    inserted = False
    for kind, _, raw in old_chunks:
        if kind == b'IDAT':
            if not inserted:
                candidate_parts.append(compressed_chunks)
                inserted = True
        else:
            candidate_parts.append(raw)
    candidate = b''.join(candidate_parts)
    after_mode, after_size, after_raw = signature(candidate)
    if (after_mode, after_size, after_raw) != (before_mode, before_size, before_raw):
        raise ValueError('Candidate decoded-pixel verification failed: ' + str(path))
    if [raw for kind, _, raw in chunks(candidate) if kind != b'IDAT'] != [
            raw for kind, _, raw in old_chunks if kind != b'IDAT']:
        raise ValueError('Ancillary/critical metadata preservation failed: ' + str(path))
    smaller = len(candidate) < len(original)
    status = 'replaced' if smaller else 'unchanged: candidate not smaller'
    final_data = candidate if smaller else original
    if smaller:
        if digest(path.read_bytes()) != row['before_file_sha256']:
            raise ValueError('Source changed concurrently; refusing replacement: ' + str(path))
        fd, temporary = tempfile.mkstemp(prefix='.' + path.name + '.', suffix='.tmp', dir=path.parent)
        try:
            with os.fdopen(fd, 'wb') as stream:
                stream.write(candidate)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, path)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
        # Verify the actual final on-disk file, not only the in-memory candidate.
        actual = path.read_bytes()
        if digest(actual) != digest(candidate) or signature(actual) != (
                before_mode, before_size, before_raw):
            raise ValueError('Post-replacement verification failed: ' + str(path))
    row.update(status=status, after_bytes=len(final_data),
               after_file_sha256=digest(final_data), after_mode=after_mode,
               after_size=list(after_size), after_raw_pixel_sha256=after_raw,
               pixels_verified=True, non_IDAT_chunks_preserved=True,
               saved_bytes=len(original) - len(final_data))
    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--utc', required=True)
    parser.add_argument('--workers', type=int, default=2)
    args = parser.parse_args()
    if args.report.exists():
        raise SystemExit('Refusing to overwrite an earlier compression report')
    root = args.root.resolve()
    paths = sorted((root / 'crops').rglob('*.png'))
    started = time.monotonic()
    report = {
        'started_utc': args.utc,
        'method': 'Pillow PNG optimize=True, compress_level=9; only IDAT chunks replaced; all other original PNG chunks preserved.',
        'scope': 'Snapshot of existing saved crop PNGs; source scans, page text, sealed readings, and checkpoint ZIPs untouched.',
        'snapshot_files': len(paths),
        'files': [],
        'errors': [],
    }
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        jobs = {pool.submit(recompress, path, root): path for path in paths}
        for index, job in enumerate(as_completed(jobs), 1):
            try:
                report['files'].append(job.result())
            except Exception as error:
                report['errors'].append({'path': str(jobs[job].relative_to(root)), 'error': str(error)})
            if index % 50 == 0:
                print(json.dumps({'processed': index, 'total': len(paths),
                                  'saved_bytes': sum(r['saved_bytes'] for r in report['files']),
                                  'errors': len(report['errors'])}), flush=True)
    report['files'].sort(key=lambda row: row['path'])
    report['before_bytes'] = sum(row['before_bytes'] for row in report['files'])
    report['after_bytes'] = sum(row['after_bytes'] for row in report['files'])
    report['saved_bytes'] = report['before_bytes'] - report['after_bytes']
    report['replaced_files'] = sum(row['status'] == 'replaced' for row in report['files'])
    report['elapsed_seconds'] = round(time.monotonic() - started, 3)
    report['all_verified'] = not report['errors'] and len(report['files']) == len(paths)
    report['current_crop_directory_bytes'] = sum(path.stat().st_size for path in (root / 'crops').rglob('*') if path.is_file())
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({key: value for key, value in report.items() if key not in ('files', 'method', 'scope')}, ensure_ascii=False), flush=True)
    if report['errors']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
