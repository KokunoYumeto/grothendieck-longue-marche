from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_66+68_002-032'
def audit(n,changes=(),note=''):
 p=ROOT/'pages'/f'{PREFIX}_68_scan{n:03d}.tex'
 s=p.read_text()
 applied=[]
 for old,new in changes:
  if old not in s: raise ValueError(f'Not found on {n}: {old}')
  s=s.replace(old,new)
  applied.append((old,new))
 if applied:p.write_text(s)
 stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 with (ROOT/'records'/'audit_observations.md').open('a') as f:
  f.write(f'\n## 68/{n:03d} — {stamp}\n\nSecond visual reading against supplied images. {note}\n')
  for old,new in applied:f.write(f'\n- Replaced `{old}` with `{new}`.\n')
 with (ROOT/'progress.log').open('a') as f:f.write(f'scan {n:03d} audited {stamp}\n')
 print(f'Audited {n:03d}: {len(applied)} changes')
