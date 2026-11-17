from pathlib import Path
from datetime import datetime,timezone
import json,sys
root=Path(__file__).resolve().parents[1]
def audit(scan,note='Compared complete image and saved text; uncertain readings retained explicitly.'):
 now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 with (root/'progress.log').open('a') as f:f.write(f'scan {scan:03} audited {now}\n')
 with (root/'records/audit_log.jsonl').open('a') as f:f.write(json.dumps({'scan':scan,'utc':now,'note':note},ensure_ascii=False)+'\n')
if __name__=='__main__':audit(int(sys.argv[1]),sys.argv[2] if len(sys.argv)>2 else 'Compared complete image and saved text; uncertain readings retained explicitly.')
