from pathlib import Path
from datetime import datetime, timezone
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
def audit(scan,replacements=(),note='Second visual reading against the whole image and full-resolution details.'):
    p=ROOT/'pages'/f'MPL_154_077-126_154_scan{scan:03d}.tex'
    s=p.read_text(); changes=[]
    for a,b in replacements:
        if a not in s: raise ValueError(f'Missing target scan {scan}: {a[:100]}')
        s=s.replace(a,b);changes.append({'before':a,'after':b})
    if r'\mspage{' in s:
        s=s.replace(r'\mspage{',r'\margin{');changes.append({'before':'\\mspage{','after':'\\margin{','reason':'Number visible; authorial attribution unestablished.'})
    p.write_text(s)
    t=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT/'records/audit_changes.jsonl').open('a') as f:f.write(json.dumps({'scan':scan,'utc':t,'note':note,'changes':changes},ensure_ascii=False)+'\n')
    with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03d} audited {t}\n')
    print(f'Audited {scan:03d}; {len(changes)} changes')
