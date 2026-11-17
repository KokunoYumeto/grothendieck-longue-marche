"""Conservative actual-byte checkpoint37 estimate; never creates a ZIP.

Run only after root confirms final renders. It snapshots current authored
bytes, predicts all changed checkpoint36 logical bytes at historical paths,
then stages the exact three prospective standard-TAR buckets. Verified prior
image/document worker measurements are reused only after exact fresh input
and unchanged codec checks; the expanded data stream is measured anew.
Old changed direct costs remain conservatively, except the proved direct-to-document migration of the old main PDF.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json
import time
import subprocess
import sys
import tempfile
import zipfile
import zlib
from checkpoint_archive_io import CheckpointReader
from checkpoint37_streaming import write_standard_tar, measure_staged_tar, json_exclusive, identity
from checkpoint_data_tar import is_data_bundle_member, DataLZMACompressor, DATA_DICTIONARY_BYTES
from checkpoint_image37_tar import Image37LZMACompressor, IMAGE37_DICTIONARY_BYTES
from checkpoint_document37_tar import Document37LZMACompressor, DOCUMENT37_DICTIONARY_BYTES

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT.parent / 'LM4_SUCCESSOR_checkpoint_36.zip'
BASELINE_BYTES = 529_083_340
BASELINE_SHA256 = '9279885c2a7ab2d1d5396f57c4e372e6fa672b5f7f6dcd4a6965df07297f3f8e'
PARENT_LOGICAL_PATHS = 11_156
PARENT_RETENTION_ROWS = 173_786
EXPECTED_IMAGE_HELPER_SHA256 = '055fa383e1bacef045f2351df86fa4d50464956c8d6c1367d78c53cf7b7cd4b5'
EXPECTED_DOCUMENT_HELPER_SHA256 = 'e9d3e34a645bfa149b6eabe6ec26ca0e025907263be72f56e3a5467a5e0df3d3'
EXPECTED_PACKAGER_SHA256 = '7db100dc8febe319482220710f5022c488caad36b663f21239eecfcfc4ae481d'
EXPECTED_STREAMING_HELPER_SHA256 = '65b3d069c83438838577f41046127c400d07de2cc1db3768feee3471c49dab17'
EXPECTED_DATA_HELPER_SHA256 = 'a0c2a19f0c3c59dc1f487bb91e85a3c5a67ac639cd663f677200e869ee61ad40'
PRIOR_OBSERVED = 'records/checkpoint37_failed_size_cap_observed.json'
PRIOR_OBSERVED_SHA256 = 'f12f63efe3f42f636a52a87f4020d1dd121a06866b3623062a4da9e86a8eff90'
PRIOR_CERTIFICATE = 'records/checkpoint37_failed_size_cap/records/checkpoint37_size_estimate.json'
PRIOR_CERTIFICATE_SHA256 = '79b015a2c122b27f1d8b4feea4cc600532d6583b542c4018c2dcc2e04c54274e'
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
    if is_data_bundle_member(rel, size, 37):
        return 'data'
    return 'direct'

def compress_size(data, method):
    """Only small direct entries; large TAR codecs run in isolated workers."""
    compressor = (zlib.compressobj(6, zlib.DEFLATED, -15)
                  if method == 'deflate' else zipfile.LZMACompressor())
    total = 0
    for offset in range(0, len(data), 1 << 20):
        total += len(compressor.compress(data[offset:offset+(1 << 20)]))
    return total + len(compressor.flush())


def stage_snapshot(stage):
    stage = Path(stage)
    assert stage.parent == ROOT.parent.resolve() and stage.name.startswith('.checkpoint37_estimate_stage_')
    assert stage.is_dir() and not any(stage.iterdir())
    started = datetime.now(timezone.utc)
    target = ROOT/'records/checkpoint37_size_estimate.json'
    assert not target.exists(), 'Preserve any preceding estimate before rerunning'
    assert ARCHIVE.stat().st_size == BASELINE_BYTES
    assert hash_path(ARCHIVE) == BASELINE_SHA256
    assert IMAGE37_DICTIONARY_BYTES == 512 * 1024 * 1024
    assert DOCUMENT37_DICTIONARY_BYTES == 256 * 1024 * 1024
    assert DATA_DICTIONARY_BYTES == 64 * 1024 * 1024
    assert hash_path(ROOT/'code/checkpoint_data_tar.py') == EXPECTED_DATA_HELPER_SHA256
    assert hash_path(ROOT/'code/checkpoint_image37_tar.py') == EXPECTED_IMAGE_HELPER_SHA256
    assert hash_path(ROOT/'code/checkpoint_document37_tar.py') == EXPECTED_DOCUMENT_HELPER_SHA256
    assert hash_path(ROOT/'code/package_checkpoint.py') == EXPECTED_PACKAGER_SHA256, 'Install the reviewed37 staged-streaming packager before estimating'
    assert hash_path(ROOT/'code/checkpoint37_streaming.py') == EXPECTED_STREAMING_HELPER_SHA256
    source_bindings = {rel: {'sha256': hash_path(ROOT/rel), 'bytes': (ROOT/rel).stat().st_size}
                       for rel in ('code/estimate_checkpoint37_size.py', 'code/package_checkpoint.py',
                                   'code/checkpoint_image37_tar.py', 'code/checkpoint_document37_tar.py',
                                   'code/checkpoint_data_tar.py', 'code/checkpoint37_streaming.py',
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
        manifest_name = PREFIX+'records/checkpoint_36_contents_sha256.tsv'
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
            if is_data_bundle_member(rel, info.file_size, 37):
                removed_direct_data.append((info.compress_size, rel))
        for rel, row in old.items():
            active = prospective.get(rel)
            unchanged = (active is not None and len(active) == int(row['bytes']) and digest(active) == row['sha256'])
            if unchanged and rel not in REWRITTEN:
                continue
            data = prior.read(PREFIX+rel)
            assert len(data) == int(row['bytes']) and digest(data) == row['sha256']
            historical = 'checkpoint_history/checkpoint_36/'+rel
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
                assert not is_data_bundle_member(rel, len(data), 37)
                removed_direct_main_pdf = {'path': rel, 'historical_path': historical,
                    'bytes': len(data), 'sha256': digest(data),
                    'compressed_payload_bytes': info.compress_size,
                    'headers_removed': 0, 'reason': 'The same exact old direct PDF is measured once in the prospective document TAR.'}
    # Every removed baseline direct payload has its complete old version in
    # this exact prospective data snapshot, at its current or historical path.
    # No ZIP header is subtracted, and no removal is based only on a suffix.
    migration_witnesses = []
    for compressed_bytes, rel in removed_direct_data:
        row = old[rel]
        stored = rel
        data = prospective.get(stored)
        if data is None or len(data) != int(row['bytes']) or digest(data) != row['sha256']:
            stored = 'checkpoint_history/checkpoint_36/'+rel
            data = prospective[stored]
        assert len(data) == int(row['bytes']) and digest(data) == row['sha256']
        assert bucket(stored, len(data)) == 'data'
        migration_witnesses.append({'old_direct_path': rel, 'data_tar_path': stored,
                                   'bytes': len(data), 'sha256': row['sha256'],
                                   'old_compressed_payload_bytes': compressed_bytes,
                                   'headers_removed': 0})
    assert len({x['old_direct_path'] for x in migration_witnesses}) == len(removed_direct_data)
    # The closed reader can retain decoded historical TAR buffers until its
    # object dies; release it before allocating any large encoder.
    del prior
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
    bundle_metrics = {}
    for kind in ('images', 'documents', 'data'):
        metrics = write_standard_tar(groups.pop(kind), stage/(kind+'.tar'))
        # Bind this complete current frozen snapshot, including every newly
        # preserved duplicate PNG path. Never force an earlier failed TAR hash.
        bundle_metrics[kind] = metrics
        print('Staged actual prospective', kind, 'TAR', json.dumps(metrics), flush=True)
    # This process exits before any512/256/64MiB encoder is allocated.
    stage_data = {'started_at': started.isoformat(), 'source_bindings': source_bindings,
        'removed_containers': removed_containers, 'removed_direct_data': removed_direct_data,
        'removed_direct_main_pdf': removed_direct_main_pdf, 'migration_witnesses': migration_witnesses,
        'predicted_history': predicted_history, 'new_direct': new_direct,
        'current_main_sha': current_main_sha, 'parent_retention_rows': parent_retention_rows,
        'current_authored_paths_snapshotted': len(original_current_paths),
        'bundle_metrics': bundle_metrics}
    json_exclusive(stage/'stage.json', stage_data)
    print('All three exact TARs staged; snapshot process exits before compression', flush=True)


def load_prior_verified_workers():
    """Reuse only verified worker facts; retain the failed outer exit explicitly."""
    assert hash_path(ROOT/PRIOR_OBSERVED) == PRIOR_OBSERVED_SHA256
    assert hash_path(ROOT/PRIOR_CERTIFICATE) == PRIOR_CERTIFICATE_SHA256
    observed = json.loads((ROOT/PRIOR_OBSERVED).read_text())
    certificate = json.loads((ROOT/PRIOR_CERTIFICATE).read_text())
    assert observed['session_id'] == 41501 and observed['actual_exit_code'] == 1
    assert observed['actual_exit_tool_chunk'] == '96b054'
    assert certificate['estimated_total_with_allowance'] > certificate['delivery_cap_bytes']
    assert certificate['baseline_bytes'] == BASELINE_BYTES
    assert certificate['baseline_sha256'] == BASELINE_SHA256
    assert certificate['baseline_identity_verified_before_and_after'] is True
    retained = {row['path']: row for row in observed['files']}
    evidence = {}
    for original in ('records/checkpoint37_size_estimate.json',
                     'records/checkpoint37_size_estimate_run.out',
                     'records/checkpoint37_size_estimate_run.err'):
        row = retained[original]
        p = ROOT/row['retained_path']
        assert p.stat().st_size == row['bytes'] and hash_path(p) == row['sha256']
        evidence[original] = dict(row)
    assert retained['records/checkpoint37_size_estimate.json']['retained_path'] == PRIOR_CERTIFICATE
    stderr = (ROOT/retained['records/checkpoint37_size_estimate_run.err']['retained_path']).read_text()
    assert stderr.rstrip().endswith('AssertionError: Conservative estimate exceeds the delivery cap; report retained')
    # Image/document encoders and deterministic staging code are unchanged.
    # The changed data selector does not participate in either codec.
    for rel in ('code/checkpoint_image37_tar.py', 'code/checkpoint_document37_tar.py',
                'code/checkpoint37_streaming.py', 'code/checkpoint_standard_tar.py'):
        row = certificate['source_bindings'][rel]
        assert (ROOT/rel).stat().st_size == row['bytes'] and hash_path(ROOT/rel) == row['sha256']
    return certificate, {'session_id': 41501, 'actual_outer_exit_code': 1,
                        'actual_exit_tool_chunk': '96b054',
                        'observed_record': PRIOR_OBSERVED,
                        'observed_record_sha256': PRIOR_OBSERVED_SHA256,
                        'certificate': PRIOR_CERTIFICATE,
                        'certificate_sha256': PRIOR_CERTIFICATE_SHA256,
                        'evidence': evidence,
                        'scope': 'The prior outer run failed only its final cap assertion. Its independently successful encode/decode worker certificates are reused only for freshly identical staged image/document bytes and unchanged codec/staging sources.'}


def reuse_verified_bundle(kind, stage_path, metrics, certificate, provenance):
    assert kind in {'images', 'documents'}
    prior = certificate['prospective_bundles'][kind]
    assert prior['metrics'] == metrics, ('Fresh complete TAR metrics differ; no automatic re-encode or certificate reuse', kind)
    expected = {'bytes': metrics['bundle_bytes'], 'sha256': metrics['bundle_sha256'],
                'crc32': metrics['bundle_crc32']}
    assert identity(stage_path) == expected
    dictionary = IMAGE37_DICTIONARY_BYTES if kind == 'images' else DOCUMENT37_DICTIONARY_BYTES
    assert prior['zip_method'] == 'ZIP_LZMA' and prior['dictionary_bytes'] == dictionary
    assert prior['encoder_process_exit_code'] == 0 and prior['decoder_process_exit_code'] == 0
    verified = prior['full_roundtrip']
    assert verified['input'] == expected == verified['roundtrip']
    assert verified['decoder_eof'] is True and verified['unused_bytes'] == 0
    assert verified['encoder_and_decoder_in_separate_processes'] is True
    assert verified['method14_header_hex'] == '090405005d'+dictionary.to_bytes(4, 'little').hex()
    assert verified['encoded_sha256'] == prior['compressed_sha256']
    assert prior['compressed_bytes'] > 9
    result = dict(prior)
    result['measurement_reused_from_verified_worker'] = True
    result['prior_outer_exit_code'] = 1
    result['prior_certificate_path'] = provenance['certificate']
    result['prior_certificate_sha256'] = provenance['certificate_sha256']
    result['fresh_staged_input_identity'] = expected
    result['codec_and_staging_sources_unchanged'] = True
    return result


def main():
    target = ROOT/'records/checkpoint37_size_estimate.json'
    assert not target.exists(), 'Preserve any preceding estimate before rerunning'
    prior_certificate, prior_provenance = load_prior_verified_workers()
    with tempfile.TemporaryDirectory(prefix='.checkpoint37_estimate_stage_', dir=ROOT.parent) as tmp:
        stage = Path(tmp)
        subprocess.run([sys.executable, str(Path(__file__).resolve()), '--stage', str(stage)], check=True)
        state = json.loads((stage/'stage.json').read_text())
        started = datetime.fromisoformat(state['started_at'])
        source_bindings = state['source_bindings']
        removed_containers = state['removed_containers']
        removed_direct_data = state['removed_direct_data']
        removed_direct_main_pdf = state['removed_direct_main_pdf']
        predicted_history = state['predicted_history']
        new_direct = state['new_direct']
        current_main_sha = state['current_main_sha']
        parent_retention_rows = state['parent_retention_rows']
        original_current_path_count = state['current_authored_paths_snapshotted']
        bundle_reports = {}
        for kind in ('images', 'documents', 'data'):
            metrics = state['bundle_metrics'][kind]
            if kind in {'images', 'documents'}:
                bundle_reports[kind] = reuse_verified_bundle(kind, stage/(kind+'.tar'), metrics, prior_certificate, prior_provenance)
                print('Reused prior verified worker after exact fresh stage check', kind, 'compressed_bytes', bundle_reports[kind]['compressed_bytes'], 'prior_outer_exit_code', 1, flush=True)
            else:
                print('Compressing isolated expanded actual prospective data TAR', json.dumps(metrics), flush=True)
                bundle_reports[kind] = measure_staged_tar(stage/(kind+'.tar'), kind, metrics, stage)
                bundle_reports[kind]['measurement_reused_from_verified_worker'] = False
                print('Completed and independently verified expanded data', 'compressed_bytes', bundle_reports[kind]['compressed_bytes'], flush=True)
        for kind in ('images', 'documents'):
            assert identity(stage/(kind+'.tar')) == bundle_reports[kind]['fresh_staged_input_identity']
        assert hash_path(ROOT/PRIOR_OBSERVED) == PRIOR_OBSERVED_SHA256
        assert hash_path(ROOT/PRIOR_CERTIFICATE) == PRIOR_CERTIFICATE_SHA256
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
            'previous_direct_data_migration_witnesses': state['migration_witnesses'],
            'prior_failed_cap_run_and_reused_workers': prior_provenance,
            'previous_direct_main_pdf_migrated': removed_direct_main_pdf,
            'previous_direct_main_pdf_compressed_payload_removed': main_removed,
            'previous_direct_main_pdf_headers_removed': 0,
            'prospective_bundles': bundle_reports,
            'current_authored_paths_snapshotted': original_current_path_count,
            'predicted_checkpoint36_historical_paths': len(predicted_history),
            'predicted_checkpoint36_historical_bytes': sum(x['bytes'] for x in predicted_history),
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
            'scope': 'Actual checkpoint36 baseline with unchanged five-million-byte allowance. The37-only selector moves research/record bytes into the same standard64MiB data TAR while root deliverables, code, formal sections and current contents/packaging manifests remain direct. Every removed baseline direct payload has an explicit complete size/hash witness in the new data snapshot; its ZIP headers remain counted. A child snapshots every current and predicted historical logical byte into exact deterministic disk TARs and exits. Fresh image and document TARs must match every metric and full length/SHA256/CRC32 of the preserved41501 worker certificates, and their codec/staging sources must be unchanged; successful prior encode/decode workers are reused while the prior outer cap failure remains explicitly exit1. No image/document encoding is rerun. Expanded data is encoded once with64MiB in a fresh child, then fully decoded in another child with SHA256/CRC32/length, EOF and no-tail validation. No encoder and decoder coexist. No ZIP is created. All old containers and migrated direct payloads are subtracted once; the old main PDF payload is separately removed once only when its exact bytes appear in the document TAR. All existing headers remain counted, and every changed/new remaining direct payload is added conservatively. Final immutable archive size remains authoritative.'
        }
        json_exclusive(target, report)
        print(json.dumps({k:v for k,v in report.items() if k not in {'predicted_history', 'previous_direct_data_migration_witnesses'}}, indent=2), flush=True)
        assert estimate+ALLOWANCE < CAP, 'Conservative estimate exceeds the delivery cap; report retained'
    

if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == '--stage':
        stage_snapshot(Path(sys.argv[2]).resolve())
    else:
        assert len(sys.argv) == 1
        main()
