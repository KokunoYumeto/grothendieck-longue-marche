"""Package current deliverables, with source images and earlier ZIPs excluded."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,zipfile
R=Path(__file__).resolve().parents[1]
output=R.parent/'MPL_67_053-101.zip'
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (R/'progress.log').open('a') as f:
 f.write(f'final archive prepared {now}: current deliverables, records, research, scripts and validation; original attachments/images/context and earlier checkpoint ZIPs excluded.\n')
def eligible(p):
 return p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.zip','.jpg','.jpeg','.png','.pdf'} and p.name!='MANIFEST_SHA256.tsv'
files=sorted(p for p in R.rglob('*') if eligible(p))
manifest=R/'MANIFEST_SHA256.tsv'
manifest.write_text('path\tsha256\tbytes\n'+''.join(f'{p.relative_to(R).as_posix()}\t{hashlib.sha256(p.read_bytes()).hexdigest()}\t{p.stat().st_size}\n' for p in files))
files.append(manifest)
with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(files):z.write(p,p.relative_to(R).as_posix())
with zipfile.ZipFile(output) as z:
 assert z.testzip() is None
 assert len(z.namelist())==len(files)
 assert 'MPL_67_053-101_transcription.tex' in z.namelist()
 assert 'MPL_67_053-101_notes.md' in z.namelist()
 assert 'CHECK_EVENTS.tsv' in z.namelist()
 assert len([x for x in z.namelist() if x.startswith('pages/') and x.endswith('.tex')])==47
 assert not any(x.endswith(('.jpg','.jpeg','.png','.zip','.pdf','.pyc')) for x in z.namelist())
 for p in files:assert z.read(p.relative_to(R).as_posix())==p.read_bytes()
result={'path':str(output),'archive_members':len(files),'bytes':output.stat().st_size,'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'zip_integrity':'passed','all_members_match_current_files':True,'prepared_at_utc':now}
(R.parent/'MPL_67_053-101_zip_validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
