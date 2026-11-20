"""Commit an already adjudicated page, update all cumulative records, then log completion."""
from pathlib import Path
import argparse,json,subprocess,sys
from datetime import datetime,timezone
O=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('key');a=p.parse_args()
d=json.loads((O/'decisions'/(a.key+'.json')).read_text())
page=next(x for x in json.loads((O/'page_order.json').read_text()) if f"{x['cote']}_scan{int(x['our_scan']):03d}"==a.key)
assert (O/'pages'/Path(page['codex_file']).name).exists()
assert all((O/'readers'/a.key/r/'reading.tex').exists() and (O/'readers'/a.key/r/'report.json').exists() for r in ['r1','r2','r3'])
assert d.get('adjudication_complete') is True
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
d['decided_utc']=now
(O/'decisions'/(a.key+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
subprocess.run([sys.executable,str(O/'scripts/build_records.py')],check=True)
with (O/'progress.log').open('a') as f:f.write(f"scan {int(page['our_scan']):03d} done {now} cote {page['cote']}\n")
s=json.loads((O/'state.json').read_text())
if a.key not in s['completed']:s['completed'].append(a.key)
(O/'state.json').write_text(json.dumps(s,indent=2)+'\n')
print('Committed',a.key,now)
