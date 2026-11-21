"""Record a one-page blind assignment after all first readings are complete."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

WORK = Path(__file__).resolve().parents[1]
page, reader = sys.argv[1:3]
path = WORK/'run_state.json'
state = json.loads(path.read_text())
assert set(state['completed']) == set(state['order']) and len(state['order']) == 24
assert reader != state['assignments'][page], 'Second reader must be different'
assert page not in state.setdefault('blind_assignments', {})
assert not (WORK/'second'/(page+'_second.tsv')).exists()
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
manifest = WORK/'audit'/'first_readings_before_blind_sha256.json'
if not manifest.exists():
    snapshot = {}
    for p in state['order']:
        for suffix in ('boxes.tsv', 'first.tsv'):
            f = WORK/'second'/(p+'_'+suffix)
            snapshot[str(f.relative_to(WORK))] = hashlib.sha256(f.read_bytes()).hexdigest()
    manifest.write_text(json.dumps({'created_utc':stamp, 'sha256':snapshot},indent=2)+'\n')
state['blind_assignments'][page] = {'reader':reader, 'assigned_utc':stamp}
path.write_text(json.dumps(state, indent=2)+'\n')
with (WORK/'progress.log').open('a') as f:
    f.write(f'blind assignment {stamp}: {page} to {reader}; different from first reader; image and neutral boxes only\n')
print(page, reader, stamp)
