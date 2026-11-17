from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def audit(scan, note):
    log=ROOT/'progress.log'
    marker=f'scan {scan:03d} audited '
    if marker in log.read_text(): raise RuntimeError('Already audited')
    with (ROOT/'records/visual_audit.md').open('a',encoding='utf-8') as f:
        f.write(f'\n## Scan {scan:03d}\n\n{note}\n')
    with log.open('a') as f: f.write(f'{marker}{utc()}\n')
    print(f'Audited {scan:03d}')
if __name__=='__main__':
    import sys
    audit(int(sys.argv[1]),sys.argv[2])
