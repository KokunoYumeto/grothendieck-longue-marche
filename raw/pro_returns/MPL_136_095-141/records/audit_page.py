from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
def audit(scan,note):
 now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 log=ROOT/'progress.log'
 if f'scan {scan:03} audited ' in log.read_text():raise ValueError('Already audited')
 with log.open('a') as f:f.write(f'scan {scan:03} audited {now}\n')
 with (ROOT/'records/audit_notes.md').open('a') as f:f.write(f'\n## Scan {scan:03}\n\n{note}\n')
 print(f'scan {scan:03} audited {now}')
