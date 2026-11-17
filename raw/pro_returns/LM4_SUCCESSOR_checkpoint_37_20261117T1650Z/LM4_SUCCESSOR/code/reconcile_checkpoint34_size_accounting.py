"""Remove one proved duplicate payload cost from completed real measurements.

No compressor or archive is started. Every failed-estimate byte is preserved.
The five-million-byte allowance and all baseline ZIP headers remain counted.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, zipfile

root = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
source = root / 'code/estimate_checkpoint34_size.py'
assert sha(source) == '3bcd93f8c56abd7f32f80a5532a2002bad7acf3e0a408b0c1e8047ba1f070320'
target = root / 'records/checkpoint34_size_estimate.json'
report = json.loads(target.read_text())
output = (root / 'records/checkpoint34_size_estimate_run.out').read_text()
error = (root / 'records/checkpoint34_size_estimate_run.err').read_text()
assert 'AssertionError: Conservative estimate exceeds the delivery cap; report retained' in error
assert report['estimated_before_allowance'] == 532725722
assert report['header_manifest_retention_late_text_allowance_bytes'] == 5000000
assert report['estimated_total_with_allowance'] == 537725722
assert report['estimated_total_with_allowance'] >= report['delivery_cap_bytes'] == 536870912
assert not report['creates_zip'] and not report['writes_authored_input_files']
for kind in ('images', 'documents', 'data'):
    measured = report['prospective_bundles'][kind]['compressed_bytes']
    assert f'Completed {kind} compressed_bytes {measured}' in output
metrics = json.loads((root / 'records/checkpoint34_metrics.json').read_text())
assert report['current_main_pdf_sha256'] == metrics['pdf_sha256'] == sha(root / 'LM4_SUCCESSOR_paper.pdf')
archive = root.parent / 'LM4_SUCCESSOR_checkpoint_33.zip'
assert archive.stat().st_size == report['baseline_bytes'] == 508499680
assert sha(archive) == report['baseline_sha256'] == '5c68edb5a023c97cb400b506f7e1b7303f19e3cac9212947491e47793d77ef96'
with zipfile.ZipFile(archive) as z:
    info = z.getinfo('LM4_SUCCESSOR/LM4_SUCCESSOR_paper.pdf')
    old_pdf = z.read(info)
    old_sha = hashlib.sha256(old_pdf).hexdigest()
    assert info.compress_type == zipfile.ZIP_DEFLATED
    assert info.file_size == len(old_pdf) == 4219277
    assert info.compress_size == 4177417
    assert old_sha == '80e44d3c3e9766d79c3e740dc83577f7a60a80947a254e6803c74725e0534c70'
    duplicate = info.compress_size
history = [row for row in report['predicted_history']
           if row['path'] == 'checkpoint_history/checkpoint_33/LM4_SUCCESSOR_paper.pdf']
assert len(history) == 1 and history[0]['sha256'] == old_sha and history[0]['bytes'] == len(old_pdf)
assert any(row[1] == 'LM4_SUCCESSOR_paper.pdf' for row in report['largest_new_direct_payloads'])
assert report['current_main_pdf_sha256'] != old_sha
# The unchanged estimator source routes every non-main PDF into its documents
# TAR, including this predicted history entry, and compresses the new main PDF
# separately. The old direct main-PDF payload is not one of the three removed
# containers and is not a data-bundle member. It is thus still in the baseline
# and counted twice. Deduct only its exact payload size, never its ZIP headers.
backup = root / 'records/checkpoint34_size_before_reconciliation'
assert not backup.exists()
backup.mkdir()
preserved = []
for rel in ['records/checkpoint34_size_estimate.json',
            'records/checkpoint34_size_estimate_run.out',
            'records/checkpoint34_size_estimate_run.err',
            'code/estimate_checkpoint34_size.py']:
    path = root / rel
    saved = backup / path.name
    shutil.copyfile(path, saved)
    assert saved.read_bytes() == path.read_bytes()
    preserved.append(dict(path=rel, preserved=str(saved.relative_to(root)),
                          bytes=path.stat().st_size, sha256=sha(path)))
correction = dict(recorded_at=datetime.now(timezone.utc).isoformat(),
    measurement_session_id=55851, measurement_actual_exit_code=1,
    measurement_exit_observation_chunk='15fae9', all_three_compression_streams_completed=True,
    failure_scope='Only the final conservative cap assertion failed after all measured streams and the report completed.',
    preserved=preserved, duplicate_previous_main_pdf_payload_bytes=duplicate,
    previous_main_pdf_sha256=old_sha, previous_main_pdf_bytes=len(old_pdf),
    predicted_historical_copy=history[0], allowance_unchanged=5000000,
    baseline_headers_deducted=0, omitted_logical_files=0, new_compression_run=False, new_zip_created=False,
    arithmetic='537725722 - 4177417 = 533548305; cap536870912 leaves3322607 bytes, still including the full5000000-byte allowance.',
    proof='The completed original estimator retains the entire parent baseline after removing only its three containers and migrated direct data payloads. The prior main PDF is neither. Its exact bytes are separately present in the measured documents TAR at the recorded predicted-history path, while the changed final main PDF is included among added direct payloads. Therefore the old direct compressed PDF payload is a duplicate. Subtracting exactly that payload leaves all baseline headers and the full allowance counted. No authored/history byte is dropped.')
correction_path = root / 'records/checkpoint34_size_accounting_correction.json'
assert not correction_path.exists()
correction_path.write_text(json.dumps(correction,indent=2)+'\n')
report['original_scope_before_reconciliation'] = report['scope']
report['scope'] += ' Exact subsequent reconciliation subtracts ONLY the proved duplicate parent main-PDF compressed payload, retaining its measured historical bytes, all headers and the full five-million-byte allowance. The measurement producer honestly exited1; the separate accounting producer has its own observed completion.'
for key in ['estimated_before_allowance', 'estimated_total_with_allowance']:
    report[key] -= duplicate
report['estimated_headroom_bytes'] = report['delivery_cap_bytes']-report['estimated_total_with_allowance']
report['accounting_correction'] = dict(path=str(correction_path.relative_to(root)), sha256=sha(correction_path),
                                     previous_main_pdf_payload_deducted=duplicate)
assert report['estimated_total_with_allowance'] == 533548305 < report['delivery_cap_bytes']
target.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(result='PASS_EXACT_DUPLICATE_ACCOUNTING',
    measured_streams_completed=True, measurement_exit_code=1, deducted_payload_bytes=duplicate,
    unchanged_allowance_bytes=5000000, estimated_total_with_allowance=533548305,
    headroom_bytes=3322607, files_omitted=0, new_zip_created=False),indent=2))
