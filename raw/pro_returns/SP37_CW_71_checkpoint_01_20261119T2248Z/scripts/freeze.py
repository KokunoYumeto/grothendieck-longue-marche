#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
root=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
files=sorted((root/'pages').glob('*.tex'))+[root/'SP37_CW_71_transcription.tex']
hashes={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
manifest=root/'frozen_hashes.json'
if len(sys.argv)>1 and sys.argv[1]=='verify':
    before=json.loads(manifest.read_text())
    if before!=hashes:raise SystemExit('FROZEN TRANSCRIPTION CHANGED')
    with (root/'progress.log').open('a') as f:f.write(f'frozen hashes unchanged {now}; verified {len(hashes)} files\n')
    print('Frozen hashes unchanged:',len(hashes),'files')
else:
    if manifest.exists():raise SystemExit('Refuse to replace existing freeze manifest')
    if len(files)!=14:raise SystemExit('Cannot freeze before all 13 scans are complete')
    manifest.write_text(json.dumps(hashes,indent=2)+'\n')
    with (root/'progress.log').open('a') as f:
        f.write(f'transcription frozen {now}\n')
        for p,h in hashes.items():f.write(f'SHA-256 {h}  {p}\n')
    print('Frozen:',len(hashes),'files')
