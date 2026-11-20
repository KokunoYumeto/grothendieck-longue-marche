"""Commit a completed, image-adjudicated blind reading. Never chooses readings."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, subprocess, sys

W = Path(__file__).resolve().parents[1]
page = sys.argv[1]
def read(suffix):
    with (W/'second'/f'{page}_{suffix}.tsv').open() as f:
        return list(csv.DictReader(f, delimiter='\t'))

order = (W/'page_order.txt').read_text().splitlines()
if any(not json.loads((W/'reports'/f'{p}.json').read_text()).get('adjudicated') for p in order):
    raise SystemExit('All first readings must be committed before auditing.')
assignments = json.loads((W/'reports/assignments.json').read_text())
if assignments['first'][page] == assignments['second'][page]:
    raise SystemExit('Second reader must be different from first reader.')
comparison = read('comparison')
decisions = read('adjudications')
needed = {x['box'] for x in comparison if x['exact_token_match']=='no'}
if len({x['box'] for x in decisions}) != len(decisions):
    raise SystemExit('Duplicate adjudication.')
if {x['box'] for x in decisions} != needed:
    raise SystemExit('Every token mismatch, and only a mismatch, needs adjudication.')
cm = {x['box']: x for x in comparison}
for d in decisions:
    if d.get('changed') not in ('yes','no') or not d.get('evidence') or not d.get('final_reading'):
        raise SystemExit('Incomplete root decision: '+d['box'])
    if d.get('confidence') not in ('high','medium','low'):
        raise SystemExit('Invalid confidence: '+d['box'])
    if not (W/d['crop']).is_file():
        raise SystemExit('Missing adjudicated crop: '+d['box'])
    d['first_reading'] = cm[d['box']]['first_reading']
    d['second_reading'] = cm[d['box']]['second_reading']
rp = W/'reports'/f'{page}.json'
r = json.loads(rp.read_text())
if r.get('audited'):
    raise SystemExit('Audit already committed.')
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
r['audited'] = True
r['audit'] = {'date':now, 'reader':assignments['second'][page], 'boxes':len(comparison),
              'differences':len(needed), 'changed':sum(d['changed']=='yes' for d in decisions),
              'adjudications':decisions}
rp.write_text(json.dumps(r, ensure_ascii=False, indent=2)+'\n')
subprocess.run([sys.executable,str(W/'scripts/build_outputs.py')],check=True)
with (W/'progress.log').open('a') as f:
    f.write(f"scan {int(r['scan']):03d} audited {now}: {len(comparison)} boxes read, {len(needed)} differences, {r['audit']['changed']} changed\n")
print(page, 'audited', r['audit']['changed'], 'places changed')
