"""Disk-staged, standard-library checkpoint37 streaming primitives.

No command in this module creates a ZIP. The encode/decode commands operate on
one raw standard method14 payload in a temporary directory outside the project.
They run in separate fresh processes, so encoder and decoder dictionaries never
coexist. The package caller alone opens the single authorized final ZIP.
"""
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
from contextlib import nullcontext
import argparse
import csv
import hashlib
import io
import json
import lzma
import struct
import subprocess
import sys
import tarfile
import tempfile
import time
import zipfile
import zlib

from checkpoint_data_tar import DATA_BUNDLE, DATA_DICTIONARY_BYTES, DataLZMACompressor, is_data_bundle_member, standard_data_dictionary
from checkpoint_image37_tar import IMAGE37_DICTIONARY_BYTES, Image37LZMACompressor, standard_image37_dictionary
from checkpoint_document37_tar import DOCUMENT37_DICTIONARY_BYTES, Document37LZMACompressor, standard_document37_dictionary

CHUNK = 1 << 20
PREFIX = 'LM4_SUCCESSOR/'
CODECS = {
    'images': (Image37LZMACompressor, IMAGE37_DICTIONARY_BYTES),
    'documents': (Document37LZMACompressor, DOCUMENT37_DICTIONARY_BYTES),
    'data': (DataLZMACompressor, DATA_DICTIONARY_BYTES),
}


def identity(path):
    sha, crc, length = hashlib.sha256(), 0, 0
    with Path(path).open('rb') as src:
        for part in iter(lambda: src.read(CHUNK), b''):
            sha.update(part)
            crc = zlib.crc32(part, crc) & 0xffffffff
            length += len(part)
    return {'bytes': length, 'sha256': sha.hexdigest(), 'crc32': crc}


def json_exclusive(path, value):
    with Path(path).open('x') as dst:
        json.dump(value, dst, indent=2)
        dst.write('\n')


def write_standard_tar(files, destination):
    """Exactly the prior deterministic PAX TAR, written directly to disk."""
    files = sorted(files)
    names = [relative for relative, _ in files]
    assert len(names) == len(set(names)), 'Duplicate logical paths'
    seen, links = {}, 0
    with Path(destination).open('xb') as raw:
        with tarfile.open(fileobj=raw, mode='w', format=tarfile.PAX_FORMAT) as tf:
            for relative, data in files:
                p = PurePosixPath(relative)
                assert not p.is_absolute() and '..' not in p.parts
                full = PREFIX + relative
                member = tarfile.TarInfo(full)
                member.mode, member.mtime = 0o644, 0
                key = (len(data), hashlib.sha256(data).hexdigest())
                if key in seen:
                    previous_name, previous_data = seen[key]
                    assert data == previous_data, 'Hash collision'
                    member.type, member.linkname, member.size = tarfile.LNKTYPE, previous_name, 0
                    tf.addfile(member)
                    links += 1
                else:
                    member.size = len(data)
                    tf.addfile(member, io.BytesIO(data))
                    seen[key] = (full, data)
    actual = identity(destination)
    return {'paths': len(files), 'unique_contents': len(seen),
            'standard_tar_hardlinks': links,
            'original_bytes': sum(len(data) for _, data in files),
            'unique_bytes': sum(size for size, _ in seen),
            'bundle_bytes': actual['bytes'], 'bundle_sha256': actual['sha256'],
            'bundle_crc32': actual['crc32']}


