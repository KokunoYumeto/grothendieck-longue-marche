from pathlib import Path
from datetime import datetime, timezone
import json, sys

root = Path(__file__).resolve().parents[1]
scan = int(sys.argv[1])
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as out:
    out.write(f'scan {scan:03d} audited {stamp}\n')
with (root/'records/audit_details.jsonl').open('a') as out:
    out.write(json.dumps({'scan':scan,'utc':stamp,'note':sys.argv[2] if len(sys.argv)>2 else 'Visual second audit against the page and transcription.'},ensure_ascii=False)+'\n')
print(f'scan {scan:03d} audited {stamp}')
