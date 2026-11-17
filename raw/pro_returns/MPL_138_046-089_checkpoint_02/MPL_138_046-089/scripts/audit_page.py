from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
def audit(scan, replacements=(), note='Visual comparison completed; retained readings and marked doubts.'):
    p=ROOT/'pages'/f'MPL_138_046-089_138_scan{scan:03}.tex'
    s=p.read_text()
    for old,new in replacements:
        if old not in s: raise ValueError((scan,old))
        s=s.replace(old,new)
    p.write_text(s)
    stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT/'audit_notes.md').open('a') as f:f.write(f'## Scan {scan:03}\n\n{note}\n\n')
    with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03} audited {stamp}\n')
    print(f'scan {scan:03} audited {stamp}')
