from pathlib import Path
from datetime import datetime,timezone
import csv
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_12_150-168+15_002-033'
def audit(cote,scan,replacements=(),additions=(),note='Visual comparison completed.'):
 p=ROOT/'pages'/f'{PREFIX}_{cote}_scan{scan:03}.tex'
 s=p.read_text()
 for old,new in replacements:
  if old not in s: raise ValueError(f'Missing replacement anchor {old!r}')
  s=s.replace(old,new)
 p.write_text(s)
 inv=ROOT/f'{PREFIX}_inventory.csv'
 with inv.open() as f: rows=list(csv.DictReader(f))
 fields=list(rows[0]); matching=[r for r in rows if int(r['cote'])==cote and int(r['scan'])==scan]
 for kind,pos,words in additions:
  i=len(matching)+1
  r=dict(zip(fields,[str(cote),str(scan),matching[0]['sheet_kind'],f'{cote}.{scan:03}.{i:02}',kind,pos,words,'yes']))
  rows.insert(rows.index(matching[-1])+1,r);matching.append(r)
 for r in rows:
  if r['kind'] in ('paragraph','theorem','page_number'):r['kind']='text'
 with inv.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
 now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 with (ROOT/'progress.log').open('a') as f:f.write(f'{cote} scan {scan:03} audited {now}\n')
 with (ROOT/'records/audit_notes.md').open('a') as f:f.write(f'## {cote}, scan {scan:03} — {now}\n\n{note}\n\n')
 print(f'{cote} scan {scan:03} audited; {len(replacements)} changes; {len(additions)} inventory additions')
