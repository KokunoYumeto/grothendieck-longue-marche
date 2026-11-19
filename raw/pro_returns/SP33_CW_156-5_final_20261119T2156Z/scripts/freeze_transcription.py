from pathlib import Path
import hashlib,json
from datetime import datetime,timezone
OUT=Path(__file__).resolve().parents[1]
def utc():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
assert not (OUT/'records/frozen_hashes.json').exists(),'Already frozen'
records=[json.loads(p.read_text()) for p in sorted((OUT/'records').glob('scan[0-9][0-9][0-9].json'))]
assert [r['scan'] for r in records]==list(range(2,26)) and all(r.get('audited_utc') for r in records)
state=json.loads((OUT/'records/run_state.json').read_text());assert state['context_opened'] is False
paths=sorted((OUT/'pages').glob('*.tex'))+[OUT/'SP33_CW_156-5_transcription.tex']
assert len(paths)==25
manifest={str(p.relative_to(OUT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
(OUT/'records/frozen_hashes.json').write_text(json.dumps(manifest,indent=2)+'\n')
frozen=utc()
with (OUT/'progress.log').open('a') as f:
 for name,h in manifest.items():f.write(f'SHA-256 {h} {name}\n')
 f.write(f'transcription frozen {frozen}\n')
state['transcription_frozen_utc']=frozen
(OUT/'records/run_state.json').write_text(json.dumps(state,indent=2)+'\n')
print(f'Transcription frozen {frozen}; {len(manifest)} SHA-256 values recorded.')
