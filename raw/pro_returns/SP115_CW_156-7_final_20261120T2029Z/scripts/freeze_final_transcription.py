#!/usr/bin/env python3
"""Freeze the decided eight page files and assembled fragment exactly once."""
from pathlib import Path
import datetime,hashlib,json
R=Path(__file__).resolve().parents[1]
pages=sorted((R/'pages').glob('H156-01_156-7_scan*.tex'))
assert [int(p.stem[-3:]) for p in pages]==list(range(2,10))
combined=R/'SP115_CW_156-7_transcription.tex'
assert combined.read_text()=='\n\n'.join(p.read_text().rstrip() for p in pages)+'\n'
dest=R/'review/FINAL_TRANSCRIPTION_SHA256.json'
if dest.exists():raise SystemExit('Refusing to overwrite final transcription freeze')
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
records=[{'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in pages+[combined]]
dest.write_text(json.dumps({'frozen_utc':now,'files':records},ensure_ascii=False,indent=2)+'\n')
with (R/'progress.log').open('a') as f:
 f.write('transcription frozen '+now+'\n')
 for r in records:f.write('SHA256 '+r['path']+' '+r['sha256']+'\n')
print(json.dumps({'frozen_utc':now,'files':len(records)},ensure_ascii=False))
