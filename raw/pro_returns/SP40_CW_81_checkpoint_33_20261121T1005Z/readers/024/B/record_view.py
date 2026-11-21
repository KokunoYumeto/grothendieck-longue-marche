import argparse
import datetime
import json
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('kind')
p.add_argument('path')
p.add_argument('status', choices=['success', 'failed_unseen'])
p.add_argument('purpose')
p.add_argument('--bbox', nargs=4, type=int)
p.add_argument('--rotation', type=float, default=0)
a = p.parse_args()
f = Path(__file__).with_name('view_audit.json')
d = json.loads(f.read_text())
d['events'].append({
    'sequence': len(d['events']) + 1,
    'logged_after_delivery_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'image_path': a.path,
    'kind': a.kind,
    'status': a.status,
    'purpose': a.purpose,
    'bbox': a.bbox,
    'rotation': a.rotation,
})
if a.status == 'success':
    d['viewing_counts'][a.kind] += 1
else:
    d['viewing_counts']['failed_unseen_deliveries'] += 1
f.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n')
