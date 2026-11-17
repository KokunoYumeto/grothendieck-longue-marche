from pathlib import Path
from datetime import datetime, timezone
import sys

root = Path(__file__).resolve().parents[1]
scan = int(sys.argv[1])
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root / 'progress.log').open('a', encoding='utf-8') as handle:
    handle.write(f'12 scan {scan:03} audited {stamp}\n')
if len(sys.argv) > 2:
    with (root / 'audit_notes.md').open('a', encoding='utf-8') as handle:
        handle.write(f'- 12/{scan:03}: {sys.argv[2]}\n')
print(f'Audit recorded: 12/{scan:03}')
