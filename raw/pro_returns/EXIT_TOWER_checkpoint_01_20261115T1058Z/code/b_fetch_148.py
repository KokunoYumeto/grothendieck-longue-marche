"""Retrieve the original Montpellier cote148 in HTTP ranges for scan verification."""
from urllib.request import urlopen,Request
from concurrent.futures import ThreadPoolExecutor,as_completed
from pathlib import Path
import time
url='https://grothendieck.umontpellier.fr/148.pdf'
length=35287128;step=524288
cache=Path('EXIT_TOWER_work/agents/B_148_ranges');cache.mkdir(exist_ok=True)
def fetch(start):
 end=min(start+step,length)-1;p=cache/str(start)
 if p.exists() and p.stat().st_size==end-start+1:return start,'cached'
 for attempt in range(3):
  try:
   with urlopen(Request(url,headers={'Range':f'bytes={start}-{end}'}),timeout=30) as r:
    b=r.read(end-start+1)
    if len(b)!=end-start+1:raise ValueError(len(b))
   p.write_bytes(b);return start,'downloaded'
  except Exception as e:
   if attempt==2:return start,repr(e)
with ThreadPoolExecutor(max_workers=8) as ex:
 for f in as_completed([ex.submit(fetch,s) for s in range(0,length,step)]):print(*f.result(),flush=True)
parts=[cache/str(s) for s in range(0,length,step)]
if all(p.exists() for p in parts):
 out=Path('EXIT_TOWER_work/agents/B_cote148.pdf')
 with out.open('wb') as w:
  for p in parts:w.write(p.read_bytes())
 print('COMPLETE',out.stat().st_size,flush=True)
