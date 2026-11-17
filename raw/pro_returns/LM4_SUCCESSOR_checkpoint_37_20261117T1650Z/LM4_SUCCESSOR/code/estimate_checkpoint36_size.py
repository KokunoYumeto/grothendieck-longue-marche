"""Conservative actual-byte checkpoint36 estimate; never creates a ZIP.

Run only after root confirms final renders. It snapshots current authored
bytes, predicts all changed checkpoint35 logical bytes at historical paths,
then builds/compresses the exact three prospective standard-TAR buckets.
Old changed direct costs remain conservatively, except the proved direct-to-document migration of the old main PDF.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json
import time
import zipfile
import zlib
from checkpoint_archive_io import CheckpointReader
from checkpoint_standard_tar import build_standard_tar
from checkpoint_data_tar import is_data_bundle_member, DataLZMACompressor, DATA_DICTIONARY_BYTES
from checkpoint_image_tar import ImageLZMACompressor, IMAGE_DICTIONARY_BYTES

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT.parent / 'LM4_SUCCESSOR_checkpoint_35.zip'
BASELINE_BYTES = 530_938_760
BASELINE_SHA256 = '33b0925ca3ba12d8944fc47243807a3c61ebb2a4f03ec47f7bb2ce1a5a83f121'
PARENT_LOGICAL_PATHS = 10_746
PARENT_RETENTION_ROWS = 163_040
EXPECTED_IMAGE_HELPER_SHA256 = 'c3de17157c5d6fa5ac66bfc64717df096c3dbcc195965be1a7d91c878df352f6'
EXPECTED_PACKAGER_SHA256 = 'cf0a5219cf66ec07e7f8509634888392929fb1eced6f05748e35d462052938dc'
PREFIX = 'LM4_SUCCESSOR/'
CONTAINERS = ('verification_images.tar', 'historical_documents.tar', 'historical_data.tar')
ALLOWANCE = 5_000_000
CAP = 536_870_912
REWRITTEN = {'records/checkpoint_version_retention.csv',
             'records/checkpoint_version_retention_summary.json',
             'checkpoint_history/README.md'}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def hash_path(path):
    sha = hashlib.sha256()
    with path.open('rb') as stream:
        for part in iter(lambda: stream.read(1 << 20), b''):
            sha.update(part)
    return sha.hexdigest()

def included(path):
    """Exact current package_checkpoint authored-file exclusion predicates."""
    rel = str(path.relative_to(ROOT))
    if rel in CONTAINERS or rel.startswith('tex_cache/'):
        return False
    if rel.startswith('work_CE/') and path.parent == ROOT/'work_CE' and (path.name.startswith('D_') or path.name.startswith('LM6_')):
        return False
    if rel.startswith('work_DE/') and path.name.endswith('_source.txt'):
        return False
    if 'work_CE/sources/' in rel and path.suffix.lower() in {'.pdf', '.txt'}:
        return False
    if (rel.startswith('work_DE/') and path.name not in {'B118_initial_spacing.pdf', 'B122_initial_layout.pdf', 'B128_initial_comma.pdf'}
            and not path.with_suffix('.tex').exists()
            and (path.suffix.lower() == '.pdf' or (path.suffix.lower() == '.txt' and path.with_suffix('.pdf').exists()
                 and path.stem not in {'DE_review', 'B_separability_review'}))):
        return False
    if '__pycache__' in path.parts or path.suffix in {'.aux', '.toc', '.blg', '.bbl'}:
        return False
    return True

def bucket(rel, size):
    suffix = Path(rel).suffix.lower()
    if suffix == '.png':
        return 'images'
    if suffix == '.pdf' and rel != 'LM4_SUCCESSOR_paper.pdf':
        return 'documents'
    if is_data_bundle_member(rel, size):
        return 'data'
    return 'direct'

def compress_size(data, method, progress=None):
    """Count actual compressor output incrementally, retaining no archive."""
    if method == 'deflate':
        compressor = zlib.compressobj(6, zlib.DEFLATED, -15)
    elif method == 'image-lzma':
        compressor = ImageLZMACompressor()
    elif method == 'data-lzma':
        compressor = DataLZMACompressor()
    else:
        compressor = zipfile.LZMACompressor()
    total = 0
    last_report = time.monotonic()
    for offset in range(0, len(data), 1 << 20):
        total += len(compressor.compress(data[offset:offset+(1 << 20)]))
        if progress and time.monotonic()-last_report >= 25:
            print(progress, 'input_bytes_processed', min(offset+(1 << 20), len(data)), 'of', len(data), flush=True)
            last_report = time.monotonic()
    total += len(compressor.flush())
    return total

def main():
    started = datetime.now(timezone.utc)
    target = ROOT/'records/checkpoint36_size_estimate.json'
    assert not target.exists(), 'Preserve any preceding estimate before rerunning'
    assert ARCHIVE.stat().st_size == BASELINE_BYTES
    assert hash_path(ARCHIVE) == BASELINE_SHA256
    assert IMAGE_DICTIONARY_BYTES == 128 * 1024 * 1024
    assert DATA_DICTIONARY_BYTES == 64 * 1024 * 1024
    assert hash_path(ROOT/'code/checkpoint_image_tar.py') == EXPECTED_IMAGE_HELPER_SHA256
    assert hash_path(ROOT/'code/package_checkpoint.py') == EXPECTED_PACKAGER_SHA256, 'Install the reviewed36 image128 proposal before estimating'
    source_bindings = {rel: {'sha256': hash_path(ROOT/rel), 'bytes': (ROOT/rel).stat().st_size}
                       for rel in ('code/estimate_checkpoint36_size.py', 'code/package_checkpoint.py',
                                   'code/checkpoint_image_tar.py', 'code/checkpoint_data_tar.py',
                                   'code/checkpoint_standard_tar.py', 'code/checkpoint_archive_io.py')}
    print('Snapshotting current authored bytes after final render completion', flush=True)
    prospective = {}
    for path in sorted(ROOT.rglob('*')):
        if path.is_file() and included(path):
            prospective[str(path.relative_to(ROOT))] = path.read_bytes()
    original_current_paths = set(prospective)
    predicted_history = []
    removed_containers = {}
    removed_direct_data = []
    removed_direct_main_pdf = None
    old = {}
    with CheckpointReader(ARCHIVE) as prior:
        manifest_name = PREFIX+'records/checkpoint_35_contents_sha256.tsv'
        manifest_data = prior.read(manifest_name)
        rows = list(csv.DictReader(io.StringIO(manifest_data.decode()), delimiter='\t'))
        old = {row['path']: row for row in rows}
        assert len(old) == len(rows)
        # A SHA manifest intentionally omits its own row, but retention includes it.
        own_rel = manifest_name[len(PREFIX):]
        old[own_rel] = {'path': own_rel, 'bytes': str(len(manifest_data)), 'sha256': digest(manifest_data)}
        assert set(PREFIX+rel for rel in old) == set(prior.names())
        assert len(old) == PARENT_LOGICAL_PATHS
        parent_retention = prior.read(PREFIX+'records/checkpoint_version_retention.csv')
        parent_retention_rows = sum(1 for _ in csv.DictReader(io.StringIO(parent_retention.decode())))
        assert parent_retention_rows == PARENT_RETENTION_ROWS
        del parent_retention
        for basename in CONTAINERS:
            name = PREFIX+basename
            if name in prior.direct:
                removed_containers[basename] = prior.z.getinfo(name).compress_size
        # All previous direct data entries move into the actual new data TAR.
        # Their ZIP headers stay counted in the baseline, conservatively.
        for info in prior.z.infolist():
            if info.is_dir() or info.filename in {PREFIX+x for x in CONTAINERS}:
                continue
            rel = info.filename[len(PREFIX):]
            if is_data_bundle_member(rel, info.file_size):
                removed_direct_data.append((info.compress_size, rel))
        for rel, row in old.items():
            active = prospective.get(rel)
            unchanged = (active is not None and len(active) == int(row['bytes']) and digest(active) == row['sha256'])
            if unchanged and rel not in REWRITTEN:
                continue
            data = prior.read(PREFIX+rel)
            assert len(data) == int(row['bytes']) and digest(data) == row['sha256']
            historical = 'checkpoint_history/checkpoint_35/'+rel
            if historical in prospective:
                assert prospective[historical] == data, ('Historical path collision', historical)
            else:
                prospective[historical] = data
                predicted_history.append({'path': historical, 'bytes': len(data), 'sha256': row['sha256']})
            if rel == 'LM4_SUCCESSOR_paper.pdf':
                info = prior.z.getinfo(PREFIX+rel)
                assert PREFIX+rel in prior.direct and info.compress_type == zipfile.ZIP_DEFLATED
                assert not unchanged and info.file_size == len(data)
                assert bucket(historical, len(data)) == 'documents'
                assert prospective[historical] == data
                assert not is_data_bundle_member(rel, len(data))
                removed_direct_main_pdf = {'path': rel, 'historical_path': historical,
                    'bytes': len(data), 'sha256': digest(data),
                    'compressed_payload_bytes': info.compress_size,
                    'headers_removed': 0, 'reason': 'The same exact old direct PDF is measured once in the prospective document TAR.'}
    print('Prospective logical files', len(prospective), 'predicted historical paths', len(predicted_history), flush=True)
    groups = {name: [] for name in ('images', 'documents', 'data')}
    new_direct = []
    current_main_sha = None
    for rel, data in sorted(prospective.items()):
        kind = bucket(rel, len(data))
        if kind != 'direct':
            groups[kind].append((rel, data))
            continue
        if rel == 'LM4_SUCCESSOR_paper.pdf':
            current_main_sha = digest(data)
        row = old.get(rel)
        if row and len(data) == int(row['bytes']) and digest(data) == row['sha256']:
            continue
        method = 'deflate' if Path(rel).suffix.lower() in {'.pdf', '.jpg', '.jpeg', '.gif', '.zip', '.gz', '.xz', '.tar'} else 'lzma'
        new_direct.append((compress_size(data, method), rel))
    if removed_direct_main_pdf is not None:
        documents = dict(groups['documents'])
        old_pdf = documents[removed_direct_main_pdf['historical_path']]
        assert len(old_pdf) == removed_direct_main_pdf['bytes']
        assert digest(old_pdf) == removed_direct_main_pdf['sha256']
        assert any(rel == 'LM4_SUCCESSOR_paper.pdf' for _, rel in new_direct)
        assert all(rel != 'LM4_SUCCESSOR_paper.pdf' for _, rel in removed_direct_data)
        del documents, old_pdf
    del prospective
    bundle_reports = {}
    for kind in ('images', 'documents', 'data'):
        bundle, metrics = build_standard_tar(groups.pop(kind))
        method = 'image-lzma' if kind == 'images' else 'data-lzma'
        dictionary_bytes = IMAGE_DICTIONARY_BYTES if kind == 'images' else DATA_DICTIONARY_BYTES
        start = time.monotonic()
        print('Compressing actual prospective', kind, 'TAR', json.dumps(metrics), flush=True)
        size = compress_size(bundle, method, progress=kind)
        bundle_reports[kind] = {'metrics': metrics, 'compressed_bytes': size, 'zip_method': 'ZIP_LZMA',
                                'dictionary_bytes': dictionary_bytes,
                                'elapsed_seconds': time.monotonic()-start}
        print('Completed', kind, 'compressed_bytes', size, flush=True)
        del bundle
    direct_added = sum(size for size, _ in new_direct)
    migrated_removed = sum(size for size, _ in removed_direct_data)
    main_removed = 0 if removed_direct_main_pdf is None else removed_direct_main_pdf['compressed_payload_bytes']
    estimate = ARCHIVE.stat().st_size-sum(removed_containers.values())-migrated_removed-main_removed+sum(x['compressed_bytes'] for x in bundle_reports.values())+direct_added
    archive_sha = hashlib.sha256()
    with ARCHIVE.open('rb') as stream:
        for part in iter(lambda: stream.read(1 << 20), b''):
            archive_sha.update(part)
    assert ARCHIVE.stat().st_size == BASELINE_BYTES and archive_sha.hexdigest() == BASELINE_SHA256
    for rel, binding in source_bindings.items():
        assert (ROOT/rel).stat().st_size == binding['bytes'] and hash_path(ROOT/rel) == binding['sha256'], ('Source changed during estimate', rel)
    report = {
        'started_at': started.isoformat(), 'recorded_at': datetime.now(timezone.utc).isoformat(),
        'baseline_archive': ARCHIVE.name, 'baseline_bytes': ARCHIVE.stat().st_size,
        'baseline_sha256': archive_sha.hexdigest(),
        'baseline_identity_verified_before_and_after': True,
        'parent_logical_paths': PARENT_LOGICAL_PATHS,
        'parent_retention_rows': parent_retention_rows,
        'source_bindings': source_bindings,
        'previous_container_compressed_bytes_removed': removed_containers,
        'previous_direct_data_entries_migrated': len(removed_direct_data),
        'previous_direct_data_compressed_bytes_removed': migrated_removed,
        'previous_direct_main_pdf_migrated': removed_direct_main_pdf,
        'previous_direct_main_pdf_compressed_payload_removed': main_removed,
        'previous_direct_main_pdf_headers_removed': 0,
        'prospective_bundles': bundle_reports,
        'current_authored_paths_snapshotted': len(original_current_paths),
        'predicted_checkpoint35_historical_paths': len(predicted_history),
        'predicted_checkpoint35_historical_bytes': sum(x['bytes'] for x in predicted_history),
        'predicted_history': predicted_history,
        'new_or_changed_direct_paths_counted': len(new_direct),
        'additional_direct_compressed_payload_bytes': direct_added,
        'largest_new_direct_payloads': sorted(new_direct, reverse=True)[:20],
        'current_main_pdf_sha256': current_main_sha,
        'estimated_before_allowance': estimate,
        'header_manifest_retention_late_text_allowance_bytes': ALLOWANCE,
        'estimated_total_with_allowance': estimate+ALLOWANCE,
        'delivery_cap_bytes': CAP, 'estimated_headroom_bytes': CAP-estimate-ALLOWANCE,
        'creates_zip': False, 'writes_authored_input_files': False,
        'scope': 'Actual checkpoint35 baseline; all three old containers and all old direct data payloads now migrated to the new data TAR are removed. Complete current and predicted historical image/document/data TARs are rebuilt from actual bytes with standard hardlinks. The complete prospective36 image bucket uses the actual128MiB ImageLZMACompressor; documents and data use the actual64MiB DataLZMACompressor. No saving from the separate closed35 image measurement is substituted. Changed old direct payload costs otherwise remain conservatively while every new direct payload is added. The old direct main PDF compressed payload is subtracted exactly once only when its identical size/hash bytes are explicitly present in the measured prospective document TAR and the changed current main PDF is counted separately. Its headers remain counted; it is not part of the removed data payloads. Forced retention-index history and every changed35 logical version are predicted under checkpoint_history/checkpoint_35; actual older identical-version reuse can only reduce those paths. Existing archive headers remain counted. FiveMB covers new headers, manifests, retention-record growth, and late text. Final immutable size remains authoritative.'
    }
    target.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'predicted_history'}, indent=2), flush=True)
    assert estimate+ALLOWANCE < CAP, 'Conservative estimate exceeds the delivery cap; report retained'

if __name__ == '__main__':
    main()
