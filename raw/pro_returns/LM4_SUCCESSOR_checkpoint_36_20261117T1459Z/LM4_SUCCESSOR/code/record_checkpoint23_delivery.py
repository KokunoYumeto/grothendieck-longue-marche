"""Record checkpoint23 after immutable verification and confirmed saved metadata."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import re

root=Path(__file__).resolve().parents[1]
read=lambda name:json.loads((root/'records'/name).read_text())
v=read('checkpoint23_archive_verification.json')
t=read('checkpoint23_system_tar_verification.json')
results=read('checkpoint23_upload_result.json')['results']
assert len(results)==1
r=results[0]
assert r['status']=='succeeded' and r['local_metadata_applied']
metadata=read('checkpoint23_library_metadata.json')
found=[]
def walk(value):
    if isinstance(value,dict):
        if value.get('library_file_id')==r['library_file_id'] and value.get('name')==r['file_name']:
            found.append(value)
        for item in value.values():walk(item)
    elif isinstance(value,list):
        for item in value:walk(item)
walk(metadata)
assert len(found)==1
item=found[0]
assert r['file_name']==v['archive']=='LM4_SUCCESSOR_checkpoint_23.zip'
assert item['size_bytes']==v['bytes']
assert item['file_id']==r['file_id'] and item['version_id']=='0'
assert v['prior_entries_retained']==61931
assert v['crc']==v['every_manifest_entry']==v['every_retained_version']=='PASS'
assert t['system_tar_restore']==t['every_original_png_path_and_byte']=='PASS'
assert t['archive_sha256']==v['sha256']
retention=read('checkpoint_version_retention_summary.json')
assert retention['archives']==22 and retention['omissions']==0
m=read('checkpoint23_metrics.json')
assert m['statements']==283 and m['pages']>=439 and m['bibliography_entries']==111
assert m['statuses']=={'Known':6,'Proved':239,'Refuted':19,'Open':19}
release=read('checkpoint23_writer_release.json')
p=read('checkpoint_23_packaging.json')
assert p['image_paths']==t['image_paths']
assert p['standard_tar_hardlinks']==t['hardlink_image_paths']
inventory_count=len(list(csv.DictReader((root/'records/computation_inventory.csv').open())))
review=(root/'records/progress_review_23h.md').read_text()
review_time=re.search(r'^Actual review record: (.+)\.$',review,re.M).group(1)
driver=(root/'records/checkpoint23_capture_driver.log').read_text()
capture_time=re.search(r'^Immutable capture completed:\s*(.+)$',driver,re.M).group(1)
qa=read('checkpoint23_visual_review.json')
record=f'''## Checkpoint23: saved and verified

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
All61931 logical entries of the twenty-two earlier archives are retained
byte-exactly,with zero omissions. History contains
{retention['total_historical_copies']} distinct copies totaling
{retention['total_historical_bytes']} bytes. The computation inventory
contains{inventory_count} programs at capture. Standard nested TAR encoding
retains all{p['image_paths']} original PNG paths,with
{p['standard_tar_hardlinks']} standard hardlinks. Independent native tar
extraction verified every path,size and byte hash,without importing the
packager or logical reader. Restore from the ZIP extraction parent:
tar -xf LM4_SUCCESSOR/verification_images.tar
All twenty-two earlier archives remain unchanged.

The final formal PDF has{m['pages']} pages,283 statements(239 Proved,
19 Refuted,19 Open,6 Known),111 printed bibliography entries and49
task/lead rows. PDF bytes:{m['pdf_bytes']}; SHA-256:{m['pdf_sha256']}.
Final QA:zero overfull boxes,warnings,undefined references anderrors.
Initial/final combined overfull counts:0/0. The complete genuine
bibliography-inclusion and author-year repair history is preserved.
Six fresh contact sheets cover{len(qa['rendered_pages'])} sampled final
pages;{len(qa['individually_inspected_pages'])} critical final pages were
inspected individually,including every page of B112--B114. No earlier
inspection substitutes for these final views.

B112--B114 are integrated with complete root and independent reviews:
the actual annular bad-region centralizer and free-five source,the
whole-region and selected-original-cover comparison,and the exact
one-neck quotient by two independently nontrivial cross commutators.
The exact actual mirror9/36 and8/24 presentations,regional base-loop
centralizer,coarse whole-height model and precise failed subgroup gates
remain at their reviewed research scope. Both main full decisions are Open.

This postcapture verification,save receipt,metadata and delivery record
enter checkpoint24. Substantive work resumed immediately after capture.
Next review/checkpoint:2026-11-17 00:49:30 UTC.
'''
for relative in ('records/checkpoints.md','records/continuation_state.md'):
    path=root/relative;old=path.read_text()
    assert '## Checkpoint23: saved and verified' not in old
    path.write_text(old+'\n'+record)
print('Checkpoint23 archive,native TAR verification,receipt and metadata agree.')
print('Delivery record written',datetime.now(timezone.utc).isoformat())
