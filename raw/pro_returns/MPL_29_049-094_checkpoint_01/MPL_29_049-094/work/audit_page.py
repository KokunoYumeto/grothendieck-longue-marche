#!/usr/bin/env python3
"""Record the root reader's completed image audit; never performs image/OCR analysis."""
from pathlib import Path
import datetime,json,csv
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_29_049-094'
def now(): return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def audit(scan, changes=(), doubts=(), note='Compared whole and both half images with saved transcription.'):
    p=ROOT/'pages'/f'{PREFIX}_29_scan{scan:03}.tex'
    t=p.read_text()
    for a,b in changes:
        if a not in t: raise ValueError(f'scan {scan}: old string absent: {a!r}')
        t=t.replace(a,b)
    p.write_text(t)
    with (ROOT/'work'/'audit_records.jsonl').open('a') as f:
        f.write(json.dumps({'scan':scan,'time':now(),'changes':len(changes),'note':note},ensure_ascii=False)+'\n')
    with (ROOT/'work'/'doubts_records.jsonl').open('a') as f:
        for d in doubts: f.write(json.dumps({'scan':scan,**d},ensure_ascii=False)+'\n')
    with (ROOT/'progress.log').open('a') as f: f.write(f'scan {scan:03} audited {now()}\n')
    rebuild()
    print(f'Audited scan {scan:03}; {len(changes)} explicit replacements')
def rebuild():
    (ROOT/f'{PREFIX}_transcription.tex').write_text('\n'.join(p.read_text().rstrip()+'\n' for p in sorted((ROOT/'pages').glob('*.tex'))))
