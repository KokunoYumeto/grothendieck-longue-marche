from pathlib import Path
import sys,json
from record_page import ROOT,now,refresh

def audit(scan, replacements=(), note='Visual reread of whole page and both halves; no further change.'):
    log=ROOT/'progress.log'
    assert 'transcription frozen' not in log.read_text()
    assert f'scan {scan:03} audited ' not in log.read_text()
    p=ROOT/'pages'/f'MPL_91_019-058_91_scan{scan:03}.tex'
    s=p.read_text()
    for old,new in replacements:
        assert old in s, (scan,old)
        s=s.replace(old,new)
    p.write_text(s)
    with (ROOT/'audit_changes.md').open('a') as f:f.write(f'\n## Scan {scan:03}\n\n{note}\n')
    with log.open('a') as f:f.write(f'scan {scan:03} audited {now()}\n')
    refresh()
    print(f'Audited {scan:03}; {len(replacements)} replacement rules.')
