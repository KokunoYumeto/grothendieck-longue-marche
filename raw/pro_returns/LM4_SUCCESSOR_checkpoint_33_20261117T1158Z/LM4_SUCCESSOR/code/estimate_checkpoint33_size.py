"""Conservative actual-byte checkpoint33 estimate; never creates a ZIP.

Run only after root confirms final renders. It snapshots current authored
bytes, predicts all changed checkpoint32 logical bytes at historical paths,
then builds/compresses the exact three prospective standard-TAR buckets.
Old changed direct costs remain in the baseline as a deliberate overcount.
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

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT.parent / 'LM4_SUCCESSOR_checkpoint_32.zip'
PREFIX = 'LM4_SUCCESSOR/'
CONTAINERS = ('verification_images.tar', 'historical_documents.tar', 'historical_data.tar')
ALLOWANCE = 5_000_000
CAP = 536_870_912
REWRITTEN = {'records/checkpoint_version_retention.csv',
             'records/checkpoint_version_retention_summary.json',
             'checkpoint_history/README.md'}

def digest(data):
    return hashlib.sha256(data).hexdigest()

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
    target = ROOT/'records/checkpoint33_size_estimate.json'
    assert not target.exists(), 'Preserve any preceding estimate before rerunning'
    print('Snapshotting current authored bytes after final render completion', flush=True)
    prospective = {}
    for path in sorted(ROOT.rglob('*')):
        if path.is_file() and included(path):
            prospective[str(path.relative_to(ROOT))] = path.read_bytes()
    original_current_paths = set(prospective)
    predicted_history = []
    removed_containers = {}
    removed_direct_data = []
    old = {}
    with CheckpointReader(ARCHIVE) as prior:
        manifest_name = PREFIX+'records/checkpoint_32_contents_sha256.tsv'
        manifest_data = prior.read(manifest_name)
        rows = list(csv.DictReader(io.StringIO(manifest_data.decode()), delimiter='\t'))
        old = {row['path']: row for row in rows}
        assert len(old) == len(rows)
        # A SHA manifest intentionally omits its own row, but retention includes it.
        own_rel = manifest_name[len(PREFIX):]
        old[own_rel] = {'path': own_rel, 'bytes': str(len(manifest_data)), 'sha256': digest(manifest_data)}
        assert set(PREFIX+rel for rel in old) == set(prior.names())
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
            historical = 'checkpoint_history/checkpoint_32/'+rel
            if historical in prospective:
                assert prospective[historical] == data, ('Historical path collision', historical)
            else:
                prospective[historical] = data
                predicted_history.append({'path': historical, 'bytes': len(data), 'sha256': row['sha256']})
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
    del prospective
    bundle_reports = {}
    for kind in ('images', 'documents', 'data'):
        bundle, metrics = build_standard_tar(groups.pop(kind))
        method = 'data-lzma' if kind in {'images','data'} else 'lzma'
        start = time.monotonic()
        print('Compressing actual prospective', kind, 'TAR', json.dumps(metrics), flush=True)
        size = compress_size(bundle, method, progress=kind)
        bundle_reports[kind] = {'metrics': metrics, 'compressed_bytes': size, 'zip_method': 'ZIP_LZMA',
                                'dictionary_bytes': DATA_DICTIONARY_BYTES if kind in {'images','data'} else 8*1024*1024,
                                'elapsed_seconds': time.monotonic()-start}
        print('Completed', kind, 'compressed_bytes', size, flush=True)
        del bundle
    direct_added = sum(size for size, _ in new_direct)
    migrated_removed = sum(size for size, _ in removed_direct_data)
    estimate = ARCHIVE.stat().st_size-sum(removed_containers.values())-migrated_removed+sum(x['compressed_bytes'] for x in bundle_reports.values())+direct_added
    archive_sha = hashlib.sha256()
    with ARCHIVE.open('rb') as stream:
        for part in iter(lambda: stream.read(1 << 20), b''):
            archive_sha.update(part)
    report = {
        'started_at': started.isoformat(), 'recorded_at': datetime.now(timezone.utc).isoformat(),
        'baseline_archive': ARCHIVE.name, 'baseline_bytes': ARCHIVE.stat().st_size,
        'baseline_sha256': archive_sha.hexdigest(),
        'previous_container_compressed_bytes_removed': removed_containers,
        'previous_direct_data_entries_migrated': len(removed_direct_data),
        'previous_direct_data_compressed_bytes_removed': migrated_removed,
        'prospective_bundles': bundle_reports,
        'current_authored_paths_snapshotted': len(original_current_paths),
        'predicted_checkpoint32_historical_paths': len(predicted_history),
        'predicted_checkpoint32_historical_bytes': sum(x['bytes'] for x in predicted_history),
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
        'scope': 'Actual checkpoint32 baseline; all three old containers and all old direct data payloads now migrated to the new data TAR are removed. Complete current and predicted historical image/document/data TARs are rebuilt from actual bytes with standard hardlinks. Images and data use the actual64MiB ZIP-LZMA compressor; historical documents use the default8MiB compressor. Changed old direct payload costs remain conservatively in the baseline while every new direct payload is added. The previous direct main PDF is also counted in the historical document TAR, deliberately overcounting it. Forced retention-index history and every changed32 logical version are predicted under checkpoint_history/checkpoint_32; actual older identical-version reuse can only reduce those paths. Existing archive headers remain counted. FiveMB covers new headers, manifests, retention-record growth, and late text. Final immutable size remains authoritative.'
    }
    target.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'predicted_history'}, indent=2), flush=True)
    assert estimate+ALLOWANCE < CAP, 'Conservative estimate exceeds the delivery cap; report retained'

if __name__ == '__main__':
    main()
