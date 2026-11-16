from pathlib import Path
import json, zipfile, datetime
p=Path(__file__).resolve().parents[1]
s=json.loads((p/'records/run_state.json').read_text())
now=datetime.datetime.now(datetime.timezone.utc)
last=datetime.datetime.strptime(s['last_checkpoint_utc'],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=datetime.timezone.utc)
if (now-last).total_seconds()<3600:
    print('Not yet due.'); raise SystemExit(0)
n=s['checkpoint_number']+1
dest=p.parent/f'MPL_36_002-052_checkpoint_{n:02d}.zip'
assert not dest.exists()
s.update(checkpoint_number=n,last_checkpoint_utc=now.strftime('%Y-%m-%d %H:%M:%S UTC'))
(p/'records/run_state.json').write_text(json.dumps(s,indent=2)+'\n')
with (p/'progress.log').open('a') as f:f.write(f'checkpoint {n:02d} prepared {s["last_checkpoint_utc"]}\n')
with zipfile.ZipFile(dest,'x',zipfile.ZIP_DEFLATED) as z:
    for f in sorted(p.rglob('*')):
        if f.is_file() and '__pycache__' not in f.parts:z.write(f,f.relative_to(p))
print(dest)
