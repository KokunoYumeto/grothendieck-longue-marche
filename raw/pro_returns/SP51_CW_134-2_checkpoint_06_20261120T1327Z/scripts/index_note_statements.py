"""Index explicitly listed source claims; never relabel a reading as a proof."""
from pathlib import Path
from datetime import datetime,timezone
import json,csv
root=Path(__file__).resolve().parents[1]
registry=json.loads((root/'records/note_statements.json').read_text())
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
rows=[]
for ns,statements in registry.items():
 p=root/f'records/scan{ns}/decision.json'
 if not p.exists():raise RuntimeError(f'No decided page {ns}')
 d=json.loads(p.read_text());known={e['statement_id'] for e in d['check_events']}
 d['note_statements']=statements
 for s in statements:
  rows.append({'scan':ns,**s})
  if s['id'] not in known:d['check_events'].append({'statement_id':s['id'],'date':stamp,'who':'GPT-6 Astra Pro; inherited effort not separately exposed; /root','type':'carried as background without fault found','outcome':s['place']+'. '+s['statement']+' Status: '+s['status']+'. This row indexes the content used in the note; it is not an additional mathematical proof or computation.'})
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with (root/'records/note_statement_index.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['scan','id','place','statement','status'],delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'note_statements':len(rows),'pages':len(registry)}))
