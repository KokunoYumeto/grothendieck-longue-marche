"""Record checkpoint20 only after immutable verification and a verified successful save."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import re

root = Path(__file__).resolve().parents[1]
verification = json.loads((root/'records/checkpoint20_archive_verification.json').read_text())
native_tar = json.loads((root/'records/checkpoint20_system_tar_verification.json').read_text())
receipts = json.loads((root/'records/checkpoint20_upload_result.json').read_text())['results']
assert len(receipts) == 1
receipt = receipts[0]
metadata = json.loads((root/'records/checkpoint20_library_metadata.json').read_text())
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
assert receipt['file_name'] == verification['archive'] == 'LM4_SUCCESSOR_checkpoint_20.zip'
assert item['size_bytes'] == verification['bytes']
assert item['file_id'] == receipt['file_id'] and item['version_id'] == '0'
assert verification['prior_entries_retained'] == 44877
assert verification['crc'] == verification['every_manifest_entry'] == verification['every_retained_version'] == 'PASS'
assert native_tar['system_tar_restore'] == native_tar['every_original_png_path_and_byte'] == 'PASS'
assert native_tar['archive_sha256'] == verification['sha256']
retention = json.loads((root/'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives'] == 19 and retention['omissions'] == 0
metrics = json.loads((root/'records/checkpoint20_metrics.json').read_text())
assert metrics['statements'] == 274 and metrics['bibliography_entries'] == 108
inventory_count = len(list(csv.DictReader((root/'records/computation_inventory.csv').open())))
review = (root/'records/progress_review_20h.md').read_text()
review_time = re.search(r'^Actual review record:(.+)\.$', review, re.M).group(1)
driver = (root/'records/checkpoint20_capture_driver.log').read_text()
capture_time = re.search(r'^Immutable capture completed:\s*(.+)$', driver, re.M).group(1)
release = json.loads((root/'records/checkpoint20_writer_release.json').read_text())
packaging = json.loads((root/'records/checkpoint_20_packaging.json').read_text())
assert packaging['image_paths'] == native_tar['image_paths']
assert packaging['standard_tar_hardlinks'] == native_tar['hardlink_image_paths']
record = f'''## Checkpoint20: saved and verified

Review:{review_time}, CONTINUE.
Immutable capture completed:{capture_time}.
Writer release recorded:{release['released_at']}.
Library creation:{item['created_at']}.
Archive:{receipt['file_name']}.
Bytes:{verification['bytes']}; logical entries:{verification['entries']};
physical ZIP entries:{verification['physical_zip_entries']};
manifest rows:{verification['manifest_rows']}.
SHA256:{verification['sha256']}.
LibraryID:{receipt['library_file_id']}.
FileID:{receipt['file_id']}.
Version:0. Independent metadata size/name/identity matched the receipt.
Local identity metadata applied successfully.

CRC/every logical manifest entry/every retained version:PASS.
All44877 earlier archive entries retained byte-exactly; no omissions.
History:{retention['total_historical_copies']} distinct copies,
{retention['total_historical_bytes']} bytes.
Computation inventory:{inventory_count} programs at capture.
The standard nested verification-images TAR retains{packaging['image_paths']}
original PNG paths, with{packaging['standard_tar_hardlinks']} standard hardlinks
for identical contents. A separate actual system-tar extraction verified
every original image path, size and byte hash without importing the
packager or logical reader. All mathematical sources, PDFs, complete
data, code, reports and logs remain direct ZIP entries. Restoration:
from the ZIP extraction parent run
tar -xf LM4_SUCCESSOR/verification_images.tar
The nested container SHA256 is{packaging['image_bundle_sha256']}.
All nineteen earlier archives remain unchanged.

Final formal PDF:{metrics['pages']} pages,{metrics['pdf_bytes']} bytes,
274 statements,108 bibliography records,49 task rows;
230 Proved,19 Refuted,19 Open,6 Known.
PDF SHA256:{metrics['pdf_sha256']}.
Visible QA:records/checkpoint20_typesetting.txt,53 rendered pages,
six contact sheets and23 individually inspected critical pages.
Zero final overflow/warning/undefined-reference/error counts.
Before/after overflow counts0/0; bibliography stranded-line repair and
all actual build attempts are explicitly recorded. All bibliography
records retain verification status.

B101--B105 are integrated. Late whole-kernel, finite-domain Tate,
source-coset, nonlinear comb/transport and actual filling-kernel
research is retained at its exact scope without extra formal rows.
Both main full decisions remain Open. This verification, receipt,
metadata and delivery record are post-snapshot and enter checkpoint21.
Substantive work resumed immediately after immutable capture.
Next review/checkpoint:2026-11-16 21:49:30 UTC.
'''
for relative in ('records/checkpoints.md','records/continuation_state.md'):
    path=root/relative
    current=path.read_text()
    assert '## Checkpoint20: saved and verified' not in current
    path.write_text(current+'\n'+record)
print('Checkpoint20 receipt, independent metadata, archive and native TAR checks agree.')
print('Next deadline:2026-11-16 21:49:30 UTC; record written',datetime.now(timezone.utc).isoformat())
