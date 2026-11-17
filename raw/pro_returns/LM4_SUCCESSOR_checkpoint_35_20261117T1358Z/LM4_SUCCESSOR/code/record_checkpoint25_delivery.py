"""Record checkpoint25 only after immutable verification and saved metadata."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import re

root = Path(__file__).resolve().parents[1]
read = lambda name: json.loads((root/'records'/name).read_text())
v = read('checkpoint25_archive_verification.json')
t = read('checkpoint25_system_tars_verification.json')
results = read('checkpoint25_upload_result.json')['results']
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
walk(read('checkpoint25_library_metadata.json'))
assert len(found) == 1
item = found[0]
assert r['file_name'] == v['archive'] == 'LM4_SUCCESSOR_checkpoint_25.zip'
assert item['size_bytes'] == v['bytes'] <= 536870912
assert item['file_id'] == r['file_id'] and item['version_id'] == '0'
assert v['prior_entries_retained'] == 74969
assert v['crc'] == v['every_manifest_entry'] == v['every_retained_version'] == 'PASS'
assert t['both_system_tar_restores'] == t['current_main_pdf_direct'] == 'PASS'
assert t['archive_sha256'] == v['sha256']
for name in ('images', 'documents'):
    assert t['containers'][name]['system_tar_restore'] == 'PASS'
    assert t['containers'][name]['every_original_path_size_and_hash'] == 'PASS'
retention = read('checkpoint_version_retention_summary.json')
assert retention['archives'] == 24 and retention['archive_entries'] == 74969 and retention['omissions'] == 0
m = read('checkpoint25_metrics.json')
assert m['statements'] == 292 and m['pages'] == 474 and m['bibliography_entries'] == 112
assert m['statuses'] == {'Known': 6, 'Proved': 248, 'Refuted': 19, 'Open': 19}
release = read('checkpoint25_writer_release.json')
p = read('checkpoint_25_packaging.json')
assert p['image_paths'] == t['containers']['images']['paths']
assert p['standard_tar_hardlinks'] == t['containers']['images']['hardlink_paths']
assert p['document_paths'] == t['containers']['documents']['paths']
assert p['standard_tar_document_hardlinks'] == t['containers']['documents']['hardlink_paths']
inventory_count = len(list(csv.DictReader((root/'records/computation_inventory.csv').open())))
review = (root/'records/progress_review_25h.md').read_text()
review_time = re.search(r'^Actual review record: (.+)\.$', review, re.M).group(1)
driver = (root/'records/checkpoint25_capture_driver.log').read_text()
capture_time = re.search(r'^Immutable capture completed:\s*(.+)$', driver, re.M).group(1)
qa = read('checkpoint25_visual_review.json')
record = f'''## Checkpoint25: saved and verified

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
All 74969 logical entries of the twenty-four earlier archives are retained
byte-exactly, with zero omissions. History contains
{retention['total_historical_copies']} distinct copies totaling
{retention['total_historical_bytes']} bytes. The computation inventory
contains {inventory_count} programs at capture. Standard nested TAR encoding
retains all {p['image_paths']} original PNG paths, with
{p['standard_tar_hardlinks']} standard hardlinks, and all
{p['document_paths']} historical/preview PDF paths, with
{p['standard_tar_document_hardlinks']} standard hardlinks. The current main
PDF remains directly in the ZIP. Independent native tar extraction of
both actual containers verified every original path, size and byte hash,
without importing the packager or logical reader. Restore from the ZIP
extraction parent with:
tar -xf LM4_SUCCESSOR/verification_images.tar
tar -xf LM4_SUCCESSOR/historical_documents.tar
All twenty-four earlier archives remain unchanged.

The final formal PDF has 474 pages, 292 statements (248 Proved,
19 Refuted, 19 Open, 6 Known), 112 printed bibliography entries and 49
task/lead rows. PDF bytes: {m['pdf_bytes']}; SHA-256: {m['pdf_sha256']}.
Final QA: zero overfull boxes, warnings, undefined references or errors;
both final log and stabilized stdout were checked case-insensitively.
The previously missed lowercase font-map warnings are explicitly
corrected in the checkpoint25 audit; original prior logs remain intact.
Initial/final combined overfull counts: 0/0. The first combined build is
final. Six separately opened contact sheets cover {len(qa['rendered_pages'])}
sampled pages; {len(qa['individually_inspected_pages'])} final pages were
inspected individually, including every mathematical page 361--385 of
B118--B123. No earlier inspection substitutes for these final views.

B118--B123 are integrated with complete root and independent reviews:
the actual full boundary/neck intersection; exact ordinary filled fixed
group; proper intermediate completed amalgam and full carrier; final
ordinary-neck retraction; intermediate completed centralizer closure;
and exact whole two-operator family-kernel reduction. All source
markings, forty node seeds and signed operator translates remain.
The later actual outer-five source retraction, proper ordinary star
with one cross relation, and family-kernel Schreier/abelianization
notes are research records at their explicitly reviewed scope.
No actual unfilled fixed-source equality or full six-source embedding
is inferred. Both main full decisions remain Open.

This postcapture verification, save receipt, metadata and delivery record
enter checkpoint26. Substantive work resumed immediately after capture.
Next review/checkpoint: 2026-11-17 02:49:30 UTC.
'''
for relative in ('records/checkpoints.md', 'records/continuation_state.md'):
    path = root/relative
    old = path.read_text()
    assert '## Checkpoint25: saved and verified' not in old
    path.write_text(old+'\n'+record)
print('Checkpoint25 archive, both native TAR restorations, receipt and metadata agree.')
print('Delivery record written', datetime.now(timezone.utc).isoformat())
