from pathlib import Path
from datetime import datetime, timezone
import sys

root = Path(__file__).resolve().parents[1]
scan = int(sys.argv[1])
note = sys.argv[2]
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
log = root/'progress.log'
prefix = f'scan {scan:03} audited '
if prefix in log.read_text():
    raise RuntimeError('Audit already recorded; use an explicit supplementary record.')
with (root/'records/visual_audit.md').open('a', encoding='utf-8') as f:
    f.write(f'## Scan {scan} — {now}\n\n{note}\n\n')
with log.open('a', encoding='utf-8') as f:
    f.write(prefix+now+'\n')
print(f'Audit recorded for {scan}.')