def encode(source, destination, kind, expected, report):
    """One encoder, bounded input/output chunks, and no decoder in this process."""
    compressor_class, dictionary = CODECS[kind]
    expected_header = bytes.fromhex('090405005d') + dictionary.to_bytes(4, 'little')
    compressor = compressor_class()
    input_sha, input_crc, input_length = hashlib.sha256(), 0, 0
    output_sha, output_length, header = hashlib.sha256(), 0, bytearray()
    started, last_report = time.monotonic(), time.monotonic()
    with Path(source).open('rb') as src, Path(destination).open('xb') as dst:
        def emit(encoded):
            nonlocal output_length
            if len(header) < 9:
                header.extend(encoded[:9-len(header)])
            dst.write(encoded)
            output_sha.update(encoded)
            output_length += len(encoded)
        for part in iter(lambda: src.read(CHUNK), b''):
            input_sha.update(part)
            input_crc = zlib.crc32(part, input_crc) & 0xffffffff
            input_length += len(part)
            emit(compressor.compress(part))
            if time.monotonic()-last_report >= 25:
                print(kind, 'input_bytes_processed', input_length, 'of', expected['bytes'], flush=True)
                last_report = time.monotonic()
        emit(compressor.flush())
    actual_input = {'bytes': input_length, 'sha256': input_sha.hexdigest(), 'crc32': input_crc}
    assert actual_input == expected, 'Staged input changed before/during encoding'
    assert bytes(header) == expected_header
    result = {'input': actual_input, 'compressed_bytes': output_length,
              'compressed_sha256': output_sha.hexdigest(),
              'dictionary_bytes': dictionary, 'method14_header_hex': header.hex(),
              'elapsed_seconds': time.monotonic()-started,
              'decoder_in_encoder_process': False}
    json_exclusive(report, result)
    print('Encoded', kind, json.dumps(result), flush=True)


def decode(source, expected, encoded_report, report):
    """Independent full stdlib LZMA decoder, after the encoder process exits.

    Parsing the verified nine-byte ZIP method14 prefix is exactly the framing
    used by zipfile.LZMADecompressor. max_length bounds every output allocation.
    """
    encoded = json.loads(Path(encoded_report).read_text())
    decoded_sha, decoded_crc, decoded_length = hashlib.sha256(), 0, 0
    encoded_sha, encoded_length = hashlib.sha256(), 0
    with Path(source).open('rb') as src:
        header = src.read(9)
        assert header.hex() == encoded['method14_header_hex']
        assert header[:4] == struct.pack('<BBH', 9, 4, 5)
        props = lzma._decode_filter_properties(lzma.FILTER_LZMA1, header[4:])
        assert props['dict_size'] == encoded['dictionary_bytes']
        decoder = lzma.LZMADecompressor(format=lzma.FORMAT_RAW, filters=[props])
        encoded_sha.update(header)
        encoded_length += len(header)
        while True:
            part = src.read(CHUNK)
            if not part:
                break
            assert not decoder.eof, 'Encoded tail after the LZMA end marker'
            encoded_sha.update(part)
            encoded_length += len(part)
            pending = part
            while True:
                block = decoder.decompress(pending, max_length=CHUNK)
                pending = b''
                decoded_sha.update(block)
                decoded_crc = zlib.crc32(block, decoded_crc) & 0xffffffff
                decoded_length += len(block)
                if decoder.eof:
                    assert decoder.unused_data == b'', 'Trailing bytes in encoded block'
                    break
                if decoder.needs_input:
                    break
        assert decoder.eof, 'Missing end marker/truncated payload'
        assert decoder.unused_data == b''
    actual = {'bytes': decoded_length, 'sha256': decoded_sha.hexdigest(), 'crc32': decoded_crc}
    assert actual == expected == encoded['input'], 'Full independent roundtrip mismatch'
    assert encoded_length == encoded['compressed_bytes']
    assert encoded_sha.hexdigest() == encoded['compressed_sha256']
    result = {'input': expected, 'roundtrip': actual, 'decoder_eof': True,
              'unused_bytes': 0, 'method14_header_hex': header.hex(),
              'encoded_sha256': encoded_sha.hexdigest(),
              'encoder_and_decoder_in_separate_processes': True,
              'decoder_output_chunk_limit': CHUNK,
              'encoded_stream_retained': False,
              'encoded_stream_temporary_file_used': True}
    json_exclusive(report, result)
    print('Verified complete independent roundtrip', json.dumps(result), flush=True)


