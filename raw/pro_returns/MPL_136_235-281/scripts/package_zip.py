"""Create an immutable hourly checkpoint or the final deliverable, excluding sources."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import zipfile

ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument('--checkpoint', type=int)
p.add_argument('--final', action='store_true')
a = p.parse_args()
assert bool(a.checkpoint) != bool(a.final)
name = f'MPL_136_235-281_checkpoint_{a.checkpoint:02d}.zip' if a.checkpoint else 'MPL_136_235-281.zip'
dest = ROOT.parent / name
assert not dest.exists(), 'Never overwrite an existing archive'
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT / 'progress.log').open('a') as f:
    f.write(f'{"hourly checkpoint" if a.checkpoint else "final archive"} {name} assembled {now}\n')
paths = [q for q in sorted(ROOT.rglob('*')) if q.is_file() and '__pycache__' not in q.parts and q.suffix not in ('.zip', '.pyc')]
with zipfile.ZipFile(dest, 'x', zipfile.ZIP_DEFLATED) as z:
    for q in paths:
        z.write(q, q.relative_to(ROOT))
with zipfile.ZipFile(dest) as z:
    assert z.testzip() is None
print(f'{dest}: {len(paths)} files, {dest.stat().st_size} bytes')
