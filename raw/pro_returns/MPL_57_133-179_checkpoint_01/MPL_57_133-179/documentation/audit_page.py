"""Record a completed personal second visual comparison, never an automated audit."""
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
def audit(scan, finding):
    stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'scan {scan:03} audited {stamp}\n')
    with (ROOT/'documentation'/'second_audit.md').open('a') as f:
        f.write(f'- {scan}: {finding}\n')
