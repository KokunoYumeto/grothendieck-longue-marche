"""Commit an adjudicated second reading and rebuild its apparatus."""
from pathlib import Path
from datetime import datetime, timezone
import json, sys, shutil, subprocess, csv, re

out = Path(__file__).resolve().parents[1]
n = int(sys.argv[1])
assert len(list((out/'documentation/decided').glob('scan*.json'))) == 24
folder = out/'documentation/reviews'/f'scan{n:03}'
r = json.loads((folder/'report.json').read_text())
assert r.get('audit_complete') is True
assert r.get('audit_review_complete') is True
with (out/'documentation/assignments.tsv').open() as f:
    assignments={int(row['scan']):row for row in csv.DictReader(f,delimiter='\t')}
assert assignments[n]['first_reader'] != re.search(r'reader_[abc]',r['audit_reader'])[0]
assert r.get('main_review_complete') and r.get('inventory_review_complete')
audit = json.loads((out/'audit'/f'scan{n:03}'/'report.json').read_text())
assert audit['complete_page_read'] and audit['inventory_checked']
assert audit['full_page_seen'] and set(audit['halves_seen']) == {'top', 'bottom'}
assert r.get('audit_adjudication'), 'Record the main reader\'s adjudication, including a no-change audit.'
assert f'scan {n:03} audited ' not in (out/'progress.log').read_text(), 'Audit was already committed.'
assignments[n]['audit_reader'] = re.search(r'reader_[abc]',r['audit_reader'])[0]
with (out/'documentation/assignments.tsv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['scan','first_reader','audit_reader'], delimiter='\t')
    writer.writeheader()
    for key in sorted(assignments):
        assignments[key]['scan'] = f'{key:03}'
        writer.writerow(assignments[key])
shutil.copyfile(folder/'page.tex', out/'pages'/f'142_scan{n:03}.tex')
(out/'documentation/decided'/f'scan{n:03}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2))
subprocess.run([sys.executable, str(out/'scripts/build_deliverables.py')], check=True)
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (out/'progress.log').open('a') as f:
    f.write(f'scan {n:03} audited {stamp}\n')
print(f'scan {n:03} audited {stamp}')
