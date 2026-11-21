from pathlib import Path
from datetime import datetime,timezone
import json,sys,shutil,subprocess
ROOT=Path(__file__).resolve().parents[1]
n=int(sys.argv[1]);p=f'149_scan{n:03d}'
source=ROOT/'review'/f'{p}.json';data=json.loads(source.read_text())
if data.get('root_reviewed') is not True:raise SystemExit('Root visual adjudication is not marked complete.')
if (ROOT/'review/accepted'/f'{p}.json').exists():raise SystemExit('Already accepted; use explicit revision instead.')
shutil.copyfile(ROOT/'review'/f'{p}.tex',ROOT/'pages'/f'{p}.tex')
(ROOT/'review/accepted'/f'{p}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
crops=set(data['inspection'].get('crops',[]))
rows=[r for r in data['changes'] if r.get('vs_C') or r.get('vs_H')]
with (ROOT/'progress.log').open('a') as f:f.write(f'scan {n:03d} done {now} cote 149: {data["line_count"]} lines read, {len(crops)} places cropped, {len(rows)} rows\n')
subprocess.run([sys.executable,str(ROOT/'scripts/assemble.py')],check=True)
