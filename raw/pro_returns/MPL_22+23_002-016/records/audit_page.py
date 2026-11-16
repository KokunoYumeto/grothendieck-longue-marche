from pathlib import Path
from datetime import datetime, timezone
import sys
r=Path(__file__).resolve().parents[1]
c,s=int(sys.argv[1]),int(sys.argv[2])
p=r/'progress.log'
prefix=f'{c} scan {s:03d} audited '
assert prefix not in p.read_text(), 'audit already logged'
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with p.open('a') as f:
 f.write(prefix+now+'\n')
 if len(sys.argv)>3:f.write(f'audit observation {c} scan {s:03d}: '+sys.argv[3]+'\n')
print(prefix+now)
