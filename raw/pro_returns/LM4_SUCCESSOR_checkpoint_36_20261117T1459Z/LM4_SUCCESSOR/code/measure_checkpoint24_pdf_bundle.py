"""Measure and independently restore a solid PDF container; create no ZIP.

Input is the immutable actual checkpoint23. Historical and preview PDFs
are read at their original paths. Its current main PDF is also included
under the exact historical path that checkpoint24 will need if the paper
changes. The next current main PDF will remain a direct ZIP entry.
"""
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import tarfile
import tempfile
import zipfile
from checkpoint_standard_tar import build_standard_tar

root = Path(__file__).resolve().parents[1]
archive = root.parent / 'LM4_SUCCESSOR_checkpoint_23.zip'
assert hashlib.sha256(archive.read_bytes()).hexdigest() == '6986909bd5d014a6c006736635de97032490273d4548562b57792aa7ffd90dd1'
prefix = 'LM4_SUCCESSOR/'
main = prefix + 'LM4_SUCCESSOR_paper.pdf'
with zipfile.ZipFile(archive) as z:
    entries = [i for i in z.infolist() if i.filename.lower().endswith('.pdf') and i.filename != main]
    files = [(i.filename[len(prefix):], z.read(i)) for i in entries]
    future_history = 'checkpoint_history/checkpoint_23/LM4_SUCCESSOR_paper.pdf'
    assert future_history not in dict(files)
    files.append((future_history, z.read(main)))
    prior_individual_compressed = sum(i.compress_size for i in entries)

bundle, metrics = build_standard_tar(files)
compressor = zipfile.LZMACompressor()
compressed = compressor.compress(bundle) + compressor.flush()
restored = zipfile.LZMADecompressor().decompress(compressed)
assert restored == bundle
expected = {prefix + name: data for name, data in files}
with tempfile.TemporaryDirectory(prefix='lm4-checkpoint24-pdf-measure-') as directory:
    temp = Path(directory)
    tar_path = temp / 'historical_documents.tar'
    tar_path.write_bytes(restored)
    seen = {}
    with tarfile.open(tar_path, 'r:') as tf:
        for member in tf.getmembers():
            path = PurePosixPath(member.name)
            assert not path.is_absolute() and '..' not in path.parts
            assert member.name in expected and member.name not in seen
            assert member.isfile() or member.islnk()
            if member.islnk():
                assert seen.get(member.linkname) == 'regular'
            seen[member.name] = 'regular' if member.isfile() else 'hardlink'
    assert set(seen) == set(expected)
    subprocess.run(['tar', '-xf', str(tar_path)], cwd=temp, check=True)
    for name, original in expected.items():
        actual = temp / name
        assert actual.is_file() and not actual.is_symlink()
        assert actual.read_bytes() == original, name

estimate = archive.stat().st_size - prior_individual_compressed + len(compressed)
out = {
    'recorded_at': datetime.now(timezone.utc).isoformat(),
    'input_archive': archive.name,
    'input_archive_bytes': archive.stat().st_size,
    'input_archive_sha256': '6986909bd5d014a6c006736635de97032490273d4548562b57792aa7ffd90dd1',
    'measurement_creates_checkpoint_zip': False,
    'input_pdf_paths_except_current': len(entries),
    'additional_projected_history_path': future_history,
    'tar_metrics': metrics,
    'previous_individual_pdf_compressed_bytes': prior_individual_compressed,
    'solid_zip_lzma_payload_bytes': len(compressed),
    'estimated_baseline_with_new_encoding': estimate,
    'allowance_for_next_interval_bytes': 30000000,
    'estimated_with_allowance': estimate + 30000000,
    'delivery_cap_bytes': 536870912,
    'lzma_exact_roundtrip': 'PASS',
    'system_tar_restore_every_original_pdf_path_and_byte': 'PASS',
    'archive23_unchanged': 'PASS',
    'scope': 'Measured actual checkpoint23 PDF bytes plus its prospective next historical main PDF. Future changes require a fresh total size estimate before capture24.',
}
assert hashlib.sha256(archive.read_bytes()).hexdigest() == out['input_archive_sha256']
(root / 'records/checkpoint24_pdf_bundle_measurement.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
