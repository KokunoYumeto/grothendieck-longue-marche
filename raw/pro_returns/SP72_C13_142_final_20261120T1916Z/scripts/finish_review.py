from pathlib import Path
from datetime import datetime,timezone
import json,sys,shutil,subprocess

out=Path(__file__).resolve().parents[1]
n=int(sys.argv[1]);folder=out/'documentation/reviews'/f'scan{n:03}'
r=json.loads((folder/'report.json').read_text())
assert r.get('main_review_complete') is True
assert r.get('inventory_review_complete') is True
shutil.copyfile(folder/'page.tex',out/'pages'/f'142_scan{n:03}.tex')
(out/'documentation/decided'/f'scan{n:03}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
subprocess.run([sys.executable,str(out/'scripts/build_deliverables.py')],check=True)
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (out/'progress.log').open('a') as f:f.write(f'scan {n:03} done {stamp} cote 142\n')
print(f'scan {n:03} done {stamp}')
