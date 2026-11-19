from work import *
log=OUT/'progress.log'
assert 'transcription frozen ' not in log.read_text(), 'Already frozen; do not refreeze'
files=sorted((OUT/'pages').glob('*.tex'))+[OUT/'SP31_CW_156-3_transcription.tex']
assert len(files)==25
assert files[-1].read_bytes()==b''.join(p.read_bytes() for p in files[:-1])
assert sum(' audited ' in l for l in log.read_text().splitlines())==24
with log.open('a') as f:
 for p in files:f.write('SHA256 '+str(p.relative_to(OUT))+' '+hashlib.sha256(p.read_bytes()).hexdigest()+'\n')
 f.write('transcription frozen '+utc()+'\n')
print(log.read_text().splitlines()[-1])
