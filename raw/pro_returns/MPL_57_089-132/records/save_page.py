from pathlib import Path
from datetime import datetime, timezone
import csv,json,sys
ROOT=Path(__file__).resolve().parents[1]
def save(n,tex,elements,doubts=(),notations=(),abbreviations=(),observations=()):
 p=ROOT/'pages'/f'MPL_57_089-132_57_scan{n:03d}.tex'
 if p.exists(): raise RuntimeError(f'Page already exists: {p}')
 p.write_text(tex.rstrip()+'\n')
 with (ROOT/'MPL_57_089-132_inventory.csv').open('a',newline='') as f:
  w=csv.writer(f)
  for i,e in enumerate(elements,1):
   kind,position,first,*sheet=e
   w.writerow([57,n,sheet[0] if sheet else 'text',i,kind,position,first,'yes'])
 data={'scan':n,'doubts':doubts,'notations':notations,'abbreviations':abbreviations,'observations':observations}
 (ROOT/'records'/f'scan{n:03d}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 with (ROOT/'progress.log').open('a') as f:
  f.write(f'57 scan {n:03d} done '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
 print(f'Saved scan {n:03d}: {len(tex)} characters; {len(elements)} inventory elements.')
