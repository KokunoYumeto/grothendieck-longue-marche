from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
def audit(scan, note):
 t=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03} audited {t}\n')
 with (ROOT/'audit_changes.md').open('a') as f:f.write(f'\n## Scan {scan:03} — {t}\n\n{note}\n')
 print(f'scan {scan:03} audited {t}')
if __name__=='__main__':
 import sys
 audit(int(sys.argv[1]),sys.argv[2])
