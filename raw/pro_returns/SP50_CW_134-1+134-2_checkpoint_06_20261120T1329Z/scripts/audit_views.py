"""Audit reported view logs against crop logs; this is not a new image reading."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import json

O=Path(__file__).resolve().parents[1]
state=json.loads((O/'state.json').read_text())
pages={f"{p['cote']}_scan{int(p['our_scan']):03d}":p for p in json.loads((O/'page_order.json').read_text())}
errors=[];rows=[]
for key in state['completed']:
    stem=pages[key]['stem']
    required=[stem+'.jpg',stem+'_a.jpg',stem+'_b.jpg']
    for reader in ('r1','r2','r3'):
        report=json.loads((O/'readers'/key/reader/'report.json').read_text())
        paths=[str(v['path']) for v in report['view_log']]
        names=[Path(p).name for p in paths]
        counts=Counter(names)
        if names[:3]!=required:errors.append(f'{key}/{reader}: initial whole/a/b order differs')
        for name in required:
            if counts[name]!=1:errors.append(f'{key}/{reader}: {name} reported {counts[name]} times')
        logfile=O/'evidence'/key/reader/'crops.jsonl'
        crops=[json.loads(line) for line in logfile.read_text().splitlines()] if logfile.exists() else []
        for c in crops:
            if counts[c['output']]!=1:errors.append(f'{key}/{reader}: crop {c["output"]} reported {counts[c["output"]]} times')
        allowed=set(required)|{c['output'] for c in crops}
        for name in names:
            if name not in allowed:errors.append(f'{key}/{reader}: unaccounted view {name}')
        rows.append(dict(page=key,reader=reader,source_views=3,crops=len(crops),reported_views=len(paths)))
result=dict(utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),scope='Completed pages only; consistency of reported view and crop logs, not an independent execution-trace certification',pages=len(state['completed']),readers=len(rows),rows=rows,errors=errors)
(O/'view_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('utc','pages','readers','errors')}))
if errors:raise SystemExit(1)
