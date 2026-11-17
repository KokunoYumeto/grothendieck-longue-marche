"""Record checkpoint22 only after immutable verification and a confirmed save."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import re

root = Path(__file__).resolve().parents[1]
read = lambda name: json.loads((root/'records'/name).read_text())
v = read('checkpoint22_archive_verification.json')
t = read('checkpoint22_system_tar_verification.json')
results = read('checkpoint22_upload_result.json')['results']
assert len(results) == 1
r = results[0]
assert r['status'] == 'succeeded' and r['local_metadata_applied']
metadata = read('checkpoint22_library_metadata.json')
found = []
def walk(value):
    if isinstance(value,dict):
        if value.get('library_file_id') == r['library_file_id'] and value.get('name') == r['file_name']:
            found.append(value)
        for item in value.values():
            walk(item)
    elif isinstance(value,list):
        for item in value:
            walk(item)
walk(metadata)
assert len(found) == 1
item = found[0]
assert r['file_name'] == v['archive'] == 'LM4_SUCCESSOR_checkpoint_22.zip'
assert item['size_bytes'] == v['bytes']
assert item['file_id'] == r['file_id'] and item['version_id'] == '0'
assert v['prior_entries_retained'] == 55959
assert v['crc'] == v['every_manifest_entry'] == v['every_retained_version'] == 'PASS'
assert t['system_tar_restore'] == t['every_original_png_path_and_byte'] == 'PASS'
assert t['archive_sha256'] == v['sha256']
retention = read('checkpoint_version_retention_summary.json')
assert retention['archives'] == 21 and retention['omissions'] == 0
m = read('checkpoint22_metrics.json')
assert m['statements'] == 280 and m['pages'] == 425 and m['bibliography_entries'] == 109
assert m['statuses'] == {'Known':6,'Proved':236,'Refuted':19,'Open':19}
release = read('checkpoint22_writer_release.json')
p = read('checkpoint_22_packaging.json')
assert p['image_paths'] == t['image_paths']
assert p['standard_tar_hardlinks'] == t['hardlink_image_paths']
inventory_count = len(list(csv.DictReader((root/'records/computation_inventory.csv').open())))
review = (root/'records/progress_review_22h.md').read_text()
review_time = re.search(r'^Actual review record: (.+)\.$',review,re.M).group(1)
driver = (root/'records/checkpoint22_capture_driver.log').read_text()
capture_time = re.search(r'^Immutable capture completed:\s*(.+)$',driver,re.M).group(1)
record = f'''## Checkpoint22: saved and verified

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
Independent metadata matches name,size,identity andversion; local identity applied.

CRC,every logical manifest entry and every retained version:PASS.
All55959 entries of the twenty-one earlier archives are retained byte-exactly,
with zero omissions. History contains{retention['total_historical_copies']}
distinct copies totaling{retention['total_historical_bytes']} bytes.
The computation inventory contains{inventory_count} programs at capture.
The standard nested verification-images TAR retains all{p['image_paths']}
original PNG paths,with{p['standard_tar_hardlinks']} standard hardlinks.
Independent native tar extraction verified every original path,size and
byte hash without importing the packager or logical reader. Restore from
the ZIP extraction parent:tar -xf LM4_SUCCESSOR/verification_images.tar
All twenty-one earlier archives remain unchanged.

The formal PDF has425 pages,280 statements(236 Proved,19 Refuted,
19 Open,6 Known),109 bibliography records and49 task/lead rows.
PDF bytes:{m['pdf_bytes']}; SHA-256:{m['pdf_sha256']}.
Final QA:zero overfull boxes,warnings,undefined references anderrors.
Initial/final overfull counts are1/0; the231.64224pt path was repaired,
and its genuine failed build,PDF,log and sources remain. Six fresh contact
sheets cover44 sampled pages;20 critical pages were inspected individually,
including every page of B108--B111. No inherited inspection is counted.

B108--B111 are integrated with complete root and independent proof reviews:
proper actual one-neck full completion,natural mixed-neck noninjection,
the actual slit bad-vertex centralizer/source and one-neck selected-cover
comparison,and an explicit nontrivial slit diagonal killed by q0.
The later annular presentation/source research is retained at its exact
reviewed stage in the computation audit and late research notes.
Both main full decisions remain Open. This postcapture verification,
save receipt,metadata and delivery record enter checkpoint23.
Substantive work resumed immediately after capture.
Next review/checkpoint:2026-11-16 23:49:30 UTC.
'''
for relative in ('records/checkpoints.md','records/continuation_state.md'):
    path = root/relative
    old = path.read_text()
    assert '## Checkpoint22: saved and verified' not in old
    path.write_text(old+'\n'+record)
print('Checkpoint22 archive,native TAR verification,receipt and metadata agree.')
print('Delivery record written',datetime.now(timezone.utc).isoformat())
