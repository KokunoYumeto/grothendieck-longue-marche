import json
import sys
from pathlib import Path
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
p = json.load(sys.stdin)
n = p['scan']
target = root / 'pages' / f'MPL_33_050-097_33_scan{n:03d}.tex'
text = target.read_text()
for old, new in p.get('replacements', []):
    if old not in text:
        raise ValueError(f'Unmatched replacement for scan {n}: {old!r}')
    text = text.replace(old, new, 1)
target.write_text(text)
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root / 'records' / 'audit_details.md').open('a') as f:
    f.write(f'\n## Scan {n:03d}\n\n')
    f.write(p.get('note', 'Re-read against the scan; retained the recorded readings and uncertainty marks.') + '\n')
with (root / 'progress.log').open('a') as f:
    f.write(f'scan {n:03d} audited {stamp}\n')
print(f'Audited {n:03d}; {len(p.get("replacements", []))} edits.')
