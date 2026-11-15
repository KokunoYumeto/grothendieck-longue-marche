#!/usr/bin/env python3
import json,sys
from pathlib import Path
from datetime import datetime,timezone
root=Path(__file__).resolve().parent.parent
v=json.load(sys.stdin); n=int(v['scan']); now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
assert (root/'pages'/f'MPL_134-8_043-087_134-8_scan{n:03}.tex').is_file()
p=root/'records'/f'scan{n:03}_audit.json'; assert not p.exists(),str(p)
v['audited_utc']=now;p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
with (root/'progress.log').open('a') as f:f.write(f'scan {n:03} audited {now}\n')
with (root/'records'/'audit_report.md').open('a') as f:
 f.write(f'## Scan {n:03} — {now}\n\n'+v['observations']+'\n\n')
 if v.get('changes'):f.write('Corrections: '+v['changes']+'\n\n')
print(f'Scan {n:03}: second visual audit recorded.')
