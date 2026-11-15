from pathlib import Path
from datetime import datetime,timezone
import sys
root=Path(__file__).resolve().parents[1]
cote,scan=map(int,sys.argv[1:3])
with (root/'progress.log').open('a') as f:
 f.write(f'{cote} scan {scan:03} audited '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
 if len(sys.argv)>3:f.write('  Audit: '+sys.argv[3]+'\n')
