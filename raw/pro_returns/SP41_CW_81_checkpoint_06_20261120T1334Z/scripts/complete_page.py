"""Finish a root-adjudicated page after its ink decisions are saved.
This only rebuilds and checks records; it does not infer readings or certify proof.
"""
from pathlib import Path
import json,sys,subprocess,datetime
w=Path(__file__).resolve().parents[1]
n=int(sys.argv[1]);p=w/f'decisions/scan{n:03d}.json'
d=json.loads(p.read_text())
assert d['status']=='decided'
for k in (1,2,3):
    for name in ('reading.tex','return.json'):
        assert (w/f'readers/scan{n:03d}/R{k}'/name).exists(),(k,name)
for script in ('order_inventory.py','build_apparatus.py','validate_tex.py','validate_records.py'):
    subprocess.run([sys.executable,str(w/'scripts'/script)],check=True)
assert json.loads((w/'validation/tex_balance.json').read_text())['all_balanced']
assert json.loads((w/'validation/record_validation.json').read_text())['all_valid']
line=f'scan {n:03d} done '
log=w/'progress.log'
assert line not in log.read_text(), 'Already completed; do not append twice.'
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with log.open('a') as f:f.write(line+now+'\n')
print(line+now)
