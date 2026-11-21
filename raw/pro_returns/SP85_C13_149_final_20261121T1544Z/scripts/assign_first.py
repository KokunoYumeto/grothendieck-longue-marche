"""Record the next first-reading page after that reader's prior page is committed.

Assignment itself is sent separately by the main reader. This script does not
read images, choose readings, or start an agent.
"""
from pathlib import Path
import json, sys, subprocess, datetime

ROOT = Path(__file__).resolve().parents[1]
page, agent = sys.argv[1:3]
path = ROOT / 'records/assignments.json'
assignments = json.loads(path.read_text())
state = json.loads((ROOT / 'records/next_steps.json').read_text())
order = [f'149_scan{n:03}' for n in state['page_order']]
remaining = [p for p in order if p not in assignments['first']]
assert remaining and page == remaining[0], 'Assign the next page in order'
prior = [p for p, a in assignments['first'].items() if a == agent]
assert all((ROOT / 'records' / f'{p}.json').is_file() for p in prior), 'Prior page must be committed first'
assignments['first'][page] = agent
path.write_text(json.dumps(assignments, indent=2) + '\n')
subprocess.run([sys.executable, str(ROOT / 'scripts/build_records.py')], check=True)
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT / 'progress.log').open('a') as f:
    f.write(f'{page} first reading assigned {now}: {agent}\n')
print(page, agent, 'assigned')
