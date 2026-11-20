"""Write derived records and mark an already adjudicated page done. No reading is automated."""
from pathlib import Path
import json,sys,subprocess,datetime
O=Path(__file__).resolve().parents[1];key=sys.argv[1]
d=json.loads((O/'decisions'/f'{key}.json').read_text())
for r in ['R1','R2','R3']:
 for f in ['reading.tex','report.json']:
  if not (O/'readers'/key/r/f).exists():raise SystemExit(f'Missing {r}/{f}')
subprocess.run([sys.executable,str(O/'scripts/build_deliverables.py')],check=True)
subprocess.run([sys.executable,str(O/'scripts/validate.py')],check=True)
v=json.loads((O/'validation.json').read_text())
if v['errors']:raise SystemExit('Validation errors must be addressed before marking page done')
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
needle=f"scan {d['scan']:03d} done "
log=O/'progress.log';old=log.read_text()
if any(x.startswith(needle) and f"cote {d['cote']}" in x for x in old.splitlines()):raise SystemExit('Page already marked done; no duplicate line written')
with log.open('a') as f:f.write(f"{needle}{now} cote {d['cote']}\n")
print(f"{key} saved and marked done {now}")
