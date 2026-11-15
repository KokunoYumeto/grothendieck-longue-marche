from pathlib import Path
from page_io import ROOT,now,rebuild

def audit(scan,observations):
    log=ROOT/'progress.log'
    if f'scan {scan:03} audited ' in log.read_text():
        raise RuntimeError('Already audited')
    rebuild()
    with (ROOT/'records/visual_audit.md').open('a',encoding='utf-8') as f:
        f.write(f'\n## Scan {scan:03} — {now()}\n\n{observations}\n')
    with log.open('a',encoding='utf-8') as f:
        f.write(f'scan {scan:03} audited {now()}\n')
    print(f'scan {scan:03} audited {now()}')
