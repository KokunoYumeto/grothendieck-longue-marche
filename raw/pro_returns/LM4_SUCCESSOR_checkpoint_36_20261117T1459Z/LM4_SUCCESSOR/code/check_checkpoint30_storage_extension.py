"""Meaningful compatibility/standard-stream check without creating any ZIP."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import struct
import zipfile
from checkpoint_archive_io import CheckpointReader
from checkpoint_data_tar import DataLZMACompressor, DATA_DICTIONARY_BYTES, standard_data_dictionary, is_data_bundle_member

root = Path(__file__).resolve().parents[1]
archive = root.parent / 'LM4_SUCCESSOR_checkpoint_29.zip'
prefix = 'LM4_SUCCESSOR/'
destination = root / 'records/checkpoint30_storage_extension_check.json'
assert not destination.exists()
before = hashlib.sha256(archive.read_bytes()).hexdigest()
assert before == '6c1af28a43117d684f484caf54372bcfa665fedd44a11a11787679b82d6b402a'
with CheckpointReader(archive) as reader:
    assert reader.data_tar is None and reader.data_members == {}
    assert len(reader.names()) == 8738
    assert hashlib.sha256(reader.read(prefix+'LM4_SUCCESSOR_paper.pdf')).hexdigest() == 'a9eb34502bd1c59fa683bcb9007a638aec57db2f81a74c2767e96766df3818f8'
    sample_path = 'work_CE/next_symmetric_nodes/symmetric_node_braids.json'
    sample = reader.read(prefix + sample_path)
    assert is_data_bundle_member(sample_path, len(sample))
    assert not is_data_bundle_member('checkpoint_history/example/page.png', 2_000_000)
    assert not is_data_bundle_member('checkpoint_history/example/paper.pdf', 2_000_000)
    assert not is_data_bundle_member('LM4_SUCCESSOR_paper.pdf', 2_000_000)
    assert is_data_bundle_member('checkpoint_history/example/proof.tex', 100)
    assert not is_data_bundle_member('sections/current_proof.tex', 100)
print('PASS latest actual two-container archive is unchanged under the extended reader.', flush=True)

original = zipfile.LZMACompressor
with standard_data_dictionary():
    compressor = zipfile._get_compressor(zipfile.ZIP_LZMA)
    assert isinstance(compressor, DataLZMACompressor)
    encoded = compressor.compress(sample) + compressor.flush()
assert zipfile.LZMACompressor is original
props_size, = struct.unpack('<H', encoded[2:4])
assert encoded[:2] == bytes([9, 4]) and props_size == 5
dictionary, = struct.unpack('<I', encoded[5:9])
assert dictionary == DATA_DICTIONARY_BYTES
decoder = zipfile.LZMADecompressor()
restored = decoder.decompress(encoded)
assert decoder.eof and restored == sample

class ExpectedContextExit(Exception):
    pass

try:
    with standard_data_dictionary():
        assert zipfile.LZMACompressor is DataLZMACompressor
        raise ExpectedContextExit()
except ExpectedContextExit:
    pass
assert zipfile.LZMACompressor is original
assert hashlib.sha256(archive.read_bytes()).hexdigest() == before
record = {
    'completed_at': datetime.now(timezone.utc).isoformat(),
    'old_actual_archive_logical_count': 8738,
    'backward_reader_compatibility': 'PASS',
    'actual_input': sample_path,
    'input_bytes': len(sample),
    'input_sha256': hashlib.sha256(sample).hexdigest(),
    'standard_zip_lzma_stream_bytes': len(encoded),
    'dictionary_bytes': dictionary,
    'unchanged_standard_decoder_roundtrip': 'PASS_EXACT_BYTES',
    'dictionary_context_normal_and_exception_restore': 'PASS',
    'original_archive_sha256': before,
    'original_archive_unchanged': True,
    'creates_zip': False,
    'scope': 'Actual legacy reader path and current ZIP method14 compressor dispatch/framing/roundtrip, without making a test archive. The sole actual checkpoint30 will receive complete manifest and independent native three-container restoration verification after capture.'
}
destination.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2), flush=True)
