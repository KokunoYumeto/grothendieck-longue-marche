#!/usr/bin/env python3
"""Verify frozen source integrity and package the finished delivery, excluding inputs."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,sys,zipfile
R=Path(__file__).resolve().parents[1]
P='MPL_33_098-146'
def utc():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
hashes=json.loads((R/'records/frozen_sha256.json').read_text())
assert len(hashes)==50
for name,digest in hashes.items():
    assert hashlib.sha256((R/name).read_bytes()).hexdigest()==digest,name
with (R/'progress.log').open('a') as f:
    f.write('final frozen transcription hashes unchanged '+utc()+'; 50/50 verified against the pre-context SHA-256 manifest\n')
result=subprocess.run([sys.executable,str(R/'tools/validate.py')],capture_output=True,text=True)
(R/'records/structural_validation_final.txt').write_text(result.stdout+result.stderr)
print(result.stdout)
assert result.returncode==0
required={f'{P}_transcription.tex',f'{P}_doubts.md',f'{P}_inventory.csv',f'{P}_notes.md','progress.log'}
required.update(f'pages/{P}_33_scan{s:03d}.tex' for s in range(98,147))
files=sorted(p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc')
relative={str(p.relative_to(R)) for p in files}
assert required<=relative
assert len([x for x in relative if x.startswith('pages/') and x.endswith('.tex')])==49
assert not any(p.suffix.lower() in {'.jpg','.jpeg','.png','.pdf','.zip'} for p in files)
assert not any(x.startswith(('scans/','context/','upload/')) for x in relative)
out=R.parent/f'{P}.zip'
with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:z.write(p,p.relative_to(R))
with zipfile.ZipFile(out) as z:
    assert z.testzip() is None
    assert set(z.namelist())==relative
    for name,digest in hashes.items():
        assert hashlib.sha256(z.read(name)).hexdigest()==digest,name
    assert z.read(f'{P}_transcription.tex').startswith(b'\\cotefile{33}\n\\scanpage{98}')
report={'verified_utc':utc(),'archive':str(out),'members':len(relative),'page_files':49,
        'frozen_hashes_unchanged':50,'archive_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
        'bytes':out.stat().st_size,'inputs_and_prior_zips_excluded':True}
(R.parent/f'{P}_package_receipt.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
