"""Record checkpoint28 only after immutable verification and saved identity."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import re

root = Path(__file__).resolve().parents[1]
read = lambda name: json.loads((root / 'records' / name).read_text())
v = read('checkpoint28_archive_verification.json')
t = read('checkpoint28_system_tars_verification.json')
results = read('checkpoint28_upload_result.json')['results']
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
walk(read('checkpoint28_library_metadata.json'))
assert len(found) == 1
item = found[0]
assert r['file_name'] == v['archive'] == 'LM4_SUCCESSOR_checkpoint_28.zip'
assert item['size_bytes'] == v['bytes'] <= 536870912
assert item['file_id'] == r['file_id'] and item['version_id'] == '0'
assert v['prior_entries_retained'] == 97426
assert v['crc'] == v['every_manifest_entry'] == v['every_retained_version'] == 'PASS'
assert t['both_system_tar_restores'] == t['current_main_pdf_direct'] == 'PASS'
assert t['both_container_zip_lzma_methods'] == 'PASS'
assert t['archive_sha256'] == v['sha256']
for kind in ('images', 'documents'):
    assert t['containers'][kind]['system_tar_restore'] == 'PASS'
    assert t['containers'][kind]['every_original_path_size_and_hash'] == 'PASS'
retention = read('checkpoint_version_retention_summary.json')
assert retention['archives'] == 27 and retention['archive_entries'] == 97426
assert retention['omissions'] == 0
m = read('checkpoint28_metrics.json')
assert m['statements'] == 308 and m['pages'] == 530 and m['bibliography_entries'] == 113
assert m['statuses'] == {'Known': 6, 'Proved': 264, 'Refuted': 19, 'Open': 19}
release = read('checkpoint28_writer_release.json')
p = read('checkpoint_28_packaging.json')
assert p['image_paths'] == t['containers']['images']['paths']
assert p['standard_tar_hardlinks'] == t['containers']['images']['hardlink_paths']
assert p['document_paths'] == t['containers']['documents']['paths']
assert p['standard_tar_document_hardlinks'] == t['containers']['documents']['hardlink_paths']
assert p['image_zip_method'] == p['document_zip_method'] == 'ZIP_LZMA'
inventory_count = len(list(csv.DictReader((root / 'records/computation_inventory.csv').open())))
review = (root / 'records/progress_review_28h.md').read_text()
review_time = re.search(r'^Actual review record: (.+)\.$', review, re.M).group(1)
driver = (root / 'records/checkpoint28_capture_driver.log').read_text()
capture_time = re.search(r'^Immutable capture completed:\s*(.+)$', driver, re.M).group(1)
qa = read('checkpoint28_visual_review.json')
late = read('checkpoint28_root_late_reviews.json')
record = f'''## Checkpoint28: saved and verified

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
All97426 logical entries of the27 previous immutable archives are retained
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
All27 earlier archives remain unchanged. Exactly one new ZIP was created.

The formal PDF has530 pages and308 statements:264 Proved,19 Refuted,
19 Open and6 Known; all113 references are printed and49 task rows retained.
PDF bytes:{m['pdf_bytes']}; SHA-256:{m['pdf_sha256']}.
The first combined build is final: no overfull boxes, actual warnings,
undefined references or errors. Its18 pre-existing underfull notices are
unchanged. Both final engine stdout and full log were scanned
case-insensitively. All21 new mathematical pages130--136 and427--440
were individually inspected, within{len(qa['individually_inspected_pages'])}
individual views. Four separately inspected contact-sheet images cover
{len(qa['rendered_pages'])} rendered pages.

The five frozen formal sources A85/A86/B135/B136/B137 have complete root
and independent source reviews. They establish the actual V4 defect
structure, canonical cusp-word/unit criterion, whole-inner compact
centralizer and exact face kernels, symmetric local edge filling and
whole ordinary edge-group intersection. The separate late research
record binds{len(late['proof_sources'])} complete proofs with their exact
current scopes and preserved corrections; it does not promote further
formal statements. In particular, no local or quotient equality is
substituted for the final ambient filling/source comparison or either
main decision. The exact Main-A full-word gate and actual Main-B K=1
decision remain Open.

This postcapture verification, save receipt, metadata and delivery record
enter checkpoint29. All three agents resumed substantive research
immediately after capture, before verification or saving.
Next review/checkpoint:2026-11-17 05:49:30 UTC.
'''
for relative in ('records/checkpoints.md', 'records/continuation_state.md'):
    path = root / relative
    old = path.read_text()
    assert '## Checkpoint28: saved and verified' not in old
    path.write_text(old + '\n' + record)
print('Checkpoint28 archive, both native TAR restorations, receipt and metadata agree.')
print('Delivery record written', datetime.now(timezone.utc).isoformat())
