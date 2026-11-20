"""Log one actually delivered and inspected local image; never call before viewing."""
from pathlib import Path
from datetime import datetime, timezone
import json, sys

OUT = Path('/workspace/scratch/42e661864e98/out')
n = int(sys.argv[1]); rel = sys.argv[2]; note = sys.argv[3]
p = OUT / rel
assert p.exists() and p.suffix.lower() in ('.jpg', '.jpeg', '.png')
assert f'scan{n:03}' in rel and '..' not in Path(rel).parts
dest = OUT / f'decisions/scan{n:03}_main_views.json'
views = json.loads(dest.read_text()) if dest.exists() else []
assert str(p) not in views, 'Do not log or re-view an already inspected crop'
views.append(str(p))
dest.write_text(json.dumps(views, indent=2) + '\n')
notes = OUT / f'working/scan{n:03}_main_crop_notes.md'
if not notes.exists(): notes.write_text(f'# Main crop adjudication: scan {n:03}\n\n')
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with notes.open('a') as f:
    f.write(f'## {len(views):02} — {rel}\n\nRecorded {stamp}. {note}\n\n')
print(f'Logged scan {n:03} main view {len(views)}: {rel}')
