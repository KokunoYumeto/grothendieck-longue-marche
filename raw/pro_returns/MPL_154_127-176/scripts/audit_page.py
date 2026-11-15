from pathlib import Path
from datetime import datetime,timezone
import hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
def audit(scan,remarks):
 p=ROOT/'pages'/f'MPL_154_127-176_154_scan{scan:03}.tex'
 now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03} audited {now}\n')
 with (ROOT/'records/visual_audit.md').open('a') as f:f.write(f'\n## Scan {scan} — {now}\n\n{remarks}\n\nSHA-256 after audit: `{hashlib.sha256(p.read_bytes()).hexdigest()}`.\n')
 print(f'scan {scan} audited')
if __name__=='__main__':audit(int(sys.argv[1]),sys.argv[2])
