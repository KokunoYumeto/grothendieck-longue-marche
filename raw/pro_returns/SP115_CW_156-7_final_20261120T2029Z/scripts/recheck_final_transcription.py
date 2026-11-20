#!/usr/bin/env python3
"""Recheck final transcription hashes at the end of the run; no page mutation."""
from pathlib import Path
import datetime,hashlib,json
R=Path(__file__).resolve().parents[1]
frozen=json.loads((R/'review/FINAL_TRANSCRIPTION_SHA256.json').read_text())
rows=[]
for r in frozen['files']:
 actual=hashlib.sha256((R/r['path']).read_bytes()).hexdigest()
 rows.append({'path':r['path'],'expected':r['sha256'],'actual':actual,'unchanged':actual==r['sha256']})
assert len(rows)==9 and all(r['unchanged'] for r in rows)
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(R/'review/FINAL_TRANSCRIPTION_RECHECK.json').write_text(json.dumps({'checked_utc':now,'all_unchanged':True,'files':rows},ensure_ascii=False,indent=2)+'\n')
with (R/'progress.log').open('a') as f:f.write('final transcription hashes rechecked '+now+': all 8 page files and combined transcription unchanged from freeze; all 9 SHA-256 values match.\n')
print(now+': all 9 frozen transcription hashes unchanged')
