"""Record the verified immutable eleventh checkpoint and its successful save."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
verification = json.loads((root / 'records/checkpoint11_archive_verification.json').read_text())
receipt = json.loads((root / 'records/checkpoint11_upload_result.json').read_text())['results'][0]
metadata = json.loads((root / 'records/checkpoint11_library_metadata.json').read_text())
found = []
def walk(value):
    if isinstance(value, dict):
        if value.get('library_file_id') == receipt['library_file_id'] and value.get('name') == receipt['file_name']:
            found.append(value)
        for item in value.values():
            walk(item)
    elif isinstance(value, list):
        for item in value:
            walk(item)
walk(metadata)
assert len(found) == 1
item = found[0]
assert receipt['status'] == 'succeeded' and receipt['local_metadata_applied']
assert item['size_bytes'] == verification['bytes'] == 283428771
assert item['file_id'] == receipt['file_id']
assert item['version_id'] == '0'
assert verification['prior_entries_retained'] == 11193
assert verification['crc'] == verification['every_manifest_entry'] == verification['every_retained_version'] == 'PASS'
text = f'''## Checkpoint11: saved and verified

Review:2026-11-16T11:49:30.000293+00:00,CONTINUE.
Immutable capture:2026-11-16T11:50:00.624934+00:00.
Created:{item['created_at']}.
Archive:{receipt['file_name']}.
Bytes:{verification['bytes']}; entries:{verification['entries']}; manifestrows:{verification['manifest_rows']}.
SHA256:{verification['sha256']}.
LibraryID:{receipt['library_file_id']}.
FileID:{receipt['file_id']}.
Version:0. Independent metadata size/name/identity matched the receipt.
Local identity metadata applied successfully.
CRC/everymanifestentry/everyretainedversion:PASS.
All11193 earlier archive entries retained byte-exactly; no omissions.
History:369 distinct copies,31319843bytes. Computation inventory:250programs.
Final formalPDF:290pages,2100874bytes,236statements,91bibliographyentries,
49taskrows;197Proved,14Refuted,19Open,6Known.
PDFSHA256:96541d457347af3da1faa61389c724db7b36f55bee7d4c98670660579f40bf2d.
VisualQA:52unique pages,6main contact sheets,15enlarged critical pages;
zero final overflow/warning/undefined-reference/error counts.

The native checkpoint link was delivered in commentary. All agent writers
resumed immediately after immutable capture. This receipt, metadata,
verification and delivery record are post-snapshot and will enter12.
No byte of checkpoint11 is changed after capture. Both main decisions
remain Open. Next review/checkpoint:2026-11-16 12:49:30UTC.
'''
p = root / 'records/checkpoints.md'
s = p.read_text()
if '## Checkpoint11: saved and verified' not in s:
    p.write_text(s + '\n' + text)
p = root / 'records/continuation_state.md'
s = p.read_text()
if '## Checkpoint11: saved and verified' not in s:
    p.write_text(s + '\n' + text)
print('Checkpoint11 receipt, independent metadata and archive checks agree.')
print('Next deadline:2026-11-16 12:49:30UTC; record written', datetime.now(timezone.utc).isoformat())
