from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
def audit(n,note='Checked against the image; existing uncertainty marks retained.'):
    stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    p=ROOT/'progress.log'
    if f'scan {n:03d} audited ' in p.read_text():raise ValueError('Already audited')
    with (ROOT/'records/audit_notes.md').open('a') as f:f.write(f'\n## Scan {n:03d} — {stamp}\n\n{note}\n')
    with p.open('a') as f:f.write(f'scan {n:03d} audited {stamp}\n')
if __name__=='__main__':
    import sys
    audit(int(sys.argv[1]),sys.argv[2] if len(sys.argv)>2 else 'Checked against the image; existing uncertainty marks retained.')
