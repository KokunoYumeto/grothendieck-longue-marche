"""Freeze and package the complete adjudicated transcription, without compilation.

Run only after scan 017 and the recorded cross-page notation reconciliation.
This script does not upload. The final archive is saved by the official upload helper.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,sys,zipfile

OUT=Path(__file__).resolve().parents[1]
PREFIX='SP48_CW_104'
def utc():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

expected=[f"{'H104-01' if n<10 else 'H104-02'}_104_scan{n:03d}.tex" for n in range(2,18)]
pages=sorted((OUT/'pages').glob('*.tex'))
if [p.name for p in pages]!=expected:raise RuntimeError('Exactly all 16 named pages are required')
log=(OUT/'progress.log').read_text()
if 'transcription frozen ' in log:raise RuntimeError('Transcription already frozen; verify existing freeze instead')
for n in range(2,18):
    if log.count(f'scan {n:03d} done ')!=1:raise RuntimeError(f'Scan {n:03d} not committed exactly once')
    d=json.loads((OUT/f'records/scan{n:03d}/decision.json').read_text())
    if not d.get('main_adjudication_complete'):raise RuntimeError(f'Incomplete adjudication for {n}')
if not (OUT/'notation_reconciliation.md').exists():raise RuntimeError('Missing final notation reconciliation record')
subprocess.run([sys.executable,str(OUT/'scripts/build_records.py')],check=True)
subprocess.run([sys.executable,str(OUT/'scripts/validate_transcription.py')],check=True)
paths=pages+[OUT/f'{PREFIX}_transcription.tex']
hashes={str(p.relative_to(OUT)):sha(p) for p in paths}
(OUT/'transcription_hashes.sha256').write_text(''.join(f'{h}  {name}\n' for name,h in hashes.items()))
with (OUT/'progress.log').open('a') as f:
    f.write('transcription frozen '+utc()+'\n')
    for name,h in hashes.items():f.write(f'SHA-256 {h} {name}\n')
if any(sha(OUT/name)!=h for name,h in hashes.items()):raise RuntimeError('Frozen transcription changed')
with (OUT/'progress.log').open('a') as f:f.write('frozen hashes checked unchanged '+utc()+' (all 16 pages and combined transcription)\n')
target=OUT.parent/f'{PREFIX}.zip'
if target.exists():raise RuntimeError('Refusing to overwrite the final archive')
files=[p for p in sorted(OUT.rglob('*')) if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts]
if any('source' in p.relative_to(OUT).parts or 'reader_inputs' in p.relative_to(OUT).parts for p in files):
    raise RuntimeError('Source inputs must not be packaged')
with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in files:z.write(p,p.relative_to(OUT))
with zipfile.ZipFile(target) as z:
    if any(hashlib.sha256(z.read(name)).hexdigest()!=h for name,h in hashes.items()):
        raise RuntimeError('Archived transcription does not match frozen hashes')
print(json.dumps({'final_archive':str(target),'bytes':target.stat().st_size,'entries':len(files),
                  'frozen_text_files':len(hashes),'archive_sha256':sha(target),'hashes_unchanged':True}))
