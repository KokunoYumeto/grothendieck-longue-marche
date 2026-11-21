"""Make the scheduled full-work checkpoint; never make an early checkpoint."""
from pathlib import Path
import datetime, json, subprocess, sys

root = Path(__file__).resolve().parents[1]
state_path = root / 'records/next_steps.json'
state = json.loads(state_path.read_text())
fmt = '%Y-%m-%d %H:%M:%S UTC'
now = datetime.datetime.now(datetime.timezone.utc)
due = datetime.datetime.strptime(state['checkpoint_due_utc'], fmt).replace(tzinfo=datetime.timezone.utc)
if now < due:
    raise SystemExit('Checkpoint not yet due: ' + state['checkpoint_due_utc'])
number = state.get('checkpoint_count', 0) + 1
name = f'SP85_C13_149_checkpoint_{number:02}.zip'
state['checkpoint_count'] = number
state['checkpoint_last_started_utc'] = now.strftime(fmt)
state['checkpoint_due_utc'] = (due + datetime.timedelta(minutes=45)).strftime(fmt)
state['checkpoint_pending_save'] = name
state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2))
with (root/'progress.log').open('a') as f:
    f.write(f'checkpoint {number:02} scheduled {due.strftime(fmt)}; packaged {now.strftime(fmt)}; all current deliverables and documentation, no inputs or earlier ZIPs\n')
subprocess.run([sys.executable, str(root/'scripts/build_records.py')], check=True)
subprocess.run([sys.executable, str(root/'scripts/package_work.py'), name], check=True)
