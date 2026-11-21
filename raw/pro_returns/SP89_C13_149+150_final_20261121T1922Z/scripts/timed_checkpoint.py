"""Start an immutable checkpoint at its prescribed 45-minute boundary."""
from pathlib import Path
import datetime,json,time,sys,subprocess
W=Path(__file__).resolve().parents[1]
deadline=datetime.datetime.fromisoformat(sys.argv[1])
if deadline.tzinfo is None:raise ValueError('UTC timezone required')
seconds=(deadline-datetime.datetime.now(datetime.timezone.utc)).total_seconds()
if seconds>60:raise ValueError('Invoke within 60 seconds of the deadline; do not block longer')
if seconds>0:time.sleep(seconds)
started=datetime.datetime.now(datetime.timezone.utc)
reports=[json.loads(p.read_text()) for p in (W/'reports').glob('*/report.json')]
first=sum(bool(r.get('main_reviewed')) for r in reports)
audits=sum(bool(r.get('audited_utc')) for r in reports)
n=len(list((W.parent/'deliverables').glob('SP89_C13_149+150_checkpoint_*.zip')))+1
with (W/'progress.log').open('a') as f:
 f.write(f'checkpoint {n:02d} snapshot started {started.isoformat()}; scheduled {deadline.strftime("%Y-%m-%d %H:%M:%S UTC")}; {first} first readings finalized, {audits} independent audits finalized\n')
subprocess.run([sys.executable,str(W/'scripts/checkpoint.py')],check=True)
