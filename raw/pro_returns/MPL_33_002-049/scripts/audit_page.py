from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
def audit(scan,note='Compared the whole-page image with the saved transcription; retained marked uncertainties.'):
 log=ROOT/'progress.log'
 assert 'transcription frozen ' not in log.read_text()
 stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 with log.open('a') as f: f.write(f'scan {scan:03d} audited {stamp}\n')
 with (ROOT/'records'/'visual_audit.md').open('a') as f: f.write(f'\n## Scan {scan:03d} — {stamp}\n\n{note}\n')
 print(f'Audited {scan:03d}')
