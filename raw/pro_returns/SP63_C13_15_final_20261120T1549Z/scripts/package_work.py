"""Package only completed deliverables and documentation; never source or image files."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,zipfile
p=argparse.ArgumentParser();p.add_argument('name');a=p.parse_args()
root=Path(__file__).resolve().parents[1];out=root.parent/a.name
if out.exists():raise SystemExit('Refusing to overwrite an existing archive')
forbidden={'.png','.jpg','.jpeg','.gif','.webp','.tif','.tiff','.bmp','.zip','.pyc'}
files=[f for f in sorted(root.rglob('*')) if f.is_file() and '__pycache__' not in f.parts and f.suffix.lower() not in forbidden]
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f:f.write(f'archive prepared {a.name} {now}\n')
with zipfile.ZipFile(out,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for f in files:z.write(f,f.relative_to(root))
 if z.testzip() is not None:raise SystemExit('ZIP CRC failure')
print(str(out));print(f'{len(files)} files; {out.stat().st_size} bytes')
