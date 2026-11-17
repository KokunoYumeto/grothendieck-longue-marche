"""Record checkpoint21 only after immutable verification and a confirmed save."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import re

root = Path(__file__).resolve().parents[1]
read = lambda name: json.loads((root/'records'/name).read_text())
v = read('checkpoint21_archive_verification.json')
t = read('checkpoint21_system_tar_verification.json')
r = read('checkpoint21_upload_result.json')['results']
assert len(r) == 1
r = r[0]
assert r['status'] == 'succeeded' and r['local_metadata_applied']
metadata = read('checkpoint21_library_metadata.json')
found = []
def walk(value):
    if isinstance(value, dict):
        if value.get('library_file_id') == r['library_file_id'] and value.get('name') == r['file_name']:
            found.append(value)
        for item in value.values():
            walk(item)
    elif isinstance(value, list):
        for item in value:
            walk(item)
walk(metadata)
assert len(found) == 1
item = found[0]
assert r['file_name'] == v['archive'] == 'LM4_SUCCESSOR_checkpoint_21.zip'
assert item['size_bytes'] == v['bytes'] == 470341798
assert item['file_id'] == r['file_id'] and item['version_id'] == '0'
assert v['prior_entries_retained'] == 50301
assert v['crc'] == v['every_manifest_entry'] == v['every_retained_version'] == 'PASS'
assert t['system_tar_restore'] == t['every_original_png_path_and_byte'] == 'PASS'
assert t['archive_sha256'] == v['sha256']
retention = read('checkpoint_version_retention_summary.json')
assert retention['archives'] == 20 and retention['omissions'] == 0
m = read('checkpoint21_metrics.json')
assert m['statements'] == 276 and m['pages'] == 408 and m['bibliography_entries'] == 108
assert m['statuses'] == {'Known':6,'Proved':232,'Refuted':19,'Open':19}
release = read('checkpoint21_writer_release.json')
p = read('checkpoint_21_packaging.json')
assert p['image_paths'] == t['image_paths'] == 1710
assert p['standard_tar_hardlinks'] == t['hardlink_image_paths'] == 509
inventory_count = len(list(csv.DictReader((root/'records/computation_inventory.csv').open())))
review = (root/'records/progress_review_21h.md').read_text()
review_time = re.search(r'^Actual review record: (.+)\.$', review, re.M).group(1)
driver = (root/'records/checkpoint21_capture_driver.log').read_text()
capture_time = re.search(r'^Immutable capture completed:\s*(.+)$', driver, re.M).group(1)
record = f'''## Checkpoint21: saved and verified

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
All 50301 entries of the twenty earlier archives are retained byte-exactly,
with zero omissions. History contains {retention['total_historical_copies']}
distinct copies totaling {retention['total_historical_bytes']} bytes.
The computation inventory contains {inventory_count} programs at capture.
The standard nested verification-images TAR retains all 1710 original PNG
paths, with 509 standard hardlinks for identical contents. Independent native
tar extraction verified each original path, size and byte hash without
importing the packager or logical reader. Restore from the extraction parent:
tar -xf LM4_SUCCESSOR/verification_images.tar
All twenty earlier archives remain unchanged.

The formal PDF has 408 pages, 276 statements (232 Proved, 19 Refuted,
19 Open, 6 Known), 108 bibliography records and 49 task/lead rows.
PDF bytes: {m['pdf_bytes']}; SHA-256: {m['pdf_sha256']}.
Final QA: zero overfull boxes, warnings, undefined references and errors.
Both build overflow counts are 0/0. Four contact sheets cover 35 rendered
pages; eight critical pages were inspected individually. The final citation
spacing repair, earlier PDF and all earlier renderings are retained.

B106--B107 are integrated. The actual shared first-neck group, natural
middle-neck noninjection on both sides, calibrated two-node HNN block,
and Main A section-test limitation are retained with complete scope reviews.
The late profinite one-neck proposal was retained as awaiting review.
Both main full decisions remain Open. Capture's first launch occurred
five seconds before the allowed one-minute window and exited at its guard
before any snapshot action; its genuine error is retained as
checkpoint21_capture_early_attempt01.log. The second launch waited to the
scheduled time and completed successfully. No extra archive was made.

This postcapture verification, save receipt, metadata and delivery record
enter checkpoint22. Substantive work resumed immediately after capture.
Next review/checkpoint: 2026-11-16 22:49:30 UTC.
'''
for relative in ('records/checkpoints.md','records/continuation_state.md'):
    path = root/relative
    old = path.read_text()
    assert '## Checkpoint21: saved and verified' not in old
    path.write_text(old+'\n'+record)
print('Checkpoint21 archive, native TAR verification, receipt and metadata agree.')
print('Delivery record written', datetime.now(timezone.utc).isoformat())
