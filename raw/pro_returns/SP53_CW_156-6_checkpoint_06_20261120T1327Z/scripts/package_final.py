"""Package the complete verified deliverables; never create an early partial final ZIP."""
from pathlib import Path
import hashlib,json,zipfile
O=Path(__file__).resolve().parents[1]
m=json.loads((O/'TRANSCRIPTION_SHA256.json').read_text())
assert len(m['hashes'])==29
for name,h in m['hashes'].items():assert hashlib.sha256((O/name).read_bytes()).hexdigest()==h,name
assert 'frozen hashes verified unchanged' in (O/'progress.log').read_text()
dest=O.parent/'deliverables/SP53_CW_156-6.zip'
assert not dest.exists(),'Do not silently replace a final archive'
files=[p for p in sorted(O.rglob('*')) if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts]
(O/'FINAL_FILES.txt').write_text('\n'.join(str(p.relative_to(O)) for p in files)+'\nFINAL_FILES.txt\n')
with zipfile.ZipFile(dest,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(O.rglob('*')):
        if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts:z.write(p,p.relative_to(O))
with zipfile.ZipFile(dest) as z:assert z.testzip() is None
print(json.dumps({'path':str(dest),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
