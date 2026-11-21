"""Record a completed visual adjudication; never decides a reading itself."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
n = int(sys.argv[1])
stem = f'149_scan{n:03d}'
comparison = json.loads((ROOT/'second'/f'{stem}_comparison.json').read_text())
adjudications = json.loads((ROOT/'second'/f'{stem}_adjudications.json').read_text())
required = [r['box'] for r in comparison if r['different']]
if [r['box'] for r in adjudications] != required:
    raise SystemExit('Every token difference must have one root adjudication, in box order.')
for r in adjudications:
    if not r.get('root_visually_inspected') or not r.get('evidence') or not r.get('final'):
        raise SystemExit(f'Incomplete visual adjudication: {r["box"]}')
    if not (ROOT/r['crop']).exists():
        raise SystemExit(f'Missing adjudication crop: {r["crop"]}')
accepted = ROOT/'review/accepted'/f'{stem}.json'
data = json.loads(accepted.read_text())
if data.get('audited'):
    raise SystemExit('Audit already recorded; do not duplicate its progress entry.')
by_box = {r['box']: r for r in comparison}
changes = []
for r in adjudications:
    if r.get('changed'):
        row = dict(r)
        row['first'] = by_box[r['box']]['first']
        row['second'] = by_box[r['box']]['second']
        changes.append(row)
data['audit_changes'] = changes
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
data['audited'] = {'utc': now, 'boxes': len(comparison), 'differences': len(required), 'changed': len(changes)}
accepted.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
with (ROOT/'progress.log').open('a') as f:
    f.write(f'scan {n:03d} audited {now}: {len(comparison)} boxes read, {len(required)} differences, {len(changes)} changed\n')
subprocess.run([sys.executable, str(ROOT/'scripts/assemble.py')], check=True)
