"""Record a completed manual second visual audit; never reads images or OCR."""
from pathlib import Path
from datetime import datetime,timezone
import json
ROOT=Path(__file__).resolve().parent
def audit(scan,changes=(),doubts=(),note=''):
    page=ROOT/'pages'/f'MPL_129_077-115_129_scan{scan:03d}.tex'
    tex=page.read_text()
    for old,new in changes:
        if old not in tex: raise ValueError((scan,'replacement not found',old))
        tex=tex.replace(old,new)
    if changes:page.write_text(tex,encoding='utf-8')
    if doubts:
        records=[json.loads(x) for x in (ROOT/'reading_records.jsonl').read_text().splitlines()]
        row=next(r for r in records if r['scan']==scan)
        row['doubts'].extend(doubts)
        (ROOT/'reading_records.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records),encoding='utf-8')
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT/'audit_records.jsonl').open('a') as f:f.write(json.dumps({'scan':scan,'time':now,'changes':list(changes),'note':note},ensure_ascii=False)+'\n')
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'scan {scan:03d} audited {now}\n')
        if note:f.write(f'audit note {scan:03d}: {note}\n')
    print(f'Audited {scan:03d}, {len(changes)} textual corrections, {len(doubts)} added doubt rows.')
