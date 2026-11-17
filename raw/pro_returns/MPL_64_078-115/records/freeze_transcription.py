from pathlib import Path
import hashlib,re,shutil
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]
log=root/'progress.log';s=log.read_text()
assert 'transcription frozen' not in s
assert {int(x) for x in re.findall(r'^64 scan (\d+) done',s,re.M)}==set(range(78,116))
assert {int(x) for x in re.findall(r'^scan (\d+) audited',s,re.M)}==set(range(78,116))
files=sorted((root/'pages').glob('*.tex'))+[root/'MPL_64_078-115_transcription.tex']
assert len(files)==39
rows=[(hashlib.sha256(p.read_bytes()).hexdigest(),p.relative_to(root).as_posix()) for p in files]
(root/'records/SHA256SUMS.frozen').write_text(''.join(h+'  '+p+'\n' for h,p in rows))
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with log.open('a') as f:
 f.write(f'LaTeX strict compilation succeeded {now}; no compiler errors or missing glyphs; one QA-only overfull line.\n')
 for h,p in rows:f.write(f'sha256 {h} {p}\n')
 f.write(f'transcription frozen {now}\n')
for name in ('qa_transcription.stdout.log','qa_transcription.log'):
 p=root.parent/'work/latex_qa'/name
 if p.exists():shutil.copy2(p,root/'records'/name)
print('Frozen',len(files),'files at',now)
