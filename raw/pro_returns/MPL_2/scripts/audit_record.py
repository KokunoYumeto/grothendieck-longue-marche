"""Log primary-reader visual audits; never performs or infers an image reading."""
from pathlib import Path
from datetime import datetime, timezone
ROOT = Path(__file__).resolve().parents[1]
def audit(scan, note, doubts=()):
    stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'scan {scan:03d} audited {stamp}\n')
    with (ROOT/'records'/'visual_audit.md').open('a',encoding='utf-8') as f:
        f.write(f'\n## Scan {scan:03d}\n\n{stamp}. {note}\n')
    with (ROOT/'MPL_2_doubts.md').open('a',encoding='utf-8') as f:
        for line,reading,alternatives,confidence in doubts:
            vals=[2,scan,line,reading,alternatives,confidence]
            f.write('| '+' | '.join(str(x).replace('|',' / ') for x in vals)+' |\n')
    print(f'Audited {scan:03d}')
