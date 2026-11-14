#!/usr/bin/env python3
"""Read back every file in an ANABELIAN_149_PUSH archive and verify its manifest.

Usage: python3 code/verify_archive.py /path/to/ANABELIAN_149_PUSH.zip
The output is a post-creation receipt; it cannot include its own final
archive hash inside that same immutable archive. The archive manifest is
the packager's internal output and this receipt is its external readback.
"""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import tarfile
import tempfile
import zipfile


def digest_stream(stream):
    digest = hashlib.sha256()
    size = 0
    while True:
        block = stream.read(4 * 1024 * 1024)
        if not block:
            return size, digest.hexdigest()
        size += len(block)
        digest.update(block)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('archive', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    prefix = 'ANABELIAN_149_PUSH/'
    manifest_name = prefix + 'archive_manifest.json'
    with zipfile.ZipFile(args.archive) as archive:
        manifest = json.loads(archive.read(manifest_name))
        expected = {prefix + row['path'] for row in manifest['files']}
        names = archive.namelist()
        assert len(names) == len(set(names)), 'Duplicate archive member'
        assert set(names) == expected | {manifest_name}, 'Archive/manifest mismatch'
        for row in manifest['files']:
            with archive.open(prefix + row['path']) as stream:
                size, digest = digest_stream(stream)
            assert size == row['bytes'], ('Size mismatch', row['path'])
            assert digest == row['sha256'], ('SHA256 mismatch', row['path'])
        historical = [row for row in manifest['files']
                      if row['path'].startswith('history/')
                      and row['path'].endswith('.zip')]
        container = manifest.get('history_container')
        if container:
            assert not historical, 'Duplicate raw and solid historical archives'
            preservation = json.loads(archive.read(prefix+'audit/history_preservation.json'))
            expected_history = {Path(row['path']).name: row for row in preservation['archives']}
            seen = set()
            with tempfile.TemporaryDirectory(prefix='anabelian-readback-') as temporary:
                local_container = Path(temporary)/'history.tar.zst'
                with archive.open(prefix+container) as source, local_container.open('wb') as target:
                    shutil.copyfileobj(source, target, 4*1024*1024)
                decoder = subprocess.Popen(['zstd','-d','-c','--long=28',str(local_container)],
                                           stdout=subprocess.PIPE)
                try:
                    with tarfile.open(fileobj=decoder.stdout, mode='r|') as history:
                        for member in history:
                            assert member.isfile(), ('Non-file history member', member.name)
                            assert member.name in expected_history, ('Unknown history member', member.name)
                            assert member.name not in seen, ('Duplicate history member', member.name)
                            row = expected_history[member.name]
                            with history.extractfile(member) as stream:
                                historical_size, historical_hash = digest_stream(stream)
                            assert historical_size == row['bytes']
                            assert historical_hash == row['sha256']
                            seen.add(member.name)
                            historical.append(row)
                    # Consume any allowed tar padding, so the decoder finishes normally.
                    while decoder.stdout.read(1024*1024):
                        pass
                    assert decoder.wait() == 0, 'Zstandard decoding failed'
                finally:
                    decoder.stdout.close()
                    if decoder.poll() is None:
                        decoder.kill()
                        decoder.wait()
            assert seen == set(expected_history), 'Missing historical checkpoint'
            assert len(historical) == preservation['checkpoint_archives'] == 10
            assert sum(row['bytes'] for row in historical) == preservation['total_bytes']
    with args.archive.open('rb') as stream:
        size, digest = digest_stream(stream)
    result = {
        'status': 'PASS',
        'archive': str(args.archive.resolve()),
        'bytes': size,
        'sha256': digest,
        'manifest_entries_read_back': len(manifest['files']),
        'all_sizes_and_sha256_matched': True,
        'historical_checkpoint_archives': len(historical),
        'historical_checkpoint_bytes': sum(row['bytes'] for row in historical),
        'historical_checkpoint_byte_streams_verified': True,
        'history_container': container,
        'research_status': manifest['status'],
        'pdf_included': manifest['pdf_included'],
    }
    rendered = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.write_text(rendered)
    print(rendered, end='')


if __name__ == '__main__':
    main()
