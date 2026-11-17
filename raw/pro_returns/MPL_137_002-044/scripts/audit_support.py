from pathlib import Path
from datetime import datetime,timezone
import json,csv
from record_page import ROOT,combine,now

def revise(scan,replacements=(),doubts=(),notation=(),elements=(),note='Compared the whole scan and visual details against the page transcription.'):
 p=ROOT/'pages'/f'MPL_137_002-044_137_scan{scan:03}.tex'
 s=p.read_text()
 for a,b in replacements:
  if a not in s:raise ValueError(f'{scan}: replacement source missing: {a!r}')
  s=s.replace(a,b)
 p.write_text(s)
 # Keep the initial saving script as an archival record. The audited page is authoritative.
 rpath=ROOT/'records'/f'{scan:03}.json';r=json.loads(rpath.read_text())
 r['doubts']+=list(doubts);r['notation']+=list(notation);r['elements']+=list(elements)
 r.setdefault('audit_notes',[]).append({'utc':now(),'note':note,'replacements':list(replacements)})
 rpath.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
 with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03} audited {now()}\n')
 rebuild_inventory();combine()
 print(f'Audited scan {scan:03}; {len(replacements)} text replacements.')

def rebuild_inventory():
 with (ROOT/'MPL_137_002-044_inventory.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
  for p in sorted((ROOT/'records').glob('*.json')):
   r=json.loads(p.read_text())
   for n,(k,pos,v) in enumerate(r['elements'],1):w.writerow([137,r['scan'],r['sheet_kind'],f'{r["scan"]:03}-{n:02}',k,pos,v,'yes'])
