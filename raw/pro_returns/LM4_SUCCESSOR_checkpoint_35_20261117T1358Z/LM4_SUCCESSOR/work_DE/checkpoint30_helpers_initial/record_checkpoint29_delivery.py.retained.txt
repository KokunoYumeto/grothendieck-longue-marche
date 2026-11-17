"""Record checkpoint29 after immutable verification and saved identity."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import re

root = Path(__file__).resolve().parents[1]
read = lambda name: json.loads((root / 'records' / name).read_text())
v = read('checkpoint29_archive_verification.json')
t = read('checkpoint29_system_tars_verification.json')
results = read('checkpoint29_upload_result.json')['results']
assert len(results) == 1
r = results[0]
assert r['status'] == 'succeeded' and r['local_metadata_applied']
found = []
def walk(value):
    if isinstance(value, dict):
        if value.get('library_file_id') == r['library_file_id'] and value.get('name') == r['file_name']:
            found.append(value)
        for item in value.values(): walk(item)
    elif isinstance(value, list):
        for item in value: walk(item)
walk(read('checkpoint29_library_metadata.json'))
assert len(found) == 1
item = found[0]
assert r['file_name'] == v['archive'] == 'LM4_SUCCESSOR_checkpoint_29.zip'
assert item['size_bytes'] == v['bytes'] <= 536870912
assert item['file_id'] == r['file_id'] and item['version_id'] == '0'
assert v['prior_entries_retained'] == 105724
assert v['crc'] == v['every_manifest_entry'] == v['every_retained_version'] == 'PASS'
assert t['both_system_tar_restores'] == t['current_main_pdf_direct'] == 'PASS'
assert t['both_container_zip_lzma_methods'] == 'PASS'
assert t['archive_sha256'] == v['sha256']
for kind in ('images', 'documents'):
    assert t['containers'][kind]['system_tar_restore'] == 'PASS'
    assert t['containers'][kind]['every_original_path_size_and_hash'] == 'PASS'
retention = read('checkpoint_version_retention_summary.json')
assert retention['archives'] == 28 and retention['archive_entries'] == 105724
assert retention['omissions'] == 0
m = read('checkpoint29_metrics.json')
assert m['statements'] == 314 and m['pages'] == 551 and m['bibliography_entries'] == 114
assert m['statuses'] == {'Known': 6, 'Proved': 270, 'Refuted': 19, 'Open': 19}
release = read('checkpoint29_writer_release.json')
p = read('checkpoint_29_packaging.json')
assert p['image_paths'] == t['containers']['images']['paths']
assert p['standard_tar_hardlinks'] == t['containers']['images']['hardlink_paths']
assert p['document_paths'] == t['containers']['documents']['paths']
assert p['standard_tar_document_hardlinks'] == t['containers']['documents']['hardlink_paths']
assert p['image_zip_method'] == p['document_zip_method'] == 'ZIP_LZMA'
inventory_count = len(list(csv.DictReader((root / 'records/computation_inventory.csv').open())))
review = (root / 'records/progress_review_29h.md').read_text()
review_time = re.search(r'^Actual review record: (.+)\.$', review, re.M).group(1)
driver = (root / 'records/checkpoint29_capture_driver.log').read_text()
capture_time = re.search(r'^Immutable capture completed:\s*(.+)$', driver, re.M).group(1)
qa = read('checkpoint29_visual_review.json')
late = read('checkpoint29_root_late_reviews.json')
record = f'''## Checkpoint29: saved and verified

Review:{review_time}, CONTINUE.
Immutable capture completed:{capture_time}.
Writer release recorded:{release['released_at']}.
Creation:{item['created_at']}.
Archive:{r['file_name']}.
Bytes:{v['bytes']}; logical entries:{v['entries']};
physical ZIP entries:{v['physical_zip_entries']}; manifest rows:{v['manifest_rows']}.
SHA-256:{v['sha256']}.
Library ID:{r['library_file_id']}.
File ID:{r['file_id']}. Version:0.
Independent metadata matches name, size, identity and version; local identity applied.

CRC, every logical manifest entry and every retained version:PASS.
All105724 logical entries of the28 previous immutable archives are retained
byte-exactly with zero omissions. History contains
{retention['total_historical_copies']} distinct copies totaling
{retention['total_historical_bytes']} bytes. The computation inventory has
{inventory_count} programs at capture. The standard image TAR retains
{p['image_paths']} original PNG paths with{p['standard_tar_hardlinks']} hardlinks;
the standard document TAR retains{p['document_paths']} historical/preview
PDF paths with{p['standard_tar_document_hardlinks']} hardlinks. Both use
lossless ZIP_LZMA. The current main PDF is a direct ZIP entry.
Independent native tar extraction of the actual archived containers
verified every original path, size and byte hash without importing the
packager or its logical reader. Restore from the ZIP extraction parent:
tar -xf LM4_SUCCESSOR/verification_images.tar
tar -xf LM4_SUCCESSOR/historical_documents.tar
All28 earlier archives remain unchanged. Exactly one new ZIP was created.

The formal PDF has551 pages and314 statements:270 Proved,19 Refuted,
19 Open and6 Known; all114 references are printed and49 task rows retained.
PDF bytes:{m['pdf_bytes']}; SHA-256:{m['pdf_sha256']}.
The first combined build is final: no overfull boxes, actual warnings,
undefined references or errors. Its18 pre-existing underfull notices
are unchanged. Both final engine stdout and full log were scanned
case-insensitively. All24 new mathematical pages136--142 and446--462
were individually inspected, within{len(qa['individually_inspected_pages'])}
individual views. Five separately inspected contact-sheet images cover
{len(qa['rendered_pages'])} rendered pages.

The six frozen formal sources A87/A88/B138/B139/B140/B141 have complete
root and independent source reviews. They establish the actual marked
cusp-frame and full coefficient criterion, modulo8 comparison, whole
compact unfilled-edge intersection, exact one-family fixed-source
comparison, named-section repair obstruction, and faithful regional
kernel/mixed filling presentation. The separate late record binds
{len(late['proof_sources'])} complete proofs with exact current scopes,
including the full-GT dyadic/odd-head reduction and unrestricted coarse
nonsplitting, without promoting additional formal statements. Their
further reviewed consequences are recorded there explicitly. No local,
quotient, or nonsplitting result is substituted for the final ambient
fixed-source equality or either main decision. Main A and the actual
Main-B icosahedral K=1 decision remain Open.

This postcapture verification, save receipt, metadata and delivery record
enter checkpoint30. All three agents resumed substantive research
immediately after capture, before verification or saving.
Next review/checkpoint:2026-11-17 06:49:30 UTC.
'''
for relative in ('records/checkpoints.md', 'records/continuation_state.md'):
    path = root / relative
    old = path.read_text()
    assert '## Checkpoint29: saved and verified' not in old
    path.write_text(old + '\n' + record)
print('Checkpoint29 archive, both native TAR restorations, receipt and metadata agree.')
print('Delivery record written', datetime.now(timezone.utc).isoformat())
