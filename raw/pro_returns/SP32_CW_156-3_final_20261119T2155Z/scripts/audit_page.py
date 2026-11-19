"""Record the root reader's completed second visual reading; no image recognition."""
from pathlib import Path
import json
from record_page import ROOT, utc, rebuild

def finish(scan, observations):
    when=utc()
    record={'scan':scan,'reader':'/root; ChatGPT GPT-6 Astra Pro; effort not exposed','time_utc':when,'observations':observations}
    (ROOT/'records'/f'audit{scan:03}.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    rebuild()
    with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03} audited {when}\n')
    print(f'Audited scan {scan:03}: {when}')
