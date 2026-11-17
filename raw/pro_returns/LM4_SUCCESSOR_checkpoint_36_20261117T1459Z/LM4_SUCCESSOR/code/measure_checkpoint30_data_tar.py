"""Measure a standard lossless data TAR and ZIP-LZMA stream; never create a ZIP.

The input is the immutable actual checkpoint29. This is an exact comparison
on those bytes, not a prediction of checkpoint30's as-yet-unwritten proofs.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import gc
import hashlib
import json
import lzma
import struct
import time
import zipfile
from checkpoint_standard_tar import build_standard_tar

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--dictionary-mib', type=int, default=64)
parser.add_argument('--tag', default='data64')
args = parser.parse_args()
assert args.dictionary_mib in (8, 16, 32, 64, 128, 256)
assert args.tag.replace('_', '').isalnum()
destination = root / f'records/checkpoint30_{args.tag}_measurement.json'
assert not destination.exists(), 'Preserve every genuine measurement.'
archive = root.parent / 'LM4_SUCCESSOR_checkpoint_29.zip'
prefix = 'LM4_SUCCESSOR/'
started = datetime.now(timezone.utc)
begin = time.monotonic()
with zipfile.ZipFile(archive) as z:
    selected = []
    replaced_compressed = 0
    for info in z.infolist():
        if info.is_dir():
            continue
        assert info.filename.startswith(prefix)
        rel = info.filename[len(prefix):]
        suffix = Path(rel).suffix.lower()
        take = (suffix not in {'.png', '.pdf', '.tar'} and
                (rel.startswith('checkpoint_history/') or
                 (suffix == '.json' and info.file_size >= 1_000_000)))
        if take:
            selected.append((rel, z.read(info)))
            replaced_compressed += info.compress_size
    actual_archive_bytes = archive.stat().st_size
print('Actual input selected', len(selected), 'paths; existing compressed payload', replaced_compressed, flush=True)
bundle, metrics = build_standard_tar(selected)
del selected
gc.collect()
print('Standard TAR metrics', json.dumps(metrics, sort_keys=True), flush=True)

options = {'id': lzma.FILTER_LZMA1, 'dict_size': args.dictionary_mib * 1024 * 1024}
props = lzma._encode_filter_properties(options)
decoded_options = lzma._decode_filter_properties(lzma.FILTER_LZMA1, props)
assert decoded_options['dict_size'] == options['dict_size']
compressor = lzma.LZMACompressor(lzma.FORMAT_RAW, filters=[decoded_options])
decoder = zipfile.LZMADecompressor()
encoded_sha = hashlib.sha256()
restored_sha = hashlib.sha256()
encoded_bytes = 0
restored_bytes = 0

def consume(encoded):
    global encoded_bytes, restored_bytes
    encoded_sha.update(encoded)
    encoded_bytes += len(encoded)
    restored = decoder.decompress(encoded)
    restored_sha.update(restored)
    restored_bytes += len(restored)

consume(struct.pack('<BBH', 9, 4, len(props)) + props)
compression_started = time.monotonic()
step = 1024 * 1024
for offset in range(0, len(bundle), step):
    consume(compressor.compress(bundle[offset:offset + step]))
    if offset and offset % (64 * step) == 0:
        print('Compressed input bytes', offset, 'elapsed', round(time.monotonic() - compression_started, 2), flush=True)
consume(compressor.flush())
assert decoder.eof
assert restored_bytes == len(bundle) == metrics['bundle_bytes']
assert restored_sha.hexdigest() == metrics['bundle_sha256']
equivalent_bytes = actual_archive_bytes - replaced_compressed + encoded_bytes
record = {
    'started_at': started.isoformat(),
    'completed_at': datetime.now(timezone.utc).isoformat(),
    'input_archive': archive.name,
    'input_archive_bytes': actual_archive_bytes,
    'input_archive_sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
    'selection': 'Every direct historical entry except PNG/PDF/TAR, plus direct JSON entries at least1000000bytes; all exact original paths retained.',
    'standard_tar': metrics,
    'zip_method': 'ZIP_LZMA',
    'dictionary_bytes': decoded_options['dict_size'],
    'zip_lzma_properties_hex': props.hex(),
    'standard_zip_lzma_stream_bytes': encoded_bytes,
    'standard_zip_lzma_stream_sha256': encoded_sha.hexdigest(),
    'existing_compressed_payload_bytes_replaced': replaced_compressed,
    'payload_saving_bytes': replaced_compressed - encoded_bytes,
    'equivalent_checkpoint29_bytes_before_header_adjustment': equivalent_bytes,
    'delivery_cap_bytes': 536870912,
    'equivalent_remaining_bytes_before_new_work': 536870912 - equivalent_bytes,
    'unchanged_standard_library_decoder_roundtrip': 'PASS_EVERY_BYTE_SHA256_AND_LENGTH',
    'decoder_eof': decoder.eof,
    'compression_seconds': time.monotonic() - compression_started,
    'elapsed_seconds': time.monotonic() - begin,
    'creates_zip': False,
    'mutates_earlier_archive': False,
    'new_work_estimate': False,
    'scope': 'Actual full-byte compression and decode of one deterministic standard TAR. The equivalent archive size retains existing ZIP headers conservatively and is not a prospective checkpoint30 size estimate. No extra archive, custom decompressor, content deletion, or lossy change.',
}
destination.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2), flush=True)
