from pathlib import Path
from datetime import datetime, timezone
import sys
from record_page import rebuild_doubts

root = Path(__file__).resolve().parents[1]
scan = int(sys.argv[1])
note = sys.argv[2] if len(sys.argv) > 2 else 'Re-read the whole image and both halves against the page file; no change.'
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
assert (root/'pages'/f'MPL_58_020-067_58_scan{scan:03d}.tex').exists()
assert not (root/'records'/'frozen_sha256.json').exists()
with (root/'progress.log').open('a', encoding='utf-8') as f:
    f.write(f'scan {scan:03d} audited {stamp}\n')
with (root/'records'/'visual_audit.md').open('a', encoding='utf-8') as f:
    f.write(f'- Scan {scan:03d} — {stamp}: {note}\n')
rebuild_doubts()
print(f'Audit recorded for scan {scan:03d}')
