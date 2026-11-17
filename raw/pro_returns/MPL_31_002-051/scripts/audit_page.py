from pathlib import Path
from save_page import BASE, utc, rebuild

def audit(scan, note):
    log=BASE/'progress.log'
    if 'context opened ' in log.read_text():
        raise RuntimeError('Transcription is frozen; audit edits are prohibited')
    if f'scan {scan:03d} audited ' in log.read_text():
        raise RuntimeError('This page already has its second-audit completion entry')
    rebuild()
    with (BASE/'records/second_audit.md').open('a',encoding='utf-8') as f:
        f.write(f'\n## Scan {scan:03d}\n\n{note}\n')
    with log.open('a',encoding='utf-8') as f:
        f.write(f'scan {scan:03d} audited {utc()}\n')
    print(f'Audited scan {scan:03d}')
