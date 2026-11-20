"""Finalize an already-adjudicated page, assemble its apparatus, then record completion."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,subprocess
W=Path(__file__).resolve().parents[1];n=int(sys.argv[1])
record_path=W/'records'/f'scan{n:03}.json'
record=json.loads(record_path.read_text())
page=W/'pages'/record['filename']
if not page.exists():raise SystemExit('Missing final page')
for reader in 'ABC':
    d=W/'readers'/f'{n:03}'/reader
    if not all((d/f).exists() for f in ['reading.tex','report.json']):raise SystemExit('Missing reader '+reader)
state=json.loads((W/'state.json').read_text())
order=[int(r['our_scan']) for r in json.loads((W/'page_map.json').read_text())]
if n in state['done']:raise SystemExit('Already committed; use an explicit logged correction')
if order[len(state['done'])]!=n:raise SystemExit('Out-of-order page')
subprocess.run([sys.executable,str(W/'scripts/build.py')],check=True)
subprocess.run([sys.executable,str(W/'scripts/validate.py')],check=True)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (W/'progress.log').open('a') as f:f.write(f'scan {n:03} done {now}\n')
state['done'].append(n);(W/'state.json').write_text(json.dumps(state,indent=2))
print('Committed scan',n,now)
