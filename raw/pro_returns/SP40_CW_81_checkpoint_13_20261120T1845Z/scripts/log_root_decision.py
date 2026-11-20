"""Append a root-authored ink decision after its crop was actually delivered.

This records the supplied observation; it never opens or interprets an image.
Input is one JSON object on stdin: scan, section, crop, text, delivered_once.
Use an already logged crop only with previous_crop=true, without another view.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, sys

r = json.load(sys.stdin)
root = Path(__file__).resolve().parents[1]
n = int(r['scan'])
key = f'{n:03d}'
ap = root / f'checks/scan{key}_root_crop_audit.json'
dp = root / f'checks/scan{key}_main_decisions.md'
a = json.loads(ap.read_text())
path = r['crop']
assert (root / path).is_file()
existing = [x for x in a['viewed_once'] if x['path'] == path]
section = str(r['section']).zfill(2)
assert f'## {section} ' not in dp.read_text()
if existing:
    assert r.get('previous_crop') is True
    existing[0]['decision_sections'].append(section)
else:
    assert r.get('delivered_once') is True and not r.get('previous_crop')
    entry = dict(path=path, decision_sections=[section],
        sha256=hashlib.sha256((root/path).read_bytes()).hexdigest(), successful_display_count=1)
    for key in ('bbox', 'source_image', 'rotation', 'width'):
        if key in r:
            entry[key] = r[key]
    a['viewed_once'].append(entry)
a['total_distinct'] = len(a['viewed_once'])
with dp.open('a') as f:
    f.write(f'## {section} — {r.get("title", "Local ink decision")}\n\n')
    f.write(f'Viewed `{path}` once.\n\n' if not existing else f'Previously inspected crop `{path}`; no repeated view.\n\n')
    f.write(r['text'].rstrip() + '\n\n')
a['last_decision_recorded_utc'] = datetime.now(timezone.utc).isoformat()
ap.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(scan=n,section=section,total_distinct=a['total_distinct'])))
