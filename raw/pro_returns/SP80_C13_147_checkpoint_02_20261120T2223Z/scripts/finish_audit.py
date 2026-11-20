"""Record a completed, root-adjudicated blind reading; never modify its baseline."""
from pathlib import Path
import csv, hashlib, json, subprocess, sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
scan = int(sys.argv[1]); stem=f'147_scan{scan}'
def read(suffix):
    with (ROOT/'second'/f'{stem}_{suffix}.tsv').open() as f:
        return list(csv.DictReader(f,delimiter='\t'))
comparison=read('comparison'); adjudications=read('adjudications')
different={r['box'] for r in comparison if r['equal']=='no'}
adjudicated={r['box'] for r in adjudications}
assert different<=adjudicated, f'Unadjudicated boxes: {different-adjudicated}'
assert len(adjudicated)==len(adjudications), 'Duplicate adjudication box.'
assert adjudicated<={r['box'] for r in comparison}
for row in adjudications:
    assert row['evidence'].strip() and row['final'].strip()
    assert row['changed'] in ('yes','no')
    assert (ROOT/row['crop']).is_file()
snapshot=json.loads((ROOT/'second/first_readings_frozen.json').read_text())
assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in snapshot['sha256'].items())
comparison_meta=json.loads((ROOT/'second'/f'{stem}_comparison_meta.json').read_text())
assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in comparison_meta['sha256'].items()), 'A recorded reading changed after token comparison.'
when=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
log=ROOT/'progress.log'
assert f'scan {scan:03d} audited ' not in log.read_text(), 'Audit already logged.'
report_path=ROOT/'review'/f'{stem}_reviewed.json'
report=json.loads(report_path.read_text())
report['audit_completed_at']=when
report['audit_counts']={'boxes':len(comparison),'differences':len(different),'changed':sum(r['changed']=='yes' for r in adjudications)}
report['audit_changes']=[{k:r.get(k,'') for k in ('box','first','second','final','evidence')} for r in adjudications if r['changed']=='yes']
report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
subprocess.run([sys.executable,str(ROOT/'scripts/assemble.py')],check=True)
with log.open('a') as f:
    f.write(f'scan {scan:03d} audited {when}: {len(comparison)} boxes read, {len(different)} differences, {report["audit_counts"]["changed"]} changed\n')
print(json.dumps(report['audit_counts']))
