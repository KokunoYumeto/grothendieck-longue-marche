"""Archive all written deliverables and work records, excluding supplied sources."""
from pathlib import Path
import argparse, datetime, zipfile
ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument('destination', type=Path)
p.add_argument('--checkpoint', type=int)
a = p.parse_args()
if a.destination.exists():
 raise SystemExit('Refusing to overwrite an existing archive')
if a.checkpoint is not None:
 now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 with (ROOT/'progress.log').open('a') as f:
  f.write(f'hourly checkpoint {a.checkpoint:02} assembled {now}\n')
with zipfile.ZipFile(a.destination, 'w', zipfile.ZIP_DEFLATED) as z:
 for source in sorted(ROOT.rglob('*')):
  if source.is_file() and '__pycache__' not in source.parts and source.suffix not in ('.pyc',):
   z.write(source, source.relative_to(ROOT))
with zipfile.ZipFile(a.destination) as z:
 if z.testzip() is not None:
  raise SystemExit('ZIP verification failed')
print(a.destination)
print(f'{a.destination.stat().st_size} bytes')
