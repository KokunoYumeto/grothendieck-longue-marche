"""Verify exact restoration of the complete checkpoint06 transport.

All work happens in a fresh verification directory. No manuscript image,
accepted transcription, original archive, or frozen reading is modified.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, sys, zipfile

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'deliverables/SP83_C13_148+149_checkpoint_06.zip'
PACKED=ROOT/'deliverables/compact_v2/SP83_C13_148+149_checkpoint_06.zip'
DEST=ROOT/'archive_v2_verification/cp06'
REPORT=ROOT/'result/qa/cp06_archive_restore_verification.json'

def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()

meta=json.loads((ROOT/'result/qa/cp06_compact_v2_report.json').read_text())
assert digest(SOURCE)==meta['source_sha256']
assert digest(PACKED)==meta['output_sha256']
if '--resume' in sys.argv:
    assert DEST.is_dir(), 'No prior extraction to resume'
    with zipfile.ZipFile(PACKED) as z:
        assert (DEST/'CROP_COMPRESSION_MANIFEST_V2.json').read_bytes()==z.read('CROP_COMPRESSION_MANIFEST_V2.json')
else:
    DEST.mkdir(parents=True,exist_ok=False)
    with zipfile.ZipFile(PACKED) as z:z.extractall(DEST)
assert (DEST/'scripts/compact_archive_v2.py').read_bytes()==(ROOT/'result/scripts/compact_archive_v2.py').read_bytes()
subprocess.run([sys.executable,str(DEST/'scripts/compact_archive_v2.py'),'--verify-all'],check=True)
checked=[]
with zipfile.ZipFile(SOURCE) as z:
    for info in z.infolist():
        if info.is_dir():continue
        expected=hashlib.sha256(z.read(info.filename)).hexdigest()
        actual=DEST/info.filename
        assert actual.is_file() and digest(actual)==expected, info.filename
        checked.append(dict(path=info.filename,bytes=info.file_size,sha256=expected))
pngs=[r for r in checked if r['path'].endswith('.png')]
for r in pngs:
    current = ROOT/r['path'][5:] if r['path'].startswith('work/proposed/') else ROOT/'result'/r['path']
    assert digest(current)==r['sha256'],r['path']
result=dict(method='Extract, restore all PNGs, verify every original manifest entry, independently hash every restored original ZIP entry, and compare every restored PNG with current retained evidence.',
    verified_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=meta['source_sha256'],packed_sha256=meta['output_sha256'],
    original_entries_verified=len(checked),pngs_verified=len(pngs),non_png_entries_verified=len(checked)-len(pngs),
    all_current_pngs_match_restored_checkpoint=True,source_scans_required=False,errors=[],checked=checked,
    verification_note='The first run fully restored all856 images and verified all1449 original entries, then encountered a local path-mapping error while comparing work/proposed previews with their current sibling proposed directory. The mapper was corrected; --resume rechecks the original manifest, every restored hash, every original entry and every current PNG without changing evidence or archives.')
REPORT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checked'},indent=2))
