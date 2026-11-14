from pathlib import Path
from datetime import datetime, timezone
import sys
root=Path(__file__).resolve().parents[1]
cote,scan=sys.argv[1:3]
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f:
    f.write(f'{cote} scan {int(scan):03} audited {stamp}\n')
if len(sys.argv)>3:
    with (root/'audit_observations.md').open('a') as f:
        f.write(f'\n## {cote} scan {int(scan):03}\n\n'+sys.argv[3]+'\n')
