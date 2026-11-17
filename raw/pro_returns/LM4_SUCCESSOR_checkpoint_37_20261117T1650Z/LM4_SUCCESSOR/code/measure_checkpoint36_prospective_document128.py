"""One128MiB encoder on the exact prospective36 document stream; no ZIP/TAR file.

The whole stream is first hashed without compression. A second deterministic
streaming pass feeds exactly one candidate encoder and a full independent
decoder. The completed estimator and every bound helper remain unchanged.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json
import lzma
import struct
import tarfile
import time
import zipfile
import zlib

from checkpoint_archive_io import CheckpointReader
from estimate_checkpoint36_size import included

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT.parent / 'LM4_SUCCESSOR_checkpoint_35.zip'
PREFIX = 'LM4_SUCCESSOR/'
ARCHIVE_BYTES = 530_938_760
ARCHIVE_SHA = '33b0925ca3ba12d8944fc47243807a3c61ebb2a4f03ec47f7bb2ce1a5a83f121'
EXPECTED_BYTES = 163_317_760
EXPECTED_SHA = '41091b481d03ffdbccc47fa2351e2a1529cc470c6a37874173d83d1ff8887f90'
DICTIONARY = 128 * 1024 * 1024
EXPECTED_SOURCES = {
    'code/estimate_checkpoint36_size.py': '293e093f5d0cdc7ed8d841182b2c33e09f0c38bde414724891ea7a3d50bc0e47',
    'code/package_checkpoint.py': 'cf0a5219cf66ec07e7f8509634888392929fb1eced6f05748e35d462052938dc',
    'code/checkpoint_image_tar.py': 'c3de17157c5d6fa5ac66bfc64717df096c3dbcc195965be1a7d91c878df352f6',
    'code/checkpoint_data_tar.py': '9e149cc79ca9790fc55a3147a4664c0886cbe1dc0b981727459a26bac35badbb',
    'records/checkpoint36_size_estimate.json': '005b64fab4b5cf9dfd302ca5c837b053b3b06045765012b187fb1d2ac2436d28',
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def hash_path(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def bind(relative):
    path = ROOT / relative
    return {'path': relative, 'bytes': path.stat().st_size,
            'sha256': hash_path(path)}


def document_paths():
    return {str(f.relative_to(ROOT)): f for f in ROOT.rglob('*.pdf')
            if f.is_file() and included(f)
            and str(f.relative_to(ROOT)) != 'LM4_SUCCESSOR_paper.pdf'}


class CandidateCompressor(zipfile.LZMACompressor):
    def _init(self):
        props = lzma._encode_filter_properties({
            'id': lzma.FILTER_LZMA1, 'dict_size': DICTIONARY})
        self._comp = lzma.LZMACompressor(lzma.FORMAT_RAW, filters=[
            lzma._decode_filter_properties(lzma.FILTER_LZMA1, props)])
        return struct.pack('<BBH', 9, 4, len(props)) + props


class CountingSink:
    def __init__(self, consume=None):
        self.digest = hashlib.sha256()
        self.crc = 0
        self.size = 0
        self.consume = consume

    def write(self, data):
        self.digest.update(data)
        self.crc = zlib.crc32(data, self.crc)
        self.size += len(data)
        if self.consume is not None:
            self.consume(data)
        return len(data)

    def result(self):
        return {'bytes': self.size, 'sha256': self.digest.hexdigest(),
                'crc32': self.crc & 0xffffffff}


def read_source(source):
    if isinstance(source, Path):
        return source.read_bytes()
    return source


def stream_documents(sources, identities, sink):
    """Same deterministic PAX members and hard links as build_standard_tar.

    Streaming avoids holding a163MB TAR alongside a128MiB encoder. Exact
    byte equality with the estimator stream is independently required.
    """
    seen = {}
    links = 0
    original_bytes = 0
    with tarfile.open(fileobj=sink, mode='w|', format=tarfile.PAX_FORMAT) as tf:
        for relative, source in sorted(sources.items()):
            data = read_source(source)
            identity = (len(data), sha(data))
            assert identity == identities[relative], ('Document changed', relative)
            original_bytes += len(data)
            info = tarfile.TarInfo(PREFIX + relative)
            info.mode = 0o644
            info.mtime = 0
            if identity in seen:
                target, previous_source = seen[identity]
                assert read_source(previous_source) == data, 'Hash collision'
                info.type = tarfile.LNKTYPE
                info.linkname = target
                info.size = 0
                tf.addfile(info)
                links += 1
            else:
                info.size = len(data)
                tf.addfile(info, io.BytesIO(data))
                seen[identity] = (PREFIX + relative, source)
    r = sink.result()
    return {'paths': len(sources), 'unique_contents': len(seen),
            'standard_tar_hardlinks': links, 'original_bytes': original_bytes,
            'unique_bytes': sum(size for size, _ in seen),
            'bundle_bytes': r['bytes'], 'bundle_sha256': r['sha256']}


def main():
    started = datetime.now(timezone.utc)
    target = ROOT / 'records/checkpoint36_prospective_document128_measurement.json'
    assert not target.exists(), 'Never overwrite a prior measurement'
    assert ARCHIVE.stat().st_size == ARCHIVE_BYTES and hash_path(ARCHIVE) == ARCHIVE_SHA
    bindings = [bind(rel) for rel in EXPECTED_SOURCES]
    for item in bindings:
        assert item['sha256'] == EXPECTED_SOURCES[item['path']]
    self_binding = bind('code/measure_checkpoint36_prospective_document128.py')

    original_estimate = json.loads((ROOT/'records/checkpoint36_size_estimate.json').read_text())
    expected_metrics = original_estimate['prospective_bundles']['documents']['metrics']
    baseline_compressed_bytes = original_estimate['prospective_bundles']['documents']['compressed_bytes']
    assert original_estimate['prospective_bundles']['documents']['dictionary_bytes'] == 64 * 1024 * 1024
    assert expected_metrics['bundle_bytes'] == EXPECTED_BYTES
    assert expected_metrics['bundle_sha256'] == EXPECTED_SHA

    sources = document_paths()
    current_paths = set(sources)
    identities = {}
    for relative, path in sources.items():
        data = path.read_bytes()
        identities[relative] = (len(data), sha(data))
    with zipfile.ZipFile(ARCHIVE) as z:
        manifest = z.read(PREFIX+'records/checkpoint_35_contents_sha256.tsv')
    rows = list(csv.DictReader(io.StringIO(manifest.decode()), delimiter='\t'))
    pending = []
    for row in rows:
        relative = row['path']
        if not relative.endswith('.pdf'):
            continue
        identity = (int(row['bytes']), row['sha256'])
        if identities.get(relative) == identity:
            continue
        historical = 'checkpoint_history/checkpoint_35/' + relative
        if historical in identities:
            assert identities[historical] == identity, 'Historical document collision'
        else:
            pending.append((relative, historical, identity))
    if pending:
        with CheckpointReader(ARCHIVE) as prior:
            for relative, historical, identity in pending:
                data = prior.read(PREFIX + relative)
                assert (len(data), sha(data)) == identity
                sources[historical] = data
                identities[historical] = identity
        del prior

    print('Preflight exact prospective document stream without compression', flush=True)
    before_sink = CountingSink()
    metrics = stream_documents(sources, identities, before_sink)
    assert metrics == expected_metrics
    before = before_sink.result()
    assert before['bytes'] == EXPECTED_BYTES and before['sha256'] == EXPECTED_SHA
    print('Preflight input identity PASS', json.dumps(before), flush=True)

    encoder = CandidateCompressor()  # The sole candidate encoder.
    decoder = zipfile.LZMADecompressor()
    compressed_sha = hashlib.sha256()
    compressed_bytes = 0
    prefix = bytearray()
    decoded = CountingSink()
    last_report = time.monotonic()
    compression_started = time.monotonic()

    def consume_output(data):
        nonlocal compressed_bytes
        if not data:
            return
        compressed_bytes += len(data)
        compressed_sha.update(data)
        if len(prefix) < 9:
            prefix.extend(data[:9-len(prefix)])
        decoded.write(decoder.decompress(data))

    def consume_input(data):
        nonlocal last_report
        consume_output(encoder.compress(data))
        if time.monotonic()-last_report >= 25:
            print('candidate128 decoded_bytes', decoded.size,
                  'of', EXPECTED_BYTES, 'compressed_bytes', compressed_bytes, flush=True)
            last_report = time.monotonic()

    encoded_input = CountingSink(consume_input)
    metrics_after = stream_documents(sources, identities, encoded_input)
    consume_output(encoder.flush())
    assert metrics_after == metrics and encoded_input.result() == before
    assert decoded.result() == before and decoder.eof
    assert not decoder._decomp.unused_data, 'Unexpected data after candidate EOF'
    assert bytes(prefix) == bytes.fromhex('090405005d00000008')
    assert set(document_paths()) == current_paths, 'Current document set changed during measurement'
    assert ARCHIVE.stat().st_size == ARCHIVE_BYTES and hash_path(ARCHIVE) == ARCHIVE_SHA
    for item in bindings + [self_binding]:
        assert bind(item['path']) == item, ('Source changed', item['path'])
    report = {
        'result': 'PASS_EXACT_PROSPECTIVE_STREAM_AND_FULL_ROUNDTRIP',
        'started_at': started.isoformat(),
        'completed_at': datetime.now(timezone.utc).isoformat(),
        'archive': ARCHIVE.name, 'archive_bytes': ARCHIVE_BYTES,
        'archive_sha256': ARCHIVE_SHA, 'archive_unchanged': True,
        'reference_estimator': bindings[0], 'actual_estimator_document_metrics': expected_metrics,
        'input_preflight': before, 'input_second_pass': encoded_input.result(),
        'candidate': {'dictionary_bytes': DICTIONARY, 'zip_method': 'ZIP_LZMA',
                      'method_number': 14, 'method14_header_hex': bytes(prefix).hex(),
                      'compressed_bytes': compressed_bytes,
                      'compressed_sha256': compressed_sha.hexdigest(),
                      'roundtrip': decoded.result(), 'decoder_eof': decoder.eof,
                      'decoder_unused_bytes': len(decoder._decomp.unused_data),
                      'compression_seconds': time.monotonic()-compression_started},
        'predicted_parent_document_versions_added': len(pending),
        'bound_unchanged_sources': bindings, 'source': self_binding,
        'encoder_count': 1, 'baseline_reencoded': False,
        'baseline_actual_document64_compressed_bytes': baseline_compressed_bytes,
        'saving_from_actual_document64_bytes': baseline_compressed_bytes - compressed_bytes,
        'creates_zip': False, 'creates_tar_file': False,
        'installs_packaging_change': False,
        'scope': 'Exactly the document stream already printed by the actual36 estimator. Exactly one document128 candidate is encoded. No image/data compressor is run or substituted. Any later accounting must bind their completed actual measurements separately and preserve the original estimate.'}
    with target.open('x') as stream:
        json.dump(report, stream, indent=2)
        stream.write('\n')
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
