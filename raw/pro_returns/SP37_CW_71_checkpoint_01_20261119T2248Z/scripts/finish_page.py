#!/usr/bin/env python3
"""Commit an already adjudicated page's records before advancing to the next scan."""
from pathlib import Path
from datetime import datetime,timezone
import json,sys,subprocess
root=Path(__file__).resolve().parents[1];n=int(sys.argv[1])
p=root/f'decisions/scan{n:03d}.json';record=json.loads(p.read_text())
assert record['scan']==n
if n>36:assert (root/f'decisions/scan{n-1:03d}.json').exists(),'Previous scan is not decided'
for who in ['R1','R2','R3']:
    d=root/f'readers/scan{n:03d}/{who}'
    assert (d/'reading.tex').is_file() and (d/'report.json').is_file(),f'Missing {who} return'
    report=json.loads((d/'report.json').read_text())
    assert report.get('inventory'),f'{who} inventory not finished'
assert (root/'pages'/record['page_file']).is_file()
assert all(x['transcribed']=='yes' for x in record['inventory'])
assert all(x['sheet_kind'] in ['text','reused_typed','typescript','letter','list','cancelled_draft','cover'] for x in record['inventory'])
subprocess.run([sys.executable,str(root/'scripts/build_outputs.py')],check=True)
log=(root/'progress.log').read_text()
if f'scan {n:03d} done ' not in log:
    with (root/'progress.log').open('a') as f:f.write(f'scan {n:03d} done '+datetime.now(timezone.utc).isoformat()+'\n')
if record.get('workflow_entry'):
    with (root/'SP37_CW_71_workflow.md').open('a') as f:f.write(f'\n### Scan {n:03d}\n\n'+record['workflow_entry']+'\n')
if n<48:
    (root/f'briefs/notation_scan{n+1:03d}.md').write_text((root/'notation.md').read_text())
    for who in ['R1','R2','R3']:(root/f'readers/scan{n+1:03d}/{who}').mkdir(parents=True,exist_ok=True)
print(f'Scan {n:03d} committed before the next page')
