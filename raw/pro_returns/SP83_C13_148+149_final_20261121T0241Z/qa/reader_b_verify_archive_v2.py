"""Independent byte-level comparison of a restored v2 CP05 with the original ZIP.

No original archive, accepted text, record, or frozen TSV is modified.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'deliverables/SP83_C13_148+149_checkpoint_05.zip'
PACKED = ROOT / 'deliverables/compact_v2/SP83_C13_148+149_checkpoint_05.zip'
DESTINATION = ROOT / 'archive_v2_verification/cp05'
REPORT = ROOT / 'result/qa/reader_b_archive_restore_verification.json'

def sha_file(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()

DESTINATION.mkdir(parents=True,exist_ok=False)
with zipfile.ZipFile(PACKED) as z:
    z.extractall(DESTINATION)
assert (DESTINATION / 'scripts/compact_archive_v2.py').read_bytes() == (ROOT / 'result/scripts/compact_archive_v2.py').read_bytes()
subprocess.run([sys.executable,str(DESTINATION/'scripts/compact_archive_v2.py'),'--verify-all'],check=True)

checked = []
with zipfile.ZipFile(SOURCE) as z:
    for info in z.infolist():
        if info.is_dir(): continue
        original = z.read(info.filename)
        expected = hashlib.sha256(original).hexdigest()
        destination = DESTINATION / info.filename
        assert destination.is_file(), info.filename
        assert sha_file(destination) == expected, info.filename
        checked.append({'path':info.filename,'bytes':len(original),'sha256':expected})

baseline = json.loads((ROOT/'result/qa/reader_b_archive_baseline.json').read_text())
source_hash = sha_file(SOURCE)
assert source_hash == baseline['original_source_sha256']
report = {'method':'Extract new v2 archive, restore all images, then independently compare every original ZIP entry with restored file bytes by SHA256.',
          'source':str(SOURCE),'source_sha256':source_hash,
          'packed':str(PACKED),'packed_sha256':sha_file(PACKED),
          'restored_directory':str(DESTINATION),
          'all_original_entries_verified':len(checked),
          'pngs_verified':sum(r['path'].endswith('.png') for r in checked),
          'non_png_entries_verified':sum(not r['path'].endswith('.png') for r in checked),
          'source_hash_matches_preexisting_v1_manifest':True,
          'checked':checked}
REPORT.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='checked'},indent=2),flush=True)
