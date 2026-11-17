from pathlib import Path
from records.record_page import ROOT,utc
import json

def audit(scan,replacements=(),note='Compared all text and graphics with the scan; retained marked uncertainties.'):
 p=ROOT/'pages'/f'MPL_138_090-133_138_scan{scan:03d}.tex'
 s=p.read_text()
 for a,b in replacements:
  if a not in s:raise ValueError(f'Not found on scan{scan}: {a}')
  s=s.replace(a,b)
 p.write_text(s)
 stamp=utc()
 with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03d} audited {stamp}\n')
 with (ROOT/'records/visual_audit.md').open('a') as f:f.write(f'\n## Scan {scan} — {stamp}\n\n{note}\n')
 print(f'Audited {scan}: {len(replacements)} edits; {stamp}')
