"""Record immutable first readings before image-only readers are assigned."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
W=Path(__file__).resolve().parents[1]
order=(W/'page_order.txt').read_text().splitlines()
for page in order:
    p=W/'reports'/f'{page}.json'
    if not p.exists() or not json.loads(p.read_text()).get('adjudicated'):
        raise SystemExit('Every first reading must be committed: '+page)
manifest=W/'second/first_readings_manifest.json'
if manifest.exists(): raise SystemExit('First-reading manifest already exists; do not overwrite it.')
paths=[W/'second'/f'{page}_{suffix}.tsv' for page in order for suffix in ('boxes','first')]
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
data={'recorded_at':now,'files':{str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
manifest.write_text(json.dumps(data,indent=2)+'\n')
with (W/'progress.log').open('a') as f:
    f.write('independent image-only second reading started '+now+'; all 24 first readings committed; first/box hashes in second/first_readings_manifest.json\n')
print('Recorded',len(paths),'first-reading and box-list hashes.')
