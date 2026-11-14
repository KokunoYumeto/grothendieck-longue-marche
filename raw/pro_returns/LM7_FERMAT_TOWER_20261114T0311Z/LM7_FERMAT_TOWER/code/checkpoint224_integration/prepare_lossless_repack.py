"""Preserve the checked deflate build and the actual upload size failure."""
from pathlib import Path
import hashlib
import json
import shutil

BASE = Path(__file__).resolve().parents[2]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
archive = BASE.parent / 'LM7_FERMAT_TOWER.zip'
assert archive.stat().st_size == 590447556
assert sha(archive) == '66160b5cd97c098977fcc49a71292c1736aa0ba791f6a3d6bbb5bf27ba8cc56a'
history = BASE / 'code/checkpoint224_integration/history/deflate_size_limit'
assert not history.exists()
history.mkdir(parents=True)
for source, target in [
    (BASE / 'code/package.py', 'package.py'),
    (BASE.parent / 'root_package224.out', 'package.out'),
    (BASE.parent / 'root_package224.err', 'package.err'),
    (BASE / 'LM7_FERMAT_TOWER_manifest.json', 'archive_manifest.json'),
    (BASE.parent / '.lm7_archive224_readback.json', 'archive_readback.json'),
]:
    shutil.copy2(source, history / target)
assert (history / 'package.out').stat().st_size > 0
assert (history / 'package.err').stat().st_size == 0
failure = {
    'operation': 'replace_library_file',
    'status': 'client_upload_rejected_size_limit',
    'library_file_id': 'libfile_39e042d09a208191924626b6d11b16fa',
    'expected_current_version': 19,
    'uploaded_version_created': False,
    'archive_bytes': archive.stat().st_size,
    'maximum_bytes': 536870912,
    'archive_sha256': sha(archive),
    'actual_tool_error': 'tool call error: failed to upload `/workspace/scratch/e34c61ec5a35/LM7_FERMAT_TOWER.zip` for `file`: file `/workspace/scratch/e34c61ec5a35/LM7_FERMAT_TOWER.zip` is too large: 590447556 bytes exceeds the limit of 536870912 bytes',
    'remedy': 'Use the standard ZIP LZMA method for large binary and JSON certificates, preserving every filename and every uncompressed byte. Retain deflate for all other files.',
    'round_trip_benchmark': 'code/checkpoint224_integration/benchmark_archive_codec.out',
}
path = BASE / 'ledger/checkpoint224_upload_size_limit.json'
path.write_text(json.dumps(failure, indent=2) + '\n')
print(json.dumps({
    'status': 'PASS', 'history': str(history.relative_to(BASE)),
    'upload_failure_record': str(path.relative_to(BASE)),
    'failure_record_sha256': sha(path),
    'all_original_content_preserved': True,
}, indent=2))
