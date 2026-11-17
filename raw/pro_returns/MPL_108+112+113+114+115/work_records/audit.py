from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
def audited(cote,scan,comment='Compared text and inventory against scan; no change.'):
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'{cote} scan {scan:03} audited {now}\n')
    with (ROOT/'work_records/audit_notes.md').open('a',encoding='utf-8') as f:
        f.write(f'- {cote} scan {scan:03}, {now}: {comment}\n')
    print(f'Audited {cote} scan {scan:03}')
def doubt(cote,scan,line,reading,alternatives,confidence):
    vals=[str(cote),f'{scan:03}',line,reading,alternatives,confidence]
    with (ROOT/'work_records/doubts_rows.md').open('a',encoding='utf-8') as f:
        f.write('| '+' | '.join(v.replace('|',' / ') for v in vals)+' |\n')
