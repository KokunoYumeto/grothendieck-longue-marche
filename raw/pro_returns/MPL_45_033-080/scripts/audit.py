from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
def audit(n,remark='No textual change after image comparison.'):
 log=ROOT/'progress.log'
 prior=log.read_text()
 assert 'transcription frozen' not in prior
 assert f'scan {n:03d} audited ' not in prior
 with log.open('a') as f:
  f.write(f'scan {n:03d} audited '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
  f.write(f'audit {n:03d}: {remark}\n')
 print(f'scan {n:03d} audited')
