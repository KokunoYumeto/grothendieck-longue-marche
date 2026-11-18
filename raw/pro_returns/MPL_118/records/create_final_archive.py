"""Build the final deliverable and verify its bytes against the frozen manifest."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, zipfile

ROOT=Path(__file__).resolve().parents[1]
out=ROOT.parent/'MPL_118.zip'
if out.exists(): raise RuntimeError('Refusing to overwrite an existing final archive')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f:
    f.write('final archive preparation '+now+': complete delivery tree; original attachments, scans, context sources and earlier checkpoint ZIPs excluded\n')
manifest_path=ROOT/'records/delivery_manifest.json'
files=[p for p in sorted(ROOT.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.zip' and p!=manifest_path]
entries={str(p.relative_to(ROOT)):{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files}
manifest_path.write_text(json.dumps({'assembled_utc':now,'scope':'All payload files except this manifest itself; archive root contains the requested filenames directly.','entries':entries},ensure_ascii=False,indent=2)+'\n')
files.append(manifest_path)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(files):z.write(p,p.relative_to(ROOT))
frozen=json.loads((ROOT/'records/frozen_sha256.json').read_text())['sha256']
with zipfile.ZipFile(out) as z:
    assert z.testzip() is None, 'Archive CRC check failed'
    assert set(z.namelist())==set(entries)|{'records/delivery_manifest.json'}
    for name,item in entries.items():
        data=z.read(name)
        assert len(data)==item['bytes'] and hashlib.sha256(data).hexdigest()==item['sha256'],name
    for name,h in frozen.items():assert hashlib.sha256(z.read(name)).hexdigest()==h,name
    assert all(not name.lower().endswith(('.jpg','.jpeg','.png','.pdf','.zip')) for name in z.namelist())
    assert all(not name.startswith(('context/','scans/','upload/')) for name in z.namelist())
result={'archive':str(out),'bytes':out.stat().st_size,'entries':len(files),
        'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
        'crc_and_payload_hashes_verified':True,'frozen_archive_entries_verified':len(frozen),
        'original_attachments_excluded':True,'created_utc':now}
print(json.dumps(result,ensure_ascii=False))
