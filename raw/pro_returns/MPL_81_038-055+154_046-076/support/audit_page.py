from pathlib import Path
from datetime import datetime,timezone
import argparse,subprocess,sys
p=argparse.ArgumentParser();p.add_argument('scan',type=int);p.add_argument('--note',required=True);a=p.parse_args()
r=Path('/workspace/scratch/89f8415d3ab0');stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
subprocess.run([sys.executable,str(r/'support/record_page.py'),str(a.scan),'--inventory-only'],check=True)
with (r/'deliver/progress.log').open('a') as f:f.write(f'scan {a.scan:03d} audited {stamp}\n')
with (r/'deliver/records/second_audit.md').open('a') as f:f.write(f'\n## Cote 154, scan {a.scan:03d} — {stamp}\n\n{a.note}\n')
