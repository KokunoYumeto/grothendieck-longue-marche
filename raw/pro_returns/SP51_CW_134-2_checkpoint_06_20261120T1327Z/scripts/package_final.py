"""Package every deliverable and work record, excluding input sources and old ZIPs."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import json,hashlib
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'records/frozen_transcription_sha256.json').read_text())
for name,digest in manifest['sha256'].items():
 if hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest:raise RuntimeError(f'Changed frozen transcription: {name}')
if 'transcription hashes unchanged' not in (root/'progress.log').read_text():raise RuntimeError('Final hash verification must be recorded')
dest=root.parent/'deliverables/SP51_CW_134-2.zip'
dest.parent.mkdir(parents=True,exist_ok=True)
if dest.exists():raise FileExistsError(dest)
files=sorted(p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.zip')
(root/'records/final_file_list.txt').write_text('\n'.join(str(p.relative_to(root)) for p in files)+'\nrecords/final_file_list.txt\n')
with ZipFile(dest,'x',ZIP_DEFLATED,compresslevel=6) as z:
 for p in sorted(root.rglob('*')):
  if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.zip':z.write(p,p.relative_to(root))
with ZipFile(dest) as z:
 bad=z.testzip()
 if bad:raise RuntimeError(f'ZIP integrity failure: {bad}')
 if sum(name.startswith('pages/') and name.endswith('.tex') for name in z.namelist())!=16:raise RuntimeError('Page count in ZIP is not 16')
print(json.dumps({'path':str(dest),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
