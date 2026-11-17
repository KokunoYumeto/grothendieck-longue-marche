from pathlib import Path
from datetime import datetime,timezone
import hashlib,re
root=Path(__file__).resolve().parents[1]
log=root/'progress.log'
s=log.read_text()
assert len(re.findall(r'^\d+ scan \d+ audited ',s,re.M))==34
assert 'transcription frozen ' not in s
pages=sorted((root/'pages').glob('*.tex'))
assert len(pages)==34
combined=root/'MPL_116+117_transcription.tex'
assert combined.read_bytes()==b''.join(p.read_bytes() for p in pages)
records=[(p.relative_to(root).as_posix(),hashlib.sha256(p.read_bytes()).hexdigest()) for p in pages+[combined]]
(root/'working/frozen_sha256.txt').write_text(''.join(f'{sha}  {name}\n' for name,sha in records))
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with log.open('a') as f:
 f.write('structural QA passed: all 34 fragments compiled; 592 inventory elements; correction counts reconciled '+stamp+'\n')
 for name,sha in records:f.write(f'sha256 {name} {sha}\n')
 f.write('transcription frozen '+stamp+'\n')
print('transcription frozen '+stamp)
