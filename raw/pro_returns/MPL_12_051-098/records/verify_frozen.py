from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys
base=Path(__file__).resolve().parents[1]
record=json.loads((base/'records'/'frozen_transcription_hashes.json').read_text())
bad=[]
for name,digest in record['sha256'].items():
    actual=hashlib.sha256((base/name).read_bytes()).hexdigest()
    if actual!=digest:bad.append(name)
result={'frozen_utc':record['frozen_utc'],'verified_files':len(record['sha256']),'unchanged':not bad,'mismatches':bad}
print(json.dumps(result,indent=2))
if bad:raise SystemExit(1)
if '--log' in sys.argv:
    with (base/'progress.log').open('a') as f:f.write('frozen SHA-256 hashes verified unchanged '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'; all '+str(len(record['sha256']))+' files\n')
