"""Record an actual image-against-text audit after the reader completes it."""
import sys,json
from pathlib import Path
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]
n=int(sys.argv[1]); note=sys.argv[2]
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f: f.write(f'scan {n:03d} audited {stamp}\n')
with (root/'records/audits.jsonl').open('a') as f:
    f.write(json.dumps({'scan':n,'utc':stamp,'note':note},ensure_ascii=False)+'\n')
print(f'Audited {n:03d}: {stamp}')
