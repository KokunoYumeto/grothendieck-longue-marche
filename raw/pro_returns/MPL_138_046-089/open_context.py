from pathlib import Path
import zipfile
from workflow import ROOT, now, log

progress=(ROOT/'progress.log').read_text()
assert 'transcription frozen ' in progress
assert 'context opened ' not in progress
source=ROOT.parent/'upload'/'MPL_138_046-089_context.zip'
target=ROOT.parent/'context'
assert not target.exists()
log('context opened '+now())
target.mkdir()
with zipfile.ZipFile(source) as z:
    for item in z.infolist():
        path=Path(item.filename)
        if path.is_absolute() or '..' in path.parts:
            raise ValueError('Unsafe archive member')
    z.extractall(target)
print('Context extracted after the transcription freeze.')
