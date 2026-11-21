"""Prepare a full checkpoint only when the recorded 45-minute interval is due."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import json, sys
from assemble import build
from package import package
B=Path(__file__).resolve().parents[1];ROOT=B.parents[1]
number=int(sys.argv[1]);name=f'SP86_C13_149_checkpoint_{number:02d}.zip'
state=json.loads((B/'run_state.json').read_text())
fmt='%Y-%m-%d %H:%M:%S UTC'
now=datetime.now(timezone.utc)
due=datetime.strptime(state['next_checkpoint_due_utc'],fmt).replace(tzinfo=timezone.utc)
assert now>=due, f'Checkpoint is not due until {due}'
assert not (ROOT/'deliverables'/name).exists()
stamp=now.strftime(fmt)
state.update(checkpoint_prepared_utc=stamp,last_checkpoint_utc=stamp,next_checkpoint_due_utc=(now+timedelta(minutes=45)).strftime(fmt),phase='final metadata reconciliation; all 23 audits complete; transcription frozen')
for path in [B/'run_state.json',ROOT/'run_state.json']:path.write_text(json.dumps(state,indent=2)+'\n')
with (B/'progress.log').open('a') as f:f.write(f'checkpoint {number:02d} prepared {stamp}: complete current deliverables and documentation; preceding checkpoint ZIPs and source attachments excluded\n')
build()
result=package(name);result['prepared_utc']=stamp
(ROOT/'deliverables'/f'checkpoint_{number:02d}_package.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
