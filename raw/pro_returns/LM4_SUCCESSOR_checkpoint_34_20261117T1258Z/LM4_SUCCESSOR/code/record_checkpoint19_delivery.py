"""Record checkpoint19 after independent immutable verification and save."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import re

root = Path(__file__).resolve().parents[1]
verification = json.loads((root/'records/checkpoint19_archive_verification.json').read_text())
receipts = json.loads((root/'records/checkpoint19_upload_result.json').read_text())['results']
assert len(receipts) == 1
receipt = receipts[0]
metadata = json.loads((root/'records/checkpoint19_library_metadata.json').read_text())
found = []
def walk(value):
    if isinstance(value, dict):
        if value.get('library_file_id') == receipt['library_file_id'] and value.get('name') == receipt['file_name']:
            found.append(value)
        for item in value.values(): walk(item)
    elif isinstance(value, list):
        for item in value: walk(item)
walk(metadata)
assert len(found) == 1
item = found[0]
assert receipt['status'] == 'succeeded' and receipt['local_metadata_applied']
assert receipt['file_name'] == verification['archive'] == 'LM4_SUCCESSOR_checkpoint_19.zip'
assert item['size_bytes'] == verification['bytes']
assert item['file_id'] == receipt['file_id'] and item['version_id'] == '0'
assert verification['prior_entries_retained'] == 39895
assert verification['crc'] == verification['every_manifest_entry'] == verification['every_retained_version'] == 'PASS'
retention = json.loads((root/'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives'] == 18 and retention['omissions'] == 0
metrics = json.loads((root/'records/checkpoint19_metrics.json').read_text())
assert metrics['statements'] == 269 and metrics['bibliography_entries'] == 108
inventory_count = len(list(csv.DictReader((root/'records/computation_inventory.csv').open())))
review = (root/'records/progress_review_19h.md').read_text()
review_time = re.search(r'^Actual review record:(.+)\.$', review, re.M).group(1)
driver = (root/'records/checkpoint19_capture_driver.log').read_text()
capture_time = re.search(r'^Immutable capture completed:\s*(.+)$', driver, re.M).group(1)
release = json.loads((root/'records/checkpoint19_writer_release.json').read_text())
encoding = json.loads((root/'records/checkpoint19_delivery_encoding.json').read_text())
assert encoding['delivery_bytes'] == verification['bytes']
assert encoding['delivery_sha256'] == verification['sha256']
assert encoding['original_unchanged'] == encoding['entry_names_order_and_every_byte'] == 'PASS'
record = f'''## Checkpoint19: saved and verified

Review: {review_time}, CONTINUE.
Immutable capture completed: {capture_time}.
Writer release recorded: {release['released_at']}.
Library creation: {item['created_at']}.
Archive: {receipt['file_name']}.
Bytes: {verification['bytes']}; entries: {verification['entries']}; manifest rows: {verification['manifest_rows']}.
SHA256: {verification['sha256']}.
LibraryID: {receipt['library_file_id']}.
FileID: {receipt['file_id']}.
Version: 0. Independent metadata size/name/identity matched the receipt.
Local identity metadata applied successfully.
The first native preparation rejected the original {encoding['original_bytes']}-byte
container because the per-file limit is {encoding['native_limit_bytes']} bytes.
The original captured ZIP remains unchanged, SHA256 {encoding['original_sha256']}.
The delivered ZIP is a lossless re-encoding of the SAME snapshot, completed
at {encoding['completed_at']}. Every entry name, order and uncompressed
byte is identical, checked against the preserved original; only the ZIP
compression method of text entries changed to standard ZIP LZMA method14.
No second snapshot or new checkpoint content was introduced.
CRC/every manifest entry/every retained version: PASS.
All 39895 earlier archive entries retained byte-exactly; no omissions.
History: {retention['total_historical_copies']} distinct copies,
{retention['total_historical_bytes']} bytes. Computation inventory: {inventory_count} programs.
Final formal PDF: {metrics['pages']} pages, {metrics['pdf_bytes']} bytes,
269 statements, 108 bibliography records, 49 task rows;
225 Proved, 19 Refuted, 19 Open, 6 Known.
PDF SHA256: {metrics['pdf_sha256']}.
Exact visible QA: records/checkpoint19_typesetting.txt.
Zero final overflow/warning/undefined-reference/error counts.
Before/after layout counts and the actual visible inspections are recorded
in the typesetting file. All bibliography records have explicit status.

The late all-eight stabilizer, actual E-cover/Smith comparison and complete
root-path chain results are retained as accepted research after the formal
build. They are not counted as extra statements in this PDF. The completed
archive remains immutable. This verification, receipt, metadata and delivery
record are post-snapshot and enter checkpoint20. Both main full decisions
remain Open. Substantive work resumed immediately after capture.
Next review/checkpoint: 2026-11-16 20:49:30 UTC.
'''
for relative in ('records/checkpoints.md', 'records/continuation_state.md'):
    p = root/relative
    s = p.read_text()
    assert '## Checkpoint19: saved and verified' not in s
    p.write_text(s+'\n'+record)
print('Checkpoint19 receipt, independent metadata and archive checks agree.')
print('Next deadline: 2026-11-16 20:49:30 UTC; record written', datetime.now(timezone.utc).isoformat())
