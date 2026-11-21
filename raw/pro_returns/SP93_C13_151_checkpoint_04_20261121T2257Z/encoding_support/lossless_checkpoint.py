#!/usr/bin/env python3
"""Stage a pixel-identical WebP encoding of a frozen PNG checkpoint.

This never edits the input ZIP or work tree. Output must be a new directory.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path, PurePosixPath
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib
import json
import os
import re
import shutil
import sys
import time

from PIL import Image, __version__ as pillow_version, features

SCHEMA = 'sp93-lossless-webp-v1'
TEXT_SUFFIXES = {'.json', '.md', '.csv', '.tsv'}
SUPPORT = 'encoding_support'

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def file_sha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as source:
        for block in iter(lambda: source.read(8 * 1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()

def safe_name(name: str) -> str:
    p = PurePosixPath(name)
    if not name or p.is_absolute() or '..' in p.parts or '\\' in name or str(p) != name:
        raise ValueError(f'Unsafe source member: {name!r}')
    return name

def frozen(name: str) -> bool:
    base = PurePosixPath(name).name
    return base == 'first_reading_manifest.json' or base.endswith(('_first.tsv', '_second.tsv', '_boxes.tsv'))

class Source:
    def __init__(self, input_zip: Path | None, work_tree: Path | None):
        self.archive = None
        self.zip_metadata = {}
        if input_zip is not None:
            self.path = input_zip.resolve(strict=True)
            self.kind = 'zip'
            self.original_sha256 = file_sha(self.path)
            self.original_size = self.path.stat().st_size
            self.archive = ZipFile(self.path)
            entries = [entry for entry in self.archive.infolist() if not entry.is_dir()]
            names = [safe_name(entry.filename) for entry in entries]
            if len(set(names)) != len(names):
                raise ValueError('Input ZIP has duplicate member names')
            self.names = sorted(names)
            self.zip_metadata = {entry.filename: entry for entry in entries}
        else:
            self.path = work_tree.resolve(strict=True)
            if not self.path.is_dir():
                raise ValueError('Work tree must be a directory')
            self.kind = 'work_tree'
            self.original_sha256 = None
            self.original_size = None
            self.names = []
            for path in sorted(self.path.rglob('*')):
                if path.is_symlink():
                    raise ValueError(f'Symlinks are not accepted in work-tree input: {path}')
                if path.is_file() and path.suffix.lower() != '.zip' and '__pycache__' not in path.parts:
                    self.names.append(safe_name(path.relative_to(self.path).as_posix()))
        if any(name.startswith(SUPPORT + '/') for name in self.names):
            raise ValueError('Input already contains encoding_support; select the original PNG snapshot/work tree')

    def read(self, name: str) -> bytes:
        return self.archive.read(name) if self.archive is not None else (self.path / name).read_bytes()

    def close(self):
        if self.archive is not None:
            self.archive.close()

def write_bytes(root: Path, name: str, data: bytes):
    target = root / safe_name(name)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    inputs = parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument('--input-zip', type=Path)
    inputs.add_argument('--work-tree', type=Path)
    parser.add_argument('--output-dir', type=Path, required=True, help='Must not already exist')
    parser.add_argument('--archive-name', help='Defaults to the input ZIP basename; required for work trees')
    parser.add_argument('--expected-sha256', help='Optional exact input ZIP hash guard')
    parser.add_argument('--snapshot-created-utc', help='Original scheduled checkpoint time, if known')
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--webp-method', type=int, choices=range(7), default=4)
    parser.add_argument('--max-bytes', type=int, default=536870912)
    args = parser.parse_args()
    if args.workers < 1 or args.workers > 16:
        raise ValueError('Workers must be between 1 and 16')
    if not features.check('webp'):
        raise ValueError('This Pillow installation lacks WebP support')
    restore_source = Path(__file__).with_name('restore_png.py')
    if not restore_source.is_file():
        raise ValueError('The sibling restore_png.py helper is required')
    archive_name = args.archive_name or (args.input_zip.name if args.input_zip else None)
    if not archive_name or Path(archive_name).name != archive_name or not archive_name.endswith('.zip'):
        raise ValueError('Archive name must be a plain .zip basename')
    output = args.output_dir.resolve()
    if output.exists():
        raise ValueError(f'Output directory already exists; refusing overwrite: {output}')
    source = Source(args.input_zip, args.work_tree)
    if source.kind == 'work_tree' and (output == source.path or source.path in output.parents):
        raise ValueError('Output directory must be outside the work tree')
    if args.expected_sha256 and source.original_sha256 != args.expected_sha256:
        raise ValueError('Input ZIP hash differs from --expected-sha256')
    crop_names = [name for name in source.names if name.startswith('crops/') and name.lower().endswith('.png')]
    if not crop_names:
        raise ValueError('No crops/*.png evidence files found')
    mapping = {name: str(PurePosixPath(name).with_suffix('.webp')) for name in crop_names}
    if any(value in source.names for value in mapping.values()):
        raise ValueError('An input WebP file collides with a proposed crop counterpart')
    old_bases = [PurePosixPath(name).name for name in crop_names]
    if len(set(old_bases)) != len(old_bases):
        raise ValueError('Duplicate crop basenames require a more specific migration policy')
    base_map = {PurePosixPath(old).name: PurePosixPath(new).name for old, new in mapping.items()}
    alternative = '|'.join(re.escape(name) for name in sorted(base_map, key=len, reverse=True))
    token_pattern = re.compile(r'(?<![A-Za-z0-9_.-])(' + alternative + r')(?![A-Za-z0-9_.-])')
    absolute_pattern = re.compile(r'(?<![A-Za-z0-9_:/.-])/[A-Za-z0-9_./-]*/crops/(' + alternative + r')(?![A-Za-z0-9_.-])')
    output.mkdir(parents=True)
    payload = output / 'payload'
    payload.mkdir()
    started = time.perf_counter()
    manifest = {
        'schema': SCHEMA,
        'created_at_utc': datetime.now(timezone.utc).isoformat(),
        'source': {'kind': source.kind, 'path': str(source.path), 'archive_basename': archive_name,
                   'original_archive_sha256': source.original_sha256,
                   'original_archive_size_bytes': source.original_size,
                   'scheduled_snapshot_created_utc': args.snapshot_created_utc,
                   'source_file_count': len(source.names)},
        'encoder': {'format': 'WEBP', 'lossless': True, 'quality': 100, 'method': args.webp_method,
                    'exact': True, 'pillow_version': pillow_version, 'libwebp_version': features.version('webp')},
        'crops': [], 'frozen_files': [], 'reference_changes': [], 'preserved_files': [],
    }

    def convert_crop(name):
        data = source.read(name)
        with Image.open(BytesIO(data)) as image:
            image.load()
            if image.format != 'PNG' or image.mode != 'RGB' or image.info:
                raise ValueError(f'Unreviewed image mode/metadata; refusing conversion: {name}, {image.mode}, {list(image.info)}')
            pixels = image.tobytes()
            target = payload / mapping[name]
            target.parent.mkdir(parents=True, exist_ok=True)
            image.save(target, format='WEBP', lossless=True, quality=100, method=args.webp_method, exact=True)
            encoded = target.read_bytes()
            with Image.open(BytesIO(encoded)) as decoded:
                decoded.load()
                if decoded.mode != 'RGB' or decoded.size != image.size or decoded.tobytes() != pixels:
                    raise ValueError(f'Exact RGB equality failed for {name}')
            return {'original_path': name, 'encoded_path': mapping[name],
                    'source_png_sha256': sha(data), 'source_png_size_bytes': len(data),
                    'webp_sha256': sha(encoded), 'webp_size_bytes': len(encoded),
                    'width': image.width, 'height': image.height, 'mode': 'RGB',
                    'rgb_sha256': sha(pixels), 'pixel_identity_verified': True,
                    'source_metadata_keys': []}

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(convert_crop, name) for name in crop_names]
        with (output / 'conversion_progress.jsonl').open('w') as progress:
            for future in as_completed(futures):
                record = future.result()
                manifest['crops'].append(record)
                progress.write(json.dumps(record, sort_keys=True) + '\n')
                progress.flush()
                count = len(manifest['crops'])
                if count % 25 == 0 or count == len(crop_names):
                    print(json.dumps({'stage': 'crop_conversion', 'completed': count, 'total': len(crop_names)}), flush=True)
    manifest['crops'].sort(key=lambda record: record['original_path'])

    for name in source.names:
        if name in mapping:
            continue
        original = source.read(name)
        delivered = original
        is_frozen = frozen(name)
        if is_frozen:
            if token_pattern.search(original.decode('utf-8')):
                raise ValueError(f'Frozen file contains a PNG crop reference that cannot be migrated: {name}')
            manifest['frozen_files'].append({'path': name, 'sha256': sha(original), 'size_bytes': len(original)})
        text_eligible = PurePosixPath(name).suffix.lower() in TEXT_SUFFIXES and not name.startswith('scripts/') and not is_frozen
        replacement_count = 0
        absolute_count = 0
        if text_eligible:
            text = original.decode('utf-8')
            def absolute_replace(match):
                nonlocal absolute_count
                absolute_count += 1
                return 'crops/' + base_map[match.group(1)]
            text = absolute_pattern.sub(absolute_replace, text)
            text, replacement_count = token_pattern.subn(lambda match: base_map[match.group(1)], text)
            delivered = text.encode('utf-8')
            if token_pattern.search(text):
                raise ValueError(f'Known PNG reference remains after staged migration: {name}')
        if delivered != original:
            backup = f'{SUPPORT}/reference_originals/{name}'
            write_bytes(payload, backup, original)
            manifest['reference_changes'].append({'path': name, 'original_sha256': sha(original),
                'delivered_sha256': sha(delivered), 'backup_path': backup,
                'basename_replacements': replacement_count, 'absolute_path_replacements': absolute_count})
        else:
            manifest['preserved_files'].append({'path': name, 'sha256': sha(original), 'size_bytes': len(original), 'frozen': is_frozen})
        write_bytes(payload, name, delivered)

    # The archived frozen files and every original non-crop byte are accounted for.
    for record in manifest['frozen_files']:
        if file_sha(payload / record['path']) != record['sha256']:
            raise ValueError(f'Frozen file changed: {record["path"]}')
    for record in manifest['reference_changes']:
        if file_sha(payload / record['backup_path']) != record['original_sha256']:
            raise ValueError(f'Reference preimage changed: {record["path"]}')
    for record in manifest['preserved_files']:
        if file_sha(payload / record['path']) != record['sha256']:
            raise ValueError(f'Preserved source file changed: {record["path"]}')
    if len(manifest['preserved_files']) + len(manifest['reference_changes']) + len(crop_names) != len(source.names):
        raise ValueError('Source file accounting mismatch')
    if source.kind == 'zip' and file_sha(source.path) != source.original_sha256:
        raise ValueError('Original checkpoint ZIP changed while staging')
    if source.kind == 'work_tree':
        final_names = sorted(path.relative_to(source.path).as_posix() for path in source.path.rglob('*')
                             if path.is_file() and path.suffix.lower() != '.zip' and '__pycache__' not in path.parts)
        if final_names != source.names:
            raise ValueError('Work-tree file inventory changed while staging')
        original_hashes = {record['original_path']: record['source_png_sha256'] for record in manifest['crops']}
        original_hashes.update({record['path']: record['sha256'] for record in manifest['preserved_files']})
        original_hashes.update({record['path']: record['original_sha256'] for record in manifest['reference_changes']})
        for name, expected_hash in original_hashes.items():
            if file_sha(source.path / name) != expected_hash:
                raise ValueError(f'Work-tree file changed while staging: {name}')
    manifest['verification'] = {
        'crop_count': len(crop_names), 'all_rgb_pixels_identical': True,
        'frozen_file_count': len(manifest['frozen_files']), 'all_frozen_files_byte_identical': True,
        'reference_changed_file_count': len(manifest['reference_changes']),
        'original_reference_bytes_preserved': True,
        'original_source_scripts_preserved': True,
        'non_crop_source_files_accounted_for': True,
        'original_archive_unchanged': source.kind == 'zip',
    }
    write_bytes(payload, f'{SUPPORT}/manifest.json', (json.dumps(manifest, indent=2, ensure_ascii=False) + '\n').encode())
    write_bytes(payload, f'{SUPPORT}/restore_png.py', restore_source.read_bytes())
    write_bytes(payload, f'{SUPPORT}/lossless_checkpoint.py', Path(__file__).read_bytes())
    source_summary = f'Original ZIP SHA256: `{source.original_sha256}`; original bytes: {source.original_size}.' if source.kind == 'zip' else 'Input was the supplied PNG work-tree snapshot.'
    readme = f'''# Lossless evidence encoding for {archive_name}

This is an encoding migration of the supplied snapshot. No later working reports or readings were added.
{source_summary}
Original scheduled checkpoint time: {args.snapshot_created_utc or 'not supplied'}.

## Pixel and text integrity

All {len(crop_names)} RGB PNG evidence crops are represented by lossless WebP counterparts. Every image was decoded and compared byte for byte in RGB, with unchanged dimensions. There was no resampling, grayscale conversion, quantization, or lossy encoding. The input crops had no ancillary Pillow metadata fields. The mapping, original PNG byte hashes, delivered WebP hashes, and decoded RGB hashes are recorded in `manifest.json`.

All {len(manifest['frozen_files'])} frozen first-reading, second-reading, box TSVs, and the first-reading manifest are byte-identical to the input. Original provenance scripts and TeX files are preserved byte for byte. Known crop filenames in {len(manifest['reference_changes'])} nonfrozen JSON/Markdown/CSV/TSV copies were changed to their delivered WebP counterparts. Recognized absolute crop paths were made relative to the archive root. Historical paths outside the converted crop inventory were retained. The exact original bytes of every reference-bearing file changed for delivery are retained under `reference_originals/`; their historical wording is recoverable exactly.

## View or continue the checkpoint

Evidence files are under `crops/` relative to the extracted archive root. Viewing them requires a WebP-capable image decoder. The encoder and verifier used Pillow {pillow_version} with libwebp {features.version('webp')}. The transcription has not acquired an image-format dependency.

To verify a fully extracted checkpoint, run from its root:

```sh
python3 encoding_support/restore_png.py --root .
```

To recreate the original PNG filenames and restore the original reference text before continuing workflows that construct `.png` paths:

```sh
python3 encoding_support/restore_png.py --root . --restore
```

The restore helper requires Pillow with WebP support. It validates all files before changes, preserves the WebP files, and verifies the recreated PNG dimensions and exact RGB hashes. Recreated PNG compressed bytes may differ from the original PNG encoding; their pixel values are identical. Existing frozen reading files are never rewritten. Run the helper before editing the delivered reference-bearing reports; it rejects unexpected modifications to avoid replacing later work.

## Archive-level receipt

The adjacent `{Path(archive_name).stem}_encoding_receipt.json` records the original and delivered archive SHA256 hashes, sizes, verification counts, and frozen file hashes. A ZIP cannot contain its own final SHA256 without a self-reference, so that final digest is retained in the separate receipt and upload record.
'''
    write_bytes(payload, f'{SUPPORT}/README.md', readme.encode('utf-8'))
    archive_path = output / archive_name
    print(json.dumps({'stage': 'packaging', 'path': str(archive_path)}), flush=True)
    with ZipFile(archive_path, 'x', compression=ZIP_DEFLATED, compresslevel=9, allowZip64=True) as archive:
        for path in sorted(payload.rglob('*')):
            if path.is_file():
                archive.write(path, path.relative_to(payload).as_posix())
    with ZipFile(archive_path) as archive:
        bad = archive.testzip()
        if bad:
            raise ValueError(f'Delivered archive CRC failure: {bad}')
        for record in manifest['frozen_files']:
            if sha(archive.read(record['path'])) != record['sha256']:
                raise ValueError(f'Archived frozen file hash mismatch: {record["path"]}')
    receipt = {
        'schema': 'sp93-lossless-encoding-receipt-v1',
        'created_at_utc': datetime.now(timezone.utc).isoformat(),
        'original_archive_path': str(source.path), 'original_archive_sha256': source.original_sha256,
        'original_archive_size_bytes': source.original_size,
        'delivered_archive_path': str(archive_path), 'delivered_archive_sha256': file_sha(archive_path),
        'delivered_archive_size_bytes': archive_path.stat().st_size,
        'limit_bytes': args.max_bytes, 'within_limit': archive_path.stat().st_size <= args.max_bytes,
        'manifest_sha256': file_sha(payload / SUPPORT / 'manifest.json'),
        'verification': manifest['verification'], 'frozen_files': manifest['frozen_files'],
        'elapsed_seconds': time.perf_counter() - started,
    }
    receipt_path = output / f'{Path(archive_name).stem}_encoding_receipt.json'
    receipt_path.write_text(json.dumps(receipt, indent=2) + '\n')
    source.close()
    print(json.dumps({'stage': 'complete', 'receipt_path': str(receipt_path), **receipt}), flush=True)
    return 0 if receipt['within_limit'] else 2

if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, KeyError) as error:
        print(f'lossless checkpoint staging failed: {error}', file=sys.stderr)
        raise SystemExit(1)
