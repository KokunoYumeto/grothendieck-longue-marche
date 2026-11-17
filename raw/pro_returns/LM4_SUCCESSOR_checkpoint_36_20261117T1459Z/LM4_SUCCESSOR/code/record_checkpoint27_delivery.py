"""Record checkpoint27 only after immutable verification and saved identity."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,re

root=Path(__file__).resolve().parents[1]
read=lambda name:json.loads((root/'records'/name).read_text())
v=read('checkpoint27_archive_verification.json')
t=read('checkpoint27_system_tars_verification.json')
results=read('checkpoint27_upload_result.json')['results']
assert len(results)==1
r=results[0]
assert r['status']=='succeeded' and r['local_metadata_applied']
found=[]
def walk(value):
    if isinstance(value,dict):
        if value.get('library_file_id')==r['library_file_id'] and value.get('name')==r['file_name']:found.append(value)
        for item in value.values():walk(item)
    elif isinstance(value,list):
        for item in value:walk(item)
walk(read('checkpoint27_library_metadata.json'))
assert len(found)==1
item=found[0]
assert r['file_name']==v['archive']=='LM4_SUCCESSOR_checkpoint_27.zip'
assert item['size_bytes']==v['bytes']<=536870912
assert item['file_id']==r['file_id'] and item['version_id']=='0'
assert v['prior_entries_retained']==89536
assert v['crc']==v['every_manifest_entry']==v['every_retained_version']=='PASS'
assert t['both_system_tar_restores']==t['current_main_pdf_direct']=='PASS'
assert t['both_container_zip_lzma_methods']=='PASS'
assert t['archive_sha256']==v['sha256']
for name in ('images','documents'):
    assert t['containers'][name]['system_tar_restore']=='PASS'
    assert t['containers'][name]['every_original_path_size_and_hash']=='PASS'
retention=read('checkpoint_version_retention_summary.json')
assert retention['archives']==26 and retention['archive_entries']==89536 and retention['omissions']==0
m=read('checkpoint27_metrics.json')
assert m['statements']==303 and m['pages']==509 and m['bibliography_entries']==113
assert m['statuses']=={'Known':6,'Proved':259,'Refuted':19,'Open':19}
release=read('checkpoint27_writer_release.json')
p=read('checkpoint_27_packaging.json')
assert p['image_paths']==t['containers']['images']['paths']
assert p['standard_tar_hardlinks']==t['containers']['images']['hardlink_paths']
assert p['document_paths']==t['containers']['documents']['paths']
assert p['standard_tar_document_hardlinks']==t['containers']['documents']['hardlink_paths']
assert p['image_zip_method']==p['document_zip_method']=='ZIP_LZMA'
inventory_count=len(list(csv.DictReader((root/'records/computation_inventory.csv').open())))
review=(root/'records/progress_review_27h.md').read_text()
review_time=re.search(r'^Actual review record: (.+)\.$',review,re.M).group(1)
driver=(root/'records/checkpoint27_capture_driver.log').read_text()
capture_time=re.search(r'^Immutable capture completed:\s*(.+)$',driver,re.M).group(1)
qa=read('checkpoint27_visual_review.json')
record=f'''## Checkpoint27: saved and verified

Review: {review_time}, CONTINUE.
Immutable capture completed: {capture_time}.
Writer release recorded: {release['released_at']}.
Creation: {item['created_at']}.
Archive: {r['file_name']}.
Bytes: {v['bytes']}; logical entries: {v['entries']};
physical ZIP entries: {v['physical_zip_entries']}; manifest rows: {v['manifest_rows']}.
SHA-256: {v['sha256']}.
Library ID: {r['library_file_id']}.
File ID: {r['file_id']}. Version: 0.
Independent metadata matches name, size, identity and version; local identity applied.

CRC, every logical manifest entry and every retained version: PASS.
All 89536 logical entries of the twenty-six earlier archives are retained
byte-exactly, with zero omissions. History contains
{retention['total_historical_copies']} distinct copies totaling
{retention['total_historical_bytes']} bytes. The computation inventory
contains {inventory_count} programs at capture. Standard nested TAR encoding
retains all {p['image_paths']} original PNG paths, with
{p['standard_tar_hardlinks']} standard hardlinks, and all
{p['document_paths']} historical/preview PDF paths, with
{p['standard_tar_document_hardlinks']} standard hardlinks. Both containers
use lossless ZIP_LZMA. The current main PDF is directly in the ZIP.
Independent native tar extraction of both actual containers verified
every original path, size and byte hash without importing the packager
or logical reader. Restore from the ZIP extraction parent with:
tar -xf LM4_SUCCESSOR/verification_images.tar
tar -xf LM4_SUCCESSOR/historical_documents.tar
All twenty-six earlier archives remain unchanged.

The final formal PDF has 509 pages, 303 statements (259 Proved,
19 Refuted, 19 Open, 6 Known), 113 printed bibliography entries and 49
task/lead rows. PDF bytes: {m['pdf_bytes']}; SHA-256: {m['pdf_sha256']}.
Final QA: no overfull boxes, actual warnings, undefined references or errors.
The final log and actual stabilized stdout were checked case-insensitively;
their 18 pre-existing underfull notices are unchanged. Initial/final
combined overfull counts: 0/0. The first combined build is final.
Four separately opened contact sheets cover {len(qa['rendered_pages'])} pages;
{len(qa['individually_inspected_pages'])} final pages were inspected individually,
including every new mathematical page 404--419 of B131--B134.
No earlier private or truncated inspection substitutes for these views.

B131--B134 have complete root and independent source reviews: actual
d-contact noncommutation and strict one-sided quotient; actual free
source pair with full topology; the entire pre-cross marked free-six
source with full topology; and the actual TWO-sheet edge presentation
with an exact ordinary matching union and separate finite-normal compact
criterion. The omitted-mirror research error was repaired before formal
integration and all original records remain preserved. No closure or
intersection exchange, finite-stage stabilization or final source
injection is inferred. The actual Main-A V4 research gives a stronger
constant-ring induced defect module, without proving the Fox unit.
Later research notes retain their individually reviewed scope and are
not silently promoted to extra formal propositions. Both main decisions,
the actual fixed-source equality and global transfer remain Open.

This postcapture verification, save receipt, metadata and delivery record
enter checkpoint28. Substantive work resumed immediately after capture.
Next review/checkpoint: 2026-11-17 04:49:30 UTC.
'''
for relative in ('records/checkpoints.md','records/continuation_state.md'):
    path=root/relative;old=path.read_text()
    assert '## Checkpoint27: saved and verified' not in old
    path.write_text(old+'\n'+record)
print('Checkpoint27 archive, both native TAR restorations, receipt and metadata agree.')
print('Delivery record written',datetime.now(timezone.utc).isoformat())
