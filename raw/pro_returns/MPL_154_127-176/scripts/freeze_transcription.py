#!/usr/bin/env python3
"""One-time assembly and freeze after root's complete visual audit."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,re,subprocess,sys

root=Path(__file__).resolve().parents[1]
log=root/'progress.log'
old=log.read_text()
assert not re.search(r'^transcription frozen ',old,re.M), 'already frozen'
assert 'context opened ' not in old, 'context has already been opened'
pages=[root/f'pages/MPL_154_127-176_154_scan{n}.tex' for n in range(127,177)]
for n,p in zip(range(127,177),pages):
    assert p.is_file()
    assert len(re.findall(rf'^154 scan {n} done ',old,re.M))==1
    assert len(re.findall(rf'^scan {n} audited ',old,re.M))==1
with (root/'records/post_audit_compile_coverage.csv').open(newline='') as f:
    coverage=list(csv.DictReader(f))
assert coverage, 'compile coverage missing'
combined=root/'MPL_154_127-176_transcription.tex'
combined.write_bytes(b'\n'.join(p.read_bytes() for p in pages))
assert combined.read_text().startswith('\\cotefile{154}\n\\scanpage{127}')
check=subprocess.run([sys.executable,str(root/'scripts/validate_package.py'),'--root',str(root)],capture_output=True,text=True)
(root/'records/pre_freeze_validation.txt').write_text(check.stdout+check.stderr)
assert check.returncode==0,check.stdout+check.stderr
files=pages+[combined]
lines=[hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(root)) for p in files]
(root/'records/frozen_hashes.sha256').write_text('\n'.join(lines)+'\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with log.open('a') as f:
    for line in lines:f.write('SHA256 '+line+'\n')
    f.write('transcription frozen '+now+'\n')
print('transcription frozen '+now)
print('51 SHA-256 hashes written; combined bytes',combined.stat().st_size)
