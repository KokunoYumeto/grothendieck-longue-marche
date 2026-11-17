"""One256MiB encoder on the exact prospective36 image stream; no ZIP/TAR file.

The whole stream is first hashed without compression. A second deterministic
streaming pass feeds exactly one candidate encoder and a full independent
decoder. Neither the running128MiB estimator nor any bound helper is changed.
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
EXPECTED_BYTES = 606_720_000
EXPECTED_SHA = '936dfe5a59bff2c3c93380d033c0c9b70160d20163c502b319423da1267f8b7d'
DICTIONARY = 256 * 1024 * 1024
EXPECTED_SOURCES = {
    'code/estimate_checkpoint36_size.py': '293e093f5d0cdc7ed8d841182b2c33e09f0c38bde414724891ea7a3d50bc0e47',
    'code/package_checkpoint.py': 'cf0a5219cf66ec07e7f8509634888392929fb1eced6f05748e35d462052938dc',
    'code/checkpoint_image_tar.py': 'c3de17157c5d6fa5ac66bfc64717df096c3dbcc195965be1a7d91c878df352f6',
    'code/checkpoint_data_tar.py': '9e149cc79ca9790fc55a3147a4664c0886cbe1dc0b981727459a26bac35badbb',
    'work_CE/checkpoint_image_tar_256_proposed36.py': 'e6019666bfc8486f3de4355c4f78dd297532e3c764114a450be1fcd4d43fb885',
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


def png_paths():
    return {str(f.relative_to(ROOT)): f for f in ROOT.rglob('*.png')
            if f.is_file() and included(f)}


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


def stream_images(sources, identities, sink):
    """Same deterministic PAX members and hard links as build_standard_tar.

    Streaming avoids holding a600MB TAR alongside a256MiB encoder. Exact
    byte equality with the estimator stream is independently required.
    """
    seen = {}
    links = 0
    original_bytes = 0
    with tarfile.open(fileobj=sink, mode='w|', format=tarfile.PAX_FORMAT) as tf:
        for relative, source in sorted(sources.items()):
            data = read_source(source)
            identity = (len(data), sha(data))
            assert identity == identities[relative], ('PNG changed', relative)
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
    target = ROOT / 'records/checkpoint36_prospective_image256_measurement.json'
    assert not target.exists(), 'Never overwrite a prior measurement'
    assert ARCHIVE.stat().st_size == ARCHIVE_BYTES and hash_path(ARCHIVE) == ARCHIVE_SHA
    bindings = [bind(rel) for rel in EXPECTED_SOURCES]
    for item in bindings:
        assert item['sha256'] == EXPECTED_SOURCES[item['path']]
    self_binding = bind('code/measure_checkpoint36_prospective_image256.py')

    log = (ROOT/'records/checkpoint36_size_estimate_run.out').read_text()
    marker = 'Compressing actual prospective images TAR '
    lines = [line[len(marker):] for line in log.splitlines() if line.startswith(marker)]
    assert len(lines) == 1, 'Require the one actual running36 estimator image record'
    expected_metrics = json.loads(lines[0])
    assert expected_metrics['bundle_bytes'] == EXPECTED_BYTES
    assert expected_metrics['bundle_sha256'] == EXPECTED_SHA

    sources = png_paths()
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
        if not relative.endswith('.png'):
            continue
        identity = (int(row['bytes']), row['sha256'])
        if identities.get(relative) == identity:
            continue
        historical = 'checkpoint_history/checkpoint_35/' + relative
        if historical in identities:
            assert identities[historical] == identity, 'Historical PNG collision'
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

    print('Preflight exact prospective image stream without compression', flush=True)
    before_sink = CountingSink()
    metrics = stream_images(sources, identities, before_sink)
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
            print('candidate256 decoded_bytes', decoded.size,
                  'of', EXPECTED_BYTES, 'compressed_bytes', compressed_bytes, flush=True)
            last_report = time.monotonic()

    encoded_input = CountingSink(consume_input)
    metrics_after = stream_images(sources, identities, encoded_input)
    consume_output(encoder.flush())
    assert metrics_after == metrics and encoded_input.result() == before
    assert decoded.result() == before and decoder.eof
    assert bytes(prefix) == bytes.fromhex('090405005d00000010')
    assert set(png_paths()) == current_paths, 'Current PNG set changed during measurement'
    assert ARCHIVE.stat().st_size == ARCHIVE_BYTES and hash_path(ARCHIVE) == ARCHIVE_SHA
    for item in bindings + [self_binding]:
        assert bind(item['path']) == item, ('Source changed', item['path'])
    report = {
        'result': 'PASS_EXACT_PROSPECTIVE_STREAM_AND_FULL_ROUNDTRIP',
        'started_at': started.isoformat(),
        'completed_at': datetime.now(timezone.utc).isoformat(),
        'archive': ARCHIVE.name, 'archive_bytes': ARCHIVE_BYTES,
        'archive_sha256': ARCHIVE_SHA, 'archive_unchanged': True,
        'reference_estimator': bindings[0], 'actual_estimator_image_metrics': expected_metrics,
        'input_preflight': before, 'input_second_pass': encoded_input.result(),
        'candidate': {'dictionary_bytes': DICTIONARY, 'zip_method': 'ZIP_LZMA',
                      'method_number': 14, 'method14_header_hex': bytes(prefix).hex(),
                      'compressed_bytes': compressed_bytes,
                      'compressed_sha256': compressed_sha.hexdigest(),
                      'roundtrip': decoded.result(), 'decoder_eof': decoder.eof,
                      'compression_seconds': time.monotonic()-compression_started},
        'predicted_parent_png_versions_added': len(pending),
        'bound_unchanged_sources': bindings, 'source': self_binding,
        'encoder_count': 1, 'baseline_reencoded': False,
        'creates_zip': False, 'creates_tar_file': False,
        'installs_packaging_change': False,
        'scope': 'Exactly the image stream already printed by the actual36 estimator. No document/data compressor is run or substituted. Any later accounting must bind their completed actual measurements separately and preserve the original128MiB estimate.'}
    with target.open('x') as stream:
        json.dump(report, stream, indent=2)
        stream.write('\n')
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
