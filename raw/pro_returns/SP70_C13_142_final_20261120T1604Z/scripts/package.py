from pathlib import Path
from datetime import datetime, timezone
from zipfile import ZipFile, ZIP_DEFLATED
import sys,hashlib
W=Path(__file__).resolve().parents[1]
name=sys.argv[1]
assert name.endswith('.zip') and '/' not in name
p=W.parent/name
if p.exists():raise SystemExit('Refusing to overwrite an existing archive')
files=[f for f in sorted(W.rglob('*')) if f.is_file() and '__pycache__' not in f.parts and f.suffix.lower() not in {'.png','.jpg','.jpeg','.webp','.gif','.zip','.pyc'}]
with ZipFile(p,'x',ZIP_DEFLATED) as z:
 for f in files:z.write(f,f.relative_to(W))
assert ZipFile(p).testzip() is None
print(str(p));print(f'{len(files)} files; {p.stat().st_size} bytes; SHA-256 {hashlib.sha256(p.read_bytes()).hexdigest()}')
