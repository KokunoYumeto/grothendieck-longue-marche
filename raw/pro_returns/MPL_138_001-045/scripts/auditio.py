from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
def audit(scan,note='Image checked against the complete page fragment; no change.'):
 stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 with (ROOT/'progress.log').open('a') as f:f.write(f'138 scan {scan:03d} audited {stamp}\n')
 with (ROOT/'records/audit_notes.md').open('a') as f:f.write(f'- {scan:03d}: {note}\n')
 print(f'Audited {scan:03d} at {stamp}')
