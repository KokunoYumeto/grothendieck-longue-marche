#!/usr/bin/env python3
"""Record completion of the operator's independent visual audit, never infer it."""
import json,sys
from datetime import datetime,timezone
from pathlib import Path
root=Path(__file__).resolve().parents[1]
d=json.load(sys.stdin)
scan=int(d['scan'])
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
d['audited_utc']=stamp
(root/'records'/f'audit{scan:03}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (root/'progress.log').open('a',encoding='utf-8') as f:
 f.write(f'scan {scan:03} audited {stamp}\n')
print(f'Visual audit recorded: {scan:03}')
