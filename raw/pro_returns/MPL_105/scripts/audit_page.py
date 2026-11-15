from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
def audit_page(scan,replacements=(),note='Visual comparison completed.'):
 p=ROOT/'pages'/f'MPL_105_105_scan{scan:03d}.tex'
 s=p.read_text()
 for old,new in replacements:
  if old not in s: raise ValueError((scan,'not found',old))
  s=s.replace(old,new)
 p.write_text(s)
 with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03d} audited '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
 with (ROOT/'records'/'visual_audit.md').open('a') as f:f.write(f'\n- Scan {scan:03d}: {note}\n')
