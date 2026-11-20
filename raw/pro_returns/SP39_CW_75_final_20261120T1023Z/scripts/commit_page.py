#!/usr/bin/env python3
"""Commit one fully adjudicated page in the required scan order."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys

root=Path(__file__).resolve().parents[1]
scan=int(sys.argv[1]);order=[26,27,28,30,31,32,33]
statepath=root/'run_state.json';state=json.loads(statepath.read_text())
assert state['completed_scans']==order[:order.index(scan)],'Pages must be committed in order, once.'
page=root/f'pages/J75-04_75_scan{scan:03}.tex'
decision=root/f'decisions/scan{scan:03}.json'
assert page.exists() and decision.exists()
rec=json.loads(decision.read_text())
assert rec['scan']==scan and rec['inventory'] and rec['notes']
assert all(x['transcribed']=='yes' for x in rec['inventory'])
for reader in 'ABC':
    d=root/f'readers/scan{scan:03}/{reader}'
    for name in ['page.tex','report.md','review.json']:assert (d/name).exists(),f'{d/name} missing'
subprocess.run([sys.executable,str(root/'scripts/build_records.py')],check=True)
state['completed_scans'].append(scan)
statepath.write_text(json.dumps(state,indent=2)+'\n')
(root/'SP39_CW_75_transcription.tex').write_text('\n'.join((root/f'pages/J75-04_75_scan{s:03}.tex').read_text().rstrip() for s in state['completed_scans'])+'\n')
with (root/'progress.log').open('a') as f:
    f.write(f'scan {scan:03} done '+datetime.now(timezone.utc).isoformat(timespec='seconds')+'\n')
print(f'Scan {scan:03} committed with changes, collation, inventory, doubts, notes and check events.')