def measure_staged_tar(source, kind, metrics, directory):
    """Wait for successful encoder exit before launching the full decoder."""
    directory, source = Path(directory), Path(source)
    expected = {'bytes': metrics['bundle_bytes'], 'sha256': metrics['bundle_sha256'],
                'crc32': metrics['bundle_crc32']}
    expected_path = directory/(kind+'.expected.json')
    payload, enc_report, dec_report = [directory/(kind+s) for s in ('.method14', '.encode.json', '.decode.json')]
    json_exclusive(expected_path, expected)
    command = [sys.executable, str(Path(__file__).resolve())]
    subprocess.run(command+['encode', str(source), str(payload), kind, str(expected_path), str(enc_report)], check=True)
    subprocess.run(command+['decode', str(payload), str(expected_path), str(enc_report), str(dec_report)], check=True)
    encoded, verified = json.loads(enc_report.read_text()), json.loads(dec_report.read_text())
    assert identity(source) == expected, 'Staged source changed after verification'
    payload.unlink()
    return {'metrics': metrics, 'compressed_bytes': encoded['compressed_bytes'],
            'zip_method': 'ZIP_LZMA', 'dictionary_bytes': encoded['dictionary_bytes'],
            'full_roundtrip': verified, 'elapsed_seconds': encoded['elapsed_seconds'],
            'encoder_process_exit_code': 0, 'decoder_process_exit_code': 0,
            'compressed_sha256': encoded['compressed_sha256']}


def write_zip_entry(z, arcname, source, expected, method, dictionary_context=None):
    """Standard ZipFile streaming writer; no uncompressed TAR blob retained."""
    info = zipfile.ZipInfo(arcname, tuple(time.localtime(time.time())[:6]))
    info.compress_type, info.external_attr = method, 0o600 << 16
    info.file_size = expected['bytes']
    info._compresslevel = 6 if method == zipfile.ZIP_DEFLATED else None
    sha, crc, length = hashlib.sha256(), 0, 0
    with (dictionary_context() if dictionary_context is not None else nullcontext()):
        with Path(source).open('rb') as src, z.open(info, 'w') as dst:
            for part in iter(lambda: src.read(CHUNK), b''):
                sha.update(part)
                crc = zlib.crc32(part, crc) & 0xffffffff
                length += len(part)
                dst.write(part)
    assert {'bytes': length, 'sha256': sha.hexdigest(), 'crc32': crc} == expected


def package_from_stage(root, number, script):
    """Stage in a separate child, then open only the final authorized ZIP."""
    root = Path(root)
    assert number >= 37
    out = root.parent/f'LM4_SUCCESSOR_checkpoint_{number:02d}.zip'
    assert not out.exists(), 'Never overwrite a checkpoint'
    with tempfile.TemporaryDirectory(prefix=f'.checkpoint{number}_stage_', dir=root.parent) as tmp:
        stage = Path(tmp)
        subprocess.run([sys.executable, str(script), str(number), '--staging-directory', str(stage)], check=True)
        metadata = json.loads((stage/'package-stage.json').read_text())
        assert metadata['number'] == number
        for relative, expected in metadata['source_bindings'].items():
            assert identity(root/relative) == expected, ('Source changed after staging', relative)
        # The child has exited: no snapshot bytes or TAR buffers remain resident.
        with zipfile.ZipFile(out, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
            for row in metadata['direct']:
                method = zipfile.ZIP_LZMA if row['zip_method'] == 'ZIP_LZMA' else zipfile.ZIP_DEFLATED
                write_zip_entry(z, PREFIX+row['path'], stage/'direct'/row['path'], row['identity'], method)
            contexts = {'images': standard_image37_dictionary,
                        'documents': standard_document37_dictionary,
                        'data': standard_data_dictionary}
            for row in metadata['bundles']:
                write_zip_entry(z, row['archive_name'], stage/row['stage_name'], row['identity'],
                                zipfile.ZIP_LZMA, contexts[row['kind']])
        for relative, expected in metadata['source_bindings'].items():
            assert identity(root/relative) == expected, ('Source changed while packaging', relative)
        print(out, flush=True)
        final = identity(out)
        print('logical files', metadata['logical_file_count'], 'bytes', final['bytes'], 'sha256', final['sha256'], flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('encode', 'decode'))
    parser.add_argument('arguments', nargs='+')
    args = parser.parse_args()
    if args.mode == 'encode':
        source, destination, kind, expected, report = args.arguments
        encode(source, destination, kind, json.loads(Path(expected).read_text()), report)
    else:
        source, expected, encoded_report, report = args.arguments
        decode(source, json.loads(Path(expected).read_text()), encoded_report, report)


if __name__ == '__main__':
    main()
