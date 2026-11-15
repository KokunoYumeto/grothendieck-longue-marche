"""Record a visual audit only after the transcriber has completed it."""
from pathlib import Path
from datetime import datetime, timezone
import sys

ROOT = Path(__file__).resolve().parents[1]

def record(scan, note="Checked whole page and both halves; no change."):
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT / 'progress.log').open('a', encoding='utf-8') as stream:
        stream.write(f'scan {scan:03d} audited {stamp}\n')
    with (ROOT / 'records' / 'audit_changes.md').open('a', encoding='utf-8') as stream:
        stream.write(f'## Scan {scan:03d}\n\n{note}\n\n')

if __name__ == '__main__':
    record(int(sys.argv[1]), sys.argv[2] if len(sys.argv) > 2 else "Checked whole page and both halves; no change.")
