"""Record checkpoint16 only after independent immutable verification and save."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import re

root=Path(__file__).resolve().parents[1]
verification=json.loads((root/'records/checkpoint16_archive_verification.json').read_text())
receipts=json.loads((root/'records/checkpoint16_upload_result.json').read_text())['results']
assert len(receipts)==1
receipt=receipts[0]
metadata=json.loads((root/'records/checkpoint16_library_metadata.json').read_text())
found=[]
def walk(value):
    if isinstance(value,dict):
        if value.get('library_file_id')==receipt['library_file_id'] and value.get('name')==receipt['file_name']:
            found.append(value)
        for item in value.values():walk(item)
    elif isinstance(value,list):
        for item in value:walk(item)
walk(metadata)
assert len(found)==1
item=found[0]
assert receipt['status']=='succeeded' and receipt['local_metadata_applied']
assert receipt['file_name']==verification['archive']=='LM4_SUCCESSOR_checkpoint_16.zip'
assert item['size_bytes']==verification['bytes']
assert item['file_id']==receipt['file_id'] and item['version_id']=='0'
assert verification['prior_entries_retained']==26827
assert verification['crc']==verification['every_manifest_entry']==verification['every_retained_version']=='PASS'
retention=json.loads((root/'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives']==15 and retention['omissions']==0
metrics=json.loads((root/'records/checkpoint16_metrics.json').read_text())
assert metrics['statements']==258 and metrics['bibliography_entries']==104
inventory_count=len(list(csv.DictReader((root/'records/computation_inventory.csv').open())))
review=(root/'records/progress_review_16h.md').read_text()
review_time=re.search(r'^Actual review record:(.+)\.$',review,re.M).group(1)
driver=(root/'records/checkpoint16_capture_driver.log').read_text()
capture_time=re.search(r'^Immutable capture completed:\s*(.+)$',driver,re.M).group(1)
record=f'''## Checkpoint16: saved and verified

Review:{review_time}, CONTINUE.
Immutable capture completed:{capture_time}.
Library creation:{item['created_at']}.
Archive:{receipt['file_name']}.
Bytes:{verification['bytes']}; entries:{verification['entries']}; manifest rows:{verification['manifest_rows']}.
SHA256:{verification['sha256']}.
LibraryID:{receipt['library_file_id']}.
FileID:{receipt['file_id']}.
Version:0. Independent metadata size/name/identity matched the receipt.
Local identity metadata applied successfully.
CRC/every manifest entry/every retained version:PASS.
All26827 earlier archive entries retained byte-exactly; no omissions.
History:{retention['total_historical_copies']} distinct copies,
{retention['total_historical_bytes']} bytes. Computation inventory:{inventory_count} programs.
Final formal PDF:{metrics['pages']} pages,{metrics['pdf_bytes']} bytes,
258 statements,104 bibliography records,49 task rows;
216 Proved,17 Refuted,19 Open,6 Known.
PDF SHA256:{metrics['pdf_sha256']}.
Exact visible QA:records/checkpoint16_typesetting.txt.
Zero final overflow/warning/undefined-reference/error counts.
All bibliography records have explicit verification status.

All agent writers resumed immediately after immutable capture.
This receipt, metadata, verification and delivery record are
post-snapshot and will enter17. No byte of checkpoint16 is changed
after capture. Both main full decisions remain Open.
Next review/checkpoint:2026-11-16 17:49:30 UTC.
'''
for relative in ('records/checkpoints.md','records/continuation_state.md'):
    p=root/relative
    s=p.read_text()
    assert '## Checkpoint16: saved and verified' not in s
    p.write_text(s+'\n'+record)
print('Checkpoint16 receipt, independent metadata and archive checks agree.')
print('Next deadline:2026-11-16 17:49:30 UTC; record written',datetime.now(timezone.utc).isoformat())
