from pathlib import Path
from datetime import datetime, timezone
import zipfile,sys
root=Path(__file__).resolve().parents[1]
n=int(sys.argv[1])
out=root.parent/f'MPL_118_checkpoint_{n:02d}.zip'
if out.exists(): raise RuntimeError('Refusing to overwrite checkpoint')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f: f.write(f'hourly checkpoint {n:02d} assembled {now}\n')
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(root.rglob('*')):
  if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.zip': z.write(p,p.relative_to(root.parent))
print(str(out))
print(out.stat().st_size)
