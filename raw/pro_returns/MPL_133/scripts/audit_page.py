from pathlib import Path
import json,csv
from record_page import ROOT,REC,utc,refresh

def audit(scan,changes=(),notes='',doubts=(),elements=()):
 p=ROOT/'pages'/f'MPL_133_133_scan{scan:03}.tex'
 r=REC/f'scan{scan:03}.json';d=json.loads(r.read_text());s=p.read_text()
 counts=[]
 for old,new in changes:
  n=s.count(old)
  if not n:raise ValueError(f'scan {scan}: absent replacement {old!r}')
  s=s.replace(old,new);counts.append(n)
 p.write_text(s);d['tex']=s;d.setdefault('doubts',[]).extend(doubts);d['elements'].extend(elements)
 d['audit']={'utc':utc(),'notes':notes,'replacements':len(changes),'occurrences':sum(counts)}
 r.write_text(json.dumps(d,ensure_ascii=False,indent=2))
 with (ROOT/'MPL_133_inventory.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
  for x in sorted(REC.glob('scan*.json')):
   q=json.loads(x.read_text())
   for i,(typ,pos,first) in enumerate(q['elements'],1):w.writerow([133,q['scan'],q['sheet_kind'],f'{q["scan"]:03}-{i:02}',typ,pos,first,'yes'])
 with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03} audited {d["audit"]["utc"]}\n')
 with (REC/'audit.md').open('a') as f:f.write(f'\n## Scan {scan:03} — {d["audit"]["utc"]}\n\n{notes or "Re-read against the image; no change."}\n')
 refresh();print(f'Audited {scan:03}; {sum(counts)} replacements; {d["audit"]["utc"]}')
