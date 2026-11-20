"""Freeze the current notation table for a new page; no images are opened."""
from pathlib import Path
import argparse, json
R=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('scan',type=int);a=p.parse_args()
order=[2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18]
idx=order.index(a.scan)
for n in order[:idx]:
 if not (R/'decisions'/f'scan{n:03}.json').exists():raise SystemExit(f'Scan {n:03} must be committed first')
if (R/'decisions'/f'scan{a.scan:03}.json').exists():raise SystemExit('Page already committed')
source=(R/'notation.md').read_text()
if '# Remaining doubts' in source:raise SystemExit('Notation source includes trailing sections')
target=R.parent/'reader_inputs'/f'scan{a.scan:03}'/'notation_snapshot.md'
if target.exists():raise SystemExit('Refusing to overwrite an existing page snapshot')
target.write_text(source)
(R/'briefs'/f'scan{a.scan:03}_notation.md').write_text(source)
history=json.loads((R/'briefs/history.json').read_text())
print(json.dumps({'scan':a.scan,'snapshot':str(target),'brief':history[-1]['file']}))
