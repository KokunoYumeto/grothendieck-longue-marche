from pathlib import Path
import json,sys,subprocess,datetime
OUT=Path(__file__).resolve().parents[1]; scan=int(sys.argv[1])
d=json.loads((OUT/'decisions'/f'scan{scan:03d}.json').read_text())
assert (OUT/'pages'/d['filename']).is_file()
assert all(i['transcribed']=='yes' for i in d['inventory'])
assert all(set(f['readers'])=={'R1','R2','R3'} for f in d['findings'])
assert d['hua_has']=='text' or all(not f.get('diff_h') for f in d['findings'])
subprocess.run([sys.executable,str(OUT/'scripts/build_records.py')],check=True)
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (OUT/'progress.log').open('a') as f:f.write(f'scan {scan:03d} done {now}\n')
print(now)
