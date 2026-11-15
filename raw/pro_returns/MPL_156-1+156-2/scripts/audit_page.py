from pathlib import Path
from datetime import datetime, timezone
import sys

root = Path(__file__).resolve().parents[1]
cote, scan = sys.argv[1], int(sys.argv[2])
comment = sys.argv[3] if len(sys.argv) > 3 else 'Second visual comparison completed.'
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f:
    f.write(f'{cote} scan {scan:03d} audited {stamp}\n')
with (root/'records'/'audit_notes.md').open('a') as f:
    f.write(f'\n## {cote} scan {scan:03d} — {stamp}\n\n{comment}\n')
print(f'Audited {cote} scan {scan:03d}.')
